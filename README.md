# Wasserhärte deutscher Städte — offener Datensatz

Die Trinkwasserhärte von 69 deutschen Großstädten, dazu der komplette DACH-Raum
(alle 17 österreichischen und 17 Schweizer Städte der Sammlung) sowie
Frankreich und Großbritannien — 172 Städte insgesamt. Erhoben 2026,
**ausschließlich aus Primärquellen**: dem Analyseblatt, der Qualitätsseite
oder dem akkreditierten Prüfbericht des jeweiligen Versorgers. Jede Zeile
nennt ihre Quelle mit URL und Stand.

Kein Wert stammt aus einem Wasserhärte-Verzeichnis oder einer anderen
Sekundärquelle. Wo ein Versorger keine einzelne Zahl veröffentlicht, steht
die Spanne über seine Wasserwerke — ein erfundener Mittelwert steht hier
nicht.

**Warum das nötig war:** Die verbreiteten Übersichten sind alt. Die
Wikipedia-Liste der Trinkwasserversorgung deutscher Großstädte trägt Werte
von 2014 bis 2024; seitdem hat Braunschweig 2024 seine Versorgung
umgestellt, Münster enthärtet seit August 2026, Pforzheim mischt auf 9 °dH
herunter — Oldenburg, dort mit minimal 1,8 °dH als weichste Stadt
geführt, liegt laut seinem Netzbetreiber heute bei 6,6–12 °dH — und für
Kufstein behaupten Wasserhärte-Verzeichnisse 12,9 °dH, während die
Stadtwerke selbst 7–9 veröffentlichen.

## Dateien

- **`hardness.json`** — der vollständige Datensatz: mg/L CaCO₃ (die
  universelle Größe), Spannen je Versorgungszone, Quelle, Quell-URL,
  Messdatum, Anmerkungen, Koordinaten.
- **`staedte.csv`** — dasselbe flach als Tabelle, mit °dH umgerechnet.

## Die Extreme (Deutschland, 2026)

Das härteste Stadtwasser fließt in **Würzburg**: 25,4–42,7 °dH aus dem
Muschelkalk, je nach Hochbehälter. Das weichste in **Hildesheim**: 1,8 °dH
Harzer Talsperrenwasser.

## Einheiten

Härte ist eine Größe auf vier Skalen: 1 °dH = 17,848 mg/L CaCO₃ = 1,7848 °f
= 0,1783 mmol/L. Der Datensatz führt mg/L CaCO₃; alles andere ist
Umrechnung. Die Härtebereiche (weich/mittel/hart) sind national verschieden
definiert — `band_international` folgt WHO/USGS (60/120/180 mg/L).

## Aufbereitete Ansicht

Jede Stadt mit Einordnung, Skalenvergleich und Karte:
**[iswatersafetodrink.in/de/wasserhaerte](https://www.iswatersafetodrink.in/de/wasserhaerte)**

## Lizenz

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de) — frei
nutzbar mit Namensnennung: *„Daten: iswatersafetodrink.in"* mit Link.
Die Einzelwerte sind Fakten der jeweils genannten Versorger; die Lizenz
betrifft die Zusammenstellung.

---

## English summary

Drinking-water hardness for the 60 largest German cities plus all covered cities in
Austria and Switzerland (DACH complete) and in France and the UK — 172 in total, surveyed in 2026 exclusively from
primary sources (each utility's own published analysis), with source URL and
date per row. `hardness.json` carries mg/L CaCO₃, per-zone ranges, notes and
coordinates; `staedte.csv` is the flat version with German degrees. Licensed
CC BY 4.0 — attribute as "Data: iswatersafetodrink.in" with a link.

## Alle deutschen Städte mit Wert, weich nach hart

| Stadt | Gesamthärte | Quelle | Stand |
|---|---|---|---|
| Hildesheim | 1.8 °dH | EVI Energieversorgung Hildesheim | aktuell |
| Halle (Saale) | 4.2 °dH | Hallesche Wasser und Stadtwirtschaft (HWS) | aktuell |
| Chemnitz | 4.3 °dH | eins energie in sachsen | 2024 |
| Siegen | 4.5 °dH | Siegener Versorgungsbetriebe (SVB) | aktuell |
| Bonn | 5.7 °dH | Stadtwerke Bonn | 2025 |
| Bremen | 6.3 °dH | swb | 2026 |
| Essen | 6.6 °dH | Stadtwerke Essen | 2026 |
| Göttingen | 6.9 °dH | Stadtwerke Göttingen | aktuell |
| Trier | 4.7–9.3 °dH | SWT Stadtwerke Trier | 2025 |
| Aachen | 3.4–10.9 °dH | STAWAG | 2025 |
| Bochum | 7.5 °dH | Stadtwerke Bochum | 2026 |
| Freiburg im Breisgau | 2.3–12.7 °dH | badenova | 2026 |
| Pforzheim | 6.0–9.0 °dH | Stadtwerke Pforzheim (SWP) | aktuell |
| Dortmund | 7.7 °dH | DEW21 | 2026 |
| Wolfsburg | 7.9 °dH | LSW Energie, Wasser und Waerme | aktuell |
| Wuppertal | 8.2 °dH | Stadt Wuppertal (WAW) | 2025 |
| Braunschweig | 8.4 °dH | BS|ENERGY | 2026 |
| Erfurt | 3.1–14.0 °dH | SWE Stadtwerke Erfurt (ThüWa) | 2025 |
| Dresden | 5.6–12.3 °dH | SachsenEnergie | 2026 |
| Saarbrücken | 5.9–12.4 °dH | Stadtwerke Saarbrücken | aktuell |
| Oldenburg | 6.6–12.0 °dH | EWE NETZ | aktuell |
| Oberhausen | 5.7–14.1 °dH | RWW Rheinisch-Westfälische Wasserwerksgesellschaft | 2025 |
| Bremerhaven | 9.0–11.4 °dH | swb | 2026 |
| Bielefeld | 4.3–17.1 °dH | Stadtwerke Bielefeld | aktuell |
| Jena | 3.2–18.5 °dH | JenaWasser | aktuell |
| Stuttgart | 9.0–13.0 °dH | Netze BW Wasser | 2026 |
| Mönchengladbach | 8.4–14.0 °dH | NEW | aktuell |
| Gelsenkirchen | 11.3 °dH | Gelsenwasser | aktuell |
| Nuremberg | 11.6 °dH | N-ERGIE | 2026 |
| Hamburg | 5.1–18.3 °dH | HAMBURG WASSER | 2025 |
| Kassel | 8.4–15.0 °dH | KASSELWASSER | aktuell |
| Heidelberg | 2.7–21.1 °dH | Stadtwerke Heidelberg Netze | 2026 |
| Frankfurt am Main | 4.0–20.0 °dH | Mainova / Hessenwasser | aktuell |
| Hanover | 12.0 °dH | enercity | 2025 |
| Erlangen | 9.8–15.3 °dH | Erlanger Stadtwerke (ESTW) | 2026 |
| Reutlingen | 9.1–16.1 °dH | FairEnergie | aktuell |
| Krefeld | 13.0 °dH | SWK Stadtwerke Krefeld | aktuell |
| Heilbronn | 9.0–18.0 °dH | Stadtwerke Heilbronn | 2025 |
| Leipzig | 8.6–18.5 °dH | Leipziger Wasserwerke | aktuell |
| Augsburg | 13.7 °dH | Stadtwerke Augsburg | 2025 |
| Lübeck | 11.1–16.3 °dH | Stadtwerke Lübeck | 2026 |
| Berlin | 14.0 °dH | Berliner Wasserbetriebe | 2025 |
| Dusseldorf | 14.0 °dH | Stadtwerke Düsseldorf | 2026 |
| Munster | 14.0 °dH | Stadtwerke Münster | 2025 |
| Rostock | 14.2 °dH | Nordwasser | aktuell |
| Magdeburg | 14.3 °dH | SWM Magdeburg | 2025 |
| Duisburg | 14.5 °dH | Stadtwerke Duisburg | 2025 |
| Cottbus | 14.9 °dH | LWG Lausitzer Wasser (Prüfbericht AQS) | 2025-01-13 |
| Kiel | 14.9 °dH | Stadtwerke Kiel | 2025 |
| Potsdam | 10.0–21.0 °dH | Energie und Wasser Potsdam (EWP) | aktuell |
| Munich | 15.8 °dH | Stadtwerke München | 2026 |
| Ulm | 12.7–19.1 °dH | Stadtwerke Ulm/Neu-Ulm (SWU) | aktuell |
| Cologne | 15.6–18.1 °dH | RheinEnergie | 2025 |
| Regensburg | 16.9 °dH | REWAG | 2025 |
| Karlsruhe | 18.0 °dH | Stadtwerke Karlsruhe | 2026 |
| Mainz | 12.6–25.1 °dH | Mainzer Netze | aktuell |
| Mannheim | 20.1 °dH | MVV Energie | 2026 |
| Ingolstadt | 20.8 °dH | Ingolstaedter Kommunalbetriebe (INKB) | aktuell |
| Würzburg | 25.4–42.7 °dH | Würzburger Versorgungs- und Verkehrs-GmbH (WVV) | 2026 |
