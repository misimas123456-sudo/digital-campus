# Anleitung für Fach-Projekte

So legst du ein Fach-Projekt in Claude an bzw. hältst es auf dem aktuellen Stand:

1. Projekt «<Fachname> – Digital Campus» erstellen (z. B. «Mathematik – Digital Campus»).
2. Folien, Skripte, Übungen und Probeprüfungen des Fachs aus `digital-campus\material\<fach-id>\` hochladen
   (dort legt der ILIAS-Agent das Kursmaterial ab). Eigene Notizen aus `Documents\HSLU\<Fach>` nur bei Bedarf dazu.
3. Die fertigen Projekt-Anweisungen des Fachs aus dem Hauptprojekt nehmen
   (Projekt-Doc `docs/fach-projekt-anweisungen.md`) bzw. den Text unten anpassen.
4. `docs/inhaltsformat.md` und `docs/navigation.md` als Dateien ins Projekt legen.
5. Erzeugte Dateien nach `digital-campus/content/<fach-id>/` speichern:
   neue Einheit nach `einheiten/`, Eintrag in `fach.json` (Status `bereit`), Termine in `termine.json`.
6. `python tools/pruefen.py` laufen lassen – erst wenn alles gültig ist, das Artifact aktualisieren.
7. Das Fach-Artifact heisst «<Fachname> – Digital Campus», enthält `index.html` + `content/<fach-id>/…`
   und setzt `<html data-theme="<fach-id>">`. Den Adapter `<script id="dc-format-v2">` in `index.html` nicht entfernen,
   solange die App intern noch das alte Format nutzt.

---

## Projekt-Anweisungen (Grundtext)

Dieses Projekt erzeugt Lerninhalte für meine Lern-App «Digital Campus» im Fach **<Fachname>**
(Fach-ID: `<fach-id>`).

- Halte dich strikt an das Inhaltsformat v2 in `inhaltsformat.md`. Gib Dateien als gültiges JSON aus.
- Jede Einheit steht in `fach.json` (mit `bereich` und `status`), auch geplante.
- Termine des Fachs gehören in `termine.json` (Format v2: `art`, `von`, `bis`, `bewertet`, `pflicht`).
- Kursmaterial kommt aus `digital-campus\material\<fach-id>\` (gehört dem ILIAS-Agent). In `Documents\HSLU` und `material\` nie etwas speichern.
- Verwende nur Inhalte aus den hochgeladenen Unterlagen und gib bei jeder Aufgabe die `quelle` an.
- Eine Einheit entspricht einer Semesterwoche, eine Lektion 3–5 Minuten (5–10 Aufgaben).
- Neue IDs: Lektion `<einheit>-l<n>`, Aufgabe `<einheit>-l<n>-a<n>`; bestehende IDs nie ändern.
- Navigation nach `navigation.md`: Dashboard-Link in der Kopfzeile, Zurück-Knopf auf jeder Stufe.
- Sprache: Deutsch.
