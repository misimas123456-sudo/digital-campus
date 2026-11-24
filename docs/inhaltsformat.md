# Inhaltsformat v2.3 (verbindlich für alle Fächer)

Stand 24.11.2026. Maschinenlesbar: `content/schema.json` (JSON Schema 2020-12, Schema-Version 2.3).
Prüfen: `python tools/pruefen.py` (siehe unten). Das Feld `"format"` in den Dateien bleibt `2`.

## Hierarchie
Fach → Einheit (eine Semesterwoche bzw. ein Block) → Abschnitt (Theorie · Schnellfragen · Programmieren/Üben) → Lektion → Aufgaben

Der Abschnitt ist keine eigene Ebene in den Dateien: Er ergibt sich pro Lektion aus `abschnitt` bzw. `art`
(siehe [Aufbau einer Einheit](#aufbau-einer-einheit-drei-abschnitte)).

## Dateien pro Fach
```
content/<fach-id>/
  fach.json                    Pflicht – Metadaten + Liste aller Einheiten
  termine.json                 Pflicht – Termine des Fachs (darf leer sein)
  einheiten/<einheit-id>.json  eine Datei pro Einheit
  …                            fachspezifische Zusätze, in fach.json unter "zusaetze" eingetragen
                               (z. B. themen.json, quellen/, testvorbereitung/)
  bilder/                      optional – Bilder für den Baustein «bild» (v2.3)
  vorbereitung/<einheit-id>.json  optional – Vorbereitung auf die nächste Lektion (v2.3),
                               in fach.json: "zusaetze": { …, "vorbereitung": "vorbereitung/" }
```
Jede Datei ausser den Einheiten beginnt mit `"format": 2`.

---

## fach.json
```json
{
  "format": 2,
  "id": "elektrotechnik",
  "name": "Elektrotechnik mit Labor",
  "kurz": "ET+L",
  "farbe": "#ddb183",
  "schrift": "Barlow",
  "status": "in-arbeit",
  "ilias": "https://elearning.hslu.ch/ilias/goto.php/grp/7268289",
  "material": "material/elektrotechnik/",
  "eigene_unterlagen": "Documents/HSLU/Elektrotechnik mit Labor",
  "arten": ["verstaendnis", "rechnen", "aufgabe"],
  "einheiten": [
    { "id": "sw01-grundgroessen", "titel": "Grundgrössen & Gleichstromkreis", "woche": 1, "bereich": "theorie", "status": "bereit" },
    { "id": "sw04-labor1-messtechnik", "titel": "Messen mit Multimeter & Netzgerät", "woche": 4, "bereich": "labor", "status": "bereit", "labor": 1 },
    { "id": "sw10-labor4", "titel": "Labor 4", "woche": 10, "bereich": "labor", "status": "geplant" }
  ],
  "zusaetze": { "termine": "termine.json" }
}
```

| Feld | Pflicht | Bedeutung |
|---|---|---|
| `format` | ja | immer `2` |
| `id` | ja | Fach-ID, nie ändern |
| `name` | ja | Fachname **ohne** «– Digital Campus» (der Zusatz entsteht in der App) |
| `kurz` | ja | HSLU-Modulkürzel wie auf ILIAS: PYTHON, MATH1B, DT, ET+L, KONST_M, KONTT1, MECH_WSK1, GRUNDING |
| `farbe`, `schrift` | ja | aus dem Design System (`docs/design-farbschema.md`) |
| `status` | ja | `geplant` · `in-arbeit` · `fertig` |
| `einheiten` | ja | alle Einheiten in Lernreihenfolge, auch geplante (darf leer sein) |
| `zusaetze` | ja | Zusatzdateien, Pfad relativ zum Fachordner; `termine` ist Pflicht |
| `ilias` | nein | Link zum ILIAS-Kurs |
| `material` | nein | Kursmaterial von ILIAS: `material/<fach-id>/` (gehört dem ILIAS-Agent, siehe unten) |
| `eigene_unterlagen` | nein | eigene Notizen unter `C:\Users\alain\Documents\HSLU\…` – nur lesen (ersetzt `quellordner`) |
| `arten` | nein | welche Übungsarten das Fach nutzt |
| `wochen` | nein | Anzahl Semesterwochen (Standard 14) |
| `abschnitte` | nein | welche Abschnitte das Fach zeigt, in dieser Reihenfolge, z. B. `["theorie", "schnellfragen", "programmieren"]`. Standard: alle, die Lektionen haben |

**Eintrag in `einheiten`:**

| Feld | Pflicht | Bedeutung |
|---|---|---|
| `id` | ja | `swXX-thema` (z. B. `sw03-git`); für Testvorbereitung `tv-thema`, für Übungsserien `serie-n-thema` |
| `titel` | ja | kurzer Titel ohne «Block 3 ·» o. ä. |
| `bereich` | ja | `theorie` · `labor` · `uebung` · `projekt` · `testvorbereitung` |
| `status` | ja | `bereit` (Datei vorhanden) · `entwurf` · `geplant` · `folien-fehlen` |
| `woche` | nein | Semesterwoche 1–16 |
| `datei` | nein | nur wenn nicht `einheiten/<id>.json` (z. B. `testvorbereitung/tv-ar-vr.json`) |

Fachspezifische Zusatzfelder sind erlaubt (z. B. ET `block`/`labor`, Konstruktion `kapitel`/`zeitraum`/`themen`/`nr`).

---

## termine.json
```json
{
  "format": 2,
  "fach": "konstruktion-maschinentechnik",
  "stand": "2026-11-08",
  "quelle": "Modulprogramm V3.0 vom 6.11.2026, Prüfungsplan HS26",
  "termine": [
    { "id": "konst-sl", "titel": "Semesterleistung & Probe-MEP", "art": "pruefung", "von": "2026-12-01",
      "zeit": "Di 15:20–17:45", "ort": "F202", "bewertet": true, "hinweis": "Laut Modulprogramm V3.0 vom 6.11." },
    { "id": "pruef-vorb", "titel": "Prüfungsvorbereitung (unterrichtsfrei)", "art": "info", "von": "2027-01-11", "bis": "2027-01-17" }
  ]
}
```

| Feld | Pflicht | Bedeutung |
|---|---|---|
| `id` | ja | eindeutig, nie ändern (Häkchen «erledigt» hängen daran) |
| `titel` | ja | |
| `art` | ja | `unterricht` · `input` · `labor` · `termin` · `abgabe` · `pruefung` · `info` |
| `von` | ja | `YYYY-MM-DD` oder Zeitpunkt `YYYY-MM-DDTHH:MM` (mit Zeitzone erlaubt) |
| `bis` | nein | Ende; fehlt es, gilt `von` |
| `zeit` | nein | Freitext, z. B. «Mi 08:30–10:55» |
| `ort` | nein | Raum / Ort |
| `bewertet` | nein | `true` = zählt für die Note |
| `pflicht` | nein | `true` = obligatorisch |
| `hinweis` | nein | kurzer Zusatz |
| `zeit_offen` | nein | `true` = Uhrzeit folgt |
| `checkliste` | nein | mitzubringen / abzugeben (Liste) |

Weitere Felder oben: `hinweis` (Text), `ohne_datum` (Liste `{id, titel, hinweis}`).
Fachspezifische Planungsdaten gehören in einen eigenen Schlüssel, z. B. ET `zeitplan` (Klassen, Gruppen A/B, Hausaufgaben).

---

## Einheit (einheiten/<id>.json)
```json
{
  "id": "sw03-git",
  "titel": "Git Grundlagen",
  "beschreibung": "Repository, Commit, Branch",
  "woche": 3,
  "bereich": "theorie",
  "quelle": "GRUNDING-Slides-SW03",
  "lektionen": [
    {
      "id": "sw03-git-l1",
      "titel": "Was ist Git?",
      "art": "verstaendnis",
      "dauer_min": 4,
      "inhalt": [ { "typ": "text", "text": "**Git** speichert Versionen …" } ],
      "aufgaben": [ …siehe unten… ]
    }
  ]
}
```
- Einheit: Pflicht `id`, `titel`, `lektionen`; optional `untertitel`, `beschreibung`, `woche`, `bereich`, `quelle`.
- `quelle`: Text, Liste von Texten oder Liste `{ "text": …, "stellen": … }`.

### Lektion
| Feld | Pflicht | Bedeutung |
|---|---|---|
| `id` | ja | `<einheit>-l<n>`, nie ändern |
| `titel` | ja | |
| `art` | ja | Übungsart, siehe unten |
| `abschnitt` | nein | `theorie` · `schnellfragen` · `programmieren` · `ueben`; fehlt es, gilt die Zuordnung aus `art` (Tabelle unten) |
| `dauer_min` | nein | 3–5 (Notebook-Aufgaben auch länger, max. 15) |
| `quelle` | nein | |
| `inhalt` | nein* | Theorie-Bausteine (vor den Aufgaben, falls es welche gibt) |
| `aufgaben` | ja* | die Aufgaben |
| `schritte` | ja* | Alternative zu `aufgaben`: Theorie und Aufgaben abwechselnd (geführte Lektion, z. B. Digitaltechnik). Theorie-Schritt: `{ "typ": "theorie", "titel": …, "bloecke": [ … ] }` |
| `aufgabe`, `zellen`, `tests`, `loesung`, `hinweise`, `schwierigkeit`, `eingaben` | nein* | Notebook-Aufgabe, siehe [Abschnitt Programmieren](#3-programmieren-notebook) |

\* Nie `aufgaben` **und** `schritte` zusammen. Mindestens eines von `aufgaben`, `schritte`, `inhalt`, `aufgabe`, `zellen`.
Damit sind ab v2.2 auch reine Lese-Lektionen (nur `inhalt`) und Notebook-Lektionen (ohne `aufgaben`) gültig.

### Theorie-Bausteine (`inhalt`, `bloecke`)
`{ "typ": "text", "text": "…" }` · `titel` (text) · `liste` (punkte, optional titel) · `formel` (tex) ·
`code` (code, sprache, optional `ausgabe`, `ausfuehrbar`, `titel`) · `merke` (text) · `hinweis` (text, optional `titel`, `quelle`) · `tabelle` (kopf, zeilen) ·
`bild` (src, alt, optional `beschriftung`) · `grafik` (svg, optional `beschriftung`).
Fachspezifische Bausteine sind erlaubt, z. B. Digitaltechnik `kette`, `zeitdiagramm`, `zustandsdiagramm`, `interaktiv`.

**v2.3:**
- `bild`: `src` relativ zum Fachordner (Bilder in `content/<fach-id>/bilder/`, max. ~1100 px breit, JPEG ≈ q80), `alt` Pflicht für Barrierefreiheit,
  `beschriftung` mit Folienangabe, z. B. `"DevOps-Phasen und Tools (F. 39)"`.
- `grafik`: eigene, selbst gezeichnete Inline-SVG `{ "typ": "grafik", "svg": "<svg viewBox=\"0 0 640 300\">…</svg>", "beschriftung": "…" }`.
  Keine festen Farben: nur die Klassen `g-box` (Fläche, Rand), `g-accb` (Akzent-Rand), `g-dim`, `g-t` (Text), `g-m` (gedämpft),
  `g-acct` (Akzent-Text), `g-l` (Linie), `g-acc` (Akzent-Linie), `g-pf` (Pfeilspitze), `g-dot`, `g-ring`, `g-ring2`, `g-lane`, `g-lane-a`.
  Die App setzt sie auf `--dc-*`-Variablen. Breite 640, Schrift ≥ 12; auf dem Handy scrollt die Grafik seitlich (min. 540 px).
- `hinweis` mit `quelle`: **Ergänzung von ausserhalb des Kursmaterials** (z. B. offizieller Scrum Guide). Nur so markiert erlaubt,
  `quelle` dann Pflicht. Darstellung: eigener Kasten mit Rand in `--dc-campus`, Titel z. B. «Ergänzung aus dem Scrum Guide 2020».

`code`-Baustein: `ausgabe` = erwartete Ausgabe, wird unter dem Code angezeigt. `ausfuehrbar: true` = in der App
mit Pyodide ausführbar (nur `sprache` python), damit man das Beispiel abändern und neu laufen lassen kann.

### Übungsarten (Feld `art`)
| `art` | Zweck | Fächer | Abschnitt (Standard) |
|---|---|---|---|
| `verstaendnis` | Theorie lesen, kurze Verständnisfragen | alle | `theorie` |
| `code` | kleine Codeblöcke lesen | Python, GRUNDING | `schnellfragen` |
| `programmieren` | Code selbst schreiben | Python | `programmieren` |
| `rechnen` | Rechenaufgaben | Mathe, DT, ET, Mechanik, Konstruktion | `ueben` |
| `aufgabe` | längere Aufgaben, Transfer, Laborvorbereitung | Mathe, ET, Konstruktion, Kontextmodul, Mechanik | `ueben` |

`rechnung` und `anwendung` sind veraltet (bleiben gültig, Abschnitt `ueben`, nicht mehr neu verwenden).
Neue fachspezifische Arten (Vorschläge in `docs/fach-projekt-anweisungen`): erst in `schema.json` ergänzen, dann nutzen.

---

## Vorbereitung (vorbereitung/<einheit-id>.json) – v2.3
Optionaler Reiter in einer Einheit: was bis zur nächsten Lektion zu tun ist. Eine Datei pro Einheit, Name = Einheit-ID.
In `fach.json` einmal `"zusaetze": { "termine": "termine.json", "vorbereitung": "vorbereitung/" }` eintragen.
```json
{
  "format": 2,
  "fach": "industrielle-digitalisierung",
  "einheit": "sw10-agile-scrum",
  "titel": "Vorbereitung SW11 – DevOps",
  "woche": 11,
  "termin": "Do 26.11.2026 · F200 Horw · Grundlagen und Praktiken von DevOps",
  "quelle": "GRUNDING_HS2026_SW10.pdf, F. 2–4, 35–49",
  "aufgaben": [ { "id": "v1", "text": "Folien 35–49 durchblättern" } ],
  "inhalt": [ { "typ": "titel", "text": "Was kommt" }, { "typ": "liste", "punkte": ["…"] } ]
}
```
`aufgaben` = Checkliste (Fortschritt lokal unter `vorb/<einheit-id>/<id>`), `inhalt` = normale Theorie-Bausteine.
Der Teil des Titels vor « – » wird zum Reiternamen («Vorbereitung SW11»).

---

## Aufbau einer Einheit: drei Abschnitte

**Fach-Startseite:** alle Einheiten aus `fach.json` als Liste, sortiert nach `woche` (ohne `woche`: in der
Reihenfolge von `fach.json`, am Schluss). Pro Einheit Titel, Woche und Fortschritt.

**Einheit öffnen:** drei Bereiche (Tabs) mit den Lektionen dieser Einheit, in Dateireihenfolge:

| Abschnitt | Inhalt | kommt aus |
|---|---|---|
| **Theorie** (`theorie`) | Skriptblöcke zum Lesen: Text, Formeln, Code-Beispiele mit Ausgabe, Merksätze | `art: verstaendnis` |
| **Schnellfragen** (`schnellfragen`) | kurze Fragen, auch mit Code, sofortige Rückmeldung + Erklärung | `art: code` |
| **Programmieren** (`programmieren`) | Notebook mit Zellen, Python im Browser (Pyodide) | `art: programmieren` |
| **Üben** (`ueben`) | dritter Bereich der Nicht-Programmier-Fächer: Rechnen, längere Aufgaben | `art: rechnen`, `aufgabe` |

Regeln:
- Ohne `abschnitt` entscheidet `art` (Tabelle bei den Übungsarten). Mit `abschnitt` lässt sich das überschreiben,
  z. B. eine `verstaendnis`-Lektion, die nur aus Quizfragen besteht → `"abschnitt": "schnellfragen"`.
- Leere Abschnitte blendet die App aus. Mit `abschnitte` in `fach.json` legt ein Fach Auswahl und Reihenfolge fest.
- Hat eine Theorie-Lektion auch `aufgaben`, zeigt die App sie nach dem Lesen als kleine Kontrollfragen.
- Der Fortschritt bleibt an den Lektions- und Aufgaben-IDs (unverändert).

### 1. Theorie (Beispiel)
Mehrere Bausteine pro Lektion in `inhalt`; Aufgaben sind hier nicht nötig.
```json
{
  "id": "sw03-schleifen-l1",
  "titel": "Die for-Schleife",
  "art": "verstaendnis",
  "abschnitt": "theorie",
  "dauer_min": 4,
  "quelle": "SW03_Schleifen, S. 4–7",
  "inhalt": [
    {
      "typ": "titel",
      "text": "Wiederholen mit for"
    },
    {
      "typ": "text",
      "text": "Eine **for-Schleife** geht der Reihe nach durch alle Elemente einer Folge. `range(n)` liefert die Zahlen $0, 1, \\dots, n-1$."
    },
    {
      "typ": "code",
      "titel": "Beispiel",
      "sprache": "python",
      "ausfuehrbar": true,
      "code": "for i in range(3):\n    print(i * 2)",
      "ausgabe": "0\n2\n4"
    },
    {
      "typ": "merke",
      "text": "`range(n)` endet **vor** n."
    }
  ]
}
```

### 2. Schnellfragen (Beispiel)
Jede Schnellfrage hat: `frage`, optional `code` (Schnipsel, `sprache` Standard python), die Antwortform
(`optionen` + `richtig` **oder** `erwartete_ausgabe`) und `erklaerung` (wird nach dem Antworten immer gezeigt).
`code` ist ab v2.2 bei **allen** Aufgabentypen erlaubt (z. B. `multiple_choice` «Wie oft läuft diese Schleife?»).
```json
{
  "id": "sw03-schleifen-l2",
  "titel": "Schleifen lesen",
  "art": "code",
  "abschnitt": "schnellfragen",
  "dauer_min": 3,
  "aufgaben": [
    {
      "id": "sw03-schleifen-l2-a1",
      "typ": "code_ausgabe",
      "frage": "Was gibt dieser Code aus?",
      "code": "s = 0\nfor i in range(4):\n    s += i\nprint(s)",
      "optionen": [
        "6",
        "10",
        "4",
        "0 1 2 3"
      ],
      "richtig": 0,
      "erklaerung": "range(4) liefert 0, 1, 2, 3 – die Summe ist 6.",
      "quelle": "SW03_Schleifen, S. 6"
    },
    {
      "id": "sw03-schleifen-l2-a2",
      "typ": "code_ausgabe",
      "frage": "Tippe die Ausgabe ein.",
      "code": "for c in \"ab\":\n    print(c * 2)",
      "erwartete_ausgabe": "aa\nbb",
      "erklaerung": "Die Schleife läuft über jedes Zeichen; c * 2 verdoppelt es.",
      "quelle": "SW03_Schleifen, S. 8"
    },
    {
      "id": "sw03-schleifen-l2-a3",
      "typ": "code_fehler",
      "frage": "Wo ist der Fehler?",
      "code": "for i in range(3)\n    print(i)",
      "fehlerzeile": 1,
      "korrektur": "for i in range(3):",
      "erklaerung": "Nach dem Schleifenkopf braucht es einen Doppelpunkt.",
      "quelle": "SW03_Schleifen, S. 5"
    },
    {
      "id": "sw03-schleifen-l2-a4",
      "typ": "multiple_choice",
      "frage": "Wie oft läuft diese Schleife?",
      "code": "for i in range(2, 8, 2):\n    pass",
      "optionen": [
        "3-mal",
        "4-mal",
        "6-mal"
      ],
      "richtig": 0,
      "erklaerung": "range(2, 8, 2) liefert 2, 4, 6.",
      "quelle": "SW03_Schleifen, S. 7"
    }
  ]
}
```
- `code_ausgabe` mit `optionen`: `richtig` = Index. Ohne `optionen`: `erwartete_ausgabe` wird mit der Eingabe
  verglichen (Leerzeichen am Zeilenende und Leerzeilen am Schluss ignoriert). Ältere Form `richtig` als Text bleibt gültig.
- `code_fehler`: `fehlerzeile` ab 1, `korrektur` = richtige Zeile.
- `frage` fehlt bei älteren `code_ausgabe`-Aufgaben; die App zeigt dann «Was gibt dieser Code aus?».

### 3. Programmieren (Notebook)
Eine Lektion = eine Notebook-Aufgabe. Felder direkt in der Lektion:

| Feld | Pflicht | Bedeutung |
|---|---|---|
| `aufgabe` | ja* | Aufgabenstellung (Markdown, Formeln mit `$…$`) |
| `zellen` | nein | Startzellen `{ "typ": "markdown" \| "code", "inhalt": "…", "gesperrt": true? }`. Ohne `zellen`: eine leere Code-Zelle |
| `tests` | nein | Python-Code mit `assert …, "Meldung"`; läuft nach der Lösung (siehe unten) |
| `loesung` | nein | Musterlösung (Python), erst auf Knopfdruck sichtbar |
| `hinweise` | nein | Liste von Tipps, einzeln aufdeckbar |
| `schwierigkeit` | nein | 1 (leicht) – 3 (schwer) |
| `eingaben` | nein | Liste von Texten, die `input()` der Reihe nach zurückgibt |

\* `aufgabe` oder `zellen` muss vorhanden sein. `gesperrt: true` = Zelle nicht bearbeitbar (vorgegebener Code).

```json
{
  "id": "sw03-schleifen-l3",
  "titel": "Notendurchschnitt",
  "art": "programmieren",
  "abschnitt": "programmieren",
  "dauer_min": 15,
  "schwierigkeit": 2,
  "quelle": "SW03_Uebung, Aufgabe 2",
  "aufgabe": "Lies zuerst die **Anzahl Noten** `n` ein, dann `n` Noten (je eine Zeile, Dezimalzahl).\n\n1. Schreibe eine Funktion `durchschnitt(noten)`, die den Mittelwert einer Liste zurückgibt.\n2. Gib am Schluss `Schnitt: x.xx` aus (2 Nachkommastellen).",
  "zellen": [
    {
      "typ": "markdown",
      "inhalt": "### Teil 1 – Funktion\nSchreibe `durchschnitt(noten)`."
    },
    {
      "typ": "code",
      "inhalt": "def durchschnitt(noten):\n    # dein Code\n    pass"
    },
    {
      "typ": "markdown",
      "inhalt": "### Teil 2 – Eingabe und Ausgabe"
    },
    {
      "typ": "code",
      "inhalt": "n = int(input(\"Anzahl Noten: \"))\nnoten = []\n# dein Code\n"
    }
  ],
  "eingaben": [
    "3",
    "4.5",
    "5",
    "5.5"
  ],
  "tests": "assert 'durchschnitt' in dir(), 'Die Funktion durchschnitt fehlt.'\nassert durchschnitt([4, 6]) == 5, 'durchschnitt([4, 6]) sollte 5 ergeben.'\nassert abs(durchschnitt([4.5, 5, 5.5]) - 5) < 1e-9, 'Mittelwert von 4.5, 5, 5.5 ist 5.'\nassert noten == [4.5, 5.0, 5.5], f'Die Liste noten sollte [4.5, 5.0, 5.5] sein, ist aber {noten}.'\nassert 'Schnitt: 5.00' in _ausgabe, 'Die Ausgabe «Schnitt: 5.00» fehlt.'",
  "hinweise": [
    "Mittelwert = Summe / Anzahl – dafür gibt es `sum()` und `len()`.",
    "Die Noten liest du in einer `for`-Schleife mit `range(n)` ein und hängst sie mit `append` an.",
    "Formatieren: `print(f\"Schnitt: {wert:.2f}\")`."
  ],
  "loesung": "def durchschnitt(noten):\n    return sum(noten) / len(noten)\n\nn = int(input(\"Anzahl Noten: \"))\nnoten = []\nfor _ in range(n):\n    noten.append(float(input()))\nprint(f\"Schnitt: {durchschnitt(noten):.2f}\")"
}
```

**So führt die App das Notebook aus** (Pyodide von `cdn.jsdelivr.net/pyodide/`, im Browser, offline nach dem ersten Laden):
- Shift+Enter führt die Zelle aus und springt zur nächsten; alle Zellen teilen einen Namensraum (wie Jupyter).
  Die Ausgabe (`print`, Fehlermeldungen, Wert der letzten Zeile) steht unter der Zelle.
- `input()` liefert der Reihe nach die Werte aus `eingaben`; sind sie aufgebraucht oder fehlen sie, fragt die App mit einem Eingabefeld.
- **Prüfen:** Namensraum neu, alle Code-Zellen von oben nach unten ausführen (mit frischen `eingaben`), die gesamte
  Ausgabe steht danach als Text in `_ausgabe`. Dann läuft `tests` im selben Namensraum.
  Kein Fehler = bestanden. `AssertionError` → die Meldung des `assert` wird angezeigt; anderer Fehler → Fehlermeldung mit Zeile.
- Darum jedes `assert` mit verständlicher Meldung schreiben (was erwartet war, was herauskam).
- Die Musterlösung muss die Tests bestehen, die Startzellen nicht.

Bestehende Lektionen mit `programmieraufgabe`-Aufgaben bleiben gültig. Die App zeigt sie ebenfalls im Abschnitt
Programmieren, als Notebook mit einer Code-Zelle (`startcode`), den bisherigen `tests` (Aufruf/erwartet) und `musterloesung`.
Neue Programmieraufgaben bitte im Notebook-Format schreiben.

---

## Aufgabentypen
Jede Aufgabe hat: `id` (eindeutig, nie ändern), `typ`, `erklaerung` (bei falscher Antwort), `quelle` (Folie/Seite).

**multiple_choice** – `richtig` = Index (ab 0)
```json
{ "id": "sw03-git-l1-a1", "typ": "multiple_choice", "frage": "Welcher Befehl erstellt einen Commit?",
  "optionen": ["git add", "git commit", "git push", "git init"], "richtig": 1, "erklaerung": "…", "quelle": "…" }
```
**wahr_falsch**
```json
{ "id": "…", "typ": "wahr_falsch", "aussage": "git push lädt Commits auf den Server.", "richtig": true, "erklaerung": "…" }
```
**lueckentext** – Lücken als `___`, Antworten der Reihe nach, Alternativen erlaubt
```json
{ "id": "…", "typ": "lueckentext", "text": "Mit ___ wechselt man den Branch.", "antworten": [["git switch", "git checkout"]] }
```
**zuordnen** – `{ "frage": …, "paare": [["ls", "Inhalt auflisten"], …] }`
**reihenfolge** – `{ "frage": …, "elemente": ["git add", "git commit", "git push"] }`
**rechnung** – numerische Antwort mit Toleranz
```json
{ "id": "…", "typ": "rechnung", "frage": "R = 220 Ω, I = 0.5 A. U = ?", "loesung": 110, "toleranz": 0.01,
  "einheit": "V", "loesungsweg": ["$U = R \\cdot I$", "$U = 110\\,\\text{V}$"], "erklaerung": "…" }
```
`loesungsweg` als Text oder Liste von Schritten.
**freitext** – `{ "frage", "musterantwort", "kriterien": [ … ] }`
**karteikarte** – `{ "vorne", "hinten" }`

**Code** (Sprache in `sprache`, Standard `python`; Code als ein String mit `\n`):
`code_ausgabe` (code, frage?, optionen + richtig **oder** erwartete_ausgabe) · `code_luecke` (code, antworten) · `code_fehler` (code, fehlerzeile, korrektur) ·
`code_reihenfolge` (zeilen) · `programmieraufgabe` (aufgabe, startcode, tests, hinweise, musterloesung, kriterien, schwierigkeit 1–3).
Bei `tests[].erwartet` steht das `repr()` des Rückgabewerts; für `print`-Aufgaben `{ "eingabe", "ausgabe" }`.

---

## Regeln
- IDs kleingeschrieben mit Bindestrichen; **bestehende IDs nie ändern** (Fortschritt hängt daran).
  Neue IDs: Lektion `<einheit>-l<n>`, Aufgabe `<einheit>-l<n>-a<n>`. Ältere Inhalte mit anderen IDs bleiben so.
- Formeln in LaTeX zwischen `$...$` (Darstellung mit KaTeX), Code in Backticks, Hervorhebung mit `**…**`.
- Eine Lektion = ein kleines Thema und eine `art`. Schnellfragen: 5–10 Aufgaben. Theorie: Bausteine, Aufgaben optional.
  Programmieren: eine Notebook-Aufgabe pro Lektion (ältere Lektionen mit `programmieraufgabe`: 1–3).
- Nur Inhalte aus dem Kursmaterial; `quelle` immer angeben.
- Jede neue Einheit zuerst in `fach.json` eintragen (Status `geplant`), mit Datei dann `bereit`.

## Woher das Material kommt
| Ort | Wer schreibt | Wer liest |
|---|---|---|
| `digital-campus\material\<fach-id>\` | nur der ILIAS-Agent (Skill «ilias-aktualisieren») | Fach-Projekte |
| `Documents\HSLU\<Fach>\` | nur du (eigene Notizen, Lösungen) | Fach-Projekte, nur lesen |
| `digital-campus\content\<fach-id>\` | Fach-Projekte | Apps, `tools/pruefen.py` |

Niemand ausser dir schreibt in `Documents\HSLU`. Im Ordner `material\` nichts von Hand ablegen – der Agent darf dort alles überschreiben.

## Adapter in den Fach-Apps
Die Fach-Apps wurden vor Format v2 gebaut. Damit sie nicht umgeschrieben werden müssen, enthält jede
`index.html` oben einen kleinen Adapter (`<script id="dc-format-v2">`). Er liest die v2-Dateien und gibt sie
der App im alten internen Format weiter. Zusätzlich findet er bei lokalen Kopien (`app/faecher/`) den Ordner
`../../content/` automatisch. Wer eine App neu baut, liest direkt v2 und lässt den Adapter weg.

## Prüfen
```
python tools/pruefen.py          # prüft alle Fächer gegen content/schema.json
```
Braucht einmalig `pip install jsonschema`. Meldet Schemafehler, fehlende Einheiten-Dateien und Dateien, die nicht in `fach.json` stehen.

## Änderungen
- **v2.3 (24.11.2026, Vorschlag aus dem Fach-Projekt Industrielle Digitalisierung, beim Aufräumen am 24.11.2026 geprüft und übernommen):**
  Baustein `grafik` (svg, beschriftung); `bild` mit `beschriftung`; `hinweis` mit `titel`, `quelle` (Web-Ergänzungen nur so markiert);
  Fach-Ordner `bilder/`; Zusatz `vorbereitung/` mit Schema `#/$defs/vorbereitung`; `tools/pruefen.py` prüft Vorbereitungsdateien.
  Nichts umbenannt oder entfernt, alle bestehenden Dateien bleiben gültig. Renderer-Vorlage: `app/faecher/industrielle-digitalisierung.html`
  (Funktion `inhaltHtml`, CSS-Block «v2.3: Grafiken, Bilder, Hinweise, Unter-Reiter, Checkliste»).
- **v2.2 (10.11.2026):** Einheit in drei Abschnitte (Theorie · Schnellfragen · Programmieren, sonst Üben). Neu, alles optional:
  Lektion `abschnitt` (Zuordnung aus `art`, wenn es fehlt), Notebook-Felder `aufgabe`, `zellen`, `tests`, `loesung`, `hinweise`,
  `schwierigkeit`, `eingaben`; Lektion braucht nicht mehr zwingend `aufgaben`/`schritte` (reine Theorie- und Notebook-Lektionen);
  Baustein `code` mit `ausgabe`, `ausfuehrbar`; `code` + `sprache` bei allen Aufgabentypen; `code_ausgabe` mit `frage` und
  `erwartete_ausgabe`; `fach.json` `abschnitte`. Nichts umbenannt oder entfernt, alle bestehenden Dateien bleiben gültig.
- **v2.1 (10.11.2026):** `fach.json` mit `ilias`, `material`, `eigene_unterlagen` (statt `quellordner`); Kursmaterial in `material/<fach-id>/`.
- **v2 (10.11.2026):** `format`, `kurz` = Modulkürzel, `status`, `schrift`, `zusaetze`; Einheiten in `fach.json` als Objekte mit `bereich`/`status`;
  `termine.json` für alle Fächer einheitlich; Lektion `aufgaben` (statt `uebungen`), `dauer_min` (statt `dauer`), optional `inhalt` und `schritte`;
  Aufgabentyp `rechnung` (statt `rechnen`), `wahr_falsch` mit `aussage`/`richtig`, `multiple_choice` mit `richtig` (statt `auswahl`/`loesung`);
  Einheit `woche` (statt `sw`), `quelle` (statt `quellen`); `art` ergänzt um `rechnen`, `aufgabe`.
- **v1 (5.11.2026):** erste Fassung.
