#!/usr/bin/env python3
"""
Prüft Theme-Regeln, die Shopify beim Upload/GitHub-Sync erzwingt, Theme Check aber nicht meldet.
Verstöße führen dazu, dass Shopify die Datei still ablehnt – und JSON-Vorlagen, die solche
Sektionen nutzen, gleich mit.

  - Namen von Sektionen, Blöcken, Presets ≤ 25 Zeichen; theme_name/theme_author ≤ 25
  - Setting-Labels ≤ 70 Zeichen
  - kein leerer Standardwert ("default": "")
  - Range-Werte in settings_data.json liegen im Raster (min + n*step) und im Bereich
  - jede in JSON-Vorlagen verwendete Sektion/jeder Blocktyp existiert im Schema
Aufruf: python3 scripts/check_shopify_rules.py   (Exit-Code 1 bei Fehlern)
"""
import glob, json, re, sys

errors = []


def strip_comment(text):
    return re.sub(r'^\s*/\*.*?\*/', '', text, flags=re.S)


def check_settings(lst, where):
    for st in lst:
        sid = st.get("id", st.get("type"))
        if st.get("default") == "":
            errors.append(f"{where}: setting '{sid}' hat leeren default")
        label = st.get("label")
        if isinstance(label, str) and not label.startswith("t:") and len(label) > 70:
            errors.append(f"{where}: label von '{sid}' > 70 Zeichen ({len(label)})")


def check_name(obj, where, kind):
    n = obj.get("name")
    if isinstance(n, str) and not n.startswith("t:") and len(n) > 25:
        errors.append(f"{where}: {kind}-Name '{n}' > 25 Zeichen")


schemas = {}
for path in sorted(glob.glob("sections/*.liquid")):
    m = re.search(r"{% schema %}(.*?){% endschema %}", open(path, encoding="utf-8").read(), re.S)
    if not m:
        schemas[path.split("/")[-1][:-7]] = {}  # Sektion ohne Schema (z. B. main-404)
        continue
    sc = json.loads(m.group(1))
    schemas[path.split("/")[-1][:-7]] = sc
    check_name(sc, path, "Sektion")
    check_settings(sc.get("settings", []), path)
    for b in sc.get("blocks", []):
        check_name(b, f"{path} [{b.get('type')}]", "Block")
        check_settings(b.get("settings", []), f"{path} [{b.get('type')}]")
    for p in sc.get("presets", []):
        check_name(p, path, "Preset")

schema = json.load(open("config/settings_schema.json", encoding="utf-8"))
for key in ("theme_name", "theme_author"):
    if len(schema[0].get(key, "")) > 25:
        errors.append(f"config/settings_schema.json: {key} > 25 Zeichen")
ranges = {}
for g in schema[1:]:
    check_settings(g.get("settings", []), f"settings_schema [{g.get('name')}]")
    for st in g.get("settings", []):
        if st.get("type") == "range":
            ranges[st["id"]] = st

data = json.loads(strip_comment(open("config/settings_data.json", encoding="utf-8").read()))
current = data.get("current")
preset = data["presets"].get(current) if isinstance(current, str) else current
for k, v in (preset or {}).items():
    r = ranges.get(k)
    if r and isinstance(v, (int, float)):
        step = r.get("step", 1)
        if not (r["min"] <= v <= r["max"]) or (v - r["min"]) % step:
            errors.append(f"settings_data: '{k}'={v} nicht im Raster {r['min']}..{r['max']} step {step}")

for path in sorted(glob.glob("templates/*.json") + glob.glob("sections/*.json")):
    d = json.loads(strip_comment(open(path, encoding="utf-8").read()))
    for key, sec in d.get("sections", {}).items():
        sc = schemas.get(sec["type"])
        if sc is None:
            errors.append(f"{path}: Sektion '{sec['type']}' existiert nicht")
            continue
        types = {b["type"] for b in sc.get("blocks", [])}
        for bk, b in sec.get("blocks", {}).items():
            if b["type"] not in types and "@app" not in types | {b["type"]}:
                errors.append(f"{path}: Blocktyp '{b['type']}' fehlt in Sektion '{sec['type']}'")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK – {len(schemas)} Sektionen, Schema, Einstellungen und Vorlagen erfüllen die Shopify-Regeln.")
