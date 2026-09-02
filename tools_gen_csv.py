#!/usr/bin/env python3
"""Regenerate staedte.csv from hardness.json. Run after any data change."""
import json, csv

d = json.load(open("hardness.json", encoding="utf-8"))
rows = []
for key, r in sorted(d["cities"].items()):
    cc, name = key.split("/", 1)
    mg = r.get("mg_l")
    rng = r.get("range_mg_l")
    if mg is None and not r.get("range_mg_l") and not r.get("band"): continue
    rows.append({
        "stadt": name, "land": cc,
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
        "stand": (r.get("measured_on") or "")[:4] or "2026",
        "quelle": r.get("source", ""), "quelle_url": r.get("source_url", ""),
    })
with open("staedte.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print(len(rows), "rows written")
