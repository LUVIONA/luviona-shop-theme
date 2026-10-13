/*
  LUVIONA – Consent-Banner auf Basis der Shopify Customer Privacy API.
  Doku: https://shopify.dev/docs/api/customer-privacy
  Verhalten:
  - Banner erscheint nur, wenn Shopify für die Region eine Einwilligung verlangt (shouldShowBanner)
    und noch keine Entscheidung vorliegt.
  - Vor der Einwilligung lädt Shopify keine Marketing-/Analytics-Pixel (Kundenereignisse mit Consent-Abfrage).
  - „Alle ablehnen“ = alle Kategorien false, „Alle akzeptieren“ = alle true, „Auswahl speichern“ = Checkboxen.
  - Link „Cookie-Einstellungen“ (Footer) öffnet das Banner erneut mit dem aktuellen Stand.
*/
(function () {
  class LuvionaConsent extends HTMLElement {
    connectedCallback() {
      this.categories = this.querySelector('[data-consent-categories]');
      this.saveButton = this.querySelector('[data-consent-action="save"]');
      this.moreButton = this.querySelector('[data-consent-action="more"]');
      this.querySelectorAll('[data-consent-action]').forEach((button) => {
        button.addEventListener('click', (event) => this.onAction(event.currentTarget.dataset.consentAction));
      });
      document.querySelectorAll('[data-luviona-cookie-settings]').forEach((link) => {
        link.addEventListener('click', (event) => {
          event.preventDefault();
          this.open(true);
        });
      });
      this.loadApi(() => {
        const api = window.Shopify && window.Shopify.customerPrivacy;
        if (!api) return;
        try {
          if (api.shouldShowBanner()) this.open(false);
        } catch (error) {
          /* API ohne Regionskonfiguration – Banner bleibt geschlossen. */
        }
      });
    }

    loadApi(callback) {
      if (window.Shopify && window.Shopify.customerPrivacy) {
        callback();
        return;
      }
      if (!window.Shopify || typeof window.Shopify.loadFeatures !== 'function') return;
      window.Shopify.loadFeatures([{ name: 'consent-tracking-api', version: '0.1' }], (error) => {
        if (!error) callback();
      });
    }

    open(withCategories) {
      const api = window.Shopify && window.Shopify.customerPrivacy;
      if (withCategories && api) {
        const current = api.currentVisitorConsent ? api.currentVisitorConsent() : {};
        this.querySelectorAll('[data-consent-category]').forEach((input) => {
          input.checked = current[input.dataset.consentCategory] === 'yes';
        });
        this.showCategories(true);
      } else {
        this.showCategories(false);
      }
      this.hidden = false;
      const title = this.querySelector('.luviona-consent__title');
      if (title && withCategories) {
        title.setAttribute('tabindex', '-1');
        title.focus();
      }
    }

    showCategories(show) {
      if (!this.categories) return;
      this.categories.hidden = !show;
      if (this.saveButton) this.saveButton.hidden = !show;
      if (this.moreButton) this.moreButton.setAttribute('aria-expanded', show ? 'true' : 'false');
    }

    onAction(action) {
      if (action === 'more') {
        this.showCategories(this.categories.hidden);
        return;
      }
      let consent;
      if (action === 'accept') consent = { analytics: true, marketing: true, preferences: true, sale_of_data: true };
      else if (action === 'reject') consent = { analytics: false, marketing: false, preferences: false, sale_of_data: false };
      else {
        consent = { analytics: false, marketing: false, preferences: false, sale_of_data: false };
        this.querySelectorAll('[data-consent-category]').forEach((input) => {
          consent[input.dataset.consentCategory] = input.checked;
        });
        consent.sale_of_data = consent.marketing;
      }
      this.setConsent(consent);
    }

    setConsent(consent) {
      const api = window.Shopify && window.Shopify.customerPrivacy;
      const done = () => {
        this.hidden = true;
        document.dispatchEvent(new CustomEvent('luviona:consent', { detail: consent }));
      };
      if (api && typeof api.setTrackingConsent === 'function') {
        api.setTrackingConsent(consent, done);
      } else {
        done();
      }
    }
  }

  if (!customElements.get('luviona-consent')) customElements.define('luviona-consent', LuvionaConsent);
})();
