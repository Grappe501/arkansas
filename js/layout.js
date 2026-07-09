/**
 * Citizens Facts — Shared layout v1.1.0
 */

function renderSiteHeader(activePath) {
  const hallsActive = activePath && activePath.startsWith('/halls');
  const educateActive = activePath && activePath.startsWith('/educate');

  return `
  <header class="site-header">
    <div class="site-header__inner">
      <div>
        <h1 class="site-title"><a href="/">Citizens Facts</a></h1>
        <p class="site-tagline">Citizens United civic education · Understand → Teach → Lead</p>
      </div>
      <nav class="site-nav" aria-label="Main navigation">
        <a href="/"${activePath === '/' ? ' aria-current="page"' : ''}>Front Door</a>
        <a href="/halls/"${hallsActive ? ' aria-current="page"' : ''}>Learning Halls</a>
        <a href="/educate/"${educateActive ? ' aria-current="page"' : ''}>Educate</a>
      </nav>
    </div>
  </header>`;
}

function renderSiteFooter() {
  return `
  <footer class="site-footer">
    <p>
      Citizens Facts · Civic Education Engine · v<span data-site-version>1.1.0</span> ·
      <a href="https://arkansas-facts.netlify.app/" rel="noopener">Live Site</a> ·
      <a href="https://github.com/Grappe501/arkansas" rel="noopener">GitHub</a>
    </p>
    <p class="site-footer__mission">Understand → Trust → Care → Teach → Lead</p>
  </footer>`;
}

function initLayout() {
  const headerSlot = document.getElementById('site-header');
  const footerSlot = document.getElementById('site-footer');
  const path = window.location.pathname;

  if (headerSlot) headerSlot.outerHTML = renderSiteHeader(path);
  if (footerSlot) footerSlot.outerHTML = renderSiteFooter();
}

document.addEventListener('DOMContentLoaded', initLayout);
