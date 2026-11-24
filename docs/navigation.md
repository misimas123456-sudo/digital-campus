# Navigation – Digital Campus

Gilt für alle Fach-Artifacts. Bei jeder Neufassung eines Fach-Artifacts beibehalten.

## Stufen
Dashboard → Fach (Übersicht/Tabs) → Einheit → Lektion

- **Dashboard-Link**: in der Kopfzeile jedes Fach-Artifacts, immer sichtbar (auch in Einheit und Lektion).
  - Markup: `<a class="dc-home" href="https://claude.ai/artifact/3nucn1BNbLGW39vSE3pUGQ" aria-label="Zurück zum Dashboard">…Haus-Icon…<span>Dashboard</span></a>`
  - Farbe Campus-Lila `--dc-campus` (#af9ee4), 1px-Linie, Pill. Unter 520px nur Icon.
  - Normaler Link ohne `target="_top"` (Artifacts laufen in einem Sandbox-Frame).
- **Zurück eine Stufe**: in jeder Einheit und Lektion ein Knopf «‹ <übergeordnete Stufe>» (z. B. «‹ Theorie», «‹ Block 3»). Auf der obersten Fach-Ebene keiner.
- Die Fach-Startansicht heisst **«Übersicht»**, nie «Dashboard» – «Dashboard» meint immer das zentrale Dashboard.

## Dashboard
- Abschnitte: Nächste 3 Pflicht-Termine · Lernplan ausserhalb der Schule · Stundenplan · Fächer · Wichtig zu wissen · Infos aktualisieren.
- Lernplan (Datei `lernplan.json`, fix): Mo Mathematik · Di Digitaltechnik, Industrielle Digitalisierung · Mi Mathematik, Konstruktion Maschinentechnik · Do Python Basics, Elektrotechnik · Fr/Sa frei · So Mechanik und Werkstoffkunde, Kontextmodul. Jeder Eintrag verlinkt auf die Lern-App des Fachs (über die Fach-ID in `faecher.json`).
