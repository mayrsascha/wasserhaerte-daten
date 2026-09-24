#!/usr/bin/env python3
"""Regenerate staedte.csv from hardness.json. Run after any data change."""
import json, csv

# Die Schluessel in hardness.json tragen den englischen bzw. landessprachlichen
# Stadtnamen ("DE/Cologne", "IT/Bolzano"). Die CSV hat deutsche Spaltennamen und
# gehoert damit in deutsche Ortsnamen. exonyme_de.json haelt die Zuordnung;
# der Originalschluessel bleibt in der Spalte "stadt_key" erhalten, damit
# bestehende Auswertungen weiter zuordnen koennen.
EXONYME = json.load(open("exonyme_de.json", encoding="utf-8"))

d = json.load(open("hardness.json", encoding="utf-8"))


def kh_columns(r):
    """Karbonathärte als Spanne ueber alles, was die Zeile traegt: Einzelwert,
    Spanne, Zonen. Gedruckte und aus der Ionenbilanz berechnete Werte stehen in
    getrennten Spalten, damit niemand eine Rechnung fuer eine Messung haelt."""
    zs = r.get("zones") or []
    pr = [v for v in [r.get("carbonate_mg_l")] if v] + (r.get("carbonate_range_mg_l") or [])
    pr += [z["carbonate_mg_l"] for z in zs if z.get("carbonate_mg_l")]
    pr += [v for z in zs for v in (z.get("carbonate_range_mg_l") or [])]
    dv = list((r.get("carbonate_derived") or {}).get("range_mg_l") or [])
    dv += [z["carbonate_derived_mg_l"] for z in zs if z.get("carbonate_derived_mg_l")]
    f = lambda xs, fn: round(fn(xs) / 17.848, 1) if xs else ""
    return {"kh_min_dH": f(pr, min), "kh_max_dH": f(pr, max),
            "kh_berechnet_min_dH": f(dv, min), "kh_berechnet_max_dH": f(dv, max),
            "kh_stand": (r.get("carbonate_measured_on") or "")[:4] if (pr or dv) else "",
            "kh_quelle_url": (r.get("carbonate_source_url") or (r.get("carbonate_derived") or {}).get("source_url") or "") if (pr or dv) else ""}
rows = []
for key, r in sorted(d["cities"].items()):
    cc, name = key.split("/", 1)
    mg = r.get("mg_l")
    rng = r.get("range_mg_l")
    if mg is None and not r.get("range_mg_l") and not r.get("band"): continue
    rows.append({
        "stadt": EXONYME.get(name, name), "stadt_key": name, "land": cc,
        "mg_l_caco3": mg if mg is not None else "",
        "dH": round(mg / 17.848, 1) if mg is not None else "",
        "zone_min_dH": round(rng[0] / 17.848, 1) if rng else "",
        "zone_max_dH": round(rng[1] / 17.848, 1) if rng else "",
        "calcium_mg_l": r.get("calcium_mg_l", ""), "magnesium_mg_l": r.get("magnesium_mg_l", ""),
        "nitrat_mg_l": r.get("nitrate_mg_l", ""), "natrium_mg_l": r.get("sodium_mg_l", ""),
        "ph": r.get("ph", ""),
        "karbonathaerte_mg_l_caco3": r.get("carbonate_mg_l", ""),
        "herkunft": ";".join(r.get("origin", [])),
        "band_international": r.get("band", ""),
        # Kein Messjahr erfinden: fehlt es beim Versorger, bleibt die Zelle leer.
        "stand": (r.get("measured_on") or "")[:4],
        "quelle": r.get("source", ""), "quelle_url": r.get("source_url", ""),
        **kh_columns(r),
    })
with open("staedte.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print(len(rows), "rows written")
