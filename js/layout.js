/**
 * Citizens Facts — Shared layout v1.15.0
 */

const SITE_CSS = '/css/action-hub.css';
const SITE_JS = '/js/action-hub.js';
const JOURNEY_CSS = '/css/journey-panel.css';
const JOURNEY_JS = '/js/journey.js';
const EXPLORE_JS = '/js/explore-further.js';

function ensureActionHubAssets() {
  if (!document.querySelector(`link[href="${SITE_CSS}"]`)) {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = SITE_CSS;
    document.head.appendChild(link);
  }
  if (!document.querySelector(`link[href="${JOURNEY_CSS}"]`)) {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = JOURNEY_CSS;
    document.head.appendChild(link);
  }
  if (!document.querySelector(`script[src="${JOURNEY_JS}"]`)) {
    const journey = document.createElement('script');
    journey.src = JOURNEY_JS;
    journey.defer = true;
    document.body.appendChild(journey);
  }
  if (!document.querySelector(`script[src="${SITE_JS}"]`)) {
    const script = document.createElement('script');
    script.src = SITE_JS;
    script.defer = true;
    document.body.appendChild(script);
  }
  if (!document.body.classList.contains('mc-body') && !document.querySelector(`script[src="${EXPLORE_JS}"]`)) {
    const explore = document.createElement('script');
    explore.src = EXPLORE_JS;
    explore.defer = true;
    document.body.appendChild(explore);
  }
}

function renderSiteHeader(activePath) {
  const exploreActive = activePath && activePath.startsWith('/explore');
  const teachActive = activePath && (activePath.startsWith('/educate') || activePath.startsWith('/teach'));
  const sourcesActive = activePath && (activePath.startsWith('/library') || activePath.startsWith('/sources'));
  const storyActive = activePath && (activePath.startsWith('/the-story') || activePath.includes('story-before'));
  const caseActive = activePath && (activePath.startsWith('/the-case') || activePath.includes('the-case'));
  const solutionsActive = activePath && (activePath.startsWith('/solutions') || activePath.startsWith('/reform') || activePath.includes('reform') || activePath.includes('montana-hawaii'));

  return `
  <header class="site-header">
    <div class="site-header__inner">
      <div>
        <h1 class="site-title"><a href="/">Citizens Facts</a></h1>
        <p class="site-tagline">Discover → Understand → Explore → Teach → Lead</p>
      </div>
      <nav class="site-nav" aria-label="Main navigation">
        <a href="/"${activePath === '/' || activePath === '/index.html' ? ' aria-current="page"' : ''}>Home</a>
        <a href="/the-story"${storyActive ? ' aria-current="page"' : ''}>The Story</a>
        <a href="/the-case"${caseActive ? ' aria-current="page"' : ''}>The Case</a>
        <a href="/solutions/"${solutionsActive ? ' aria-current="page"' : ''}>Solutions</a>
        <a href="/teach"${teachActive ? ' aria-current="page"' : ''}>Teach</a>
        <a href="/sources"${sourcesActive ? ' aria-current="page"' : ''}>Sources</a>
        <a href="/explore/"${exploreActive ? ' aria-current="page"' : ''}>Explore</a>
      </nav>
    </div>
  </header>`;
}

function renderSiteFooter() {
  return `
  <footer class="site-footer">
    <p>
      Citizens Facts · v<span data-site-version>1.15.0</span> ·
      <a href="/explore/">Site Map</a> ·
      <a href="/library/">Sources</a> ·
      <a href="/solutions/">Solutions Center</a> ·
      <a href="/mission-control/knowledge-graph.html">Knowledge Graph</a> ·
      <a href="/mission-control/">Mission Control</a> ·
      <a href="/mission-control/phases.html">Phase Registry</a> ·
      <a href="/mission-control/architecture.html">Architecture</a> ·
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
