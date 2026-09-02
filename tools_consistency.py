#!/usr/bin/env python3
"""Internal consistency check for hardness.json. No network.

Every row must hold together arithmetically: a calcium/magnesium pair must
reproduce the row's hardness, carbonate hardness cannot exceed total
hardness, the international band must match the figure, spans must contain
their anchor, and quality values must sit inside physical bounds.

KNOWN carries the documented exceptions: rows whose source's own published
figures disagree internally by 5-10 percent (rounded headlines, mixed
sampling dates in multi-network communes). They are accepted under the
tolerance stated in PRUEFPROTOKOLL.md and listed here so a regression from
5 to 15 percent still fails the run.
"""
import json
import re
import sys

DH, MMOL = 17.848, 100.0869

# key -> maximum accepted Ca/Mg deviation, with the documented reason.
KNOWN = {
    "AT/Salzburg": 0.07,      # headline is the rounded "rund 10 dH"
    "CH/Baden": 0.07,         # source's own table averages disagree
    "DE/Göttingen": 0.06,     # utility page rounding
    "FR/Cannes": 0.07,        # multi-network commune, mixed sample dates
    "FR/Chateauroux": 0.10,
    "FR/Le Havre": 0.09,
    "FR/Rouen": 0.07,
}

BANDS = [(60, "soft"), (120, "moderately hard"), (180, "hard"), (10**9, "very hard")]
NON_INTL_BANDS = ("weich", "mittel / hart", "varies by supply zone")


def band_of(mg):
    return next(b for lim, b in BANDS if mg < lim)


def main():
    d = json.load(open("hardness.json", encoding="utf-8"))
    problems = []
    for k, r in sorted(d["cities"].items()):
        mg, rng = r.get("mg_l"), r.get("range_mg_l")
        ref = mg or (rng and (rng[0] + rng[1]) / 2)
        ca, mgn = r.get("calcium_mg_l"), r.get("magnesium_mg_l")
        if (ca is None) != (mgn is None):
            problems.append(f"{k}: calcium without magnesium or vice versa")
        if ca and mgn and mg:
            calc = (ca / 40.078 + mgn / 24.305) * MMOL
            off = abs(calc - mg) / mg
            if off > KNOWN.get(k, 0.05):
                problems.append(f"{k}: Ca/Mg give {calc:.1f}, row says {mg} ({off*100:.1f}%)")
        kh = r.get("carbonate_mg_l")
        if kh and ref and kh > ref * 1.10:
            problems.append(f"{k}: carbonate {kh} exceeds total hardness {ref:.0f}")
        if mg is not None and r.get("band") and r["band"] not in NON_INTL_BANDS:
            if r["band"] != band_of(mg):
                problems.append(f"{k}: band '{r['band']}' but {mg} mg/L is '{band_of(mg)}'")
        if rng:
            if rng[0] > rng[1]:
                problems.append(f"{k}: range reversed {rng}")
            if mg is not None and not (rng[0] - 0.05 <= mg <= rng[1] + 0.05):
                problems.append(f"{k}: figure {mg} outside its own range {rng}")
        if (v := r.get("ph")) and not 6.0 <= v <= 9.5:
            problems.append(f"{k}: pH {v} out of bounds")
        if (v := r.get("nitrate_mg_l")) and v >= 50:
            problems.append(f"{k}: nitrate {v} at or above the legal limit")
        if (v := r.get("sodium_mg_l")) and v >= 200:
            problems.append(f"{k}: sodium {v} at or above the legal limit")
        if not r.get("source_url"):
            problems.append(f"{k}: no source_url")
    print(f"{len(d['cities'])} rows, {len(problems)} problems")
    for p in problems:
        print(" ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
