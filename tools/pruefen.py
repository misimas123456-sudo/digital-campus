"""Prüft alle Inhalte in content/ gegen content/schema.json (Inhaltsformat v2).
Aufruf im Ordner digital-campus:  python tools/pruefen.py
Einmalig nötig:                   pip install jsonschema"""
import json, pathlib, sys
try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("Bitte zuerst installieren:  pip install jsonschema")

ROOT = pathlib.Path(__file__).resolve().parent.parent / "content"
S = json.loads((ROOT / "schema.json").read_text(encoding="utf-8"))
def validator(teil): return Draft202012Validator({"$defs": S["$defs"], "$ref": "#/$defs/" + teil})
V = {t: validator(t) for t in ["faecher", "fach", "termine", "einheit", "vorbereitung"]}
fehler = geprueft = 0

def pruefe(datei, teil):
    global fehler, geprueft
    geprueft += 1
    try:
        daten = json.loads(datei.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"✗ {datei.relative_to(ROOT)}: kein gültiges JSON ({e})"); fehler += 1; return None
    for e in list(V[teil].iter_errors(daten))[:10]:
        stelle = "/".join(map(str, e.absolute_path)) or "(oben)"
        print(f"✗ {datei.relative_to(ROOT)} → {stelle}: {e.message[:200]}"); fehler += 1
    return daten

pruefe(ROOT / "faecher.json", "faecher")
for ordner in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    fach = pruefe(ordner / "fach.json", "fach") if (ordner / "fach.json").exists() else None
    if not fach:
        print(f"✗ {ordner.name}: fach.json fehlt"); fehler += 1; continue
    zus = fach.get("zusaetze", {})
    for name, pfad in zus.items():
        if not (ordner / pfad).exists():
            print(f"✗ {ordner.name}: Zusatz «{name}» → {pfad} fehlt"); fehler += 1
    if zus.get("termine") and (ordner / zus["termine"]).exists():
        pruefe(ordner / zus["termine"], "termine")
    vb = zus.get("vorbereitung")
    if vb and (ordner / vb).is_dir():
        ids = {e["id"] for e in fach.get("einheiten", [])}
        for p in sorted((ordner / vb).glob("*.json")):
            d = pruefe(p, "vorbereitung")
            if d and (d.get("einheit") != p.stem or p.stem not in ids):
                print(f"✗ {p.relative_to(ROOT)}: Name/«einheit» muss eine Einheit-ID aus fach.json sein"); fehler += 1
    eingetragen = set()
    for e in fach.get("einheiten", []):
        pfad = ordner / (e.get("datei") or f"einheiten/{e['id']}.json"); eingetragen.add(pfad.resolve())
        if pfad.exists():
            d = pruefe(pfad, "einheit")
            if d and d.get("id") != e["id"]:
                print(f"✗ {pfad.relative_to(ROOT)}: id «{d.get('id')}» passt nicht zu fach.json «{e['id']}»"); fehler += 1
        elif e.get("status") in ("bereit", "entwurf"):
            print(f"✗ {ordner.name}: Einheit {e['id']} hat Status {e['status']}, aber {pfad.relative_to(ROOT)} fehlt"); fehler += 1
    if (ordner / "einheiten").exists():
        for p in sorted((ordner / "einheiten").glob("*.json")):
            if p.resolve() not in eingetragen:
                print(f"✗ {p.relative_to(ROOT)}: steht nicht in fach.json"); fehler += 1

print(f"\n{geprueft} Dateien geprüft – " + ("alles gültig ✓" if not fehler else f"{fehler} Fehler"))
sys.exit(1 if fehler else 0)
