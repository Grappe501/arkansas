/**
 * Citizens Facts — Shared layout v1.2.0
 */

function renderSiteHeader(activePath) {
  const hallsActive = activePath && activePath.startsWith('/halls');
  const educateActive = activePath && (activePath.startsWith('/educate') || activePath.startsWith('/teach'));
  const libraryActive = activePath && activePath.startsWith('/library');

  return `
  <header class="site-header">
    <div class="site-header__inner">
      <div>
        <h1 class="site-title"><a href="/">Citizens Facts</a></h1>
        <p class="site-tagline">Citizens United civic education · Understand → Teach → Lead</p>
      </div>
      <nav class="site-nav" aria-label="Main navigation">
        <a href="/"${activePath === '/' || activePath === '/index.html' ? ' aria-current="page"' : ''}>Front Door</a>
        <a href="/halls/"${hallsActive ? ' aria-current="page"' : ''}>Halls</a>
        <a href="/library/"${libraryActive ? ' aria-current="page"' : ''}>Library</a>
        <a href="/educate/"${educateActive ? ' aria-current="page"' : ''}>Teach Locally</a>
      </nav>
    </div>
  </header>`;
}

function renderStickyCta() {
  if (window.location.pathname.startsWith('/educate')) return '';
  return `
  <a href="/educate/" class="sticky-cta" aria-label="Lead education locally">
    Lead Education Locally
  </a>`;
}

function renderSiteFooter() {
  return `
  <footer class="site-footer">
    <p>
      Citizens Facts · Civic Education Engine · v<span data-site-version>1.3.0</span> ·
      <a href="/builds/">Builds</a> ·
      <a href="/BUILD_PLAN.md">Build Plan</a> ·
      <a href="https://arkansas-facts.netlify.app/" rel="noopener">Live Site</a> ·
      <a href="https://github.com/Grappe501/arkansas" rel="noopener">GitHub</a>
    </p>
    <p class="site-footer__mission">Understand → Trust → Care → Teach → Lead</p>
  </footer>
  ${renderStickyCta()}`;
}

function initLayout() {
  const headerSlot = document.getElementById('site-header');
  const footerSlot = document.getElementById('site-footer');
  const path = window.location.pathname;

  if (headerSlot) headerSlot.outerHTML = renderSiteHeader(path);
  if (footerSlot) footerSlot.outerHTML = renderSiteFooter();
}

document.addEventListener('DOMContentLoaded', initLayout);
