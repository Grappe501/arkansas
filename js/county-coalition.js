/**
 * County Coalition Pages — ACUCOS v1.0 (Build #14)
 */

async function initCountyCoalitionPage() {
  const root = document.getElementById('county-coalition-root');
  if (!root) return;

  const params = new URLSearchParams(window.location.search);
  const slug = params.get('county');
  if (!slug) {
    root.innerHTML = '<p>Select a county from <a href="/coalition/counties.html">the county index</a>.</p>';
    return;
  }

  const [indexRes, directoryRes, eventsRes] = await Promise.all([
    fetch('/data/county-coalition-index.json'),
    fetch('/data/coalition-directory.json'),
    fetch('/data/coalition-events.json')
  ]);
  const index = await indexRes.json();
  const directory = await directoryRes.json();
  const events = await eventsRes.json();

  const county = index.counties.find(c => c.slug === slug);
  if (!county) {
    root.innerHTML = `<p>County not found. <a href="/coalition/counties.html">Browse all counties</a>.</p>`;
    return;
  }

  const orgs = directory.organizations.filter(o =>
    (o.county || '').toLowerCase() === county.name.toLowerCase()
  );
  const countyEvents = events.events.filter(e =>
    (e.county || '').toLowerCase() === county.name.toLowerCase()
  );

  document.title = `${county.name} County Coalition | Citizens Facts`;

  root.innerHTML = `
    <nav class="breadcrumb"><a href="/">Front Door</a> → <a href="/coalition/">ACEI Coalition</a> → <a href="/coalition/counties.html">Counties</a> → ${county.name}</nav>
    <header class="hall-header">
      <span class="ladder-badge">ACEI Coalition · County</span>
      <h1>${county.name} County Coalition</h1>
      <p class="hall-purpose">Local educational partners, events, and outreach in ${county.name} County, Arkansas.</p>
      <p><span class="status-badge status-badge--coming">Completeness: ${county.completeness_pct}%</span>
         <span class="status-badge">${county.status.replace(/_/g, ' ')}</span></p>
    </header>
    <section class="proof-grid">
      <article class="proof-card"><h3>Organizations</h3><p>${orgs.length || county.organizations}</p></article>
      <article class="proof-card"><h3>Education Leaders</h3><p>${county.education_leaders}</p></article>
      <article class="proof-card"><h3>Upcoming Events</h3><p>${countyEvents.length || county.upcoming_events}</p></article>
      <article class="proof-card"><h3>Conversations</h3><p>${county.community_conversations}</p></article>
    </section>
    <section aria-labelledby="orgs-heading">
      <h2 id="orgs-heading" class="section-title">Coalition Organizations</h2>
      ${orgs.length ? `<ul>${orgs.map(o => `<li><strong>${o.organization_name}</strong> — ${o.participation_level || o.partnership_level || 'partner'}</li>`).join('')}</ul>` : '<p>No coalition organizations in this county yet. <a href="/coalition/join.html">Be the first partner →</a></p>'}
    </section>
    <section aria-labelledby="events-heading">
      <h2 id="events-heading" class="section-title">Upcoming Educational Events</h2>
      ${countyEvents.length ? `<ul>${countyEvents.map(e => `<li>${e.event_title || e.title} — ${e.event_date || ''}</li>`).join('')}</ul>` : '<p>No scheduled events. <a href="/coalition/events.html#submit">Submit an event →</a></p>'}
    </section>
    <section class="cta-banner cta-banner--coalition">
      <h2>Help ${county.name} County meet the coalition vision</h2>
      <p>Goal: at least one active educational partner in every Arkansas county.</p>
      <a href="/coalition/join.html" class="cta-button">Partner From ${county.name} County</a>
    </section>`;
}

async function initCountyCoalitionIndex() {
  const root = document.getElementById('county-coalition-index');
  if (!root) return;

  const res = await fetch('/data/county-coalition-index.json');
  const index = await res.json();

  const rows = index.counties
    .sort((a, b) => a.name.localeCompare(b.name))
    .map(c => `
      <tr>
        <td><a href="/coalition/county.html?county=${c.slug}">${c.name}</a></td>
        <td>${c.organizations}</td>
        <td>${c.completeness_pct}%</td>
        <td>${c.status.replace(/_/g, ' ')}</td>
      </tr>`).join('');

  root.innerHTML = `
    <table class="mc-table" style="width:100%">
      <thead><tr><th>County</th><th>Organizations</th><th>Completeness</th><th>Status</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>
    <p class="form-note">${index.summary.needs_outreach}</p>`;
}

document.addEventListener('DOMContentLoaded', () => {
  initCountyCoalitionPage();
  initCountyCoalitionIndex();
});
