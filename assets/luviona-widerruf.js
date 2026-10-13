/* LUVIONA – zweistufiges Widerrufsformular: Angaben → Zusammenfassung → „Widerruf bestätigen“. */
(function () {
  const form = document.getElementById('LuvionaWiderrufForm');
  if (!form) return;
  const step1 = form.querySelector('[data-widerruf-step="1"]');
  const step2 = form.querySelector('[data-widerruf-step="2"]');
  const next = form.querySelector('[data-widerruf-next]');
  const back = form.querySelector('[data-widerruf-back]');
  if (!step1 || !step2 || !next) return;

  function show(step) {
    const toStep2 = step === 2;
    step1.hidden = toStep2;
    step2.hidden = !toStep2;
    const focusTarget = toStep2 ? step2.querySelector('h2') : step1.querySelector('input');
    if (focusTarget) {
      focusTarget.setAttribute('tabindex', '-1');
      focusTarget.focus({ preventScroll: false });
    }
    (toStep2 ? step2 : step1).scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  next.addEventListener('click', function () {
    const fields = step1.querySelectorAll('input, textarea');
    let valid = true;
    fields.forEach(function (field) {
      if (!field.checkValidity()) {
        if (valid) field.reportValidity();
        valid = false;
      }
    });
    if (!valid) return;
    step2.querySelectorAll('[data-summary-for]').forEach(function (dd) {
      const field = document.getElementById(dd.getAttribute('data-summary-for'));
      dd.textContent = field && field.value.trim() ? field.value.trim() : '–';
    });
    show(2);
  });

  if (back) back.addEventListener('click', function () { show(1); });

  // Enter in Schritt 1 darf nicht direkt absenden – erst die Zusammenfassung zeigen.
  step1.addEventListener('keydown', function (event) {
    if (event.key === 'Enter' && event.target.tagName !== 'TEXTAREA') {
      event.preventDefault();
      next.click();
    }
  });
})();
