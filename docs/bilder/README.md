# Produkt- und Kampagnenbilder

Alle Bilder in diesem Ordner sind **KI-generiert bzw. KI-bearbeitet** (Kennzeichnungspflicht EU AI Act Art. 50, § 5 UWG). Das Theme blendet auf Produktseiten automatisch den Hinweis „Abbildung KI-generiert …“ ein. Zu **jedem Artikel muss zusätzlich mindestens ein echtes Produktfoto mit Größenvergleich** ergänzt werden (fehlt noch).

Format: JPEG, 1254 × 1254 px (Hero 1448 × 1086 px), Qualität 88, 200–390 KB. Shopify liefert daraus automatisch WebP/AVIF in allen Größen.

## Zuordnung

| Datei | Produkt / Einsatz | Position | Alt-Text (so in Shopify eintragen) |
|---|---|---|---|
| `court-classic-gruen-weiss-packshot.jpg` | Court Classic – Grün/Weiß | 1 | Tennis Armband Damen grün weiß mit goldfarbenem Tennisschläger und Tennisball – LUVIONA Court Classic, Packshot mit Geschenkbox |
| `court-classic-gruen-weiss-tragebild.jpg` | Court Classic – Grün/Weiß | 2 | Court Classic Armband grün weiß am Handgelenk, Tragebild |
| `court-classic-bordeaux-weiss-packshot.jpg` | Court Classic – Bordeaux/Weiß | 1 | Tennis Armband Damen bordeaux weiß mit goldfarbenem Tennisschläger – LUVIONA Court Classic, Packshot mit Geschenkbox |
| `court-classic-bordeaux-weiss-tragebild.jpg` | Court Classic – Bordeaux/Weiß | 2 | Court Classic Armband bordeaux weiß am Handgelenk, Tragebild |
| `court-classic-bordeaux-weiss-tragebild-satin.jpg` | Court Classic – Bordeaux/Weiß | 3 | Court Classic Armband bordeaux weiß am Handgelenk auf Satin |
| `court-classic-navy-weiss-silber-packshot.jpg` | Court Classic – Navy/Weiß (Silber) | 1 | Tennis Armband Damen navy weiß mit silberfarbenem Tennisschläger – LUVIONA Court Classic, Packshot mit Geschenkbox |
| `court-classic-navy-weiss-silber-tragebild.jpg` | Court Classic – Navy/Weiß (Silber) | 2 | Court Classic Armband navy weiß silberfarben am Handgelenk, Tragebild |
| `match-point-armband-packshot.jpg` | Match Point Armband | 1 | Tennisschläger Armband goldfarben mit Flechtnetz, Tennisball und Verlängerungskette – LUVIONA Match Point, Packshot |
| `match-point-armband-tragebild.jpg` | Match Point Armband | 2 | Match Point Armband goldfarben am Handgelenk, Tragebild |
| `match-point-kette-tragebild.jpg` | Match Point Kette | 1 | Tennisschläger Kette goldfarben mit Tennisball – LUVIONA Match Point, Tragebild am Hals |
| `match-point-kette-tragebild-hero.jpg` | Match Point Kette · **Startseiten-Hero** | 2 | Match Point Kette goldfarben auf Satin, Tragebild |
| `love-charm-olive-packshot.jpg` | Love Charm · Variante Olive | 1 (Variantenbild) | Taschenanhänger Lipgloss Bag Charm Damen Kunstleder olive mit goldfarbenen Details – LUVIONA Love Charm |
| `love-charm-rose-packshot.jpg` | Love Charm · Variante Rosé | 2 (Variantenbild) | Taschenanhänger Lipgloss Bag Charm Damen Kunstleder rosé – LUVIONA Love Charm |
| `love-charm-creme-packshot.jpg` | Love Charm · Variante Creme | 3 (Variantenbild) | Taschenanhänger Lipgloss Bag Charm Damen Kunstleder creme – LUVIONA Love Charm |

**Noch fehlend:** Love Charm in Taupe und Lavendel · je Artikel ein echtes Foto mit Lineal/Münze · Packshot der Match Point Kette (nur Tragebilder vorhanden) · freigestelltes Logo (SVG/PNG) für Header und Favicon.

## Einsatz im Theme

| Stelle | Bild | Wo einstellen |
|---|---|---|
| Startseite – Hero | `match-point-kette-tragebild-hero.jpg` | Theme-Editor → Startseite → Bild-Banner → Bild (vorher unter Inhalte → Dateien hochladen). Querformat 4:3, Text steht links in der Navy-Box; mobil unter dem Bild. |
| Startseite – Markengeschichte | `court-classic-gruen-weiss-tragebild.jpg` | Bild mit Text → Bild |
| Startseite – Instagram-Bereich | `match-point-armband-tragebild.jpg`, `love-charm-rose-packshot.jpg`, `court-classic-bordeaux-weiss-tragebild-satin.jpg`, `court-classic-navy-weiss-silber-tragebild.jpg` | LUVIONA Instagram → 4 Bild-Blöcke |
| Über LUVIONA | `court-classic-navy-weiss-silber-packshot.jpg`, `love-charm-creme-packshot.jpg` | Bild mit Text (zwei Sektionen) |
| Produktseiten | siehe Tabelle oben | Produkt → Medien (oder per CSV-Import, siehe unten) |

## Produkt-Import mit Bildern

`docs/produkte-import.csv` enthält die Bilder als `Image Src` mit `Image Position` und `Image Alt Text`. Shopify lädt Bilder beim Import nur von **öffentlich erreichbaren URLs**. Die CSV verweist auf

```
https://raw.githubusercontent.com/LUVIONA/luviona-shop-theme/main/docs/bilder/<datei>.jpg
```

Das funktioniert nur, wenn das Repository **öffentlich** ist. Ist es privat, die Bilder vorher unter *Inhalte → Dateien* hochladen, die dortigen URLs in die Spalte `Image Src` kopieren oder die Bilder nach dem Import manuell den Produkten zuordnen.

## Prüfpunkte vor dem Livegang (§ 5 UWG)

- Bilder dürfen das Produkt nicht besser zeigen als geliefert: Flechtnetz im Schläger, Emaille-Griff in Grün/Bordeaux/Navy, Tennisball-Anhänger, Schiebeknoten, Verlängerungskette beim Match Point Armband – alles mit dem Muster abgleichen.
- Die Navy-Box und der Seidenschal mit Monogramm sind Requisiten. Nur als Geschenkbox bewerben, was tatsächlich mitgeliefert wird. Perlenohrringe und Tasche gehören **nicht** zum Lieferumfang; ggf. in der Beschreibung klarstellen („Abbildung zeigt Dekoration“).
- Der Lieferanten-Screenshot (Angabe „14K Gold Plated“) ist bewusst **nicht** im Repo. „14-karätig vergoldet“ nur verwenden, wenn der Lieferant das schriftlich belegt; sonst bleibt es bei „goldfarben“.
- Metadaten: Die Original-PNGs enthalten nur einen minimalen EXIF-Block (Auflösung) und **keine** C2PA-/IPTC-Kennzeichnung. Der EXIF-Block wurde in die JPEGs übernommen. Die Angabe „Digital Source Type: trainedAlgorithmicMedia“ (IPTC) muss vor dem Upload nachgetragen werden, z. B. mit ExifTool: `exiftool -XMP-iptcExt:DigitalSourceType="http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia" docs/bilder/*.jpg`. Shopify liefert optimierte Kopien ohne Metadaten aus – die sichtbare Kennzeichnung im Theme bleibt deshalb ohnehin Pflicht.
