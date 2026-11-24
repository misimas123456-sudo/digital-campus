# Projekt-Anweisungen «Python Basics – Digital Campus» (zum Kopieren)

Dieses Projekt erzeugt Lerninhalte für meine Lern-App «Digital Campus» im Fach **Python Basics**
(Fach-ID: `python-basics`). Eine Einheit entspricht einer Semesterwoche, die Einheit-IDs stehen in
`einheiten-plan.md`.

Jede Einheit hat drei Abschnitte (Feld `abschnitt`, sonst aus `art`), Format siehe `docs/inhaltsformat.md` v2.2:
1. **Theorie** (`art: verstaendnis`, `abschnitt: theorie`) – Skriptblöcke in `inhalt`: titel, text, liste, tabelle,
   `code` mit `ausgabe` und `ausfuehrbar: true`, merke, hinweis. Keine Aufgaben nötig.
2. **Schnellfragen** (`art: code` oder `verstaendnis` mit `abschnitt: schnellfragen`) – 5–10 kurze Fragen:
   multiple_choice, wahr_falsch, zuordnen, karteikarte, code_ausgabe (Optionen oder `erwartete_ausgabe`),
   code_luecke, code_fehler, code_reihenfolge. `code` ist bei allen Typen erlaubt.
3. **Programmieren** (`art: programmieren`) – eine Notebook-Aufgabe pro Lektion: `aufgabe`, `zellen`
   (markdown/code, `gesperrt` für Vorgaben), `tests` (Python mit `assert …, "Meldung"`, `_ausgabe` = gesamte
   Ausgabe), `loesung`, `hinweise`, `schwierigkeit` 1–3, `eingaben` für `input()`.

Regeln:
- Nur Stoff bis zur jeweiligen Woche (in SW03 z. B. noch keine Funktionen); `quelle` immer angeben.
- Code-Ausgaben genau so, wie Python sie druckt (vor dem Speichern ausführen).
- Musterlösung muss die Tests bestehen, die Startzellen nicht.
- IDs nie ändern; neue Lektionen fortlaufend `<einheit>-l<n>`.
- Nach Änderungen `python tools/pruefen.py` laufen lassen.
- Sprache: Deutsch (Schweizer Rechtschreibung).
