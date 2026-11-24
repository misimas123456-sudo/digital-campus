# Design: Farben & Schriften pro Fach

Design System «Design System – Digital Campus»: https://claude.ai/artifact/MTcZF5k1c3ymUHWvUR8tNg
Dateien: `design/tokens.json`, `design/tokens.css`, `design/fonts/`.

Grundsatz: immer Dark Mode, clean, feine Akzente. Neutrale Flächen (pro Fach minimal getönt), Fachfarbe nur für
Fortschritt, aktiven Tab, einen Primär-Button pro Ansicht, Links und 1px-Akzentlinien. Keine Verläufe, kein Glow,
keine farbigen Kartenflächen. Dashboard/Navigation/Termine: Campus-Lila `#af9ee4` + Outfit.
Code: JetBrains Mono. Formeln: KaTeX (nur Digitaltechnik nutzt noch MathJax).

Umsetzung: `<html data-theme="<fach-id>">`; Komponenten nutzen nur Variablen. In den Artifacts heissen sie `--dc-*`
(z. B. `--dc-accent`, `--dc-surface`, `--dc-font-fach`), in `design/tokens.css` ohne Präfix.

| Fach-ID | Fach | Akzent | Schrift |
|---|---|---|---|
| `python-basics` | Python Basics | `#c9bb83` Senfgelb | Space Grotesk |
| `mathematik` | Mathematik | `#a4bbe5` Taubenblau | Fraunces |
| `digitaltechnik` | Digitaltechnik | `#9dc7a5` Salbeigrün | Chakra Petch |
| `elektrotechnik` | Elektrotechnik mit Labor | `#ddb183` Bernstein/Kupfer | Barlow |
| `konstruktion-maschinentechnik` | Konstruktion Maschinentechnik | `#9ac2d4` Stahlblau-grau | Archivo |
| `kontextmodul` | Kontextmodul | `#d4adc6` Altrosa/Mauve | Lora |
| `mechanik-werkstoffkunde` | Mechanik und Werkstoffkunde | `#daa198` Rost/Terrakotta | Bricolage Grotesque |
| `industrielle-digitalisierung` | Industrielle Digitalisierung (GRUNDING) | `#92c6c2` Petrol | Sora |

Gemeinsam: text `#ebeaef`, text-muted `#aaaab2`, text-faint `#807f87`,
success `#8ec7a1`, warning `#dcc188`, danger `#dc8b88`.
Abstände 4px-Raster, Radien 6/10/16/pill, Linien 1px.
