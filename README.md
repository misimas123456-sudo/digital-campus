# Digital Campus

Eigene Lern-App für meine HSLU-Fächer – spielerisch, in kleinen Lektionen (Duolingo-Prinzip),
auf Handy (Android) und Computer. Gratis, nicht im App Store.

## Einstieg
- **Dashboard – Digital Campus** (Startseite): https://claude.ai/artifact/3nucn1BNbLGW39vSE3pUGQ
- **Termine & Prüfungen – Digital Campus**: https://claude.ai/artifact/GXwh5vzPhKFvxRuxK99jqC
- Fach-Apps: Links in `content/faecher.json` und auf dem Dashboard.

## Namen
- Sichtbarer Name überall: **«<Fachname> – Digital Campus»** (Artifacts, Claude-Projekte, Seitentitel).
- Intern (Ordner, Dateien, Speicher-Schlüssel) immer die **Fach-ID**. Fach-IDs nie ändern.
- **GRUNDING** = umgangssprachlich für **Industrielle Digitalisierung** (`industrielle-digitalisierung`).

## Fächer

| Fach-ID | Fach | Kürzel | Status |
|---|---|---|---|
| `python-basics` | Python Basics | PYTHON | in Arbeit |
| `mathematik` | Mathematik | MATH1B | in Arbeit |
| `digitaltechnik` | Digitaltechnik | DT | in Arbeit |
| `elektrotechnik` | Elektrotechnik mit Labor | ET+L | in Arbeit |
| `konstruktion-maschinentechnik` | Konstruktion Maschinentechnik | KONST_M | in Arbeit |
| `kontextmodul` | Kontextmodul | KONTT1 | in Arbeit |
| `mechanik-werkstoffkunde` | Mechanik und Werkstoffkunde | MECH_WSK1 | geplant |
| `industrielle-digitalisierung` | Industrielle Digitalisierung (GRUNDING) | GRUNDING | in Arbeit |

## Ordnerstruktur

```
digital-campus/
  README.md                       diese Übersicht
  docs/
    inhaltsformat.md              Inhaltsformat v2.3 – verbindlich für alle Fächer
    navigation.md                 Navigation (Dashboard-Link, Zurück-Knöpfe)
    design-farbschema.md          Farben & Schriften pro Fach
    frag-claude.md, frag-claude-modul.html   «Frag Claude»-Knopf (Modul v1)
    lektions-position.md          Weitermachen bei der gleichen Übung
    mathe-namensregeln.md         Zusatzregeln Mathematik
    fach-projekt-anweisungen.md   Anweisungstexte für die Fach-Projekte
    architektur.md, roadmap.md, fach-projekt-anleitung.md
  design/                         Design System: tokens.json, tokens.css, fonts/
  material/<fach-id>/             Kursmaterial von ILIAS – gehört dem ILIAS-Agent, nicht von Hand bearbeiten (nicht im Git)
  tools/
    pruefen.py                    prüft alle Inhalte gegen content/schema.json
  content/
    schema.json                   JSON Schema (Einheit, fach.json, termine.json, faecher.json)
    faecher.json                  Liste aller Fächer mit Links
    <fach-id>/
      fach.json                   Metadaten + Liste aller Einheiten (Pflicht)
      termine.json                Termine des Fachs (Pflicht, darf leer sein)
      einheiten/<swXX-thema>.json eine Einheit pro Semesterwoche
      …                           Zusätze, in fach.json unter "zusaetze" (themen.json, quellen/, testvorbereitung/)
  app/
    termine.html                  Termine & Prüfungen
    faecher/<fach-id>.html        Fach-Apps (lokale Kopien der Artifacts)
```

Jedes Fach-Artifact hat innen dieselbe Struktur: `index.html` + `content/<fach-id>/…`.
Die lokalen Kopien in `app/faecher/` lesen `../../content/<fach-id>/` (automatisch, über den Adapter).

## Arbeitsweise
- **Claude-Projekt «Digital Campus»** = Dachprojekt: App-Grundgerüst, Dashboard, Design, Inhaltsformat.
- **Ein Claude-Projekt pro Fach** («<Fachname> – Digital Campus») erzeugt Inhalte nach `docs/inhaltsformat.md`.
- Nach jeder Änderung an Inhalten: `python tools/pruefen.py` laufen lassen.
- **Kursmaterial** holt der ILIAS-Agent nach `material/<fach-id>/`. Deine **eigenen Unterlagen** bleiben in `Documents/HSLU` –
  dort schreibt kein Agent hinein; Fach-Projekte lesen sie nur.
- `Documents/HSLU` bleibt Google-Drive-synchronisiert Dieser Ordner liegt bewusst
  **ausserhalb** von Google Drive, damit Git sauber funktioniert.

## Git & GitHub
- Der Ordner ist ein **öffentliches** GitHub-Repository (Versionsverlauf + Backup, später Hosting der PWA über GitHub Pages).
- Was **nicht** ins Repo kommt, steht in `.gitignore`: Kursmaterial (`material/`), der Volltext der Mathe-Skripte
  (`content/mathematik/quellen/`), Folien- und Übungsbilder (`content/*/bilder/`), Backups und Claude-PDFs.
  Grund: HSLU-Material ist urheberrechtlich geschützt und darf nicht öffentlich sein.
- Neue Ordner mit Kursmaterial oder Screenshots von Folien immer zuerst in `.gitignore` eintragen.
- Arbeitsablauf mit GitHub Desktop: nach jeder Arbeitssitzung **Commit** (kurze Beschreibung, was geändert wurde) → **Push origin**.
