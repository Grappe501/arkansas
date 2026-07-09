/**
 * Citizens United Mission Control v1.11.0 — Build #7
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

document.addEventListener('DOMContentLoaded', () => {
  initMissionControl();
  initBuildDetail();
  initPhaseRegistryPage();
  initArchitectureBlueprint();
  initContentInventory();
  initMridDashboard();
});
