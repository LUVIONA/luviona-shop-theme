# 05 · Shopify-Einrichtung (Schritt für Schritt)

## 1. Theme hochladen
1. Repository als ZIP (`Code → Download ZIP`) oder per Shopify CLI (`shopify theme push`) in **Onlineshop → Themes** hochladen.
2. Theme „LUVIONA – Court Style Accessories“ anpassen → Theme-Einstellungen prüfen (Logo, Social-Links, LUVIONA-Gruppen).
3. Voraussetzungen vor dem Veröffentlichen: Produkte, Kollektionen, Seiten, Menüs, Richtlinien (unten).

## 2. Sprache, Markt, Währung, Versand
- **Einstellungen → Sprachen:** Deutsch als Standardsprache (Theme-Locale `de.default.json`); keine weiteren Sprachen veröffentlichen.
- **Einstellungen → Märkte:** nur **Deutschland** (Primärmarkt), EUR. Keine internationalen Märkte aktivieren.
- **Einstellungen → Versand und Zuliefern:** Versandprofil „Allgemein“ → Zone **Deutschland** → eine Rate: *Kostenloser Versand (2–4 Werktage)*, 0,00 €. Keine weiteren Zonen.
- **Einstellungen → Standorte:** Versandstandort in Deutschland (GbR-Anschrift).

## 3. Steuern (Kleinunternehmer § 19 UStG)
- **Einstellungen → Steuern und Zölle:** Region Deutschland → **keine** Steuererhebung (Steuersatz 0 %, keine Registrierung eintragen). „Alle Preise inkl. Steuern anzeigen“ **deaktivieren**.
- Produkte: „Steuer auf dieses Produkt erheben“ kann aktiv bleiben (0 %).
- Theme: **Theme-Einstellungen → LUVIONA – Preise & Steuern → Steuermodus: Kleinunternehmer.**
- Später Regelbesteuerung: Steuer 19 % aktivieren, „Preise inkl. Steuern“ an, Theme-Steuermodus auf „Regelbesteuerung“ (zeigt „inkl. MwSt.“), Rechnungs-App umstellen, Checkout-Texte zurücksetzen.

## 4. Checkout-Texte (Sprache bearbeiten)
**Onlineshop → Themes → … → Standard-Theme-Inhalt bearbeiten** (bzw. *Einstellungen → Checkout → Checkout-Sprache anpassen*), Bereich **Checkout & System**:

| Suchbegriff | Standard | Neu |
|---|---|---|
| „Jetzt bezahlen“ / „Bestellung abschließen“ / „Pay now“ (Button Zahlung) | Jetzt bezahlen | **Zahlungspflichtig bestellen** |
| „Jetzt kaufen“ (Express-Buttons) | Jetzt kaufen | belassen oder „Jetzt kaufen“ (zulässig) |
| „Inkl. Steuern“, „Steuern inklusive“, „inkl. MwSt.“ (Zusammenfassung, Steuerzeile) | Inkl. Steuern | leer bzw. „Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.“ |
| „Steuern“ (Zeile in der Übersicht) | Steuern | wird bei 0 % nicht angezeigt; Text leer lassen |
| „Versand“ Rate | – | „Kostenloser Versand (2–4 Werktage)“ (aus Versandeinstellung) |

- **Einstellungen → Checkout:** Kundenkonten „optional“ (Gastbestellung), Marketing-Optionen: E-Mail-Newsletter-Checkbox **nicht vorausgewählt** (besser deaktivieren), SMS aus, Adressautovervollständigung ok.
- **Einstellungen → Checkout → Richtlinien im Checkout-Footer:** werden automatisch aus *Einstellungen → Richtlinien* verlinkt.
- Zusätzlicher Hinweistext im Checkout: *Einstellungen → Checkout → Branding/Anpassen* → Footer-Text (Checkout-Editor, falls verfügbar): „Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.“

## 5. Richtlinien & Seiten
**Einstellungen → Richtlinien** (Texte aus dem Abmahnschutz-Paket einfügen):
- Rückgabe- und Erstattungsrichtlinie → **Widerrufsbelehrung** (+ Muster-Widerrufsformular am Ende)
- Datenschutzerklärung
- Allgemeine Geschäftsbedingungen
- Versandrichtlinie → „Versand & Zahlung“-Kurzfassung (optional; Theme verlinkt sonst die Seite)
- Impressum/Rechtlicher Hinweis (falls im Admin verfügbar) – sonst Seite

**Onlineshop → Seiten** (Handle = URL, Template rechts in der Seitenbearbeitung wählen):

| Titel | Handle | Template |
|---|---|---|
| Impressum | `impressum` | page.rechtstext |
| Muster-Widerrufsformular | `muster-widerrufsformular` | page.rechtstext |
| Versand & Zahlung | `versand-und-zahlung` | page.rechtstext |
| Hinweis zu unseren Bildern | `hinweis-zu-unseren-bildern` | page.rechtstext |
| Barrierefreiheit | `barrierefreiheit` | page.rechtstext |
| Vertrag widerrufen | `widerruf` | **page.widerruf** |
| Über LUVIONA | `ueber-uns` | page.ueber-uns |
| FAQ | `faq` | page.faq |
| Kontakt | `kontakt` | page.kontakt |

Danach **Theme-Einstellungen → LUVIONA – Rechtliches/Preise:** Seiten „Vertrag widerrufen“, „Versand & Zahlung“, „Hinweis zu unseren Bildern“ zuweisen (Vorbelegung über Handles ist bereits gesetzt).

## 6. Navigation (Onlineshop → Navigation)
- **Hauptmenü** (`main-menu`): Kollektion → `/collections/all` · Armbänder → `/collections/armbaender` · Ketten → `/collections/ketten` · Love Charm → `/products/love-charm` · Über LUVIONA · FAQ · Kontakt
- **Service** (Handle `service`): Versand & Zahlung · FAQ · Kontakt · Größen & Pflege (→ FAQ) · Barrierefreiheit · Hinweis zu unseren Bildern
- **Rechtliches** (Handle `rechtliches`): Impressum · Datenschutz (`/policies/privacy-policy`) · AGB (`/policies/terms-of-service`) · Widerrufsbelehrung (`/policies/refund-policy`) · Muster-Widerrufsformular · Versand & Zahlung
- **Kundenkonto-Hauptmenü** (`customer-account-main-menu`): + „Vertrag widerrufen“ → `/pages/widerruf`
- Footer-Blöcke sind auf die Menüs `service` und `rechtliches` vorkonfiguriert (`sections/footer-group.json`).

## 7. Kollektionen & Filter
- Kollektionen: `armbaender` (Produkttyp = Armband), `ketten` (Kette), `taschen-charms` (Kosmetik/Taschen-Charm), optional `geschenke` (Tag `geschenk`). Automatische Bedingungen über Produkttyp/Tag.
- **App „Shopify Search & Discovery“** (kostenlos) installieren → Filter: Produktart, Preis, Metallfarbe (Metafeld oder Tag `gold`/`silber`), Farbe (Variantenoption bei Charm, Tag bei Armbändern). Ergänzungsprodukte („Passt dazu“) je Produkt pflegen: Armbänder → Love Charm + Kette; Charm → Armbänder.
- Kollektionssortierung: manuell (Hero-Produkt zuerst).

## 8. Produkte & Metafelder
- Import: `docs/produkte-import.csv` (Produkte → Importieren). Preise, Varianten, Tags, SEO sind enthalten; Bilder und Metafelder danach pflegen.
- **Einheitspreis** (Love Charm): Produkt → Variante → „Einheitspreis anzeigen“ → Gesamtmenge **[x] ml**, Basis 1 ml.
- **Metafelddefinitionen anlegen:** Einstellungen → Benutzerdefinierte Daten → Produkte → Definition hinzufügen, Namespace und Schlüssel exakt wie unten (Zugriff „Storefront“ lesen):

| Name | Namespace.Schlüssel | Typ | Verwendung |
|---|---|---|---|
| Lieferzeit | `luviona.lieferzeit` | Einzeiliger Text | überschreibt Theme-Lieferzeit |
| Material & Maße | `luviona.material` | Rich Text | Akkordeon |
| Pflegehinweise | `luviona.pflege` | Rich Text | Akkordeon (optional, Standardtext im Block) |
| Lieferumfang / Größe / Hinweise | `luviona.lieferumfang`, `luviona.groesse`, `luviona.hinweise` | Rich Text | optionale Akkordeons |
| Hersteller – Name | `luviona.hersteller_name` | Einzeiliger Text | GPSR |
| Hersteller – Anschrift | `luviona.hersteller_anschrift` | Mehrzeiliger Text | GPSR |
| Hersteller – Kontakt | `luviona.hersteller_kontakt` | Einzeiliger Text | GPSR |
| EU-Verantwortliche (GPSR) | `luviona.eu_verantwortliche` | Mehrzeiliger Text | GPSR |
| Produktkennung | `luviona.produktkennung` | Einzeiliger Text | GPSR (sonst SKU) |
| Warnhinweise | `luviona.warnhinweise` | Mehrzeiliger Text | GPSR |
| Materialkonformität (REACH) | `luviona.material_konformitaet` | Mehrzeiliger Text | GPSR |
| KI-Bilder | `luviona.ki_bilder` | Wahr/Falsch | `false` blendet KI-Hinweis aus |
| Verwendungszweck | `luviona.verwendungszweck` | Einzeiliger Text | Kosmetik |
| Füllmenge | `luviona.fuellmenge` | Einzeiliger Text („3 ml“) | Kosmetik |
| INCI | `luviona.inci` | Mehrzeiliger Text | Kosmetik |
| PAO | `luviona.pao` | Einzeiliger Text („12M“) | Kosmetik |
| MHD | `luviona.mhd` | Einzeiliger Text | Kosmetik (alternativ zu PAO) |
| Chargen-Hinweis | `luviona.charge_hinweis` | Einzeiliger Text | Kosmetik |
| Verantwortliche Person (KosmetikVO) | `luviona.kosmetik_verantwortliche` | Mehrzeiliger Text | Kosmetik |
| Allergene | `luviona.allergene` | Mehrzeiliger Text | Kosmetik |
| Kosmetik-Warnhinweise | `luviona.kosmetik_warnhinweise` | Mehrzeiliger Text | Kosmetik |

- Love Charm: Produkttyp **Kosmetik**, Theme-Template **product.kosmetik**, Varianten = Farben (Taupe, Rosé, Lavendel, Olive, Creme) mit Farb-Swatches (Option „Farbe“ → Swatch-Werte in den Kategorie-Metafeldern oder Bild je Variante).
- SKU je Variante vergeben (Produktkennung GPSR).

## 9. Cookie-Banner & Tracking
- **Einstellungen → Kundendatenschutz:** Cookie-Banner → Regionen **EU/EWR, Deutschland** → „Datenerhebung vor Einwilligung einschränken“. **Entweder** Shopifys Banner aktivieren (dann Theme-Banner in den Theme-Einstellungen ausschalten) **oder** das Theme-Banner nutzen (Standard; Shopify-Banner deaktiviert lassen, damit nicht zwei erscheinen).
- Pixel: **Einstellungen → Kundenereignisse** → Meta/TikTok/Google-Pixel nur als App-Pixel oder Custom Pixel mit **Datenschutzeinstellung „Erforderliche Einwilligung: Marketing/Analyse“**. Niemals Pixel-Code ins Theme kopieren.
- Analyse: Shopify-Berichte sind serverseitig; alternativ Plausible/Matomo (EU-Hosting, cookielos) über Custom Pixel mit Consent.

## 10. Widerrufsbutton – E-Mail-Fluss
- Das Formular sendet über Shopifys Kontaktformular an die **Absender-/Kundenservice-E-Mail** (Einstellungen → Benachrichtigungen → Absender). Richte bei united-domains eine Weiterleitungsregel ein: Betreff enthält „Widerruf über das Online-Formular“ → `widerruf@luviona.de`.
- **Pflicht-Eingangsbestätigung** an die Kundin (automatisch, dauerhafter Datenträger): Shopify sendet beim Kontaktformular keine Kopie an die Absenderin. Optionen: (a) Formular-App mit Autoresponder (z. B. „Hulk Form Builder“, „Powerful Contact Form Builder“, „Improved Contact Form“ – EU-Datenverarbeitung/AVV prüfen, in Datenschutzerklärung aufnehmen) und deren Formular als App-Block auf `page.widerruf` statt des Theme-Formulars; (b) Mail-Autoresponder bei united-domains auf `widerruf@luviona.de`, der eine Bestätigung mit Datum/Uhrzeit sendet (nur, wenn das Formular direkt an diese Adresse geht). Bis dahin: manuell, unverzüglich bestätigen.
- Bestellbestätigung ebenfalls von `bestellung@luviona.de` (Absender in Shopify verifizieren, DKIM-Einträge bei united-domains setzen).

## 11. Domain & E-Mail (united-domains)
- Shopify: **Einstellungen → Domains → Vorhandene Domain verbinden** `luviona.de`. Bei united-domains setzen: **A-Record `@` → 23.227.38.65**, **CNAME `www` → shops.myshopify.com** (Werte in der Shopify-Anleitung prüfen). **MX-Einträge nicht ändern** – Mail bleibt bei united-domains.
- In Shopify `luviona.de` als **primäre Domain**, `www.luviona.de` leitet automatisch weiter; SSL wird automatisch ausgestellt (bis 48 h).
- Absenderdomain: Einstellungen → Benachrichtigungen → Absender-E-Mail `bestellung@luviona.de` → „Authentifizieren“ → die angezeigten DKIM-CNAME-Einträge bei united-domains anlegen. SPF: `v=spf1 include:shops.shopify.com include:<united-domains-SPF> ~all` (SPF von united-domains ergänzen, nicht ersetzen).
- Aliase: info@, bestellung@, widerruf@, datenschutz@ → ein Postfach.

## 12. Zahlung
- Shopify Payments aktivieren (Kreditkarte, Apple Pay, Google Pay, Klarna, Shop Pay) + PayPal Express. Footer-Logos erscheinen automatisch (`shop.enabled_payment_types`).
- Express-Buttons („Jetzt kaufen“) auf der Produktseite sind aktiv (`show_dynamic_checkout`) – sie führen in den regulären Checkout mit Bestellübersicht; bei Bedarf im Theme-Editor abschalten.

## 13. Apps (sparsam, jede in die Datenschutzerklärung)
| Zweck | Empfehlung | Hinweis |
|---|---|---|
| Filter & Empfehlungen | Shopify Search & Discovery | kostenlos, Shopify-eigen |
| Rechnungen Kleinunternehmer | z. B. „Sufio“, „Order Printer Pro“ oder „easybill“/„sevdesk“-Anbindung | § 19-Hinweis, fortlaufende Nummer, kein USt-Ausweis, EU-Datenverarbeitung prüfen |
| Widerruf-Autoresponder | Formular-App (s. 10) | AVV + DSGVO |
| Newsletter | Shopify Email (DOI aktivieren) oder EU-Anbieter (z. B. CleverReach, rapidmail, Brevo) | Double-Opt-in, Abmeldelink |
| Consent | Theme-Banner (ohne App) oder Shopify-Banner; Alternativ DSGVO-App (z. B. Consentmo, Pandectes) mit Script-Blocking | nicht doppelt |
| Bewertungen (später) | z. B. Judge.me/Shopify-eigene Produktbewertungen | Echtheitsprüfung dokumentieren (§ 5b UWG) |

## 14. SEO & Technik
- Shopify erzeugt `sitemap.xml` und `robots.txt` automatisch; Startseiten-Meta-Titel/-Beschreibung unter *Onlineshop → Einstellungen*: „LUVIONA – Court Style Accessories | Tennis-Schmuck & Bag Charms“ / „Tennis-Armbänder, Schläger-Ketten und der Love Charm mit Lipgloss. Entworfen und versandkostenfrei versendet aus Deutschland.“
- Strukturierte Daten: Produkt (Product/Offer mit Preis, Verfügbarkeit, Versandland über Shopify), Organisation und Breadcrumbs liefert Dawn (`product | structured_data`, Header-JSON-LD). Shop-Name/Logo in den Einstellungen pflegen.
- Google Search Console per DNS-TXT bei united-domains verifizieren.
- Performance: Lighthouse mobil nach dem Hochladen prüfen (Ziel LCP < 2 s): Hero-Bild ≤ 250 KB, Produktbilder ≤ 300 KB.
