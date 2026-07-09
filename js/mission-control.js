/**
 * Citizens United Mission Control v1.16.0 — Build #12
 */

const isAdmin = () =>
  window.location.pathname.includes('/admin/') ||
  new URLSearchParams(window.location.search).has('admin');

function pctBar(label, value, note = '', colorClass = 'blue') {
  const c = value >= 70 ? 'green' : value >= 30 ? 'yellow' : 'blue';
  return `
    <div class="mc-bar-row">
      <div class="mc-bar-row__header">
        <span class="mc-bar-row__label">${label}</span>
        <span class="mc-bar-row__pct">${value}%</span>
      </div>
      <div class="mc-bar"><div class="mc-bar__fill mc-bar__fill--${colorClass || c}" style="width:${Math.max(value, 2)}%"></div></div>
      ${note ? `<p class="mc-bar-note">${note}</p>` : ''}
    </div>`;
}

function renderHeader(data, admin) {
  const ex = data.executive;
  return `
    <header class="mc-header">
      <p class="mc-header__eyebrow">${admin ? '🔒 Admin' : 'Public'} · ${data.identity.public_name}</p>
      <h1>Citizens United Education Platform</h1>
      <p class="mc-header__question">Where are we today? What changed? What is left to build?</p>
      <div class="mc-executive mc-executive--hero">
        <div class="mc-stat mc-stat--wide"><div class="mc-stat__label">Overall Completion</div><div class="mc-stat__value mc-stat__value--hero">${ex.overall_completion}%</div></div>
        <div class="mc-stat"><div class="mc-stat__label">Current Build</div><div class="mc-stat__value">#${ex.current_build.number}</div></div>
        <div class="mc-stat"><div class="mc-stat__label">Active Phase</div><div class="mc-stat__value">${ex.active_phase}</div></div>
        <div class="mc-stat"><div class="mc-stat__label">Last Completed</div><div class="mc-stat__value">${ex.last_completed}</div></div>
        <div class="mc-stat"><div class="mc-stat__label">Next Build</div><div class="mc-stat__value">#${ex.next_build.number} ${ex.next_build.title}</div></div>
        <div class="mc-stat"><div class="mc-stat__label">GitHub</div><div class="mc-stat__value">${ex.github_status}</div></div>
        <div class="mc-stat"><div class="mc-stat__label">Netlify</div><div class="mc-stat__value">${ex.netlify_status.replace('_', ' ')}</div></div>
        <div class="mc-stat"><div class="mc-stat__label">Public Launch</div><div class="mc-stat__value">${ex.public_launch_label} (${ex.public_launch_readiness}%)</div></div>
      </div>
    </header>`;
}

function renderFiveQuestions(b) {
  return `
    <section class="mc-card mc-five-q">
      <h3>The Five Questions</h3>
      <ol>
        <li><strong>What has been built?</strong> ${b.what_built}</li>
        <li><strong>What is being built now?</strong> ${b.building_now}</li>
        <li><strong>What is blocked?</strong> ${b.blocked.join('; ')}</li>
        <li><strong>What is ready for public use?</strong> ${b.ready_public.join('; ')}</li>
        <li><strong>What needs to happen next?</strong> ${b.next}</li>
      </ol>
    </section>`;
}

function renderPhaseDetail(p, full = false) {
  const deps = p.dependencies?.length
    ? `<p class="mc-phase-deps"><strong>Depends on:</strong> ${p.dependencies.join(' → ')}</p>`
    : '';
  const deliverables = p.deliverables?.length
    ? `<ul class="mc-deliverables">${p.deliverables.map(d => `<li>${d}</li>`).join('')}</ul>`
    : '';
  const routes = p.routes?.length
    ? `<p class="mc-bar-note"><strong>Routes:</strong> ${p.routes.map(r => r.startsWith('http') ? `<a href="${r}" target="_blank" rel="noopener">${r}</a>` : `<a href="${r}">${r}</a>`).join(' · ')}</p>`
    : '';
  return `
    <div class="mc-phase" data-phase>
      <button type="button" class="mc-phase__header" aria-expanded="false">
        <span class="mc-phase__toggle">▶</span>
        <span class="mc-phase__title">Phase ${p.id} — ${p.title}</span>
        <span class="mc-phase__status mc-phase__status--${p.status}">${p.status.replace(/_/g, ' ')}</span>
        <span class="mc-phase__pct">${p.completion}%</span>
      </button>
      <div class="mc-phase__body" hidden>
        ${full && p.mission ? `<p class="mc-phase-mission">${p.mission}</p>` : ''}
        ${pctBar('Phase completion', p.completion)}
        <div class="mc-phase__meta">
          <span>${p.steps_complete}/${p.steps_total} steps</span>
          ${p.active_step ? `<span>Active: ${p.active_step}</span>` : ''}
          ${p.blocked ? `<span>Blocked: ${p.blocked}</span>` : ''}
          <span>Updated ${p.updated}</span>
        </div>
        ${full && deliverables ? `<h4 class="mc-phase-sub">Deliverables</h4>${deliverables}` : ''}
        ${full && p.completion_criteria ? `<p class="mc-bar-note"><strong>Done when:</strong> ${p.completion_criteria}</p>` : ''}
        ${full ? deps : ''}
        ${p.notes ? `<p class="mc-bar-note">${p.notes}</p>` : ''}
        ${full ? routes : ''}
      </div>
    </div>`;
}

function renderPhases(phases, full = false) {
  const sorted = [...phases].sort((a, b) => a.id - b.id);
  return sorted.map(p => renderPhaseDetail(p, full)).join('');
}

function renderDependencyMap(sequence) {
  return `
    <div class="mc-dep-map" aria-label="Phase dependency sequence">
      ${sequence.map((title, i) => `
        <span class="mc-dep-map__node">
          <span class="mc-dep-map__num">${i + 1}</span>
          <span class="mc-dep-map__label">${title}</span>
        </span>
        ${i < sequence.length - 1 ? '<span class="mc-dep-map__arrow" aria-hidden="true">→</span>' : ''}
      `).join('')}
    </div>`;
}

function renderSteps(steps, filterPhase = null) {
  const filtered = filterPhase
    ? steps.filter(s => s.registry_phase === filterPhase)
    : steps;
  return `
    <table class="mc-table">
      <thead><tr><th>#</th><th>Registry</th><th>BUILD_PLAN</th><th>Title</th><th>Status</th><th>%</th></tr></thead>
      <tbody>
        ${filtered.map(s => `
          <tr class="mc-table__row--${s.status}">
            <td>${s.num}</td>
            <td>P${s.registry_phase}</td>
            <td>${s.build_plan_phase ?? '—'}</td>
            <td>${s.title}${s.notes ? ` <em class="mc-table__gaps">(${s.notes})</em>` : ''}</td>
            <td>${s.status}</td>
            <td>${s.pct}%</td>
          </tr>`).join('')}
      </tbody>
    </table>
    <p class="mc-bar-note">${filtered.length} of ${steps.length} BUILD_PLAN steps · mapped to 15-phase registry</p>`;
}

function renderBuildMap(nodes) {
  const statusClass = { complete: 'complete', building: 'building', planning: 'planning', not_started: 'not_started', review: 'testing', blocked: 'blocked' };
  return `
    <div class="mc-build-map mc-build-map--grid">
      ${nodes.map(n => `
        <a href="${n.href}" class="mc-build-map__node mc-build-map__node--${statusClass[n.status] || 'not_started'}" target="${n.href.startsWith('http') ? '_blank' : '_self'}" rel="noopener">${n.label}</a>
      `).join('')}
    </div>
    <div class="mc-legend">
      <span>Gray: Not started</span><span>Blue: Planning</span><span>Yellow: Building</span>
      <span>Purple: Review</span><span>Green: Complete</span><span>Red: Blocked</span>
    </div>`;
}

function renderResearchReadiness(items) {
  return `
    <table class="mc-table">
      <thead><tr><th>Category</th><th>Collected</th><th>Reviewed</th><th>Summarized</th><th>Cited</th><th>Gaps</th></tr></thead>
      <tbody>
        ${items.map(r => `
          <tr><td>${r.category}</td><td>${r.collected}</td><td>${r.reviewed}</td>
          <td>${r.summarized}</td><td>${r.cited}</td><td class="mc-table__gaps">${r.gaps}</td></tr>`).join('')}
      </tbody>
    </table>`;
}

function renderAdminPanel(admin) {
  if (!admin) return '';
  return `
    <section class="mc-card mc-admin-panel">
      <h3>🔒 Admin — Internal</h3>
      <p><strong>Notes:</strong> ${admin.internal_notes}</p>
      <p><strong>Blocked:</strong> ${admin.blocked_tasks.join(' · ')}</p>
      <p><strong>Risks:</strong> ${admin.risks.join(' · ')}</p>
      <p><strong>Signups:</strong> ${admin.signup_records_note}</p>
    </section>`;
}

function initPhaseToggles() {
  document.querySelectorAll('[data-phase]').forEach(phase => {
    const btn = phase.querySelector('.mc-phase__header');
    const body = phase.querySelector('.mc-phase__body');
    const toggle = phase.querySelector('.mc-phase__toggle');
    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', !open);
      body.hidden = open;
      toggle.textContent = open ? '▶' : '▼';
    });
  });
}

async function loadMissionData() {
  const [mcRes, regRes] = await Promise.all([
    fetch('/data/mission-control.json'),
    fetch('/data/phase-registry.json')
  ]);
  const data = await mcRes.json();
  const registry = await regRes.json();
  data.registry = registry;
  data.phases = registry.phases;
  return data;
}

async function initMissionControl() {
  const root = document.getElementById('mc-root');
  if (!root) return;

  const admin = isAdmin();
  const data = await loadMissionData();
  const reg = data.registry;

  const pr = data.public_readiness;
  const civic = data.civic_action;
  const dep = data.deployment;

  root.innerHTML = `
    ${renderHeader(data, admin)}
    ${renderFiveQuestions(data.briefing)}
    <div class="mc-progress-block">
      <h2>Layered Progress — Honest Metrics</h2>
      <p class="mc-principle">${data.identity.principle}</p>
      ${data.progress_bars.map(b => pctBar(b.label, b.value, b.note)).join('')}
    </div>
    <div class="mc-grid-2">
      <div class="mc-card">
        <h3>Public Readiness Score</h3>
        <div class="mc-stat__value mc-stat__value--hero" style="font-size:2.5rem">${pr.score}%</div>
        <ul class="mc-readiness-list">
          ${pr.questions.map(q => `<li>${q.ready ? '✓' : '○'} ${q.q} <em>(${q.pct}%)</em></li>`).join('')}
        </ul>
      </div>
      <div class="mc-card">
        <h3>Civic Action Readiness</h3>
        <div class="mc-stat__value mc-stat__value--hero" style="font-size:2.5rem">${civic.readiness_score}%</div>
        <div class="mc-phase-item"><span>Education leads</span><span>${civic.education_leader_signups}</span></div>
        <div class="mc-phase-item"><span>Network signups</span><span>${civic.contact_network_signups}</span></div>
        <div class="mc-phase-item"><span>Community ideas</span><span>${civic.community_ideas}</span></div>
        <p class="mc-bar-note">Counts from Netlify Forms when integrated.</p>
      </div>
    </div>
    ${renderAdminPanel(admin ? data.admin_only : null)}
    <p class="mc-bar-note">${reg.guiding_principle}</p>
    <h2 class="mc-section-title">Facts Framework <a href="/mission-control/facts.html" class="mc-inline-link">Canonical Facts →</a></h2>
    <p class="mc-bar-note">Build #18 — 6 fact categories (FACT-1000–6000), confidence levels, 4 presentation depths, evidence traceability.</p>
    <h2 class="mc-section-title">Component Registry <a href="/mission-control/components.html" class="mc-inline-link">Master Inventory →</a></h2>
    <p class="mc-bar-note">Build #17 — 42 components (A–G), ACEI branding, linked to design system.</p>
    <h2 class="mc-section-title">Route Registry <a href="/mission-control/routes.html" class="mc-inline-link">Complete Inventory →</a></h2>
    <p class="mc-bar-note">Build #16 — 81 routes across 9 groups, Action Hub links, launch priorities.</p>
    <h2 class="mc-section-title">Canonical Data Model <a href="/mission-control/data-model.html" class="mc-inline-link">Relationship Architecture →</a></h2>
    <p class="mc-bar-note">Build #15 — 10 canonical objects, 20 relationship types, geographic &amp; timeline intelligence. Everything connected.</p>
    <h2 class="mc-section-title">ACEI Coalition <a href="/mission-control/coalition.html" class="mc-inline-link">Coalition System →</a></h2>
    <p class="mc-bar-note">Build #14 — ACEI Coalition System (formerly ACUCOS), 75 county pages, 6 participation levels.</p>
    <h2 class="mc-section-title">Arkansas Civic Ecosystem <a href="/mission-control/civic-ecosystem.html" class="mc-inline-link">County Dashboard →</a></h2>
    <p class="mc-bar-note">Build #12 — Arkansas Education Ladder (7 levels), 75-county map, Arkansas Action Hub.</p>
    <h2 class="mc-section-title">Knowledge Graph <a href="/mission-control/knowledge-graph.html" class="mc-inline-link">Educational Intelligence →</a></h2>
    <p class="mc-bar-note">Build #11 — 38 KG nodes, 62 edges, Explore Further on all content pages, 10 knowledge clusters.</p>
    <h2 class="mc-section-title">Research Framework <a href="/mission-control/research.html" class="mc-inline-link">Evidence Registry →</a></h2>
    <p class="mc-bar-note">Build #10 — Research Constitution v1.0, Evidence IDs, 5-tier source hierarchy, claim verification.</p>
    <h2 class="mc-section-title">Design System <a href="/mission-control/design.html" class="mc-inline-link">Design Language →</a></h2>
    <p class="mc-bar-note">Build #9 — institutional tokens, 14 components, <a href="/design-system/">showcase</a>.</p>
    <h2 class="mc-section-title">Citizen Journey <a href="/mission-control/journey.html" class="mc-inline-link">UX blueprint →</a></h2>
    <p class="mc-bar-note">Build #8 — 6 personas, 7-stage ladder, session memory, stage-aware Action Hub.</p>
    <h2 class="mc-section-title">MRID System <a href="/mission-control/mrid.html" class="mc-inline-link">Traceability →</a></h2>
    <p class="mc-bar-note">Build #7 — permanent requirement IDs across 16 domains. Nothing anonymous.</p>
    <h2 class="mc-section-title">Content Inventory <a href="/mission-control/inventory.html" class="mc-inline-link">Full registry →</a></h2>
    <p class="mc-bar-note">Build #6 — stable IDs for every asset. Nothing created without registry entry.</p>
    <h2 class="mc-section-title">Site Architecture <a href="/mission-control/architecture.html" class="mc-inline-link">Full blueprint →</a></h2>
    <p class="mc-bar-note">Build #5 — 10 primary sections, 82 subsections, canonical URLs. <a href="/explore/">Public site map</a></p>
    <h2 class="mc-section-title">Master Phase Registry <a href="/mission-control/phases.html" class="mc-inline-link">Full registry →</a></h2>
    ${renderPhases(data.phases, true)}
    <h2 class="mc-section-title">Step-Level Tracking</h2>
    <div class="mc-card">${renderSteps(data.steps)}</div>
    <h2 class="mc-section-title">Living Build Map</h2>
    ${renderBuildMap(data.build_map)}
    <h2 class="mc-section-title">Research Readiness</h2>
    <div class="mc-card">${renderResearchReadiness(data.research_readiness)}</div>
    <h2 class="mc-section-title">Deployment Dashboard</h2>
    <div class="mc-card">
      <div class="mc-phase-item"><span>Repository</span><span>${dep.repository_connected ? 'Connected' : '—'}</span></div>
      <div class="mc-phase-item"><span>Production branch</span><span>${dep.production_branch}</span></div>
      <div class="mc-phase-item"><span>Last commit</span><span><code>${dep.last_commit}</code></span></div>
      <div class="mc-phase-item"><span>Last deploy</span><span>${dep.last_successful_deploy}</span></div>
      <div class="mc-phase-item"><span>Production</span><span><a href="${dep.production_url}" target="_blank" rel="noopener">${dep.production_status}</a></span></div>
      <div class="mc-phase-item"><span>Forms</span><span>${dep.forms_configured ? 'Yes' : 'No'}</span></div>
      <div class="mc-phase-item"><span>Redirects</span><span>${dep.redirects_configured ? 'Yes' : 'No'}</span></div>
    </div>
    <h2 class="mc-section-title">Build Records</h2>
    <ul class="mc-builds-list">
      ${[...data.builds].map(b => `
        <li><a href="/mission-control/build.html?b=${b.number}">
          <span>Build #${b.number} — ${b.title}</span><span>v${b.version || '—'} · ${b.status}</span>
        </a></li>`).join('')}
    </ul>
    <p class="mc-bar-note">
      <a href="${admin ? '/mission-control/' : '/admin/mission-control/'}">${admin ? '← Public view' : 'Admin view →'}</a>
      · <a href="/data/mission-control.json">JSON</a> · <code>?dev=1</code> dev console
    </p>`;

  initPhaseToggles();
  if (new URLSearchParams(window.location.search).has('dev') || admin) initDevConsole(data);
}

function initDevConsole(data) {
  if (document.querySelector('.mc-dev-console')) return;
  const el = document.createElement('div');
  el.className = 'mc-dev-console';
  el.innerHTML = `
    <span><strong>Dev Console</strong></span>
    <span>Build #${data.executive.current_build.number}</span>
    <span>Next: #${data.executive.next_build.number}</span>
    <a href="${data.deployment.repo_url}">GitHub</a>
    <a href="${data.deployment.production_url}">Netlify</a>`;
  document.body.appendChild(el);
}

async function initBuildDetail() {
  const root = document.getElementById('mc-build-detail');
  if (!root) return;
  const num = parseInt(new URLSearchParams(window.location.search).get('b'), 10);
  const res = await fetch('/data/mission-control.json');
  const data = await res.json();
  const build = data.builds.find(b => b.number === num);
  if (!build) { root.innerHTML = '<p>Build not found.</p>'; return; }

  root.innerHTML = `
    <nav class="breadcrumb"><a href="/mission-control/">Mission Control</a> → Build #${build.number}</nav>
    <header class="mc-header"><h1>Build #${build.number} — ${build.title}</h1>
    <p class="mc-header__question">Permanent institutional memory · Build DNA</p></header>
    <div class="mc-dna">
      ${Object.entries({ Status: build.status, Version: build.version, Started: build.started, Completed: build.completed, Purpose: build.purpose, Branch: build.branch, Commit: build.git_commit, Review: build.review_status }).map(([k,v]) => `
        <div class="mc-dna__item"><strong>${k}</strong>${v || '—'}</div>`).join('')}
    </div>
    ${build.summary ? `<div class="mc-card"><h3>Summary</h3><p>${build.summary}</p></div>` : ''}
    ${build.decisions_made ? `<div class="mc-card"><h3>Decisions</h3><ul>${build.decisions_made.map(d => `<li>${d}</li>`).join('')}</ul></div>` : ''}
    ${build.risks ? `<div class="mc-card"><h3>Risks</h3><ul>${(Array.isArray(build.risks) ? build.risks : [build.risks]).map(r => `<li>${r}</li>`).join('')}</ul></div>` : ''}
    ${build.lessons ? `<div class="mc-card"><h3>Lessons</h3><p>${build.lessons}</p></div>` : ''}
    <p><a href="/mission-control/">← Mission Control</a></p>`;
}

function renderArchitectureSection(section) {
  const subs = (section.subsections || []).map(s => `
    <li><span class="mc-arch-status mc-arch-status--${s.status}">${s.status}</span> ${s.title}
      <code class="mc-arch-slug">${section.canonical_url}/${s.slug}</code></li>`).join('');
  return `
    <div class="mc-phase" data-phase>
      <button type="button" class="mc-phase__header" aria-expanded="false">
        <span class="mc-phase__toggle">▶</span>
        <span class="mc-phase__title">${section.title}</span>
        <span class="mc-phase__status mc-phase__status--${section.status === 'live' ? 'live' : section.status === 'partial' ? 'building' : 'planning'}">${section.status}</span>
        <code class="mc-arch-canonical">${section.canonical_url}</code>
      </button>
      <div class="mc-phase__body" hidden>
        ${section.question ? `<p class="mc-phase-mission"><strong>Q:</strong> ${section.question}</p>` : ''}
        <p class="mc-bar-note">${section.purpose}</p>
        <p class="mc-bar-note"><strong>Current:</strong> <a href="${section.current_url}">${section.current_url}</a> · Registry Phase ${section.registry_phase}</p>
        ${subs ? `<h4 class="mc-phase-sub">Subsections (${section.subsections.length})</h4><ul class="mc-deliverables mc-arch-list">${subs}</ul>` : ''}
      </div>
    </div>`;
}

async function initArchitectureBlueprint() {
  const root = document.getElementById('mc-architecture-root');
  if (!root) return;

  const [archRes, mcRes] = await Promise.all([
    fetch('/data/site-architecture.json'),
    fetch('/data/mission-control.json')
  ]);
  const arch = await archRes.json();
  const mc = await mcRes.json();
  const counts = arch.destination_counts;

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Site Architecture</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #5 · ${arch.title}</p>
      <h1>Master Site Architecture</h1>
      <p class="mc-header__question">${arch.design_philosophy.architecture_principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Primary Sections</div><div class="mc-stat__value">${counts.primary_sections}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Subsections</div><div class="mc-stat__value">${counts.primary_subsections}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live Now</div><div class="mc-stat__value">${counts.live_now}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned</div><div class="mc-stat__value">${counts.planned_subsections}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">IA Completion</div><div class="mc-stat__value">${mc.progress_bars.find(b => b.id === 'ia')?.value ?? '—'}%</div></div>
    </div>
    <section class="mc-card">
      <h3>Design Philosophy</h3>
      <p class="mc-bar-note">${arch.design_philosophy.navigation_rule}</p>
      <ul class="mc-deliverables">${arch.design_philosophy.principles.map(p => `<li>${p}</li>`).join('')}</ul>
    </section>
    <section class="mc-card">
      <h3>Reader Journey</h3>
      <div class="mc-dep-map">
        ${arch.reader_journey.map((s, i) => `
          <span class="mc-dep-map__node"><span class="mc-dep-map__num">${s.stage}</span><span class="mc-dep-map__label">${s.title}</span></span>
          ${i < arch.reader_journey.length - 1 ? '<span class="mc-dep-map__arrow">→</span>' : ''}`).join('')}
      </div>
    </section>
    <section class="mc-card">
      <h3>Cross-Linking (required on every page)</h3>
      <p class="mc-bar-note">${arch.cross_linking.rule}</p>
      <ul class="mc-deliverables">${arch.cross_linking.required_on_every_page.map(c => `<li>${c}</li>`).join('')}</ul>
    </section>
    <section class="mc-card">
      <h3>Search Strategy</h3>
      <p class="mc-bar-note">${arch.search_strategy.implementation}</p>
      <ul class="mc-deliverables">${arch.search_strategy.modes.map(m => `<li>${m}</li>`).join('')}</ul>
    </section>
    <h2 class="mc-section-title">Primary Navigation <a href="/explore/" class="mc-inline-link">Public site map →</a></h2>
    ${arch.primary_navigation.map(renderArchitectureSection).join('')}
    <h2 class="mc-section-title">Secondary Navigation</h2>
    <div class="mc-card">
      <ul class="mc-deliverables">${arch.secondary_navigation.map(n => `
        <li>${n.title} — <code>${n.canonical_url}</code> <span class="mc-arch-status mc-arch-status--${n.status}">${n.status}</span></li>`).join('')}</ul>
    </div>
    <h2 class="mc-section-title">Action Hub Actions</h2>
    <div class="mc-card">
      <p class="mc-bar-note">${arch.action_hub.principle}</p>
      <ul class="mc-deliverables">${arch.action_hub.actions.map(a => `
        <li><a href="${a.url}">${a.title}</a> — ${a.reader_stage} <span class="mc-arch-status mc-arch-status--${a.status}">${a.status}</span></li>`).join('')}</ul>
    </div>
    <p class="mc-bar-note">
      <a href="/docs/SITE_ARCHITECTURE.md">SITE_ARCHITECTURE.md</a> ·
      <a href="/data/site-architecture.json">JSON</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initPhaseToggles();
  initDevConsole(mc);
}

async function initPhaseRegistryPage() {
  const root = document.getElementById('mc-phases-root');
  if (!root) return;

  const data = await loadMissionData();
  const reg = data.registry;

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Master Phase Registry</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #4 · ${reg.title}</p>
      <h1>Master Phase Registry</h1>
      <p class="mc-header__question">Every feature belongs to exactly one phase. Honest progress at every layer.</p>
    </header>
    <section class="mc-card">
      <h3>Guiding Principle</h3>
      <p class="mc-principle">${reg.guiding_principle}</p>
      <p class="mc-bar-note">${reg.build_plan_note}</p>
    </section>
    <h2 class="mc-section-title">Phase Dependency Map</h2>
    ${renderDependencyMap(reg.dependency_sequence)}
    <h2 class="mc-section-title">All 15 Phases</h2>
    ${renderPhases(reg.phases, true)}
    <h2 class="mc-section-title">100-Step BUILD_PLAN Tracker</h2>
    <div class="mc-card">${renderSteps(data.steps)}</div>
    <p class="mc-bar-note">
      <a href="/docs/PHASE_REGISTRY.md">PHASE_REGISTRY.md</a> ·
      <a href="/data/phase-registry.json">JSON</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initPhaseToggles();
  initDevConsole(data);
}

function renderInventoryRow(item) {
  const url = item.url ? `<a href="${item.url}">${item.url}</a>` : '—';
  return `
    <tr class="mc-table__row--${item.status}" id="${item.id}">
      <td><code>${item.id}</code></td>
      <td>${item.mrid || '—'}</td>
      <td>${item.title}</td>
      <td>${item.parent_section}</td>
      <td>${item.reader_level}</td>
      <td>${item.status}</td>
      <td>${item.completion_pct}%</td>
      <td>${item.source_status}</td>
      <td>${item.review_status}</td>
      <td class="mc-inv-url">${url}</td>
    </tr>`;
}

function initInventoryFilters(items, onFilter) {
  const root = document.getElementById('mc-inv-filters');
  if (!root) return;
  const domains = [...new Set(items.map(i => i.domain).filter(Boolean))].sort((a, b) => a - b);
  const statuses = [...new Set(items.map(i => i.status))].sort();

  root.innerHTML = `
    <label>Domain <select id="mc-inv-domain"><option value="">All</option>
      ${domains.map(d => `<option value="${d}">${d}</option>`).join('')}</select></label>
    <label>Status <select id="mc-inv-status"><option value="">All</option>
      ${statuses.map(s => `<option value="${s}">${s}</option>`).join('')}</select></label>
    <label>Level <select id="mc-inv-level"><option value="">All</option>
      <option value="L1">L1</option><option value="L2">L2</option><option value="L3">L3</option><option value="L4">L4</option></select></label>
    <label>Search <input type="search" id="mc-inv-search" placeholder="ID or title…"></label>`;

  const apply = () => {
    const dom = root.querySelector('#mc-inv-domain').value;
    const st = root.querySelector('#mc-inv-status').value;
    const lvl = root.querySelector('#mc-inv-level').value;
    const q = root.querySelector('#mc-inv-search').value.toLowerCase();
    const filtered = items.filter(i => {
      if (dom && String(i.domain) !== dom) return false;
      if (st && i.status !== st) return false;
      if (lvl && i.reader_level !== lvl) return false;
      if (q && !i.id.toLowerCase().includes(q) && !i.title.toLowerCase().includes(q)) return false;
      return true;
    });
    onFilter(filtered);
  };

  root.querySelectorAll('select, input').forEach(el => el.addEventListener('input', apply));
  root.querySelectorAll('select').forEach(el => el.addEventListener('change', apply));
}

async function initContentInventory() {
  const root = document.getElementById('mc-inventory-root');
  if (!root) return;

  const [invRes, mcRes] = await Promise.all([
    fetch('/data/content-inventory.json'),
    fetch('/data/mission-control.json')
  ]);
  const inv = await invRes.json();
  const mc = await mcRes.json();
  const s = inv.summary;

  const renderTable = (items) => {
    const el = document.getElementById('mc-inv-table-body');
    if (!el) return;
    el.innerHTML = items.map(renderInventoryRow).join('');
    const count = document.getElementById('mc-inv-count');
    if (count) count.textContent = `${items.length} of ${inv.items.length} items`;
  };

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Content Inventory</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #6 · ${inv.title}</p>
      <h1>Master Content Inventory</h1>
      <p class="mc-header__question">${inv.principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Registered</div><div class="mc-stat__value">${s.registered_items}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Published</div><div class="mc-stat__value">${s.published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Partial/Outlined</div><div class="mc-stat__value">${s.partial_or_outlined}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned</div><div class="mc-stat__value">${s.planned}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">V1 Target</div><div class="mc-stat__value">~${s.v1_target_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg Completion</div><div class="mc-stat__value">${s.average_completion_pct}%</div></div>
    </div>
    <section class="mc-card">
      <h3>ID Standard</h3>
      <p class="mc-bar-note">${inv.id_standard}</p>
    </section>
    <h2 class="mc-section-title">Content Domains</h2>
    <div class="mc-card">
      <table class="mc-table">
        <thead><tr><th>ID</th><th>Code</th><th>Domain</th><th>Est.</th><th>Registered</th></tr></thead>
        <tbody>
          ${inv.domains.map(d => `
            <tr><td>${d.id}</td><td><code>${d.code}</code></td><td>${d.title}</td>
            <td>${d.estimated_assets}</td><td>${d.registered}</td></tr>`).join('')}
        </tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Cross-Domain Assets</h2>
    <div class="mc-card">
      <ul class="mc-deliverables">${inv.cross_domain.map(c => `
        <li><code>${c.prefix}</code> ${c.title} — est. ${c.estimated_assets}, registered ${c.registered_items}</li>`).join('')}</ul>
    </div>
    <h2 class="mc-section-title">All Registered Items</h2>
    <div class="mc-inv-filters" id="mc-inv-filters"></div>
    <p class="mc-bar-note" id="mc-inv-count">${inv.items.length} items</p>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>ID</th><th>MRID</th><th>Title</th><th>Section</th><th>Level</th><th>Status</th><th>%</th><th>Sources</th><th>Review</th><th>URL</th></tr></thead>
        <tbody id="mc-inv-table-body"></tbody>
      </table>
    </div>
    <p class="mc-bar-note">
      <a href="/docs/CONTENT_INVENTORY.md">CONTENT_INVENTORY.md</a> ·
      <a href="/data/content-inventory.json">JSON</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  renderTable(inv.items);
  initInventoryFilters(inv.items, renderTable);
  initDevConsole(mc);

  const hash = window.location.hash.slice(1);
  if (hash) {
    const row = document.getElementById(hash);
    if (row) {
      row.scrollIntoView({ behavior: 'smooth', block: 'center' });
      row.classList.add('mc-inv-highlight');
    }
  }
}

function findDependents(mrid, all) {
  return all.filter(r =>
    r.dependencies?.includes(mrid) ||
    r.related?.includes(mrid) ||
    r.traceability?.content_pages?.some(c => c === mrid)
  );
}

function renderMridDetail(req, all) {
  const deps = findDependents(req.mrid, all);
  const tr = req.traceability || {};
  return `
    <div class="mc-mrid-detail" id="mrid-detail">
      <h3><code>${req.mrid}</code> — ${req.title}</h3>
      <div class="mc-dna">
        <div class="mc-dna__item"><strong>Status</strong>${req.status}</div>
        <div class="mc-dna__item"><strong>Completion</strong>${req.completion_pct}%</div>
        <div class="mc-dna__item"><strong>Phase</strong>${req.phase}</div>
        <div class="mc-dna__item"><strong>Domain</strong>${req.domain}</div>
        <div class="mc-dna__item"><strong>Review</strong>${req.review_status}</div>
        <div class="mc-dna__item"><strong>Sources</strong>${req.source_coverage}</div>
      </div>
      ${req.content_id ? `<p class="mc-bar-note"><strong>Content ID:</strong> <a href="/mission-control/inventory.html#${req.content_id}">${req.content_id}</a></p>` : ''}
      ${req.url ? `<p class="mc-bar-note"><strong>URL:</strong> <a href="${req.url}">${req.url}</a></p>` : ''}
      ${req.builds?.length ? `<p class="mc-bar-note"><strong>Builds:</strong> ${req.builds.map(b => `<a href="/mission-control/build.html?b=${b}">#${b}</a>`).join(' · ')}</p>` : ''}
      ${req.dependencies?.length ? `<p class="mc-bar-note"><strong>Depends on:</strong> ${req.dependencies.map(d => `<a href="#${d}">${d}</a>`).join(', ')}</p>` : ''}
      ${req.related?.length ? `<p class="mc-bar-note"><strong>Related:</strong> ${req.related.filter(Boolean).map(d => `<a href="#${d}">${d}</a>`).join(', ')}</p>` : ''}
      ${deps.length ? `<p class="mc-bar-note"><strong>Dependents (${deps.length}):</strong> ${deps.map(d => `<a href="#${d.mrid}">${d.mrid}</a>`).join(', ')}</p>` : ''}
      ${tr.research_sources?.length ? `<p class="mc-bar-note"><strong>Research:</strong> ${tr.research_sources.join(', ')}</p>` : ''}
      <button type="button" class="mc-mrid-close" id="mrid-close">Close</button>
    </div>`;
}

function renderMridRow(req) {
  const url = req.url ? `<a href="${req.url}">↗</a>` : '';
  return `
    <tr class="mc-table__row--${req.status}" id="${req.mrid}" data-mrid="${req.mrid}">
      <td><code>${req.mrid}</code></td>
      <td>${req.domain}</td>
      <td>${req.title}</td>
      <td>P${req.phase}</td>
      <td>${req.status}</td>
      <td>${req.completion_pct}%</td>
      <td>${req.content_id || '—'}</td>
      <td>${url}</td>
    </tr>`;
}

async function initMridDashboard() {
  const root = document.getElementById('mc-mrid-root');
  if (!root) return;

  const [mridRes, mcRes] = await Promise.all([
    fetch('/data/mrid-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const reg = await mridRes.json();
  const mc = await mcRes.json();
  const s = reg.summary;
  const all = reg.requirements;

  const renderTable = (items) => {
    const el = document.getElementById('mc-mrid-table-body');
    if (!el) return;
    el.innerHTML = items.map(renderMridRow).join('');
    const count = document.getElementById('mc-mrid-count');
    if (count) count.textContent = `${items.length} of ${all.length} requirements`;
    el.querySelectorAll('tr').forEach(row => {
      row.addEventListener('click', () => {
        const id = row.dataset.mrid;
        const req = all.find(r => r.mrid === id);
        if (!req) return;
        const slot = document.getElementById('mc-mrid-detail-slot');
        if (slot) {
          slot.innerHTML = renderMridDetail(req, all);
          slot.querySelector('#mrid-close')?.addEventListener('click', () => { slot.innerHTML = ''; });
          slot.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      });
    });
  };

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → MRID System</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #7 · ${reg.title}</p>
      <h1>Master Requirement ID System</h1>
      <p class="mc-header__question">${reg.principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Requirements</div><div class="mc-stat__value">${s.total_requirements}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Published</div><div class="mc-stat__value">${s.published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Domains</div><div class="mc-stat__value">${s.domains_active}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Content Linked</div><div class="mc-stat__value">${s.content_items_linked}</div></div>
    </div>
    <section class="mc-card">
      <h3>16 Domain Codes</h3>
      <div class="mc-dep-map">
        ${reg.domain_codes.map(d => `
          <span class="mc-dep-map__node"><span class="mc-dep-map__num">${d.code}</span><span class="mc-dep-map__label">${d.title}</span></span>`).join('')}
      </div>
    </section>
    <section class="mc-card">
      <h3>Dependency Lookup</h3>
      <p class="mc-bar-note">Enter an MRID to find what depends on it, what it links to, and its traceability chain.</p>
      <label>MRID <input type="search" id="mc-mrid-lookup" placeholder="e.g. CASE-021, NAV-004, REFORM-015" style="margin-left:0.5rem;padding:0.35rem 0.5rem;background:var(--mc-surface-alt);border:1px solid var(--mc-border);color:var(--mc-text);border-radius:4px;width:220px"></label>
    </section>
    <div id="mc-mrid-detail-slot"></div>
    <h2 class="mc-section-title">All Requirements</h2>
    <div class="mc-inv-filters" id="mc-mrid-filters"></div>
    <p class="mc-bar-note" id="mc-mrid-count">${all.length} requirements</p>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>MRID</th><th>Domain</th><th>Title</th><th>Phase</th><th>Status</th><th>%</th><th>Content ID</th><th></th></tr></thead>
        <tbody id="mc-mrid-table-body"></tbody>
      </table>
    </div>
    <p class="mc-bar-note">
      <a href="/docs/MRID_SYSTEM.md">MRID_SYSTEM.md</a> ·
      <a href="/data/mrid-registry.json">JSON</a> ·
      <a href="/mission-control/inventory.html">Content Inventory</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  renderTable(all);

  const filterRoot = document.getElementById('mc-mrid-filters');
  const domains = [...new Set(all.map(r => r.domain))].sort();
  const statuses = [...new Set(all.map(r => r.status))].sort();
  filterRoot.innerHTML = `
    <label>Domain <select id="mc-mrid-domain"><option value="">All</option>${domains.map(d => `<option value="${d}">${d}</option>`).join('')}</select></label>
    <label>Status <select id="mc-mrid-status"><option value="">All</option>${statuses.map(s => `<option value="${s}">${s}</option>`).join('')}</select></label>
    <label>Search <input type="search" id="mc-mrid-search" placeholder="MRID or title…"></label>`;

  const applyFilter = () => {
    const dom = filterRoot.querySelector('#mc-mrid-domain').value;
    const st = filterRoot.querySelector('#mc-mrid-status').value;
    const q = filterRoot.querySelector('#mc-mrid-search').value.toLowerCase();
    const filtered = all.filter(r => {
      if (dom && r.domain !== dom) return false;
      if (st && r.status !== st) return false;
      if (q && !r.mrid.toLowerCase().includes(q) && !r.title.toLowerCase().includes(q)) return false;
      return true;
    });
    renderTable(filtered);
  };
  filterRoot.querySelectorAll('select, input').forEach(el => {
    el.addEventListener('input', applyFilter);
    el.addEventListener('change', applyFilter);
  });

  document.getElementById('mc-mrid-lookup')?.addEventListener('keydown', (e) => {
    if (e.key !== 'Enter') return;
    const id = e.target.value.trim().toUpperCase();
    const req = all.find(r => r.mrid === id);
    const slot = document.getElementById('mc-mrid-detail-slot');
    if (req && slot) {
      slot.innerHTML = renderMridDetail(req, all);
      slot.querySelector('#mrid-close')?.addEventListener('click', () => { slot.innerHTML = ''; });
      document.getElementById(req.mrid)?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      document.getElementById(req.mrid)?.classList.add('mc-inv-highlight');
    } else if (slot) {
      slot.innerHTML = `<div class="mc-card"><p>MRID <code>${id}</code> not found.</p></div>`;
    }
  });

  initDevConsole(mc);

  const hash = window.location.hash.slice(1);
  if (hash) {
    const req = all.find(r => r.mrid === hash);
    if (req) {
      const slot = document.getElementById('mc-mrid-detail-slot');
      if (slot) slot.innerHTML = renderMridDetail(req, all);
      document.getElementById(hash)?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
}

async function initJourneyBlueprint() {
  const root = document.getElementById('mc-journey-root');
  if (!root) return;

  const [uxRes, mcRes] = await Promise.all([
    fetch('/data/ux-journey.json'),
    fetch('/data/mission-control.json')
  ]);
  const ux = await uxRes.json();
  const mc = await mcRes.json();

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Citizen Journey</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #8 · ${ux.title}</p>
      <h1>User Experience Architecture</h1>
      <p class="mc-header__question">${ux.principle}</p>
    </header>
    <section class="mc-card">
      <h3>Design Philosophy</h3>
      <ul class="mc-deliverables">${ux.design_philosophy.map(p => `<li><strong>${p.title}</strong> — ${p.description}</li>`).join('')}</ul>
    </section>
    <h2 class="mc-section-title">Learning Ladder</h2>
    <div class="mc-dep-map">
      ${ux.learning_ladder.map((s, i) => `
        <span class="mc-dep-map__node"><span class="mc-dep-map__num">${s.stage}</span><span class="mc-dep-map__label">${s.title}</span></span>
        ${i < ux.learning_ladder.length - 1 ? '<span class="mc-dep-map__arrow">→</span>' : ''}`).join('')}
    </div>
    <h2 class="mc-section-title">Visitor Personas (6)</h2>
    <div class="mc-card">
      ${ux.personas.map(p => `
        <div class="mc-phase" style="margin-bottom:0.75rem;padding-bottom:0.75rem;border-bottom:1px solid var(--mc-border)">
          <strong>${p.title}</strong> <code>${p.mrid}</code>
          <p class="mc-bar-note">Goal: ${p.goal}</p>
          <p class="mc-bar-note">Journey: ${p.journey.join(' → ')}</p>
        </div>`).join('')}
    </div>
    <h2 class="mc-section-title">Completion Milestones</h2>
    <ul class="mc-deliverables">${ux.milestones.map(m => `<li><code>${m.mrid}</code> ${m.title} — <a href="${m.url}">${m.url}</a></li>`).join('')}</ul>
    <h2 class="mc-section-title">Success Indicators</h2>
    <table class="mc-table">
      <thead><tr><th>Metric</th><th>Target v1</th><th>Status</th></tr></thead>
      <tbody>${ux.success_indicators.map(s => `
        <tr><td>${s.title}</td><td>${s.target_v1}</td><td>${s.status}</td></tr>`).join('')}</tbody>
    </table>
    <h2 class="mc-section-title">v1 Implementation</h2>
    <div class="mc-card">
      <ul class="mc-deliverables">${Object.entries(ux.implementation).map(([k, v]) => `<li><strong>${k}:</strong> ${v}</li>`).join('')}</ul>
    </div>
    <h2 class="mc-section-title">Accessibility</h2>
    <ul class="mc-deliverables">${ux.accessibility.map(a => `<li>${a}</li>`).join('')}</ul>
    <p class="mc-bar-note">
      <a href="/docs/UX_JOURNEY.md">UX_JOURNEY.md</a> ·
      <a href="/data/ux-journey.json">JSON</a> ·
      <a href="/">Try on live site</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initDesignBlueprint() {
  const root = document.getElementById('mc-design-root');
  if (!root) return;

  const [dsRes, mcRes] = await Promise.all([
    fetch('/data/design-system.json'),
    fetch('/data/mission-control.json')
  ]);
  const ds = await dsRes.json();
  const mc = await mcRes.json();

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Design System</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #9 · ${ds.title}</p>
      <h1>Visual Design System</h1>
      <p class="mc-header__question">${ds.principle}</p>
    </header>
    <section class="mc-card">
      <h3>Design Identity</h3>
      <p class="mc-bar-note">Evokes: ${ds.identity.evokes.join(' · ')}</p>
      <p class="mc-bar-note"><strong>Avoids:</strong> ${ds.identity.avoids.join(', ')}</p>
    </section>
    <h2 class="mc-section-title">Emotional Journey</h2>
    <div class="mc-dep-map">
      ${ds.emotional_journey.map((e, i) => `
        <span class="mc-dep-map__node"><span class="mc-dep-map__num">${e.stage}</span><span class="mc-dep-map__label">${e.emotion}</span></span>
        ${i < ds.emotional_journey.length - 1 ? '<span class="mc-dep-map__arrow">→</span>' : ''}`).join('')}
    </div>
    <h2 class="mc-section-title">Color Domains</h2>
    <div class="mc-card">
      <ul class="mc-deliverables">${ds.color_philosophy.domains.map(d => `<li><code>${d.token}</code> — ${d.use}</li>`).join('')}</ul>
      <p class="mc-bar-note">${ds.color_philosophy.rule}</p>
    </div>
    <h2 class="mc-section-title">Page Layout Layers</h2>
    <ol class="mc-deliverables">${ds.layout_layers.map((l, i) => `<li>${i + 1}. ${l}</li>`).join('')}</ol>
    <h2 class="mc-section-title">Component Library (${ds.components.length})</h2>
    <table class="mc-table">
      <thead><tr><th>MRID</th><th>Component</th><th>Class</th><th>Status</th></tr></thead>
      <tbody>${ds.components.map(c => `
        <tr><td><code>${c.mrid}</code></td><td>${c.id}</td><td><code>.${c.class}</code></td><td>${c.status}</td></tr>`).join('')}</tbody>
    </table>
    <p class="mc-bar-note"><a href="/design-system/">Live component showcase →</a></p>
    <h2 class="mc-section-title">Data Viz Standards</h2>
    <ul class="mc-deliverables">${ds.data_viz_standards.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Accessibility</h2>
    <ul class="mc-deliverables">${ds.accessibility.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Trust Signals</h2>
    <ul class="mc-deliverables">${ds.trust_signals.map(t => `<li>${t}</li>`).join('')}</ul>
    <p class="mc-bar-note">
      <a href="/docs/DESIGN_LANGUAGE.md">DESIGN_LANGUAGE.md</a> ·
      <a href="/css/design-tokens.css">Tokens</a> ·
      <a href="/css/components.css">Components</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

function renderEvidenceRow(item) {
  const url = item.url
    ? (item.url.startsWith('http') ? `<a href="${item.url}" target="_blank" rel="noopener">↗</a>` : `<a href="${item.url}">↗</a>`)
    : '';
  const mrids = item.related_mrids?.length
    ? item.related_mrids.map(m => `<a href="/mission-control/mrid.html#${m}">${m}</a>`).join(', ')
    : '—';
  return `
    <tr class="mc-table__row--${item.review_status}" id="${item.ev_id}" data-ev="${item.ev_id}">
      <td><code>${item.ev_id}</code></td>
      <td>T${item.tier}</td>
      <td>${item.source_type}</td>
      <td>${item.title}</td>
      <td>${item.jurisdiction || '—'}</td>
      <td>${item.review_status}</td>
      <td>${item.workflow_stage}</td>
      <td>${mrids}</td>
      <td>${url}</td>
    </tr>`;
}

function initEvidenceFilters(items, onFilter) {
  const root = document.getElementById('mc-ev-filters');
  if (!root) return;
  const tiers = [...new Set(items.map(i => i.tier))].sort((a, b) => a - b);
  const types = [...new Set(items.map(i => i.source_type))].sort();
  const statuses = [...new Set(items.map(i => i.review_status))].sort();

  root.innerHTML = `
    <label>Tier <select id="mc-ev-tier"><option value="">All</option>
      ${tiers.map(t => `<option value="${t}">Tier ${t}</option>`).join('')}</select></label>
    <label>Type <select id="mc-ev-type"><option value="">All</option>
      ${types.map(t => `<option value="${t}">${t}</option>`).join('')}</select></label>
    <label>Review <select id="mc-ev-review"><option value="">All</option>
      ${statuses.map(s => `<option value="${s}">${s}</option>`).join('')}</select></label>
    <label>Search <input type="search" id="mc-ev-search" placeholder="EV-ID or title…"></label>`;

  const apply = () => {
    const tier = root.querySelector('#mc-ev-tier').value;
    const type = root.querySelector('#mc-ev-type').value;
    const review = root.querySelector('#mc-ev-review').value;
    const q = root.querySelector('#mc-ev-search').value.toLowerCase();
    const filtered = items.filter(i => {
      if (tier && String(i.tier) !== tier) return false;
      if (type && i.source_type !== type) return false;
      if (review && i.review_status !== review) return false;
      if (q && !i.ev_id.toLowerCase().includes(q) && !i.title.toLowerCase().includes(q) && !i.topic?.toLowerCase().includes(q)) return false;
      return true;
    });
    onFilter(filtered);
  };

  root.querySelectorAll('select, input').forEach(el => {
    el.addEventListener('input', apply);
    el.addEventListener('change', apply);
  });
}

async function initResearchBlueprint() {
  const root = document.getElementById('mc-research-root');
  if (!root) return;

  const [rfRes, evRes, mcRes] = await Promise.all([
    fetch('/data/research-framework.json'),
    fetch('/data/evidence-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const rf = await rfRes.json();
  const ev = await evRes.json();
  const mc = await mcRes.json();
  const s = ev.summary;

  const renderTable = (items) => {
    const el = document.getElementById('mc-ev-table-body');
    if (!el) return;
    el.innerHTML = items.map(renderEvidenceRow).join('');
    const count = document.getElementById('mc-ev-count');
    if (count) count.textContent = `${items.length} of ${ev.items.length} sources`;
  };

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Research Dashboard</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #10 · ${rf.title}</p>
      <h1>Research &amp; Evidence Framework</h1>
      <p class="mc-header__question">${rf.principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Total Sources</div><div class="mc-stat__value">${s.total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Tier 1 Primary</div><div class="mc-stat__value">${s.primary_sources}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Government</div><div class="mc-stat__value">${s.government_sources}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Academic</div><div class="mc-stat__value">${s.academic_sources}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Awaiting Review</div><div class="mc-stat__value">${s.awaiting_review}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">V1 Target</div><div class="mc-stat__value">~${s.v1_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Citation Coverage</div><div class="mc-stat__value">${s.citation_coverage_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Evidence Complete</div><div class="mc-stat__value">${s.evidence_completeness_pct}%</div></div>
    </div>
    <section class="mc-card">
      <h3>Research Philosophy</h3>
      <ul class="mc-deliverables">${rf.philosophy.map(p => `<li><strong>${p.title}</strong> — ${p.description}</li>`).join('')}</ul>
    </section>
    <h2 class="mc-section-title">Source Hierarchy (5 Tiers)</h2>
    <div class="mc-card">
      <table class="mc-table">
        <thead><tr><th>Tier</th><th>Category</th><th>Authority</th><th>Examples</th></tr></thead>
        <tbody>${rf.source_tiers.map(t => `
          <tr><td>${t.tier}</td><td>${t.title}</td><td>${t.authority}</td>
          <td>${t.examples.slice(0, 3).join('; ')}${t.note ? ` <em>(${t.note})</em>` : ''}</td></tr>`).join('')}
        </tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Review Workflow</h2>
    <div class="mc-dep-map">
      ${rf.review_workflow.map((w, i) => `
        <span class="mc-dep-map__node"><span class="mc-dep-map__num">${w.stage}</span><span class="mc-dep-map__label">${w.title}</span></span>
        ${i < rf.review_workflow.length - 1 ? '<span class="mc-dep-map__arrow">→</span>' : ''}`).join('')}
    </div>
    <h2 class="mc-section-title">Claim Verification Statuses</h2>
    <ul class="mc-deliverables">${rf.claim_verification_statuses.map(v => `<li><strong>${v.label}</strong> — ${v.description}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Research Gaps</h2>
    <ul class="mc-deliverables">${s.research_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Evidence Registry</h2>
    <div class="mc-inv-filters" id="mc-ev-filters"></div>
    <p class="mc-bar-note" id="mc-ev-count">${ev.items.length} sources</p>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>EV-ID</th><th>Tier</th><th>Type</th><th>Title</th><th>Jurisdiction</th><th>Review</th><th>Workflow</th><th>MRIDs</th><th>URL</th></tr></thead>
        <tbody id="mc-ev-table-body"></tbody>
      </table>
    </div>
    <p class="mc-bar-note">
      <a href="/docs/RESEARCH_CONSTITUTION.md">RESEARCH_CONSTITUTION.md</a> ·
      <a href="/data/evidence-registry.json">Evidence JSON</a> ·
      <a href="/data/claims-ledger.json">Claims ledger</a> ·
      <a href="/mission-control/facts.html">Facts Framework</a> ·
      <a href="/library/">Source Library</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  renderTable(ev.items);
  initEvidenceFilters(ev.items, renderTable);
  initDevConsole(mc);

  const hash = window.location.hash.slice(1);
  if (hash) {
    const row = document.getElementById(hash);
    if (row) {
      row.scrollIntoView({ behavior: 'smooth', block: 'center' });
      row.classList.add('mc-inv-highlight');
    }
  }
}

function renderKgRow(node) {
  const url = node.url
    ? (node.url.startsWith('http') ? `<a href="${node.url}" target="_blank" rel="noopener">↗</a>` : `<a href="${node.url}">↗</a>`)
    : '';
  return `
    <tr class="mc-table__row--${node.type}" id="${node.kg_id}" data-kg="${node.kg_id}">
      <td><code>${node.kg_id}</code></td>
      <td>${node.type}</td>
      <td>${node.title}</td>
      <td>${node.cluster || '—'}</td>
      <td>${node.completion_pct ?? '—'}%</td>
      <td>${url}</td>
    </tr>`;
}

function initKgFilters(items, onFilter) {
  const root = document.getElementById('mc-kg-filters');
  if (!root) return;
  const types = [...new Set(items.map(i => i.type))].sort();
  const clusters = [...new Set(items.map(i => i.cluster).filter(Boolean))].sort();

  root.innerHTML = `
    <label>Type <select id="mc-kg-type"><option value="">All</option>
      ${types.map(t => `<option value="${t}">${t}</option>`).join('')}</select></label>
    <label>Cluster <select id="mc-kg-cluster"><option value="">All</option>
      ${clusters.map(c => `<option value="${c}">${c}</option>`).join('')}</select></label>
    <label>Search <input type="search" id="mc-kg-search" placeholder="KG-ID or title…"></label>`;

  const apply = () => {
    const type = root.querySelector('#mc-kg-type').value;
    const cluster = root.querySelector('#mc-kg-cluster').value;
    const q = root.querySelector('#mc-kg-search').value.toLowerCase();
    const filtered = items.filter(i => {
      if (type && i.type !== type) return false;
      if (cluster && i.cluster !== cluster) return false;
      if (q && !i.kg_id.toLowerCase().includes(q) && !i.title.toLowerCase().includes(q)) return false;
      return true;
    });
    onFilter(filtered);
  };

  root.querySelectorAll('select, input').forEach(el => {
    el.addEventListener('input', apply);
    el.addEventListener('change', apply);
  });
}

async function initKnowledgeGraphBlueprint() {
  const root = document.getElementById('mc-kg-root');
  if (!root) return;

  const [kgRes, regRes, mcRes] = await Promise.all([
    fetch('/data/knowledge-graph.json'),
    fetch('/data/kg-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const kg = await kgRes.json();
  const reg = await regRes.json();
  const mc = await mcRes.json();
  const s = reg.summary;

  const renderTable = (items) => {
    const el = document.getElementById('mc-kg-table-body');
    if (!el) return;
    el.innerHTML = items.map(renderKgRow).join('');
    const count = document.getElementById('mc-kg-count');
    if (count) count.textContent = `${items.length} of ${reg.nodes.length} nodes`;
  };

  const hub = reg.nodes.find(n => n.kg_id === reg.hub_node);

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Knowledge Graph</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #11 · ${kg.title}</p>
      <h1>Knowledge Graph &amp; Educational Intelligence</h1>
      <p class="mc-header__question">${kg.principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Nodes</div><div class="mc-stat__value">${s.total_nodes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Edges</div><div class="mc-stat__value">${s.total_edges}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Hub</div><div class="mc-stat__value" style="font-size:1rem">${hub?.title || '—'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg Complete</div><div class="mc-stat__value">${s.avg_completion_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Orphans</div><div class="mc-stat__value">${s.orphan_nodes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">V1 Target</div><div class="mc-stat__value">~${s.v1_target_nodes}</div></div>
    </div>
    <h2 class="mc-section-title">Knowledge Map</h2>
    <div class="mc-dep-map">
      ${kg.knowledge_clusters.map((c, i) => `
        <span class="mc-dep-map__node"><span class="mc-dep-map__num">${c.order}</span><span class="mc-dep-map__label">${c.title}<br><small>${s.by_cluster[c.id] || 0} nodes</small></span></span>
        ${i < kg.knowledge_clusters.length - 1 ? '<span class="mc-dep-map__arrow">↓</span>' : ''}`).join('')}
    </div>
    <h2 class="mc-section-title">Object Types (${kg.object_types.length})</h2>
    <div class="mc-card">
      <table class="mc-table">
        <thead><tr><th>Type</th><th>Prefix</th><th>Registered</th></tr></thead>
        <tbody>${kg.object_types.map(t => `
          <tr><td>${t.title}</td><td><code>${t.prefix}</code></td><td>${s.by_type[t.id] || 0}</td></tr>`).join('')}
        </tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Educational Intelligence</h2>
    <ul class="mc-deliverables">${kg.educational_intelligence.map(r => `
      <li><strong>${r.condition}</strong> → ${r.recommend.join(', ')}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Future AI Layer <span class="mc-bar-note">(${kg.future_ai_layer.status})</span></h2>
    <ul class="mc-deliverables">${kg.future_ai_layer.capabilities.map(c => `<li>${c}</li>`).join('')}</ul>
    <p class="mc-bar-note"><strong>Rule:</strong> ${kg.future_ai_layer.rule}</p>
    <h2 class="mc-section-title">Knowledge Registry</h2>
    <div class="mc-inv-filters" id="mc-kg-filters"></div>
    <p class="mc-bar-note" id="mc-kg-count">${reg.nodes.length} nodes</p>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>KG-ID</th><th>Type</th><th>Title</th><th>Cluster</th><th>%</th><th>URL</th></tr></thead>
        <tbody id="mc-kg-table-body"></tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Completeness Dimensions</h2>
    <ul class="mc-deliverables">${kg.completeness_dimensions.map(d => `<li>${d.replace(/_/g, ' ')}</li>`).join('')}</ul>
    <p class="mc-bar-note">
      <a href="/docs/KNOWLEDGE_GRAPH.md">KNOWLEDGE_GRAPH.md</a> ·
      <a href="/data/kg-registry.json">Registry JSON</a> ·
      <a href="/halls/what-court-decided.html">Try Explore Further live</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  renderTable(reg.nodes);
  initKgFilters(reg.nodes, renderTable);
  initDevConsole(mc);

  const hash = window.location.hash.slice(1);
  if (hash) {
    const row = document.getElementById(hash);
    if (row) {
      row.scrollIntoView({ behavior: 'smooth', block: 'center' });
      row.classList.add('mc-inv-highlight');
    }
  }
}

async function initCivicEcosystemBlueprint() {
  const root = document.getElementById('mc-civic-root');
  if (!root) return;

  const [civicRes, countiesRes, mcRes] = await Promise.all([
    fetch('/data/civic-ecosystem.json'),
    fetch('/data/arkansas-counties.json'),
    fetch('/data/mission-control.json')
  ]);
  const civic = await civicRes.json();
  const counties = await countiesRes.json();
  const mc = await mcRes.json();
  const ladder = civic.arkansas_education_ladder || civic.civic_growth_ladder || [];
  const metrics = civic.leadership_metrics;
  const ca = mc.civic_action || {};

  const metricValue = (id) => {
    const map = {
      total_participants: ca.education_leader_signups + ca.contact_network_signups,
      registered_participants: ca.education_leader_signups + ca.contact_network_signups,
      active_learners: ca.contact_network_signups,
      active_subscribers: ca.contact_network_signups,
      community_educators: ca.education_leader_signups,
      county_leaders: ca.approved_local_leads || 0,
      regional_leaders: ca.approved_local_leads || 0,
      research_contributors: 0,
      community_conversations: 0,
      resource_downloads: ca.toolkit_requests,
      friend_family_shares: ca.share_actions,
      official_shares: 0,
      model_law_contributors: ca.model_law_submissions,
      ballot_lab_participants: ca.ballot_lab_submissions
    };
    return map[id] ?? 0;
  };

  const countyRows = counties.counties
    .sort((a, b) => b.participants - a.participants || a.name.localeCompare(b.name))
    .map(c => `
      <tr class="${c.participants > 0 ? 'mc-table__row--approved' : ''}">
        <td>${c.name}</td>
        <td>${c.participants}</td>
        <td>${c.educators}</td>
        <td>${c.conversations}</td>
      </tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Civic Ecosystem</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #12 · ${civic.title}</p>
      <h1>Arkansas Civic Action Ecosystem</h1>
      <p class="mc-header__question">${civic.principle}</p>
    </header>
    <section class="mc-card">
      <h3>Arkansas Pilot</h3>
      <p class="mc-bar-note">${civic.purpose}</p>
      <p class="mc-bar-note"><strong>${civic.pilot_state.name}</strong> (${civic.pilot_state.counties} counties) — ${civic.pilot_state.role}</p>
      <p class="mc-bar-note"><strong>Education before action:</strong> ${civic.education_before_action}</p>
    </section>
    <h2 class="mc-section-title">Arkansas Education Ladder (7 Levels)</h2>
    <div class="mc-dep-map">
      ${ladder.map((l, i) => `
        <span class="mc-dep-map__node"><span class="mc-dep-map__num">${l.level}</span><span class="mc-dep-map__label">${l.title}</span></span>
        ${i < ladder.length - 1 ? '<span class="mc-dep-map__arrow">→</span>' : ''}`).join('')}
    </div>
    <div class="mc-card">
      <ul class="mc-deliverables">${ladder.map(l => `
        <li><strong>Level ${l.level} — ${l.title}</strong> — ${l.mission}${l.tracks_county ? ' <em>(county tracked)</em>' : ''}</li>`).join('')}</ul>
    </div>
    <h2 class="mc-section-title">Arkansas Leadership Metrics</h2>
    <div class="mc-executive mc-executive--hero">
      ${metrics.slice(0, 6).map(m => `
        <div class="mc-stat"><div class="mc-stat__label">${m.title}</div><div class="mc-stat__value">${metricValue(m.id)}</div></div>`).join('')}
    </div>
    <table class="mc-table">
      <thead><tr><th>Metric</th><th>Source</th><th>Value</th></tr></thead>
      <tbody>${metrics.map(m => `
        <tr><td>${m.title}</td><td>${m.source}</td><td>${metricValue(m.id)}</td></tr>`).join('')}
      </tbody>
    </table>
    <p class="mc-bar-note">Readiness: ${ca.readiness_score}% · Metrics measure Arkansas educational network growth, not political outcomes.</p>
    <h2 class="mc-section-title">Arkansas County Map (${counties.counties_total} counties)</h2>
    <p class="mc-bar-note">${counties.summary.needs_outreach}</p>
    <div class="mc-card mc-inv-table-wrap" style="max-height:320px;overflow-y:auto">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>County</th><th>Participants</th><th>Educators</th><th>Conversations</th></tr></thead>
        <tbody>${countyRows}</tbody>
      </table>
    </div>
    <p class="mc-bar-note">Counties with engagement: ${counties.summary.counties_with_participants} · Interactive map planned.</p>
    <h2 class="mc-section-title">${civic.action_hub.title || 'Action Hub'} (${civic.action_hub.actions.length} actions)</h2>
    <table class="mc-table">
      <thead><tr><th>Action</th><th>Min Level</th><th>Route</th></tr></thead>
      <tbody>${civic.action_hub.actions.map(a => `
        <tr><td>${a.icon} ${a.title}</td><td>${a.min_level}</td><td><a href="${a.url}">${a.url}</a></td></tr>`).join('')}
      </tbody>
    </table>
    <h2 class="mc-section-title">Arkansas Workspaces</h2>
    <ul class="mc-deliverables">
      <li><strong>${civic.community_conversation_program.title || 'Community Conversation'}</strong> — <a href="${civic.community_conversation_program.route}">${civic.community_conversation_program.route}</a></li>
      <li><strong>${civic.policy_development_center.title || 'Policy Center'}</strong> — Model Law · <a href="${civic.policy_development_center.model_law_workspace.route}">draft-laws</a></li>
      <li><strong>${civic.policy_development_center.ballot_initiative_lab.title || 'Ballot Lab'}</strong> — <a href="${civic.policy_development_center.ballot_initiative_lab.route}">ballot-lab</a></li>
      <li><strong>${civic.public_official_resource_center.title || 'Public Officials'}</strong> — <a href="${civic.public_official_resource_center.route}">contact-legislators</a></li>
    </ul>
    <h2 class="mc-section-title">Future Expansion</h2>
    <p class="mc-bar-note">${civic.future_expansion.note} Architecture: ${civic.future_expansion.architecture}</p>
    <p class="mc-bar-note">
      <a href="/docs/CIVIC_PARTICIPATION_CONSTITUTION.md">CIVIC_PARTICIPATION_CONSTITUTION.md</a> ·
      <a href="/data/civic-ecosystem.json">JSON</a> ·
      <a href="/data/arkansas-counties.json">Counties</a> ·
      <a href="/">Try Arkansas Action Hub</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCoalitionBlueprint() {
  const root = document.getElementById('mc-coalition-root');
  if (!root) return;

  const [coalitionRes, directoryRes, eventsRes, countyIndexRes, mcRes] = await Promise.all([
    fetch('/data/coalition-ecosystem.json'),
    fetch('/data/coalition-directory.json'),
    fetch('/data/coalition-events.json'),
    fetch('/data/county-coalition-index.json'),
    fetch('/data/mission-control.json')
  ]);
  const coalition = await coalitionRes.json();
  const directory = await directoryRes.json();
  const events = await eventsRes.json();
  const countyIndex = await countyIndexRes.json();
  const mc = await mcRes.json();
  const ca = mc.civic_action || {};
  const co = mc.coalition_outreach || {};
  const acei = coalition.acei_coalition || coalition.acucos || {};
  const levels = coalition.participation_levels || coalition.membership_levels || [];
  const categories = coalition.coalition_categories || coalition.organization_types || [];
  const dashboard = coalition.coalition_dashboard || coalition.growth_dashboard || {};
  const social = coalition.social_media_outreach || coalition.social_media_command_center || {};

  const metricValue = (id) => {
    const map = {
      total_organizations: directory.summary.total_organizations,
      new_organizations_month: directory.summary.new_this_month || co.new_organizations_month || 0,
      counties_represented: directory.summary.counties_represented,
      organizational_categories: Object.values(directory.summary.by_category || {}).filter(v => v > 0).length,
      active_partnerships: directory.summary.active_partnerships || co.active_partnerships || 0,
      upcoming_events: events.summary.upcoming,
      completed_events: events.summary.past || co.completed_events || 0,
      community_conversations: co.community_conversations || 0,
      average_attendance: co.average_attendance || 0,
      counties_hosting_events: co.counties_hosting_events || 0,
      toolkit_downloads: ca.toolkit_requests || co.toolkit_downloads || 0,
      presentation_downloads: co.presentation_downloads || 0,
      video_views: co.video_views || 0,
      research_downloads: co.research_downloads || 0,
      faq_usage: co.faq_usage || 0,
      individual_referrals: co.individual_referrals || 0,
      organizational_referrals: co.organization_referrals || 0,
      education_leader_signups: ca.education_leader_signups || 0,
      returning_organizations: co.returning_organizations || 0,
      coalition_retention: co.coalition_retention || 0
    };
    return map[id] ?? 0;
  };

  const renderMetricSection = (title, metrics) => `
    <h2 class="mc-section-title">${title}</h2>
    <div class="mc-executive">${(metrics || []).map(m => `
      <div class="mc-stat"><div class="mc-stat__label">${m.title}</div><div class="mc-stat__value">${metricValue(m.id)}</div></div>`).join('')}
    </div>`;

  const levelRows = levels.map(l => `
    <tr><td>${l.title}</td><td>${l.description}</td><td>${directory.summary.by_level?.[l.id] ?? directory.summary.by_level?.[l.legacy_id] ?? 0}</td></tr>`).join('');

  const countyRows = countyIndex.counties
    .sort((a, b) => b.organizations - a.organizations || a.name.localeCompare(b.name))
    .map(c => `
      <tr class="${c.organizations > 0 ? 'mc-table__row--approved' : ''}">
        <td><a href="${c.route}">${c.name}</a></td>
        <td>${c.organizations}</td>
        <td>${c.completeness_pct}%</td>
        <td>${c.education_leaders}</td>
        <td>${c.upcoming_events}</td>
      </tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → ACEI Coalition</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #14 · ${acei.name || coalition.title}</p>
      <h1>ACEI Coalition Dashboard</h1>
      <p class="mc-header__question">${coalition.governing_principle}</p>
    </header>
    <section class="mc-card">
      <h3>Coalition Vision</h3>
      <p class="mc-bar-note">${coalition.coalition_vision || coalition.purpose}</p>
      <p class="mc-bar-note"><strong>Living ecosystem</strong> — not a supporter list. Mission Control tracks coalition growth as a primary success measure.</p>
    </section>
    ${renderMetricSection('Organization Metrics', dashboard.organization_metrics)}
    ${renderMetricSection('Event Metrics', dashboard.event_metrics)}
    ${renderMetricSection('Resource Metrics', dashboard.resource_metrics)}
    ${renderMetricSection('Growth Metrics', dashboard.growth_metrics)}
    <p class="mc-bar-note">ACEI Coalition readiness: ${co.readiness_score ?? 12}% · Metrics at 0 until organizations join and forms integrate.</p>
    <h2 class="mc-section-title">Participation Levels (${levels.length})</h2>
    <table class="mc-table"><thead><tr><th>Level</th><th>Role</th><th>Organizations</th></tr></thead><tbody>${levelRows}</tbody></table>
    <h2 class="mc-section-title">Coalition Categories (${categories.length})</h2>
    <ul class="mc-deliverables">${categories.map(c => `<li><strong>${c.title}</strong>${c.examples ? ' — ' + c.examples.join(', ') : c.description ? ' — ' + c.description : ''}</li>`).join('')}</ul>
    <h2 class="mc-section-title">County Completeness (${countyIndex.counties_total} counties)</h2>
    <p class="mc-bar-note">${countyIndex.summary.needs_outreach} · Counties with partner: ${countyIndex.summary.counties_with_partner}</p>
    <div class="mc-card mc-inv-table-wrap" style="max-height:320px;overflow-y:auto">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>County</th><th>Orgs</th><th>Complete</th><th>Leaders</th><th>Events</th></tr></thead>
        <tbody>${countyRows}</tbody>
      </table>
    </div>
    <p class="mc-bar-note"><a href="/coalition/counties.html">Public county index →</a> · Interactive map planned.</p>
    <h2 class="mc-section-title">Growth Engine</h2>
    <ul class="mc-deliverables">${(coalition.growth_engine?.pathways || []).map(p => `<li><strong>${p.title}</strong> — ${p.description}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recognition System</h2>
    <p class="mc-bar-note">${coalition.recognition_system?.principle || ''}</p>
    <p class="mc-bar-note">${(coalition.recognition_system?.awards || []).map(a => a.title).join(' · ')}</p>
    <h2 class="mc-section-title" id="social">Social Media Outreach</h2>
    <p class="mc-bar-note">${social.emphasis || ''}</p>
    <table class="mc-table"><thead><tr><th>Channel</th><th>Status</th></tr></thead>
      <tbody>${(social.channels || []).map(ch => `<tr><td>${ch.label}</td><td>${ch.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Future Integrations</h2>
    <table class="mc-table"><thead><tr><th>System</th><th>Route</th><th>Status</th></tr></thead>
      <tbody>${(coalition.future_integrations || []).map(i => `<tr><td>${i.title}</td><td><a href="${i.route}">${i.route}</a></td><td>${i.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Workspaces</h2>
    <ul class="mc-deliverables">
      <li><strong>ACEI Coalition Hub</strong> — <a href="/coalition/">/coalition/</a></li>
      <li><strong>Join</strong> — <a href="/coalition/join.html">/coalition/join.html</a></li>
      <li><strong>${coalition.coalition_resource_portal?.title || 'Resource Portal'}</strong> — <a href="${coalition.coalition_resource_portal?.route || '/coalition/resources.html'}">resources</a></li>
      <li><strong>Event Calendar</strong> — <a href="/coalition/events.html">/coalition/events.html</a></li>
    </ul>
    <p class="mc-bar-note">
      <a href="/docs/ACUCOS_CONSTITUTION.md">Coalition Constitution</a> ·
      <a href="/data/coalition-ecosystem.json">Blueprint JSON</a> ·
      <a href="/data/county-coalition-index.json">County index</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initDataModelBlueprint() {
  const root = document.getElementById('mc-data-model-root');
  if (!root) return;

  const [modelRes, relRes, mcRes] = await Promise.all([
    fetch('/data/canonical-data-model.json'),
    fetch('/data/relationship-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const model = await modelRes.json();
  const rel = await relRes.json();
  const mc = await mcRes.json();
  const rh = mc.relationship_health || {};
  const metrics = model.mission_control_integration?.relationship_health_metrics || [];

  const metricValue = (id) => rh[id] ?? 0;

  const objectRows = model.canonical_objects.map(o => `
    <tr>
      <td><strong>${o.title}</strong></td>
      <td><code>${o.id_prefix || o.id}</code></td>
      <td>${(o.schema || o.registry || o.directory || o.calendar || o.workspace || '—').replace(/^.*\//, '')}</td>
      <td>${(o.relationships_out || []).join(', ')}</td>
    </tr>`).join('');

  const chainRows = (model.relationship_engine?.example_chain || []).map(s => `
    <tr><td>${s.step}</td><td>${s.object}</td><td>${s.action}</td><td>${s.target}</td></tr>`).join('');

  const relTypeRows = rel.relationship_types.map(r => `
    <tr><td>${r.title}</td><td>${(r.from || []).join(', ')}</td><td>→</td><td>${(r.to || []).join(', ')}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Canonical Data Model</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #15 · ${model.title}</p>
      <h1>Master Data Model &amp; Relationships</h1>
      <p class="mc-header__question">${model.governing_principle}</p>
    </header>
    <section class="mc-card">
      <h3>Platform Philosophy</h3>
      <p class="mc-bar-note"><strong>${model.philosophy}</strong></p>
      <p class="mc-bar-note">${model.purpose}</p>
    </section>
    <h2 class="mc-section-title">Relationship Health</h2>
    <div class="mc-executive mc-executive--hero">
      ${metrics.slice(0, 6).map(m => `
        <div class="mc-stat"><div class="mc-stat__label">${m.title}</div><div class="mc-stat__value">${metricValue(m.id)}</div></div>`).join('')}
    </div>
    <table class="mc-table">
      <thead><tr><th>Metric</th><th>Value</th></tr></thead>
      <tbody>${metrics.map(m => `<tr><td>${m.title}</td><td>${metricValue(m.id)}</td></tr>`).join('')}
      </tbody>
    </table>
    <p class="mc-bar-note">Readiness: ${rh.readiness_score ?? 8}% · Edges: ${rel.summary.edges_recorded} · Relationship growth is a major success indicator.</p>
    <h2 class="mc-section-title">Canonical Objects (${model.canonical_objects.length})</h2>
    <table class="mc-table">
      <thead><tr><th>Object</th><th>Prefix</th><th>Registry</th><th>Relationships →</th></tr></thead>
      <tbody>${objectRows}</tbody>
    </table>
    <h2 class="mc-section-title">Relationship Engine — Example Chain</h2>
    <table class="mc-table">
      <thead><tr><th>Step</th><th>Object</th><th>Action</th><th>Target</th></tr></thead>
      <tbody>${chainRows}</tbody>
    </table>
    <h2 class="mc-section-title">Relationship Types (${rel.relationship_types.length})</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:280px;overflow-y:auto">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>Type</th><th>From</th><th></th><th>To</th></tr></thead>
        <tbody>${relTypeRows}</tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Geographic Intelligence</h2>
    <div class="mc-dep-map">
      ${(model.geographic_intelligence?.hierarchy || []).map((h, i, arr) => `
        <span class="mc-dep-map__node"><span class="mc-dep-map__label">${h}</span></span>
        ${i < arr.length - 1 ? '<span class="mc-dep-map__arrow">↓</span>' : ''}`).join('')}
    </div>
    <p class="mc-bar-note">${model.geographic_intelligence?.counties_total || 75} Arkansas counties · ${model.geographic_intelligence?.mission_control || ''}</p>
    <h2 class="mc-section-title">Search Intelligence (planned)</h2>
    <ul class="mc-deliverables">${(model.search_intelligence?.example_queries || []).map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Future AI Readiness</h2>
    <p class="mc-bar-note">${model.future_ai_readiness?.principle || ''}</p>
    <ul class="mc-deliverables">${(model.future_ai_readiness?.capabilities || []).map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Platform Integrations</h2>
    <table class="mc-table">
      <thead><tr><th>System</th><th>Build</th><th>Role</th></tr></thead>
      <tbody>${(model.platform_integrations || []).map(i => `
        <tr><td><a href="${i.route}">${i.system}</a></td><td>#${i.build}</td><td>${i.role}</td></tr>`).join('')}
      </tbody>
    </table>
    <h2 class="mc-section-title">Implementation Pivot — Builds #16–#20</h2>
    <p class="mc-bar-note">${model.implementation_pivot?.note || ''}</p>
    <ul class="mc-deliverables">${(model.implementation_pivot?.next_builds || []).map(b => `
      <li><strong>Build #${b.number}</strong> — ${b.title}</li>`).join('')}</ul>
    <p class="mc-bar-note">
      <a href="/docs/CANONICAL_DATA_CONSTITUTION.md">CANONICAL_DATA_CONSTITUTION.md</a> ·
      <a href="/data/canonical-data-model.json">Model JSON</a> ·
      <a href="/data/relationship-registry.json">Relationships</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initRouteRegistryBlueprint() {
  const root = document.getElementById('mc-routes-root');
  if (!root) return;

  const [routesRes, mcRes] = await Promise.all([
    fetch('/data/route-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const reg = await routesRes.json();
  const mc = await mcRes.json();
  const s = reg.summary;

  const statusBadge = (st) => {
    const colors = { live: 'approved', redirect: 'building', stub: 'coming', planned: 'planning' };
    return colors[st] || 'coming';
  };

  const groupSections = reg.groups.map(g => {
    const rows = g.routes.map(rt => `
      <tr class="${rt.status === 'live' ? 'mc-table__row--approved' : ''}">
        <td><code>${rt.path}</code></td>
        <td>${rt.title}</td>
        <td>${rt.status}</td>
        <td>${rt.launch_priority}</td>
        <td>${rt.current_destination ? `<a href="${rt.current_destination}">${rt.current_destination}</a>` : '—'}</td>
      </tr>`).join('');
    return `
      <h2 class="mc-section-title">${g.number}. ${g.title} (${g.routes.length})</h2>
      <div class="mc-card mc-inv-table-wrap" style="max-height:240px;overflow-y:auto;margin-bottom:1.5rem">
        <table class="mc-table mc-inv-table">
          <thead><tr><th>Path</th><th>Title</th><th>Status</th><th>Priority</th><th>Destination</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
      </div>`;
  }).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Route Registry</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #16 · ${reg.title}</p>
      <h1>Complete Page &amp; Route Inventory</h1>
      <p class="mc-header__question">${reg.principle}</p>
    </header>
    <section class="mc-card">
      <h3>Route Purposes</h3>
      <ul class="mc-deliverables">${reg.purposes.map(p => `<li><strong>${p.title}</strong></li>`).join('')}</ul>
    </section>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Total routes</div><div class="mc-stat__value">${s.total_routes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live</div><div class="mc-stat__value">${s.live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Redirect</div><div class="mc-stat__value">${s.redirect}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Stub</div><div class="mc-stat__value">${s.stub}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned</div><div class="mc-stat__value">${s.planned}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Must launch</div><div class="mc-stat__value">${s.must_launch}</div></div>
    </div>
    <h2 class="mc-section-title">Required Action Hub Links (${reg.action_hub_links.length})</h2>
    <table class="mc-table">
      <thead><tr><th>Link</th><th>Path</th><th>Status</th></tr></thead>
      <tbody>${reg.action_hub_links.map(l => `
        <tr><td>${l.title}</td><td><a href="${l.path}">${l.path}</a></td><td>${l.status}</td></tr>`).join('')}
      </tbody>
    </table>
    <h2 class="mc-section-title">Launch Priorities</h2>
    <p class="mc-bar-note"><strong>Must launch:</strong> ${reg.launch_priorities.must_launch.join(' · ')}</p>
    <p class="mc-bar-note"><strong>Stub OK:</strong> ${reg.launch_priorities.stub_ok.join(' · ')}</p>
    <p class="mc-bar-note"><strong>Later:</strong> ${reg.launch_priorities.later.join(' · ')}</p>
    ${groupSections}
    <p class="mc-bar-note">
      <a href="/docs/ROUTE_REGISTRY.md">ROUTE_REGISTRY.md</a> ·
      <a href="/data/route-registry.json">JSON</a> ·
      <a href="/explore/">Public site map</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initComponentRegistryBlueprint() {
  const root = document.getElementById('mc-components-root');
  if (!root) return;

  const [compRes, brandRes, designRes, mcRes] = await Promise.all([
    fetch('/data/component-registry.json'),
    fetch('/data/brand-identity.json'),
    fetch('/data/design-system.json'),
    fetch('/data/mission-control.json')
  ]);
  const reg = await compRes.json();
  const brand = await brandRes.json();
  const design = await designRes.json();
  const mc = await mcRes.json();
  const s = reg.summary;

  const byCat = {};
  reg.components.forEach(c => {
    if (!byCat[c.category]) byCat[c.category] = [];
    byCat[c.category].push(c);
  });

  const catSections = reg.categories.map(cat => {
    const items = byCat[cat.id] || [];
    const rows = items.map(c => `
      <tr class="${c.status === 'live' ? 'mc-table__row--approved' : ''}">
        <td><code>${c.id}</code></td>
        <td>${c.title}</td>
        <td>${c.status}</td>
        <td>${c.css_class || '—'}</td>
        <td>${c.design_system_ref || '—'}</td>
      </tr>`).join('');
    return `
      <h2 class="mc-section-title">Category ${cat.id} — ${cat.title} (${items.length})</h2>
      <table class="mc-table"><thead><tr><th>ID</th><th>Component</th><th>Status</th><th>CSS</th><th>DSGN</th></tr></thead><tbody>${rows}</tbody></table>`;
  }).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Component Registry</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #17 · ${reg.title}</p>
      <h1>Master Component Registry</h1>
      <p class="mc-header__question">${reg.governing_principle}</p>
    </header>
    <section class="mc-card">
      <h3>${brand.organization.name} (${brand.organization.abbrev})</h3>
      <p class="mc-bar-note"><strong>${brand.platform.name}</strong> — ${brand.platform.note}</p>
      <p class="mc-bar-note">Coalition: ${brand.coalition_system.name} <em>(renamed from ${brand.coalition_system.legacy_name})</em></p>
    </section>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Components</div><div class="mc-stat__value">${s.total_components}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live</div><div class="mc-stat__value">${s.live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Partial</div><div class="mc-stat__value">${s.partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Stub</div><div class="mc-stat__value">${s.stub}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned</div><div class="mc-stat__value">${s.planned}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">DSGN linked</div><div class="mc-stat__value">${s.design_system_linked}</div></div>
    </div>
    <h2 class="mc-section-title">Component Principles</h2>
    <ul class="mc-deliverables">${reg.principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Design System (Build #9)</h2>
    <p class="mc-bar-note">${design.components?.length || 14} legacy <code>ds-*</code> components in <a href="/design-system/">showcase</a></p>
    ${catSections}
    <h2 class="mc-section-title">Recommended: Build #${reg.recommended_next_build.number} — ${reg.recommended_next_build.title}</h2>
    <ul class="mc-deliverables">${reg.recommended_next_build.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <p class="mc-bar-note">
      <a href="/docs/COMPONENT_REGISTRY.md">COMPONENT_REGISTRY.md</a> ·
      <a href="/data/component-registry.json">JSON</a> ·
      <a href="/data/brand-identity.json">Brand</a> ·
      <a href="/mission-control/design.html">Design System</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

function renderFactRow(item) {
  const ev = (item.evidence_ids || []).map(id => `<code>${id}</code>`).join(' ') || '—';
  const kg = (item.related_topics || []).slice(0, 2).map(id => `<code>${id}</code>`).join(' ') || '—';
  const statusClass = item.review_status === 'confirmed' ? 'mc-table__row--approved' : '';
  return `
    <tr class="${statusClass}" id="${item.fact_id}">
      <td><code>${item.fact_id}</code></td>
      <td><code>${item.category_id}</code></td>
      <td>${item.short_statement}</td>
      <td>${item.review_status}</td>
      <td>${item.philosophy_question}</td>
      <td>${ev}</td>
      <td>${kg}</td>
    </tr>`;
}

async function initFactsFrameworkBlueprint() {
  const root = document.getElementById('mc-facts-root');
  if (!root) return;

  const [fwRes, regRes, mcRes] = await Promise.all([
    fetch('/data/facts-framework.json'),
    fetch('/data/facts-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const fw = await fwRes.json();
  const reg = await regRes.json();
  const mc = await mcRes.json();
  const s = reg.summary;

  const byCat = fw.categories.map(cat => {
    const count = s.by_category?.[cat.id] ?? 0;
    return `
      <tr>
        <td><code>${cat.id}</code></td>
        <td>${cat.title}</td>
        <td>${count}</td>
        <td>${cat.examples.slice(0, 3).join('; ')}…</td>
      </tr>`;
  }).join('');

  const factRows = reg.items.map(renderFactRow).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Facts Framework</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #18 · ${fw.title}</p>
      <h1>Citizens United Facts Framework</h1>
      <p class="mc-header__question">${fw.principle}</p>
    </header>
    <section class="mc-card">
      <h3>${fw.organization}</h3>
      <p class="mc-bar-note"><strong>${fw.platform}</strong></p>
      <p class="mc-bar-note">${fw.governing_principle}</p>
    </section>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Facts cataloged</div><div class="mc-stat__value">${s.total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Verified</div><div class="mc-stat__value">${s.verified}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Confirmed</div><div class="mc-stat__value">${s.confirmed}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Strongly supported</div><div class="mc-stat__value">${s.strongly_supported}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Under review</div><div class="mc-stat__value">${s.under_review}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Awaiting sources</div><div class="mc-stat__value">${s.awaiting_sources}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Arkansas facts</div><div class="mc-stat__value">${s.arkansas_facts}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">V1 target</div><div class="mc-stat__value">~${s.v1_target}</div></div>
    </div>
    <h2 class="mc-section-title">Fact Philosophy — Five Questions</h2>
    <ul class="mc-deliverables">${fw.philosophy_questions.map(q => `<li><strong>${q.question}</strong></li>`).join('')}</ul>
    <h2 class="mc-section-title">Fact Categories (${fw.categories.length})</h2>
    <table class="mc-table">
      <thead><tr><th>ID</th><th>Category</th><th>Facts</th><th>Examples</th></tr></thead>
      <tbody>${byCat}</tbody>
    </table>
    <h2 class="mc-section-title">Confidence Levels</h2>
    <ul class="mc-deliverables">${fw.confidence_levels.map(c => `<li><strong>${c.label}</strong> — ${c.description}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Presentation Levels (L1–L4)</h2>
    <table class="mc-table">
      <thead><tr><th>Level</th><th>Format</th><th>Field</th></tr></thead>
      <tbody>${fw.presentation_levels.map(p => `<tr><td>${p.id}</td><td>${p.title}</td><td><code>${p.field}</code></td></tr>`).join('')}</tbody>
    </table>
    <h2 class="mc-section-title">"How We Know" — Required Transparency</h2>
    <p class="mc-bar-note">Every major educational page includes sources readers can verify:</p>
    <ul class="mc-deliverables">${fw.how_we_know_section.includes.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${s.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Facts Registry (${s.total})</h2>
    <p class="mc-bar-note">Fact completeness: ${s.fact_completeness_pct}% · ${s.migrated_from_claims} migrated from claims ledger</p>
    <div class="mc-card mc-inv-table-wrap" style="max-height:360px;overflow-y:auto">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>ID</th><th>Category</th><th>Statement</th><th>Status</th><th>Question</th><th>EV-IDs</th><th>KG-IDs</th></tr></thead>
        <tbody>${factRows}</tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Platform Integrations</h2>
    <table class="mc-table">
      <thead><tr><th>System</th><th>Build</th><th>Link</th></tr></thead>
      <tbody>${fw.integrations.map(i => `<tr><td>${i.system}</td><td>#${i.build}</td><td><a href="${i.route}">${i.route}</a></td></tr>`).join('')}</tbody>
    </table>
    <h2 class="mc-section-title">Recommended: Build #${fw.recommended_next_build.number} — ${fw.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${fw.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/FACTS_CONSTITUTION.md">FACTS_CONSTITUTION.md</a> ·
      <a href="/data/facts-registry.json">Facts JSON</a> ·
      <a href="/data/facts-framework.json">Framework JSON</a> ·
      <a href="/mission-control/research.html">Evidence Registry</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

document.addEventListener('DOMContentLoaded', () => {
  initMissionControl();
  initBuildDetail();
  initPhaseRegistryPage();
  initArchitectureBlueprint();
  initContentInventory();
  initMridDashboard();
  initJourneyBlueprint();
  initDesignBlueprint();
  initResearchBlueprint();
  initKnowledgeGraphBlueprint();
  initCivicEcosystemBlueprint();
  initCoalitionBlueprint();
  initDataModelBlueprint();
  initRouteRegistryBlueprint();
  initComponentRegistryBlueprint();
  initFactsFrameworkBlueprint();
});
