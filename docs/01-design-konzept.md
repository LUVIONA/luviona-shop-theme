# 01 · Design-Konzept – LUVIONA Court Style Accessories

> Stand: Oktober 2026 · Shopify Online Store 2.0 · Basis: Dawn 16.0.0

## 1. Moodboard (in Worten)

| Thema | Bild im Kopf | Umsetzung im Theme |
|---|---|---|
| Country-Club & Sandplatz | Rote Asche, weiße Linien, Sonne am späten Nachmittag | Creme-Hintergrund, Navy-Header/Footer, Champagner-Linien als „Court-Linien“ |
| Old Money / Tennis-Core | Perlen, Satin, Travertin, gebundene Kordeln | Satin-Verlauf (scheme-4), zurückhaltende Texturklasse `luviona-texture`, viel Weißraum |
| Feminin, nicht verspielt | Serifen-Headlines, luftige Versalien mit Spationierung | Cormorant Garamond + Jost (Versalien, 18 % Letter-Spacing) |
| Logo-Zitat | Herz mit Schläger | Ornament `snippets/luviona-ornament.liquid` als Trenner (404, Seiten, Sektionen) |
| Produktfarben | Court-Grün, Bordeaux, Royal-Navy, Tennisball-Gelbgrün | Akzent-Farbschemata 5/6, Gelbgrün nur als Hover/Badge-Akzent (sparsam) |

## 2. Farbsystem

| Token | Hex | Verwendung | Kontrast geprüft (WCAG 2.1 AA) |
|---|---|---|---|
| Navy `--luviona-navy` | `#0B1C3D` | Header, Footer, Buttons, Text auf Creme | 14,9 : 1 auf Creme ✅ |
| Champagner-Gold `--luviona-gold` | `#C9A27A` | Linien, Ornamente, Button-Hover-Fläche, Text **nur auf Navy** | 7,2 : 1 auf Navy ✅ · 2,1 : 1 auf Creme ❌ (deshalb kein Fließtext in Gold auf Creme) |
| Gold dunkel `--luviona-gold-dark` | `#7A5C33` | Gold-Textakzente (Eyebrows, Icons, Links) auf Creme/Weiß | 5,4 : 1 auf Creme ✅ |
| Gold hell `--luviona-gold-light` | `#E8D9BF` | Satin-Flächen (scheme-4), Trennflächen | Text Navy 12,1 : 1 ✅ |
| Creme/Elfenbein `--luviona-creme` | `#F6F0E6` | Haupthintergrund, Text auf Navy | 14,9 : 1 auf Navy ✅ |
| Court-Grün | `#1F4D3A` | Akzentschema 5 (z. B. Banner), Produktfarbe | 8,5 : 1 mit Creme ✅ |
| Bordeaux | `#7A1F2B` | Sale-Badge (Schema 6), Platzhalter-Markierung | 9,0 : 1 mit Creme ✅ |
| Royal-Navy | `#24357A` | Produkt-Swatch | 9,9 : 1 mit Creme ✅ |
| Tennisball | `#C8DC3C` | nur sparsam: Badge/Hover-Akzent | Navy-Text 11,0 : 1 ✅ |

**Farbschemata im Theme-Editor** (`config/settings_data.json`):

| Schema | Hintergrund | Text | Button | Einsatz |
|---|---|---|---|---|
| scheme-1 „Creme“ | #F6F0E6 | Navy | Navy / Creme | Standard für alle Inhaltssektionen |
| scheme-2 „Weiß“ | #FFFFFF | Navy | Navy / Creme | Consent-Banner, Karten, Drawer |
| scheme-3 „Navy“ | #0B1C3D | Creme | Gold / Navy | Announcement-Bar, Hero-Textbox, Footer, Geschenk-Sektion |
| scheme-4 „Champagner-Satin“ | Verlauf #EFE4D2 → #E6D7BF | Navy | Navy / Creme | Markengeschichte, Newsletter |
| scheme-5 „Court-Grün“ | #1F4D3A | Creme | Creme / Grün | Kampagnen-Banner |
| scheme-6 „Bordeaux“ | #7A1F2B | Creme | Creme / Bordeaux | Sale-Badge |

## 3. Typografie (lokal gehostet)

| Rolle | Schrift | Datei (assets/) | Gewicht | Stil |
|---|---|---|---|---|
| Headlines, Produkttitel, Preise im Set | **Cormorant Garamond** (variable, 300–700) | `luviona-cormorant-garamond-variable.woff2` (+ Italic) | 500 | Serife, angelehnt ans Logo, Zeilenhöhe 1,15 |
| Fließtext, Navigation, Buttons, Captions | **Jost** (variable, 100–900) | `luviona-jost-variable.woff2` (+ Italic) | 400 / 600 | Geometrische Sans, Versalien mit 18 % Spationierung („COURT STYLE ACCESSORIES“) |

- Einbindung: `assets/luviona-fonts.css` (`@font-face`, `font-display: swap`), Preload in `layout/theme.liquid`. **Kein** Abruf von Google Fonts, kein Shopify-Font-CDN, solange die Theme-Einstellung „Eigene Schriftdateien lokal laden“ aktiv ist.
- Lizenz: SIL Open Font License 1.1 (Kopien in `docs/lizenzen/`). Kommerzielle Nutzung und Self-Hosting ausdrücklich erlaubt.
- Fallback (Einstellung aus): Playfair Display + Montserrat aus der Shopify-Bibliothek.
- Skalierung: Body 100 %, Headings 115 % (Cormorant läuft optisch klein). Basisgröße 15 px mobil / 16 px Desktop, Zeilenhöhe 1,7 im Fließtext (Lesbarkeit, BFSG/WCAG 1.4.12).

## 4. Komponenten

| Komponente | Datei | Besonderheit |
|---|---|---|
| Button primär | `base.css` + `luviona.css` | Navy, Versalien, Hover → Champagner-Gold mit Navy-Text (7,2 : 1) |
| Button sekundär | — | Outline Navy, Hover-Text Gold dunkel |
| Fokuszustand | `luviona.css` | 2 px Gold-dunkel-Outline + heller Ring, auf Navy-Flächen Champagner |
| Goldene Trennlinie + Ornament | `snippets/luviona-ornament.liquid`, `.luviona-divider` | Herz/Schläger-Symbol, Verlauf zu transparent |
| Vertrauensleiste | `sections/luviona-trust-bar.liquid` | 4 Icons (Inline-SVG, kein Icon-Font), Linien oben/unten |
| Produktkarte | `snippets/card-product.liquid` | Zentriert, weißer Bildgrund, Zoom 3 % bei Hover, Preis + Pflichthinweis kompakt |
| Preis-Pflichthinweis | `snippets/luviona-price-note.liquid` | „versandkostenfrei in Deutschland · Gemäß § 19 UStG …“ |
| Akkordeon | Dawn `details/summary` | Versal-Titel in Jost, Inhalt 14 px |
| Hinweisbox | `.luviona-note` | Gold-Rahmen, 8 % Goldfläche (Geschenkhinweis) |
| Platzhalter | `.luviona-placeholder` | Bordeaux schraffiert – fällt im Editor sofort auf |
| Consent-Banner | `snippets/luviona-consent.liquid` | Bottom-Sheet, nicht modal, zwei gleichwertige Hauptbuttons |
| Widerrufsformular | `sections/luviona-widerruf-form.liquid` | Zwei Schritte, Zusammenfassung, „Widerruf bestätigen“ |
| Warenkorb-Add-on | `sections/luviona-cart-addon.liquid` | Keine Vorauswahl, ein Klick, blendet sich nach dem Hinzufügen aus |
| Set-Vorschlag | `sections/luviona-sets.liquid` | Zwei Produkte + „+“, Set-Preis nur wenn eingetragen |
| Instagram | `sections/luviona-instagram.liquid` | Eigene Bilder + Link, kein Embed |

## 5. Bild- und Medienregeln

- Format: Shopify liefert automatisch WebP/AVIF über `image_url`/`image_tag`; alle Bilder außer Hero/erstes Galeriebild mit `loading="lazy"`.
- Hero: 2000 × 1250 px (16:10), Fokus links/mitte, Tragebild mit Sandplatz. Mobil wird der Text unter das Bild gestellt (`show_text_below`), damit nichts abgeschnitten wird.
- Produktbilder: 2000 × 2000 px, Packshot auf Creme/Satin + Tragebild + **mindestens ein echtes Foto mit Größenvergleich** (Lineal/Münze). KI-Bilder: C2PA/IPTC-Metadaten behalten, Hinweis erscheint automatisch unter der Galerie.
- Alt-Texte mit Keywords (z. B. „Tennis Armband Damen grün weiß goldfarbener Schläger – LUVIONA Court Classic“), nie nur Dateiname.
- Keine Bilder, die realen Personen/Tennisprofis ähneln; keine Turnier-Logos oder -Farbkombinationen.

## 6. Performance-Budget (Ziel < 2 s mobil)

- Keine externen Skripte außer Shopify-eigenen (Standard-Events, Checkout). Keine Google-Fonts, kein Icon-CDN, kein Instagram-Embed.
- Theme-CSS: `base.css` (Dawn) + `luviona.css` (~12 KB) + `luviona-fonts.css`.
- Fonts: 4 variable WOFF2-Dateien, nur Regular + Serif werden vorgeladen (≈ 260 KB), Italics laden bei Bedarf.
- Pixel (Meta/TikTok/Google) nur über Shopify-Kundenereignisse mit Consent → kein Render-Blocking.
- Apps sparsam: jede App = Skript + Datenschutzerklärung.
