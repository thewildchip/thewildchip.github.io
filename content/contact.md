+++
title = "contact"
description = "Daniel's Contact."
toc = false
comments = false
showreadingtime = false
showlastmod = false
+++

<div class="email-reveal">
  <button class="email-reveal__button" type="button" aria-expanded="false">
    click to reveal
  </button>
  <span class="email-reveal__value" aria-live="polite"></span>
</div>

<script>
  (() => {
    const reveal = document.querySelector('.email-reveal');
    if (!reveal) return;

    const button = reveal.querySelector('.email-reveal__button');
    const value = reveal.querySelector('.email-reveal__value');
    const address = [100, 97, 110, 105, 101, 108, 112, 97, 110, 111, 111, 114, 64, 103, 109, 97, 105, 108, 46, 99, 111, 109]
      .map((code) => String.fromCharCode(code))
      .join('');

    button.addEventListener('click', () => {
      const link = document.createElement('a');
      link.href = `mailto:${address}`;
      link.textContent = address;

      value.replaceChildren(link);
      button.hidden = true;
      button.setAttribute('aria-expanded', 'true');
    }, { once: true });
  })();
</script>