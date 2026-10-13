# 02 · Wireframes Mobil + Desktop

Legende: `[ ]` Sektion/Block · `(Dawn)` = Standard-Dawn-Sektion · `(LUVIONA)` = eigene Sektion · Reihenfolge = Reihenfolge im Template.

## Globale Elemente

### Header (`sections/header-group.json`)
```
Mobil (≤ 749 px)                         Desktop (≥ 990 px)
┌──────────────────────────────┐         ┌──────────────────────────────────────────────┐
│ Kostenloser Versand · 14 Tage│ (Navy)  │ Kostenloser Versand innerhalb Deutschlands · … │
├──────────────────────────────┤         ├──────────────────────────────────────────────┤
│ ☰        LUVIONA        🔍 🛒 │         │                  LUVIONA (Logo)               │
└──────────────────────────────┘         │  KOLLEKTION  ARMBÄNDER  KETTEN  LOVE CHARM   │
   Drawer-Menü: Kollektion, Armbänder,   │  ÜBER LUVIONA  FAQ  KONTAKT      🔍 👤 🛒    │
   Ketten, Love Charm, Über uns, FAQ,    └──────────────────────────────────────────────┘
   Kontakt; darunter Konto-Link           Sticky beim Hochscrollen, goldene Linie unten
```

### Footer (`sections/footer-group.json`, Navy)
```
┌ Markeninfo + Instagram/TikTok ┬ Service ────────┬ Rechtliches ─────────┬ Newsletter ─────────┐
│ LUVIONA – Court Style …       │ Versand & Zahlung│ Impressum            │ Bleib am Ball       │
│                               │ FAQ              │ Datenschutz          │ [E-Mail-Adresse  →] │
│                               │ Kontakt          │ AGB                  │ DOI-Hinweis         │
│                               │ Größen & Pflege  │ Widerrufsbelehrung   │                     │
│                               │ Barrierefreiheit │ Muster-Widerrufsform.│                     │
│                               │ Hinweis KI-Bilder│ Versand & Zahlung    │                     │
├───────────────────────────────┴──────────────────┴──────────────────────┴─────────────────────┤
│         [ Vertrag widerrufen ]        Cookie-Einstellungen                                    │
│   Alle Preise: Gemäß § 19 UStG wird keine Umsatzsteuer berechnet. Versandkostenfrei in DE.    │
│   © 2026 LUVIONA · Shopify-Richtlinienlinks · Zahlungsarten-Logos                             │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```
Max. 2 Klicks zu jedem Rechtstext: Footer-Link (1 Klick) von jeder Seite.

---

## 1. Startseite (`templates/index.json`)

```
Mobil                                     Desktop
┌─────────────────────────┐               ┌──────────────────────────────────────────────┐
│ [Hero-Bild Tragebild]   │               │ [Hero-Bild 16:10, Text links in Navy-Box]     │
│ COURT STYLE ACCESSORIES │ (Text unter   │  COURT STYLE ACCESSORIES                      │
│ Dein Spiel. Dein Style. │  dem Bild)    │  Dein Spiel. Dein Style.                      │
│ [Kollektion entdecken]  │               │  [Kollektion entdecken] [Love Charm]          │
│ [Love Charm]            │               └──────────────────────────────────────────────┘
├─────────────────────────┤               ┌────────┬────────┬────────┬────────┐ (LUVIONA Vertrauensleiste)
│ 🚚 Versand │ 📍 aus DE  │               │ 🚚     │ 📍     │ ↩︎      │ 🎁     │
│ ↩︎ 14 Tage │ 🎁 Geschenk│               └────────┴────────┴────────┴────────┘
├─────────────────────────┤               ┌──────────────────────────────────────────────┐
│ Die Kollektion          │ (Dawn         │ Die Kollektion · Intro-Text                   │
│ [Karte] [Karte]  swipe→ │  featured-    │ [Karte] [Karte] [Karte]                       │
│ Preis · versandkostenfrei│ collection)  │ [Karte] [Karte] [Karte]   [Alle ansehen]      │
├─────────────────────────┤               ├──────────────────────────────────────────────┤
│ [Bild Satin/Travertin]  │ (Dawn image-  │ [Bild]            ÜBER LUVIONA                │
│ ÜBER LUVIONA            │  with-text,   │                   Für alle, die den Court …   │
│ Für alle, die den Court…│  Schema 4)    │                   [Unsere Geschichte]         │
├─────────────────────────┤               ├──────────────────────────────────────────────┤
│ KOMBINIEREN             │ (LUVIONA      │ KOMBINIEREN · Schöner zu zweit                │
│ [Armband] + [Kette]     │  Sets)        │ ┌ Match Point Set ┐  ┌ Court Classic + Charm ┐│
│ Zusammen 69,80 €        │               │ │ [P1] + [P2]     │  │ [P1] + [P2]           ││
│ [Court Classic + Charm] │               │ └─────────────────┘  └───────────────────────┘│
├─────────────────────────┤               ├──────────────────────────────────────────────┤
│ GESCHENKIDEE (Navy)     │ (Dawn rich-   │ GESCHENKIDEE · Für die Tennispartnerin …      │
│ Für die Tennispartnerin…│  text)        │ [Geschenke entdecken]                         │
├─────────────────────────┤               ├──────────────────────────────────────────────┤
│ INSTAGRAM               │ (LUVIONA      │ INSTAGRAM · Zeig uns deinen Court Style       │
│ [img][img]              │  Instagram)   │ [img][img][img][img]      [@luviona.de]       │
│ [img][img] [@luviona.de]│               │                                               │
├─────────────────────────┤               ├──────────────────────────────────────────────┤
│ Bleib am Ball (Satin)   │ (Dawn         │ Bleib am Ball · Text · [E-Mail →] · DOI-Hinweis│
│ [E-Mail-Adresse →]      │  newsletter)  │                                               │
└─────────────────────────┘               └──────────────────────────────────────────────┘
```

## 2. Shop / Kollektion (`templates/collection.json`)

```
Mobil                                   Desktop
┌───────────────────────────┐           ┌───────────────────────────────────────────────┐
│ Kollektion · Beschreibung │           │ Kollektion · Beschreibung                      │
│ [Filter ▾]   [Sortieren ▾]│ Drawer    │ Produktart ▾  Metallfarbe ▾  Farbe ▾  Preis ▾  │ horizontal
│ 12 Produkte               │           │                                  Sortieren ▾   │
│ [Karte]     [Karte]       │           │ [Karte]      [Karte]      [Karte]              │
│ Name                      │           │ Name                                           │
│ 34,90 €                   │           │ 34,90 €                                        │
│ versandkostenfrei · § 19  │           │ versandkostenfrei in Deutschland · Gemäß § 19 … │
│ [Karte]     [Karte]       │           │ [Karte]      [Karte]      [Karte]              │
├───────────────────────────┤           ├───────────────────────────────────────────────┤
│ Vertrauensleiste (4)      │           │ Vertrauensleiste (4)                           │
└───────────────────────────┘           └───────────────────────────────────────────────┘
```
Filter (Shopify Search & Discovery): Produktart (Armband / Kette / Taschen-Charm / Kosmetik), Metallfarbe (Gold / Silber), Farbe, Preis. Einrichtung siehe `05-shopify-einrichtung.md`.

## 3. Produktseite (`templates/product.json`, `product.kosmetik.json`)

```
Mobil                                       Desktop
┌─────────────────────────────┐             ┌──────────────────────────┬──────────────────────────┐
│ [Galerie, swipe, 1/5]       │             │ [Hauptbild]              │ Court Classic – Grün/Weiß │
│ Abbildung KI-generiert …    │             │ [thumb][thumb][thumb]    │ 34,90 €                   │
│ Court Classic – Grün/Weiß   │             │ Abbildung KI-generiert.  │ versandkostenfrei in DE · │
│ 34,90 €                     │             │ Das Originalprodukt …    │ Gemäß § 19 UStG …         │
│ versandkostenfrei · § 19    │             │ (Lightbox-Zoom)          │ 🚚 Lieferzeit 2–4 Werktage │
│ 🚚 Lieferzeit 2–4 Werktage  │             │                          │ Farbe: ● ● ●  (Swatches)  │
│ Farbe ● ● ● ● ●  (Swatches) │             │                          │ Anzahl [− 1 +]            │
│ Anzahl [− 1 +]              │             │                          │ [ IN DEN WARENKORB ]      │
│ [ IN DEN WARENKORB ]        │             │                          │ [ Express-Zahlung ]       │
│ [ Express-Zahlung ]         │             │                          │ 🎁 Perfekt als Geschenk … │
│ 🎁 Perfekt als Geschenk …   │             │                          │ Beschreibung              │
│ Beschreibung                │             │                          │ ▸ Material & Maße         │
│ ▸ Material & Maße           │             │                          │ ▸ Pflegehinweise          │
│ ▸ Pflegehinweise            │             │                          │ ▸ Hersteller & Sicherheit │
│ ▸ Hersteller & Sicherheit   │             │                          │ ▸ Inhaltsstoffe (nur Gloss)│
│ ▸ Inhaltsstoffe (nur Gloss) │             │                          │ ▸ Versand & Widerruf      │
│ ▸ Versand & Widerruf        │             └──────────────────────────┴──────────────────────────┘
├─────────────────────────────┤             ┌───────────────────────────────────────────────────────┐
│ Passt dazu  [Karte][Karte]  │             │ Passt dazu            [Karte] [Karte] [Karte]          │
│ Das könnte dir … [ ][ ]     │             │ Das könnte dir auch gefallen [ ] [ ] [ ] [ ]           │
│ Vertrauensleiste            │             │ Vertrauensleiste (inkl. „Sichere Zahlung“)             │
└─────────────────────────────┘             └───────────────────────────────────────────────────────┘
```
Bewertungen: Block ist vorhanden (Dawn `rating`), wird **nicht** ins Template aufgenommen, bis echte Bewertungen + Echtheitshinweis vorliegen.

## 4. Warenkorb & Checkout (`templates/cart.json` + Shopify-Checkout)

```
Warenkorb (Theme)                              Checkout (Shopify, konfiguriert per „Sprache bearbeiten“)
┌──────────────────────────────────────┐       ┌──────────────────────────────────────────────┐
│ Dein Warenkorb        Weiter stöbern │       │ Kontakt (Gastbestellung, E-Mail)             │
│ [img] Court Classic Grün  34,90 €    │       │ Lieferadresse (nur Deutschland)              │
│       Anzahl [− 1 +]  🗑              │       │ Versand: Kostenloser Versand (0,00 €)        │
│ Notiz / Grußkartentext [________]    │       │ Zahlung: Shopify Payments / PayPal / Klarna  │
├──────────────────────────────────────┤       │ Rechnungsadresse                              │
│ NOCH DAZU?  [img] Love Charm 27,90 € │       │ ───────────── Übersicht ─────────────         │
│  Farbe [Taupe ▾]  [In den Warenkorb] │       │ Artikel, Merkmale, Gesamtpreis, Lieferzeit   │
├──────────────────────────────────────┤       │ Links: AGB · Widerrufsbelehrung · Datenschutz │
│ Gesamtsumme              34,90 €     │       │ Hinweis: Gemäß § 19 UStG keine USt.           │
│ Alle Preise: Gemäß § 19 UStG … ·     │       │ [ ZAHLUNGSPFLICHTIG BESTELLEN ]               │
│ Versandkostenfrei in Deutschland ·   │       └──────────────────────────────────────────────┘
│ Lieferzeit 2–4 Werktage              │       Keine vorangekreuzten Checkboxen, Newsletter
│ [ ZUR KASSE ]  [Express-Buttons]     │       separat & freiwillig, Korrektur jederzeit möglich.
└──────────────────────────────────────┘
```

## 5. Über LUVIONA (`page.ueber-uns.json`) – Seiteninhalt → Bild/Text „Wie alles begann“ → Bild/Text „Unser Anspruch“ (Satin) → Vertrauensleiste

## 6. FAQ (`page.faq.json`) – Seitentitel → Akkordeon (9 Fragen, erste offen) → „Noch Fragen?“ mit Kontakt-Button

## 7. Kontakt (`page.kontakt.json`) – Seitentitel + Text (Adresse/E-Mail) → Formular: Name (optional) · E-Mail* · Nachricht* → Datenschutzhinweis → [Nachricht senden]

## 8. Vertrag widerrufen (`page.widerruf.json`)
```
Schritt 1: Deine Angaben (Name*, E-Mail*, Anschrift) · Deine Bestellung (Bestellnummer*, Datum, Artikel)
           Datenschutzhinweis · [Weiter zur Bestätigung]
Schritt 2: „Bitte prüfe deine Angaben“ (Zusammenfassung) · Erklärungstext
           [Zurück]  [WIDERRUF BESTÄTIGEN]
Schritt 3: „Dein Widerruf ist bei uns eingegangen.“ + nächste Schritte (+ automatische E-Mail, siehe 05)
```

## 9. Rechtsseiten (`page.rechtstext.json` / Shopify-Richtlinien) – schmale Textspalte, Platzhalter-Hinweis nur im Editor

## 10. 404 – „FEHLER 404 · Diese Seite ist nicht im Spiel“ · Ornament · Text · [Weiter stöbern]
