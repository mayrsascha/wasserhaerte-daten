# Prüfprotokoll

Stand: 2. September 2026. Jede Zeile dieses Datensatzes wurde gegen ihre
Primärquelle geprüft; dieses Protokoll dokumentiert wie.

## Methode

1. **Konsistenzprüfung** über alle 173 Zeilen: Umrechnung mg/L CaCO₃ ↔ °dH ↔ °f,
   Einzelwert innerhalb der Zonenspanne, internationale Einstufung gegen die
   WHO/USGS-Grenzen (60/120/180 mg/L), Koordinaten innerhalb des Landes.
2. **URL-Prüfung** aller 110 eindeutigen Quell-URLs (Status, Weiterleitungen).
   Weiterleitungen wurden auf die Ziel-URL umgeschrieben.
3. **Wertprüfung**: Jede Quelle wurde maschinell geladen (HTML oder PDF) und
   auf den eingetragenen Wert in seiner Originaleinheit durchsucht, mit
   Komma- und Punktschreibweise, mmol-Äquivalent und Rundungsnachbarn.

## Ergebnis

- **103 Zeilen maschinell bestätigt**: Der Wert steht wörtlich auf der
  verlinkten Quelle.
- **48 französische Zeilen**: direkt aus der Hubeau-API des französischen
  Gesundheitsministeriums übernommen (Parameter „Titre hydrotimétrique",
  jüngste Messung je Commune); die API ist selbst die Primärquelle.
- **14 Zeilen per Browser-Sicherheitsschranke oder Archiv**: Graz und Leipzig
  liefern Inhalte nur an echte Browser aus (Bot-Schutz); die Werte wurden im
  Browser gegengeprüft. Leipzig wurde inzwischen direkt aus der
  Jahresdurchschnittsanalyse 2025 der KWL belegt, Graz über die archivierte
  Kopie der Versorgerseite (Internet Archive, Stand 17.06.2024), die den
  Bereich „15 °dH bis 17 °dH" wörtlich nennt. Damit ist jede Zeile des
  Datensatzes gegen ihre Primärquelle geprüft. Wiesbaden ist offline; die Werte stammen aus den
  archivierten Zonen-Analysen der WLW (Mai 2024), der Quelllink zeigt auf die
  Archivkopie.
- **8 dokumentierte Handfälle**:
  - *Cottbus, Lübeck, Münster*: Die Analyse liegt als Scan bzw. hinter einem
    Download-Portal; Werte aus dem Dokument selbst abgelesen (Cottbus zudem
    aus Calcium + Magnesium des akkreditierten Prüfberichts nachgerechnet;
    das ist die Definition der Gesamthärte).
  - *Lausanne, Belfast, Bristol, Cardiff*: Der Versorger veröffentlicht den
    Wert nur über eine Adress-/Postleitzahl-Abfrage; die genannte Zone steht
    in der jeweiligen Anmerkung.
  - *Portsmouth*: Das Blatt weist die Gesamthärte „as calcium" aus
    (115,4 mg/l Ca); die Umrechnung in CaCO₃ (×2,497) ist eine exakte
    Einheitenumrechnung derselben Größe.

## Grundsätze

- Kein Wert stammt aus einem Wasserhärte-Verzeichnis oder einer Ratgeberseite.
- Wo ein Versorger keine Einzelzahl nennt, steht die Spanne und nie ein
  erfundener Mittelwert (Ausnahme: als „Mittelwert der veröffentlichten
  Spanne" gekennzeichnete Zeilen, deren Spanne mitgeliefert wird).
- Elementares Calcium wird nicht in Härte umgerechnet (York), Gesamthärte in
  Calcium-Einheiten schon (Portsmouth). Der Unterschied steht in den Notizen.

## Calcium und Magnesium

Zwölf Städte tragen zusätzlich die Calcium- und Magnesiumwerte des
Versorgers. Ein Paar wird nur übernommen, wenn es die Gesamthärte der Zeile
rechnerisch reproduziert (Toleranz 10 Prozent), denn Calcium plus Magnesium
ist die Definition der Gesamthärte. Ein Paar, das nicht aufgeht, hieße, dass
eine der Zahlen falsch ist.

## Nitrat, Natrium, pH und Karbonathärte

83 Städte tragen weitere Werte aus derselben Analyse wie ihr
Härtewert. Übernommen wird ein Wert nur, wenn die Stadt eine
Einzelzonen-Zeile ist (bei Zonen-Städten variieren diese Werte je Werk wie
die Härte selbst), die Quelle ein Einzeldokument ist und der Wert innerhalb
der Plausibilitätsgrenzen liegt; die gesetzlichen Grenzwerte selbst werden
als Treffer ausgeschlossen. Verworfen wurden unter anderem alle
trinkwasser.ch-Zeilen, weil der Parser dort die Anzahl der Messungen statt
des Messwerts griff.

## Herkunft

39 Städte tragen die Herkunft des Wassers als strukturiertes Feld
(Talsperre, See, Quelle, Grundwasser, Uferfiltrat, Fernwasser), abgeleitet
aus den Versorgerangaben und von Hand geprüft. Der Stichwort-Durchgang
allein hätte Speicherbehälter zu Talsperren gemacht; solche Treffer wurden
korrigiert oder verworfen.

## Frankreich: alle Werte aus der Hubeau-API

Für die französischen Städte liefert Hubeau auch Calcium, Magnesium, Nitrat,
Natrium, pH und den Titre alcalimétrique complet (Karbonathärte). Ein
Calcium-Magnesium-Paar wird nur gespeichert, wenn es die Gesamthärte der
Zeile reproduziert; Nizza zum Beispiel scheiterte an dieser Prüfung und
trägt darum bewusst kein Paar. Die Karbonathärte ist kanonisch in mg/L
CaCO₃ abgelegt und wird je Land in dessen Einheit angezeigt.

## Vollständigkeits-Durchgang vom 2. September 2026

Ein letzter Durchgang hat für jede Stadt mit Einzelwert die Quelle neu
abgerufen und dort verlinkte Analyse-Dokumente verfolgt. Angenommen wurde
ein Dokument nur, wenn seine eigene Gesamthärte die Kennzahl der Zeile
reproduziert (Toleranz 12 Prozent). Neu aufgenommen:

- **München** (Trinkwasser-Analysewerte der SWM, Mittelwert-Spalte):
  Calcium 78,0, Magnesium 20,9, Natrium 5,9, Nitrat 6,5, pH 7,56.
- **Regensburg** (Chemische Analyse der REWAG, Oktober 2025): Calcium 96,
  Magnesium 15, Natrium 11, Nitrat 30, pH 7,4. Die Gesamthärte des
  Berichts (16,9 °dH) ist exakt die Kennzahl der Zeile.
- **Halle (Saale)** (Mittelwertanalyse 2025 der HWS): Calcium 24,22,
  Magnesium 3,28, Natrium 7,67, Nitrat 8,78, pH 8,41, Karbonathärte
  2,59 °dH (kanonisch 46,2 mg/L CaCO₃).
- **Karlsruhe** (Jahresmittelwerte Wasserwerk KA): Nitrat 10,3, Natrium
  7,4; Calcium und Magnesium stehen dort in mmol/l (2,46 und 0,86) und
  sind stöchiometrisch in mg/L umgerechnet (98,6 und 20,9).
- **Salzburg** (Wasserbeschaffenheit der Salzburg AG): Calcium 53,6,
  Magnesium 13,3 für das Hauptversorgungsgebiet.
- **Genf** (Bilan de l'eau der SIG): Calcium 43,9, Magnesium 5,9,
  Natrium 9,4 aus dem Seewasser-Netz, aus dem auch die Kennzahl der
  Zeile stammt.
- **Portsmouth** (Zonenblatt Farlington North): Nitrat 34,4, Natrium 9,5,
  pH 7,28 als Jahresmittel; Calcium ist dort nicht einzeln ausgewiesen,
  weil das Blatt die Härte als Calcium-Äquivalent angibt.
- **Frankreich**: ein zweiter Hubeau-Durchgang über die jeweils sechs
  jüngsten Proben schloss 26 Lücken (6x Ca/Mg, 16x Natrium, 3x pH,
  1x Nitrat).

Genauso wichtig ist, was NICHT aufgenommen wurde. Verworfen, weil die
Dokumente werks- oder zonenspezifisch sind und die Stadtkennzahl eine
Mischung ist: Bochum, Krefeld, Leoben, Graz, Augsburg (dessen
Einzelanalyse mit 12,8 °dH sogar außerhalb der veröffentlichten Spanne
13,5-13,9 liegt), Aberdeen, Edinburgh, Glasgow. Verworfene Artefakte
dieses Durchgangs: Methoden-Fußnoten als Messwerte (Regensburg "22"),
der Schweizer Nitrat-Grenzwert 40 als Zürcher Messwert, Stationscodes
in Laborberichten (Braunschweig, Wolfsburg). Cottbus' Prüfbericht ist
ein Scan ohne Textebene; seine übrigen Werte fehlen darum weiter.

## Nachtrag vom 2. September 2026: vier Städte mit Saschas Hilfe

- **Berlin** ist jetzt ehrlich modelliert. Die alte Zeile sagte "14,0 °dH";
  die Analysedaten der Berliner Wasserbetriebe für die zentrale PLZ 10115
  zeigen 14,0 bis 25,7 °dH, weil die Wasserwerke im Verbund ein wechselndes
  Mischwasser pumpen. Berlin ist darum eine Spannen-Stadt (249,9 bis 458,7
  mg/L) mit Verweis auf die PLZ-Abfrage des Versorgers. Das zuvor
  gespeicherte Natrium (37) wurde entfernt, die echte Spanne ist 21 bis 53.
- **Cottbus** wurde von der Einzelprobe (13. Januar 2025) auf die
  veröffentlichten Fünfjahresmittel 2021-2025 des Werks Sachsendorf
  umgestellt, per Screenshot aus dem Scan abgelesen: 16 °dH, Calcium 93,5,
  Magnesium 11,9, Natrium 14,0, Nitrat 1,5, pH 7,54. Ca+Mg reproduzieren
  die Härte auf 1,1 Prozent.
- **Basel** trägt jetzt die Jahresmittel 2025 der beiden Werke (Lange Erlen
  17,3 °f, Hardwasser 18,1 °f, beides Rheinuferfiltrat) statt der groben
  Spanne 16-19, dazu pH 7,7, der in beiden Werken identisch gemessen ist.
  Calcium, Magnesium, Nitrat und Natrium unterscheiden sich zwischen den
  Werken und bleiben darum bewusst leer.
- **Zürich** bleibt bewusst wertfrei, jetzt mit Beleg: der offene Datensatz
  der Stadt (data.stadt-zuerich.ch, dib_wvz_trinkwasserqualitaet) enthält
  nur Werksausgänge (Lengg, Moos, Hardhof), keine Netzproben, und die
  Werke unterscheiden sich in der Gesamthärte um bis zu 23 Prozent.
- **Düsseldorf** liefert ein Lehrstück: die Trinkwasseranalyse 2026 der
  Stadtwerke nennt Gesamthärte 15,0 °dH, aber ihre eigenen Werte Calcium
  65 und Magnesium 8,6 ergeben nur 11,1 °dH; zugleich sagt die
  Wasserhärte-Seite "etwa 14,0". Ein in sich widersprüchliches Blatt
  spendet keine Werte.

## Präzisions-Runde vom 2. September 2026

Ein Durchgang über die schwächsten Zeilen des Datensatzes, von unten:

- **Essen** stand auf "etwa 6,6 °dH" von der FAQ-Seite der Stadtwerke.
  Die Jahresanalyse 2025 des Verbundwasserwerks Essen sagt 7,7 °dH, und
  Calcium 42 plus Magnesium 7,9 reproduzieren genau diesen Wert; die
  Live-Analysedaten von Gelsenwasser (dieselbe Quelle, eigene API)
  bestätigen alle Werte unabhängig. Die Zeile trägt jetzt die Analyse:
  7,7 °dH, Ca, Mg, Karbonathärte 6,2 °dH, Natrium 41, Nitrat 9,2, pH 7,9.
- **Recklinghausen** trinkt komplett Halterner Wasser; die Jahresmediane
  des Werks aus den Gelsenwasser-Livedaten (Ca 73, Mg 4,8 reproduzieren
  die 11,3 °dH auf 0,2 Prozent) füllen die Zeile vollständig.
- **Gelsenkirchen** übernimmt dieselben Halterner Werte, weil die
  Kennzahl der Zeile das Halterner Wasser ist; die Ortsteile mit
  Essener Wasser stehen in der Notiz.
- **Dortmund** stand auf "etwa 7,7 °dH". Die vier Ruhrtal-Werke, die
  DEW21 beliefern, laufen als Jahresmediane 7,3 bis 8,2 °dH; die Zeile
  trägt jetzt diese Spanne um die 7,7. Einzelwerte bleiben leer, weil
  die Werke sich real unterscheiden.
- **Mödling** nennt auf der Gemeindeseite 19 °dH und Nitrat 15 mg/l;
  beides ist jetzt erfasst und die Zeile hat eine Notiz.
- **Zürich** hat jetzt eine Notiz, die erklärt, warum kein Einzelwert
  ehrlich wäre (Werksausgänge 141 bis 174 mg/l, wechselnde Mischung).
- **Koblenz** bleibt ohne Zahl: die Härtebekanntmachung 2023 der VWM
  nennt nur Härtebereiche je Zone. Die evm bietet eine individuelle
  Analyse auf Anfrage binnen zwei Arbeitstagen an.
- **Hull und York** bleiben ohne Zahl: Yorkshire Water veröffentlicht
  elementares Calcium ohne Magnesium, daraus lässt sich keine
  Gesamthärte errechnen, und das Postleitzahl-Tool ließ sich nicht
  maschinell bedienen.

Methodischer Neuzugang: Die Trinkwasseranalyse-Widgets von Gelsenwasser
und Wasserwerke Westfalen laden ihre Daten von einer offenen JSON-API
(twa-gelsenwasser), die pro Ort und Wasserwerk Jahresmediane aller
Parameter liefert. Das ist die sauberste deutsche Quelle nach Hubeau.
