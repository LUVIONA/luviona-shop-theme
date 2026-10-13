# 06 · Checkout & Transaktions-E-Mails

Der Shopify-Checkout ist nicht Teil des Themes; er wird über Einstellungen und *Sprache bearbeiten* rechtssicher gemacht (Schritte in `05-shopify-einrichtung.md`, Abschnitt 4). Diese Datei dokumentiert den Soll-Zustand und liefert die E-Mail-Ergänzungen.

## Soll-Zustand Checkout (§§ 312i, 312j BGB, PAngV)
1. **Kontakt:** E-Mail, Gastbestellung (kein Kontozwang), Newsletter-Checkbox nicht vorausgewählt (besser aus).
2. **Lieferung:** nur Deutschland; Versandrate „Kostenloser Versand (2–4 Werktage)“ – damit steht die Lieferzeit auch im Checkout.
3. **Zahlung:** Shopify Payments (Karte, Apple/Google Pay, Klarna), PayPal; Zahlungsarten bereits im Footer und auf der Produktseite sichtbar.
4. **Übersicht (letzte Seite):** Artikel mit Bild/Variante/Menge, Einzel- und Gesamtpreis, Lieferadresse, Rechnungsadresse, Versandart, Zahlungsart – alles mit „Ändern“-Links (Korrekturmöglichkeit).
5. **Steuerzeile:** bei 0 % erscheint keine Steuer; Texte „Inkl. Steuern“ entfernt; Hinweis „Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.“ im Checkout-Footer.
6. **Button:** „Zahlungspflichtig bestellen“.
7. **Footer-Links:** Widerrufsbelehrung, AGB, Datenschutzerklärung, Impressum, Versand.
8. **Danke-Seite:** Bestellnummer, Zusammenfassung, Hinweis auf Bestätigungs-E-Mail.

## Bestellbestätigung (Einstellungen → Benachrichtigungen → Bestellbestätigung)
Pflicht: Vertragstext (Bestellung), AGB, Widerrufsbelehrung + Muster-Widerrufsformular auf einem dauerhaften Datenträger. Vorgehen:
1. Vorlage „Bestellbestätigung“ öffnen → Betreff: `Deine LUVIONA-Bestellung {{ name }} – Bestätigung`.
2. Den Inhalt von `docs/email/bestellbestaetigung-zusatz.liquid` **vor dem schließenden `</body>`** bzw. nach dem Bestellblock einfügen. Er enthält den § 19-Hinweis, die Lieferzeit und zieht Widerrufsbelehrung + AGB automatisch aus den Shopify-Richtlinien (`shop.refund_policy.body`, `shop.terms_of_service.body`).
3. Testmail senden („Testmail senden“) und prüfen, dass **keine Steuerzeile** erscheint (bei 0 % blendet Shopify sie aus) und die Rechtstexte vollständig sind.
4. Absender `bestellung@luviona.de` (DKIM verifiziert), Antwortadresse `info@luviona.de`.

## Rechnung
Shopify erstellt keine Rechnung im Rechtssinn – Rechnungs-App mit Kleinunternehmer-Option (fortlaufende Nummer, § 19-Hinweis, kein USt-Ausweis, LUVIONA GbR als Rechnungssteller) einsetzen oder Rechnungen aus der Buchhaltungssoftware versenden. Rechnung nur per E-Mail (nicht ins Paket), Hinweis dazu in FAQ Nr. 6.

## Versandbestätigung
Betreff: `Deine LUVIONA-Bestellung ist unterwegs`. Sendungsnummer-Link ist Standard. Zusatzsatz: „Du hast 14 Tage Zeit, deine Bestellung zu widerrufen – am einfachsten über ‚Vertrag widerrufen‘ auf luviona.de.“

## Widerruf-Eingangsbestätigung (Pflichttext, Autoresponder/Formular-App)
```
Betreff: Eingangsbestätigung deines Widerrufs – LUVIONA

Hallo {{ name }},

wir haben deine Widerrufserklärung am {{ datum }} um {{ uhrzeit }} Uhr erhalten (Bestellnummer {{ bestellnummer }}).
Bitte sende die Ware innerhalb von 14 Tagen an:
LUVIONA GbR · [PLATZHALTER: Anschrift]

Die Erstattung erfolgt über das von dir genutzte Zahlungsmittel innerhalb von 14 Tagen nach Eingang deiner Erklärung;
wir können die Rückzahlung verweigern, bis wir die Ware zurückerhalten haben oder du den Nachweis der Rücksendung erbracht hast.
[PLATZHALTER: Rücksendekosten-Regelung]

Diese E-Mail ist deine Eingangsbestätigung gemäß § 356 Abs. 1 BGB.

Dein LUVIONA-Team · info@luviona.de · [PLATZHALTER: Anschrift] · LUVIONA GbR, vertreten durch [PLATZHALTER: Name 1, Name 2]
```
