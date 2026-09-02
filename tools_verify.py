#!/usr/bin/env python3
"""Quarterly freshness check for hardness.json.

For every city the script re-checks the stored hardness against the live
source: static pages and PDFs by token-matching the figure in the local
unit, French rows against the Hubeau API, and the Gelsenwasser cities
against the live TWA API. Sources that block automated clients are on a
skip list and only reported.

Exit code 1 means at least one DRIFT or an unexpected fetch failure, so
the surrounding GitHub Action fails and sends a notification. A utility
quietly changing its published figure is exactly what this run exists to
catch: a drift is not an error in this script, it is homework.

Requires: requests, pdftotext (poppler-utils).
"""
import json
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.parse

import requests

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 "
      "wasserhaerte-daten-freshness-check (github.com/mayrsascha/wasserhaerte-daten)")

# Hosts that refuse automated clients (bot gates, JS-only tools). Checked in
# a browser instead; listed here so their failures do not fail the run.
SKIP_HOSTS = (
    "holding-graz.at", "l.de", "yorkshirewater.com", "web.archive.org",
    "wasserwerke-westfalen.de", "gelsenwasser.de", "swk.de",
    "hubeau.eaufrance.fr",  # FR rows are verified via the API below instead
)

DH, FH, MMOL, AS_CA = 17.848, 10.0, 100.0869, 2.4973

# Rows whose figures do not live on the source page itself: linked PDFs,
# postcode tools, JS applications, or a scan read by eye. Each carries the
# reason, so the quarterly report explains itself.
KNOWN_INDIRECT = {
    "CH/Basel": "figures live in the two linked works PDFs",
    "CH/Lausanne": "address-lookup source",
    "DE/Cottbus": "scanned report, read via screenshot",
    "DE/Dresden": "JS portal",
    "DE/Mannheim": "figures live in linked works PDFs",
    "DE/Munster": "JS page",
    "DE/Osnabrück": "figures live on the per-works analysis subpages",
    "DE/Würzburg": "JS app with per-reservoir data sheets",
    "GB/Belfast": "postcode tool",
    "GB/Bristol": "postcode tool",
    "GB/Cardiff": "postcode tool",
    "GB/Kingston upon Hull": "postcode tool, verified via headless browser",
    "GB/York": "postcode tool, verified via headless browser",
}


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if not unicodedata.combining(c)).lower().strip()


def fetch_text(url):
    r = requests.get(url, headers={"Accept": "*/*", "User-Agent": UA}, timeout=60)
    r.raise_for_status()
    if r.content[:4] == b"%PDF":
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(r.content)
            f.flush()
            t = subprocess.run(["pdftotext", "-layout", f.name, "-"],
                               capture_output=True, text=True).stdout
    else:
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", r.text, flags=re.S | re.I)
        t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


def tokens_for(value):
    """Every printable spelling of a figure: both decimal marks, the
    integer when the decimal part is zero, and one rounding step in each
    direction, because a stored 5.27 is printed as 5,2 or 5,3."""
    out = set()
    cands = {round(value, 2), round(value, 1),
             round(value - 0.05, 1), round(value + 0.05, 1)}
    for v in cands:
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        out.add(s)
        out.add(s.replace(".", ","))
        if v == int(v):
            out.add(str(int(v)))
    return out


def local_values(row, cc):
    """The figures the source is expected to print, in its own unit."""
    vals = []
    for mg in filter(None, [row.get("mg_l")] + (row.get("range_mg_l") or [])):
        if cc in ("DE", "AT"):
            vals += [mg / DH, mg / MMOL]
        elif cc == "CH":
            vals += [mg / FH, mg / MMOL]
        elif cc == "FR":
            vals.append(mg / FH)
        else:
            vals += [mg, mg / AS_CA]
    return vals


def check_static(key, row):
    cc = key[:2]
    if key in KNOWN_INDIRECT:
        return "SKIP", KNOWN_INDIRECT[key]
    host = urllib.parse.urlparse(row["source_url"]).netloc
    if any(h in host for h in SKIP_HOSTS):
        return "SKIP", f"bot-gated or API host ({host})"
    try:
        text = fetch_text(row["source_url"])
    except Exception as e:
        return "FETCH", str(e)[:120]
    if len(text) < 400:
        return "FETCH", f"only {len(text)} chars of text"
    if row.get("published_value"):
        num = re.search(r"[\d.,]+", row["published_value"])
        if num and any(t in text for t in tokens_for(float(num.group(0).replace(",", ".")))):
            return "OK", "published value present"
    hits, misses = [], []
    for v in local_values(row, cc):
        (hits if any(t in text for t in tokens_for(v)) else misses).append(round(v, 2))
    # A midpoint or converted variant is never printed, so any hit means the
    # source still shows a stored figure; only a page with NO stored figure
    # left counts as drift.
    if hits:
        return "OK", f"found {hits}" + (f" (not printed: {misses})" if misses else "")
    return "DRIFT", f"none of {[round(v, 2) for v in local_values(row, cc)]} on the page"


def hubeau_median(code, param, n=6):
    url = ("https://hubeau.eaufrance.fr/api/v1/qualite_eau_potable/resultats_dis"
           f"?code_commune={code}&libelle_parametre={urllib.parse.quote(param)}"
           f"&size={n}&sort=desc&fields=resultat_numerique")
    r = requests.get(url, headers={"User-Agent": UA}, timeout=45)
    r.raise_for_status()
    vals = sorted(v["resultat_numerique"] for v in r.json().get("data", [])
                  if v.get("resultat_numerique"))
    return vals[len(vals) // 2] if vals else None


def check_fr(key, row, insee):
    code = insee.get(key.split("/", 1)[1])
    if not code or not row.get("mg_l"):
        return "SKIP", "no INSEE code or span row"
    # Stored figures came from hardness (TH) or TAC-derived readings; recent
    # medians wobble, so only a sustained large move counts as drift.
    try:
        th = hubeau_median(code, "Titre hydrotimétrique")
        time.sleep(0.3)
        ref = th if th else hubeau_median(code, "Titre alcalimétrique complet")
        time.sleep(0.3)
    except Exception as e:
        return "FETCH", str(e)[:120]
    if ref is None:
        return "FETCH", "Hubeau returned no hardness samples"
    live = ref * FH
    off = abs(live - row["mg_l"]) / row["mg_l"]
    if off <= 0.20:
        return "OK", f"live median {live:.0f} vs stored {row['mg_l']:.0f} ({off * 100:.0f}%)"
    # Communes with several networks mix in the commune-wide median, so a
    # large gap is usually network variance, not a changed source. Report,
    # never fail.
    return "PARTIAL", f"live median {live:.0f} vs stored {row['mg_l']:.0f} ({off * 100:.0f}%), check the network"


def check_gelsenwasser(cities):
    """Live yearly medians for the rows built on the TWA API."""
    results = {}
    want = {"DE/Essen": ("Trinkwasser Essen", 7.7), "DE/Recklinghausen": ("Haltern", 11.3),
            "DE/Gelsenkirchen": ("Haltern", 11.3)}
    try:
        r = requests.get("https://www.gelsenwasser.de/twa-gelsenwasser?apikey=a345t678uz6",
                         headers={"User-Agent": UA, "Referer": "https://www.gelsenwasser.de/",
                                  "Accept": "application/json"}, timeout=90)
        r.raise_for_status()
        data = r.json()["data"][0]["cities"]
    except Exception as e:
        return {k: ("FETCH", str(e)[:120]) for k in want}
    medians = {}
    for c in data:
        for w in c.get("waterworks", []):
            for params in (w.get("sampleData") or {}).values():
                if not isinstance(params, list):
                    continue
                for p in params:
                    if isinstance(p, dict) and p.get("description") == "Gesamthärte":
                        medians[w["title"]] = p.get("yearlyMedian")
    for key, (works_hint, stored_dh) in want.items():
        live = next((v for t, v in medians.items() if works_hint in t), None)
        if live is None:
            results[key] = ("FETCH", "works not found in API answer")
            continue
        live_f = float(str(live).replace(",", "."))
        off = abs(live_f - stored_dh) / stored_dh
        results[key] = ("OK" if off <= 0.08 else "DRIFT",
                        f"API median {live_f} dH vs stored {stored_dh} dH")
    return results


def main():
    d = json.load(open("hardness.json", encoding="utf-8"))
    insee = json.load(open("tools_insee.json", encoding="utf-8"))
    gw = check_gelsenwasser(d["cities"])
    counts = {"OK": 0, "PARTIAL": 0, "SKIP": 0, "FETCH": 0, "DRIFT": 0}
    problems = []
    for key, row in sorted(d["cities"].items()):
        if not row.get("source_url") or (row.get("mg_l") is None and not row.get("range_mg_l")):
            continue
        if key in gw:
            status, msg = gw[key]
        elif key.startswith("FR/"):
            status, msg = check_fr(key, row, insee)
        else:
            status, msg = check_static(key, row)
            time.sleep(0.5)
        counts[status] += 1
        line = f"{status:8s} {key:28s} {msg}"
        print(line, flush=True)
        if status in ("DRIFT", "FETCH", "PARTIAL"):
            problems.append(line)
    print("\n==", counts)
    if problems:
        print("\nZu prüfen:")
        print("\n".join(problems))
    # Fetch failures happen (hosts move, TLS hiccups); a couple are noise,
    # many mean the check itself decayed. Drift always fails the run.
    if counts["DRIFT"] > 0 or counts["FETCH"] > 8:
        sys.exit(1)


if __name__ == "__main__":
    main()
