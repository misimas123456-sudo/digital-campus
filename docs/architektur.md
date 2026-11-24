# Architektur

## Phase 1 – MVP als Claude-Artifact
- Eine Web-App (HTML/JS), gehostet als Claude-Artifact, per Link auf PC und Handy.
- Fortschritt in der Artifact-Datenbank (pro Person, geräteübergreifend).
- Claude direkt eingebaut (Erklärungen, freie Antworten bewerten).
- Optional: Connectors (z. B. Microsoft 365 für Mail/Kalender).

## Phase 2 – Eigenständige App
- Code nach `app/` als Vite-Projekt übernehmen.
- PWA (installierbar auf Android) + optional Capacitor → APK, direkt installiert (kein Play Store nötig).
- Datenbank: Supabase o. ä.; Claude über eigene Serverfunktion mit API-Schlüssel.

## Wichtigste Regel: Plattform-Funktionen kapseln
Alles, was von Claude-Artifacts abhängt, läuft über eine Zwischenschicht:

| Modul | Phase 1 | Phase 2 |
|---|---|---|
| `storage` (Fortschritt) | Artifact-DB | Supabase / localStorage |
| `ai` (Claude fragen) | Artifact `sample` | eigene API-Funktion |
| `integrations` (Mail, Kalender) | Connectors | Microsoft Graph |

Beim Umzug wird nur diese Schicht ersetzt, Inhalte und UI bleiben.

## Bildschirme (MVP)
1. **Start:** Fachauswahl mit Fortschritt pro Fach, Streak, XP.
2. **Fach:** Lernpfad (Einheiten → Lektionen), gesperrt/offen/erledigt.
3. **Lektion:** 5–10 Aufgaben nacheinander, sofortiges Feedback, Erklärung bei Fehler.
4. **Abschluss:** XP, Fehler wiederholen.
5. **Campus (später):** Links zu Hochschul-Seiten, Mail, Stundenplan.
