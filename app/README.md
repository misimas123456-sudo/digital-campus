# App

- `faecher/<fach-id>.html` – lokale Kopien der Fach-Artifacts («<Fachname> – Digital Campus»), alle 8 Fächer.
  Sie laden ihre Inhalte aus `../../content/<fach-id>/` (der Adapter `dc-format-v2` sucht dort automatisch).
  Zum Testen lokal über einen Webserver öffnen, z. B. im Ordner `digital-campus`: `python -m http.server`
  und dann http://localhost:8000/app/faecher/python-basics.html (direkt per Doppelklick blockiert der Browser `fetch`).
- `termine.html` – «Termine & Prüfungen – Digital Campus».
- Das Dashboard («Dashboard – Digital Campus») ist ein Claude-Dashboard und existiert nur als Artifact.

Design: `../design/` (Design System «Digital Campus»). Jede Seite setzt `<html data-theme="<fach-id>">`.
Navigation: `../docs/navigation.md`.

Phase 2: Vite-Projekt + PWA / Capacitor (siehe `docs/architektur.md`).
