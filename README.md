# LUVIONA – Court Style Accessories · Shopify-Theme

Mobil-optimiertes Shopify-Theme (Online Store 2.0) für den Schmuck- und Bag-Charm-Shop **LUVIONA**, ausgelegt auf den Verkauf von Deutschland an Endkund:innen in Deutschland (B2C) – rechtssicher nach deutschem und EU-Recht (Stand Oktober 2026). Basis: [Shopify Dawn 16.0.0](https://github.com/Shopify/dawn) (MIT-Lizenz, siehe `LICENSE.md`).

## Lieferumfang

| Nr. | Deliverable | Wo |
|---|---|---|
| 1 | Design-Konzept (Moodboard, Farb-/Typo-System, Komponenten) | `docs/01-design-konzept.md` |
| 2 | Wireframes Mobil + Desktop für alle Seiten | `docs/02-wireframes.md` |
| 3 | Ausgearbeitete Startseite, Produktseite, Warenkorb + Checkout-Konfiguration | `templates/index.json`, `templates/product*.json`, `templates/cart.json`, `docs/06-checkout-und-emails.md` |
| 4 | Texte (Startseite, Produkte, Über uns, FAQ, Systemtexte – Deutsch, du-Form) | `docs/03-texte.md`, in den Templates hinterlegt, `docs/produkte-import.csv` |
| 5 | Rechts-Checkliste + Platzhalterliste | `docs/04-rechts-checkliste.md` |
| + | Shopify-Einrichtung Schritt für Schritt (Markt, Steuern, Checkout-Texte, Metafelder, Cookie, Domain/DNS, Apps) | `docs/05-shopify-einrichtung.md` |
| + | E-Mail-Ergänzung Bestellbestätigung (§ 19 UStG, Widerrufsbelehrung, AGB) | `docs/email/bestellbestaetigung-zusatz.liquid` |

## Was das Theme gegenüber Dawn ergänzt

**Design**
- Farbsystem Navy `#0B1C3D` · Champagner-Gold `#C9A27A` · Creme `#F6F0E6` + Akzente (Court-Grün, Bordeaux, Royal-Navy), 6 Farbschemata, Kontraste WCAG 2.1 AA geprüft (`assets/luviona.css`).
- Lokal gehostete Schriften Cormorant Garamond + Jost (variable WOFF2, OFL) – kein Google-Fonts-Abruf (`assets/luviona-fonts.css`, Theme-Einstellung „Eigene Schriftdateien lokal laden“).
- Goldene Trennlinien, Herz/Schläger-Ornament, Versalien-Navigation mit Spationierung, Hover in Gold, sichtbare Fokuszustände.

**Rechtliches (im Theme umgesetzt)**
- Pflichtangaben direkt am Preis: „versandkostenfrei in Deutschland · Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.“ auf Produktseite, Karten, Warenkorb, Drawer, Footer – umschaltbar auf Regelbesteuerung („inkl. MwSt.“) per Theme-Einstellung. Shopify-Standardtexte „inkl. Steuern“ entfernt.
- Konkrete Lieferzeit als Produktblock (global + Metafeld-Override).
- Akkordeons **Hersteller & Produktsicherheit (GPSR)** und **Inhaltsstoffe & Kosmetik-Angaben** (INCI, Füllmenge + Grundpreis, PAO, Verantwortliche Person, Warnhinweise, Hygiene-Hinweis) aus Metafeldern `luviona.*`; Platzhalter sind im Editor rot markiert.
- KI-Bild-Hinweis unter jeder Produktgalerie (EU AI Act Art. 50) + Seite „Hinweis zu unseren Bildern“.
- **Widerrufsbutton**: Footer-Button „Vertrag widerrufen“ → zweistufiges Online-Formular mit „Widerruf bestätigen“ (`sections/luviona-widerruf-form.liquid`).
- **Consent-Banner** auf Basis der Shopify Customer Privacy API: „Alle ablehnen“ gleichwertig zu „Alle akzeptieren“, keine Vorauswahl, nicht modal, Link „Cookie-Einstellungen“ im Footer (`snippets/luviona-consent.liquid`, `assets/luviona-consent.js`).
- Kontaktformular mit nur E-Mail + Nachricht als Pflichtfelder und Datenschutzhinweis; Newsletter mit Double-Opt-in-Hinweistext.
- Keine Fake-Verknappung, keine Superlative, Add-on ohne Vorauswahl, Gastbestellung.

**Conversion**
- Vertrauensleiste, Set-Vorschläge („Armband + Kette“, „Armband + Love Charm“), Warenkorb-Add-on „Noch dazu? Love Charm“, „Passt dazu“-Empfehlungen (Ergänzungsprodukte), Geschenkhinweis, Instagram-Bereich ohne Embed.

## Neue/geänderte Dateien (Überblick)
```
assets/luviona.css · luviona-fonts.css · luviona-*.woff2 · luviona-consent.js · luviona-widerruf.js · icon-shield.svg
snippets/luviona-price-note · luviona-icon · luviona-ornament · luviona-metafield · luviona-ai-notice
         luviona-consent · luviona-cookie-link · luviona-block-gpsr · luviona-block-kosmetik
sections/luviona-trust-bar · luviona-instagram · luviona-sets · luviona-cart-addon · luviona-widerruf-form
         (geändert) main-product · footer · contact-form · newsletter · main-404 · main-cart-footer · related-products · featured-product
templates/index · product · product.kosmetik · cart · collection · page.faq · page.ueber-uns · page.kontakt · page.widerruf · page.rechtstext
config/settings_schema.json (LUVIONA-Gruppen) · settings_data.json (Preset „LUVIONA“)
locales/de.default.json (Deutsch als Standard, neue Schlüssel `luviona.*`)
docs/ (Deliverables, Produkt-CSV, Lizenzen)
```

## Entwicklung
```bash
npm i -g @shopify/cli            # einmalig
shopify theme dev --store luviona.myshopify.com   # lokale Vorschau
shopify theme check               # Lint (CI führt das bei jedem Push aus)
shopify theme push                # ins Theme hochladen
```
Dawn-Updates können weiterhin per `git pull upstream main` eingespielt werden (Upstream: `https://github.com/Shopify/dawn.git`); Konflikte sind in den oben genannten geänderten Dateien zu erwarten.

## Lizenz
Theme-Code: MIT (Dawn, Shopify Inc.) – siehe `LICENSE.md`. Schriften: SIL Open Font License 1.1 – siehe `docs/lizenzen/`. Marken- und Textinhalte: © LUVIONA GbR.

## Shop automatisch einrichten (Produkte, Bilder, Seiten, Menüs)

`scripts/shopify_setup.py` legt über die Shopify Admin API alle Produkte inkl. Bilder und Varianten, die Metafelddefinitionen `luviona.*`, vier Kollektionen, alle Seiten mit den richtigen Vorlagen sowie Hauptmenü, Service- und Rechtliches-Menü an. Das Skript ist mehrfach ausführbar und überschreibt keine bereits befüllten Seiteninhalte. Benötigt `SHOPIFY_STORE` (myshopify-Adresse) und `SHOPIFY_ADMIN_TOKEN` (Admin-API-Token mit read/write für products, content, online_store_navigation, publications).

Startseite und „Über LUVIONA“ zeigen die KI-Bilder bereits ohne Upload: Sie liegen als WebP in `assets/` und werden genutzt, solange im Theme-Editor kein eigenes Bild gewählt ist – jeweils mit dem Hinweis „Abbildung KI-generiert“.
