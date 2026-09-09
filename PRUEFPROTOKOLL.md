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

## Stufe-1-Heilungen vom 2. September 2026

Drei der vier Städte ohne Zahl haben jetzt eine, eine Fehleinschätzung
ist korrigiert:

- **Leverkusen**: Die Wasseranalyse 2026 der EVL für das
  Dhünn-Talsperrenwasser nennt 0,94 mmol/l (5,2 °dH) mit vollem
  Wertesatz; Calcium 31,9 und Magnesium 3,5 reproduzieren die Härte
  exakt. Das Gebiet Rheindorf (Grundwasser, ebenfalls weich) steht in
  der Notiz.
- **Hull und York**: Die frühere Einschätzung, Yorkshire Water
  veröffentliche elementares Calcium ohne Härtebezug, war falsch. Das
  Postleitzahl-Tool beschriftet den Wert ausdrücklich als "Water
  hardness average" in mg/l Calcium, also Gesamthärte in
  Calcium-Einheiten nach britischer Konvention. Hull Central West 2024:
  148,4 mg/l Ca = 370,6 mg/l CaCO₃; York East 2024: 98,8 mg/l Ca =
  246,7 mg/l CaCO₃ (Faktor 100,0869/40,078 = 2,4973). Belegt per
  Screenshot der Abfrage vom 2. September 2026, maschinell ist das
  Tool nicht bedienbar.
- **Koblenz** bleibt ohne Zahl, jetzt abschließend geklärt: die
  Härtebekanntmachung 2023 enthält nur die gesetzlichen
  Härtebereichs-Definitionen und Zonen-Etiketten (mittel/hart), und
  das Trinkwasserinformationssystem Rheinland-Pfalz ist "zur Zeit
  überarbeitet und vorübergehend nicht erreichbar". Der einzige Weg zu
  Zahlen ist die individuelle Analyse, die die evm auf Anfrage binnen
  zwei Arbeitstagen erstellt.
- **Klagenfurt**: Die vier Untersuchungszeugnisse vom Juni 2026
  (Straschitz II, HB Spitalberg, Zwirnawald, Wasserschiene Krappfeld)
  messen 13,8 bis 18 °dH bei Unsicherheiten von ±3 bis ±4 — teils
  unter der veröffentlichten Spanne 17-20. Die Notiz sagt das jetzt;
  Einzelwerte bleiben leer, weil alle Parameter zwischen den vier
  Netzpunkten variieren.

## Vollständigkeits- und Frische-Runde vom 3. September 2026

**Der Frische-Check** (tools_verify.py, läuft quartalsweise als GitHub
Action "Frische-Check") prüft jede Zahl gegen ihre lebende Quelle:
statische Seiten und PDFs per Token-Abgleich in der Landeseinheit (auch
mmol/l und Härte-als-Calcium), die französischen Städte gegen die
Hubeau-API, die Gelsenwasser-Städte gegen die TWA-API. Schon der erste
Testlauf fand zwei echte Abweichungen:

- **Bochum** veröffentlicht nicht mehr 7,45 °dH stadtweit, sondern zwei
  Zonen: 7,3 (übriges Stadtgebiet) und 7,6 (Langendreer und Werne, direkt
  aus dem Wasserwerk Witten). Die Zeile trägt jetzt 7,3 mit Spanne und
  den kompletten Quartalsmitteln der größeren Zone (Calcium 41,
  Magnesium 6,9 reproduzieren die Härte auf 0,4 Prozent).
- **Aachen**: Das Analyseblatt 2024 der STAWAG nennt inzwischen 3,0-8,4
  und 6,0-14,0 °dH für die beiden Versorgungsbereiche; die alte Spanne
  3,4-10,9 war überholt.

**Hull und York sind jetzt maschinell verifiziert und komplett**: Das
Postleitzahl-Tool von Yorkshire Water lässt sich mit einem echten
Browser (Playwright) bedienen und liefert unter dem Härtewert eine
vollständige Stofftabelle. Der Beweis für die Calcium-Konvention steht
in den Zahlen selbst: York meldet "hardness average 98,8 mg/l calcium",
und Calcium 86,6 plus Magnesium 7,4 mal 1,649 ergibt exakt 98,8. Beide
Städte tragen jetzt Calcium, Magnesium, Nitrat, Natrium und pH; Hulls
Nitrat von 41,3 mg/l liegt bemerkenswert nah am Grenzwert 50.

**Weitere Vervollständigungen**: Braunschweig und Wolfsburg von Hand aus
den akkreditierten Prüfberichten gelesen (die Stationscodes hatten den
Parser zweimal getäuscht), beide validieren auf unter 0,5 Prozent.
Karlsruhe korrigiert: die zuvor übernommenen Werte stammten vom
Höhenstadtteile-Blatt; die Zeile trägt jetzt die Jahresmittelwerte 2025
"aus den Karlsruher Wasserwerken" (18,3 °dH, kompletter Satz, Ca/Mg aus
mmol/l umgerechnet). Herkunft von 40 auf 65 Städte erweitert, nur aus
expliziten Versorgerangaben. 27 undatierte Zeilen tragen als Stand das
Abrufjahr 2026 der lebenden Quellseite.

## Leverkusen-Rheindorf (3. September 2026)

Der zweite EVL-Analysebogen (Wasserwerk Rheindorf, versorgt Hitdorf,
Rheindorf, Bürrig, Küppersteg, Opladen und Alkenrath) macht Leverkusen
sauber zweizonig: Dhünn 0,94 mmol/l, Rheindorf 1,39 mmol/l. Bemerkenswert:
die Überschrift des Rheindorf-Bogens behauptet "1,54 Millimol, Härtebereich
mittel", aber die eigene Tabelle summiert die Erdalkalien zu 1,39 mmol/l,
und Calcium 41,3 plus Magnesium 8,6 ergeben exakt diese 1,39. Die
gemessene Tabelle gewinnt gegen die Prosa; damit sind beide Leverkusener
Zonen weich, wie es die EVL an anderer Stelle auch selbst sagt.

## Senior-Durchgang vom 3. September 2026

Ein letzter Konsistenz-Durchgang über alle 173 Zeilen mit verschärfter
Toleranz. Ergebnis:

- **15 französische Calcium/Magnesium-Paare nachgeschärft**: Ein tieferer
  Hubeau-Durchgang (zwölf statt sechs Proben je Parameter) fand Paare, die
  die Zeilenhärte besser reproduzieren; die mittlere Abweichung der
  betroffenen Städte fiel von 5-10 auf unter 3 Prozent, elf davon unter
  1,5 Prozent.
- **Wiener Neustadt verliert sein Calcium/Magnesium-Paar**: Das Blatt der
  Stadt ist zonengegliedert, und das Paar reproduzierte die Kennzahl nur
  auf 6,9 Prozent; im Einklang mit der früheren Entscheidung, aus diesem
  Blatt keine Einzelwerte zu übernehmen, ist das Paar entfernt.
- **Rueil-Malmaison verliert seine Karbonathärte**: 208,5 mg/L lag über
  der Gesamthärte von 185,5, was physikalisch nicht zusammenpasst; die
  beiden Hubeau-Proben stammten von verschiedenen Terminen.
- **Sieben dokumentierte Restabweichungen bleiben** (Salzburg, Baden,
  Göttingen, Cannes, Châteauroux, Le Havre, Rouen, je 5-8 Prozent): dort
  widersprechen sich die veröffentlichten Zahlen der Quelle selbst in
  dieser Größenordnung (gerundete Kennzahl, Mehrnetz-Gemeinde, gemischte
  Probentermine). Sie stehen als Ausnahmen mit Obergrenze in
  tools_consistency.py; wächst eine davon, schlägt der Lauf fehl.

Die Konsistenzprüfung (Ca+Mg-Arithmetik, Karbonat kleiner Gesamthärte,
Band-Grenzen, Spannen-Logik, Wertebereiche, Quellenpflicht) läuft seither
als eigener Schritt vor jedem Frische-Check.

## Tiefenprüfung vom 3. September 2026

Auf ausdrücklichen Wunsch ein weiterer, härterer Durchgang mit Prüfungen,
die es vorher nicht gab. Ergebnisse:

1. **Alle 346 gebauten Härteseiten Feld für Feld gegen den Datensatz**
   (Kopfzahl, Spannen, Calcium/Magnesium, Karbonathärte, alle vier
   Einheitenumrechnungen, Geräte-Stufe, Rang, Median, Städtezahl,
   Stand-Jahr; beide Sprachen, mit exakter kaufmännischer Rundung):
   null Abweichungen. Zwei scheinbare Treffer (Ulm, Freiburg) lösten
   sich als Messerschneiden-Rundung der Site-Konstante 100,09 gegen die
   exakte Molmasse 100,0869 auf; die Seite rechnet konsistent mit ihrer
   eigenen, hier dokumentierten Konstante.
2. **Jeder gespeicherte Zusatzwert wortwörtlich gegen seinen Quelltext**:
   141 Werte wörtlich im Quelldokument gefunden (inklusive
   mmol-Schreibweisen und Landeseinheiten), 33 über ihren Kanal
   verifiziert (Gelsenwasser-API, Yorkshire-Checker, Cottbus-Screenshot).
   Einziger Fund: Göttingens Magnesium stand als gerundete 7,4 im
   Datensatz, die Quelle druckt die Spanne 7,36-8,74; die Zeile trägt
   jetzt wortwörtlich 7,36.
3. **Frankreich-Stichprobe über die Hubeau-API**: 40 von 40 geprüften
   Werten aus acht Städten stehen exakt in den jüngsten Proben ihrer
   Gemeinde.
4. **CSV Zelle für Zelle gegen das JSON**: 173 Zeilen, null Differenzen.
5. **Alle 114 externen Links der Härteseiten**: 109 antworten mit 200.
   Die fünf übrigen sind erklärt: Graz und Leipzig sperren
   Nicht-Browser (im Browser erreichbar, seit je dokumentiert), Mainova
   sperrt curl, liefert aber im echten Browser, wo die Seite "zwischen
   4 und 20 °dH" sagt und damit die Frankfurter Spanne exakt bestätigt;
   der Wiesbadener Wayback-Link drosselt automatische Abrufe; der
   fünfte Treffer war ein preconnect-Tag, kein Leserlink.

Bekannte, bewusst belassene Kleinigkeit: Cherbourg und Lorient teilen
sich exakt 132,0 mg/L und tragen darum die willkürlich geordneten
Plätze 46 und 47 ihres Landes-Rankings.

## Abgleich mit aquascala.de, 8. September 2026

`hardness.json` ist jetzt die Datei, aus der aquascala.de baut; der Stand hier
und dort ist derselbe. Neu gegenüber dem Stand vom 2. September: die fünf
Südtiroler Städte (Bozen, Brixen, Bruneck, Leifers, Meran) und die 17 Werte
der Frische-Prüfung vom 6. September (überwiegend österreichische Städte,
gegen die Trinkwasserdatenbank geprüft; Details im Website-Repository, Commit
„Freshness pass"). `checked_on` am Dateianfang nennt das Datum dieser Prüfung.

## Frische-Check vom 8. September 2026

Vollständiger Lauf gegen alle Quellen: 139 Werte bestätigt, 8 teilweise (eine
Zahl der Spanne gefunden), 23 Sichtprüfungen laut Liste, 7 Quellen nicht
abrufbar, 0 Abweichungen. Drei Meldungen des ersten Laufs waren Grenzen des
Skripts (Bozen: Einheit; Erfurt: Tabelle im Script-Block; Wels: PDF ohne
Textebene) und sind behoben beziehungsweise als Sichtprüfung geführt.

Sichtprüfungen, Sascha Mayr, 8. September 2026:

- **AT/Wels**: Prüfbericht Agrolab vom 4. November 2025, Probenahme 8. Oktober
  2025, Entnahmestelle HB-Heitzing, Gesamthärte 10,5 °dH. Unverändert; die
  untere Grenze 9,6 °dH stammt aus den Netzmessstellen vom Juli 2026.
- **DE/Erfurt**: Adressabfrage der SWE, neun Adressen quer über die Stadt.
  Innenstadt und Süden (Anger, Domplatz, Bahnhofstraße, Juri-Gagarin-Ring,
  Schmidtstedter Straße, Nordhäuser Straße, Rudolstädter Straße) 12,8 °dH,
  Gispersleben (Alacher Straße) 12,5 °dH, Stotternheim (Erfurter Landstraße)
  3,2 °dH, jeweils als Messwert je Versorgungsgebiet. Die Spanne 3,2 bis
  26,4 °dH bleibt; 26,4 steht für die 62 Grundwasser-Adressen in derselben
  Tabelle der Seite.
- **IT (Landesumweltagentur)**: Tabelle liegt hinter einer klickbaren Grafik;
  die Werte wurden am 6. September aus genau dieser Tabelle übernommen
  (Proben Oktober bis Dezember 2025), keine erneute Lesung nötig.

`checked_on` steht damit auf 2026-09-08.


## 9. September 2026 — Nachprüfung Hildesheim, Leverkusen, Mannheim

Anlass: vor einer Presseansprache sollten die beiden Enden der deutschen
Rangliste noch einmal an der Quelle stehen.

- **DE/Hildesheim, 1,8 °dH: bestätigt.** Die EVI führt Hildesheim und die
  Ortschaften Einum, Achtum, Uppen, Bavenstedt, Sorsum, Neuhof und Marienrode
  im Härtebereich 1 „weich" mit einem Jahresmittel von 1,8 °dH und verlinkt
  dazu die Analyse des Wasserwerks Söse I. Dieselbe Analyse liegt beim
  Vorlieferanten Harzwasserwerke: Gesamthärte 1,8 °dH im Mittel, 1,7 bis 2,0
  °dH, aus den Monatsanalysen des Jahres 2025, veröffentlicht im Februar 2026
  (https://www.harzwasserwerke.de/wp-content/uploads/2026/02/WW-Soese-Reinwasser-I-2025.pdf).
  Eine neuere Jahresanalyse kann es noch nicht geben. Die anderswo kursierenden
  Zahlen 2,9 und 3,2 °dH gehören zum Wasserwerk Grane, dessen Analyse 2025 im
  Mittel 3,0 °dH mit einem Maximum von 3,2 °dH ausweist.
- **DE/Leverkusen: geändert, Einzelwert entfernt.** Die EVL schreibt auf ihrer
  Trinkwasserseite „Aktuell versorgen wir Wiesdorf und Manfort über das
  Currenta-Wasserwerk" und verlinkt eine Analyse mit Stand April 2026: 2,04
  mmol/l, 11,4 °dH, Härtebereich mittel. Die Stadtmitte lag damit außerhalb der
  bisherigen Spanne 5,3 bis 7,8 °dH. Die Zeile führt jetzt 5,3 bis 11,4 °dH
  ohne Einzelwert und fällt aus der Rangliste.
- **DE/Mannheim: Wert korrigiert.** Bisher stand hier der Mittelpunkt dreier
  Wasserwerke. Die amtliche Bekanntmachung der MVV nennt für 2024 eine
  Gesamthärte von 3,6 mmol/l beziehungsweise 20 °dH für das gesamte
  Liefergebiet. Wert auf 20,0 °dH, Jahr auf 2024, Quelle auf die Bekanntmachung.

Damit stehen 33 deutsche Städte mit Einzelwert in der Rangliste.

## 9. September 2026 — zehn fehlende Großstädte ergänzt

Abgleich gegen die Liste der deutschen Städte über 100.000 Einwohnern: elf
fehlten. Zehn sind jetzt aufgenommen, jeweils mit der Angabe des eigenen
Versorgers.

- **Spanne über Versorgungszonen**, weil der Versorger keine Stadtzahl nennt:
  Hagen 4,2 bis 7,2 °dH (Mark-E, beide Wässer und alle Mischungen im Netz),
  Hamm 7,2 bis 8,3 (EWV, drei benannte Zonen), Herne 7,3 bis 11,3 (Stadtwerke
  Herne, Witten weich und Haltern mittel), Paderborn 5,68 bis 17,1 (fünf
  Wasserwerke über drei Härtebereiche), Neuss 14,66 bis 15,36 (zwei Zonen,
  Straßenliste beim Versorger), Fürth 14,7 bis 16,7 (zwei Druckzonen, ohne
  Datum, Umstellung im Herbst 2026), Bottrop 8,0 bis 13,5 (RWW, die
  Straßenseite entscheidet zwischen weich und mittel), Salzgitter 3,3 bis 6,3
  (WEVG, drei Versorgungsbereiche).
- **Einzelwert**, weil der Versorger eine Zahl fürs ganze Gebiet nennt:
  Remscheid 5,1 °dH (EWR, Jahresmittel 2025) und Moers 13,2 °dH (Enni, Stand
  April 2026, zentrale Entkarbonisierung seit 2006). Beide selbst am
  Versorgerdokument nachgelesen.

**Bergisch Gladbach bleibt offen.** Die BELKAW nennt 12,8 °dH ohne
Analysentabelle und ohne Messdatum; auf der abgerufenen Seite war die Zahl
nicht auffindbar. Eine undatierte Einzelzahl kommt nicht in die Rangliste.

Deutschland steht damit bei 80 Städten, davon 35 mit Einzelwert. Neu in der
Rangliste der weichsten: Remscheid auf Platz 5.

## 9. September 2026 — Version 2026.09.09

Der Datensatz hat sich an diesem Tag geändert, ohne vollständig neu geprüft
worden zu sein. Deshalb trennen die Dateien jetzt zwei Daten: `checked_on`
bleibt der letzte vollständige Abgleich gegen alle Quellen, der 8. September,
und `updated_on` nennt den Stand des Inhalts. Die Versionsnummer folgt
`updated_on`, damit zwei Ausgaben im selben Monat unterscheidbar sind.

Geändert gegenüber 2026.09: Leverkusen ohne Einzelwert, Mannheim auf die
amtliche Zahl korrigiert, zehn Großstädte ergänzt, Fürth und Salzgitter mit
geschärfter Quelle und Notiz, Moers um Magnesium und Natrium erweitert.
Dreizehn Zeilen wurden dabei einzeln gegen ihre Quelle nachgeprüft, zwölf
davon maschinell bestätigt, Mannheim von Hand.

## 9. September 2026 — Bergisch Gladbach ergänzt, Koblenz bleibt ohne Zahl

- **DE/Bergisch Gladbach aufgenommen.** Die BELKAW nennt auf ihrer Seite
  2,28 mol/m³ beziehungsweise 12,8 °dH ohne Datum. Das Datum steht in der
  Trinkwasseranalyse Ausgabe 2026, „Jahresmittelwerte der Daten aus 2025“
  (https://www.belkaw.de/trinkwasseranalyse-belkaw-2026.pdfx). Die Datei
  trägt die Endung .pdfx und war deshalb bei der Suche nach PDF-Dateien
  nicht aufgefallen. Gesamthärte für das ganze Stadtgebiet, Härtebereich
  mittel, Karbonathärte 8,4 °dH. Gegenprobe: 69 mg/l Calcium und 14 mg/l
  Magnesium ergeben 12,89 °dH.
- **DE/Koblenz bleibt ohne Zahl.** Die amtliche Bekanntmachung der
  Vereinigte Wasserwerke Mittelrhein für Koblenz vom November 2023 nennt je
  Versorgungszone nur den Härtebereich, mittel oder hart, und als einzige
  Zahlen die Grenzen des Wasch- und Reinigungsmittelgesetzes selbst. Die
  Übersichtskarte vom November 2024 verfährt genauso. Eine Gesamthärte in
  °dH oder mmol/l veröffentlicht der Versorger für Koblenz nicht. Die Stadt
  bleibt deshalb in beiden Ranglisten außen vor.

Deutschland steht damit bei 81 Städten, 36 davon mit Einzelwert.
