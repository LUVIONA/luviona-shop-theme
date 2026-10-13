# 04 · Rechts-Checkliste (Deutschland, B2C, Stand Oktober 2026)

Zum Abhaken vor dem Launch. **Rechtstexte kommen ausschließlich aus dem Abmahnschutz-Paket (united-domains)** – nichts selbst formulieren. Spalte „Umsetzung“ zeigt, was das Theme bereits erledigt und was im Shopify-Admin bzw. von dir zu tun ist.

Legende: ✅ im Theme umgesetzt · ⚙️ Shopify-Admin-Einstellung (siehe `05-shopify-einrichtung.md`) · 📝 Rechtstext/Angabe von dir bzw. vom Anbieter

## A. Impressum (§ 5 DDG, § 18 Abs. 2 MStV)
- [ ] 📝 Seite „Impressum“ (Handle `impressum`, Template `page.rechtstext`) mit Text aus dem Abmahnschutz-Paket
- [ ] 📝 „LUVIONA GbR“ (bzw. „LUVIONA eGbR“ + Registergericht/-nummer, falls eingetragen)
- [ ] 📝 Vor- und Nachnamen **beider** Gesellschafter:innen als Vertretungsberechtigte → **[PLATZHALTER: Name 1, Name 2]**
- [ ] 📝 Ladungsfähige Anschrift (kein Postfach), E-Mail `info@luviona.de`, Telefon oder zweiter schneller Kontaktweg
- [ ] 📝 USt-IdNr. nur falls vorhanden; **Steuernummer nicht** ins Impressum
- [ ] 📝 Verantwortliche/r nach § 18 Abs. 2 MStV (eine Person mit Anschrift)
- [ ] ✅ Kein Link zur EU-OS-Plattform (seit 20.07.2025 abgeschaltet) – das Theme enthält keinen; im Rechtstext prüfen
- [ ] 📝 Hinweis nach § 36 VSBG (Verbraucherschlichtung) – aus dem Paket
- [ ] ⚙️ Alternativ/zusätzlich Shopify-Richtlinie „Impressum/Legal notice“ befüllen (wird im Footer automatisch verlinkt)
- [ ] ✅ Von jeder Seite mit max. 2 Klicks erreichbar (Footer-Menü „Rechtliches“ + Shopify-Richtlinienlinks)

## B. Preise (PAngV) & Kleinunternehmer (§ 19 UStG)
- [ ] ✅ Hinweis „Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.“ unter **jedem** Preis (Produktseite, Karten/Kollektion, Warenkorb, Drawer) + im Footer
- [ ] ✅ „versandkostenfrei in Deutschland“ direkt am Preis, verlinkt auf Seite „Versand & Zahlung“
- [ ] ✅ **Kein** „inkl. Steuern/MwSt.“ im Theme (Shopify-Standardtexte entfernt/geleert)
- [ ] ⚙️ Checkout-Texte „inkl. Steuern“ über *Sprache bearbeiten* entfernen; § 19-Hinweis im Checkout-Footer/Richtlinien
- [ ] ⚙️ Einstellungen → Steuern: keine Steuer für Deutschland; Produkte als „steuerpflichtig“ belassen, Steuersatz 0 % (später Umstellung auf Regelbesteuerung: Theme-Einstellung „Steuermodus“ + Steuern aktivieren)
- [ ] ⚙️ Bestellbestätigung/Rechnung mit § 19-Hinweis (siehe `06-checkout-und-emails.md`), Rechnungs-App mit Kleinunternehmer-Option
- [ ] ✅ Streichpreise: Dawn zeigt Vergleichspreis; **du** trägst beim Rabatt den niedrigsten Preis der letzten 30 Tage als Vergleichspreis ein (§ 11 PAngV) – 📝 vor jeder Aktion prüfen
- [ ] ✅/⚙️ Grundpreis Lipgloss (§ 4 PAngV): Shopify-Einheitspreis an der Love-Charm-Variante pflegen („[PLATZHALTER: x] ml“, Basis 1 ml) → Theme zeigt ihn automatisch am Preis und im Kosmetik-Block
- [ ] ✅ Lieferzeit konkret („Lieferzeit 2–4 Werktage“) auf Produktseite, im Warenkorb, in Vertrauensleiste – 📝 Zeitraum bestätigen

## C. Checkout (§§ 312i, 312j BGB)
- [ ] ⚙️ Bestellbutton exakt **„Zahlungspflichtig bestellen“** (Sprache bearbeiten → Checkout)
- [ ] ⚙️ Zusammenfassung vor Bestellabschluss (Shopify-Standard: Artikel, Preis, Lieferadresse, Zahlungsart, Korrektur möglich) – Lieferzeit im Checkout über Versandratenname „Kostenloser Versand (2–4 Werktage)“
- [ ] ⚙️ AGB, Widerrufsbelehrung, Datenschutz im Checkout-Footer verlinkt (Richtlinien befüllt)
- [ ] ✅/⚙️ Keine vorangekreuzten Checkboxen; Newsletter-Checkbox im Checkout **aus** (Einstellungen → Checkout → Marketing-Optionen: nicht vorausgewählt oder deaktiviert)
- [ ] ⚙️ Gastbestellung erlaubt (Kundenkonten „optional“)
- [ ] ⚙️ Zahlungsarten zu Beginn sichtbar (Footer-Logos ✅ + Vertrauensleiste ✅); mind. eine kostenlose Zahlungsart
- [ ] ⚙️ Bestellbestätigung mit Vertragstext, AGB, Widerrufsbelehrung + Muster-Widerrufsformular (E-Mail-Vorlage ergänzen)
- [ ] ⚙️ Shopify Markets: nur Deutschland, EUR, Versand nur DE, Versandprofil „Kostenloser Versand“

## D. Widerruf (EU-RL 2023/2673 – Widerrufsbutton seit 19.06.2026 Pflicht)
- [ ] 📝 Widerrufsbelehrung (14 Tage) + Muster-Widerrufsformular aus dem Paket → Shopify-Richtlinie „Rückgabe/Widerruf“ + Seite `muster-widerrufsformular`
- [ ] ✅ Button „Vertrag widerrufen“ im Footer → Seite `/pages/widerruf` (Template `page.widerruf`)
- [ ] ✅ Online-Formular: Name, Bestellnummer, E-Mail → Zusammenfassung → **„Widerruf bestätigen“**
- [ ] ⚙️ Automatische **Eingangsbestätigung per E-Mail** an die Kundin (dauerhafter Datenträger): Formular-App oder Autoresponder einrichten (Pflicht!)
- [ ] ⚙️ Eingang an `widerruf@luviona.de` (Shopify-Kontakt-E-Mail bzw. Weiterleitungsfilter auf Betreff „Widerruf über das Online-Formular“)
- [ ] ⚙️ Link „Vertrag widerrufen“ im Kundenkonto-Menü (Navigation → Kundenkonto-Hauptmenü)
- [ ] 📝 Regelung Rücksendekosten in Belehrung + FAQ einheitlich (**[PLATZHALTER]**)
- [ ] ✅ Hinweis Hygiene-Ausnahme für entsiegelten Lipgloss (§ 312g Abs. 2 Nr. 3 BGB) im Kosmetik-Block, FAQ und Widerrufsseite – 📝 auch in der Belehrung; Gloss versiegelt liefern

## E. AGB & Gewährleistung
- [ ] 📝 AGB aus dem Paket → Shopify-Richtlinie „AGB“ (Vertragspartner: LUVIONA GbR)
- [ ] 📝 Gesetzliche Gewährleistung 2 Jahre; „Garantie“ nirgends verwendet ✅ (Theme-Texte geprüft)

## F. Datenschutz (DSGVO, TDDDG)
- [ ] 📝 Datenschutzerklärung aus dem Paket, Dienstleisterliste: Shopify (Hosting/Shop, Shopify Payments, Shop Pay), PayPal, Klarna, [PLATZHALTER: Versanddienstleister], [PLATZHALTER: Newsletter-Tool – Shopify Email oder extern], [PLATZHALTER: Rechnungs-App], [PLATZHALTER: Formular-/Widerrufs-App], [PLATZHALTER: Analyse – Shopify Analytics / Plausible / Matomo], Kontaktformular (Shopify), united-domains (Domain/Mail)
- [ ] ⚙️ AVV mit allen Dienstleistern (Shopify: Data Processing Addendum in den AGB; Apps einzeln prüfen)
- [ ] ✅ HTTPS überall (Shopify erzwingt TLS), www → non-www Weiterleitung ⚙️ (Domains: `luviona.de` als primär)
- [ ] ✅ Schriften, Icons, Skripte lokal – keine Google Fonts, kein Icon-CDN, kein Instagram-Embed
- [ ] ✅ Kontaktformular nur E-Mail + Nachricht als Pflicht, Datenschutzhinweis darunter
- [ ] ⚙️ Newsletter: Double-Opt-in aktivieren (Einstellungen → Benachrichtigungen → Kundenbenachrichtigungen → „Double-Opt-in“ bzw. im Newsletter-Tool), Abmeldelink in jeder Mail, Einwilligung protokolliert (Shopify speichert Zeitstempel) ✅ Hinweistext im Theme
- [ ] 📝 Kein Gutschein-Zwang ohne transparente Info (aktueller Text verspricht keinen Gutschein)

## G. Cookies & Tracking (§ 25 TDDDG)
- [ ] ✅ Theme-Consent-Banner: „Alle ablehnen“ = „Alle akzeptieren“ (Größe, Farbe, Ebene), keine Vorauswahl, nicht modal, Rechtsseiten erreichbar, Widerruf über „Cookie-Einstellungen“ im Footer
- [ ] ⚙️ Einstellungen → Kundendatenschutz → Cookie-Banner/Regionen: Datenerhebung für EU/DE **„vor Einwilligung einschränken“** (sonst lädt Shopify Pixel trotzdem) – oder Shopifys Banner nutzen und Theme-Banner ausschalten (nicht beides)
- [ ] ⚙️ Pixel (Meta, TikTok, Google) nur über **Kundenereignisse (Customer Events)** mit „Benötigt Einwilligung: Marketing/Analyse“
- [ ] ⚙️ Analyse möglichst cookielos (Shopify-Analytics-Basis oder Plausible/Matomo EU-gehostet)
- [ ] 📝 Cookie-Abschnitt in der Datenschutzerklärung (Kategorien: notwendig, Präferenzen, Statistik, Marketing)

## H. KI-generierte Bilder (EU AI Act Art. 50, § 5 UWG)
- [ ] ✅ Hinweis unter jeder Produktgalerie: „Abbildung KI-generiert. Das Originalprodukt kann in Farbe und Details leicht abweichen.“ (abschaltbar pro Produkt via Metafeld `luviona.ki_bilder` = false)
- [ ] 📝 Seite „Hinweis zu unseren Bildern“ (Handle `hinweis-zu-unseren-bildern`, Text in `03-texte.md`), im Footer verlinkt
- [ ] 📝 Bilder zeigen das Produkt **nicht besser als es ist** (Größe, Farbe, Glanz, Flechtnetz, Teileanzahl) – Abgleich mit Muster
- [ ] 📝 Mind. **ein echtes Produktfoto** pro Artikel inkl. Größenvergleich (Lineal/Münze) hochladen
- [ ] 📝 Keine Ähnlichkeit mit realen Personen/Profis; C2PA/IPTC-Metadaten („trainedAlgorithmicMedia“) in den Dateien belassen (Shopify behält Originaldatei; prüfen)

## I. Produktsicherheit (GPSR, EU 2023/988) & REACH
- [ ] ✅ Akkordeon „Hersteller & Produktsicherheit“ auf jeder Produktseite: Hersteller (Name, Postanschrift, E-Mail), ggf. EU-Verantwortliche, Produktkennung (SKU), Warnhinweise
- [ ] 📝 Hersteller = **LUVIONA GbR** (wenn ihr unter eigener Marke in Verkehr bringt) bzw. tatsächlicher Hersteller + EU-Verantwortliche bei Nicht-EU-Import → Block-Standardwerte/Metafelder befüllen
- [ ] 📝 SKU je Variante vergeben (Produktkennung)
- [ ] 📝 REACH-Konformität (Nickel, Blei, Cadmium): **[PLATZHALTER: Prüfbericht des Lieferanten]** → Metafeld `luviona.material_konformitaet`
- [ ] 📝 „nickelfrei“/„hypoallergen“ nur mit Prüfnachweis – aktuell nirgends behauptet ✅

## J. Kosmetik – Lipgloss (EU-KosmetikVO 1223/2009)
- [ ] 📝 Verantwortliche Person in der EU klären (bei Nicht-EU-Herkunft + Eigenmarke = **ihr**) → Name + Anschrift auf dem Gloss **und** Metafeld `luviona.kosmetik_verantwortliche`
- [ ] 📝 CPNP-Notifizierung vor Verkauf, CPSR (Sicherheitsbewertung) und PIF (Produktinformationsdatei) → **[PLATZHALTER: Nachweise vom Hersteller]**
- [ ] ✅/📝 Produktseite zeigt: INCI, Füllmenge + Grundpreis, PAO/MHD, Chargen-Hinweis, Verwendungszweck, Warnhinweise, Allergene → Metafelder befüllen
- [ ] ✅ Keine Wirkversprechen in den Texten („pflegend“, „plumping“, „dermatologisch getestet“ vermieden); „vegan“/„tierversuchsfrei“ nur mit Beleg
- [ ] 📝 Kennzeichnung auf Produkt + Hülle auf Deutsch
- [ ] ✅ Eigene Produktlinie „Kosmetik“: Produkttyp `Kosmetik`, Template `product.kosmetik`, Filter „Produktart“
- [ ] ✅ Hygiene-Hinweis zum Widerruf (siehe D)

## K. Verpackungsgesetz (nur für euch)
- [ ] 📝 LUCID-Registrierung (Zentrale Stelle Verpackungsregister) **vor** dem ersten Verkauf
- [ ] 📝 Lizenzierung der Versandverpackungen bei einem dualen System; Registrierungsnummer im Shopify-Admin notieren (nicht auf der Website nötig)

## L. Wettbewerbs- & Markenrecht
- [ ] ✅ Keine geschützten Turnier-/Markennamen in Theme-Texten, Produktnamen, Tags, Meta-Tags (geprüft: kein „Wimbledon“, „Roland Garros“, „US Open“, keine Krokodil-Motive) – 📝 bei Social-Media-Hashtags beibehalten
- [ ] 📝 Marke „LUVIONA“ bei DPMA/EUIPO recherchieren, ggf. anmelden
- [ ] ✅ Bewertungen vor Launch nicht angezeigt (Block nicht im Template); bei späterer App: Echtheitshinweis (§ 5b Abs. 3 UWG) über Theme-Einstellung „Hinweis zur Echtheit von Bewertungen“
- [ ] 📝 Influencer-Inhalte als „Werbung/Anzeige“ kennzeichnen (Instagram-Sektion hat optionales Hinweisfeld)
- [ ] ✅ Keine Fake-Verknappung, kein Countdown, keine Superlative, keine Dark Patterns (Add-on ohne Vorauswahl, Gastbestellung, kein Confirmshaming)
- [ ] ✅ Gendergerechte Sprache (Käufer:innen, Abonnentinnen/Kundinnen situativ, du-Form)

## M. Barrierefreiheit (BFSG / WCAG 2.1 AA)
- [ ] ✅ Kontraste geprüft (siehe `01-design-konzept.md`), Fokuszustände sichtbar, Skip-Link, Alt-Text-Pflicht im Theme, Formulare mit Labels, Akkordeons tastaturbedienbar, Schriftgrößen in rem
- [ ] 📝 Seite „Barrierefreiheit“ (Handle `barrierefreiheit`) mit Text aus `03-texte.md`, im Footer verlinkt
- [ ] 📝 Alt-Texte für alle hochgeladenen Bilder pflegen; Hero-Textbild kein Text im Bild

---

## Platzhalterliste – was du noch lieferst

| # | Platzhalter | Wo einsetzen |
|---|---|---|
| 1 | Namen beider Gesellschafter:innen, Anschrift, Telefon, ggf. Registerdaten der (e)GbR | Impressum, AGB, GPSR-Block-Standardwerte, Kontaktseite, Kosmetik-Verantwortliche |
| 2 | Rechtstexte: Impressum, Datenschutzerklärung, AGB, Widerrufsbelehrung, Muster-Widerrufsformular (Abmahnschutz-Paket) | Shopify-Richtlinien + Seiten `impressum`, `muster-widerrufsformular` |
| 3 | Material/Beschichtung/Maße/Gewicht je Produkt | Metafeld `luviona.material` |
| 4 | Lieferzeit (bestätigen) | Theme-Einstellung, Versandrate, FAQ |
| 5 | Aktivierte Zahlungsanbieter | FAQ, Seite „Versand & Zahlung“, Vertrauensleiste |
| 6 | Hersteller/EU-Verantwortliche (Schmuck), Prüfberichte REACH | Metafelder `luviona.hersteller_*`, `luviona.eu_verantwortliche`, `luviona.material_konformitaet` |
| 7 | Echte Produktfotos mit Größenvergleich | Produktmedien |
| 8 | Lipgloss: INCI, Füllmenge (ml), PAO/MHD, CPNP-Nachweis, Verantwortliche Person, Allergene | Metafelder `luviona.inci`, `luviona.fuellmenge`, `luviona.pao`/`mhd`, `luviona.kosmetik_verantwortliche`, `luviona.allergene` + Einheitspreis |
| 9 | Rücksendekosten-Regelung | Widerrufsbelehrung, FAQ Nr. 5 |
| 10 | Instagram-Profil-URL, Bilder | Theme-Einstellungen Social, Instagram-Sektion |
| 11 | Logo (SVG/PNG, Navy-Hintergrund + Freisteller), Favicon | Theme-Einstellungen Logo |
| 12 | Dienstleisterliste für die Datenschutzerklärung | Rechtstext-Anbieter |
| 13 | Versanddienstleister | Datenschutz, Seite „Versand & Zahlung“ |
| 14 | Datum „Stand“ für Barrierefreiheitsseite | Seite `barrierefreiheit` |
