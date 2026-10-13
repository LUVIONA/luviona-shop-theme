#!/usr/bin/env python3
"""
LUVIONA – richtet den Shopify-Shop per Admin GraphQL API ein (idempotent, mehrfach ausführbar).

Legt an bzw. aktualisiert:
  1. Metafelddefinitionen  luviona.*            (GPSR, Kosmetik, Material, Lieferzeit …)
  2. Produkte inkl. Bilder, Varianten, SEO      (Quelle: docs/produkte-import.csv)
  3. Smart-Kollektionen                          (Armbänder, Ketten, Taschen-Charms, Geschenke)
  4. Seiten mit Theme-Vorlagen                  (Impressum, Widerruf, FAQ, Über uns, Kontakt …)
  5. Menüs                                       (Hauptmenü, Service, Rechtliches)
  und veröffentlicht alles im Vertriebskanal „Online Store“.

Benötigte Umgebungsvariablen:
  SHOPIFY_STORE          z. B. luviona-xyz.myshopify.com  (die myshopify-Adresse, nicht luviona.de)
  und ENTWEDER (App aus dem Shopify Dev Dashboard, Standard seit 2026):
  SHOPIFY_CLIENT_ID      Client-ID der App
  SHOPIFY_CLIENT_SECRET  Client-Secret der App  → das Skript holt sich per Client-Credentials-Grant
                         ein Zugriffstoken (gültig ca. 24 h)
  ODER (ältere, im Admin erstellte App):
  SHOPIFY_ADMIN_TOKEN    Admin-API-Zugriffstoken (shpat_…)
  Scopes der App: write_products, read_products, write_content, read_content,
                  write_online_store_navigation, read_online_store_navigation,
                  write_publications, read_publications
  SHOPIFY_API_VERSION  optional, Standard 2026-07

Aufruf:
  python3 scripts/shopify_setup.py            # alles
  python3 scripts/shopify_setup.py --dry-run  # nur anzeigen, was passieren würde
  python3 scripts/shopify_setup.py products pages   # nur einzelne Schritte

Rechtstexte (AGB, Datenschutz, Widerruf) werden bewusst NICHT angelegt – die kommen aus dem
Abmahnschutz-Paket. Impressum & Co. bekommen nur Platzhalter, die nichts überschreiben,
wenn die Seite bereits Inhalt hat.
"""
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.environ.get("SHOPIFY_STORE", "").replace("https://", "").strip("/")
TOKEN = os.environ.get("SHOPIFY_ADMIN_TOKEN", "")
CLIENT_ID = os.environ.get("SHOPIFY_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("SHOPIFY_CLIENT_SECRET", "")
VERSION = os.environ.get("SHOPIFY_API_VERSION", "2026-07")
DRY = "--dry-run" in sys.argv
STEPS = [a for a in sys.argv[1:] if not a.startswith("--")] or [
    "metafields", "products", "collections", "pages", "menus"]


# --------------------------------------------------------------------------- API
def fetch_token():
    """Client-Credentials-Grant für Dev-Dashboard-Apps, die im eigenen Shop installiert sind."""
    body = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": CLIENT_ID,
                                   "client_secret": CLIENT_SECRET}).encode()
    req = urllib.request.Request(f"https://{STORE}/admin/oauth/access_token", data=body,
                                 headers={"Content-Type": "application/x-www-form-urlencoded",
                                          "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Token-Abruf fehlgeschlagen (HTTP {e.code}): {e.read().decode()[:300]}\n"
                         "Prüfen: App im Dev Dashboard veröffentlicht (Version freigegeben) und im Shop installiert?")
    print(f"Token erhalten, Scopes: {data.get('scope')}")
    return data["access_token"]


def gql(query, variables=None):
    if DRY:
        return {}
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        f"https://{STORE}/admin/api/{VERSION}/graphql.json", data=body,
        headers={"Content-Type": "application/json", "X-Shopify-Access-Token": TOKEN})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503) and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise SystemExit(f"HTTP {e.code}: {e.read().decode()[:500]}")
        if data.get("errors"):
            if any("THROTTLED" in json.dumps(x) for x in data["errors"]) and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise SystemExit("GraphQL-Fehler: " + json.dumps(data["errors"], ensure_ascii=False)[:1500])
        return data["data"]
    raise SystemExit("Zu viele Wiederholungen")


def user_errors(result, key):
    errs = (result.get(key) or {}).get("userErrors") or []
    for e in errs:
        print(f"    ! {key}: {e.get('field')} – {e.get('message')}")
    return errs


def log(msg):
    print(("[dry-run] " if DRY else "") + msg)


_publication = None


def online_store_publication():
    global _publication
    if _publication is None and not DRY:
        d = gql("{ publications(first: 20) { nodes { id name } } }")
        names = {n["name"]: n["id"] for n in d["publications"]["nodes"]}
        _publication = names.get("Online Store") or names.get("Onlineshop") or next(iter(names.values()), None)
    return _publication


def publish(gid):
    pub = online_store_publication()
    if not pub or DRY:
        return
    r = gql("""mutation($id: ID!, $input: [PublicationInput!]!) {
      publishablePublish(id: $id, input: $input) { userErrors { field message } } }""",
            {"id": gid, "input": [{"publicationId": pub}]})
    user_errors(r, "publishablePublish")


# ------------------------------------------------------------------ 1. Metafelder
METAFIELDS = [
    ("lieferzeit", "Lieferzeit", "single_line_text_field"),
    ("material", "Material & Maße", "rich_text_field"),
    ("pflege", "Pflegehinweise", "rich_text_field"),
    ("lieferumfang", "Lieferumfang", "rich_text_field"),
    ("groesse", "Größe & Verstellbarkeit", "rich_text_field"),
    ("hinweise", "Sonstige Hinweise", "rich_text_field"),
    ("hersteller_name", "Hersteller – Name", "single_line_text_field"),
    ("hersteller_anschrift", "Hersteller – Anschrift", "multi_line_text_field"),
    ("hersteller_kontakt", "Hersteller – Kontakt", "single_line_text_field"),
    ("eu_verantwortliche", "EU-Verantwortliche (GPSR)", "multi_line_text_field"),
    ("produktkennung", "Produktkennung", "single_line_text_field"),
    ("warnhinweise", "Warnhinweise", "multi_line_text_field"),
    ("material_konformitaet", "Materialkonformität (REACH)", "multi_line_text_field"),
    ("ki_bilder", "KI-Bilder (Hinweis anzeigen)", "boolean"),
    ("verwendungszweck", "Kosmetik – Verwendungszweck", "single_line_text_field"),
    ("fuellmenge", "Kosmetik – Füllmenge", "single_line_text_field"),
    ("inci", "Kosmetik – INCI", "multi_line_text_field"),
    ("pao", "Kosmetik – PAO", "single_line_text_field"),
    ("mhd", "Kosmetik – MHD", "single_line_text_field"),
    ("charge_hinweis", "Kosmetik – Chargen-Hinweis", "single_line_text_field"),
    ("kosmetik_verantwortliche", "Kosmetik – Verantwortliche Person", "multi_line_text_field"),
    ("allergene", "Kosmetik – Allergene", "multi_line_text_field"),
    ("kosmetik_warnhinweise", "Kosmetik – Warnhinweise", "multi_line_text_field"),
]


def step_metafields():
    print("\n== Metafelddefinitionen ==")
    existing = set()
    if not DRY:
        d = gql("""{ metafieldDefinitions(first: 100, ownerType: PRODUCT, namespace: "luviona") {
                    nodes { key } } }""")
        existing = {n["key"] for n in d["metafieldDefinitions"]["nodes"]}
    for key, name, typ in METAFIELDS:
        if key in existing:
            log(f"  = luviona.{key} existiert")
            continue
        log(f"  + luviona.{key} ({typ})")
        r = gql("""mutation($d: MetafieldDefinitionInput!) {
          metafieldDefinitionCreate(definition: $d) { userErrors { field message } } }""",
                {"d": {"namespace": "luviona", "key": key, "name": name, "type": typ,
                       "ownerType": "PRODUCT", "access": {"storefront": "PUBLIC_READ"}}})
        if not DRY:
            user_errors(r, "metafieldDefinitionCreate")


# ------------------------------------------------------------------- 2. Produkte
def load_products():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "docs", "produkte-import.csv"), encoding="utf-8")))
    products = {}
    for r in rows:
        h = r["Handle"]
        p = products.setdefault(h, {"handle": h, "files": [], "variants": []})
        if r["Title"]:
            p.update(title=r["Title"], body=r["Body (HTML)"], vendor=r["Vendor"], type=r["Type"],
                     tags=[t.strip() for t in r["Tags"].split(",") if t.strip()],
                     option=r["Option1 Name"], seo_title=r["SEO Title"], seo_desc=r["SEO Description"],
                     price=r["Variant Price"], grams=r["Variant Grams"])
        if r["Image Src"]:
            p["files"].append({"originalSource": r["Image Src"], "alt": r["Image Alt Text"], "contentType": "IMAGE"})
        if r["Option1 Value"]:
            p["variants"].append({"value": r["Option1 Value"], "sku": r["Variant SKU"],
                                  "price": r["Variant Price"] or p.get("price"),
                                  "image": r.get("Variant Image", "")})
    return list(products.values())


def find_id(kind, handle):
    if DRY:
        return None
    d = gql(f'{{ {kind}(first: 1, query: "handle:{handle}") {{ nodes {{ id }} }} }}')
    nodes = d[kind]["nodes"]
    return nodes[0]["id"] if nodes else None


def step_products():
    print("\n== Produkte ==")
    for p in load_products():
        option = p["option"] or "Title"
        values = [v["value"] for v in p["variants"]]
        alt_by_src = {f["originalSource"]: f["alt"] for f in p["files"]}
        files = list(p["files"])
        variants = []
        for v in p["variants"]:
            var = {
                "optionValues": [{"optionName": option, "name": v["value"]}],
                "price": v["price"],
                "taxable": True,
                "inventoryPolicy": "DENY",
                "inventoryItem": {"tracked": False, "sku": v["sku"] or None,
                                  "requiresShipping": True,
                                  "measurement": {"weight": {"value": float(p.get("grams") or 0), "unit": "GRAMS"}}},
            }
            if v["image"]:
                var["file"] = {"originalSource": v["image"], "alt": alt_by_src.get(v["image"], p["title"]),
                               "contentType": "IMAGE"}
            variants.append(var)
        inp = {
            "handle": p["handle"], "title": p["title"], "descriptionHtml": p["body"],
            "vendor": p["vendor"], "productType": p["type"], "tags": p["tags"], "status": "ACTIVE",
            "seo": {"title": p["seo_title"], "description": p["seo_desc"]},
            "productOptions": [{"name": option, "values": [{"name": x} for x in values]}],
            "variants": variants, "files": files,
            "metafields": [{"namespace": "luviona", "key": "ki_bilder", "type": "boolean", "value": "true"}],
        }
        if p["type"] == "Kosmetik":
            inp["templateSuffix"] = "kosmetik"
            inp["metafields"].append({"namespace": "luviona", "key": "verwendungszweck",
                                      "type": "single_line_text_field", "value": "Lipgloss"})
        pid = find_id("products", p["handle"])
        if pid:
            inp["id"] = pid
        log(f"  {'~' if pid else '+'} {p['title']}  ({len(variants)} Varianten, {len(files)} Bilder)")
        r = gql("""mutation($input: ProductSetInput!) {
          productSet(synchronous: true, input: $input) {
            product { id handle } userErrors { field message } } }""", {"input": inp})
        if DRY:
            continue
        if not user_errors(r, "productSet"):
            publish(r["productSet"]["product"]["id"])


# ----------------------------------------------------------------- 3. Kollektionen
COLLECTIONS = [
    ("armbaender", "Armbänder", "TYPE", "Armband",
     "<p>Geflochtene Kordelarmbänder und feine Gliederketten mit Tennisschläger und Tennisball – goldfarben oder silberfarben, versandkostenfrei in Deutschland.</p>"),
    ("ketten", "Ketten", "TYPE", "Kette",
     "<p>Die Match Point Kette: feine goldfarbene Gliederkette mit Schläger-Anhänger und Tennisball.</p>"),
    ("taschen-charms", "Taschen-Charms & Kosmetik", "TYPE", "Kosmetik",
     "<p>Der Love Charm: Taschenanhänger aus Kunstleder mit herausnehmbarem Lipgloss – in fünf Farben.</p>"),
    ("geschenke", "Geschenke", "TAG", "geschenk",
     "<p>Für Tennispartnerin, Trainerin oder Team – auf Wunsch in der navy LUVIONA-Box mit Grußkarte.</p>"),
]


def step_collections():
    print("\n== Kollektionen ==")
    for handle, title, column, cond, desc in COLLECTIONS:
        cid = find_id("collections", handle)
        if cid:
            log(f"  = {title} existiert")
            publish(cid)
            continue
        log(f"  + {title} ({column} = {cond})")
        r = gql("""mutation($input: CollectionInput!) {
          collectionCreate(input: $input) { collection { id } userErrors { field message } } }""",
                {"input": {"handle": handle, "title": title, "descriptionHtml": desc,
                           "ruleSet": {"appliedDisjunctively": False,
                                       "rules": [{"column": column, "relation": "EQUALS", "condition": cond}]}}})
        if not DRY and not user_errors(r, "collectionCreate"):
            publish(r["collectionCreate"]["collection"]["id"])


# ---------------------------------------------------------------------- 4. Seiten
PH = '<p><strong>[PLATZHALTER: Text aus dem Abmahnschutz-Paket (united-domains) hier einfügen.]</strong></p>'
PAGES = [
    ("impressum", "Impressum", "rechtstext", PH + "<p>LUVIONA GbR<br>[PLATZHALTER: Name 1, Name 2]<br>[PLATZHALTER: Anschrift]<br>E-Mail: info@luviona.de</p>"),
    ("muster-widerrufsformular", "Muster-Widerrufsformular", "rechtstext", PH + '<p>Du kannst deinen Widerruf auch ganz einfach online erklären: <a href="/pages/widerruf">Vertrag widerrufen</a>.</p>'),
    ("versand-und-zahlung", "Versand & Zahlung", "rechtstext",
     "<h2>Versand</h2><p>Wir versenden ausschließlich innerhalb Deutschlands – versandkostenfrei, aus Deutschland mit [PLATZHALTER: Versanddienstleister]. Lieferzeit 2–4 Werktage nach Zahlungseingang.</p>"
     "<h2>Zahlung</h2><p>[PLATZHALTER: aktivierte Zahlungsarten, z. B. PayPal, Kreditkarte, Klarna, Apple Pay, Google Pay]. Es fallen keine zusätzlichen Gebühren an.</p>"
     "<h2>Preise</h2><p>Gemäß § 19 UStG wird keine Umsatzsteuer berechnet. Deine Rechnung erhältst du per E-Mail.</p>"),
    ("hinweis-zu-unseren-bildern", "Hinweis zu unseren Bildern", "rechtstext",
     "<p>Einige Produkt- und Tragebilder in unserem Shop sind mit Hilfe künstlicher Intelligenz erstellt oder bearbeitet worden. Wir kennzeichnen sie direkt am Bild.</p>"
     "<p>Die KI-Bilder zeigen das Produkt so, wie es ist – Größe, Farbe, Glanz und Details (zum Beispiel das Flechtnetz im Schläger) entsprechen dem gelieferten Artikel. Kleine Abweichungen in Farbe und Details sind möglich. Dekoration wie Taschen, Schals oder Ohrringe gehört nicht zum Lieferumfang.</p>"
     "<p>Zu jedem Artikel findest du außerdem mindestens ein echtes Produktfoto mit Größenvergleich. Keine unserer KI-Bilder stellt reale Personen dar.</p><p>Fragen? info@luviona.de</p>"),
    ("barrierefreiheit", "Barrierefreiheit", "rechtstext",
     "<p>Wir möchten, dass alle unseren Shop nutzen können. luviona.de orientiert sich an den Web Content Accessibility Guidelines (WCAG) 2.1, Stufe AA: ausreichende Kontraste, skalierbare Schrift, Tastaturbedienung mit sichtbarem Fokus, Alternativtexte für Bilder und verständliche Formulare.</p>"
     "<p>Als Kleinstunternehmen sind wir vom Barrierefreiheitsstärkungsgesetz (BFSG) ausgenommen, setzen die Anforderungen aber freiwillig um.</p>"
     "<p>Stößt du auf eine Barriere? Schreib uns an info@luviona.de – wir kümmern uns darum.</p>"),
    ("widerruf", "Vertrag widerrufen", "widerruf", ""),
    ("ueber-uns", "Über LUVIONA", "ueber-uns",
     "<p>Court Style Accessories – Schmuck für alle, die den Tennisplatz lieben und ihren Stil überall tragen wollen.</p>"),
    ("faq", "FAQ", "faq", "<p>Hier findest du Antworten auf die häufigsten Fragen rund um Versand, Größen, Pflege und Rückgabe.</p>"),
    ("kontakt", "Kontakt", "kontakt",
     "<p>Wir freuen uns auf deine Nachricht.</p><p>LUVIONA GbR<br>[PLATZHALTER: Anschrift]<br>info@luviona.de</p>"),
]


def step_pages():
    print("\n== Seiten ==")
    for handle, title, suffix, body in PAGES:
        pid = None
        has_body = False
        if not DRY:
            d = gql(f'{{ pages(first: 1, query: "handle:{handle}") {{ nodes {{ id body }} }} }}')
            if d["pages"]["nodes"]:
                pid = d["pages"]["nodes"][0]["id"]
                has_body = bool((d["pages"]["nodes"][0]["body"] or "").strip())
        if pid:
            page = {"templateSuffix": suffix, "isPublished": True}
            if not has_body and body:
                page["body"] = body
            log(f"  ~ {title} (Vorlage page.{suffix}{', Inhalt bleibt' if has_body else ''})")
            r = gql("""mutation($id: ID!, $page: PageUpdateInput!) {
              pageUpdate(id: $id, page: $page) { userErrors { field message } } }""", {"id": pid, "page": page})
            if not DRY:
                user_errors(r, "pageUpdate")
        else:
            log(f"  + {title} (/pages/{handle}, Vorlage page.{suffix})")
            r = gql("""mutation($page: PageCreateInput!) {
              pageCreate(page: $page) { page { id } userErrors { field message } } }""",
                    {"page": {"title": title, "handle": handle, "body": body,
                              "templateSuffix": suffix, "isPublished": True}})
            if not DRY:
                user_errors(r, "pageCreate")


# ----------------------------------------------------------------------- 5. Menüs
def resource_ids():
    ids = {}
    if DRY:
        return ids
    for kind in ("pages", "collections", "products"):
        d = gql(f"{{ {kind}(first: 100) {{ nodes {{ id handle }} }} }}")
        for n in d[kind]["nodes"]:
            ids[(kind, n["handle"])] = n["id"]
    return ids


def item(ids, title, kind=None, handle=None, url=None):
    if kind and (kind, handle) in ids:
        t = {"pages": "PAGE", "collections": "COLLECTION", "products": "PRODUCT"}[kind]
        return {"title": title, "type": t, "resourceId": ids[(kind, handle)]}
    if kind == "collections" and handle == "all":
        return {"title": title, "type": "CATALOG"}
    return {"title": title, "type": "HTTP", "url": url or f"/{kind}/{handle}"}


def step_menus():
    print("\n== Menüs ==")
    ids = resource_ids()
    menus = {
        "main-menu": ("Hauptmenü", [
            item(ids, "Kollektion", "collections", "all"),
            item(ids, "Armbänder", "collections", "armbaender"),
            item(ids, "Ketten", "collections", "ketten"),
            item(ids, "Love Charm", "products", "love-charm"),
            item(ids, "Geschenke", "collections", "geschenke"),
            item(ids, "Über LUVIONA", "pages", "ueber-uns"),
            item(ids, "FAQ", "pages", "faq"),
            item(ids, "Kontakt", "pages", "kontakt"),
        ]),
        "service": ("Service", [
            item(ids, "Versand & Zahlung", "pages", "versand-und-zahlung"),
            item(ids, "FAQ", "pages", "faq"),
            item(ids, "Kontakt", "pages", "kontakt"),
            item(ids, "Vertrag widerrufen", "pages", "widerruf"),
            item(ids, "Barrierefreiheit", "pages", "barrierefreiheit"),
            item(ids, "Hinweis zu unseren Bildern", "pages", "hinweis-zu-unseren-bildern"),
        ]),
        "rechtliches": ("Rechtliches", [
            item(ids, "Impressum", "pages", "impressum"),
            item(ids, "Datenschutz", url="/policies/privacy-policy"),
            item(ids, "AGB", url="/policies/terms-of-service"),
            item(ids, "Widerrufsbelehrung", url="/policies/refund-policy"),
            item(ids, "Muster-Widerrufsformular", "pages", "muster-widerrufsformular"),
            item(ids, "Versand & Zahlung", "pages", "versand-und-zahlung"),
        ]),
    }
    existing = {}
    if not DRY:
        d = gql("{ menus(first: 50) { nodes { id handle } } }")
        existing = {n["handle"]: n["id"] for n in d["menus"]["nodes"]}
    for handle, (title, items) in menus.items():
        if handle in existing:
            log(f"  ~ {title} ({handle}) – {len(items)} Einträge")
            r = gql("""mutation($id: ID!, $title: String!, $handle: String!, $items: [MenuItemUpdateInput!]!) {
              menuUpdate(id: $id, title: $title, handle: $handle, items: $items) { userErrors { field message } } }""",
                    {"id": existing[handle], "title": title, "handle": handle, "items": items})
            if not DRY:
                user_errors(r, "menuUpdate")
        else:
            log(f"  + {title} ({handle}) – {len(items)} Einträge")
            r = gql("""mutation($title: String!, $handle: String!, $items: [MenuItemCreateInput!]!) {
              menuCreate(title: $title, handle: $handle, items: $items) { userErrors { field message } } }""",
                    {"title": title, "handle": handle, "items": items})
            if not DRY:
                user_errors(r, "menuCreate")


# ------------------------------------------------------------------------- main
def main():
    global TOKEN
    if not DRY and not TOKEN and STORE and CLIENT_ID and CLIENT_SECRET:
        TOKEN = fetch_token()
    if not DRY and (not STORE or not TOKEN):
        raise SystemExit("SHOPIFY_STORE und entweder SHOPIFY_CLIENT_ID + SHOPIFY_CLIENT_SECRET "
                         "oder SHOPIFY_ADMIN_TOKEN müssen gesetzt sein (siehe Kopf dieser Datei).")
    if not DRY:
        shop = gql("{ shop { name myshopifyDomain primaryDomain { host } } }")["shop"]
        print(f"Shop: {shop['name']} ({shop['myshopifyDomain']}, {shop['primaryDomain']['host']}), API {VERSION}")
    for step in STEPS:
        {"metafields": step_metafields, "products": step_products, "collections": step_collections,
         "pages": step_pages, "menus": step_menus}[step]()
    print("\nFertig.")


if __name__ == "__main__":
    main()
