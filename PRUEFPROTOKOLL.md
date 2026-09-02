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

Sechzehn Städte tragen weitere Werte aus derselben Analyse wie ihr
Härtewert. Übernommen wird ein Wert nur, wenn die Stadt eine
Einzelzonen-Zeile ist (bei Zonen-Städten variieren diese Werte je Werk wie
die Härte selbst), die Quelle ein Einzeldokument ist und der Wert innerhalb
der Plausibilitätsgrenzen liegt; die gesetzlichen Grenzwerte selbst werden
als Treffer ausgeschlossen. Verworfen wurden unter anderem alle
trinkwasser.ch-Zeilen, weil der Parser dort die Anzahl der Messungen statt
des Messwerts griff.
