/**
 * Public site map — renders from site-architecture.json (Build #5)
 */

function statusLabel(status) {
  return status.replace('_', ' ');
}

function subsectionLink(parent, sub) {
  if (sub.url) return sub.url;
  if (sub.status === 'live' || sub.status === 'partial') {
    return `${parent.canonical_url}/${sub.slug}`;
  }
  return null;
}

async function initSiteMap() {
  const root = document.getElementById('site-map-root');
  if (!root) return;

  const res = await fetch('/data/site-architecture.json');
  const arch = await res.json();

  const journey = arch.reader_journey.map((s, i) => `
    <span class="site-map-journey__stage">${s.title}</span>
    ${i < arch.reader_journey.length - 1 ? '<span class="site-map-journey__arrow" aria-hidden="true">→</span>' : ''}
  `).join('');

  const sections = arch.primary_navigation.map(section => {
    const href = section.current_url || section.canonical_url;
    const subs = (section.subsections || []).map(sub => {
      const link = subsectionLink(section, sub);
      const inner = link
        ? `<a href="${link}">${sub.title}</a>`
        : sub.title;
      return `<li><span class="site-map-status site-map-status--${sub.status}">${statusLabel(sub.status)}</span> ${inner}</li>`;
    }).join('');

    return `
      <section class="site-map-section" id="${section.id}">
        <div class="site-map-section__header">
          <h2><a href="${href}">${section.title}</a></h2>
          <span class="site-map-status site-map-status--${section.status}">${statusLabel(section.status)}</span>
          <code style="font-size:0.75rem;color:var(--text-muted)">${section.canonical_url}</code>
        </div>
        ${section.question ? `<p class="site-map-section__question">${section.question}</p>` : ''}
        ${section.purpose ? `<p class="site-map-section__purpose">${section.purpose}</p>` : ''}
        ${subs ? `<ul class="site-map-subsections">${subs}</ul>` : ''}
      </section>`;
  }).join('');

  const secondary = arch.secondary_navigation.map(item => {
    const live = item.status === 'live';
    const href = item.current_url || item.canonical_url;
    return live
      ? `<a href="${href}">${item.title}</a>`
      : `<a href="#" aria-disabled="true" title="Coming soon">${item.title}</a>`;
  }).join('');

  root.innerHTML = `
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> → Explore the Platform</nav>
    <header class="site-map-intro hall-header">
      <span class="ladder-badge">Site Map · Build #5</span>
      <h1>Explore the Platform</h1>
      <p class="hall-purpose">${arch.design_philosophy.navigation_rule}</p>
      <p class="hall-purpose">${arch.design_philosophy.architecture_principle}</p>
    </header>
    <h2 class="visually-hidden">Reader Journey</h2>
    <div class="site-map-journey" aria-label="Reader journey stages">${journey}</div>
    ${sections}
    <section>
      <h2>Also Available</h2>
      <div class="site-map-secondary">${secondary}</div>
    </section>
    <div class="site-map-cta">
      <p><strong>Every page is being built in layers.</strong> Start at L1 (one minute), go deeper when ready, return to overview anytime.</p>
      <p><a href="/educate/">Become an Education Leader →</a></p>
    </div>`;
}

document.addEventListener('DOMContentLoaded', initSiteMap);
