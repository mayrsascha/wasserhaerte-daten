# Wasserhärte nach Stadt: offener Datensatz

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22666436.svg)](https://doi.org/10.5281/zenodo.22666436)

Die Trinkwasserhärte von Städten in Deutschland, Österreich, der Schweiz und
Südtirol sowie in Frankreich und Großbritannien. Welche Städte enthalten sind,
zeigt `staedte.csv`; die Liste wächst. Erhoben 2026,
**ausschließlich aus Primärquellen**: dem Analyseblatt, der Qualitätsseite
oder dem akkreditierten Prüfbericht des jeweiligen Versorgers. Jede Zeile
nennt ihre Quelle mit URL und Stand.

Kein Wert stammt aus einem Wasserhärte-Verzeichnis oder einer anderen
Sekundärquelle. Wo ein Versorger keine einzelne Zahl veröffentlicht, steht
die Spanne über seine Wasserwerke. Ein erfundener Mittelwert steht hier
nicht.

**Warum das nötig war:** Die verbreiteten Übersichten sind alt. Die
Wikipedia-Liste der Trinkwasserversorgung deutscher Großstädte trägt Werte
von 2014 bis 2024; seitdem hat Braunschweig 2024 seine Versorgung
umgestellt, Münster enthärtet seit August 2026, Pforzheim mischt auf 9 °dH
herunter. Oldenburg, dort mit minimal 1,8 °dH als weichste Stadt
geführt, liegt laut seinem Netzbetreiber heute bei 6,6–12 °dH. Und für
Kufstein behaupten Wasserhärte-Verzeichnisse 12,9 °dH, während die
Stadtwerke selbst 7–9 veröffentlichen.

**[Prüfprotokoll](PRUEFPROTOKOLL.md):** Jede Zeile wird vierteljährlich gegen
ihre Primärquelle geprüft; das Datum der letzten vollständigen Prüfung steht
als `checked_on` am Anfang von `hardness.json`, die Handfälle stehen im Protokoll.

## Verantwortlich, Kontakt

Sascha Mayr. Fehler, neuere Werte oder fehlende Städte: bitte ein
[Issue](https://github.com/mayrsascha/wasserhaerte-daten/issues) mit Link auf die
Veröffentlichung des Versorgers. Issues bleiben offen, bis sie geklärt sind, und
die Klärung steht dann im Prüfprotokoll. Wer lieber schreibt: die Adresse steht im
[Impressum von aquascala.de](https://aquascala.de/impressum).

## Arbeitsweise

Was Werkzeuge tun und was ich tue, damit man den Datensatz einordnen kann:

- Jeder Wert stammt aus der Veröffentlichung des Versorgers, nie aus einer
  Zweitquelle. Welche Veröffentlichung als Quelle gilt, entscheide ich; die
  Regeln dazu stehen im Prüfprotokoll.
- Ein Skript (`tools_verify.py`, vierteljährlich als Action) vergleicht jeden
  gespeicherten Wert mit der Quelle im Netz. Eine Abweichung ist ein Hinweis,
  keine Änderung: die Quelle wird neu gelesen, und erst dann wird der Wert
  geändert, mit Datum und Begründung im Prüfprotokoll.
- Umrechnungen und Konsistenzprüfungen sind Code (`tools_consistency.py`),
  nicht Schätzung. Die CSV wird aus der JSON-Datei erzeugt, nie von Hand gepflegt.
- Beim Sammeln, Lesen von Analyseblättern und Formulieren helfen Sprachmodelle
  als Werkzeug. Jede Änderung am Datensatz und jeder Text geht vor der
  Veröffentlichung über meinen Tisch; die Verantwortung für das, was hier steht,
  liegt bei mir.
- Wasserhärte ist kein Gesundheitswert; die WHO nennt keinen Grenzwert. Wo der
  Datensatz Werte mit Gesundheitsbezug führt (Nitrat, PFAS, Blei), stehen nur
  die veröffentlichten Messwerte und der gesetzliche Grenzwert, keine Deutung.

## Zitieren

Mayr, Sascha (2026): Wasserhärte nach Stadt: offener Datensatz. Version 2026.09.
Zenodo. https://doi.org/10.5281/zenodo.22666437

Der Konzept-DOI https://doi.org/10.5281/zenodo.22666436 zeigt immer auf die neueste
Version; jede Quartalsprüfung bekommt eine eigene. Details in `CITATION.cff` und auf
[aquascala.de/lizenz](https://aquascala.de/lizenz).

## Dateien

- **`hardness.json`**: der vollständige Datensatz: mg/L CaCO₃ (die
  universelle Größe), Spannen je Versorgungszone, Quelle, Quell-URL,
  Messdatum, Anmerkungen, Koordinaten.
- **`staedte.csv`**: dasselbe flach als Tabelle, mit °dH umgerechnet.

## Die Extreme

Welche Städte das härteste und das weichste Wasser haben, steht in der jährlichen
Rangliste auf [aquascala.de/wasserhaerte/rangliste-2026](https://aquascala.de/wasserhaerte/rangliste-2026).

## Einheiten

Härte ist eine Größe auf vier Skalen: 1 °dH = 17,848 mg/L CaCO₃ = 1,7848 °f
= 0,1783 mmol/L. Der Datensatz führt mg/L CaCO₃; alles andere ist
Umrechnung. Die Härtebereiche (weich/mittel/hart) sind national verschieden
definiert; `band_international` folgt WHO/USGS (60/120/180 mg/L).

## Aufbereitete Ansicht

Jede Stadt mit Einordnung, Skalenvergleich und Karte:
**[aquascala.de/wasserhaerte](https://aquascala.de/wasserhaerte)**. Der Datensatz zum
Herunterladen, die Methodik und die Zitierweise: [aquascala.de/daten](https://aquascala.de/daten),
[aquascala.de/methodik](https://aquascala.de/methodik), [aquascala.de/lizenz](https://aquascala.de/lizenz).

## Lizenz

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de): frei
nutzbar mit Namensnennung: *„Daten: aquascala.de"* mit Link; die vollständige
Zitierweise steht auf [aquascala.de/lizenz](https://aquascala.de/lizenz).
Die Einzelwerte sind Fakten der jeweils genannten Versorger; die Lizenz
betrifft die Zusammenstellung.

---

## English summary

Drinking-water hardness for cities in Germany, Austria, Switzerland, South Tyrol,
France and the UK (`staedte.csv` lists which), surveyed in 2026 exclusively from
primary sources (each utility's own published analysis), with source URL and
date per row. `hardness.json` carries mg/L CaCO₃, per-zone ranges, notes and
coordinates; `staedte.csv` is the flat version with German degrees. Licensed
CC BY 4.0; attribute as "Data: aquascala.de" with a link. The rendered pages, the
download and the citation form live at [aquascala.de](https://aquascala.de/daten).
