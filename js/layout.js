/**
 * Citizens Facts — Shared layout v1.4.0
 */

const SITE_CSS = '/css/action-hub.css';
const SITE_JS = '/js/action-hub.js';

function ensureActionHubAssets() {
  if (!document.querySelector(`link[href="${SITE_CSS}"]`)) {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = SITE_CSS;
    document.head.appendChild(link);
  }
  if (!document.querySelector(`script[src="${SITE_JS}"]`)) {
    const script = document.createElement('script');
    script.src = SITE_JS;
    script.defer = true;
    document.body.appendChild(script);
  }
}

function renderSiteHeader(activePath) {
  const hallsActive = activePath && activePath.startsWith('/halls');
  const educateActive = activePath && (activePath.startsWith('/educate') || activePath.startsWith('/teach'));
  const libraryActive = activePath && activePath.startsWith('/library');
  const actionActive = activePath && activePath.startsWith('/action');

  return `
  <header class="site-header">
    <div class="site-header__inner">
      <div>
        <h1 class="site-title"><a href="/">Citizens Facts</a></h1>
        <p class="site-tagline">Learn → Participate → Organize → Build Solutions</p>
      </div>
      <nav class="site-nav" aria-label="Main navigation">
        <a href="/"${activePath === '/' || activePath === '/index.html' ? ' aria-current="page"' : ''}>Front Door</a>
        <a href="/halls/"${hallsActive ? ' aria-current="page"' : ''}>Halls</a>
        <a href="/library/"${libraryActive ? ' aria-current="page"' : ''}>Library</a>
        <a href="/educate/"${educateActive ? ' aria-current="page"' : ''}>Teach</a>
        <a href="/action/share.html"${actionActive ? ' aria-current="page"' : ''}>Organize</a>
      </nav>
    </div>
  </header>`;
}

function renderSiteFooter() {
  return `
  <footer class="site-footer">
    <p>
      Citizens Facts · v<span data-site-version>1.8.0</span> ·
      <a href="/mission-control/">Mission Control</a> ·
      <a href="/mission-control/phases.html">Phase Registry</a> ·
      <a href="/builds/">Builds</a> ·
      <a href="/BUILD_PLAN.md">Build Plan</a> ·
      <a href="/docs/CIVIC_ACTION.md">Civic Action</a> ·
      <a href="https://github.com/Grappe501/arkansas" rel="noopener">GitHub</a>
    </p>
    <p class="site-footer__mission">Discover → Understand → Explore → Evaluate → Discuss → Teach → Lead</p>
  </footer>`;
}

function initLayout() {
  const headerSlot = document.getElementById('site-header');
  const footerSlot = document.getElementById('site-footer');
  const path = window.location.pathname;

  if (headerSlot) headerSlot.outerHTML = renderSiteHeader(path);
  if (footerSlot) footerSlot.outerHTML = renderSiteFooter();
  ensureActionHubAssets();
}

document.addEventListener('DOMContentLoaded', initLayout);
