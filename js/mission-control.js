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
    <h2 class="mc-section-title">Strategic Plan 2035 <a href="/mission-control/arkansas-strategic-plan-2035.html" class="mc-inline-link">Decade Roadmap #84 →</a></h2>
    <p class="mc-bar-note">Build #84 — Master Arkansas Strategic Plan 2035. Accomplishment roadmap to statewide civic education institution. 7 goals, 10 metrics, 5yr/10yr milestones, annual review. 0/75 counties · 0/200K · scorecard not live. ~55% readiness.</p>
    <h2 class="mc-section-title">Civic Ecosystem <a href="/mission-control/arkansas-civic-ecosystem.html" class="mc-inline-link">Connected Network #83 →</a></h2>
    <p class="mc-bar-note">Build #83 — Master Arkansas Civic Ecosystem. One institution, one state, one connected network. 12 living systems, 4 loops, health score, executive dashboard. 0/12 instrumented · health score not live. ~54% readiness.</p>
    <h2 class="mc-section-title">Public Trust <a href="/mission-control/public-trust-institutional-credibility.html" class="mc-inline-link">Trust Architecture #82 →</a></h2>
    <p class="mc-bar-note">Build #82 — Public Trust & Institutional Credibility. Trust is the product. 7-layer pyramid, trust dashboard, annual audit, founder standard. 0 corrections · audit not conducted. ~50% readiness.</p>
    <h2 class="mc-section-title">Digital Twin <a href="/mission-control/institutional-digital-twin.html" class="mc-inline-link">Executive Simulation #81 →</a></h2>
    <p class="mc-bar-note">Build #81 — Institutional Digital Twin & Executive Simulation. See entire institution before it happens. What-if scenarios, forecasting, statewide heat map, decision support. MC becomes planning system. 0 simulations · twin not live. ~51% readiness.</p>
    <h2 class="mc-section-title">Civic Institution Roadmap <a href="/mission-control/arkansas-civic-institution-roadmap.html" class="mc-inline-link">Legacy Vision #80 →</a></h2>
    <p class="mc-bar-note">Build #80 — Twenty-Year Vision & Institutional Legacy Plan. 80 builds complete. Four eras, 8 goals, legacy map, founder reflection. Website is beginning; institution is destination. Era 1 Foundation · 1/10 milestones. ~48% readiness.</p>
    <h2 class="mc-section-title">Neighborhood Operating System <a href="/mission-control/arkansas-neighborhood-operating-system.html" class="mc-inline-link">ANOS #79 →</a></h2>
    <p class="mc-bar-note">Build #79 — Master Arkansas Neighborhood Operating System. Final layer — last 500 feet. Growth cycle, health score, mentorship trees, 200K strategy. Neighborhoods build trust. 0 profiles · 0/200K connected. ~47% readiness.</p>
    <h2 class="mc-section-title">City Operating System <a href="/mission-control/arkansas-city-operating-system.html" class="mc-inline-link">ArCOS #78 →</a></h2>
    <p class="mc-bar-note">Build #78 — Master Arkansas City Operating System. 250 cities, digital twins, 6 readiness levels, neighborhood integration. Counties structure · cities connect · neighborhoods trust. 0/250 digital twins · 0 past initial interest. ~48% readiness.</p>
    <h2 class="mc-section-title">County Operating System <a href="/mission-control/arkansas-county-operating-system.html" class="mc-inline-link">ACOS #77 →</a></h2>
    <p class="mc-bar-note">Build #77 — Master Arkansas County Operating System. 75 counties, digital twins, 6 readiness levels, health index. One county at a time. 0/75 digital twins · 0 past Awareness. ~47% readiness.</p>
    <h2 class="mc-section-title">Founding Constitution <a href="/mission-control/organizational-constitution.html" class="mc-inline-link">Organizational Charter #76 →</a></h2>
    <p class="mc-bar-note">Build #76 — Master Organizational Constitution. 15 articles, 6 values, 10 departments, motto, creed, founder principle. Everything flows from this document. 0/10 departments · 0 amendments. ~46% readiness.</p>
    <h2 class="mc-section-title">Volunteer & Funding <a href="/mission-control/volunteer-funding-constitution.html" class="mc-inline-link">Independence Charter #75 →</a></h2>
    <p class="mc-bar-note">Build #75 — Volunteer & Funding Constitution. All-volunteer institution, financial independence, no special access. Educate first always. 0 volunteers · 0 funding sources. ~45% readiness.</p>
    <h2 class="mc-section-title">Reform Center <a href="/mission-control/arkansas-civic-innovation-reform.html" class="mc-inline-link">Civic Solutions #74 →</a></h2>
    <p class="mc-bar-note">Build #74 — Civic Innovation & Reform Center. Eight reform libraries, proposal framework, solution builder. Center explains; citizens decide. 0 analyses · 0/8 libraries. ~44% readiness.</p>
    <h2 class="mc-section-title">Research Institute <a href="/mission-control/arkansas-research-institute.html" class="mc-inline-link">Policy Lab #73 →</a></h2>
    <p class="mc-bar-note">Build #73 — Research Institute & Policy Innovation Laboratory. Eight divisions, research standards, policy lab. Expand knowledge not certainty. 0 projects · 0 white papers · 0/8 divisions. ~43% readiness.</p>
    <h2 class="mc-section-title">Arkansas Communications <a href="/mission-control/arkansas-communications.html" class="mc-inline-link">One Voice #72 →</a></h2>
    <p class="mc-bar-note">Build #72 — Communications & Public Education System. One institutional voice, content pyramid, editorial calendar. Education before persuasion. 0 articles · 0 videos · 0 emails. ~42% readiness.</p>
    <h2 class="mc-section-title">Community Listening <a href="/mission-control/arkansas-community-listening.html" class="mc-inline-link">Listening Network #71 →</a></h2>
    <p class="mc-bar-note">Build #71 — Community Intelligence & Listening System. Six sources, question observatory, pulse reports. Learn from Arkansas. 0 questions · 0 leader reports · 0 pulse reports. ~41% readiness.</p>
    <h2 class="mc-section-title">Arkansas Command Strategy <a href="/mission-control/arkansas-command-strategy.html" class="mc-inline-link">Statewide Execution #70 →</a></h2>
    <p class="mc-bar-note">Build #70 — Arkansas Command Strategy. 75 counties · 250 cities · 200K connected. Five phases, readiness models, flywheel. Phase 1 in progress. 0/75 · 0/250 · 0/200K. ~39% readiness.</p>
    <h2 class="mc-section-title">Relational Growth Engine <a href="/mission-control/relational-organizing-growth-engine.html" class="mc-inline-link">Network Effect #69 →</a></h2>
    <p class="mc-bar-note">Build #69 — Relational Organizing & Arkansas Growth Engine. Five-people question, share hub, relationship trees. Primary expansion. 0 trees · 0 invitations · 0/200K. ~34% readiness.</p>
    <h2 class="mc-section-title">Citizen Leadership Academy <a href="/mission-control/citizen-leadership-academy.html" class="mc-inline-link">Human Engine #68 →</a></h2>
    <p class="mc-bar-note">Build #68 — Citizen Leadership Academy. 6 certification levels, Learn→Multiply. Teachers not spokespeople. Highest priority. 0 learners · 0 graduates. ~34% readiness.</p>
    <h2 class="mc-section-title">Impact Measurement <a href="/mission-control/impact-measurement.html" class="mc-inline-link">Civic Scorecard #67 →</a></h2>
    <p class="mc-bar-note">Build #67 — Impact Measurement & Arkansas Civic Scorecard. 5 pillars, measure understanding not traffic. Overall civic score 0 · 0 leaders. ~31% readiness.</p>
    <h2 class="mc-section-title">Sustainability & Stewardship <a href="/mission-control/sustainability-stewardship.html" class="mc-inline-link">Institution That Lasts #66 →</a></h2>
    <p class="mc-bar-note">Build #66 — Sustainability, Funding & Institutional Stewardship. 5 principles, funding portfolio, volunteer stewardship. Never compromise integrity. 0 funding sources · 0 volunteers. ~38% readiness.</p>
    <h2 class="mc-section-title">Civic Intelligence Command Center <a href="/mission-control/civic-intelligence-command-center.html" class="mc-inline-link">Executive MC #65 →</a></h2>
    <p class="mc-bar-note">Build #65 — Civic Intelligence Command Center. Executive nervous system, 10 department boards, readiness index. Unifies 65 builds. 8% launch · 0 leaders. ~43% readiness.</p>
    <h2 class="mc-section-title">Arkansas Action Network <a href="/mission-control/arkansas-action-network.html" class="mc-inline-link">200K Arkansans #64 →</a></h2>
    <p class="mc-bar-note">Build #64 — Arkansas Action Network & Leadership Pipeline. 8-level pyramid, invitation engine, progress map. Primary growth engine. 0 county teams · 0/200K connected. ~38% readiness.</p>
    <h2 class="mc-section-title">Campaign Finance Observatory <a href="/mission-control/campaign-finance-observatory.html" class="mc-inline-link">Follow the Money #63 →</a></h2>
    <p class="mc-bar-note">Build #63 — Campaign Finance Data Observatory. 8 divisions, Before & After Explorer, data integrity standards. Flagship system. 0 datasets · 0 charts. ~36% readiness.</p>
    <h2 class="mc-section-title">Citizen Action Center <a href="/mission-control/citizen-action-center.html" class="mc-inline-link">Learn to Participate #62 →</a></h2>
    <p class="mc-bar-note">Build #62 — Citizen Action Center. 6 pathways, learn→participate bridge. Not advocacy. 0 registered · 2 action hub items. ~42% readiness.</p>
    <h2 class="mc-section-title">Coalition Network <a href="/mission-control/coalition-network.html" class="mc-inline-link">Building Arkansas #61 →</a></h2>
    <p class="mc-bar-note">Build #61 — Master Coalition & Civic Alliance Network. 6 categories, 4 levels, resource center. 0 orgs · 0/75 counties. Highest strategic priority. ~44% coalition readiness.</p>
    <h2 class="mc-section-title">Institutional AI <a href="/mission-control/institutional-ai.html" class="mc-inline-link">Civic Intelligence #60 →</a></h2>
    <p class="mc-bar-note">Build #60 — Institutional AI Brain. 7 roles, Rule #1 source grounding, confidence levels. Not a chatbot — evidence is authority. 0 answered · no RAG. ~42% AI readiness.</p>
    <h2 class="mc-section-title">Relationship OS <a href="/mission-control/relationship-os.html" class="mc-inline-link">Institutional CRM #59 →</a></h2>
    <p class="mc-bar-note">Build #59 — Relationship Operating System. 5 networks, CRM dashboard, health score model. 0 active relationships · 0 edges. ~54% ROS readiness.</p>
    <h2 class="mc-section-title">Civic Atlas <a href="/mission-control/civic-atlas.html" class="mc-inline-link">Geographic Intelligence #58 →</a></h2>
    <p class="mc-bar-note">Build #58 — Arkansas Civic Atlas. 7-level hierarchy, Educational Coverage Score, 75 counties at ECS=0. 0 communities · map planned. ~52% atlas readiness.</p>
    <h2 class="mc-section-title">Neighborhood Organizing <a href="/mission-control/neighborhood-organizing.html" class="mc-inline-link">Last Mile #57 →</a></h2>
    <p class="mc-bar-note">Build #57 — Neighborhood Organizing & Relational Network. 4 geographic layers, relational organizing, last mile dashboard. 0 neighborhoods · 0 leaders. ~50% last mile readiness.</p>
    <h2 class="mc-section-title">Statewide Growth <a href="/mission-control/statewide-growth.html" class="mc-inline-link">Arkansas Network #56 →</a></h2>
    <p class="mc-bar-note">Build #56 — Statewide Growth & Leadership Blueprint. 75 counties, 250 cities, 200K participant objective. 0 leaders · 0 participants. ~48% growth blueprint readiness.</p>
    <h2 class="mc-section-title">Master Plan <a href="/mission-control/master-plan.html" class="mc-inline-link">★ North Star #55 →</a></h2>
    <p class="mc-bar-note">Build #55 — Master Master Plan. Permanent constitution synthesizing 55 builds. Read first. Planning complete — translation layer next. ~56% master plan readiness.</p>
    <h2 class="mc-section-title">Build Bible <a href="/mission-control/build-bible.html" class="mc-inline-link">★ Milestone #50 →</a></h2>
    <p class="mc-bar-note">Build #50 — Master Build Bible. Planning phase complete — 50 builds, 28 systems, 12 pillars. Implementation begins. 49% bible readiness.</p>
    <h2 class="mc-section-title">Data Architecture <a href="/mission-control/data-architecture.html" class="mc-inline-link">Canonical Dictionary →</a></h2>
    <p class="mc-bar-note">Build #51 — Master Data Architecture & Canonical Data Dictionary. 12 domains (100–1200), single source of truth. 0 relationship edges. 41% data architecture readiness.</p>
    <h2 class="mc-section-title">UX Architecture <a href="/mission-control/ux-architecture.html" class="mc-inline-link">Experience Blueprint →</a></h2>
    <p class="mc-bar-note">Build #52 — Master User Experience Architecture. 7 emotional stages, Learning + Civic Compass, Action Hub live. 0 delight moments. 39% UX readiness.</p>
    <h2 class="mc-section-title">Launch Strategy <a href="/mission-control/launch-strategy.html" class="mc-inline-link">Arkansas Rollout →</a></h2>
    <p class="mc-bar-note">Build #53 — Master Launch Strategy. Phase 0 Private Development. 8% public launch readiness — not recommended. 39% launch strategy readiness.</p>
    <h2 class="mc-section-title">PMO <a href="/mission-control/pmo.html" class="mc-inline-link">Execution System →</a></h2>
    <p class="mc-bar-note">Build #54 — Master Project Management Office. 10 departments, risk register, dependency maps. 0 owners assigned. 46% PMO readiness.</p>
    <h2 class="mc-section-title">Governance & Constitution <a href="/mission-control/governance.html" class="mc-inline-link">Institutional Rules →</a></h2>
    <p class="mc-bar-note">Build #49 — Master governance & institutional constitution. 6 values, 7 steward roles. 0 stewards assigned. 44% governance readiness.</p>
    <h2 class="mc-section-title">Technical Architecture <a href="/mission-control/technical-architecture.html" class="mc-inline-link">Production Engineering →</a></h2>
    <p class="mc-bar-note">Build #48 — Master technical architecture & deployment blueprint. Next.js/Neon target. GitHub→Netlify live. 3/8 stack layers. 38% readiness.</p>
    <h2 class="mc-section-title">Visitor Journey <a href="/mission-control/visitor-journey.html" class="mc-inline-link">8 Stages →</a></h2>
    <p class="mc-bar-note">Build #47 — Master visitor journey & behavioral architecture, curiosity to legacy. 1/8 stages tracked. 0 Education Leaders. 40% journey readiness.</p>
    <h2 class="mc-section-title">Content Production Matrix <a href="/mission-control/content-production-matrix.html" class="mc-inline-link">14 Domains →</a></h2>
    <p class="mc-bar-note">Build #46 — Master content production matrix, ~2045 asset target, production queue, executive dashboard. 15 edu published. 22% matrix readiness.</p>
    <h2 class="mc-section-title">Systems Integration <a href="/mission-control/systems-integration.html" class="mc-inline-link">12 Systems →</a></h2>
    <p class="mc-bar-note">Build #45 — Master systems integration blueprint, 12 systems, information flow cycle. MC as conductor. 3/12 live data flows. 28% integration readiness.</p>
    <h2 class="mc-section-title">Institutional Roadmap <a href="/mission-control/institutional-roadmap.html" class="mc-inline-link">V1–V10 →</a></h2>
    <p class="mc-bar-note">Build #44 — Master institutional roadmap, strategic evolution V1–V10. Current: V1 Foundation. 44 builds ≠ V10. 32% institutional maturity.</p>
    <h2 class="mc-section-title">Research Methodology <a href="/mission-control/research-methodology.html" class="mc-inline-link">10 Principles →</a></h2>
    <p class="mc-bar-note">Build #43 — Master research methodology & standards, 11-stage workflow, source checklist. Extends Build #10. 25% methodology readiness.</p>
    <h2 class="mc-section-title">Civic Action Lab <a href="/mission-control/civic-action-lab.html" class="mc-inline-link">6 Divisions →</a></h2>
    <p class="mc-bar-note">Build #42 — Master civic action lab, legislative & ballot studios, comparative reforms. Educate first — not a campaign HQ. 26% lab readiness.</p>
    <h2 class="mc-section-title">Evidence Ledger <a href="/mission-control/evidence-ledger.html" class="mc-inline-link">Claims Registry →</a></h2>
    <p class="mc-bar-note">Build #41 — Master evidence ledger & claims registry, A–E strength levels, 7-stage review. 3/500 CLAIM-* records. 22% ledger readiness.</p>
    <h2 class="mc-section-title">Institutional Brain <a href="/mission-control/civic-intelligence.html" class="mc-inline-link">Civic Intelligence →</a></h2>
    <p class="mc-bar-note">Build #40 — Master knowledge graph & civic intelligence, 17 node types, 7 layers. 38/500 KG nodes. 24% brain readiness.</p>
    <h2 class="mc-section-title">Media Studio <a href="/mission-control/media-studio.html" class="mc-inline-link">8 Divisions →</a></h2>
    <p class="mc-bar-note">Build #39 — Documentary experience & multimedia learning, 6 chapters, media standards. 0 videos published. 18% media readiness.</p>
    <h2 class="mc-section-title">Interactive Learning Lab <a href="/mission-control/learning-lab.html" class="mc-inline-link">10 Labs →</a></h2>
    <p class="mc-bar-note">Build #38 — Civic discovery & simulation, 10 laboratories, accessibility standards. 0 interactive experiences live. 22% lab readiness.</p>
    <h2 class="mc-section-title">Master Research Library <a href="/mission-control/research-library.html" class="mc-inline-link">7 Collections →</a></h2>
    <p class="mc-bar-note">Build #37 — Digital archive A–G, reading lists, relationship engine. Preserve don't summarize. 22% library readiness.</p>
    <h2 class="mc-section-title">Trust Framework <a href="/mission-control/trust.html" class="mc-inline-link">Public Trust OS →</a></h2>
    <p class="mc-bar-note">Build #36 — Evidence, transparency, trust pyramid, A–D evidence levels. v2 DB: Netlify or Neon. 24% trust readiness.</p>
    <h2 class="mc-section-title">Master Curriculum <a href="/mission-control/curriculum.html" class="mc-inline-link">6 Tiers →</a></h2>
    <p class="mc-bar-note">Build #35 — Educational framework, 6 learning paths, 4 reading levels. Understanding before opinion. 26% curriculum readiness.</p>
    <h2 class="mc-section-title">Narrative Architecture <a href="/mission-control/narrative.html" class="mc-inline-link">8 Acts →</a></h2>
    <p class="mc-bar-note">Build #34 — Educational narrative system, 4 storytelling layers, documentary museum journey. 24% narrative readiness.</p>
    <h2 class="mc-section-title">Encyclopedia & Knowledge Library <a href="/mission-control/encyclopedia.html" class="mc-inline-link">9 Categories →</a></h2>
    <p class="mc-bar-note">Build #33 — Living encyclopedia, 9-section entry structure, completion score, KG relationship graph. 19% encyclopedia readiness.</p>
    <h2 class="mc-section-title">Educational Campaign OS <a href="/mission-control/campaign-os.html" class="mc-inline-link">4 Horizons →</a></h2>
    <p class="mc-bar-note">Build #32 — Multi-year strategic growth blueprint, annual cycle, quarterly reviews, innovation pipeline. Horizon One active.</p>
    <h2 class="mc-section-title">County Operating System <a href="/mission-control/county-os.html" class="mc-inline-link">75 Counties →</a></h2>
    <p class="mc-bar-note">Build #31 — County profiles, education score, leadership roles, regional groupings. 28% county OS readiness.</p>
    <h2 class="mc-section-title">Outreach Engine <a href="/mission-control/outreach.html" class="mc-inline-link">Arkansas Campaigns →</a></h2>
    <p class="mc-bar-note">Build #30 — 5 pillars, 7 campaigns, share toolkit, county outreach. 22% outreach readiness.</p>
    <h2 class="mc-section-title">Research Observatory <a href="/mission-control/research-observatory.html" class="mc-inline-link">Early Warning System →</a></h2>
    <p class="mc-bar-note">Build #29 — 6 research divisions, 9-stage workflow, legislative tracking, gap tracker. 18% observatory readiness.</p>
    <h2 class="mc-section-title">Education Academy <a href="/mission-control/education-academy.html" class="mc-inline-link">Leader Development →</a></h2>
    <p class="mc-bar-note">Build #28 — 4 learning stages, 8 curriculum modules, certification, presentation toolkit. 24% academy readiness.</p>
    <h2 class="mc-section-title">Content Production Factory <a href="/mission-control/content-factory.html" class="mc-inline-link">Editorial OS →</a></h2>
    <p class="mc-bar-note">Build #27 — 7 content types, 11-stage workflow, standard article structure, evergreen review. 28% factory readiness.</p>
    <h2 class="mc-section-title">AI Knowledge Engine <a href="/mission-control/ai-knowledge.html" class="mc-inline-link">Educational Intelligence →</a></h2>
    <p class="mc-bar-note">Build #26 — Arkansas Civic Librarian, 5 learning modes, evidence-first responses, guardrails. Architecture only — 14% readiness.</p>
    <h2 class="mc-section-title">Executive Command Center <a href="/mission-control/executive.html" class="mc-inline-link">MC 2.0 →</a></h2>
    <p class="mc-bar-note">Build #25 — 9 workspaces, health indicators, smart alerts, build timeline, Arkansas readiness map.</p>
    <h2 class="mc-section-title">Contact Intelligence <a href="/mission-control/contact-intelligence.html" class="mc-inline-link">Relationship Network →</a></h2>
    <p class="mc-bar-note">Build #24 — Civic Education Profiles, interest/skills taxonomies, county intelligence, privacy-first relationship architecture.</p>
    <h2 class="mc-section-title">Wireframe Blueprint <a href="/mission-control/wireframes.html" class="mc-inline-link">25 Screens →</a></h2>
    <p class="mc-bar-note">Build #23 — Screen architecture, sections per route, outcome mapping, mobile requirements.</p>
    <h2 class="mc-section-title">Database Schema <a href="/mission-control/database.html" class="mc-inline-link">Entity Blueprint →</a></h2>
    <p class="mc-bar-note">Build #22 — 15 entities, 10 join tables, v1 static storage, Supabase/Postgres migration path.</p>
    <h2 class="mc-section-title">Repository Blueprint <a href="/mission-control/repository.html" class="mc-inline-link">Folder Structure →</a></h2>
    <p class="mc-bar-note">Build #21 — Branch model, target src/ layout, docs taxonomy, scripts, GitHub labels &amp; milestones.</p>
    <h2 class="mc-section-title">Platform Architecture <a href="/mission-control/platform.html" class="mc-inline-link">Technical Blueprint →</a></h2>
    <p class="mc-bar-note">Build #20 — Stack, data, security, v1 success criteria, implementation roadmap (#21–#25).</p>
    <h2 class="mc-section-title">Knowledge Atlas <a href="/mission-control/atlas.html" class="mc-inline-link">Learning Worlds →</a></h2>
    <p class="mc-bar-note">Build #19 — 7 learning worlds, 51 districts, 6 knowledge trails, Learning Compass schema.</p>
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

async function initKnowledgeAtlasBlueprint() {
  const root = document.getElementById('mc-atlas-root');
  if (!root) return;

  const [atlasRes, mcRes] = await Promise.all([
    fetch('/data/knowledge-atlas.json'),
    fetch('/data/mission-control.json')
  ]);
  const atlas = await atlasRes.json();
  const mc = await mcRes.json();
  const s = atlas.summary;
  const ec = atlas.educational_completion;

  const worldSections = atlas.worlds.map(w => {
    const rows = w.districts.map(d => `
      <tr class="${d.status === 'live' ? 'mc-table__row--approved' : ''}">
        <td><code>${d.id}</code></td>
        <td>${d.title}</td>
        <td>${d.status}</td>
        <td>${d.completion_pct}%</td>
        <td>${(d.routes || []).map(r => `<a href="${r}">${r}</a>`).join('<br>') || '—'}</td>
      </tr>`).join('');
    return `
      <h2 class="mc-section-title">World ${w.number} — ${w.title} (${w.completion_pct}%)</h2>
      <p class="mc-bar-note">${w.purpose}</p>
      <table class="mc-table">
        <thead><tr><th>ID</th><th>District</th><th>Status</th><th>Complete</th><th>Routes</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>`;
  }).join('');

  const trailCards = atlas.trails.map(t => `
    <div class="mc-card">
      <h3>${t.title}</h3>
      ${t.duration ? `<p class="mc-bar-note">${t.duration}${t.audience ? ' · ' + t.audience : ''}</p>` : ''}
      ${t.focus ? `<p class="mc-bar-note">${t.focus}</p>` : ''}
      <ol class="mc-deliverables">${t.stops.map(st => `<li><a href="${st.route}">${st.title || st.route}</a></li>`).join('')}</ol>
    </div>`).join('');

  const completionRows = Object.entries(ec)
    .filter(([k]) => k !== 'overall_educational_readiness')
    .map(([k, v]) => `<tr><td>${k.replace(/_/g, ' ')}</td><td>${v}%</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Knowledge Atlas</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #19 · ${atlas.title}</p>
      <h1>Knowledge Atlas &amp; Learning Paths</h1>
      <p class="mc-header__question"><em>${atlas.core_question}</em></p>
    </header>
    <section class="mc-card">
      <h3>${atlas.organization}</h3>
      <p class="mc-bar-note"><strong>${atlas.platform}</strong></p>
      <p class="mc-bar-note">${atlas.governing_principle}</p>
    </section>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Learning worlds</div><div class="mc-stat__value">${s.worlds}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Districts</div><div class="mc-stat__value">${s.districts}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live districts</div><div class="mc-stat__value">${s.districts_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Partial</div><div class="mc-stat__value">${s.districts_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned / stub</div><div class="mc-stat__value">${s.districts_planned + s.districts_stub}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Knowledge trails</div><div class="mc-stat__value">${s.trails}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Mapped routes</div><div class="mc-stat__value">${s.mapped_routes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Educational readiness</div><div class="mc-stat__value">${ec.overall_educational_readiness}%</div></div>
    </div>
    <h2 class="mc-section-title">Educational Completion</h2>
    <p class="mc-bar-note">Measures institutional maturity — not page count alone.</p>
    <table class="mc-table"><thead><tr><th>Dimension</th><th>Coverage</th></tr></thead><tbody>${completionRows}</tbody></table>
    <h2 class="mc-section-title">Atlas Map Hierarchy</h2>
    <div class="mc-dep-map">${atlas.atlas_map_hierarchy.map((l, i) => `
      <span class="mc-dep-map__node"><span class="mc-dep-map__num">${l.level}</span><span class="mc-dep-map__label">${l.title}${l.count ? ' (' + l.count + ')' : ''}</span></span>
      ${i < atlas.atlas_map_hierarchy.length - 1 ? '<span class="mc-dep-map__arrow">↓</span>' : ''}`).join('')}</div>
    <h2 class="mc-section-title">Learning Compass (${atlas.learning_compass.status})</h2>
    <p class="mc-bar-note">${atlas.learning_compass.note}</p>
    <ul class="mc-deliverables">${atlas.learning_compass.fields.map(f => `<li><strong>${f.label}</strong>${f.source ? ' — ' + f.source : ''}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Educational Checkpoints</h2>
    <ul class="mc-deliverables">${atlas.checkpoints.map(c => `<li>${c.title}</li>`).join('')}</ul>
    ${worldSections}
    <h2 class="mc-section-title">Knowledge Trails (${atlas.trails.length})</h2>
    <div class="mc-grid-2">${trailCards}</div>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${atlas.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${atlas.recommended_next_build.number} — ${atlas.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${atlas.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/KNOWLEDGE_ATLAS.md">KNOWLEDGE_ATLAS.md</a> ·
      <a href="/data/knowledge-atlas.json">Atlas JSON</a> ·
      <a href="/mission-control/facts.html">Facts Framework</a> ·
      <a href="/mission-control/journey.html">UX Journey</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initPlatformArchitectureBlueprint() {
  const root = document.getElementById('mc-platform-root');
  if (!root) return;

  const [archRes, mcRes] = await Promise.all([
    fetch('/data/platform-architecture.json'),
    fetch('/data/mission-control.json')
  ]);
  const arch = await archRes.json();
  const mc = await mcRes.json();
  const s = arch.summary;

  const stackRows = arch.technology_stack.map(l => `
    <tr class="${l.status === 'live' ? 'mc-table__row--approved' : ''}">
      <td>${l.title}</td>
      <td>${l.status}</td>
      <td>${l.current_implementation || '—'}</td>
    </tr>`).join('');

  const objRows = arch.objectives.map(o => `
    <tr><td>${o.title}</td><td>${o.status}</td><td>${o.readiness_pct}%</td></tr>`).join('');

  const moduleSections = arch.platform_modules.map(m => {
    const caps = m.capabilities.map(c => `<li>${c.cap} — <em>${c.status}</em></li>`).join('');
    return `<div class="mc-card"><h3>${m.title}</h3><ul class="mc-deliverables">${caps}</ul><p class="mc-bar-note"><a href="${m.route}">${m.route}</a></p></div>`;
  }).join('');

  const v1Rows = arch.v1_success_criteria.map(c => `
    <tr class="${c.status === 'live' ? 'mc-table__row--approved' : ''}">
      <td>${c.criterion}</td><td>${c.status}</td><td>${c.pct}%</td>
    </tr>`).join('');

  const roadmapRows = arch.implementation_roadmap.map(r => `
    <tr><td>#${r.build}</td><td>${r.title}</td><td>${r.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Platform Architecture</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #20 · ${arch.title}</p>
      <h1>Master Platform Blueprint</h1>
      <p class="mc-header__question"><strong>${arch.philosophy}</strong></p>
    </header>
    <section class="mc-card">
      <h3>Platform Identity</h3>
      <p class="mc-bar-note"><strong>${arch.platform}</strong></p>
      <p class="mc-bar-note">${arch.organization} <em>(${arch.organization_note})</em></p>
      <p class="mc-bar-note">${arch.governing_principle}</p>
    </section>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Stack layers</div><div class="mc-stat__value">${s.stack_layers}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live</div><div class="mc-stat__value">${s.stack_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Partial</div><div class="mc-stat__value">${s.stack_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Architecture readiness</div><div class="mc-stat__value">${s.architecture_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">V1 success avg</div><div class="mc-stat__value">${s.v1_success_avg_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">MC systems live</div><div class="mc-stat__value">${s.mc_systems_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Objectives avg</div><div class="mc-stat__value">${s.objectives_avg_readiness}%</div></div>
    </div>
    <h2 class="mc-section-title">Platform Objectives</h2>
    <table class="mc-table"><thead><tr><th>Objective</th><th>Status</th><th>Readiness</th></tr></thead><tbody>${objRows}</tbody></table>
    <h2 class="mc-section-title">Technology Stack</h2>
    <table class="mc-table"><thead><tr><th>Layer</th><th>Status</th><th>Current</th></tr></thead><tbody>${stackRows}</tbody></table>
    <p class="mc-bar-note">Technical philosophy: ${arch.technical_philosophy.join(' · ')}</p>
    <h2 class="mc-section-title">Content &amp; Data Architecture</h2>
    <p class="mc-bar-note">Page metadata: ${arch.content_architecture.page_metadata.join(', ')}</p>
    <ul class="mc-deliverables">${arch.content_architecture.trackers.map(t => `<li><strong>${t.system}</strong> (Build #${t.build}) — <a href="${t.route}">${t.route}</a></li>`).join('')}</ul>
    <p class="mc-bar-note">Canonical objects (${arch.data_architecture.canonical_objects.length}): ${arch.data_architecture.canonical_objects.join(', ')} · Database: ${arch.data_architecture.database.status} (Build #${arch.data_architecture.database.build})</p>
    <h2 class="mc-section-title">Mission Control Systems</h2>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${arch.mission_control_systems.map(m => `<tr><td>${m.label}</td><td>${m.status}</td><td><a href="${m.route}">${m.route}</a></td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Platform Modules</h2>
    <div class="mc-grid-2">${moduleSections}</div>
    <h2 class="mc-section-title">Security Principles</h2>
    <table class="mc-table"><thead><tr><th>Requirement</th><th>Status</th><th>Note</th></tr></thead>
      <tbody>${arch.security_principles.map(x => `<tr><td>${x.req}</td><td>${x.status}</td><td>${x.note || ''}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Performance Standards</h2>
    <ul class="mc-deliverables">${arch.performance_standards.map(p => `<li><strong>${p.std}</strong> — ${p.status}${p.note ? ' (' + p.note + ')' : ''}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Development Workflow</h2>
    <div class="mc-dep-map">${arch.development_workflow.map((w, i) => `
      <span class="mc-dep-map__node"><span class="mc-dep-map__num">${w.stage}</span><span class="mc-dep-map__label">${w.title}</span></span>
      ${i < arch.development_workflow.length - 1 ? '<span class="mc-dep-map__arrow">→</span>' : ''}`).join('')}</div>
    <h2 class="mc-section-title">Version 1 Success Criteria</h2>
    <table class="mc-table"><thead><tr><th>Criterion</th><th>Status</th><th>Progress</th></tr></thead><tbody>${v1Rows}</tbody></table>
    <h2 class="mc-section-title">Implementation Roadmap (Builds #21–#25)</h2>
    <table class="mc-table"><thead><tr><th>Build</th><th>Title</th><th>Status</th></tr></thead><tbody>${roadmapRows}</tbody></table>
    <h2 class="mc-section-title">Scalability Targets</h2>
    <ul class="mc-deliverables">${arch.scalability_targets.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${arch.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Related Architecture</h2>
    <ul class="mc-deliverables">${arch.integrations.map(i => `<li><strong>${i.system}</strong> (Build #${i.build}) — <a href="${i.route}">${i.route}</a>${i.note ? ' — ' + i.note : ''}</li>`).join('')}</ul>
    <p class="mc-bar-note">
      <a href="/docs/PLATFORM_ARCHITECTURE.md">PLATFORM_ARCHITECTURE.md</a> ·
      <a href="/data/platform-architecture.json">JSON</a> ·
      <a href="/mission-control/architecture.html">Site IA</a> ·
      <a href="/mission-control/data-model.html">Data Model</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initRepositoryBlueprint() {
  const root = document.getElementById('mc-repository-root');
  if (!root) return;

  const [bpRes, mcRes] = await Promise.all([
    fetch('/data/repository-blueprint.json'),
    fetch('/data/mission-control.json')
  ]);
  const bp = await bpRes.json();
  const mc = await mcRes.json();
  const s = bp.summary;
  const cur = bp.current_layout;

  const workstreamRows = bp.workstreams.map(w => `
    <tr class="${w.status === 'live' ? 'mc-table__row--approved' : ''}">
      <td>${w.title}</td><td>${w.status}</td>
      <td>${w.current_paths.join(', ')}</td>
    </tr>`).join('');

  const docsRows = bp.docs_folders.map(d => `
    <tr><td><code>${d.path}</code></td><td>${d.status}</td><td>${d.current_mapping}</td></tr>`).join('');

  const srcRows = bp.src_folders.map(f => `
    <tr><td><code>${f.path}</code></td><td>${f.status}</td><td>${f.current_mapping}</td></tr>`).join('');

  const scriptRows = bp.target_scripts.map(sc => `
    <tr><td><code>${sc.name}</code></td><td>${sc.status}</td><td>${sc.current_equivalent || '—'}</td></tr>`).join('');

  const migRows = bp.migration_map.map(m => `
    <tr><td>${m.from}</td><td>${m.to}</td><td>${m.status}</td></tr>`).join('');

  const milestoneRows = bp.github_milestones.map(m => `
    <tr class="${m.status === 'complete' ? 'mc-table__row--approved' : ''}">
      <td>${m.number}</td><td>${m.title}</td><td>${m.status}</td>
    </tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Repository Blueprint</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #21 · ${bp.title}</p>
      <h1>GitHub &amp; Folder Structure</h1>
      <p class="mc-header__question">${bp.philosophy}</p>
    </header>
    <section class="mc-card">
      <h3>Repository Names</h3>
      <p class="mc-bar-note"><strong>Recommended:</strong> <code>${bp.repository_names.recommended}</code></p>
      <p class="mc-bar-note"><strong>Current remote:</strong> <a href="https://github.com/${bp.repository_names.current_remote}">${bp.repository_names.current_remote}</a> · Local: <code>${bp.repository_names.current_local}</code></p>
      <p class="mc-bar-note"><em>${s.note}</em></p>
    </section>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Workstreams</div><div class="mc-stat__value">${s.workstreams}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Structure readiness</div><div class="mc-stat__value">${s.structure_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Current pattern</div><div class="mc-stat__value" style="font-size:1rem">${cur.pattern}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Has src/</div><div class="mc-stat__value">${cur.has_src ? 'Yes' : 'No'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Scripts</div><div class="mc-stat__value">${cur.script_count} ${cur.scripts_language}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Migration done</div><div class="mc-stat__value">${s.migration_executed ? 'Yes' : 'No'}</div></div>
    </div>
    <h2 class="mc-section-title">Four Workstreams</h2>
    <table class="mc-table"><thead><tr><th>Workstream</th><th>Status</th><th>Current paths</th></tr></thead><tbody>${workstreamRows}</tbody></table>
    <h2 class="mc-section-title">Branch Structure</h2>
    <table class="mc-table"><thead><tr><th>Branch</th><th>Purpose</th><th>Status</th></tr></thead>
      <tbody>${bp.branch_structure.map(b => `<tr><td><code>${b.name}</code></td><td>${b.purpose}</td><td>${b.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Current Layout (v0)</h2>
    <p class="mc-bar-note">${cur.description}</p>
    <p class="mc-bar-note">Root folders: ${cur.root_folders.join(', ')}</p>
    <h2 class="mc-section-title">Target docs/ Taxonomy</h2>
    <table class="mc-table"><thead><tr><th>Folder</th><th>Status</th><th>Current mapping</th></tr></thead><tbody>${docsRows}</tbody></table>
    <h2 class="mc-section-title">Target src/ Structure</h2>
    <table class="mc-table"><thead><tr><th>Folder</th><th>Status</th><th>Current mapping</th></tr></thead><tbody>${srcRows}</tbody></table>
    <h2 class="mc-section-title">Target Scripts</h2>
    <table class="mc-table"><thead><tr><th>Script</th><th>Status</th><th>Current equivalent</th></tr></thead><tbody>${scriptRows}</tbody></table>
    <h2 class="mc-section-title">Package Scripts</h2>
    <p class="mc-bar-note"><strong>Current:</strong> <code>${Object.keys(bp.package_scripts.current).join(', ')}</code></p>
    <p class="mc-bar-note"><strong>Target:</strong> dev, build, check, mission-control, content:validate, sources:validate, routes:validate</p>
    <h2 class="mc-section-title">Netlify</h2>
    <p class="mc-bar-note"><strong>Current:</strong> publish <code>${bp.netlify.current.publish}</code> — ${bp.netlify.current.note}</p>
    <p class="mc-bar-note"><strong>Target:</strong> <code>npm run build</code> → <code>${bp.netlify.target.publish}</code> (Node ${bp.netlify.target.node_version})</p>
    <h2 class="mc-section-title">Migration Map</h2>
    <table class="mc-table"><thead><tr><th>From</th><th>To</th><th>Status</th></tr></thead><tbody>${migRows}</tbody></table>
    <h2 class="mc-section-title">GitHub Labels (${bp.github_labels.length})</h2>
    <p class="mc-bar-note">${bp.github_labels.map(l => `<code>${l}</code>`).join(' ')}</p>
    <h2 class="mc-section-title">GitHub Milestones</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Milestone</th><th>Status</th></tr></thead><tbody>${milestoneRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${bp.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${bp.recommended_next_build.number} — ${bp.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${bp.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/REPOSITORY_ARCHITECTURE.md">REPOSITORY_ARCHITECTURE.md</a> ·
      <a href="/data/repository-blueprint.json">JSON</a> ·
      <a href="/mission-control/platform.html">Platform Blueprint</a> ·
      <a href="https://github.com/${bp.repository_names.current_remote}">GitHub</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initDatabaseSchemaBlueprint() {
  const root = document.getElementById('mc-database-root');
  if (!root) return;

  const [schemaRes, mcRes] = await Promise.all([
    fetch('/data/database-schema.json'),
    fetch('/data/mission-control.json')
  ]);
  const schema = await schemaRes.json();
  const mc = await mcRes.json();
  const s = schema.summary;
  const cm = schema.canonical_model;

  const entityRows = schema.entities.map(e => `
    <tr class="${e.storage_status === 'live' ? 'mc-table__row--approved' : ''}">
      <td><code>${e.table}</code></td>
      <td>${e.title}</td>
      <td>${e.fields.length}</td>
      <td>${e.storage_status}</td>
      <td>${e.canonical_model_id || '—'}</td>
    </tr>`).join('');

  const joinRows = schema.join_tables.map(j => `
    <tr><td><code>${j.table}</code></td><td>${j.from} → ${j.to}</td><td>${j.status}</td></tr>`).join('');

  const metricRows = schema.mission_control_metrics.map(m => `
    <tr><td>${m.title}</td><td><code>${m.source}</code></td><td>${m.current}</td></tr>`).join('');

  const erMermaid = `erDiagram
    PERSON ||--o{ PERSON_ORGANIZATIONS : joins
    ORGANIZATION ||--o{ PERSON_ORGANIZATIONS : has
    COUNTY ||--o{ PERSON : contains
    COUNTY ||--o{ ORGANIZATION : contains
    COUNTY ||--o{ EVENT : hosts
    PERSON ||--o{ EVENT : hosts
    ORGANIZATION ||--o{ EVENT : hosts
    EVENT ||--o{ EVENT_RESOURCES : uses
    EDUCATIONAL_RESOURCE ||--o{ EVENT_RESOURCES : supports
    FACT ||--o{ FACT_SOURCES : cites
    SOURCE ||--o{ FACT_SOURCES : supports
    PERSON ||--o{ REFERRAL : sends
    PERSON ||--o{ EDUCATIONAL_PACKET_SHARE : shares
    PUBLIC_OFFICIAL ||--o{ EDUCATIONAL_PACKET_SHARE : receives
    ORGANIZATION ||--o{ COALITION_SIGN_ON : signs`;

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Database Schema</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #22 · ${schema.title}</p>
      <h1>Database Schema &amp; ERD</h1>
      <p class="mc-header__question">${schema.purpose}</p>
    </header>
    <section class="mc-card">
      <h3>${schema.platform}</h3>
      <p class="mc-bar-note"><strong>Database deployed:</strong> ${s.database_deployed ? 'Yes' : 'No'} · <strong>v1 storage:</strong> ${s.v1_storage}</p>
      <p class="mc-bar-note"><strong>Migration target:</strong> ${s.migration_target}</p>
      <p class="mc-bar-note">${schema.governing_principle}</p>
    </section>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Entities</div><div class="mc-stat__value">${s.entities}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Join tables</div><div class="mc-stat__value">${s.join_tables}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Fields</div><div class="mc-stat__value">${s.fields_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Schema readiness</div><div class="mc-stat__value">${s.schema_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live entities</div><div class="mc-stat__value">${s.entities_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Partial</div><div class="mc-stat__value">${s.entities_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned/stub</div><div class="mc-stat__value">${s.entities_planned + s.entities_stub}</div></div>
    </div>
    <h2 class="mc-section-title">Data Philosophy</h2>
    <ul class="mc-deliverables">${schema.philosophy_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Primary Entities (${s.entities})</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:400px;overflow-y:auto">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>Table</th><th>Entity</th><th>Fields</th><th>Storage</th><th>Canonical ID</th></tr></thead>
        <tbody>${entityRows}</tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Entity Relationships (ERD overview)</h2>
    <pre class="mc-bar-note" style="white-space:pre-wrap;font-size:0.85rem">${erMermaid}</pre>
    <h2 class="mc-section-title">Join Tables (${s.join_tables})</h2>
    <table class="mc-table"><thead><tr><th>Table</th><th>Relationship</th><th>Status</th></tr></thead><tbody>${joinRows}</tbody></table>
    <h2 class="mc-section-title">Signup Types (${schema.signup_types.length})</h2>
    <p class="mc-bar-note">${schema.signup_types.join(' · ')}</p>
    <h2 class="mc-section-title">Canonical Model Link (Build #${cm.build})</h2>
    <p class="mc-bar-note">${cm.objects_in_canonical} canonical objects → ${cm.objects_in_schema} schema entities. New: ${cm.new_entities.join(', ')}.</p>
    <p class="mc-bar-note"><a href="${cm.route}">Data Model dashboard →</a> · ${cm.relationship_types} relationship types</p>
    <h2 class="mc-section-title">v1 Storage Strategy</h2>
    <table class="mc-table"><thead><tr><th>Method</th><th>Status</th><th>Examples</th></tr></thead>
      <tbody>${schema.storage_strategy.v1_current.map(x => `<tr><td>${x.method}</td><td>${x.status}</td><td>${(x.examples || []).join(', ')}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Future Storage</h2>
    <ul class="mc-deliverables">${schema.storage_strategy.v2_future.map(x => `<li><strong>${x.method}</strong> — ${x.status}${x.note ? ' (' + x.note + ')' : ''}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Mission Control Metrics</h2>
    <table class="mc-table"><thead><tr><th>Metric</th><th>Source</th><th>Current</th></tr></thead><tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Privacy</h2>
    <p class="mc-bar-note">${schema.privacy_principle}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${schema.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${schema.recommended_next_build.number} — ${schema.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${schema.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/DATABASE_SCHEMA.md">DATABASE_SCHEMA.md</a> ·
      <a href="/data/database-schema.json">JSON</a> ·
      <a href="/mission-control/data-model.html">Canonical Data Model</a> ·
      <a href="/mission-control/facts.html">Facts</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initWireframeBlueprint() {
  const root = document.getElementById('mc-wireframes-root');
  if (!root) return;

  const [wfRes, mcRes] = await Promise.all([
    fetch('/data/wireframe-blueprint.json'),
    fetch('/data/mission-control.json')
  ]);
  const wf = await wfRes.json();
  const mc = await mcRes.json();
  const s = wf.summary;
  const outcomeLabels = wf.outcomes;

  const screenRows = wf.screens.map(sc => `
    <tr class="${sc.implementation_status === 'live' ? 'mc-table__row--approved' : ''}">
      <td>${sc.number}</td>
      <td><strong>${sc.title}</strong></td>
      <td><code>${sc.route}</code></td>
      <td>${outcomeLabels[sc.outcome] || sc.outcome}</td>
      <td>${sc.section_count}</td>
      <td>${sc.wireframe_status}</td>
      <td>${sc.implementation_status}</td>
    </tr>`).join('');

  const detailCards = wf.screens.map(sc => `
    <div class="mc-card">
      <h3>${sc.number}. ${sc.title}</h3>
      <p class="mc-bar-note"><code>${sc.route}</code> · ${sc.primary_goal}</p>
      <p class="mc-bar-note">Current: <code>${sc.current_route || '—'}</code> · World: ${sc.learning_world || '—'}</p>
      <ol class="mc-deliverables">${sc.sections.map(sec => `<li>${sec}</li>`).join('')}</ol>
      ${sc.notes ? `<p class="mc-bar-note"><em>${sc.notes}</em></p>` : ''}
    </div>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Wireframe Blueprint</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #23 · ${wf.title}</p>
      <h1>Major Screen Wireframes</h1>
      <p class="mc-header__question">${wf.screen_principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Screens</div><div class="mc-stat__value">${s.screens}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Sections</div><div class="mc-stat__value">${s.sections_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Wireframe readiness</div><div class="mc-stat__value">${s.wireframe_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Impl. live</div><div class="mc-stat__value">${s.implementation_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Impl. partial</div><div class="mc-stat__value">${s.implementation_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned/stub</div><div class="mc-stat__value">${s.implementation_planned}</div></div>
    </div>
    <h2 class="mc-section-title">Four Outcomes</h2>
    <ul class="mc-deliverables">${Object.entries(outcomeLabels).map(([k, v]) => `<li><strong>${k}</strong> — ${v} (${s.by_outcome[k] || 0} screens)</li>`).join('')}</ul>
    <h2 class="mc-section-title">Screen Inventory</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:360px;overflow-y:auto">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>#</th><th>Screen</th><th>Route</th><th>Outcome</th><th>Sections</th><th>Wireframe</th><th>Impl.</th></tr></thead>
        <tbody>${screenRows}</tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Global Components</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Component</th><th>Used on</th></tr></thead>
      <tbody>${wf.global_components.map(c => `<tr><td><code>${c.id}</code></td><td>${c.title}</td><td>${c.screens}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Mobile Requirements</h2>
    <ul class="mc-deliverables">${wf.mobile_requirements.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Screen Section Details (${s.screens})</h2>
    <div class="mc-grid-2">${detailCards}</div>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${wf.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${wf.recommended_next_build.number} — ${wf.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${wf.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/WIREFRAME_BLUEPRINT.md">WIREFRAME_BLUEPRINT.md</a> ·
      <a href="/data/wireframe-blueprint.json">JSON</a> ·
      <a href="/mission-control/routes.html">Route Registry</a> ·
      <a href="/mission-control/components.html">Components</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initContactIntelligenceBlueprint() {
  const root = document.getElementById('mc-contact-intelligence-root');
  if (!root) return;

  const [ciRes, mcRes] = await Promise.all([
    fetch('/data/contact-intelligence.json'),
    fetch('/data/mission-control.json')
  ]);
  const ci = await ciRes.json();
  const mc = await mcRes.json();
  const s = ci.summary;
  const tax = ci.taxonomies;

  const moduleRows = ci.modules.map(m => `
    <tr class="${m.implementation_status === 'partial' ? 'mc-table__row--approved' : ''}">
      <td><code>${m.id}</code></td>
      <td><strong>${m.title}</strong></td>
      <td>${m.field_count}</td>
      <td>${m.database_entity || '—'}</td>
      <td>${m.implementation_status}</td>
    </tr>`).join('');

  const moduleCards = ci.modules.map(m => `
    <div class="mc-card">
      <h3>${m.id} — ${m.title}</h3>
      <p class="mc-bar-note">${m.purpose}</p>
      <p class="mc-bar-note">Entity: <code>${m.database_entity || 'policy'}</code> · Status: ${m.implementation_status}</p>
      <ul class="mc-deliverables">${m.fields.map(f => {
        const label = typeof f === 'string' ? f : (f.name || f);
        return `<li>${label}</li>`;
      }).join('')}</ul>
      ${m.notes ? `<p class="mc-bar-note"><em>${m.notes}</em></p>` : ''}
    </div>`).join('');

  const metricRows = ci.mc_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td><code>${m.entity}</code></td><td>${m.status}</td></tr>`).join('');

  const integrationRows = ci.integrations.map(i => `
    <tr><td>${i.system}</td><td>${i.route ? `<code>${i.route}</code>` : '—'}</td><td>${i.type}</td><td>${i.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Contact Intelligence</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #24 · ${ci.title}</p>
      <h1>Arkansas Community Intelligence</h1>
      <p class="mc-header__question">${ci.governing_principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Modules</div><div class="mc-stat__value">${s.modules}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Fields</div><div class="mc-stat__value">${s.fields_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Readiness</div><div class="mc-stat__value">${s.contact_intelligence_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Interest topics</div><div class="mc-stat__value">${s.interest_topics}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Skills</div><div class="mc-stat__value">${s.skills_defined}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">MC metrics</div><div class="mc-stat__value">${s.mc_metrics_defined}</div></div>
    </div>
    <h2 class="mc-section-title">Relationship Philosophy</h2>
    <p class="mc-bar-note">${ci.relationship_philosophy}</p>
    <h2 class="mc-section-title">Taxonomies</h2>
    <div class="mc-grid-2">
      <div class="mc-card"><h3>Interest Topics (${tax.interests.length})</h3><ul class="mc-deliverables">${tax.interests.map(t => `<li>${t}</li>`).join('')}</ul></div>
      <div class="mc-card"><h3>Skills Inventory (${tax.skills.length})</h3><ul class="mc-deliverables">${tax.skills.map(t => `<li>${t}</li>`).join('')}</ul></div>
      <div class="mc-card"><h3>Community Connections (${tax.community_connections.length})</h3><ul class="mc-deliverables">${tax.community_connections.map(t => `<li>${t}</li>`).join('')}</ul></div>
      <div class="mc-card"><h3>Communication Preferences (${tax.communication_preferences.length})</h3><ul class="mc-deliverables">${tax.communication_preferences.map(t => `<li>${t}</li>`).join('')}</ul></div>
    </div>
    <h2 class="mc-section-title">Module Inventory</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:360px;overflow-y:auto">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>ID</th><th>Module</th><th>Fields</th><th>Entity</th><th>Status</th></tr></thead>
        <tbody>${moduleRows}</tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Mission Control Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Entity</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Privacy & Trust</h2>
    <ul class="mc-deliverables">${tax.privacy_principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Future Integrations (${s.integrations_mapped})</h2>
    <table class="mc-table"><thead><tr><th>System</th><th>Route</th><th>Type</th><th>Status</th></tr></thead>
      <tbody>${integrationRows}</tbody></table>
    <h2 class="mc-section-title">Module Details (${s.modules})</h2>
    <div class="mc-grid-2">${moduleCards}</div>
    <h2 class="mc-section-title">Related Registries</h2>
    <ul class="mc-deliverables">${ci.related_registries.map(r => `<li><a href="${r.route}">${r.title}</a> (Build #${r.build})</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ci.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ci.recommended_next_build.number} — ${ci.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ci.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/CONTACT_INTELLIGENCE.md">CONTACT_INTELLIGENCE.md</a> ·
      <a href="/data/contact-intelligence.json">JSON</a> ·
      <a href="/mission-control/database.html">Database Schema</a> ·
      <a href="/mission-control/data-model.html">Data Model</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initExecutiveCommandCenter() {
  const root = document.getElementById('mc-executive-root');
  if (!root) return;

  const [mc2Res, mcRes] = await Promise.all([
    fetch('/data/mc2-executive.json'),
    fetch('/data/mission-control.json')
  ]);
  const mc2 = await mc2Res.json();
  const mc = await mcRes.json();
  const s = mc2.summary;
  const ex = mc.executive || {};

  const panelCards = mc2.executive_panels.map(p => {
    if (p.id === 'MC2-EP-04' && typeof p.value === 'object') {
      const v = p.value;
      return `<div class="mc-card"><h3>${p.title}</h3>
        <div class="mc-phase-item"><span>Educational</span><span>${v.educational}%</span></div>
        <div class="mc-phase-item"><span>Technical</span><span>${v.technical}%</span></div>
        <div class="mc-phase-item"><span>Research</span><span>${v.research}%</span></div>
        <div class="mc-phase-item"><span>Coalition</span><span>${v.coalition}%</span></div>
        <div class="mc-phase-item"><span>Launch</span><span>${v.launch}%</span></div>
        <p class="mc-bar-note">Status: ${p.status}</p></div>`;
    }
    if (p.id === 'MC2-EP-05' && typeof p.value === 'object') {
      const v = p.value;
      const map = mc2.arkansas_readiness_map;
      return `<div class="mc-card"><h3>${p.title}</h3>
        <div class="mc-phase-item"><span>Counties active</span><span>${v.counties_active} / ${v.counties_total}</span></div>
        <div class="mc-phase-item"><span>Education leaders</span><span>${v.education_leaders}</span></div>
        <div class="mc-phase-item"><span>Coalition orgs</span><span>${v.coalition_orgs}</span></div>
        <div class="mc-phase-item"><span>Events</span><span>${v.events}</span></div>
        <div class="mc-phase-item"><span>Conversations</span><span>${v.conversations}</span></div>
        <p class="mc-bar-note"><a href="${map.route}">County map →</a> · Signature visualization · ${p.status}</p></div>`;
    }
    if (p.id === 'MC2-EP-02' && typeof p.value === 'object') {
      const b = p.value;
      return `<div class="mc-card"><h3>${p.title}</h3>
        <div class="mc-stat__value">#${b.number || '—'}</div>
        <p>${b.title || '—'}</p>
        <p class="mc-bar-note">Next: #${ex.next_build?.number || '—'} — ${ex.next_build?.title || '—'}</p></div>`;
    }
    return `<div class="mc-card"><h3>${p.title}</h3>
      <div class="mc-stat__value">${typeof p.value === 'object' ? JSON.stringify(p.value) : p.value}${p.unit === 'percent' ? '%' : ''}</div>
      <p class="mc-bar-note">Status: ${p.status}</p></div>`;
  }).join('');

  const workspaceRows = mc2.workspaces.map(w => `
    <tr class="${w.implementation_status === 'partial' ? 'mc-table__row--approved' : ''}">
      <td><code>${w.id}</code></td>
      <td><strong>${w.title}</strong>${w.route ? ` <a href="${w.route}" class="mc-inline-link">→</a>` : ''}</td>
      <td>${w.track_count}</td>
      <td>${w.implementation_status}</td>
    </tr>`).join('');

  const healthRows = mc2.health_indicators.map(h => `
    <tr><td>${h.title}</td><td><strong>${h.score}%</strong></td><td>${h.status}</td><td class="mc-bar-note">${h.source}</td></tr>`).join('');

  const alertRows = mc2.smart_alerts.map(a => `
    <tr><td>${a.title}</td><td>${a.automated ? '✓ Automated' : '○ Defined'}</td><td>${a.status}</td></tr>`).join('');

  const reportRows = mc2.executive_reports.map(r => `
    <tr><td>${r.title}</td><td>${r.status}</td><td class="mc-bar-note">${r.note || '—'}</td></tr>`).join('');

  const successBlocks = Object.entries(mc2.success_metrics).map(([cat, metrics]) => `
    <div class="mc-card"><h3>${cat.charAt(0).toUpperCase() + cat.slice(1)}</h3>
      <ul class="mc-deliverables">${metrics.map(m =>
        `<li>${m.metric}${m.current !== undefined ? ` <em>(${m.current})</em>` : ''} — ${m.status}</li>`
      ).join('')}</ul></div>`).join('');

  const intelRows = mc2.future_intelligence.map(f => `
    <tr><td>${f.capability}</td><td>${f.status}</td><td class="mc-bar-note">${f.note || '—'}</td></tr>`).join('');

  const buildRows = (mc.builds || []).slice(0, 12).map(b => `
    <tr><td>#${b.number}</td><td>${b.title}</td><td>v${b.version || '—'}</td><td>${b.status}</td><td>${b.completed || b.started || '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Executive Command Center</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #25 · ${mc2.title}</p>
      <h1>Executive Command Center</h1>
      <p class="mc-header__question">${mc2.governing_principle}</p>
      <p class="mc-bar-note"><strong>If it matters, it is visible.</strong> · <a href="/mission-control/">MC v1 Dashboard</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">MC2 readiness</div><div class="mc-stat__value">${s.mc2_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Workspaces</div><div class="mc-stat__value">${s.workspaces}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Project health</div><div class="mc-stat__value">${s.overall_project_health}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Builds recorded</div><div class="mc-stat__value">${s.builds_in_timeline}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Alerts automated</div><div class="mc-stat__value">${s.smart_alerts_automated}/${s.smart_alerts_defined}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Platform completion</div><div class="mc-stat__value">${ex.overall_completion || '—'}%</div></div>
    </div>
    <h2 class="mc-section-title">Executive Dashboard Panels</h2>
    <div class="mc-grid-2">${panelCards}</div>
    <h2 class="mc-section-title">Mission Control Workspaces</h2>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table mc-inv-table">
        <thead><tr><th>ID</th><th>Workspace</th><th>Tracks</th><th>Status</th></tr></thead>
        <tbody>${workspaceRows}</tbody>
      </table>
    </div>
    <h2 class="mc-section-title">Project Health Indicators</h2>
    <table class="mc-table"><thead><tr><th>Indicator</th><th>Score</th><th>Status</th><th>Source</th></tr></thead>
      <tbody>${healthRows}</tbody></table>
    <h2 class="mc-section-title">Smart Alerts</h2>
    <table class="mc-table"><thead><tr><th>Alert</th><th>Automation</th><th>Status</th></tr></thead>
      <tbody>${alertRows}</tbody></table>
    <h2 class="mc-section-title">Executive Reports</h2>
    <table class="mc-table"><thead><tr><th>Report</th><th>Status</th><th>Notes</th></tr></thead>
      <tbody>${reportRows}</tbody></table>
    <h2 class="mc-section-title">Success Dashboard — Educational Impact</h2>
    <div class="mc-grid-2">${successBlocks}</div>
    <h2 class="mc-section-title">Build Timeline (${mc2.build_timeline.builds_complete} complete)</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:320px;overflow-y:auto">
      <table class="mc-table"><thead><tr><th>#</th><th>Title</th><th>Version</th><th>Status</th><th>Date</th></tr></thead>
        <tbody>${buildRows}</tbody></table>
    </div>
    <p class="mc-bar-note">Schema: ${mc2.build_timeline.schema.join(' · ')}</p>
    <h2 class="mc-section-title">Future Intelligence Layer</h2>
    <table class="mc-table"><thead><tr><th>Capability</th><th>Status</th><th>Notes</th></tr></thead>
      <tbody>${intelRows}</tbody></table>
    <h2 class="mc-section-title">Executive Principles</h2>
    <ul class="mc-deliverables">${mc2.executive_principles.map(p =>
      `<li><strong>${p.principle}</strong> — ${p.description}</li>`
    ).join('')}</ul>
    <h2 class="mc-section-title">Command Center <code>${mc2.command_center.route}</code></h2>
    <ul class="mc-deliverables">${mc2.command_center.capabilities.map(c => `<li>${c}</li>`).join('')}</ul>
    <p class="mc-bar-note">Status: ${mc2.command_center.status} — private admin workspace</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${mc2.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${mc2.recommended_next_build.number} — ${mc2.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${mc2.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MISSION_CONTROL_2.md">MISSION_CONTROL_2.md</a> ·
      <a href="/data/mc2-executive.json">JSON</a> ·
      <a href="/data/mission-control.json">mission-control.json</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initAiKnowledgeEngine() {
  const root = document.getElementById('mc-ai-knowledge-root');
  if (!root) return;

  const [aiRes, mcRes] = await Promise.all([
    fetch('/data/ai-knowledge-engine.json'),
    fetch('/data/mission-control.json')
  ]);
  const ai = await aiRes.json();
  const mc = await mcRes.json();
  const s = ai.summary;

  const modeRows = ai.learning_modes.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.description}</td><td>${m.status}</td></tr>`).join('');

  const capRows = ai.capabilities.map(c => `
    <tr class="${c.implementation_status === 'partial' ? 'mc-table__row--approved' : ''}">
      <td><code>${c.id}</code></td><td><strong>${c.title}</strong></td>
      <td>${c.feature_count}</td><td>${c.implementation_status}</td></tr>`).join('');

  const questionRows = ai.example_questions.map(q => `
    <tr><td>${q.q}</td><td>${q.category}</td><td>${q.fact_type}</td></tr>`).join('');

  const sourceRows = ai.knowledge_sources.map(ks => `
    <tr><td>${ks.title}</td><td><a href="${ks.route}">JSON</a></td>
      <td>${ks.records || '—'}</td><td>${ks.status}</td></tr>`).join('');

  const capCards = ai.capabilities.map(c => `
    <div class="mc-card"><h3>${c.id} — ${c.title}</h3>
      <p class="mc-bar-note">${c.purpose || c.notes || ''}</p>
      <ul class="mc-deliverables">${c.features.map(f =>
        `<li>${typeof f === 'string' ? f : (f.q || f.title || JSON.stringify(f))}</li>`
      ).join('')}</ul>
      ${c.notes ? `<p class="mc-bar-note"><em>${c.notes}</em></p>` : ''}</div>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → AI Knowledge Engine</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #26 · ${ai.title}</p>
      <h1>Educational Intelligence Architecture</h1>
      <p class="mc-header__question">${ai.governing_principle}</p>
      <p class="mc-bar-note"><strong>Arkansas Civic Librarian</strong> — ${ai.persona.role}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">AI readiness</div><div class="mc-stat__value">${s.ai_engine_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Capabilities</div><div class="mc-stat__value">${s.capabilities}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Learning modes</div><div class="mc-stat__value">${s.learning_modes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Example Qs</div><div class="mc-stat__value">${s.example_questions}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Knowledge sources</div><div class="mc-stat__value">${s.knowledge_sources}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Chat UI</div><div class="mc-stat__value">${s.chat_ui_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Core Principles</h2>
    <ul class="mc-deliverables">${ai.core_principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Arkansas Civic Librarian</h2>
    <ul class="mc-deliverables">${ai.persona.traits.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Learning Modes</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Mode</th><th>Description</th><th>Status</th></tr></thead>
      <tbody>${modeRows}</tbody></table>
    <h2 class="mc-section-title">Evidence-First Response Schema</h2>
    <ul class="mc-deliverables">${ai.response_schema.map(f => `<li>${f.replace(/_/g, ' ')}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Example Questions</h2>
    <table class="mc-table"><thead><tr><th>Question</th><th>Category</th><th>Fact type</th></tr></thead>
      <tbody>${questionRows}</tbody></table>
    <h2 class="mc-section-title">Capabilities</h2>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table"><thead><tr><th>ID</th><th>Capability</th><th>Features</th><th>Status</th></tr></thead>
        <tbody>${capRows}</tbody></table>
    </div>
    <h2 class="mc-section-title">Verified Knowledge Sources</h2>
    <table class="mc-table"><thead><tr><th>Source</th><th>Registry</th><th>Records</th><th>Status</th></tr></thead>
      <tbody>${sourceRows}</tbody></table>
    <h2 class="mc-section-title">Guardrails</h2>
    <ul class="mc-deliverables">${ai.guardrails.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Technical Requirements</h2>
    <ul class="mc-deliverables">${Object.entries(ai.technical_requirements).map(([k, v]) =>
      `<li><strong>${k.replace(/_/g, ' ')}</strong>: ${v}</li>`
    ).join('')}</ul>
    <h2 class="mc-section-title">Capability Details</h2>
    <div class="mc-grid-2">${capCards}</div>
    <h2 class="mc-section-title">Future Vision</h2>
    <p class="mc-bar-note">${ai.future_vision.role}</p>
    <ul class="mc-deliverables">${ai.future_vision.destinations.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ai.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ai.recommended_next_build.number} — ${ai.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ai.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/AI_KNOWLEDGE_ENGINE.md">AI_KNOWLEDGE_ENGINE.md</a> ·
      <a href="/data/ai-knowledge-engine.json">JSON</a> ·
      <a href="/mission-control/knowledge-graph.html">Knowledge Graph</a> ·
      <a href="/mission-control/research.html">Research</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initContentProductionFactory() {
  const root = document.getElementById('mc-content-factory-root');
  if (!root) return;

  const [cpfRes, mcRes] = await Promise.all([
    fetch('/data/content-production-factory.json'),
    fetch('/data/mission-control.json')
  ]);
  const cpf = await cpfRes.json();
  const mc = await mcRes.json();
  const s = cpf.summary;
  const inv = cpf.inventory_alignment;

  const typeRows = cpf.content_types.map(ct => `
    <tr class="${ct.status === 'partial' ? 'mc-table__row--approved' : ''}">
      <td><code>${ct.id}</code></td><td><strong>${ct.title}</strong></td>
      <td><code>${ct.template_id}</code></td><td>${ct.status}</td></tr>`).join('');

  const workflowRows = cpf.workflow_stages.map(w => `
    <tr><td>${w.stage}</td><td>${w.title}</td><td><code>${w.inventory_status}</code></td><td>${w.status}</td></tr>`).join('');

  const metricRows = cpf.dashboard_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td>
      <td>${m.current !== null && m.current !== undefined ? m.current : '—'}</td><td>${m.status}</td></tr>`).join('');

  const statusBreakdown = Object.entries(inv.status_breakdown || {}).map(([k, v]) =>
    `<div class="mc-phase-item"><span>${k}</span><span>${v}</span></div>`
  ).join('');

  const typeCards = cpf.content_types.map(ct => `
    <div class="mc-card"><h3>${ct.title}</h3>
      <p class="mc-bar-note">Template: <code>${ct.template_id}</code> · ${ct.status}</p>
      <ul class="mc-deliverables">${(ct.examples || ct.sections || []).map(e => `<li>${e}</li>`).join('')}</ul>
      ${ct.notes ? `<p class="mc-bar-note"><em>${ct.notes}</em></p>` : ''}</div>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Content Production Factory</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #27 · ${cpf.title}</p>
      <h1>Editorial Operating System</h1>
      <p class="mc-header__question">${cpf.governing_principle}</p>
      <p class="mc-bar-note">Editorial mission: ${cpf.editorial_mission.join(' · ')}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Factory readiness</div><div class="mc-stat__value">${s.factory_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Content types</div><div class="mc-stat__value">${s.content_types}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Assets registered</div><div class="mc-stat__value">${s.assets_registered}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Published</div><div class="mc-stat__value">${s.assets_published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">In pipeline</div><div class="mc-stat__value">${s.assets_in_pipeline}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Workflow stages</div><div class="mc-stat__value">${s.workflow_stages}</div></div>
    </div>
    <h2 class="mc-section-title">Standard Article Structure (${s.article_structure_sections} sections)</h2>
    <ol class="mc-deliverables">${cpf.article_structure.map(sec => `<li>${sec}</li>`).join('')}</ol>
    <h2 class="mc-section-title">Reading Levels</h2>
    <table class="mc-table"><thead><tr><th>Level</th><th>Title</th><th>Facts depth</th><th>Status</th></tr></thead>
      <tbody>${cpf.reading_levels.map(r => `<tr><td>L${r.level}</td><td>${r.title}</td><td>${r.facts_depth}</td><td>${r.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Content Types</h2>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table"><thead><tr><th>ID</th><th>Type</th><th>Template</th><th>Status</th></tr></thead>
        <tbody>${typeRows}</tbody></table>
    </div>
    <h2 class="mc-section-title">Editorial Workflow</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Stage</th><th>Inventory status</th><th>Factory status</th></tr></thead>
      <tbody>${workflowRows}</tbody></table>
    <h2 class="mc-section-title">Content Dashboard Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Inventory Status <a href="/mission-control/inventory.html" class="mc-inline-link">Full registry →</a></h2>
    <div class="mc-card">${statusBreakdown || '<p class="mc-bar-note">No breakdown available.</p>'}</div>
    <h2 class="mc-section-title">Educational Quality Gates</h2>
    <ul class="mc-deliverables">${cpf.quality_gates.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Source Requirements</h2>
    <ul class="mc-deliverables">${cpf.source_requirements.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Visual Types</h2>
    <ul class="mc-deliverables">${cpf.visual_types.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Evergreen Review</h2>
    <table class="mc-table"><thead><tr><th>Topic</th><th>Interval</th><th>Status</th></tr></thead>
      <tbody>${cpf.evergreen_review.map(e => `<tr><td>${e.topic}</td><td>${e.interval_months ? e.interval_months + ' months' : (e.interval || '—')}</td><td>${e.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Institutional Voice</h2>
    <ul class="mc-deliverables">${cpf.institutional_voice.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Content Type Details</h2>
    <div class="mc-grid-2">${typeCards}</div>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cpf.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cpf.recommended_next_build.number} — ${cpf.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cpf.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/CONTENT_PRODUCTION_FACTORY.md">CONTENT_PRODUCTION_FACTORY.md</a> ·
      <a href="/data/content-production-factory.json">JSON</a> ·
      <a href="/mission-control/inventory.html">Content Inventory</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initEducationAcademy() {
  const root = document.getElementById('mc-education-academy-root');
  if (!root) return;

  const [acadRes, mcRes] = await Promise.all([
    fetch('/data/education-academy.json'),
    fetch('/data/mission-control.json')
  ]);
  const acad = await acadRes.json();
  const mc = await mcRes.json();
  const s = acad.summary;

  const stageCards = acad.learning_stages.map(st => `
    <div class="mc-card">
      <h3>Stage ${st.stage}: ${st.title}</h3>
      <p class="mc-bar-note">${st.focus}</p>
      ${st.questions ? `<ul class="mc-deliverables">${st.questions.map(q => `<li>${q}</li>`).join('')}</ul>` : ''}
      ${st.distinctions ? `<ul class="mc-deliverables">${st.distinctions.map(d => `<li>${d}</li>`).join('')}</ul>` : ''}
      ${st.topics ? `<ul class="mc-deliverables">${st.topics.map(t => `<li>${t}</li>`).join('')}</ul>` : ''}
      ${st.activities ? `<ul class="mc-deliverables">${st.activities.map(a => `<li>${a}</li>`).join('')}</ul>` : ''}
      <p class="mc-bar-note">${st.route ? `<a href="${st.route}">${st.route}</a> · ` : ''}${st.status}${st.notes ? ` — <em>${st.notes}</em>` : ''}</p>
    </div>`).join('');

  const moduleRows = acad.curriculum_modules.map(m => `
    <tr class="${m.status === 'partial' ? 'mc-table__row--approved' : ''}">
      <td>${m.number}</td><td><strong>${m.title}</strong></td>
      <td>${m.world || '—'}</td>
      <td>${m.route ? `<a href="${m.route}">${m.route}</a>` : '—'}</td>
      <td>${m.status}</td></tr>`).join('');

  const metricRows = acad.leadership_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.current}</td><td>${m.status}</td></tr>`).join('');

  const audienceRows = acad.audience_toolkits.map(a => `
    <tr><td>${a.audience}</td><td>${a.route ? `<a href="${a.route}">${a.route}</a>` : '—'}</td><td>${a.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Education Academy</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #28 · ${acad.title}</p>
      <h1>Community Education Academy</h1>
      <p class="mc-header__question">${acad.governing_principle}</p>
      <p class="mc-bar-note">${acad.academy_mission} · <a href="${acad.public_route}">Public signup →</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Academy readiness</div><div class="mc-stat__value">${s.academy_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Modules</div><div class="mc-stat__value">${s.curriculum_modules}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Learning stages</div><div class="mc-stat__value">${s.learning_stages}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Modules partial</div><div class="mc-stat__value">${s.modules_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Audience toolkits</div><div class="mc-stat__value">${s.audience_toolkits}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Enrollment tracking</div><div class="mc-stat__value">${s.enrollment_tracking_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Four Learning Stages</h2>
    <div class="mc-grid-2">${stageCards}</div>
    <h2 class="mc-section-title">Academy Curriculum (${s.curriculum_modules} modules)</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Module</th><th>World</th><th>Interim route</th><th>Status</th></tr></thead>
      <tbody>${moduleRows}</tbody></table>
    <h2 class="mc-section-title">Module Materials (each module)</h2>
    <ul class="mc-deliverables">${acad.module_materials.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acad.certification.title}</h2>
    <p class="mc-bar-note"><em>${acad.certification.disclaimer}</em></p>
    <ul class="mc-deliverables">${acad.certification.competencies.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Presentation Toolkit</h2>
    <ul class="mc-deliverables">${acad.presentation_toolkit.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Audience-Specific Toolkits</h2>
    <table class="mc-table"><thead><tr><th>Audience</th><th>Route</th><th>Status</th></tr></thead>
      <tbody>${audienceRows}</tbody></table>
    <h2 class="mc-section-title">Leadership Dashboard Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Continuing Education</h2>
    <ul class="mc-deliverables">${acad.continuing_education.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Future Expansion</h2>
    <ul class="mc-deliverables">${acad.future_expansion.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Mission Control Integration</h2>
    <table class="mc-table"><thead><tr><th>Metric</th><th>Source</th><th>Status</th></tr></thead>
      <tbody>${acad.mc_integration.map(i => `<tr><td>${i.metric}</td><td>${i.source || '—'}</td><td>${i.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${acad.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${acad.recommended_next_build.number} — ${acad.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${acad.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/COMMUNITY_EDUCATION_ACADEMY.md">COMMUNITY_EDUCATION_ACADEMY.md</a> ·
      <a href="/data/education-academy.json">JSON</a> ·
      <a href="/educate/">Educate signup</a> ·
      <a href="/mission-control/civic-ecosystem.html">Civic Ecosystem</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initResearchObservatory() {
  const root = document.getElementById('mc-research-observatory-root');
  if (!root) return;

  const [obsRes, mcRes] = await Promise.all([
    fetch('/data/research-observatory.json'),
    fetch('/data/mission-control.json')
  ]);
  const obs = await obsRes.json();
  const mc = await mcRes.json();
  const s = obs.summary;

  const divRows = obs.divisions.map(d => `
    <tr class="${d.status === 'partial' ? 'mc-table__row--approved' : ''}">
      <td><code>${d.id}</code></td><td><strong>Division ${d.letter}: ${d.title}</strong></td>
      <td>${d.status}</td><td class="mc-bar-note">${d.notes || '—'}</td></tr>`).join('');

  const divCards = obs.divisions.map(d => `
    <div class="mc-card"><h3>Division ${d.letter} — ${d.title}</h3>
      <p class="mc-bar-note"><strong>Tracks:</strong></p>
      <ul class="mc-deliverables">${d.tracks.map(t => `<li>${t}</li>`).join('')}</ul>
      <p class="mc-bar-note"><strong>Outputs:</strong></p>
      <ul class="mc-deliverables">${d.outputs.map(o => `<li>${o}</li>`).join('')}</ul>
      ${d.route ? `<p class="mc-bar-note"><a href="${d.route}">${d.route}</a></p>` : ''}
      ${d.notes ? `<p class="mc-bar-note"><em>${d.notes}</em></p>` : ''}</div>`).join('');

  const workflowRows = obs.workflow_stages.map(w => `
    <tr><td>${w.stage}</td><td>${w.title}</td><td>${w.status}</td></tr>`).join('');

  const panelRows = obs.dashboard_panels.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.title}</td><td>${p.current}</td><td>${p.status}</td></tr>`).join('');

  const gapRows = obs.research_gaps.map(g => `
    <tr><td>${g.topic}</td><td>${g.source}</td><td>${g.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Research Observatory</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #29 · ${obs.title}</p>
      <h1>Living Research & Legislative Intelligence</h1>
      <p class="mc-header__question">${obs.governing_principle}</p>
      <p class="mc-bar-note"><strong>Early warning system</strong> — <a href="${obs.legacy_route}">Research Framework →</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Observatory readiness</div><div class="mc-stat__value">${s.observatory_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Divisions</div><div class="mc-stat__value">${s.divisions}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Evidence records</div><div class="mc-stat__value">${s.evidence_records}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Needing updates</div><div class="mc-stat__value">${s.evidence_needing_updates}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Research gaps</div><div class="mc-stat__value">${s.research_gaps_tracked}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Alerts automated</div><div class="mc-stat__value">${s.future_alerts_automated}/${s.future_alerts_defined}</div></div>
    </div>
    <h2 class="mc-section-title">Mission</h2>
    <p class="mc-bar-note">${obs.mission}</p>
    <h2 class="mc-section-title">Research Divisions</h2>
    <div class="mc-card mc-inv-table-wrap">
      <table class="mc-table"><thead><tr><th>ID</th><th>Division</th><th>Status</th><th>Notes</th></tr></thead>
        <tbody>${divRows}</tbody></table>
    </div>
    <h2 class="mc-section-title">Research Workflow (${s.workflow_stages} stages)</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${workflowRows}</tbody></table>
    <h2 class="mc-section-title">Priority Levels</h2>
    <div class="mc-grid-2">${obs.priority_levels.map(p => `
      <div class="mc-card"><h3>Priority ${p.level}: ${p.title}</h3>
        <ul class="mc-deliverables">${p.examples.map(e => `<li>${e}</li>`).join('')}</ul></div>`).join('')}</div>
    <h2 class="mc-section-title">Legislative Tracking Page Structure</h2>
    <ol class="mc-deliverables">${obs.legislative_page_sections.map(sec => `<li>${sec}</li>`).join('')}</ol>
    <h2 class="mc-section-title">Observatory Dashboard</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Panel</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${panelRows}</tbody></table>
    <h2 class="mc-section-title">Research Gap Tracker</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:280px;overflow-y:auto">
      <table class="mc-table"><thead><tr><th>Topic</th><th>Source</th><th>Status</th></tr></thead>
        <tbody>${gapRows}</tbody></table>
    </div>
    <h2 class="mc-section-title">Community Research Contributions</h2>
    <ul class="mc-deliverables">${obs.community_contributions.map(c => `<li>${c}</li>`).join('')}</ul>
    <p class="mc-bar-note">All contributions undergo editorial review before incorporation.</p>
    <h2 class="mc-section-title">Future Intelligence Alerts</h2>
    <table class="mc-table"><thead><tr><th>Alert</th><th>Automation</th><th>Status</th></tr></thead>
      <tbody>${obs.future_alerts.map(a => `<tr><td>${a.alert}</td><td>${a.automated ? 'Automated' : 'Human review'}</td><td>${a.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Division Details</h2>
    <div class="mc-grid-2">${divCards}</div>
    <h2 class="mc-section-title">Mission Control Integration</h2>
    <table class="mc-table"><thead><tr><th>Use</th><th>Source</th><th>Status</th></tr></thead>
      <tbody>${obs.mc_integration.map(i => `<tr><td>${i.use}</td><td>${i.source || '—'}</td><td>${i.status}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${obs.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${obs.recommended_next_build.number} — ${obs.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${obs.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/RESEARCH_OBSERVATORY.md">RESEARCH_OBSERVATORY.md</a> ·
      <a href="/data/research-observatory.json">JSON</a> ·
      <a href="/mission-control/research.html">Research Framework</a> ·
      <a href="/data/evidence-registry.json">Evidence Registry</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initOutreachEngine() {
  const root = document.getElementById('mc-outreach-root');
  if (!root) return;

  const [outRes, mcRes] = await Promise.all([
    fetch('/data/outreach-engine.json'),
    fetch('/data/mission-control.json')
  ]);
  const out = await outRes.json();
  const mc = await mcRes.json();
  const s = out.summary;

  const pillarCards = out.pillars.map(p => `
    <div class="mc-card">
      <h3>Pillar ${p.number}: ${p.title}</h3>
      <p class="mc-bar-note">${p.purpose}</p>
      <ul class="mc-deliverables">${(p.destinations || p.content_types || p.venues || p.activities || p.audiences || []).map(i => `<li>${i}</li>`).join('')}</ul>
      ${p.route ? `<p class="mc-bar-note"><a href="${p.route}">${p.route}</a> · ${p.status}</p>` : `<p class="mc-bar-note">${p.status}</p>`}
    </div>`).join('');

  const campaignRows = out.campaigns.map(c => `
    <tr class="${c.status === 'partial' ? 'mc-table__row--approved' : ''}">
      <td><code>${c.id}</code></td><td>${c.title}</td><td>${c.focus}</td>
      <td>${c.route ? `<a href="${c.route}">${c.route}</a>` : '—'}</td><td>${c.status}</td></tr>`).join('');

  const analyticsRows = out.analytics_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td>
      <td>${m.current !== undefined ? m.current : '—'}</td><td>${m.status}</td></tr>`).join('');

  const panelRows = out.dashboard_panels.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.title}</td><td>${p.current}</td><td>${p.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Outreach Engine</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #30 · ${out.title}</p>
      <h1>Arkansas Outreach Engine</h1>
      <p class="mc-header__question">${out.governing_principle}</p>
      <p class="mc-bar-note"><strong>Help more Arkansans understand Citizens United.</strong></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Outreach readiness</div><div class="mc-stat__value">${s.outreach_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pillars</div><div class="mc-stat__value">${s.pillars}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Campaigns</div><div class="mc-stat__value">${s.campaigns}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Campaigns partial</div><div class="mc-stat__value">${s.campaigns_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Analytics live</div><div class="mc-stat__value">${s.analytics_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Share toolkit</div><div class="mc-stat__value">${s.share_toolkit_items}</div></div>
    </div>
    <h2 class="mc-section-title">Outreach Sequence</h2>
    <p class="mc-bar-note">${out.outreach_sequence.join(' → ')}</p>
    <h2 class="mc-section-title">Five Outreach Pillars</h2>
    <div class="mc-grid-2">${pillarCards}</div>
    <h2 class="mc-section-title">Outreach Campaigns</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Campaign</th><th>Focus</th><th>Route</th><th>Status</th></tr></thead>
      <tbody>${campaignRows}</tbody></table>
    <h2 class="mc-section-title">Resource Distribution</h2>
    <ul class="mc-deliverables">${out.resource_formats.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Share Toolkit</h2>
    <ul class="mc-deliverables">${out.share_toolkit.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Outreach Analytics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${analyticsRows}</tbody></table>
    <p class="mc-bar-note">Educational impact over popularity.</p>
    <h2 class="mc-section-title">Arkansas County Outreach</h2>
    <ul class="mc-deliverables">${out.county_outreach_profile.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Outreach Dashboard</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Panel</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${panelRows}</tbody></table>
    <h2 class="mc-section-title">Continuous Improvement</h2>
    <ul class="mc-deliverables">${out.continuous_improvement.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${out.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${out.recommended_next_build.number} — ${out.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${out.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/OUTREACH_ENGINE.md">OUTREACH_ENGINE.md</a> ·
      <a href="/data/outreach-engine.json">JSON</a> ·
      <a href="/action/share.html">Share</a> ·
      <a href="/coalition/">Coalition</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCountyOperatingSystem() {
  const root = document.getElementById('mc-county-os-root');
  if (!root) return;

  const [cosRes, cciRes, mcRes] = await Promise.all([
    fetch('/data/county-operating-system.json'),
    fetch('/data/county-coalition-index.json'),
    fetch('/data/mission-control.json')
  ]);
  const cos = await cosRes.json();
  const cci = await cciRes.json();
  const mc = await mcRes.json();
  const s = cos.summary;
  const st = cos.statewide_totals;

  const scoreCards = cos.education_score_categories.map(cat => `
    <div class="mc-card"><h3>${cat.title}</h3>
      <ul class="mc-deliverables">${cat.indicators.map(i => `<li>${i}</li>`).join('')}</ul>
      <p class="mc-bar-note">Status: ${cat.status}</p></div>`).join('');

  const regionRows = cos.regions.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.title}</td><td>${r.status}</td></tr>`).join('');

  const metricRows = cos.county_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td></tr>`).join('');

  const countySample = (cci.counties || []).slice(0, 15).map(c => `
    <tr><td>${c.name}</td><td><a href="${c.route}">${c.slug}</a></td>
      <td>${c.education_leaders}</td><td>${c.organizations}</td>
      <td>${c.completeness_pct}%</td><td>${c.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → County Operating System</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #31 · ${cos.title}</p>
      <h1>Arkansas County Education Network</h1>
      <p class="mc-header__question">${cos.governing_principle}</p>
      <p class="mc-bar-note">Canonical: <code>${cos.canonical_county_route}</code> · Current: <code>${cos.current_county_route}</code></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">County OS readiness</div><div class="mc-stat__value">${s.county_os_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties</div><div class="mc-stat__value">${s.counties_scaffolded}/${s.counties_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">With partner</div><div class="mc-stat__value">${s.counties_with_partner}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Education leaders</div><div class="mc-stat__value">${st.education_leaders}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Organizations</div><div class="mc-stat__value">${st.organizations}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Conversations</div><div class="mc-stat__value">${st.community_conversations}</div></div>
    </div>
    <h2 class="mc-section-title">County Profile Sections (${s.profile_sections})</h2>
    <ol class="mc-deliverables">${cos.county_profile_sections.map(sec => `<li>${sec}</li>`).join('')}</ol>
    <h2 class="mc-section-title">County Education Score — 5 Categories</h2>
    <div class="mc-grid-2">${scoreCards}</div>
    <p class="mc-bar-note">No competitive rankings — indicators support planning only.</p>
    <h2 class="mc-section-title">County Leadership Roles</h2>
    <ul class="mc-deliverables">${cos.leadership_roles.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Regional Groupings (${s.regions})</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Region</th><th>Status</th></tr></thead>
      <tbody>${regionRows}</tbody></table>
    <h2 class="mc-section-title">Outreach Gap Signals</h2>
    <ul class="mc-deliverables">${cos.outreach_gap_signals.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">County Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">75 Counties <a href="/coalition/counties.html" class="mc-inline-link">County map →</a></h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:320px;overflow-y:auto">
      <table class="mc-table"><thead><tr><th>County</th><th>Slug</th><th>Leaders</th><th>Orgs</th><th>Complete</th><th>Status</th></tr></thead>
        <tbody>${countySample}</tbody></table>
    </div>
    <p class="mc-bar-note">Showing 15 of ${s.counties_scaffolded} — full index in county-coalition-index.json</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cos.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cos.recommended_next_build.number} — ${cos.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cos.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/COUNTY_OPERATING_SYSTEM.md">COUNTY_OPERATING_SYSTEM.md</a> ·
      <a href="/data/county-operating-system.json">JSON</a> ·
      <a href="/data/county-coalition-index.json">County Index</a> ·
      <a href="/mission-control/civic-ecosystem.html">Civic Ecosystem</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initEducationalCampaignOperatingSystem() {
  const root = document.getElementById('mc-campaign-os-root');
  if (!root) return;

  const [ecosRes, mcRes] = await Promise.all([
    fetch('/data/educational-campaign-operating-system.json'),
    fetch('/data/mission-control.json')
  ]);
  const ecos = await ecosRes.json();
  const mc = await mcRes.json();
  const s = ecos.summary;
  const ch = ecos.current_horizon;
  const snap = ecos.platform_snapshot;

  const horizonCards = ecos.horizons.map(h => {
    const objRows = (h.objectives || []).map(o =>
      `<li>${o.title} <em>(${o.status}, ${o.pct}%)</em></li>`
    ).join('');
    const indRows = (h.success_indicators || []).map(i =>
      `<li>${i.met ? '✓' : '○'} ${i.title}</li>`
    ).join('');
    const mcInd = (h.mc_indicators || []).length
      ? `<p class="mc-bar-note">MC indicators: ${h.mc_indicators.join(' · ')}</p>` : '';
    return `<div class="mc-card">
      <h3>Horizon ${h.number}: ${h.title}</h3>
      <p class="mc-bar-note">${h.mission}</p>
      <p class="mc-bar-note">Status: <strong>${h.status}</strong></p>
      ${objRows ? `<ul class="mc-deliverables">${objRows}</ul>` : ''}
      ${indRows ? `<p class="mc-bar-note">Success indicators:</p><ul class="mc-deliverables">${indRows}</ul>` : ''}
      ${mcInd}
    </div>`;
  }).join('');

  const seasonRows = ecos.annual_operating_cycle.map(season => `
    <div class="mc-card"><h3>${season.season}</h3>
      <p class="mc-bar-note">Focus: ${season.focus}</p>
      <ul class="mc-deliverables">${season.activities.map(a => `<li>${a}</li>`).join('')}</ul>
    </div>`).join('');

  const riskRows = ecos.risk_management.risks.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.title}</td><td>${r.status}</td><td>${r.severity}</td></tr>`).join('');

  const measureRows = ecos.success_measurements.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const memoryRows = ecos.institutional_memory.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td>
      <td>${m.route ? `<a href="${m.route}">${m.route}</a>` : '—'}</td></tr>`).join('');

  const innovationRows = ecos.innovation_pipeline.categories.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.title}</td><td>${c.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Educational Campaign OS</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #32 · ${ecos.title}</p>
      <h1>Multi-Year Strategic Growth Blueprint</h1>
      <p class="mc-header__question">${ecos.governing_principle}</p>
      <p class="mc-bar-note">${ecos.subtitle} — master roadmap for long-term planning.</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Campaign OS readiness</div><div class="mc-stat__value">${s.campaign_os_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Current horizon</div><div class="mc-stat__value">H${ch.number}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">H1 objectives</div><div class="mc-stat__value">${ch.objectives_complete_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Indicators met</div><div class="mc-stat__value">${ch.success_indicators_met}/${ch.success_indicators_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Builds complete</div><div class="mc-stat__value">${snap.builds_complete}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Education leaders</div><div class="mc-stat__value">${snap.education_leader_signups}</div></div>
    </div>
    <h2 class="mc-section-title">Four Strategic Horizons</h2>
    <div class="mc-grid-2">${horizonCards}</div>
    <h2 class="mc-section-title">Annual Operating Cycle (${s.annual_seasons} seasons)</h2>
    <div class="mc-grid-2">${seasonRows}</div>
    <h2 class="mc-section-title">Quarterly Review Topics (${s.quarterly_topics})</h2>
    <ul class="mc-deliverables">${ecos.quarterly_review_topics.map(t => `<li>${t}</li>`).join('')}</ul>
    <p class="mc-bar-note">Quarterly reports: ${s.quarterly_reports_live ? 'live' : 'planned — not automated yet'}</p>
    <h2 class="mc-section-title">Annual Educational Summit</h2>
    <p class="mc-bar-note">Status: ${ecos.annual_summit.status}</p>
    <ul class="mc-deliverables">${ecos.annual_summit.agenda.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Innovation Pipeline (${s.innovation_categories} categories)</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Category</th><th>Status</th></tr></thead>
      <tbody>${innovationRows}</tbody></table>
    <p class="mc-bar-note">Queue live: ${ecos.innovation_pipeline.queue_live ? 'yes' : 'no — categories defined only'}</p>
    <h2 class="mc-section-title">Strategic Risk Management (${ecos.risk_management.active_risks} active)</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Risk</th><th>Status</th><th>Severity</th></tr></thead>
      <tbody>${riskRows}</tbody></table>
    <h2 class="mc-section-title">Success Measurements</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Measure</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${measureRows}</tbody></table>
    <p class="mc-bar-note">Educational outcomes over website traffic.</p>
    <h2 class="mc-section-title">Institutional Memory</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Item</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${memoryRows}</tbody></table>
    <h2 class="mc-section-title">Future Readiness</h2>
    <p class="mc-bar-note">${ecos.future_readiness.note}</p>
    <p class="mc-bar-note">Current focus: ${ecos.future_readiness.current_focus}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ecos.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ecos.recommended_next_build.number} — ${ecos.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ecos.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/EDUCATIONAL_CAMPAIGN_OPERATING_SYSTEM.md">EDUCATIONAL_CAMPAIGN_OPERATING_SYSTEM.md</a> ·
      <a href="/data/educational-campaign-operating-system.json">JSON</a> ·
      <a href="/mission-control/executive.html">Executive Command Center</a> ·
      <a href="/mission-control/phases.html">Phase Registry</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initEncyclopediaKnowledgeLibrary() {
  const root = document.getElementById('mc-encyclopedia-root');
  if (!root) return;

  const [encRes, kgRes, mcRes] = await Promise.all([
    fetch('/data/encyclopedia-knowledge-library.json'),
    fetch('/data/kg-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const enc = await encRes.json();
  const kg = await kgRes.json();
  const mc = await mcRes.json();
  const s = enc.summary;
  const cs = enc.completion_score;
  const rg = enc.relationship_graph;

  const categoryRows = enc.categories.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.number} — ${c.title}</td>
      <td>${c.entries_published}/${c.entries_planned}</td><td>${c.completion_pct}%</td><td>${c.status}</td></tr>`).join('');

  const categoryCards = enc.categories.map(c => `
    <div class="mc-card"><h3>Category ${c.number}: ${c.title}</h3>
      <p class="mc-bar-note">${c.entries_published}/${c.entries_planned} entries · ${c.status}</p>
      <ul class="mc-deliverables">${c.examples.map(e => `<li>${e}</li>`).join('')}</ul>
    </div>`).join('');

  const completionBars = [
    ['Planned', cs.entries_planned, cs.entries_planned],
    ['Published', cs.entries_published, cs.entries_planned],
    ['Fully sourced', cs.entries_fully_sourced, cs.entries_published],
    ['Under review', cs.entries_under_review, cs.entries_published],
    ['Needing updates', cs.entries_needing_updates, cs.entries_published],
  ].map(([label, val, max]) => `
    <div class="mc-phase-item"><span>${label}</span><span>${val}${max && label !== 'Planned' ? ` / ${max}` : ''}</span></div>`).join('');

  const kgSample = (kg.nodes || []).slice(0, 12).map(n => `
    <tr><td><code>${n.kg_id}</code></td><td>${n.title}</td><td>${n.type}</td>
      <td>${n.completion_pct || 0}%</td><td>${n.url ? `<a href="${n.url}">→</a>` : '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Encyclopedia & Knowledge Library</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #33 · ${enc.title}</p>
      <h1>Research Encyclopedia & Knowledge Library</h1>
      <p class="mc-header__question">${enc.governing_principle}</p>
      <p class="mc-bar-note">Canonical: <code>${enc.canonical_entry_route}</code> · Current: ${enc.current_entry_route}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Encyclopedia readiness</div><div class="mc-stat__value">${s.encyclopedia_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Published</div><div class="mc-stat__value">${s.entries_published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned</div><div class="mc-stat__value">${s.entries_planned}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Fully sourced</div><div class="mc-stat__value">${s.entries_fully_sourced}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">KG nodes</div><div class="mc-stat__value">${rg.nodes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Cross-links</div><div class="mc-stat__value">${cs.cross_link_completeness_pct}%</div></div>
    </div>
    <h2 class="mc-section-title">Reader Questions (${s.reader_questions})</h2>
    <ul class="mc-deliverables">${enc.reader_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Nine Encyclopedia Categories</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Category</th><th>Published/Planned</th><th>Complete</th><th>Status</th></tr></thead>
      <tbody>${categoryRows}</tbody></table>
    <div class="mc-grid-2">${categoryCards}</div>
    <h2 class="mc-section-title">Entry Structure (${s.entry_structure_sections} sections)</h2>
    <ol class="mc-deliverables">${enc.entry_structure.map(sec => `<li>${sec}</li>`).join('')}</ol>
    <h2 class="mc-section-title">Encyclopedia Completion Score</h2>
    <div class="mc-card">${completionBars}
      <p class="mc-bar-note">Catalog: ${cs.overall_completion_pct}% · Avg entry: ${cs.avg_entry_completion_pct}% · Orphans: ${cs.orphan_entries}</p>
      <p class="mc-bar-note">Cross-link completeness: ${cs.cross_link_completeness_pct}% · Reading-level: ${cs.reading_level_completeness_pct}%</p>
    </div>
    <h2 class="mc-section-title">Relationship Graph <a href="/mission-control/knowledge-graph.html" class="mc-inline-link">KG →</a></h2>
    <p class="mc-bar-note">${rg.nodes} nodes · ${rg.edges} edges · Hub: <code>${rg.hub_node}</code> · Status: ${rg.status}</p>
    <ul class="mc-deliverables">${rg.targets.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">KG Entries (sample)</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:320px;overflow-y:auto">
      <table class="mc-table"><thead><tr><th>KG ID</th><th>Title</th><th>Type</th><th>Complete</th><th>Link</th></tr></thead>
        <tbody>${kgSample}</tbody></table>
    </div>
    <h2 class="mc-section-title">Search Axes (${s.search_axes})</h2>
    <ul class="mc-deliverables">${enc.search.axes.map(a => `<li>${a}</li>`).join('')}</ul>
    <p class="mc-bar-note">Search live: ${s.encyclopedia_search_live ? 'yes' : 'no — planned'}</p>
    <h2 class="mc-section-title">Citation Standards</h2>
    <ul class="mc-deliverables">${enc.citation_standards.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${enc.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${enc.recommended_next_build.number} — ${enc.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${enc.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/ENCYCLOPEDIA_ARCHITECTURE.md">ENCYCLOPEDIA_ARCHITECTURE.md</a> ·
      <a href="/data/encyclopedia-knowledge-library.json">JSON</a> ·
      <a href="/data/kg-registry.json">KG Registry</a> ·
      <a href="/data/facts-registry.json">Facts Registry</a> ·
      <a href="/mission-control/knowledge-graph.html">Knowledge Graph</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initNarrativeArchitecture() {
  const root = document.getElementById('mc-narrative-root');
  if (!root) return;

  const [narrRes, mcRes] = await Promise.all([
    fetch('/data/narrative-architecture.json'),
    fetch('/data/mission-control.json')
  ]);
  const narr = await narrRes.json();
  const mc = await mcRes.json();
  const s = narr.summary;
  const nc = narr.narrative_completion;

  const actRows = narr.acts.map(a => `
    <tr><td>Act ${a.roman}</td><td>${a.title}</td><td>${a.question}</td>
      <td><a href="${a.primary_route}">${a.primary_route}</a></td>
      <td>${a.narrative_pct}%</td><td>${a.status}</td></tr>`).join('');

  const actCards = narr.acts.map(a => `
    <div class="mc-card"><h3>Act ${a.roman}: ${a.title}</h3>
      <p class="mc-bar-note"><strong>${a.question}</strong></p>
      <p class="mc-bar-note">${a.narrative_pct}% · Layers: ${a.layers_live.join(', ')}</p>
      <ul class="mc-deliverables">${a.topics.map(t => `<li>${t}</li>`).join('')}</ul>
      <p class="mc-bar-note">Outcome: ${a.reader_outcome}</p>
    </div>`).join('');

  const layerRows = narr.narrative_layers.map(l => `
    <tr><td><code>${l.id}</code></td><td>Layer ${l.layer}: ${l.title}</td>
      <td>${l.duration}</td><td>${l.status}</td></tr>`).join('');

  const componentRows = narr.story_components.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.title}</td><td>${c.status}</td></tr>`).join('');

  const visualRows = narr.visual_storytelling.map(v => `
    <tr><td><code>${v.id}</code></td><td>${v.title}</td><td>${v.status}</td>
      <td>${v.route ? `<a href="${v.route}">${v.route}</a>` : '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Narrative Architecture</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #34 · ${narr.title}</p>
      <h1>Storytelling & Narrative Architecture</h1>
      <p class="mc-header__question">${narr.governing_principle}</p>
      <blockquote class="mc-bar-note" style="font-style:italic;border-left:3px solid var(--mc-accent);padding-left:1rem">${narr.master_narrative}</blockquote>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Narrative readiness</div><div class="mc-stat__value">${s.narrative_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Acts</div><div class="mc-stat__value">${s.acts_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg act complete</div><div class="mc-stat__value">${s.avg_act_narrative_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Mapped pages</div><div class="mc-stat__value">${s.acts_with_primary_page}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Layers</div><div class="mc-stat__value">${s.narrative_layers}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Continuity</div><div class="mc-stat__value">${s.continuity_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Eight Narrative Acts</h2>
    <table class="mc-table"><thead><tr><th>Act</th><th>Title</th><th>Question</th><th>Route</th><th>Complete</th><th>Status</th></tr></thead>
      <tbody>${actRows}</tbody></table>
    <div class="mc-grid-2">${actCards}</div>
    <h2 class="mc-section-title">Narrative Layers (${s.narrative_layers})</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Layer</th><th>Duration</th><th>Status</th></tr></thead>
      <tbody>${layerRows}</tbody></table>
    <h2 class="mc-section-title">Storytelling Standards</h2>
    <ul class="mc-deliverables">${narr.storytelling_standards.map(st => `<li>${st}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Story Components</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Component</th><th>Status</th></tr></thead>
      <tbody>${componentRows}</tbody></table>
    <h2 class="mc-section-title">Visual Storytelling</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Element</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${visualRows}</tbody></table>
    <h2 class="mc-section-title">Narrative Continuity</h2>
    <p class="mc-bar-note">Status: ${narr.narrative_continuity.status}</p>
    <ul class="mc-deliverables">${narr.narrative_continuity.requirements.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Narrative Completion</h2>
    <div class="mc-card">
      <div class="mc-phase-item"><span>Acts with primary page</span><span>${nc.acts_with_primary_page}/${nc.acts_total}</span></div>
      <div class="mc-phase-item"><span>Layers partial</span><span>${nc.layers_partial}/${nc.layers_defined}</span></div>
      <div class="mc-phase-item"><span>Visual elements partial</span><span>${nc.visual_elements_partial}/${s.visual_elements}</span></div>
      <div class="mc-phase-item"><span>KG nodes linked</span><span>${nc.kg_nodes_linked}</span></div>
      <div class="mc-phase-item"><span>Facts linked</span><span>${nc.facts_linked}</span></div>
    </div>
    <h2 class="mc-section-title">Educational Integrity</h2>
    <p class="mc-bar-note">${narr.educational_integrity.principle}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${narr.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${narr.recommended_next_build.number} — ${narr.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${narr.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/NARRATIVE_ARCHITECTURE.md">NARRATIVE_ARCHITECTURE.md</a> ·
      <a href="/data/narrative-architecture.json">JSON</a> ·
      <a href="/mission-control/journey.html">UX Journey</a> ·
      <a href="/mission-control/encyclopedia.html">Encyclopedia</a> ·
      <a href="/halls/story-before.html">Act I →</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initMasterCurriculum() {
  const root = document.getElementById('mc-curriculum-root');
  if (!root) return;

  const [currRes, academyRes, mcRes] = await Promise.all([
    fetch('/data/master-curriculum.json'),
    fetch('/data/education-academy.json'),
    fetch('/data/mission-control.json')
  ]);
  const curr = await currRes.json();
  const academy = await academyRes.json();
  const mc = await mcRes.json();
  const s = curr.summary;
  const cc = curr.curriculum_completion;

  const tierRows = curr.tiers.map(t => `
    <tr><td>Tier ${t.tier}</td><td>${t.title}</td><td>${t.estimated_time}</td>
      <td>${t.lessons_live}/${t.lessons_total}</td><td>${t.completion_pct}%</td>
      <td><a href="${t.primary_route}">${t.primary_route}</a></td><td>${t.status}</td></tr>`).join('');

  const tierCards = curr.tiers.map(t => `
    <div class="mc-card"><h3>Tier ${t.tier}: ${t.title}</h3>
      <p class="mc-bar-note"><strong>Goal:</strong> ${t.learning_goal}</p>
      <p class="mc-bar-note">${t.estimated_time} · ${t.completion_pct}% · ${t.lessons_live}/${t.lessons_total} lessons</p>
      <ul class="mc-deliverables">${t.core_lessons.map(l => `<li>${l}</li>`).join('')}</ul>
      <p class="mc-bar-note">Outcome: ${t.completion_outcome}</p>
    </div>`).join('');

  const pathRows = curr.learning_paths.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.title}</td><td>${p.duration}</td>
      <td>${p.audience}</td><td>Tiers ${p.tiers.join(', ')}</td><td>${p.status}</td></tr>`).join('');

  const levelRows = curr.reading_levels.map(r => `
    <tr><td><code>${r.id}</code></td><td>Level ${r.level}: ${r.title}</td><td>${r.status}</td></tr>`).join('');

  const outcomeRows = curr.educational_outcomes.map(o => `
    <tr><td><code>${o.id}</code></td><td>${o.title}</td><td>${o.status}</td><td>${o.current}</td></tr>`).join('');

  const integrationRows = curr.curriculum_integration.map(i => `
    <tr><td>${i.title}</td><td><a href="${i.route}">${i.route}</a></td><td>Build #${i.build}</td><td>${i.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Master Curriculum</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #35 · ${curr.title}</p>
      <h1>Master Curriculum & Learning Standards</h1>
      <p class="mc-header__question">${curr.governing_principle}</p>
      <blockquote class="mc-bar-note" style="font-style:italic;border-left:3px solid var(--mc-accent);padding-left:1rem">${curr.educational_philosophy}</blockquote>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Curriculum readiness</div><div class="mc-stat__value">${s.curriculum_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Tiers</div><div class="mc-stat__value">${s.tiers_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg tier</div><div class="mc-stat__value">${s.avg_tier_completion_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Lessons live</div><div class="mc-stat__value">${s.lessons_live}/${s.lessons_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Learning paths</div><div class="mc-stat__value">${s.learning_paths}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Enrollment</div><div class="mc-stat__value">${s.enrollment_tracking_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Six Learning Tiers</h2>
    <table class="mc-table"><thead><tr><th>Tier</th><th>Title</th><th>Time</th><th>Lessons</th><th>Complete</th><th>Route</th><th>Status</th></tr></thead>
      <tbody>${tierRows}</tbody></table>
    <div class="mc-grid-2">${tierCards}</div>
    <h2 class="mc-section-title">Learning Paths (${s.learning_paths})</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Path</th><th>Duration</th><th>Audience</th><th>Tiers</th><th>Status</th></tr></thead>
      <tbody>${pathRows}</tbody></table>
    <h2 class="mc-section-title">Reading Levels (${s.reading_levels})</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Level</th><th>Status</th></tr></thead>
      <tbody>${levelRows}</tbody></table>
    <h2 class="mc-section-title">Learning Assessments</h2>
    <ul class="mc-deliverables">${curr.assessments.map(a => `<li>${a.title} <em>(${a.status})</em></li>`).join('')}</ul>
    <p class="mc-bar-note">Optional self-assessments — reinforce learning, not high-stakes tests.</p>
    <h2 class="mc-section-title">Educational Outcomes</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Outcome</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${outcomeRows}</tbody></table>
    <h2 class="mc-section-title">Curriculum Integration (${s.integration_systems} systems)</h2>
    <table class="mc-table"><thead><tr><th>System</th><th>Route</th><th>Build</th><th>Status</th></tr></thead>
      <tbody>${integrationRows}</tbody></table>
    <h2 class="mc-section-title">Academy Alignment</h2>
    <p class="mc-bar-note">${curr.academy_alignment.modules} academy modules · ${curr.academy_alignment.stages} learning stages</p>
    <p class="mc-bar-note">${curr.academy_alignment.note}</p>
    <h2 class="mc-section-title">Curriculum Maintenance</h2>
    <ul class="mc-deliverables">${curr.curriculum_maintenance.triggers.map(t => `<li>${t}</li>`).join('')}</ul>
    <p class="mc-bar-note">Review schedule live: ${curr.curriculum_maintenance.review_schedule_live ? 'yes' : 'no'}</p>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${curr.long_term_vision.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${curr.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${curr.recommended_next_build.number} — ${curr.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${curr.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CURRICULUM.md">MASTER_CURRICULUM.md</a> ·
      <a href="/data/master-curriculum.json">JSON</a> ·
      <a href="/mission-control/education-academy.html">Education Academy</a> ·
      <a href="/mission-control/narrative.html">Narrative</a> ·
      <a href="/start-here/">Tier 1 →</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initTrustFramework() {
  const root = document.getElementById('mc-trust-root');
  if (!root) return;

  const [trustRes, factsRes, evRes, mcRes] = await Promise.all([
    fetch('/data/trust-framework.json'),
    fetch('/data/facts-registry.json'),
    fetch('/data/evidence-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const trust = await trustRes.json();
  const facts = await factsRes.json();
  const ev = await evRes.json();
  const mc = await mcRes.json();
  const s = trust.summary;
  const snap = trust.registry_snapshot;
  const db = trust.database_decision;

  const pyramidCards = trust.trust_pyramid.map(p => `
    <div class="mc-card"><h3>Level ${p.level}: ${p.title}</h3>
      <p class="mc-bar-note">Status: ${p.status}</p>
      <ul class="mc-deliverables">${p.requirements.map(r => `<li>${r}</li>`).join('')}</ul>
    </div>`).join('');

  const evidenceRows = trust.evidence_levels.map(e => `
    <tr><td><code>${e.id}</code></td><td>Level ${e.level}</td><td>${e.title}</td>
      <td>${e.count}</td><td>${e.status}</td></tr>`).join('');

  const reviewRows = trust.fact_review_process.map(r => `
    <tr><td>${r.stage}</td><td>${r.title}</td><td>${r.status}</td></tr>`).join('');

  const metricRows = trust.trust_dashboard_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const panelRows = trust.transparency_panels.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.title}</td><td>${p.purpose}</td><td>${p.status}</td></tr>`).join('');

  const accountabilityRows = trust.public_accountability.map(a => `
    <tr><td>${a.title}</td><td>${a.status}</td>
      <td>${a.route ? `<a href="${a.route}">${a.route}</a>` : '—'}</td></tr>`).join('');

  const trialRows = db.v2_trial_recommended.map(t => `
    <tr><td>${t.provider}</td><td>${t.type}</td><td>${t.status}</td><td>${t.rationale}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Trust Framework</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #36 · ${trust.title}</p>
      <h1>Evidence, Transparency & Trust</h1>
      <p class="mc-header__question">${trust.governing_principle}</p>
      <blockquote class="mc-bar-note" style="font-style:italic;border-left:3px solid var(--mc-accent);padding-left:1rem">${trust.trust_philosophy}</blockquote>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Trust readiness</div><div class="mc-stat__value">${s.trust_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Facts verified</div><div class="mc-stat__value">${snap.facts_verified}/${snap.facts_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Evidence sources</div><div class="mc-stat__value">${snap.evidence_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Citation coverage</div><div class="mc-stat__value">${snap.citation_coverage_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pyramid levels</div><div class="mc-stat__value">${s.trust_pyramid_levels}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Panels live</div><div class="mc-stat__value">${s.transparency_panels_live}</div></div>
    </div>
    <h2 class="mc-section-title">Trust Pyramid</h2>
    <div class="mc-grid-2">${pyramidCards}</div>
    <h2 class="mc-section-title">Evidence Levels (A–D)</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Level</th><th>Title</th><th>Count</th><th>Status</th></tr></thead>
      <tbody>${evidenceRows}</tbody></table>
    <h2 class="mc-section-title">Source Transparency Standards</h2>
    <ul class="mc-deliverables">${trust.source_transparency_standards.map(st => `<li>${st}</li>`).join('')}</ul>
    <p class="mc-bar-note">Page-level sourcing live: ${s.page_sourcing_live ? 'yes' : 'no'}</p>
    <h2 class="mc-section-title">Fact Review Process</h2>
    <table class="mc-table"><thead><tr><th>Stage</th><th>Step</th><th>Status</th></tr></thead>
      <tbody>${reviewRows}</tbody></table>
    <h2 class="mc-section-title">Transparency Panels</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Panel</th><th>Purpose</th><th>Status</th></tr></thead>
      <tbody>${panelRows}</tbody></table>
    <h2 class="mc-section-title">Trust Dashboard Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Public Accountability</h2>
    <table class="mc-table"><thead><tr><th>Page</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${accountabilityRows}</tbody></table>
    <h2 class="mc-section-title">Database Decision (v2)</h2>
    <p class="mc-bar-note"><strong>v1:</strong> ${db.v1_current.storage} (${db.v1_current.status})</p>
    <p class="mc-bar-note"><strong>Rule:</strong> ${db.governing_rule}</p>
    <table class="mc-table"><thead><tr><th>Provider</th><th>Type</th><th>Status</th><th>Rationale</th></tr></thead>
      <tbody>${trialRows}</tbody></table>
    <p class="mc-bar-note"><strong>Deferred:</strong> ${db.v2_full_when_needed.provider} — ${db.v2_full_when_needed.rationale}</p>
    <h2 class="mc-section-title">Long-Term Goal</h2>
    <p class="mc-bar-note">${trust.long_term_goal}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${trust.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${trust.recommended_next_build.number} — ${trust.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${trust.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/PUBLIC_TRUST_OPERATING_SYSTEM.md">PUBLIC_TRUST_OPERATING_SYSTEM.md</a> ·
      <a href="/data/trust-framework.json">JSON</a> ·
      <a href="/data/facts-registry.json">Facts</a> ·
      <a href="/data/evidence-registry.json">Evidence</a> ·
      <a href="/mission-control/database.html">Database Schema</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initMasterResearchLibrary() {
  const root = document.getElementById('mc-research-library-root');
  if (!root) return;

  const [libRes, evRes, mcRes] = await Promise.all([
    fetch('/data/master-research-library.json'),
    fetch('/data/evidence-registry.json'),
    fetch('/data/mission-control.json')
  ]);
  const lib = await libRes.json();
  const ev = await evRes.json();
  const mc = await mcRes.json();
  const s = lib.summary;

  const collectionRows = lib.master_collections.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.letter}</td><td>${c.title}</td>
      <td>${c.documents_archived}/${c.documents_planned}</td><td>${c.completion_pct}%</td><td>${c.status}</td></tr>`).join('');

  const collectionCards = lib.master_collections.map(c => `
    <div class="mc-card"><h3>Collection ${c.letter}: ${c.title}</h3>
      <p class="mc-bar-note">${c.documents_archived}/${c.documents_planned} documents · ${c.status}</p>
      <ul class="mc-deliverables">${c.contains.map(x => `<li>${x}</li>`).join('')}</ul>
    </div>`).join('');

  const listRows = lib.reading_lists.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.title}</td><td>${r.focus}</td>
      <td><a href="${r.route}">${r.route}</a></td><td>${r.status}</td></tr>`).join('');

  const metricRows = lib.library_dashboard_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const workspaceRows = lib.research_workspace.tools.map(t => `
    <tr><td><code>${t.id}</code></td><td>${t.title}</td><td>${t.status}</td></tr>`).join('');

  const evSample = (ev.items || []).slice(0, 10).map(i => `
    <tr><td><code>${i.ev_id}</code></td><td>${i.title}</td><td>${i.source_type}</td>
      <td>${i.review_status || '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Master Research Library</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #37 · ${lib.title}</p>
      <h1>Master Research Library & Digital Archive</h1>
      <p class="mc-header__question">${lib.governing_principle}</p>
      <p class="mc-bar-note">Public: <a href="${lib.public_route}">${lib.public_route}</a> · Canonical: <code>${lib.canonical_archive_route}</code></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Library readiness</div><div class="mc-stat__value">${s.library_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Archived</div><div class="mc-stat__value">${s.documents_archived}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planned</div><div class="mc-stat__value">${s.documents_planned}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Completion</div><div class="mc-stat__value">${s.archive_completion_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Collections</div><div class="mc-stat__value">${s.collections_with_content}/7</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Workspace</div><div class="mc-stat__value">${s.workspace_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Library Philosophy</h2>
    <p class="mc-bar-note">${lib.library_philosophy}</p>
    <h2 class="mc-section-title">Master Collections A–G</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Col</th><th>Collection</th><th>Docs</th><th>Complete</th><th>Status</th></tr></thead>
      <tbody>${collectionRows}</tbody></table>
    <div class="mc-grid-2">${collectionCards}</div>
    <h2 class="mc-section-title">Archive Organization</h2>
    <ul class="mc-deliverables">${lib.archive_organization.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <p class="mc-bar-note">ID: ${lib.archive_organization.id_format} · Evidence: ${lib.archive_organization.evidence_id_format}</p>
    <h2 class="mc-section-title">Relationship Engine</h2>
    <ul class="mc-deliverables">${lib.relationship_engine.targets.map(t => `<li>${t}</li>`).join('')}</ul>
    <p class="mc-bar-note">${lib.relationship_engine.kg_nodes} KG nodes linked</p>
    <h2 class="mc-section-title">Curated Reading Lists</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>List</th><th>Focus</th><th>Route</th><th>Status</th></tr></thead>
      <tbody>${listRows}</tbody></table>
    <h2 class="mc-section-title">Research Workspace</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Tool</th><th>Status</th></tr></thead>
      <tbody>${workspaceRows}</tbody></table>
    <h2 class="mc-section-title">Search Axes (${s.search_axes})</h2>
    <ul class="mc-deliverables">${lib.search_discovery.axes.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Library Dashboard Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Evidence Registry (sample)</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:280px;overflow-y:auto">
      <table class="mc-table"><thead><tr><th>EV ID</th><th>Title</th><th>Type</th><th>Review</th></tr></thead>
        <tbody>${evSample}</tbody></table>
    </div>
    <h2 class="mc-section-title">Research Gaps</h2>
    <ul class="mc-deliverables">${lib.evidence_alignment.research_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${lib.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${lib.recommended_next_build.number} — ${lib.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${lib.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_RESEARCH_LIBRARY.md">MASTER_RESEARCH_LIBRARY.md</a> ·
      <a href="/data/master-research-library.json">JSON</a> ·
      <a href="/data/evidence-registry.json">Evidence Registry</a> ·
      <a href="/library/">Source Library</a> ·
      <a href="/mission-control/trust.html">Trust Framework</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initLearningLaboratory() {
  const root = document.getElementById('mc-learning-lab-root');
  if (!root) return;

  const [labRes, mcRes] = await Promise.all([
    fetch('/data/learning-laboratory.json'),
    fetch('/data/mission-control.json')
  ]);
  const lab = await labRes.json();
  const mc = await mcRes.json();
  const s = lab.summary;

  const labRows = lab.laboratories.map(l => `
    <tr><td>Lab ${l.number}</td><td>${l.title}</td><td>${l.readiness_pct}%</td>
      <td><a href="${l.interim_route}">${l.interim_route}</a></td>
      <td>${l.interactive_live ? 'Yes' : 'No'}</td><td>${l.status}</td></tr>`).join('');

  const labCards = lab.laboratories.map(l => `
    <div class="mc-card"><h3>Lab ${l.number}: ${l.title}</h3>
      <p class="mc-bar-note">${l.purpose}</p>
      <p class="mc-bar-note">${l.readiness_pct}% · Interactive: ${l.interactive_live ? 'live' : 'no'} · ${l.status}</p>
      <ul class="mc-deliverables">${l.features.map(f => `<li>${f}</li>`).join('')}</ul>
      ${l.note ? `<p class="mc-bar-note">${l.note}</p>` : ''}
    </div>`).join('');

  const metricRows = lab.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Learning Laboratory</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #38 · ${lab.title}</p>
      <h1>Interactive Learning Laboratory</h1>
      <p class="mc-header__question">${lab.governing_principle}</p>
      <p class="mc-bar-note">${lab.learning_philosophy}</p>
      <p class="mc-bar-note">Canonical: <code>${lab.canonical_lab_route}</code></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Lab readiness</div><div class="mc-stat__value">${s.learning_lab_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Laboratories</div><div class="mc-stat__value">${s.laboratories_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg lab</div><div class="mc-stat__value">${s.avg_lab_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Interactive live</div><div class="mc-stat__value">${s.interactive_experiences_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Partial</div><div class="mc-stat__value">${s.laboratories_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Engagement</div><div class="mc-stat__value">${s.engagement_tracking_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Ten Laboratories</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Laboratory</th><th>Ready</th><th>Interim</th><th>Interactive</th><th>Status</th></tr></thead>
      <tbody>${labRows}</tbody></table>
    <div class="mc-grid-2">${labCards}</div>
    <h2 class="mc-section-title">Accessibility Standards</h2>
    <ul class="mc-deliverables">${lab.accessibility_standards.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Engagement Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Future Expansion</h2>
    <ul class="mc-deliverables">${lab.future_expansion.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${lab.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${lab.recommended_next_build.number} — ${lab.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${lab.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/INTERACTIVE_LEARNING_LABORATORY.md">INTERACTIVE_LEARNING_LABORATORY.md</a> ·
      <a href="/data/learning-laboratory.json">JSON</a> ·
      <a href="/halls/money-map.html">Money Flow →</a> ·
      <a href="/mission-control/knowledge-graph.html">Knowledge Graph</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initMediaStudio() {
  const root = document.getElementById('mc-media-studio-root');
  if (!root) return;

  const [mediaRes, mcRes] = await Promise.all([
    fetch('/data/media-studio.json'),
    fetch('/data/mission-control.json')
  ]);
  const media = await mediaRes.json();
  const mc = await mcRes.json();
  const s = media.summary;

  const divRows = media.divisions.map(d => `
    <tr><td>Div ${d.number}</td><td>${d.title}</td><td>${d.readiness_pct}%</td>
      <td><a href="${d.interim_route}">${d.interim_route}</a></td>
      <td>${d.video_live ? 'Yes' : 'No'}</td><td>${d.status}</td></tr>`).join('');

  const divCards = media.divisions.map(d => `
    <div class="mc-card"><h3>Division ${d.number}: ${d.title}</h3>
      <p class="mc-bar-note">${d.purpose}</p>
      <p class="mc-bar-note">${d.readiness_pct}% · Video: ${d.video_live ? 'live' : 'no'} · ${d.status}</p>
      <ul class="mc-deliverables">${d.examples.map(e => `<li>${e}</li>`).join('')}</ul>
      ${d.note ? `<p class="mc-bar-note">${d.note}</p>` : ''}
    </div>`).join('');

  const chapterRows = media.documentary_chapters.map(c => `
    <tr><td>Ch ${c.number}</td><td>${c.title}</td><td>${c.readiness_pct}%</td>
      <td><a href="${c.interim_route}">${c.interim_route}</a></td>
      <td>${c.video_live ? 'Yes' : 'No'}</td><td>${c.status}</td></tr>`).join('');

  const metricRows = media.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Media Studio</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #39 · ${media.title}</p>
      <h1>Documentary Experience & Media Studio</h1>
      <p class="mc-header__question">${media.governing_principle}</p>
      <p class="mc-bar-note">${media.vision}</p>
      <p class="mc-bar-note">Canonical: <code>${media.canonical_media_route}</code></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Media readiness</div><div class="mc-stat__value">${s.media_studio_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Divisions</div><div class="mc-stat__value">${s.divisions_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg division</div><div class="mc-stat__value">${s.avg_division_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Videos</div><div class="mc-stat__value">${s.videos_published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Chapters</div><div class="mc-stat__value">${s.documentary_chapters_partial}/${s.documentary_chapters_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Engagement</div><div class="mc-stat__value">${s.engagement_tracking_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Eight Media Divisions</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Division</th><th>Ready</th><th>Interim</th><th>Video</th><th>Status</th></tr></thead>
      <tbody>${divRows}</tbody></table>
    <div class="mc-grid-2">${divCards}</div>
    <h2 class="mc-section-title">Documentary Chapters</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Chapter</th><th>Ready</th><th>Interim</th><th>Video</th><th>Status</th></tr></thead>
      <tbody>${chapterRows}</tbody></table>
    <h2 class="mc-section-title">Chapter Structure (8 elements)</h2>
    <ul class="mc-deliverables">${media.chapter_structure.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Media Standards</h2>
    <ul class="mc-deliverables">${media.media_standards.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Accessibility Standards</h2>
    <ul class="mc-deliverables">${media.accessibility_standards.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Community Media Library</h2>
    <ul class="mc-deliverables">${media.community_media_library.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Engagement Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Future Expansion</h2>
    <ul class="mc-deliverables">${media.future_expansion.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${media.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${media.recommended_next_build.number} — ${media.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${media.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/DOCUMENTARY_EXPERIENCE_MEDIA_STUDIO.md">DOCUMENTARY_EXPERIENCE_MEDIA_STUDIO.md</a> ·
      <a href="/data/media-studio.json">JSON</a> ·
      <a href="/mission-control/narrative.html">Narrative →</a> ·
      <a href="/educate/#toolkit">Presentation Toolkit</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCivicIntelligence() {
  const root = document.getElementById('mc-civic-intelligence-root');
  if (!root) return;

  const [ciRes, mcRes] = await Promise.all([
    fetch('/data/civic-intelligence.json'),
    fetch('/data/mission-control.json')
  ]);
  const ci = await ciRes.json();
  const mc = await mcRes.json();
  const s = ci.summary;

  const nodeRows = ci.node_types.map(n => `
    <tr><td>${n.title}</td><td><code>${n.prefix}</code></td><td>${n.nodes_live}</td><td>${n.status}</td></tr>`).join('');

  const relRows = ci.relationship_types.map(r => `
    <tr><td>${r.title}</td><td>${r.edges_live}</td><td>${r.status}</td></tr>`).join('');

  const layerRows = ci.intelligence_layers.map(l => `
    <tr><td>${l.title}</td><td>${l.readiness_pct}%</td><td><a href="${l.route}">${l.route}</a></td><td>${l.status}</td></tr>`).join('');

  const layerCards = ci.intelligence_layers.map(l => `
    <div class="mc-card"><h3>${l.title}</h3>
      <p class="mc-bar-note">${l.purpose}</p>
      <p class="mc-bar-note">${l.readiness_pct}% · ${l.status}</p>
      ${l.note ? `<p class="mc-bar-note">${l.note}</p>` : ''}
    </div>`).join('');

  const depChain = ci.educational_dependency_chain.map(d => `
    <li>${'→ '.repeat(d.level - 1)}${d.title}${d.kg_id ? ` <code>${d.kg_id}</code>` : ''}</li>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Civic Intelligence</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #40 · ${ci.title}</p>
      <h1>Institutional Brain & Civic Intelligence</h1>
      <p class="mc-header__question">${ci.governing_principle}</p>
      <p class="mc-bar-note">${ci.vision}</p>
      <p class="mc-bar-note">Canonical: <code>${ci.canonical_brain_route}</code> · Foundation: <a href="/mission-control/knowledge-graph.html">KG Build #11</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Brain readiness</div><div class="mc-stat__value">${s.civic_intelligence_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">KG nodes</div><div class="mc-stat__value">${s.kg_nodes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">KG edges</div><div class="mc-stat__value">${s.kg_edges}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Orphans</div><div class="mc-stat__value">${s.kg_orphan_nodes}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Growth</div><div class="mc-stat__value">${s.kg_growth_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Brain viz</div><div class="mc-stat__value">${s.brain_visualization_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Node Types (${s.node_types_total})</h2>
    <table class="mc-table"><thead><tr><th>Type</th><th>Prefix</th><th>Live</th><th>Status</th></tr></thead>
      <tbody>${nodeRows}</tbody></table>
    <h2 class="mc-section-title">Relationship Types (${s.relationship_types_total})</h2>
    <table class="mc-table"><thead><tr><th>Type</th><th>Edges</th><th>Status</th></tr></thead>
      <tbody>${relRows}</tbody></table>
    <h2 class="mc-section-title">Intelligence Layers</h2>
    <table class="mc-table"><thead><tr><th>Layer</th><th>Ready</th><th>Route</th><th>Status</th></tr></thead>
      <tbody>${layerRows}</tbody></table>
    <div class="mc-grid-2">${layerCards}</div>
    <h2 class="mc-section-title">Educational Dependency Chain</h2>
    <ul class="mc-deliverables">${depChain}</ul>
    <h2 class="mc-section-title">Community Intelligence Chain</h2>
    <ul class="mc-deliverables">${ci.community_intelligence_chain.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Knowledge Navigation</h2>
    <ul class="mc-deliverables">${ci.knowledge_navigation.map(k => `<li>${k}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Sample Questions (Question Engine)</h2>
    <ul class="mc-deliverables">${ci.sample_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Institutional Brain Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${ci.mc_integration.metrics.map(m => `
        <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td>
          <td>${m.current}${m.target ? ` / ${m.target}` : ''}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Future AI Integration</h2>
    <ul class="mc-deliverables">${ci.future_ai_integration.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ci.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ci.recommended_next_build.number} — ${ci.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ci.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/INSTITUTIONAL_BRAIN.md">INSTITUTIONAL_BRAIN.md</a> ·
      <a href="/data/civic-intelligence.json">JSON</a> ·
      <a href="/data/kg-registry.json">KG Registry</a> ·
      <a href="/mission-control/knowledge-graph.html">Knowledge Graph</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initEvidenceLedger() {
  const root = document.getElementById('mc-evidence-ledger-root');
  if (!root) return;

  const [ledgerRes, mcRes] = await Promise.all([
    fetch('/data/evidence-ledger.json'),
    fetch('/data/mission-control.json')
  ]);
  const ledger = await ledgerRes.json();
  const mc = await mcRes.json();
  const s = ledger.summary;

  const strengthRows = ledger.evidence_strength_levels.map(l => `
    <tr><td>Level ${l.level}</td><td>${l.title}</td><td>${l.claims_at_level}</td><td>${l.status}</td></tr>`).join('');

  const claimRows = ledger.claims.map(c => `
    <tr><td><code>${c.claim_id}</code></td><td>${c.claim_statement.slice(0, 60)}…</td>
      <td>${c.evidence_strength}</td><td>${c.evidence_count}</td><td>${c.status}</td></tr>`).join('');

  const claimCards = ledger.claims.map(c => `
    <div class="mc-card"><h3><code>${c.claim_id}</code></h3>
      <p class="mc-bar-note">${c.claim_statement}</p>
      <p class="mc-bar-note">Strength: ${c.evidence_strength} · ${c.workflow_stage} · ${c.status}</p>
      <p class="mc-bar-note">EV: ${c.evidence_ids.join(', ')}${c.fact_id ? ` · FACT: ${c.fact_id}` : ''}</p>
      <p class="mc-bar-note"><strong>Why it matters:</strong> ${c.educational_context}</p>
      ${c.note ? `<p class="mc-bar-note">${c.note}</p>` : ''}
    </div>`).join('');

  const workflowRows = ledger.review_workflow.map(w => `
    <tr><td>${w.stage}</td><td>${w.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Evidence Ledger</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #41 · ${ledger.title}</p>
      <h1>Master Evidence Ledger & Claims Registry</h1>
      <p class="mc-header__question">${ledger.governing_principle}</p>
      <p class="mc-bar-note">${ledger.core_philosophy}</p>
      <p class="mc-bar-note">Canonical: <code>${ledger.canonical_claim_route}</code> · Format: <code>${ledger.id_format}</code></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Ledger readiness</div><div class="mc-stat__value">${s.evidence_ledger_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Claims</div><div class="mc-stat__value">${s.claims_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Verified</div><div class="mc-stat__value">${s.claims_verified}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Awaiting review</div><div class="mc-stat__value">${s.claims_awaiting_review}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">EV items</div><div class="mc-stat__value">${s.evidence_items_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Audit trail</div><div class="mc-stat__value">${s.audit_trail_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Evidence Strength Levels (A–E)</h2>
    <table class="mc-table"><thead><tr><th>Level</th><th>Type</th><th>Claims</th><th>Status</th></tr></thead>
      <tbody>${strengthRows}</tbody></table>
    <h2 class="mc-section-title">Claim Registry</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Statement</th><th>Strength</th><th>Sources</th><th>Status</th></tr></thead>
      <tbody>${claimRows}</tbody></table>
    <div class="mc-grid-2">${claimCards}</div>
    <h2 class="mc-section-title">Review Workflow</h2>
    <table class="mc-table"><thead><tr><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${workflowRows}</tbody></table>
    <h2 class="mc-section-title">Evidence Link Types</h2>
    <ul class="mc-deliverables">${ledger.evidence_link_types.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Contradictory Evidence Policy</h2>
    <ul class="mc-deliverables">${ledger.contradictory_evidence_policy.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Public Transparency</h2>
    <ul class="mc-deliverables">${ledger.public_transparency.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Evidence Ledger Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${ledger.mc_integration.metrics.map(m => `
        <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td>
          <td>${m.current}${m.target ? ` / ${m.target}` : ''}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Foundations</h2>
    <ul class="mc-deliverables">${Object.entries(ledger.foundations).map(([k, v]) =>
      `<li>${k}: <a href="${v['route']}">${v['route']}</a> (Build #${v['build']})</li>`).join('')}</ul>
    <h2 class="mc-section-title">Future AI Integration</h2>
    <ul class="mc-deliverables">${ledger.future_ai_integration.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ledger.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ledger.recommended_next_build.number} — ${ledger.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ledger.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_EVIDENCE_LEDGER.md">MASTER_EVIDENCE_LEDGER.md</a> ·
      <a href="/data/evidence-ledger.json">JSON</a> ·
      <a href="/data/claims-ledger.json">Legacy Claims</a> ·
      <a href="/data/evidence-registry.json">Evidence Registry</a> ·
      <a href="/mission-control/trust.html">Trust Framework</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCivicActionLab() {
  const root = document.getElementById('mc-civic-action-lab-root');
  if (!root) return;

  const [labRes, mcRes] = await Promise.all([
    fetch('/data/civic-action-lab.json'),
    fetch('/data/mission-control.json')
  ]);
  const lab = await labRes.json();
  const mc = await mcRes.json();
  const s = lab.summary;

  const divRows = lab.divisions.map(d => `
    <tr><td>Div ${d.number}</td><td>${d.title}</td><td>${d.readiness_pct}%</td>
      <td><a href="${d.interim_route}">${d.interim_route}</a></td><td>${d.status}</td></tr>`).join('');

  const divCards = lab.divisions.map(d => `
    <div class="mc-card"><h3>Division ${d.number}: ${d.title}</h3>
      <p class="mc-bar-note">${d.purpose}</p>
      <p class="mc-bar-note">${d.readiness_pct}% · ${d.status}</p>
      <ul class="mc-deliverables">${d.examples.map(e => `<li>${e}</li>`).join('')}</ul>
      ${d.note ? `<p class="mc-bar-note">${d.note}</p>` : ''}
    </div>`).join('');

  const metricRows = lab.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const philosophy = lab.core_philosophy.map((p, i) =>
    `${p}${i < lab.core_philosophy.length - 1 ? ' →' : ''}`).join(' ');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Civic Action Lab</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #42 · ${lab.title}</p>
      <h1>Master Civic Action Lab</h1>
      <p class="mc-header__question">${lab.governing_principle}</p>
      <p class="mc-bar-note">${lab.not_a_campaign}</p>
      <p class="mc-bar-note">Philosophy: ${philosophy}</p>
      <p class="mc-bar-note">Canonical: <code>${lab.canonical_lab_route}</code></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Lab readiness</div><div class="mc-stat__value">${s.civic_action_lab_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Divisions</div><div class="mc-stat__value">${s.divisions_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg division</div><div class="mc-stat__value">${s.avg_division_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Comparisons</div><div class="mc-stat__value">${s.comparative_studies_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Draft builder</div><div class="mc-stat__value">${s.guided_draft_builder_live ? 'Live' : 'Planned'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Submissions</div><div class="mc-stat__value">${s.model_law_submissions + s.ballot_lab_submissions}</div></div>
    </div>
    <h2 class="mc-section-title">Six Divisions</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Division</th><th>Ready</th><th>Interim</th><th>Status</th></tr></thead>
      <tbody>${divRows}</tbody></table>
    <div class="mc-grid-2">${divCards}</div>
    <h2 class="mc-section-title">Legislative Tracker (7 elements)</h2>
    <ul class="mc-deliverables">${lab.legislative_tracker.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Draft Builder</h2>
    <p class="mc-bar-note">${lab.draft_builder.title} — ${lab.draft_builder.status}</p>
    <ul class="mc-deliverables">${lab.draft_builder.workspaces.map(w =>
      `<li>${w.title}: <a href="${w.route}">${w.route}</a> (${w.status})</li>`).join('')}</ul>
    <ul class="mc-deliverables">${lab.draft_builder.steps.map(st => `<li>${st}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Public Official Education Center</h2>
    <p class="mc-bar-note"><a href="${lab.public_official_center.route}">${lab.public_official_center.route}</a> · ${lab.public_official_center.status}</p>
    <ul class="mc-deliverables">${lab.public_official_center.audiences.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Civic Action Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Future Expansion</h2>
    <ul class="mc-deliverables">${lab.future_expansion.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${lab.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${lab.recommended_next_build.number} — ${lab.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${lab.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CIVIC_ACTION_LAB.md">MASTER_CIVIC_ACTION_LAB.md</a> ·
      <a href="/data/civic-action-lab.json">JSON</a> ·
      <a href="/solutions/">Solutions Hub</a> ·
      <a href="/action/ballot-lab.html">Ballot Lab</a> ·
      <a href="/action/contact-legislators.html">Official Education</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initResearchMethodology() {
  const root = document.getElementById('mc-research-methodology-root');
  if (!root) return;

  const [rmRes, mcRes] = await Promise.all([
    fetch('/data/research-methodology.json'),
    fetch('/data/mission-control.json')
  ]);
  const rm = await rmRes.json();
  const mc = await mcRes.json();
  const s = rm.summary;

  const principleRows = rm.principles.map(p => `
    <tr><td>P${p.number}</td><td>${p.title}</td><td>${p.readiness_pct}%</td>
      <td>${p.in_build_10 ? 'Build #10' : 'New'}</td><td>${p.status}</td></tr>`).join('');

  const principleCards = rm.principles.map(p => `
    <div class="mc-card"><h3>Principle ${p.number}: ${p.title}</h3>
      <p class="mc-bar-note">${p.description}</p>
      <p class="mc-bar-note">${p.readiness_pct}% · ${p.status}${p.in_build_10 ? ' · in Build #10' : ''}</p>
      ${p.examples ? `<ul class="mc-deliverables">${p.examples.map(e => `<li>${e}</li>`).join('')}</ul>` : ''}
    </div>`).join('');

  const workflowRows = rm.research_workflow.map(w => `
    <tr><td>${w.stage}</td><td>${w.title}</td><td>${w.status}</td></tr>`).join('');

  const metricRows = rm.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td>
      <td>${m.current}${m.target ? ` / ${m.target}` : ''}${m.unit || ''}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Research Methodology</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #43 · ${rm.title}</p>
      <h1>Research Methodology & Standards</h1>
      <p class="mc-header__question">${rm.governing_principle}</p>
      <p class="mc-bar-note"><strong>${rm.core_question}</strong></p>
      <p class="mc-bar-note">Foundation: <a href="/mission-control/research.html">Research Framework Build #10</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Methodology readiness</div><div class="mc-stat__value">${s.research_methodology_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Principles</div><div class="mc-stat__value">${s.principles_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg principle</div><div class="mc-stat__value">${s.avg_principle_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">EV items</div><div class="mc-stat__value">${s.evidence_items}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Citations</div><div class="mc-stat__value">${s.citation_coverage_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Adherence</div><div class="mc-stat__value">${s.adherence_tracking_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Ten Research Principles</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Principle</th><th>Ready</th><th>Origin</th><th>Status</th></tr></thead>
      <tbody>${principleRows}</tbody></table>
    <div class="mc-grid-2">${principleCards}</div>
    <h2 class="mc-section-title">Research Workflow (11 stages)</h2>
    <table class="mc-table"><thead><tr><th>Stage</th><th>Step</th><th>Status</th></tr></thead>
      <tbody>${workflowRows}</tbody></table>
    <h2 class="mc-section-title">Source Evaluation Checklist</h2>
    <ul class="mc-deliverables">${rm.source_evaluation_checklist.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Citation Standards</h2>
    <ul class="mc-deliverables">${rm.citation_standards.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Research Documentation</h2>
    <ul class="mc-deliverables">${rm.research_documentation.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Quality Assurance</h2>
    <ul class="mc-deliverables">${rm.quality_assurance.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Institutional Responsibility</h2>
    <ul class="mc-deliverables">${rm.institutional_responsibility.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Research Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Future Research Capacity</h2>
    <ul class="mc-deliverables">${rm.future_capacity.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${rm.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${rm.recommended_next_build.number} — ${rm.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${rm.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_RESEARCH_METHODOLOGY.md">MASTER_RESEARCH_METHODOLOGY.md</a> ·
      <a href="/data/research-methodology.json">JSON</a> ·
      <a href="/data/research-framework.json">Research Framework</a> ·
      <a href="/data/evidence-registry.json">Evidence Registry</a> ·
      <a href="/docs/CITATION_GUIDE.md">Citation Guide</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

  initDevConsole(mc);
}

async function initInstitutionalRoadmap() {
  const root = document.getElementById('mc-institutional-roadmap-root');
  if (!root) return;

  const [irRes, mcRes] = await Promise.all([
    fetch('/data/institutional-roadmap.json'),
    fetch('/data/mission-control.json')
  ]);
  const ir = await irRes.json();
  const mc = await mcRes.json();
  const s = ir.summary;

  const versionRows = ir.versions.map(v => `
    <tr><td>V${v.version}</td><td>${v.title}</td><td>${v.maturity_pct}%</td>
      <td>${v.current_phase}</td><td>${v.status}</td></tr>`).join('');

  const versionCards = ir.versions.map(v => `
    <div class="mc-card"><h3>V${v.version}: ${v.title}</h3>
      <p class="mc-bar-note"><strong>Goal:</strong> ${v.primary_goal}</p>
      <p class="mc-bar-note">${v.maturity_pct}% · ${v.current_phase} · ${v.status}</p>
      <p class="mc-bar-note"><strong>Deliverables:</strong></p>
      <ul class="mc-deliverables">${v.deliverables.slice(0, 4).map(d => `<li>${d}</li>`).join('')}
        ${v.deliverables.length > 4 ? `<li>+${v.deliverables.length - 4} more</li>` : ''}</ul>
      ${v.note ? `<p class="mc-bar-note">${v.note}</p>` : ''}
    </div>`).join('');

  const metricRows = ir.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Institutional Roadmap</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #44 · ${ir.title}</p>
      <h1>Master Institutional Roadmap</h1>
      <p class="mc-header__question">${ir.governing_principle}</p>
      <p class="mc-bar-note">${ir.current_institutional_phase}</p>
      <p class="mc-bar-note">Software: Build #${ir.software_build} (v${ir.software_version}) · Institutional: <strong>${ir.current_institutional_version}</strong> → ${ir.next_institutional_version}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Institutional maturity</div><div class="mc-stat__value">${s.institutional_maturity_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Current version</div><div class="mc-stat__value">${s.current_institutional_version}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">V1 maturity</div><div class="mc-stat__value">${s.v1_maturity_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg version</div><div class="mc-stat__value">${s.avg_version_maturity_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Software builds</div><div class="mc-stat__value">${s.software_builds_complete}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Annual review</div><div class="mc-stat__value">${s.annual_review_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Institutional Vision</h2>
    <ul class="mc-deliverables">${ir.institutional_vision.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Ten Institutional Versions</h2>
    <table class="mc-table"><thead><tr><th>Ver</th><th>Title</th><th>Maturity</th><th>Phase</th><th>Status</th></tr></thead>
      <tbody>${versionRows}</tbody></table>
    <div class="mc-grid-2">${versionCards}</div>
    <h2 class="mc-section-title">Success Definition</h2>
    <p class="mc-bar-note">${ir.success_definition}</p>
    <h2 class="mc-section-title">Cross-Version Priorities</h2>
    <ul class="mc-deliverables">${ir.cross_version_priorities.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Annual Strategic Review</h2>
    <ul class="mc-deliverables">${ir.annual_strategic_review.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Preservation Strategy</h2>
    <ul class="mc-deliverables">${ir.preservation_strategy.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Long-Term Sustainability</h2>
    <ul class="mc-deliverables">${ir.sustainability_planning.map(su => `<li>${su}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Institutional Maturity Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ir.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ir.recommended_next_build.number} — ${ir.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ir.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_INSTITUTIONAL_ROADMAP.md">MASTER_INSTITUTIONAL_ROADMAP.md</a> ·
      <a href="/data/institutional-roadmap.json">JSON</a> ·
      <a href="/mission-control/campaign-os.html">Campaign OS</a> ·
      <a href="/builds/">Build Registry</a> ·
      <a href="/mission-control/executive.html">Executive</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initSystemsIntegration() {
  const root = document.getElementById('mc-systems-integration-root');
  if (!root) return;

  const [siRes, mcRes] = await Promise.all([
    fetch('/data/systems-integration.json'),
    fetch('/data/mission-control.json')
  ]);
  const si = await siRes.json();
  const mc = await mcRes.json();
  const s = si.summary;
  const health = si.systems_health_dashboard;

  const sysRows = si.systems.map(sys => `
    <tr><td>${sys.number}</td><td>${sys.title}</td><td>${sys.integration_pct}%</td>
      <td><a href="${sys.route}">${sys.route}</a></td>
      <td>${sys.data_flow_live ? 'Yes' : 'No'}</td><td>${sys.status}</td></tr>`).join('');

  const sysCards = si.systems.map(sys => `
    <div class="mc-card"><h3>System ${sys.number}: ${sys.title}</h3>
      <p class="mc-bar-note">${sys.purpose}</p>
      <p class="mc-bar-note">${sys.integration_pct}% · Flow: ${sys.data_flow_live ? 'live' : 'manual'} · ${sys.status}</p>
      <p class="mc-bar-note"><strong>Produces:</strong> ${sys.produces.slice(0, 3).join(', ')}…</p>
      ${sys.note ? `<p class="mc-bar-note">${sys.note}</p>` : ''}
    </div>`).join('');

  const healthRows = health.indicators.map(h => `
    <tr><td>${h.title}</td><td>${h.score}%</td><td>${h.status}</td></tr>`).join('');

  const flow = si.information_flow.map((f, i) =>
    `${f}${i < si.information_flow.length - 1 ? ' →' : ''}`).join(' ');

  const journey = si.unified_user_journey.map((j, i) =>
    `${j}${i < si.unified_user_journey.length - 1 ? ' →' : ''}`).join(' ');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Systems Integration</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #45 · ${si.title}</p>
      <h1>Master Systems Integration Blueprint</h1>
      <p class="mc-header__question">${si.governing_principle}</p>
      <p class="mc-bar-note">${si.purpose}</p>
      <p class="mc-bar-note">Conductor: <a href="/mission-control/">Mission Control</a> · Nervous system: <a href="/mission-control/civic-intelligence.html">Knowledge Graph</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Integration readiness</div><div class="mc-stat__value">${s.systems_integration_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Systems</div><div class="mc-stat__value">${s.systems_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live flows</div><div class="mc-stat__value">${s.systems_with_live_data_flow}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg integration</div><div class="mc-stat__value">${s.avg_system_integration_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Health avg</div><div class="mc-stat__value">${s.avg_systems_health_score}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Synthesis</div><div class="mc-stat__value">${s.executive_synthesis_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Twelve Primary Systems</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>System</th><th>Integration</th><th>Route</th><th>Live flow</th><th>Status</th></tr></thead>
      <tbody>${sysRows}</tbody></table>
    <div class="mc-grid-2">${sysCards}</div>
    <h2 class="mc-section-title">Information Flow Cycle</h2>
    <p class="mc-bar-note">${flow}</p>
    <h2 class="mc-section-title">Systems Health Dashboard</h2>
    <table class="mc-table"><thead><tr><th>Indicator</th><th>Score</th><th>Status</th></tr></thead>
      <tbody>${healthRows}</tbody></table>
    <h2 class="mc-section-title">Executive Intelligence Questions</h2>
    <ul class="mc-deliverables">${si.executive_intelligence.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Unified User Journey</h2>
    <p class="mc-bar-note">${journey}</p>
    <h2 class="mc-section-title">Institutional Memory</h2>
    <ul class="mc-deliverables">${si.institutional_memory.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Integration Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${si.mc_integration.metrics.map(m => `
        <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('')}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${si.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${si.recommended_next_build.number} — ${si.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${si.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_SYSTEMS_INTEGRATION.md">MASTER_SYSTEMS_INTEGRATION.md</a> ·
      <a href="/data/systems-integration.json">JSON</a> ·
      <a href="/mission-control/executive.html">Executive</a> ·
      <a href="/data/institutional-roadmap.json">Roadmap</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

  initDevConsole(mc);
}

async function initContentProductionMatrix() {
  const root = document.getElementById('mc-content-production-matrix-root');
  if (!root) return;

  const [cpmRes, mcRes] = await Promise.all([
    fetch('/data/content-production-matrix.json'),
    fetch('/data/mission-control.json')
  ]);
  const cpm = await cpmRes.json();
  const mc = await mcRes.json();
  const s = cpm.summary;
  const dash = cpm.executive_production_dashboard;
  const cap = cpm.capacity_planning;

  const domainRows = cpm.domains.map(d => `
    <tr><td>${d.id}</td><td>${d.title}</td><td>${d.estimated_assets}</td>
      <td>${d.registered}</td><td>${d.published}</td><td>${d.in_pipeline}</td>
      <td>${d.queue_coverage_pct}%</td><td>${d.status}</td></tr>`).join('');

  const domainCards = cpm.domains.map(d => `
    <div class="mc-card"><h3>Domain ${d.id}: ${d.title}</h3>
      <p class="mc-bar-note">${d.purpose}</p>
      <p class="mc-bar-note">${d.registered}/${d.estimated_assets} queued · ${d.published} published · ${d.status}</p>
      <p class="mc-bar-note"><strong>Examples:</strong> ${d.examples.slice(0, 3).join(', ')}…</p>
    </div>`).join('');

  const prodRows = dash.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.current}</td>
      <td>${m.target}</td><td>${m.status}</td></tr>`).join('');

  const queueRows = cpm.production_queue.items.map(q => `
    <tr><td><code>${q.production_id}</code></td><td>${q.title}</td>
      <td>${q.matrix_domain}</td><td>${q.stage}</td><td>${q.completion_pct}%</td>
      <td>${q.url ? `<a href="${q.url}">view</a>` : '—'}</td></tr>`).join('');

  const stageFlow = cpm.production_stages.map((st, i) =>
    `${st}${i < cpm.production_stages.length - 1 ? ' →' : ''}`).join(' ');

  const metricRows = cpm.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Content Production Matrix</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #46 · ${cpm.title}</p>
      <h1>Master Content Production Matrix</h1>
      <p class="mc-header__question">${cpm.governing_principle}</p>
      <p class="mc-bar-note">${cpm.purpose}</p>
      <p class="mc-bar-note">Extends <a href="/mission-control/inventory.html">Content Inventory</a> · <a href="/mission-control/content-factory.html">Production Factory</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Matrix readiness</div><div class="mc-stat__value">${s.production_matrix_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Domains</div><div class="mc-stat__value">${s.domains_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Queued</div><div class="mc-stat__value">${s.assets_registered}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Published</div><div class="mc-stat__value">${s.assets_published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">In pipeline</div><div class="mc-stat__value">${s.assets_in_pipeline}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Completion</div><div class="mc-stat__value">${s.overall_completion_pct}%</div></div>
    </div>
    <h2 class="mc-section-title">Executive Production Dashboard</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${prodRows}</tbody></table>
    <h2 class="mc-section-title">Fourteen Content Domains</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Domain</th><th>Est.</th><th>Queued</th><th>Pub.</th><th>Pipeline</th><th>Coverage</th><th>Status</th></tr></thead>
      <tbody>${domainRows}</tbody></table>
    <div class="mc-grid-2">${domainCards}</div>
    <h2 class="mc-section-title">Production Pipeline</h2>
    <p class="mc-bar-note">${stageFlow}</p>
    <h2 class="mc-section-title">Production ID Prefixes</h2>
    <p class="mc-bar-note">${cpm.production_id_prefixes.join(' · ')}</p>
    <h2 class="mc-section-title">Production Queue (sample ${cpm.production_queue.sample_size})</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Title</th><th>Domain</th><th>Stage</th><th>%</th><th>URL</th></tr></thead>
      <tbody>${queueRows}</tbody></table>
    <p class="mc-bar-note"><a href="${cpm.production_queue.full_registry}">Full registry → ${cpm.production_queue.total_registered} items</a></p>
    <h2 class="mc-section-title">Capacity Planning</h2>
    <ul class="mc-deliverables">
      <li>Remaining: ${cap.remaining_assets} assets</li>
      <li>Queue coverage: ${cap.queue_coverage_pct}%</li>
      <li>Research backlog: ${cap.research_backlog}</li>
      <li>Editorial workload: ${cap.editorial_workload}</li>
      <li>Review workload: ${cap.review_workload}</li>
      <li>Expected completion: ${cap.expected_completion}</li>
    </ul>
    <h2 class="mc-section-title">Future Automation</h2>
    <ul class="mc-deliverables">${cpm.future_automation.capabilities.map(a => `<li>${a}</li>`).join('')}</ul>
    <p class="mc-bar-note">${cpm.future_automation.editorial_gate}</p>
    <h2 class="mc-section-title">Matrix Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cpm.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cpm.recommended_next_build.number} — ${cpm.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cpm.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CONTENT_PRODUCTION_MATRIX.md">MASTER_CONTENT_PRODUCTION_MATRIX.md</a> ·
      <a href="/data/content-production-matrix.json">JSON</a> ·
      <a href="/mission-control/inventory.html">Content Inventory</a> ·
      <a href="/mission-control/systems-integration.html">Systems Integration</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initVisitorJourney() {
  const root = document.getElementById('mc-visitor-journey-root');
  if (!root) return;

  const [vjRes, mcRes] = await Promise.all([
    fetch('/data/visitor-journey.json'),
    fetch('/data/mission-control.json')
  ]);
  const vj = await vjRes.json();
  const mc = await mcRes.json();
  const s = vj.summary;

  const stageRows = vj.transformation_stages.map(st => `
    <tr><td>${st.number}</td><td>${st.title}</td><td>${st.success_metric}</td>
      <td>${st.tracking_live ? 'Yes' : 'No'}</td><td>${st.status}</td></tr>`).join('');

  const stageCards = vj.transformation_stages.map(st => `
    <div class="mc-card"><h3>Stage ${st.number}: ${st.title}</h3>
      <p class="mc-bar-note">${st.description}</p>
      <p class="mc-bar-note"><strong>Goal:</strong> ${st.platform_goal}</p>
      <p class="mc-bar-note"><strong>Metric:</strong> ${st.success_metric} · ${st.tracking_live ? 'tracked' : 'not tracked'}</p>
      ${st.note ? `<p class="mc-bar-note">${st.note}</p>` : ''}
    </div>`).join('');

  const mapFlow = vj.journey_map.map((r, i) =>
    `${r.title}${i < vj.journey_map.length - 1 ? ' →' : ''}`).join(' ');

  const stageFlow = vj.transformation_stages.map((st, i) =>
    `${st.title}${i < vj.transformation_stages.length - 1 ? ' →' : ''}`).join(' ');

  const decisionRows = vj.decision_points.map(d => `
    <tr><td>${d.order}</td><td>${d.invitation}</td><td><a href="${d.route}">${d.route}</a></td>
      <td>${d.stage}</td></tr>`).join('');

  const analyticsRows = vj.journey_analytics.metrics.map(a => `
    <tr><td><code>${a.id}</code></td><td>${a.title}</td><td>${a.current}</td>
      <td>${a.target}</td><td>${a.status}</td></tr>`).join('');

  const metricRows = vj.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const mappingRows = vj.build_8_mapping.mapping.map(m => `
    <tr><td>${m.build_8 || '—'}</td><td>${m.build_47 || m.build_47_only || '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Visitor Journey</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #47 · ${vj.title}</p>
      <h1>Master Visitor Journey & Behavioral Architecture</h1>
      <p class="mc-header__question">${vj.governing_principle}</p>
      <p class="mc-bar-note">${vj.purpose}</p>
      <p class="mc-bar-note">Extends <a href="/mission-control/journey.html">Build #8 Citizen Journey</a> · <a href="/data/ux-journey.json">ux-journey.json</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Journey readiness</div><div class="mc-stat__value">${s.visitor_journey_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Stages</div><div class="mc-stat__value">${s.stages_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Tracked</div><div class="mc-stat__value">${s.stages_with_live_tracking}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Leaders</div><div class="mc-stat__value">${s.education_leader_signups}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Milestones</div><div class="mc-stat__value">${s.milestones_achieved}/${s.milestones_defined}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Analytics</div><div class="mc-stat__value">${s.journey_analytics_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Eight Transformation Stages</h2>
    <p class="mc-bar-note">${stageFlow}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>Stage</th><th>Success Metric</th><th>Tracked</th><th>Status</th></tr></thead>
      <tbody>${stageRows}</tbody></table>
    <div class="mc-grid-2">${stageCards}</div>
    <h2 class="mc-section-title">Journey Map</h2>
    <p class="mc-bar-note">${mapFlow}</p>
    <h2 class="mc-section-title">Decision Points</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>Invitation</th><th>Route</th><th>Stage</th></tr></thead>
      <tbody>${decisionRows}</tbody></table>
    <h2 class="mc-section-title">Behavioral Design</h2>
    <p class="mc-bar-note"><strong>Encourage:</strong> ${vj.behavioral_design.encourage.join(', ')}</p>
    <p class="mc-bar-note"><strong>Avoid:</strong> ${vj.behavioral_design.avoid.join(', ')} — ${vj.behavioral_design.principle}</p>
    <h2 class="mc-section-title">Motivation Milestones</h2>
    <ul class="mc-deliverables">${vj.motivation_system.milestones.map(m => `<li><code>${m.id}</code> ${m.title} (${m.stage}) — ${m.status}</li>`).join('')}</ul>
    <p class="mc-bar-note">${vj.motivation_system.recognition_style}</p>
    <h2 class="mc-section-title">Journey Analytics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${analyticsRows}</tbody></table>
    <h2 class="mc-section-title">Build #8 → Build #47 Mapping</h2>
    <table class="mc-table"><thead><tr><th>Build #8 Ladder</th><th>Build #47 Stage</th></tr></thead>
      <tbody>${mappingRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Community Model</h2>
    <ul class="mc-deliverables">${Object.entries(vj.long_term_community_model).map(([k, v]) => `<li><strong>${k.replace(/_/g, ' ')}:</strong> ${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Journey Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${vj.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${vj.recommended_next_build.number} — ${vj.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${vj.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_VISITOR_JOURNEY.md">MASTER_VISITOR_JOURNEY.md</a> ·
      <a href="/data/visitor-journey.json">JSON</a> ·
      <a href="/mission-control/journey.html">Build #8 Journey</a> ·
      <a href="/mission-control/systems-integration.html">Systems Integration</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initTechnicalArchitecture() {
  const root = document.getElementById('mc-technical-architecture-root');
  if (!root) return;

  const [taRes, mcRes] = await Promise.all([
    fetch('/data/technical-architecture.json'),
    fetch('/data/mission-control.json')
  ]);
  const ta = await taRes.json();
  const mc = await mcRes.json();
  const s = ta.summary;

  const stackRows = ta.technology_stack.map(l => `
    <tr><td>${l.layer}</td><td>${l.target}</td><td>${l.status}</td>
      <td>${l.current}</td></tr>`).join('');

  const apiRows = ta.apis.map(a => `
    <tr><td><code>${a.id}</code></td><td>${a.name}</td><td>${a.status}</td><td>${a.current}</td></tr>`).join('');

  const envRows = ta.environments.map(e => `
    <tr><td>${e.title}</td><td>${e.status}</td><td>${e.current}</td></tr>`).join('');

  const monRows = ta.monitoring.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.area}</td><td>${m.status}</td><td>${m.current || m.note || ''}</td></tr>`).join('');

  const perfRows = ta.performance_standards.map(p => `
    <tr><td>${p.standard}</td><td>${p.status}</td><td>${p.note || ''}</td></tr>`).join('');

  const metricRows = ta.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const deployFlow = ta.deployment_workflow.map((d, i) =>
    `${d}${i < ta.deployment_workflow.length - 1 ? ' →' : ''}`).join(' ');

  const aiFlow = ta.ai_layer.sources.map((src, i) =>
    `${src}${i < ta.ai_layer.sources.length - 1 ? ' →' : ''}`).join(' ');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Technical Architecture</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #48 · ${ta.title}</p>
      <h1>Master Technical Architecture & Deployment Blueprint</h1>
      <p class="mc-header__question">${ta.governing_principle}</p>
      <p class="mc-bar-note">${ta.purpose}</p>
      <p class="mc-bar-note">Extends <a href="/mission-control/platform.html">Build #20 Platform Blueprint</a> · <a href="/mission-control/repository.html">Repository</a> · <a href="/mission-control/database.html">Database Schema</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Architecture readiness</div><div class="mc-stat__value">${s.technical_architecture_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Stack live</div><div class="mc-stat__value">${s.stack_live}/${s.stack_layers_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">APIs partial</div><div class="mc-stat__value">${s.apis_partial_or_live}/${s.apis_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Preview deploys</div><div class="mc-stat__value">${s.preview_deploys_live ? 'Yes' : 'No'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Next.js</div><div class="mc-stat__value">${s.nextjs_migration ? 'Yes' : 'Planned'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Neon DB</div><div class="mc-stat__value">${s.neon_postgres_live ? 'Yes' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Technology Stack</h2>
    <table class="mc-table"><thead><tr><th>Layer</th><th>Target</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${stackRows}</tbody></table>
    <h2 class="mc-section-title">Deployment Workflow</h2>
    <p class="mc-bar-note">${deployFlow}</p>
    <h2 class="mc-section-title">Environments</h2>
    <table class="mc-table"><thead><tr><th>Environment</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${envRows}</tbody></table>
    <h2 class="mc-section-title">CMS Philosophy</h2>
    <p class="mc-bar-note">${ta.cms_philosophy.approach}</p>
    <p class="mc-bar-note">${ta.cms_philosophy.article_lifecycle.join(' → ')}</p>
    <p class="mc-bar-note">${ta.cms_philosophy.current}</p>
    <h2 class="mc-section-title">Search Architecture</h2>
    <p class="mc-bar-note">${ta.search_architecture.index_types.join(' · ')}</p>
    <h2 class="mc-section-title">AI Layer (Grounded)</h2>
    <p class="mc-bar-note">${ta.ai_layer.principle}</p>
    <p class="mc-bar-note">${aiFlow}</p>
    <p class="mc-bar-note">${ta.ai_layer.current}</p>
    <h2 class="mc-section-title">Internal APIs</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>API</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${apiRows}</tbody></table>
    <h2 class="mc-section-title">Target File Structure</h2>
    <p class="mc-bar-note"><code>${ta.file_architecture.directories.join(' · ')}</code></p>
    <p class="mc-bar-note">${ta.file_architecture.current}</p>
    <h2 class="mc-section-title">Performance Standards</h2>
    <table class="mc-table"><thead><tr><th>Standard</th><th>Status</th><th>Note</th></tr></thead>
      <tbody>${perfRows}</tbody></table>
    <h2 class="mc-section-title">Accessibility Standards</h2>
    <ul class="mc-deliverables">${ta.accessibility_standards.map(a => `<li>${a.standard} — ${a.status}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Security</h2>
    <ul class="mc-deliverables">${ta.security.map(sec => `<li>${sec.area} — ${sec.status}${sec.note ? ' (' + sec.note + ')' : ''}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Analytics Philosophy</h2>
    <p class="mc-bar-note"><strong>Measure:</strong> ${ta.analytics_philosophy.measure.join(' → ')}</p>
    <p class="mc-bar-note"><strong>Avoid:</strong> ${ta.analytics_philosophy.avoid.join(', ')}</p>
    <h2 class="mc-section-title">Monitoring</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Area</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${monRows}</tbody></table>
    <h2 class="mc-section-title">Backup Strategy</h2>
    <ul class="mc-deliverables">${ta.backup_strategy.map(b => `<li>${b.item} — ${b.status}${b.note ? ' (' + b.note + ')' : ''}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Technical Principles</h2>
    <ul class="mc-deliverables">${ta.technical_principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Architecture Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ta.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ta.recommended_next_build.number} — ${ta.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ta.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_TECHNICAL_ARCHITECTURE.md">MASTER_TECHNICAL_ARCHITECTURE.md</a> ·
      <a href="/data/technical-architecture.json">JSON</a> ·
      <a href="/mission-control/platform.html">Platform Blueprint</a> ·
      <a href="/mission-control/visitor-journey.html">Visitor Journey</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initGovernanceConstitution() {
  const root = document.getElementById('mc-governance-root');
  if (!root) return;

  const [govRes, mcRes] = await Promise.all([
    fetch('/data/governance-constitution.json'),
    fetch('/data/mission-control.json')
  ]);
  const gov = await govRes.json();
  const mc = await mcRes.json();
  const s = gov.summary;

  const valueRows = gov.institutional_values.map(v => `
    <tr><td><code>${v.id}</code></td><td>${v.title}</td><td>${v.status}</td><td>${v.implementation}</td></tr>`).join('');

  const stewardRows = gov.governance_structure.stewards.map(st => `
    <tr><td><code>${st.id}</code></td><td>${st.title}</td><td>${st.scope}</td>
      <td>${st.assigned ? 'Yes' : 'No'}</td><td>${st.status}</td></tr>`).join('');

  const respRows = gov.institutional_responsibilities.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.title}</td><td>${r.status}</td>
      <td>${r.route ? `<a href="${r.route}">${r.route}</a>` : '—'}</td></tr>`).join('');

  const pubRows = gov.public_accountability.map(p => `
    <tr><td>${p.document}</td><td>${p.status}</td>
      <td>${p.route ? `<a href="${p.route}">view</a>` : '—'}</td></tr>`).join('');

  const decRows = gov.decision_categories.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.title}</td><td>${d.description}</td><td>${d.mc_logging}</td></tr>`).join('');

  const memRows = gov.institutional_memory.map(m => `
    <tr><td>${m.type}</td><td>${m.status}</td><td>${m.current || ''}</td></tr>`).join('');

  const metricRows = gov.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const corrFlow = gov.correction_policy.steps.map((st, i) =>
    `${st}${i < gov.correction_policy.steps.length - 1 ? ' →' : ''}`).join(' ');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Governance & Constitution</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #49 · ${gov.title}</p>
      <h1>Master Governance, Stewardship & Institutional Constitution</h1>
      <p class="mc-header__question">${gov.governing_principle}</p>
      <p class="mc-bar-note">${gov.purpose}</p>
      <p class="mc-bar-note">Extends <a href="/builds/002-project-constitution.md">Build #2 Project Constitution</a> · <a href="/mission-control/research-methodology.html">Research Methodology</a> · <a href="/mission-control/trust.html">Trust Framework</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Governance readiness</div><div class="mc-stat__value">${s.governance_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Values</div><div class="mc-stat__value">${s.values_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Stewards</div><div class="mc-stat__value">${s.stewards_assigned}/${s.stewards_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Public docs</div><div class="mc-stat__value">${s.public_docs_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Annual review</div><div class="mc-stat__value">${s.annual_review_live ? 'Live' : 'Planned'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Builds logged</div><div class="mc-stat__value">${s.builds_logged}</div></div>
    </div>
    <h2 class="mc-section-title">Mission Statement</h2>
    <p class="mc-bar-note">${gov.mission_statement}</p>
    <h2 class="mc-section-title">Institutional Values</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Value</th><th>Status</th><th>Implementation</th></tr></thead>
      <tbody>${valueRows}</tbody></table>
    <h2 class="mc-section-title">Institutional Responsibilities</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Responsibility</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${respRows}</tbody></table>
    <h2 class="mc-section-title">Steward Roles</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Steward</th><th>Scope</th><th>Assigned</th><th>Status</th></tr></thead>
      <tbody>${stewardRows}</tbody></table>
    <p class="mc-bar-note">${gov.governance_structure.note}</p>
    <h2 class="mc-section-title">Decision Categories</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Category</th><th>Scope</th><th>MC Logging</th></tr></thead>
      <tbody>${decRows}</tbody></table>
    <h2 class="mc-section-title">Correction Policy</h2>
    <p class="mc-bar-note">${corrFlow}</p>
    <p class="mc-bar-note">${gov.correction_policy.principle}</p>
    <p class="mc-bar-note">${gov.correction_policy.current}</p>
    <h2 class="mc-section-title">Public Accountability</h2>
    <table class="mc-table"><thead><tr><th>Document</th><th>Status</th><th>Link</th></tr></thead>
      <tbody>${pubRows}</tbody></table>
    <h2 class="mc-section-title">Community Participation</h2>
    <ul class="mc-deliverables">${gov.community_participation.channels.map(c => `<li>${c.channel} — ${c.status}${c.note ? ' (' + c.note + ')' : ''}</li>`).join('')}</ul>
    <p class="mc-bar-note">${gov.community_participation.review_gate}</p>
    <h2 class="mc-section-title">Institutional Memory</h2>
    <table class="mc-table"><thead><tr><th>Type</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${memRows}</tbody></table>
    <h2 class="mc-section-title">Annual Institutional Review</h2>
    <p class="mc-bar-note"><strong>${gov.annual_institutional_review.title}</strong> — ${gov.annual_institutional_review.frequency} · ${gov.annual_institutional_review.status}</p>
    <ul class="mc-deliverables">${gov.annual_institutional_review.dimensions.map(d => `<li>${d}</li>`).join('')}</ul>
    <p class="mc-bar-note">${gov.annual_institutional_review.note}</p>
    <h2 class="mc-section-title">Institutional Oath</h2>
    <blockquote class="mc-bar-note" style="border-left:3px solid var(--mc-accent);padding-left:1rem;font-style:italic">
      ${gov.institutional_oath.join('<br>')}
    </blockquote>
    <h2 class="mc-section-title">Governance Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${gov.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${gov.recommended_next_build.number} — ${gov.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${gov.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_GOVERNANCE_CONSTITUTION.md">MASTER_GOVERNANCE_CONSTITUTION.md</a> ·
      <a href="/data/governance-constitution.json">JSON</a> ·
      <a href="/mission-control/institutional-roadmap.html">Institutional Roadmap</a> ·
      <a href="/builds/002-project-constitution.md">Project Constitution</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initDataArchitecture() {
  const root = document.getElementById('mc-data-architecture-root');
  if (!root) return;

  const [daRes, mcRes] = await Promise.all([
    fetch('/data/data-architecture.json'),
    fetch('/data/mission-control.json')
  ]);
  const da = await daRes.json();
  const mc = await mcRes.json();
  const s = da.summary;
  const dom = da.canonical_domains;

  const domainRows = dom.domains.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.number}</td><td>${d.title}</td>
      <td><code>${d.id_field}</code></td><td>${d.status}</td><td>${d.records}</td>
      <td>${d.implementation}</td>
      <td>${d.route ? `<a href="${d.route}">registry</a>` : '—'}</td></tr>`).join('');

  const fieldRows = da.canonical_object_model.fields.map(f => `
    <tr><td><code>${f.field}</code></td><td>${f.title}</td><td>${f.required ? 'Yes' : 'No'}</td><td>${f.enforced}</td></tr>`).join('');

  const metaRows = da.metadata_standards.fields.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.field}</td><td>${m.status}</td></tr>`).join('');

  const verbRows = da.relationship_standards.verbs.map(v => `
    <tr><td><code>${v.verb}</code></td><td>${v.description}</td></tr>`).join('');

  const stateRows = da.publishing_states.states.map(st => `
    <tr><td>${st.state}</td><td>${st.order}</td><td>${st.mc_tracked}</td></tr>`).join('');

  const apiRows = da.api_philosophy.apis.map(a => `
    <tr><td><code>${a.id}</code></td><td>${a.name}</td><td>${a.status}</td></tr>`).join('');

  const metricRows = da.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const counts = da.mc_data_dashboard.current_counts;
  const extendLinks = da.extends.map(e =>
    `<a href="${e.route}">Build #${e.build} ${e.title}</a>`).join(' · ');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Data Architecture</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #51 · ${da.title}</p>
      <h1>Master Data Architecture & Canonical Data Dictionary</h1>
      <p class="mc-header__question">${da.governing_principle}</p>
      <p class="mc-bar-note">${da.purpose}</p>
      <p class="mc-bar-note">Extends ${extendLinks}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Data architecture readiness</div><div class="mc-stat__value">${s.data_architecture_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Domains</div><div class="mc-stat__value">${dom.domains_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Live / partial</div><div class="mc-stat__value">${dom.domains_live} / ${dom.domains_partial}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Knowledge published</div><div class="mc-stat__value">${counts.knowledge_published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Evidence records</div><div class="mc-stat__value">${counts.evidence_records}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Relationship edges</div><div class="mc-stat__value">${counts.relationship_edges}</div></div>
    </div>
    <h2 class="mc-section-title">Data Philosophy</h2>
    <p class="mc-bar-note"><strong>Wrong question:</strong> ${da.data_philosophy.wrong_question}</p>
    <p class="mc-bar-note"><strong>Right question:</strong> ${da.data_philosophy.right_question}</p>
    <ul class="mc-deliverables">${da.data_philosophy.rules.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Twelve Canonical Data Domains</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>#</th><th>Domain</th><th>ID Field</th><th>Status</th><th>Records</th><th>Implementation</th><th>Registry</th></tr></thead>
      <tbody>${domainRows}</tbody></table>
    <h2 class="mc-section-title">Canonical Object Model</h2>
    <p class="mc-bar-note">${da.canonical_object_model.note} · ${da.canonical_object_model.legacy_objects} legacy objects in Build #15 model.</p>
    <table class="mc-table"><thead><tr><th>Field</th><th>Title</th><th>Required</th><th>Enforced</th></tr></thead>
      <tbody>${fieldRows}</tbody></table>
    <h2 class="mc-section-title">Metadata Standards</h2>
    <p class="mc-bar-note">${da.metadata_standards.mc_dependency}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Field</th><th>Status</th></tr></thead>
      <tbody>${metaRows}</tbody></table>
    <h2 class="mc-section-title">Relationship Standards</h2>
    <p class="mc-bar-note">${da.relationship_standards.principle} · ${da.relationship_standards.legacy_types} legacy types · ${da.relationship_standards.edges_recorded} edges recorded</p>
    <table class="mc-table"><thead><tr><th>Verb</th><th>Description</th></tr></thead>
      <tbody>${verbRows}</tbody></table>
    <h2 class="mc-section-title">Versioning</h2>
    <p class="mc-bar-note">${da.versioning.chain.join(' → ')}</p>
    <p class="mc-bar-note">${da.versioning.current}</p>
    <h2 class="mc-section-title">Publishing States</h2>
    <p class="mc-bar-note">${da.publishing_states.flow}</p>
    <table class="mc-table"><thead><tr><th>State</th><th>Order</th><th>MC Tracked</th></tr></thead>
      <tbody>${stateRows}</tbody></table>
    <h2 class="mc-section-title">Search Index</h2>
    <p class="mc-bar-note">${da.search_index.status} — ${da.search_index.current}</p>
    <ul class="mc-deliverables">${da.search_index.indexed_fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">API Philosophy</h2>
    <p class="mc-bar-note">${da.api_philosophy.principle}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>API</th><th>Status</th></tr></thead>
      <tbody>${apiRows}</tbody></table>
    <h2 class="mc-section-title">Database Philosophy</h2>
    <p class="mc-bar-note">${da.database_philosophy.current}</p>
    <ul class="mc-deliverables">
      <li>Normalize: ${da.database_philosophy.normalize ? 'yes' : 'no'}</li>
      <li>Denormalize when: ${da.database_philosophy.denormalize_when}</li>
      <li>Referential integrity: ${da.database_philosophy.referential_integrity}</li>
      <li>Historical records: ${da.database_philosophy.historical_records}</li>
    </ul>
    <h2 class="mc-section-title">Institutional Data Health</h2>
    <table class="mc-table"><thead><tr><th>Metric</th><th>Count</th></tr></thead>
      <tbody>
        <tr><td>Knowledge assets published</td><td>${counts.knowledge_published}</td></tr>
        <tr><td>Evidence records</td><td>${counts.evidence_records}</td></tr>
        <tr><td>Counties indexed</td><td>${counts.counties_indexed}</td></tr>
        <tr><td>Organizations</td><td>${counts.organizations}</td></tr>
        <tr><td>Relationship edges</td><td>${counts.relationship_edges}</td></tr>
        <tr><td>Builds logged</td><td>${counts.builds_logged}</td></tr>
        <tr><td>Media assets</td><td>${counts.media_assets}</td></tr>
        <tr><td>Education Leaders</td><td>${counts.education_leaders}</td></tr>
      </tbody></table>
    <h2 class="mc-section-title">Future Expansion</h2>
    <ul class="mc-deliverables">${da.future_expansion.map(x => `<li>${x}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${da.long_term_vision}</p>
    <h2 class="mc-section-title">Data Architecture Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${da.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${da.recommended_next_build.number} — ${da.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${da.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_DATA_ARCHITECTURE.md">MASTER_DATA_ARCHITECTURE.md</a> ·
      <a href="/data/data-architecture.json">JSON</a> ·
      <a href="/mission-control/data-model.html">Canonical Data Model (#15)</a> ·
      <a href="/mission-control/database.html">Database Schema (#22)</a> ·
      <a href="/mission-control/knowledge-graph.html">Knowledge Graph</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initBuildBible() {
  const root = document.getElementById('mc-build-bible-root');
  if (!root) return;

  const [bbRes, mcRes] = await Promise.all([
    fetch('/data/build-bible.json'),
    fetch('/data/mission-control.json')
  ]);
  const bb = await bbRes.json();
  const mc = await mcRes.json();
  const s = bb.summary;
  const fnd = bb.phase_i_foundation;

  const fndRows = fnd.systems.map(sys => `
    <tr><td><code>${sys.id}</code></td><td>${sys.title}</td>
      <td>${sys.build ? '#' + sys.build : '—'}</td>
      <td>${sys.route ? `<a href="${sys.route}">link</a>` : '—'}</td>
      <td>${sys.status}</td></tr>`).join('');

  const pillarCards = bb.institutional_pillars.pillars.map(p => `
    <div class="mc-card"><h3>Pillar ${p.number}: ${p.title}</h3>
      <p class="mc-bar-note">${p.purpose}</p>
      <p class="mc-bar-note">${p.systems.join(' · ')}</p>
    </div>`).join('');

  const engineRows = bb.operating_engines.engines.map(e => `
    <tr><td>${e.title}</td><td>${e.components.join(', ')}</td><td>${e.readiness_pct}%</td></tr>`).join('');

  const wsRows = bb.workstreams.streams.map(w => `
    <tr><td><code>${w.id}</code></td><td>${w.title}</td><td>${w.focus}</td>
      <td>${w.readiness_pct}%</td><td>${w.status}</td></tr>`).join('');

  const phaseCards = bb.development_phases.phases.map(ph => `
    <div class="mc-card"><h3>Phase ${ph.letter} — ${ph.title}</h3>
      <p class="mc-bar-note">${ph.status} · ${ph.note || ''}</p>
      <ul class="mc-deliverables">${ph.items.map(i => `<li>${i}</li>`).join('')}</ul>
    </div>`).join('');

  const indexRows = bb.master_index.recent_builds.map(b => `
    <tr><td>#${b.build}</td><td>${b.title}</td><td><a href="${b.route}">${b.route}</a></td></tr>`).join('');

  const metricRows = bb.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const journey = bb.ultimate_visitor_journey.map((j, i) =>
    `${j}${i < bb.ultimate_visitor_journey.length - 1 ? ' →' : ''}`).join(' ');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Build Bible</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #50 · ★ MILESTONE · ${bb.title}</p>
      <h1>Master Build Bible</h1>
      <p class="mc-header__question">${bb.governing_principle}</p>
      <p class="mc-bar-note">${bb.purpose}</p>
      <p class="mc-bar-note"><strong>${bb.milestone.shift}</strong> — ${bb.milestone.planning_phase} planning · ${bb.milestone.implementation_phase} implementation</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Planning builds</div><div class="mc-stat__value">${s.planning_builds_complete}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Foundation systems</div><div class="mc-stat__value">${s.foundation_systems}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pillars</div><div class="mc-stat__value">${s.pillars_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Engine avg</div><div class="mc-stat__value">${s.avg_engine_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Launch readiness</div><div class="mc-stat__value">${s.public_launch_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Bible readiness</div><div class="mc-stat__value">${s.build_bible_readiness_pct}%</div></div>
    </div>
    <h2 class="mc-section-title">Phase I — Institutional Foundation (${fnd.systems_total} systems)</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>System</th><th>Build</th><th>Route</th><th>Status</th></tr></thead>
      <tbody>${fndRows}</tbody></table>
    <h2 class="mc-section-title">Twelve Institutional Pillars</h2>
    <div class="mc-grid-2">${pillarCards}</div>
    <h2 class="mc-section-title">Four Operating Engines</h2>
    <table class="mc-table"><thead><tr><th>Engine</th><th>Components</th><th>Readiness</th></tr></thead>
      <tbody>${engineRows}</tbody></table>
    <h2 class="mc-section-title">Permanent Workstreams</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Stream</th><th>Focus</th><th>Readiness</th><th>Status</th></tr></thead>
      <tbody>${wsRows}</tbody></table>
    <h2 class="mc-section-title">Implementation Phases (A–E)</h2>
    <div class="mc-grid-2">${phaseCards}</div>
    <h2 class="mc-section-title">Mission Control Responsibilities</h2>
    <ul class="mc-deliverables">${bb.mission_control_responsibilities.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Arkansas Focus</h2>
    <p class="mc-bar-note">${bb.arkansas_focus.question}</p>
    <h2 class="mc-section-title">Ultimate Visitor Journey</h2>
    <p class="mc-bar-note">${journey}</p>
    <h2 class="mc-section-title">What Comes Next — Implementation</h2>
    <ul class="mc-deliverables">${bb.what_comes_next.priorities.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${bb.long_term_vision.combines.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recent Blueprint Index</h2>
    <table class="mc-table"><thead><tr><th>Build</th><th>Blueprint</th><th>Registry</th></tr></thead>
      <tbody>${indexRows}</tbody></table>
    <p class="mc-bar-note"><a href="${bb.master_index.build_registry}">Full Build Registry →</a></p>
    <h2 class="mc-section-title">Build Bible Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${bb.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${bb.recommended_next_build.number} — ${bb.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${bb.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_BUILD_BIBLE.md">MASTER_BUILD_BIBLE.md</a> ·
      <a href="/data/build-bible.json">JSON</a> ·
      <a href="/BUILD_PLAN.md">Build Plan</a> ·
      <a href="/mission-control/systems-integration.html">Systems Integration</a> ·
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
  initKnowledgeAtlasBlueprint();
  initPlatformArchitectureBlueprint();
  initRepositoryBlueprint();
  initDatabaseSchemaBlueprint();
  initWireframeBlueprint();
  initContactIntelligenceBlueprint();
  initExecutiveCommandCenter();
  initAiKnowledgeEngine();
  initContentProductionFactory();
  initEducationAcademy();
  initResearchObservatory();
  initOutreachEngine();
  initCountyOperatingSystem();
  initEducationalCampaignOperatingSystem();
  initEncyclopediaKnowledgeLibrary();
  initNarrativeArchitecture();
  initMasterCurriculum();
  initTrustFramework();
  initMasterResearchLibrary();
  initLearningLaboratory();
  initMediaStudio();
  initCivicIntelligence();
  initEvidenceLedger();
  initCivicActionLab();
  initResearchMethodology();
  initInstitutionalRoadmap();
  initSystemsIntegration();
  initContentProductionMatrix();
  initVisitorJourney();
  initTechnicalArchitecture();
  initGovernanceConstitution();
  initBuildBible();
  initDataArchitecture();
  initUxArchitecture();
  initLaunchStrategy();
  initPmo();
  initMasterPlan();
  initStatewideGrowth();
  initNeighborhoodOrganizing();
  initCivicAtlas();
  initRelationshipOs();
  initInstitutionalAi();
  initCoalitionNetwork();
  initCitizenActionCenter();
  initCampaignFinanceObservatory();
  initArkansasActionNetwork();
  initCivicIntelligenceCommandCenter();
  initSustainabilityStewardship();
  initImpactMeasurement();
  initCitizenLeadershipAcademy();
  initRelationalOrganizingGrowthEngine();
  initArkansasCommandStrategy();
  initArkansasCommunityListening();
  initArkansasCommunications();
  initArkansasResearchInstitute();
  initArkansasCivicInnovationReform();
  initVolunteerFundingConstitution();
  initOrganizationalConstitution();
  initArkansasCountyOperatingSystem();
  initArkansasCityOperatingSystem();
  initArkansasNeighborhoodOperatingSystem();
  initArkansasCivicInstitutionRoadmap();
  initInstitutionalDigitalTwin();
  initPublicTrustInstitutionalCredibility();
  initArkansasCivicEcosystem();
  initArkansasStrategicPlan2035();
});

async function initUxArchitecture() {
  const root = document.getElementById('mc-ux-architecture-root');
  if (!root) return;

  const [uxRes, mcRes] = await Promise.all([
    fetch('/data/ux-architecture.json'),
    fetch('/data/mission-control.json')
  ]);
  const ux = await uxRes.json();
  const mc = await mcRes.json();
  const s = ux.summary;

  const emotionRows = ux.emotional_journey.stages.map(st => `
    <tr><td>${st.order}</td><td><code>${st.id}</code></td><td>${st.emotion}</td>
      <td><em>${st.visitor_thought}</em></td><td>${st.status}</td><td>${st.implementation}</td></tr>`).join('');

  const goalRows = ux.first_time_visitor.goals.map(g => `
    <tr><td>${g.goal}</td><td>${g.status}</td><td>${g.route ? `<a href="${g.route}">${g.route}</a>` : '—'}</td></tr>`).join('');

  const navRows = ux.navigation_philosophy.nav_intents.map(n => `
    <tr><td>${n.label}</td><td>${n.intent}</td><td>${n.status}</td>
      <td>${n.route ? `<a href="${n.route}">${n.route}</a>` : '—'}</td><td>${n.note || ''}</td></tr>`).join('');

  const layerRows = ux.progressive_disclosure.layers.map(l => `
    <tr><td>${l.level}</td><td>${l.title}</td><td>${l.status}</td></tr>`).join('');

  const compassRows = ux.learning_compass.questions.map(q => `
    <tr><td>${q.question}</td><td>${q.status}</td><td>${q.current}</td></tr>`).join('');

  const civicRows = ux.civic_compass.actions.map(a => `
    <tr><td>${a.title}</td><td>${a.status}</td><td>${a.route ? `<a href="${a.route}">${a.route}</a>` : '—'}</td><td>${a.note || ''}</td></tr>`).join('');

  const hubRows = ux.floating_action_hub.items.map(i => `
    <tr><td>${i.title}</td><td>${i.status}</td><td>${i.note || ''}</td></tr>`).join('');

  const trustRows = ux.trust_signals.signals.map(t => `
    <tr><td>${t.signal}</td><td>${t.status}</td><td>${t.pages_with || ''}</td></tr>`).join('');

  const delightRows = ux.delight_moments.moments.map(d => `
    <tr><td>${d.moment}</td><td>${d.status}</td></tr>`).join('');

  const metricRows = ux.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const extendLinks = ux.extends.map(e =>
    `<a href="${e.route}">Build #${e.build} ${e.title}</a>`).join(' · ');

  const personality = ux.institutional_personality.join(' · ');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → UX Architecture</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #52 · ${ux.title}</p>
      <h1>Master User Experience Architecture</h1>
      <p class="mc-header__question">${ux.governing_principle}</p>
      <p class="mc-bar-note">${ux.purpose}</p>
      <p class="mc-bar-note">Extends ${extendLinks}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">UX readiness</div><div class="mc-stat__value">${s.ux_architecture_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Emotional stages</div><div class="mc-stat__value">${s.emotional_stages}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Action hub live</div><div class="mc-stat__value">${s.action_hub_live_items}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Search</div><div class="mc-stat__value">${s.search_live ? 'Live' : 'Planned'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Delight moments</div><div class="mc-stat__value">${s.delight_moments_live}/7</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Education Leaders</div><div class="mc-stat__value">${s.education_leaders}</div></div>
    </div>
    <h2 class="mc-section-title">Experience Philosophy</h2>
    <p class="mc-bar-note"><strong>Metaphor:</strong> ${ux.experience_philosophy.metaphor}</p>
    <ul class="mc-deliverables">${ux.experience_philosophy.qualities.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Emotional Journey</h2>
    <p class="mc-bar-note">${ux.emotional_journey.note}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Stage</th><th>Visitor thought</th><th>Status</th><th>Implementation</th></tr></thead>
      <tbody>${emotionRows}</tbody></table>
    <h2 class="mc-section-title">First-Time Visitor (30 seconds)</h2>
    <table class="mc-table"><thead><tr><th>Goal</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${goalRows}</tbody></table>
    <h2 class="mc-section-title">Navigation Philosophy</h2>
    <p class="mc-bar-note">${ux.navigation_philosophy.principle}</p>
    <table class="mc-table"><thead><tr><th>Label</th><th>Intent</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${navRows}</tbody></table>
    <h2 class="mc-section-title">Progressive Disclosure</h2>
    <p class="mc-bar-note">${ux.progressive_disclosure.principle} · Depth toggle: ${ux.progressive_disclosure.depth_toggle_live}</p>
    <table class="mc-table"><thead><tr><th>Level</th><th>Layer</th><th>Status</th></tr></thead>
      <tbody>${layerRows}</tbody></table>
    <h2 class="mc-section-title">Learning Compass</h2>
    <p class="mc-bar-note">${ux.learning_compass.component_id} — ${ux.learning_compass.status} · ${ux.learning_compass.schema_fields} schema fields</p>
    <table class="mc-table"><thead><tr><th>Question</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${compassRows}</tbody></table>
    <h2 class="mc-section-title">Civic Compass</h2>
    <p class="mc-bar-note">${ux.civic_compass.principle} · ${ux.civic_compass.implementation}</p>
    <table class="mc-table"><thead><tr><th>Action</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${civicRows}</tbody></table>
    <h2 class="mc-section-title">Floating Action Hub</h2>
    <p class="mc-bar-note">${ux.floating_action_hub.version} — ${ux.floating_action_hub.status} · ${ux.floating_action_hub.pages_with_hub}</p>
    <table class="mc-table"><thead><tr><th>Item</th><th>Status</th><th>Note</th></tr></thead>
      <tbody>${hubRows}</tbody></table>
    <h2 class="mc-section-title">Reading Experience</h2>
    <ul class="mc-deliverables">${ux.reading_experience.principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <p class="mc-bar-note">${ux.reading_experience.current}</p>
    <h2 class="mc-section-title">Visual Identity</h2>
    <p class="mc-bar-note"><strong>Communicate:</strong> ${ux.visual_identity.communicate.join(', ')}</p>
    <p class="mc-bar-note"><strong>Never feel like:</strong> ${ux.visual_identity.never_feel_like.join(', ')}</p>
    <p class="mc-bar-note"><strong>Target:</strong> ${ux.visual_identity.target_feel} — ${ux.visual_identity.current}</p>
    <h2 class="mc-section-title">Trust Signals</h2>
    <p class="mc-bar-note">${ux.trust_signals.principle}</p>
    <table class="mc-table"><thead><tr><th>Signal</th><th>Status</th><th>Pages</th></tr></thead>
      <tbody>${trustRows}</tbody></table>
    <h2 class="mc-section-title">Search Experience</h2>
    <p class="mc-bar-note">${ux.search_experience.status} — ${ux.search_experience.current}</p>
    <ul class="mc-deliverables">${ux.search_experience.fallbacks.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Mobile Experience</h2>
    <p class="mc-bar-note">${ux.mobile_experience.status} — ${ux.mobile_experience.current}</p>
    <h2 class="mc-section-title">Accessibility</h2>
    <p class="mc-bar-note">${ux.accessibility_experience.status} — ${ux.accessibility_experience.current}</p>
    <h2 class="mc-section-title">Community Experience</h2>
    <p class="mc-bar-note">${ux.community_experience.status} — ${ux.community_experience.current}</p>
    <h2 class="mc-section-title">Mission Control Experience</h2>
    <p class="mc-bar-note">${ux.mission_control_experience.principle} — ${ux.mission_control_experience.builds_logged} builds logged</p>
    <h2 class="mc-section-title">Delight Moments</h2>
    <p class="mc-bar-note">${ux.delight_moments.principle}</p>
    <table class="mc-table"><thead><tr><th>Moment</th><th>Status</th></tr></thead>
      <tbody>${delightRows}</tbody></table>
    <h2 class="mc-section-title">Institutional Personality</h2>
    <p class="mc-bar-note">${personality}</p>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${ux.long_term_vision.visitor_quotes.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">UX Architecture Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ux.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ux.recommended_next_build.number} — ${ux.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ux.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_UX_ARCHITECTURE.md">MASTER_UX_ARCHITECTURE.md</a> ·
      <a href="/data/ux-architecture.json">JSON</a> ·
      <a href="/mission-control/visitor-journey.html">Visitor Journey (#47)</a> ·
      <a href="/mission-control/journey.html">Citizen Journey (#8)</a> ·
      <a href="/mission-control/atlas.html">Knowledge Atlas</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initLaunchStrategy() {
  const root = document.getElementById('mc-launch-strategy-root');
  if (!root) return;

  const [lsRes, mcRes] = await Promise.all([
    fetch('/data/launch-strategy.json'),
    fetch('/data/mission-control.json')
  ]);
  const ls = await lsRes.json();
  const mc = await mcRes.json();
  const s = ls.summary;
  const phases = ls.launch_phases;

  const phaseRows = phases.phases.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.number}</td><td>${p.title}</td><td>${p.status}</td>
      <td>${p.readiness_pct}%</td><td>${p.public_visibility}</td><td>${p.note}</td></tr>`).join('');

  const chkRows = ls.readiness_checklist.items.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.item}</td><td>${c.status}</td><td>${c.current}</td></tr>`).join('');

  const metricRows = ls.launch_metrics.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.status}</td><td>${m.tracking}</td></tr>`).join('');

  const lccRows = ls.launch_command_center.readiness_dimensions.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.dimension}</td><td>${d.pct}%</td><td>${d.status}</td></tr>`).join('');

  const feedbackRows = ls.feedback_architecture.categories.map(f => `
    <tr><td>${f.category}</td><td>${f.status}</td></tr>`).join('');

  const mcMetricRows = ls.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const extendLinks = ls.extends.map(e =>
    `<a href="${e.route}">Build #${e.build} ${e.title}</a>`).join(' · ');

  const launchRec = ls.readiness_checklist.public_launch_recommended
    ? 'Yes — checklist gate cleared'
    : `No — ${s.public_launch_readiness_pct}% public launch readiness`;

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Launch Strategy</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #53 · ${ls.title}</p>
      <h1>Master Launch Strategy & Arkansas Rollout Blueprint</h1>
      <p class="mc-header__question">${ls.governing_principle}</p>
      <p class="mc-bar-note">${ls.purpose}</p>
      <p class="mc-bar-note">Extends ${extendLinks}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Launch strategy readiness</div><div class="mc-stat__value">${s.launch_strategy_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Current phase</div><div class="mc-stat__value">Phase ${phases.current_phase}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Public launch readiness</div><div class="mc-stat__value">${s.public_launch_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Checklist score</div><div class="mc-stat__value">${s.checklist_score_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Launch recommended</div><div class="mc-stat__value">${s.public_launch_recommended ? 'Yes' : 'No'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Education Leaders</div><div class="mc-stat__value">${s.education_leaders}</div></div>
    </div>
    <h2 class="mc-section-title">Launch Philosophy</h2>
    <p class="mc-bar-note"><strong>Wrong question:</strong> ${ls.launch_philosophy.wrong_question}</p>
    <p class="mc-bar-note"><strong>Right question:</strong> ${ls.launch_philosophy.right_question}</p>
    <p class="mc-bar-note">${ls.launch_philosophy.tone}</p>
    <h2 class="mc-section-title">Six Launch Phases</h2>
    <p class="mc-bar-note"><strong>Current:</strong> Phase ${phases.current_phase} — ${phases.current_phase_title}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>#</th><th>Phase</th><th>Status</th><th>Readiness</th><th>Visibility</th><th>Note</th></tr></thead>
      <tbody>${phaseRows}</tbody></table>
    <h2 class="mc-section-title">Launch Readiness Checklist</h2>
    <p class="mc-bar-note">${ls.readiness_checklist.principle} · Public launch recommended: <strong>${launchRec}</strong></p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Requirement</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${chkRows}</tbody></table>
    <h2 class="mc-section-title">Launch Metrics (Educational)</h2>
    <p class="mc-bar-note">${ls.launch_metrics.principle}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Tracking</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Communication Strategy</h2>
    <p class="mc-bar-note"><strong>Pillars:</strong> ${ls.communication_strategy.pillars.join(' · ')}</p>
    <p class="mc-bar-note">${ls.communication_strategy.framing} — ${ls.communication_strategy.current}</p>
    <h2 class="mc-section-title">Feedback Architecture</h2>
    <p class="mc-bar-note">${ls.feedback_architecture.principle} · ${ls.feedback_architecture.phase_1_dashboard}</p>
    <table class="mc-table"><thead><tr><th>Category</th><th>Status</th></tr></thead>
      <tbody>${feedbackRows}</tbody></table>
    <h2 class="mc-section-title">Arkansas Growth Strategy</h2>
    <p class="mc-bar-note">${ls.arkansas_growth_strategy.strategy} — ${ls.arkansas_growth_strategy.counties_with_participation}/${ls.arkansas_growth_strategy.counties_total} counties with participation</p>
    <ul class="mc-deliverables">${ls.arkansas_growth_strategy.priorities.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Annual Relaunch</h2>
    <p class="mc-bar-note">${ls.annual_relaunch.title} — ${ls.annual_relaunch.status}</p>
    <ul class="mc-deliverables">${ls.annual_relaunch.activities.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Success Definition</h2>
    <ul class="mc-deliverables">${ls.success_definition.criteria.map(c => `<li>${c}</li>`).join('')}</ul>
    <p class="mc-bar-note">${ls.success_definition.measure}</p>
    <h2 class="mc-section-title">Launch Command Center</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Dimension</th><th>Readiness</th><th>Status</th></tr></thead>
      <tbody>${lccRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${ls.long_term_vision}</p>
    <h2 class="mc-section-title">Launch Metrics (Mission Control)</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${mcMetricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ls.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ls.recommended_next_build.number} — ${ls.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ls.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_LAUNCH_STRATEGY.md">MASTER_LAUNCH_STRATEGY.md</a> ·
      <a href="/data/launch-strategy.json">JSON</a> ·
      <a href="/mission-control/institutional-roadmap.html">Institutional Roadmap</a> ·
      <a href="/mission-control/outreach.html">Outreach Engine</a> ·
      <a href="/mission-control/county-os.html">County OS</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initPmo() {
  const root = document.getElementById('mc-pmo-root');
  if (!root) return;

  const [pmoRes, mcRes] = await Promise.all([
    fetch('/data/pmo.json'),
    fetch('/data/mission-control.json')
  ]);
  const pmo = await pmoRes.json();
  const mc = await mcRes.json();
  const s = pmo.summary;
  const depts = pmo.departments;

  const deptRows = depts.departments.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.number}</td><td>${d.title}</td>
      <td>${d.readiness_pct}%</td><td>${d.status}</td><td>${d.primary_dashboard}</td>
      <td>${d.owner_assigned ? 'Yes' : 'No'}</td>
      <td>${d.route ? `<a href="${d.route}">dashboard</a>` : '—'}</td>
      <td>${d.note}</td></tr>`).join('');

  const questionRows = pmo.pmo_mission.daily_questions.map(q => `
    <tr><td>${q.q}</td><td>${q.status}</td><td>${q.source}</td></tr>`).join('');

  const workflowRows = pmo.pmo_workflow.stages.map(w => `
    <tr><td>${w.order}</td><td>${w.title}</td><td>${w.mc_tracked}</td></tr>`).join('');

  const fieldRows = pmo.work_item_structure.fields.map(f => `
    <tr><td><code>${f.field}</code></td><td>${f.required ? 'Yes' : 'No'}</td><td>${f.enforced}</td></tr>`).join('');

  const riskRows = pmo.risk_register.risks.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.risk}</td><td>${r.likelihood}</td><td>${r.impact}</td>
      <td>${r.status}</td><td>${r.mitigation}</td></tr>`).join('');

  const depRows = pmo.dependency_management.chains.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.from}</td><td>→</td><td>${d.to}</td><td>${d.status}</td></tr>`).join('');

  const resourceRows = pmo.resource_allocation.areas.map(a => `
    <tr><td>${a.area}</td><td>${a.effort_pct}%</td><td>${a.readiness_pct}%</td><td>${a.bottleneck}</td></tr>`).join('');

  const widgetRows = pmo.pmo_dashboard.widgets.map(w => `
    <tr><td><code>${w.id}</code></td><td>${w.widget}</td><td>${w.status}</td><td>${w.source}</td></tr>`).join('');

  const metricRows = pmo.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  const extendLinks = pmo.extends.map(e =>
    `<a href="${e.route}">Build #${e.build} ${e.title}</a>`).join(' · ');

  const briefing = pmo.executive_weekly_review.current_briefing || {};

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → PMO</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #54 · ${pmo.title}</p>
      <h1>Master Project Management Office</h1>
      <p class="mc-header__question">${pmo.governing_principle}</p>
      <p class="mc-bar-note">${pmo.purpose}</p>
      <p class="mc-bar-note">Extends ${extendLinks}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">PMO readiness</div><div class="mc-stat__value">${s.pmo_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Departments</div><div class="mc-stat__value">${depts.departments_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg dept readiness</div><div class="mc-stat__value">${s.avg_department_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Owners assigned</div><div class="mc-stat__value">${s.owners_assigned}/10</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Open risks</div><div class="mc-stat__value">${s.risks_open}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Work items</div><div class="mc-stat__value">${s.work_items_logged}</div></div>
    </div>
    <h2 class="mc-section-title">Daily Five Questions</h2>
    <p class="mc-bar-note">${s.daily_questions_live}/5 answerable instantly in Mission Control</p>
    <table class="mc-table"><thead><tr><th>Question</th><th>Status</th><th>Source</th></tr></thead>
      <tbody>${questionRows}</tbody></table>
    <h2 class="mc-section-title">Ten PMO Departments</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>#</th><th>Department</th><th>Readiness</th><th>Status</th><th>Dashboard</th><th>Owner</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${deptRows}</tbody></table>
    <h2 class="mc-section-title">PMO Workflow</h2>
    <p class="mc-bar-note">${pmo.pmo_workflow.flow}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>Stage</th><th>MC Tracked</th></tr></thead>
      <tbody>${workflowRows}</tbody></table>
    <h2 class="mc-section-title">Work Item Structure</h2>
    <p class="mc-bar-note">${pmo.work_item_structure.current}</p>
    <table class="mc-table"><thead><tr><th>Field</th><th>Required</th><th>Enforced</th></tr></thead>
      <tbody>${fieldRows}</tbody></table>
    <h2 class="mc-section-title">Executive Weekly Review</h2>
    <p class="mc-bar-note">${pmo.executive_weekly_review.frequency} — ${pmo.executive_weekly_review.status} · ${pmo.executive_weekly_review.note}</p>
    <p class="mc-bar-note"><strong>What built:</strong> ${briefing.what_built || '—'}</p>
    <p class="mc-bar-note"><strong>Building now:</strong> ${briefing.building_now || '—'}</p>
    <p class="mc-bar-note"><strong>Blocked:</strong> ${(briefing.blocked || []).join(' · ')}</p>
    <p class="mc-bar-note"><strong>Next:</strong> ${briefing.next || '—'}</p>
    <h2 class="mc-section-title">Monthly Institutional Review</h2>
    <p class="mc-bar-note">${pmo.monthly_institutional_review.title} — ${pmo.monthly_institutional_review.status}</p>
    <ul class="mc-deliverables">${pmo.monthly_institutional_review.dimensions.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Risk Register</h2>
    <p class="mc-bar-note">${s.risks_open} open / ${s.risks_total} documented</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Risk</th><th>Likelihood</th><th>Impact</th><th>Status</th><th>Mitigation</th></tr></thead>
      <tbody>${riskRows}</tbody></table>
    <h2 class="mc-section-title">Dependency Management</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>From</th><th></th><th>To</th><th>Status</th></tr></thead>
      <tbody>${depRows}</tbody></table>
    <h2 class="mc-section-title">Resource Allocation</h2>
    <table class="mc-table"><thead><tr><th>Area</th><th>Effort</th><th>Readiness</th><th>Bottleneck</th></tr></thead>
      <tbody>${resourceRows}</tbody></table>
    <h2 class="mc-section-title">Institutional Calendar</h2>
    <p class="mc-bar-note">${pmo.institutional_calendar.status} — ${pmo.institutional_calendar.current}</p>
    <h2 class="mc-section-title">PMO Dashboard Widgets</h2>
    <p class="mc-bar-note">${s.pmo_widgets_live}/${pmo.pmo_dashboard.widgets.length} widgets live</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Widget</th><th>Status</th><th>Source</th></tr></thead>
      <tbody>${widgetRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${pmo.long_term_vision}</p>
    <h2 class="mc-section-title">PMO Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${pmo.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${pmo.recommended_next_build.number} — ${pmo.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${pmo.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_PMO.md">MASTER_PMO.md</a> ·
      <a href="/data/pmo.json">JSON</a> ·
      <a href="/mission-control/executive.html">Executive Office</a> ·
      <a href="/mission-control/build-bible.html">Build Bible</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initMasterPlan() {
  const root = document.getElementById('mc-master-plan-root');
  if (!root) return;

  const [mpRes, mcRes] = await Promise.all([
    fetch('/data/master-plan.json'),
    fetch('/data/mission-control.json')
  ]);
  const mp = await mpRes.json();
  const mc = await mcRes.json();
  const s = mp.summary;

  const pillarRows = mp.twelve_pillars.pillars.map(p => `
    <tr><td>${p.number}</td><td><code>${p.id}</code></td><td>${p.title}</td>
      <td><a href="${p.route}">→</a></td></tr>`).join('');

  const engineRows = mp.four_engines.engines.map(e => `
    <tr><td><code>${e.id}</code></td><td>${e.title}</td><td>${e.readiness_pct}%</td>
      <td>${e.components.join(', ')}</td></tr>`).join('');

  const journeyRows = mp.visitor_journey.stages.map(j => `
    <tr><td>${j.stage}</td><td>${j.title}</td><td>${j.status}</td></tr>`).join('');

  const levelRows = mp.educational_philosophy.levels.map(l => `
    <tr><td>L${l.level}</td><td>${l.title}</td><td>${l.status}</td></tr>`).join('');

  const modelRows = mp.institutional_model.facets.map(f => `
    <tr><td>${f.facet}</td><td>${f.status}</td><td>${f.route ? `<a href="${f.route}">→</a>` : '—'}</td></tr>`).join('');

  const growthRows = mp.institutional_growth.dimensions.map(g => `
    <tr><td>${g.dimension}</td><td>${g.focus}</td><td>${g.readiness_pct}%</td></tr>`).join('');

  const successRows = mp.success_five_year.goals.map(g => `
    <tr><td>${g.goal}</td><td>${g.status}</td><td>${g.current}</td></tr>`).join('');

  const implRows = mp.next_major_phase.workstreams.map(w => `
    <tr><td><code>${w.id}</code></td><td>${w.workstream}</td><td>${w.status}</td>
      <td>${w.route ? `<a href="${w.route}">→</a>` : '—'}</td></tr>`).join('');

  const docRows = mp.constitution_index.documents.map(d => `
    <tr><td>#${d.build}</td><td>${d.title}</td><td>${d.role}</td><td>${d.status}</td>
      <td><a href="${d.route}">doc</a></td></tr>`).join('');

  const metricRows = mp.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.status}</td><td>${m.current}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Master Plan ★</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #55 · ${mp.title} · ★ MILESTONE</p>
      <h1>Master Master Plan</h1>
      <p class="mc-header__question">${mp.governing_principle}</p>
      <p class="mc-bar-note">${mp.purpose}</p>
      <p class="mc-bar-note"><strong>Motto:</strong> <em>${mp.institutional_motto}</em></p>
      <p class="mc-bar-note">${mp.milestone.note}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Master plan readiness</div><div class="mc-stat__value">${s.master_plan_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Planning builds</div><div class="mc-stat__value">${s.planning_builds_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg engine readiness</div><div class="mc-stat__value">${s.avg_engine_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Constitution docs</div><div class="mc-stat__value">${s.constitution_docs}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Public launch</div><div class="mc-stat__value">${s.public_launch_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">5-year goals</div><div class="mc-stat__value">${s.five_year_goals_achieved}/7</div></div>
    </div>
    <h2 class="mc-section-title">The Why</h2>
    <p class="mc-bar-note">${mp.the_why.context}</p>
    <ul class="mc-deliverables">${mp.the_why.gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <p class="mc-bar-note"><strong>Arkansas:</strong> ${mp.the_why.arkansas_purpose}</p>
    <h2 class="mc-section-title">Mission & Vision</h2>
    <p class="mc-bar-note"><strong>Mission:</strong> ${mp.mission}</p>
    <p class="mc-bar-note">${mp.mission_rule}</p>
    <p class="mc-bar-note"><strong>Vision:</strong> ${mp.vision.capabilities.join(' · ')}</p>
    <p class="mc-bar-note">${mp.vision.outcome}</p>
    <h2 class="mc-section-title">Arkansas Model</h2>
    <p class="mc-bar-note">${mp.arkansas_model.principle}</p>
    <p class="mc-bar-note"><strong>Every feature asks:</strong> ${mp.arkansas_model.question}</p>
    <h2 class="mc-section-title">Institutional Model (10 Facets)</h2>
    <table class="mc-table"><thead><tr><th>Facet</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${modelRows}</tbody></table>
    <h2 class="mc-section-title">Twelve Pillars</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Pillar</th><th>Route</th></tr></thead>
      <tbody>${pillarRows}</tbody></table>
    <h2 class="mc-section-title">Four Operating Engines</h2>
    <p class="mc-bar-note">Average readiness: ${mp.four_engines.avg_readiness_pct}%</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Engine</th><th>Readiness</th><th>Components</th></tr></thead>
      <tbody>${engineRows}</tbody></table>
    <h2 class="mc-section-title">Visitor Journey</h2>
    <p class="mc-bar-note">${mp.visitor_journey.flow}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${journeyRows}</tbody></table>
    <h2 class="mc-section-title">Educational Philosophy (5 Layers)</h2>
    <table class="mc-table"><thead><tr><th>Level</th><th>Layer</th><th>Status</th></tr></thead>
      <tbody>${levelRows}</tbody></table>
    <h2 class="mc-section-title">Philosophies</h2>
    <p class="mc-bar-note"><strong>Trust:</strong> ${mp.philosophies.trust.join(' · ')}</p>
    <p class="mc-bar-note"><strong>Technology:</strong> ${mp.philosophies.technology.join(' · ')}</p>
    <p class="mc-bar-note"><strong>Research:</strong> ${mp.philosophies.research.join(' · ')}</p>
    <p class="mc-bar-note"><strong>Community:</strong> ${mp.philosophies.community.join(' · ')}</p>
    <h2 class="mc-section-title">Knowledge Graph</h2>
    <p class="mc-bar-note">${mp.knowledge_graph.principle} — ${s.knowledge_graph_nodes}/${mp.knowledge_graph.nodes_target} nodes</p>
    <p class="mc-bar-note">${mp.knowledge_graph.entity_types.join(' · ')}</p>
    <h2 class="mc-section-title">Institutional Growth</h2>
    <table class="mc-table"><thead><tr><th>Dimension</th><th>Focus</th><th>Readiness</th></tr></thead>
      <tbody>${growthRows}</tbody></table>
    <h2 class="mc-section-title">Five-Year Success</h2>
    <table class="mc-table"><thead><tr><th>Goal</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${successRows}</tbody></table>
    <h2 class="mc-section-title">Next Major Phase — Execution</h2>
    <p class="mc-bar-note">${mp.next_major_phase.planning_status} — ${mp.next_major_phase.dominant_activities.join(' + ')}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Workstream</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${implRows}</tbody></table>
    <h2 class="mc-section-title">Institutional Promise</h2>
    <ul class="mc-deliverables">${mp.institutional_promise.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Constitution Index — Read Order</h2>
    <p class="mc-bar-note"><strong>Read first:</strong> <a href="${mp.constitution_index.read_first}">MASTER_MASTER_PLAN.md</a></p>
    <table class="mc-table"><thead><tr><th>Build</th><th>Document</th><th>Role</th><th>Status</th><th>Link</th></tr></thead>
      <tbody>${docRows}</tbody></table>
    <h2 class="mc-section-title">Master Plan Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Status</th><th>Current</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${mp.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${mp.recommended_next_build.number} — ${mp.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${mp.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_MASTER_PLAN.md">MASTER_MASTER_PLAN.md</a> ·
      <a href="/data/master-plan.json">JSON</a> ·
      <a href="/mission-control/build-bible.html">Build Bible (#50)</a> ·
      <a href="/mission-control/pmo.html">PMO (#54)</a> ·
      <a href="/mission-control/launch-strategy.html">Launch Strategy</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initStatewideGrowth() {
  const root = document.getElementById('mc-statewide-growth-root');
  if (!root) return;

  const [sgRes, mcRes, citiesRes] = await Promise.all([
    fetch('/data/statewide-growth.json'),
    fetch('/data/mission-control.json'),
    fetch('/data/arkansas-cities.json')
  ]);
  const sg = await sgRes.json();
  const mc = await mcRes.json();
  const citiesData = await citiesRes.json();
  const s = sg.summary;

  const objRows = sg.statewide_objectives.map(o => `
    <tr><td>${o.number}</td><td><code>${o.id}</code></td><td>${o.title}</td>
      <td>${o.progress_pct}%</td><td>${o.status}</td></tr>`).join('');

  const ladderRows = sg.leadership_ladder.stages.map(st => `
    <tr><td>${st.stage}</td><td><code>${st.id}</code></td><td>${st.title}</td><td>${st.status}</td></tr>`).join('');

  const benchRows = sg.community_benchmarks.map(b => `
    <tr><td><code>${b.id}</code></td><td>${b.benchmark}</td><td>${b.current}</td>
      <td>${b.target}</td><td>${b.status}</td></tr>`).join('');

  const channelRows = sg.recruitment_channels.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.channel}</td><td>${c.status}</td>
      <td>${c.route ? `<a href="${c.route}">→</a>` : '—'}</td></tr>`).join('');

  const indicatorRows = sg.success_indicators.map(i => `
    <tr><td><code>${i.id}</code></td><td>${i.indicator}</td><td>${i.current}</td>
      <td>${i.target ?? '—'}</td><td>${i.status}</td></tr>`).join('');

  const geoRows = sg.geographic_dashboards.map(g => `
    <tr><td><code>${g.id}</code></td><td>${g.title}</td><td>${g.metrics.join(', ')}</td><td>${g.status}</td></tr>`).join('');

  const metricRows = sg.mc_integration.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.current}</td>
      <td>${m.target ?? '—'}</td><td>${m.status}</td></tr>`).join('');

  const topCities = citiesData.cities.slice(0, 15).map(c => `
    <tr><td>${c.rank}</td><td>${c.name}</td><td>${c.population_estimate.toLocaleString()}</td>
      <td>${c.education_leaders}</td><td>${c.status}</td></tr>`).join('');

  const obj1 = sg.statewide_objectives[0].current;

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Statewide Growth</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #56 · ${sg.title}</p>
      <h1>Arkansas Civic Education Network</h1>
      <p class="mc-header__question">${sg.governing_principle}</p>
      <p class="mc-bar-note">${sg.purpose}</p>
      <p class="mc-bar-note"><strong>Vision:</strong> ${sg.arkansas_vision}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Growth readiness</div><div class="mc-stat__value">${s.statewide_growth_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties w/ leaders</div><div class="mc-stat__value">${s.counties_with_leaders}/${s.counties_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Cities w/ leaders</div><div class="mc-stat__value">${s.cities_with_leaders}/${s.cities_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Participants</div><div class="mc-stat__value">${s.participants_current.toLocaleString()}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Target</div><div class="mc-stat__value">${(s.participants_target / 1000).toFixed(0)}K</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Benchmarks met</div><div class="mc-stat__value">${s.benchmarks_met}/${s.benchmarks_total}</div></div>
    </div>
    <h2 class="mc-section-title">Three Statewide Objectives</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Objective</th><th>Progress</th><th>Status</th></tr></thead>
      <tbody>${objRows}</tbody></table>
    <h2 class="mc-section-title">Objective One — County Coverage Tiers</h2>
    <div class="mc-executive">
      <div class="mc-stat"><div class="mc-stat__label">No leaders</div><div class="mc-stat__value">${obj1.no_leaders}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">One leader</div><div class="mc-stat__value">${obj1.one_leader}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Meeting target (3–5)</div><div class="mc-stat__value">${obj1.meeting_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Exceeding (10+)</div><div class="mc-stat__value">${obj1.exceeding_target}</div></div>
    </div>
    <h2 class="mc-section-title">Leadership Ladder</h2>
    <p class="mc-bar-note">${sg.leadership_ladder.flow}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${ladderRows}</tbody></table>
    <h2 class="mc-section-title">Neighborhood Network</h2>
    <p class="mc-bar-note">${sg.neighborhood_network.principle} · Privacy-first: ${sg.neighborhood_network.privacy_first ? 'yes' : 'no'}</p>
    <ul class="mc-deliverables">${sg.neighborhood_network.participation_types.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Geographic Coverage Dashboards</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Dashboard</th><th>Metrics</th><th>Status</th></tr></thead>
      <tbody>${geoRows}</tbody></table>
    <h2 class="mc-section-title">Community Benchmarks</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Benchmark</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${benchRows}</tbody></table>
    <h2 class="mc-section-title">Recruitment Channels</h2>
    <p class="mc-bar-note">Every pathway leads back to learning resources.</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Channel</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${channelRows}</tbody></table>
    <h2 class="mc-section-title">County Growth Plans</h2>
    <p class="mc-bar-note">${sg.county_growth_plans.counties_needing_support} counties need support · <a href="${sg.county_growth_plans.route}">County OS</a></p>
    <ul class="mc-deliverables">${sg.county_growth_plans.components.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Success Indicators</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${indicatorRows}</tbody></table>
    <h2 class="mc-section-title">Top 15 Cities (250 indexed)</h2>
    <table class="mc-table"><thead><tr><th>Rank</th><th>City</th><th>Population</th><th>Leaders</th><th>Status</th></tr></thead>
      <tbody>${topCities}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${sg.long_term_vision.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Mission Control Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${sg.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${sg.recommended_next_build.number} — ${sg.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${sg.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_STATEWIDE_GROWTH.md">MASTER_STATEWIDE_GROWTH.md</a> ·
      <a href="/data/statewide-growth.json">JSON</a> ·
      <a href="/data/arkansas-cities.json">250 Cities</a> ·
      <a href="/mission-control/county-os.html">County OS</a> ·
      <a href="/mission-control/master-plan.html">Master Plan</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initNeighborhoodOrganizing() {
  const root = document.getElementById('mc-neighborhood-organizing-root');
  if (!root) return;

  const [noRes, mcRes] = await Promise.all([
    fetch('/data/neighborhood-organizing.json'),
    fetch('/data/mission-control.json')
  ]);
  const no = await noRes.json();
  const mc = await mcRes.json();
  const s = no.summary;

  const layerRows = no.four_geographic_layers.map(l => `
    <tr><td>L${l.layer}</td><td><code>${l.id}</code></td><td>${l.title}</td>
      <td>${l.mission}</td><td>${l.target ?? '—'}</td><td>${l.status}</td></tr>`).join('');

  const pathwayRows = no.relational_organizing.pathways.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.pathway}</td><td>${p.status}</td></tr>`).join('');

  const kitRows = no.neighborhood_resource_kits.items.map(k => `
    <tr><td><code>${k.id}</code></td><td>${k.item}</td><td>${k.status}</td>
      <td>${k.route ? `<a href="${k.route}">→</a>` : '—'}</td></tr>`).join('');

  const formatRows = no.community_conversation_model.formats.map(f => `<li>${f}</li>`).join('');

  const mentorRows = no.mentorship_network.stages.map(st => `
    <tr><td>${st.stage}</td><td><code>${st.id}</code></td><td>${st.title}</td><td>${st.status}</td></tr>`).join('');

  const healthRows = no.community_health_indicators.map(h => `
    <tr><td><code>${h.id}</code></td><td>${h.indicator}</td><td>${h.current}</td><td>${h.status}</td></tr>`).join('');

  const systemRows = no.system_connections.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td></tr>`).join('');

  const dashRows = no.neighborhood_dashboard.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.title}</td><td>${m.current}</td>
      <td>${m.target ?? '—'}</td><td>${m.status}</td></tr>`).join('');

  const vizRows = no.arkansas_neighbor_goal.visualization_dimensions.map(v => `
    <tr><td>${v.dimension}</td><td>${v.current}</td><td>${v.target}</td><td>${v.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Neighborhood Organizing</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #57 · ${no.title}</p>
      <h1>The Last Mile Architecture</h1>
      <p class="mc-header__question">${no.governing_principle}</p>
      <p class="mc-bar-note">${no.purpose}</p>
      <p class="mc-bar-note"><strong>Vision:</strong> ${no.vision}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Last mile readiness</div><div class="mc-stat__value">${s.neighborhood_organizing_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Neighborhoods</div><div class="mc-stat__value">${s.neighborhoods_represented}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Neighborhood Leaders</div><div class="mc-stat__value">${s.neighborhood_leaders}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Conversations</div><div class="mc-stat__value">${s.active_conversations}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Participants</div><div class="mc-stat__value">${s.participants_current.toLocaleString()}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Map status</div><div class="mc-stat__value" style="font-size:1.25rem">${s.illumination_map_status}</div></div>
    </div>
    <h2 class="mc-section-title">Four Geographic Layers</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Layer</th><th>Mission</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${layerRows}</tbody></table>
    <h2 class="mc-section-title">Neighborhood Education Leaders</h2>
    <p class="mc-bar-note"><strong>Role:</strong> ${no.neighborhood_education_leaders.role}</p>
    <p class="mc-bar-note"><strong>Purpose:</strong> ${no.neighborhood_education_leaders.purpose}</p>
    <ul class="mc-deliverables">${no.neighborhood_education_leaders.activities.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Neighborhood Profiles</h2>
    <p class="mc-bar-note">${no.neighborhood_profiles.privacy} · <a href="${no.neighborhood_profiles.registry}">Registry</a> · ${no.neighborhood_profiles.profiles_count} profiles</p>
    <ul class="mc-deliverables">${no.neighborhood_profiles.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Relational Organizing</h2>
    <p class="mc-bar-note">${no.relational_organizing.principle}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Pathway</th><th>Status</th></tr></thead>
      <tbody>${pathwayRows}</tbody></table>
    <h2 class="mc-section-title">Arkansas Neighbor Goal — 200,000 Connected</h2>
    <p class="mc-bar-note">${no.arkansas_neighbor_goal.progress_pct}% progress · Aligned with ${no.arkansas_neighbor_goal.aligned_with}</p>
    <table class="mc-table"><thead><tr><th>Dimension</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${vizRows}</tbody></table>
    <h2 class="mc-section-title">Neighborhood Resource Kits</h2>
    <p class="mc-bar-note">${no.neighborhood_resource_kits.items_ready}/${no.neighborhood_resource_kits.items_total} items ready · ${no.neighborhood_resource_kits.emphasis}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Item</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${kitRows}</tbody></table>
    <h2 class="mc-section-title">Community Conversation Model</h2>
    <p class="mc-bar-note">${no.community_conversation_model.emphasis}</p>
    <ul class="mc-deliverables">${formatRows}</ul>
    <h2 class="mc-section-title">Last Mile Dashboard</h2>
    <p class="mc-bar-note">Illumination map: ${no.neighborhood_dashboard.illumination_map_status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">Mentorship Network</h2>
    <p class="mc-bar-note">${no.mentorship_network.flow}</p>
    <p class="mc-bar-note">${no.mentorship_network.principle}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${mentorRows}</tbody></table>
    <h2 class="mc-section-title">Community Health Indicators</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${healthRows}</tbody></table>
    <h2 class="mc-section-title">Privacy Principles</h2>
    <ul class="mc-deliverables">${no.privacy_principles.principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Connections</h2>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${no.long_term_vision.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${no.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${no.recommended_next_build.number} — ${no.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${no.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_NEIGHBORHOOD_ORGANIZING.md">MASTER_NEIGHBORHOOD_ORGANIZING.md</a> ·
      <a href="/data/neighborhood-organizing.json">JSON</a> ·
      <a href="/data/neighborhood-profiles.json">Profiles</a> ·
      <a href="/mission-control/statewide-growth.html">Statewide Growth (#56)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCivicAtlas() {
  const root = document.getElementById('mc-civic-atlas-root');
  if (!root) return;

  const [caRes, mcRes] = await Promise.all([
    fetch('/data/civic-atlas.json'),
    fetch('/data/mission-control.json')
  ]);
  const ca = await caRes.json();
  const mc = await mcRes.json();
  const s = ca.summary;

  const hierarchyRows = ca.geographic_hierarchy.levels.map(l => `
    <tr><td>L${l.level}</td><td><code>${l.id}</code></td><td>${l.title}</td>
      <td>${l.scope}</td><td>${l.status}</td></tr>`).join('');

  const ecsRows = ca.educational_coverage_score.components.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.category}</td><td>${c.weight_pct}%</td>
      <td>${c.indicators.join(', ')}</td><td>${c.status}</td></tr>`).join('');

  const needsRows = ca.community_needs_assessment.signals.map(n => `
    <tr><td><code>${n.id}</code></td><td>${n.signal}</td><td>${n.count}</td><td>${n.status}</td></tr>`).join('');

  const assetTypeRows = ca.community_assets_directory.asset_types.map(t => `<li>${t}</li>`).join('');

  const growthRows = ca.community_growth_dashboard.metrics.map(g => `
    <tr><td><code>${g.id}</code></td><td>${g.metric}</td><td>${g.current}</td><td>${g.status}</td></tr>`).join('');

  const panelRows = ca.mc_integration.panels.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.panel}</td><td>${p.status}</td></tr>`).join('');

  const layerRows = ca.map_layers.layers.map(l => `
    <tr><td><code>${l.id}</code></td><td>${l.layer}</td><td>${l.status}</td></tr>`).join('');

  const regionRows = ca.region_coverage.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.title}</td><td>${r.counties_mapped}</td>
      <td>${r.avg_coverage_score}</td><td>${r.status}</td></tr>`).join('');

  const systemRows = ca.system_connections.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td></tr>`).join('');

  const bottomCounties = ca.county_coverage.counties.slice(0, 10).map(c => `
    <tr><td>${c.name}</td><td>${c.education_coverage_score}</td>
      <td>${c.education_leaders}</td><td>${c.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Civic Atlas</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #58 · ${ca.title}</p>
      <h1>Arkansas Civic Atlas</h1>
      <p class="mc-header__question">${ca.governing_principle}</p>
      <p class="mc-bar-note">${ca.purpose}</p>
      <p class="mc-bar-note"><strong>Not political targeting:</strong> Educational planning system</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Atlas readiness</div><div class="mc-stat__value">${s.civic_atlas_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Avg ECS score</div><div class="mc-stat__value">${s.statewide_avg_coverage_score}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties scored</div><div class="mc-stat__value">${s.counties_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Communities</div><div class="mc-stat__value">${s.communities_joined}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Assets cataloged</div><div class="mc-stat__value">${s.assets_cataloged}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Map</div><div class="mc-stat__value" style="font-size:1.1rem">${s.interactive_map_status}</div></div>
    </div>
    <h2 class="mc-section-title">Planning Questions</h2>
    <ul class="mc-deliverables">${ca.planning_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Geographic Hierarchy</h2>
    <p class="mc-bar-note">${ca.geographic_hierarchy.flow}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Level</th><th>Scope</th><th>Status</th></tr></thead>
      <tbody>${hierarchyRows}</tbody></table>
    <h2 class="mc-section-title">Educational Coverage Score</h2>
    <p class="mc-bar-note">${ca.educational_coverage_score.principle} · Scale: ${ca.educational_coverage_score.scale}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Category</th><th>Weight</th><th>Indicators</th><th>Status</th></tr></thead>
      <tbody>${ecsRows}</tbody></table>
    <h2 class="mc-section-title">7 Regions</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Region</th><th>Counties mapped</th><th>Avg ECS</th><th>Status</th></tr></thead>
      <tbody>${regionRows}</tbody></table>
    <h2 class="mc-section-title">Sample Counties (ECS Baseline)</h2>
    <table class="mc-table"><thead><tr><th>County</th><th>ECS</th><th>Leaders</th><th>Status</th></tr></thead>
      <tbody>${bottomCounties}</tbody></table>
    <h2 class="mc-section-title">Community Assets Directory</h2>
    <p class="mc-bar-note">${s.assets_cataloged} assets · <a href="${ca.community_assets_directory.registry}">Registry</a></p>
    <ul class="mc-deliverables">${assetTypeRows}</ul>
    <h2 class="mc-section-title">Community Needs Assessment</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Signal</th><th>Count</th><th>Status</th></tr></thead>
      <tbody>${needsRows}</tbody></table>
    <h2 class="mc-section-title">Arkansas Civic Calendar</h2>
    <p class="mc-bar-note">${ca.arkansas_civic_calendar.events_scheduled} events · Browse by: ${ca.arkansas_civic_calendar.browse_by.join(', ')}</p>
    <ul class="mc-deliverables">${ca.arkansas_civic_calendar.event_types.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Community Growth Dashboard</h2>
    <p class="mc-bar-note">Geographic visualization: ${ca.community_growth_dashboard.geographic_visualization}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${growthRows}</tbody></table>
    <h2 class="mc-section-title">Map Layers</h2>
    <p class="mc-bar-note">Interactive map: ${ca.map_layers.interactive_map_status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Layer</th><th>Status</th></tr></thead>
      <tbody>${layerRows}</tbody></table>
    <h2 class="mc-section-title">Civic Story Archive</h2>
    <p class="mc-bar-note">${ca.civic_story_archive.stories_documented} stories documented</p>
    <ul class="mc-deliverables">${ca.civic_story_archive.story_types.map(st => `<li>${st}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Resource Allocation Engine</h2>
    <ul class="mc-deliverables">${ca.resource_allocation_engine.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">MC Atlas Dashboard Panels</h2>
    <p class="mc-bar-note">${ca.mc_integration.panels_live}/${ca.mc_integration.panels.length} panels partial or live</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Panel</th><th>Status</th></tr></thead>
      <tbody>${panelRows}</tbody></table>
    <h2 class="mc-section-title">Future Expansion</h2>
    <ul class="mc-deliverables">${ca.future_expansion.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Connections</h2>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${ca.long_term_vision.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ca.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ca.recommended_next_build.number} — ${ca.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ca.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CIVIC_ATLAS.md">MASTER_CIVIC_ATLAS.md</a> ·
      <a href="/data/civic-atlas.json">JSON</a> ·
      <a href="/data/community-profiles.json">Profiles</a> ·
      <a href="/data/community-assets.json">Assets</a> ·
      <a href="/mission-control/statewide-growth.html">Statewide Growth</a> ·
      <a href="/mission-control/neighborhood-organizing.html">Neighborhood (#57)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initRelationshipOs() {
  const root = document.getElementById('mc-relationship-os-root');
  if (!root) return;

  const [rosRes, mcRes] = await Promise.all([
    fetch('/data/relationship-os.json'),
    fetch('/data/mission-control.json')
  ]);
  const ros = await rosRes.json();
  const mc = await mcRes.json();
  const s = ros.summary;

  const networkRows = ros.five_networks.map(n => `
    <tr><td>${n.number}</td><td><code>${n.id}</code></td><td>${n.title}</td>
      <td>${n.tracks.slice(0, 3).join(', ')}…</td><td>${n.status}</td></tr>`).join('');

  const timelineRows = ros.relationship_timeline.stages.map(st => `
    <tr><td>${st.stage}</td><td><code>${st.id}</code></td><td>${st.event}</td><td>${st.status}</td></tr>`).join('');

  const healthRows = ros.relationship_health_score.indicators.map(h => `
    <tr><td><code>${h.id}</code></td><td>${h.indicator}</td><td>${h.weight_pct}%</td><td>${h.status}</td></tr>`).join('');

  const oppRows = ros.opportunity_tracker.opportunities.map(o => `
    <tr><td><code>${o.id}</code></td><td>${o.opportunity}</td><td>${o.count}</td><td>${o.status}</td></tr>`).join('');

  const widgetRows = ros.crm_dashboard.widgets.map(w => `
    <tr><td><code>${w.id}</code></td><td>${w.widget}</td><td>${w.current}</td><td>${w.status}</td></tr>`).join('');

  const mentorRows = ros.mentorship_mapping.levels.map(m => `
    <tr><td>${m.level}</td><td>${m.role}</td><td>${m.status}</td></tr>`).join('');

  const systemRows = ros.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Relationship OS</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #59 · ${ros.title} · ${ros.acronym}</p>
      <h1>Institutional Relationship Brain</h1>
      <p class="mc-header__question">${ros.governing_principle}</p>
      <p class="mc-bar-note">${ros.purpose}</p>
      <p class="mc-bar-note"><strong>Not traditional CRM:</strong> Civic education relationships — not sales or fundraising</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">ROS readiness</div><div class="mc-stat__value">${s.relationship_os_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Participants</div><div class="mc-stat__value">${s.total_participants}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Active relationships</div><div class="mc-stat__value">${s.active_relationships}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Relationship edges</div><div class="mc-stat__value">${s.relationship_edges}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Edge types defined</div><div class="mc-stat__value">${s.relationship_types_defined}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">CRM widgets live</div><div class="mc-stat__value">${s.crm_widgets_live}/10</div></div>
    </div>
    <h2 class="mc-section-title">Relationship Philosophy</h2>
    <p class="mc-bar-note">${ros.relationship_philosophy.principle}</p>
    <ul class="mc-deliverables">${ros.relationship_philosophy.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Five Relationship Networks</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Network</th><th>Tracks</th><th>Status</th></tr></thead>
      <tbody>${networkRows}</tbody></table>
    <h2 class="mc-section-title">Relationship Timeline</h2>
    <p class="mc-bar-note">${ros.relationship_timeline.flow}</p>
    <p class="mc-bar-note">${ros.relationship_timeline.events_recorded} events recorded</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Event</th><th>Status</th></tr></thead>
      <tbody>${timelineRows}</tbody></table>
    <h2 class="mc-section-title">Relationship Health Score</h2>
    <p class="mc-bar-note">${ros.relationship_health_score.purpose} · Avg: ${s.statewide_avg_health_score}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Weight</th><th>Status</th></tr></thead>
      <tbody>${healthRows}</tbody></table>
    <h2 class="mc-section-title">Communication History</h2>
    <p class="mc-bar-note">${ros.communication_history.communications_logged} communications logged</p>
    <ul class="mc-deliverables">${ros.communication_history.types.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Opportunity Tracker</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Opportunity</th><th>Count</th><th>Status</th></tr></thead>
      <tbody>${oppRows}</tbody></table>
    <h2 class="mc-section-title">Mentorship Mapping</h2>
    <p class="mc-bar-note">${ros.mentorship_mapping.chain} · ${s.mentor_pairs} pairs</p>
    <table class="mc-table"><thead><tr><th>Level</th><th>Role</th><th>Status</th></tr></thead>
      <tbody>${mentorRows}</tbody></table>
    <h2 class="mc-section-title">Privacy Framework</h2>
    <ul class="mc-deliverables">${ros.privacy_framework.principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">CRM Dashboard Widgets</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Widget</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${widgetRows}</tbody></table>
    <h2 class="mc-section-title">Relationship Registry</h2>
    <p class="mc-bar-note">${s.relationship_types_defined} types · ${s.relationship_edges} edges · <a href="${ros.relationship_registry.route}">Registry</a></p>
    <h2 class="mc-section-title">Contact Intelligence Link</h2>
    <p class="mc-bar-note">Build #${ros.contact_intelligence_link.build} · ${ros.contact_intelligence_link.modules} modules · <a href="${ros.contact_intelligence_link.route}">Contact Intelligence</a></p>
    <h2 class="mc-section-title">Integration Stack</h2>
    <p class="mc-bar-note">${ros.integration.flow}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${ros.long_term_vision.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ros.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ros.recommended_next_build.number} — ${ros.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ros.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_RELATIONSHIP_OS.md">MASTER_RELATIONSHIP_OS.md</a> ·
      <a href="/data/relationship-os.json">JSON</a> ·
      <a href="/data/relationship-registry.json">Edge Registry</a> ·
      <a href="/mission-control/contact-intelligence.html">Contact Intelligence</a> ·
      <a href="/mission-control/civic-atlas.html">Civic Atlas</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initInstitutionalAi() {
  const root = document.getElementById('mc-institutional-ai-root');
  if (!root) return;

  const [iaRes, mcRes] = await Promise.all([
    fetch('/data/institutional-ai.json'),
    fetch('/data/mission-control.json')
  ]);
  const ia = await iaRes.json();
  const mc = await mcRes.json();
  const s = ia.summary;

  const roleRows = ia.seven_roles.map(r => `
    <tr><td>${r.number}</td><td><code>${r.id}</code></td><td>${r.title}</td>
      <td>${r.audience}</td><td>${r.visibility}</td><td>${r.status}</td></tr>`).join('');

  const sourceRows = ia.institutional_rule_one.sources.map(src => `
    <tr><td><code>${src.id}</code></td><td>${src.source}</td>
      <td>${src.count ?? '—'}</td><td>${src.status}</td>
      <td>${src.route ? `<a href="${src.route}">→</a>` : '—'}</td></tr>`).join('');

  const confRows = ia.confidence_levels.levels.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.level}</td><td>${c.definition}</td></tr>`).join('');

  const metricRows = ia.mc_ai_dashboard.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.current}</td><td>${m.status}</td></tr>`).join('');

  const systemRows = ia.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Institutional AI</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #60 · ${ia.title}</p>
      <h1>Arkansas Civic Intelligence System</h1>
      <p class="mc-header__question">${ia.governing_principle}</p>
      <p class="mc-bar-note">${ia.purpose}</p>
      <p class="mc-bar-note"><strong>Not a chatbot.</strong> Evidence is the authority. AI is the guide.</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">AI readiness</div><div class="mc-stat__value">${s.institutional_ai_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Roles defined</div><div class="mc-stat__value">${s.seven_roles_defined}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Roles operational</div><div class="mc-stat__value">${s.roles_operational}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Questions answered</div><div class="mc-stat__value">${s.questions_answered}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Chat UI</div><div class="mc-stat__value" style="font-size:1rem">${s.chat_ui_live ? 'live' : 'off'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">RAG pipeline</div><div class="mc-stat__value" style="font-size:1rem">${s.rag_pipeline_live ? 'live' : 'off'}</div></div>
    </div>
    <h2 class="mc-section-title">AI Philosophy</h2>
    <p class="mc-bar-note"><strong>Core question:</strong> "${ia.ai_philosophy.core_question}"</p>
    <p class="mc-bar-note"><strong>Not designed for:</strong> ${ia.ai_philosophy.not_designed_for.join(' · ')}</p>
    <h2 class="mc-section-title">Institutional Rule #1</h2>
    <p class="mc-bar-note">${ia.institutional_rule_one.rule}</p>
    <p class="mc-bar-note">${ia.institutional_rule_one.unknown_response}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Source</th><th>Count</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${sourceRows}</tbody></table>
    <h2 class="mc-section-title">Seven AI Roles</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Role</th><th>Audience</th><th>Visibility</th><th>Status</th></tr></thead>
      <tbody>${roleRows}</tbody></table>
    <h2 class="mc-section-title">Confidence Levels</h2>
    <p class="mc-bar-note">${ia.confidence_levels.never_disguise_uncertainty ? 'Never disguise uncertainty.' : ''}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Level</th><th>Definition</th></tr></thead>
      <tbody>${confRows}</tbody></table>
    <h2 class="mc-section-title">Source Panel</h2>
    <p class="mc-bar-note">${ia.source_panel.principle}</p>
    <ul class="mc-deliverables">${ia.source_panel.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">AI Memory</h2>
    <p class="mc-bar-note">${ia.ai_memory.prohibited}. User control: ${ia.ai_memory.user_control ? 'yes' : 'no'}</p>
    <ul class="mc-deliverables">${ia.ai_memory.allowed.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Safety Principles</h2>
    <ul class="mc-deliverables">${ia.safety_principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Technical Status</h2>
    <p class="mc-bar-note">API: ${ia.technical_status.api_provider} · Citation required: ${ia.technical_status.citation_required ? 'yes' : 'no'}</p>
    <h2 class="mc-section-title">MC AI Dashboard</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Future Capabilities</h2>
    <ul class="mc-deliverables">${ia.future_capabilities.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Integration</h2>
    <p class="mc-bar-note">${ia.integration.flow}</p>
    <p class="mc-bar-note">${ia.integration.principle}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Extends Build #26</h2>
    <p class="mc-bar-note">${ia.persona.name} · <a href="${ia.extends_build_26.route}">AI Knowledge Engine</a> · ${ia.extends_build_26.learning_modes} learning modes</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ia.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ia.recommended_next_build.number} — ${ia.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ia.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_INSTITUTIONAL_AI.md">MASTER_INSTITUTIONAL_AI.md</a> ·
      <a href="/data/institutional-ai.json">JSON</a> ·
      <a href="/mission-control/ai-knowledge.html">AI Engine (#26)</a> ·
      <a href="/mission-control/evidence-ledger.html">Evidence Ledger</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCoalitionNetwork() {
  const root = document.getElementById('mc-coalition-network-root');
  if (!root) return;

  const [cnRes, mcRes] = await Promise.all([
    fetch('/data/coalition-network.json'),
    fetch('/data/mission-control.json')
  ]);
  const cn = await cnRes.json();
  const mc = await mcRes.json();
  const s = cn.summary;

  const catRows = cn.partnership_categories.map(c => `
    <tr><td>${c.number}</td><td><code>${c.id}</code></td><td>${c.title}</td>
      <td>${c.current}</td><td>${c.status}</td></tr>`).join('');

  const levelRows = cn.partnership_levels.map(l => `
    <tr><td><code>${l.id}</code></td><td>${l.level}</td><td>${l.commitment}</td>
      <td>${l.current}</td><td>${l.status}</td></tr>`).join('');

  const metricRows = cn.growth_metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.current}</td>
      <td>${m.target ?? '—'}</td><td>${m.status}</td></tr>`).join('');

  const reqRows = cn.partnership_requests.request_types.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.request}</td><td>${r.workflow_status}</td></tr>`).join('');

  const systemRows = cn.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Coalition Network</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #61 · ${cn.title}</p>
      <h1>Building Arkansas Together</h1>
      <p class="mc-header__question">${cn.governing_principle}</p>
      <p class="mc-bar-note">${cn.purpose}</p>
      <p class="mc-bar-note"><strong>Mission:</strong> ${cn.coalition_mission}</p>
      <p class="mc-bar-note"><strong>Strategic priority:</strong> ${cn.strategic_priority.rank} — monitor coalition health</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Coalition readiness</div><div class="mc-stat__value">${s.coalition_network_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Organizations</div><div class="mc-stat__value">${s.organizations_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties</div><div class="mc-stat__value">${s.counties_represented}/${s.counties_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Cities</div><div class="mc-stat__value">${s.cities_represented}/250</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Joint events</div><div class="mc-stat__value">${s.joint_events}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pending requests</div><div class="mc-stat__value">${s.pending_requests}</div></div>
    </div>
    <h2 class="mc-section-title">Coalition Principles</h2>
    <ul class="mc-deliverables">${cn.coalition_principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <p class="mc-bar-note">${cn.common_ground}</p>
    <h2 class="mc-section-title">Six Partnership Categories</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Category</th><th>Partners</th><th>Status</th></tr></thead>
      <tbody>${catRows}</tbody></table>
    <h2 class="mc-section-title">Partnership Levels</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Level</th><th>Commitment</th><th>Count</th><th>Status</th></tr></thead>
      <tbody>${levelRows}</tbody></table>
    <h2 class="mc-section-title">Coalition Profile Fields</h2>
    <ul class="mc-deliverables">${cn.coalition_profile.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Resource Center</h2>
    <p class="mc-bar-note">${cn.resource_center.items_available}/${cn.resource_center.items_total} items available</p>
    <ul class="mc-deliverables">${cn.resource_center.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">County Coalition Dashboard</h2>
    <p class="mc-bar-note">${s.counties_represented}/${s.counties_total} counties with partners · <a href="${cn.county_coalition_dashboard.public_route}">Public counties</a></p>
    <ul class="mc-deliverables">${cn.county_coalition_dashboard.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Collaboration Hub</h2>
    <p class="mc-bar-note">${cn.collaboration_hub.principle}</p>
    <ul class="mc-deliverables">${cn.collaboration_hub.features.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Coalition Recognition</h2>
    <ul class="mc-deliverables">${cn.coalition_recognition.types.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Growth Metrics</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">Partnership Requests</h2>
    <p class="mc-bar-note">${s.pending_requests} pending</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Request Type</th><th>Workflow</th></tr></thead>
      <tbody>${reqRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${cn.integration.unifies}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <ul class="mc-deliverables">${cn.long_term_vision.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cn.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cn.recommended_next_build.number} — ${cn.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cn.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_COALITION_NETWORK.md">MASTER_COALITION_NETWORK.md</a> ·
      <a href="/data/coalition-network.json">JSON</a> ·
      <a href="/coalition/">Coalition Hub</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCitizenActionCenter() {
  const root = document.getElementById('mc-citizen-action-center-root');
  if (!root) return;

  const [cacRes, mcRes] = await Promise.all([
    fetch('/data/citizen-action-center.json'),
    fetch('/data/mission-control.json')
  ]);
  const cac = await cacRes.json();
  const mc = await mcRes.json();
  const s = cac.summary;

  const stageRows = cac.guiding_philosophy.stages.map(st => `
    <tr><td>${st.step}</td><td>${st.stage}</td><td>${st.status}</td></tr>`).join('');

  const pathwayRows = cac.six_pathways.map(p => `
    <tr><td>${p.number}</td><td><code>${p.id}</code></td><td>${p.title}</td>
      <td>${p.audience}</td><td>${p.status}</td>
      <td>${p.route ? `<a href="${p.route}">→</a>` : '—'}</td></tr>`).join('');

  const metricRows = cac.mc_citizen_dashboard.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.current}</td>
      <td>${m.target ?? '—'}</td><td>${m.status}</td></tr>`).join('');

  const systemRows = cac.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td>
      <td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Citizen Action Center</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #62 · ${cac.title}</p>
      <h1>The Arkansas Citizen Action Center</h1>
      <p class="mc-header__question">${cac.governing_principle}</p>
      <p class="mc-bar-note">${cac.purpose}</p>
      <p class="mc-bar-note"><strong>Bridge:</strong> ${cac.bridge_role} · <strong>Not advocacy:</strong> ${cac.not_advocacy ? 'Yes' : 'No'}</p>
      <p class="mc-bar-note"><strong>Guiding sequence:</strong> ${cac.guiding_philosophy.sequence} — ${cac.guiding_philosophy.rule}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Citizen Action readiness</div><div class="mc-stat__value">${s.citizen_action_center_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pathways</div><div class="mc-stat__value">${s.pathways_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Registered</div><div class="mc-stat__value">${s.registered_participants}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Action hub live</div><div class="mc-stat__value">${s.action_hub_items_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">200K goal</div><div class="mc-stat__value">${s.participants_connected}/${s.participants_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties active</div><div class="mc-stat__value">${s.counties_with_activity}/75</div></div>
    </div>
    <h2 class="mc-section-title">Guiding Philosophy</h2>
    <table class="mc-table"><thead><tr><th>Step</th><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${stageRows}</tbody></table>
    <h2 class="mc-section-title">Six Citizen Pathways</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Pathway</th><th>Audience</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${pathwayRows}</tbody></table>
    ${cac.six_pathways.map(p => `
      <h3 class="mc-subsection-title">${p.title}</h3>
      <ul class="mc-deliverables">${p.options.map(o => `<li>${o}</li>`).join('')}</ul>
      ${p.emphasis ? `<p class="mc-bar-note">${p.emphasis}</p>` : ''}
      ${p.mc_tracks ? `<p class="mc-bar-note">MC tracks: ${p.mc_tracks}</p>` : ''}
      ${p.note ? `<p class="mc-bar-note">${p.note}</p>` : ''}
      ${p.review ? `<p class="mc-bar-note">${p.review}</p>` : ''}`).join('')}
    <h2 class="mc-section-title">Public Official Resource Center</h2>
    <p class="mc-bar-note">${cac.public_official_resource_center.principle} · ${cac.public_official_resource_center.packets_available} packets · ${cac.public_official_resource_center.status}</p>
    <ul class="mc-deliverables">${cac.public_official_resource_center.sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <p class="mc-bar-note"><strong>Audiences:</strong> ${cac.public_official_resource_center.audiences.join(' · ')}</p>
    <h2 class="mc-section-title">Relational Sharing Hub</h2>
    <p class="mc-bar-note">${cac.relational_sharing_hub.title} · per-page tools: ${cac.relational_sharing_hub.per_page_tools ? 'specified' : 'no'} · visualization: ${cac.relational_sharing_hub.visualization_status}</p>
    <ul class="mc-deliverables">${cac.relational_sharing_hub.audiences.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Citizen Dashboard</h2>
    <p class="mc-bar-note">${cac.citizen_dashboard.title} · ${cac.citizen_dashboard.status} · ${cac.citizen_dashboard.registered_users} registered</p>
    <ul class="mc-deliverables">${cac.citizen_dashboard.panels.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">County Action Pages</h2>
    <p class="mc-bar-note">${cac.county_action_pages.counties_with_activity}/${cac.county_action_pages.counties_total} counties · <a href="${cac.county_action_pages.route}">County index</a> · ${cac.county_action_pages.status}</p>
    <ul class="mc-deliverables">${cac.county_action_pages.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Mission Control Citizen Dashboard</h2>
    <p class="mc-bar-note">${cac.mc_citizen_dashboard.measures}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${cac.integration.extends}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Future Expansion</h2>
    <ul class="mc-deliverables">${cac.future_expansion.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${cac.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cac.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cac.recommended_next_build.number} — ${cac.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cac.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CITIZEN_ACTION_CENTER.md">MASTER_CITIZEN_ACTION_CENTER.md</a> ·
      <a href="/data/citizen-action-center.json">JSON</a> ·
      <a href="/mission-control/civic-action-lab.html">Civic Action Lab</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCampaignFinanceObservatory() {
  const root = document.getElementById('mc-campaign-finance-observatory-root');
  if (!root) return;

  const [cfoRes, mcRes] = await Promise.all([
    fetch('/data/campaign-finance-observatory.json'),
    fetch('/data/mission-control.json')
  ]);
  const cfo = await cfoRes.json();
  const mc = await mcRes.json();
  const s = cfo.summary;

  const divisionRows = cfo.eight_divisions.map(d => `
    <tr><td>${d.number}</td><td><code>${d.id}</code></td><td>${d.title}</td>
      <td>${d.status}</td></tr>`).join('');

  const metricRows = cfo.mc_observatory_dashboard.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.current}</td>
      <td>${m.target ?? '—'}</td><td>${m.status}</td></tr>`).join('');

  const systemRows = cfo.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td>
      <td>${sys.note ?? '—'}</td></tr>`).join('');

  const stageRows = cfo.before_after_explorer.stages.map(st => `
    <tr><td>${st.stage}</td><td>${st.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Campaign Finance Observatory</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #63 · ${cfo.title}</p>
      <h1>The Arkansas Campaign Finance Intelligence Center</h1>
      <p class="mc-header__question">${cfo.governing_principle}</p>
      <p class="mc-bar-note">${cfo.purpose}</p>
      <p class="mc-bar-note"><strong>Flagship system:</strong> ${cfo.flagship_system ? 'Yes' : 'No'} · <strong>Distinct from:</strong> ${cfo.distinct_from.system} (${cfo.distinct_from.difference})</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Observatory readiness</div><div class="mc-stat__value">${s.campaign_finance_observatory_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Divisions</div><div class="mc-stat__value">${s.divisions_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Datasets</div><div class="mc-stat__value">${s.datasets_published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Charts</div><div class="mc-stat__value">${s.charts_completed}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Research notes</div><div class="mc-stat__value">${s.research_notes_completed}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Arkansas charts</div><div class="mc-stat__value">${s.arkansas_charts}</div></div>
    </div>
    <h2 class="mc-section-title">Mission Questions</h2>
    <ul class="mc-deliverables">${cfo.mission_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Eight Research Divisions</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Division</th><th>Status</th></tr></thead>
      <tbody>${divisionRows}</tbody></table>
    ${cfo.eight_divisions.map(d => `
      <h3 class="mc-subsection-title">${d.title}</h3>
      <p class="mc-bar-note">${d.focus}</p>
      <ul class="mc-deliverables">${(d.topics || d.fields || d.examples || []).map(t => `<li>${t}</li>`).join('')}</ul>
      ${d.goal ? `<p class="mc-bar-note">${d.goal}</p>` : ''}
      ${d.note ? `<p class="mc-bar-note">${d.note}</p>` : ''}
      ${d.per_page ? `<p class="mc-bar-note">Per page: ${d.per_page}</p>` : ''}`).join('')}
    <h2 class="mc-section-title">${cfo.before_after_explorer.title}</h2>
    <p class="mc-bar-note">${cfo.before_after_explorer.emphasis} · ${cfo.before_after_explorer.status}</p>
    <table class="mc-table"><thead><tr><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${stageRows}</tbody></table>
    <h2 class="mc-section-title">${cfo.methodology_pages.title}</h2>
    <p class="mc-bar-note">Required per chart: ${cfo.methodology_pages.required_per_chart ? 'Yes' : 'No'} · ${cfo.methodology_pages.status}</p>
    <ul class="mc-deliverables">${cfo.methodology_pages.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cfo.data_integrity_standards.title}</h2>
    <p class="mc-bar-note">${cfo.data_integrity_standards.status}</p>
    <ul class="mc-deliverables">${cfo.data_integrity_standards.required_fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cfo.mc_observatory_dashboard.title}</h2>
    <p class="mc-bar-note">Living research program: ${cfo.mc_observatory_dashboard.living_research_program ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${cfo.integration.chain}</p>
    <p class="mc-bar-note">${cfo.integration.principle}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${cfo.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cfo.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cfo.recommended_next_build.number} — ${cfo.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cfo.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CAMPAIGN_FINANCE_OBSERVATORY.md">MASTER_CAMPAIGN_FINANCE_OBSERVATORY.md</a> ·
      <a href="/data/campaign-finance-observatory.json">JSON</a> ·
      <a href="/mission-control/evidence-ledger.html">Evidence Ledger</a> ·
      <a href="/mission-control/research-library.html">Research Library</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasActionNetwork() {
  const root = document.getElementById('mc-arkansas-action-network-root');
  if (!root) return;

  const [aanRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-action-network.json'),
    fetch('/data/mission-control.json')
  ]);
  const aan = await aanRes.json();
  const mc = await mcRes.json();
  const s = aan.summary;

  const pyramidRows = aan.leadership_pyramid.map(l => `
    <tr><td>${l.level}</td><td><code>${l.id}</code></td><td>${l.role}</td>
      <td>${l.goal}</td><td>${l.current}</td><td>${l.status}</td>
      <td>${l.route ? `<a href="${l.route}">→</a>` : '—'}</td></tr>`).join('');

  const objectiveRows = aan.growth_objectives.map(o => `
    <tr><td><code>${o.id}</code></td><td>${o.title}</td><td>${o.current}</td>
      <td>${o.target ?? '—'}</td><td>${o.status}</td></tr>`).join('');

  const invitationRows = aan.invitation_engine.stages.map(st => `
    <tr><td>${st.stage}</td><td>${st.audience}</td><td>${st.status}</td></tr>`).join('');

  const successionRows = aan.leadership_succession.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.current}</td><td>${m.status}</td></tr>`).join('');

  const analyticsRows = aan.growth_analytics.questions.map(q => `
    <tr><td><code>${q.id}</code></td><td>${q.question}</td><td>${q.status}</td></tr>`).join('');

  const systemRows = aan.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td>${sys.route ? `<a href="${sys.route}">→</a>` : '—'}</td>
      <td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Action Network</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #64 · ${aan.title}</p>
      <h1>Building a Statewide Civic Education Movement</h1>
      <p class="mc-header__question">${aan.governing_principle}</p>
      <p class="mc-bar-note">${aan.purpose}</p>
      <p class="mc-bar-note"><strong>Primary growth engine:</strong> ${aan.primary_growth_engine ? 'Yes' : 'No'} · <strong>Unifies:</strong> ${aan.integration.unifies}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Network readiness</div><div class="mc-stat__value">${s.arkansas_action_network_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pyramid levels</div><div class="mc-stat__value">${s.pyramid_levels}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">County teams</div><div class="mc-stat__value">${s.county_teams}/${s.county_teams_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">City teams</div><div class="mc-stat__value">${s.city_teams}/${s.city_teams_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Connected</div><div class="mc-stat__value">${s.connected_arkansans}/${s.connected_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Neighborhood leaders</div><div class="mc-stat__value">${s.neighborhood_leaders}</div></div>
    </div>
    <h2 class="mc-section-title">Arkansas Leadership Pyramid</h2>
    <table class="mc-table"><thead><tr><th>Level</th><th>ID</th><th>Role</th><th>Goal</th><th>Current</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${pyramidRows}</tbody></table>
    ${aan.leadership_pyramid.map(l => `
      <h3 class="mc-subsection-title">Level ${l.level}: ${l.role}</h3>
      <p class="mc-bar-note">Goal: ${l.goal}</p>
      <p class="mc-bar-note"><strong>MC tracks:</strong> ${l.mc_tracks.join(' · ')}</p>
      ${l.examples ? `<ul class="mc-deliverables">${l.examples.map(e => `<li>${e}</li>`).join('')}</ul>` : ''}
      ${l.responsibilities ? `<ul class="mc-deliverables">${l.responsibilities.map(r => `<li>${r}</li>`).join('')}</ul>` : ''}`).join('')}
    <h2 class="mc-section-title">Growth Objectives</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Objective</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${objectiveRows}</tbody></table>
    <h2 class="mc-section-title">${aan.invitation_engine.title}</h2>
    <p class="mc-bar-note">${aan.invitation_engine.principle} · per-page: ${aan.invitation_engine.per_page ? 'Yes' : 'No'} · ${aan.invitation_engine.status}</p>
    <table class="mc-table"><thead><tr><th>Invitation</th><th>Audience</th><th>Status</th></tr></thead>
      <tbody>${invitationRows}</tbody></table>
    <h2 class="mc-section-title">${aan.leadership_academy.title}</h2>
    <p class="mc-bar-note">${aan.leadership_academy.status}</p>
    ${aan.leadership_academy.pathways.map(p => `
      <h3 class="mc-subsection-title">${p.level}</h3>
      <ul class="mc-deliverables">${p.topics.map(t => `<li>${t}</li>`).join('')}</ul>
      ${p.route ? `<p class="mc-bar-note"><a href="${p.route}">Education Academy →</a></p>` : ''}`).join('')}
    <h2 class="mc-section-title">${aan.arkansas_progress_map.title}</h2>
    <p class="mc-bar-note">Visual heartbeat: ${aan.arkansas_progress_map.visual_heartbeat ? 'Yes' : 'No'} · ${aan.arkansas_progress_map.status} · <a href="${aan.arkansas_progress_map.route}">Civic Atlas</a></p>
    <ul class="mc-deliverables">${aan.arkansas_progress_map.layers.map(l => `<li>${l}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${aan.community_recognition.title}</h2>
    <p class="mc-bar-note">${aan.community_recognition.status}</p>
    <ul class="mc-deliverables">${aan.community_recognition.types.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${aan.leadership_succession.title}</h2>
    <p class="mc-bar-note">${aan.leadership_succession.principle}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${successionRows}</tbody></table>
    <h2 class="mc-section-title">${aan.growth_analytics.title}</h2>
    <p class="mc-bar-note">${aan.growth_analytics.focus}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Question</th><th>Status</th></tr></thead>
      <tbody>${analyticsRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${aan.integration.chain}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${aan.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${aan.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${aan.recommended_next_build.number} — ${aan.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${aan.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_ACTION_NETWORK.md">MASTER_ARKANSAS_ACTION_NETWORK.md</a> ·
      <a href="/data/arkansas-action-network.json">JSON</a> ·
      <a href="/mission-control/statewide-growth.html">Statewide Growth</a> ·
      <a href="/mission-control/civic-atlas.html">Civic Atlas</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCivicIntelligenceCommandCenter() {
  const root = document.getElementById('mc-civic-intelligence-command-center-root');
  if (!root) return;

  const [ciccRes, mcRes] = await Promise.all([
    fetch('/data/civic-intelligence-command-center.json'),
    fetch('/data/mission-control.json')
  ]);
  const cicc = await ciccRes.json();
  const mc = await mcRes.json();
  const s = cicc.summary;
  const idx = cicc.institutional_readiness_index;

  const execRows = cicc.executive_dashboard.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.current}${m.unit ? ` ${m.unit}` : ''}</td>
      <td>${m.target ?? '—'}</td><td>${m.status}</td></tr>`).join('');

  const kpiRows = cicc.executive_kpi_cards.cards.map(k => `
    <tr><td><code>${k.id}</code></td><td>${k.label}</td><td>${k.current}${k.unit ? ` ${k.unit}` : ''}</td>
      <td>${k.route ? `<a href="${k.route}">→</a>` : '—'}</td><td>${k.status}</td></tr>`).join('');

  const deptRows = cicc.department_operations_boards.departments.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.department}</td><td>${d.status}</td>
      <td><a href="${d.route}">→</a></td></tr>`).join('');

  const pulseRows = cicc.institutional_pulse.signals.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.signal}</td><td>${p.status}</td>
      <td>${p.note ?? '—'}</td></tr>`).join('');

  const growthRows = cicc.arkansas_growth_dashboard.metrics.map(g => `
    <tr><td><code>${g.id}</code></td><td>${g.goal}</td><td>${g.current}</td>
      <td>${g.target ?? '—'}</td><td>${g.progress_pct ?? g.status ?? '—'}</td></tr>`).join('');

  const readinessRows = idx.categories.map(c => `
    <tr><td>${c.category}</td><td>${c.score}%</td><td>${c.status}</td></tr>`).join('');

  const systemRows = cicc.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Civic Intelligence Command Center</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #65 · ${cicc.title}</p>
      <h1>The Executive Mission Control</h1>
      <p class="mc-header__question">${cicc.governing_principle}</p>
      <p class="mc-bar-note">${cicc.purpose}</p>
      <p class="mc-bar-note"><strong>Operational brain:</strong> ${cicc.operational_brain ? 'Yes' : 'No'} · <strong>5-second health check:</strong> ${cicc.five_second_health_check ? 'Specified' : 'No'} · <a href="${cicc.legacy_executive_route}">MC 2.0 Executive →</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Command Center readiness</div><div class="mc-stat__value">${s.civic_intelligence_command_center_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Readiness Index</div><div class="mc-stat__value">${s.institutional_readiness_index}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Health Score</div><div class="mc-stat__value">${s.institutional_health_score}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Launch readiness</div><div class="mc-stat__value">${s.launch_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Departments</div><div class="mc-stat__value">${s.departments_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Connected</div><div class="mc-stat__value">${s.connected_arkansans}/${s.connected_target}</div></div>
    </div>
    <h2 class="mc-section-title">Executive Philosophy</h2>
    <p class="mc-bar-note">Audience: ${cicc.executive_philosophy.audience}</p>
    <ul class="mc-deliverables">${cicc.executive_philosophy.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cicc.executive_dashboard.title}</h2>
    <p class="mc-bar-note">No drilling required: ${cicc.executive_dashboard.no_drilling_required ? 'Yes' : 'No'} · ${cicc.executive_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${execRows}</tbody></table>
    <h2 class="mc-section-title">${cicc.executive_kpi_cards.title}</h2>
    <p class="mc-bar-note">Always visible · links to detail · ${cicc.executive_kpi_cards.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>KPI</th><th>Current</th><th>Detail</th><th>Status</th></tr></thead>
      <tbody>${kpiRows}</tbody></table>
    <h2 class="mc-section-title">${cicc.arkansas_operations_map.title}</h2>
    <p class="mc-bar-note">Fullscreen · health color coding · ${cicc.arkansas_operations_map.status} · live: ${cicc.arkansas_operations_map.live ? 'Yes' : 'No'} · <a href="${cicc.arkansas_operations_map.route}">Civic Atlas</a></p>
    <ul class="mc-deliverables">${cicc.arkansas_operations_map.layers.map(l => `<li>${l}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cicc.department_operations_boards.title}</h2>
    <p class="mc-bar-note">Board fields: ${cicc.department_operations_boards.board_fields.join(' · ')}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Department</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${deptRows}</tbody></table>
    <h2 class="mc-section-title">${cicc.institutional_pulse.title}</h2>
    <p class="mc-bar-note">Measurable heartbeat: ${cicc.institutional_pulse.measurable_heartbeat ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Signal</th><th>Status</th><th>Note</th></tr></thead>
      <tbody>${pulseRows}</tbody></table>
    <h2 class="mc-section-title">${cicc.arkansas_growth_dashboard.title}</h2>
    <p class="mc-bar-note">Flagship dashboard · <a href="${cicc.arkansas_growth_dashboard.route}">Action Network →</a></p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Goal</th><th>Current</th><th>Target</th><th>Progress</th></tr></thead>
      <tbody>${growthRows}</tbody></table>
    <h2 class="mc-section-title">${cicc.executive_alerts.title}</h2>
    <p class="mc-bar-note">Proactive · priority by urgency · ${cicc.executive_alerts.active_alerts} active · ${cicc.executive_alerts.status}</p>
    <ul class="mc-deliverables">${cicc.executive_alerts.alert_types.map(a => `<li>${a.example}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cicc.opportunity_engine.title}</h2>
    <p class="mc-bar-note">${cicc.opportunity_engine.active_opportunities} active · ${cicc.opportunity_engine.status}</p>
    <ul class="mc-deliverables">${cicc.opportunity_engine.opportunity_types.map(o => `<li>${o.example}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cicc.weekly_executive_briefing.title}</h2>
    <p class="mc-bar-note">Auto-generated: ${cicc.weekly_executive_briefing.auto_generated ? 'Yes' : 'No'} · live: ${cicc.weekly_executive_briefing.live ? 'Yes' : 'No'} · ${cicc.weekly_executive_briefing.status}</p>
    <ul class="mc-deliverables">${cicc.weekly_executive_briefing.sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cicc.annual_state_of_civic_education.title}</h2>
    <p class="mc-bar-note">Signature publication · ${cicc.annual_state_of_civic_education.status}</p>
    <ul class="mc-deliverables">${cicc.annual_state_of_civic_education.sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cicc.ai_executive_advisor.title}</h2>
    <p class="mc-bar-note">Future · ${cicc.ai_executive_advisor.data_source} · <a href="${cicc.ai_executive_advisor.route}">Institutional AI</a></p>
    <ul class="mc-deliverables">${cicc.ai_executive_advisor.example_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cicc.executive_decision_log.title}</h2>
    <p class="mc-bar-note">${cicc.executive_decision_log.entries_from_builds} build entries · ${cicc.executive_decision_log.status}</p>
    <ul class="mc-deliverables">${cicc.executive_decision_log.preserves.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${idx.title}</h2>
    <p class="mc-bar-note">Overall: <strong>${idx.overall_score}%</strong> · ${idx.measures}</p>
    <table class="mc-table"><thead><tr><th>Category</th><th>Score</th><th>Status</th></tr></thead>
      <tbody>${readinessRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${cicc.integration.unifies} · Extends: ${cicc.integration.extends}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${cicc.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cicc.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cicc.recommended_next_build.number} — ${cicc.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cicc.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CIVIC_INTELLIGENCE_COMMAND_CENTER.md">MASTER_CIVIC_INTELLIGENCE_COMMAND_CENTER.md</a> ·
      <a href="/data/civic-intelligence-command-center.json">JSON</a> ·
      <a href="/mission-control/executive.html">MC 2.0 Executive</a> ·
      <a href="/mission-control/arkansas-action-network.html">Action Network</a> ·
      <a href="/mission-control/civic-atlas.html">Civic Atlas</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initSustainabilityStewardship() {
  const root = document.getElementById('mc-sustainability-stewardship-root');
  if (!root) return;

  const [ssRes, mcRes] = await Promise.all([
    fetch('/data/sustainability-stewardship.json'),
    fetch('/data/mission-control.json')
  ]);
  const ss = await ssRes.json();
  const mc = await mcRes.json();
  const s = ss.summary;

  const principleRows = ss.five_sustainability_principles.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.principle}</td><td>${p.test}</td><td>${p.status}</td></tr>`).join('');

  const fundingRows = ss.funding_portfolio.categories.map(f => `
    <tr><td><code>${f.id}</code></td><td>${f.category}</td><td>${f.sources}</td><td>${f.status}</td></tr>`).join('');

  const allocRows = ss.resource_allocation.areas.map(a => `
    <tr><td>${a.area}</td><td>${a.status}</td><td><a href="${a.route}">→</a></td></tr>`).join('');

  const volunteerRows = ss.volunteer_stewardship.metrics.map(v => `
    <tr><td><code>${v.id}</code></td><td>${v.metric}</td><td>${v.current}${v.unit ? ` ${v.unit}` : ''}</td><td>${v.status}</td></tr>`).join('');

  const dashboardRows = ss.sustainability_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td><td>${d.current}${d.unit ? ` ${d.unit}` : ''}</td>
      <td>${d.target ?? '—'}</td><td>${d.status}</td></tr>`).join('');

  const systemRows = ss.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td><td><a href="${sys.route}">→</a></td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Sustainability & Stewardship</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #66 · ${ss.title}</p>
      <h1>Building an Institution That Lasts</h1>
      <p class="mc-header__question">${ss.governing_principle}</p>
      <p class="mc-bar-note">${ss.purpose}</p>
      <p class="mc-bar-note"><strong>Core philosophy:</strong> ${ss.core_philosophy}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Stewardship readiness</div><div class="mc-stat__value">${s.sustainability_stewardship_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Funding sources</div><div class="mc-stat__value">${s.funding_sources_active}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Volunteers</div><div class="mc-stat__value">${s.volunteers_onboarded}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Reserve</div><div class="mc-stat__value">${s.operational_reserve}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Builds documented</div><div class="mc-stat__value">${s.documentation_builds}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Annual report</div><div class="mc-stat__value">${s.annual_report_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Five Sustainability Principles</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Principle</th><th>Test</th><th>Status</th></tr></thead>
      <tbody>${principleRows}</tbody></table>
    <h2 class="mc-section-title">${ss.funding_portfolio.title}</h2>
    <p class="mc-bar-note">Avoid single source: ${ss.funding_portfolio.avoid_single_source ? 'Yes' : 'No'} · ${ss.funding_portfolio.total_active_sources} active · ${ss.funding_portfolio.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Category</th><th>Sources</th><th>Status</th></tr></thead>
      <tbody>${fundingRows}</tbody></table>
    ${ss.funding_portfolio.categories.map(f => `<p class="mc-bar-note"><strong>${f.category}:</strong> ${f.description}</p>`).join('')}
    <h2 class="mc-section-title">${ss.financial_transparency.title}</h2>
    <p class="mc-bar-note">${ss.financial_transparency.balance} · report live: ${ss.financial_transparency.report_live ? 'Yes' : 'No'} · ${ss.financial_transparency.status}</p>
    <ul class="mc-deliverables">${ss.financial_transparency.annual_reporting_sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ss.resource_allocation.title}</h2>
    <table class="mc-table"><thead><tr><th>Area</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${allocRows}</tbody></table>
    <h2 class="mc-section-title">${ss.institutional_reserve.title}</h2>
    <p class="mc-bar-note">${ss.institutional_reserve.objective} · current: ${ss.institutional_reserve.current_reserve} · ${ss.institutional_reserve.status}</p>
    <h2 class="mc-section-title">${ss.volunteer_stewardship.title}</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${volunteerRows}</tbody></table>
    <h2 class="mc-section-title">${ss.knowledge_preservation.title}</h2>
    <p class="mc-bar-note">${ss.knowledge_preservation.principle} · ${ss.knowledge_preservation.builds_documented} builds documented</p>
    <ul class="mc-deliverables">${ss.knowledge_preservation.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ss.technology_sustainability.title}</h2>
    <p class="mc-bar-note">Version control: ${ss.technology_sustainability.version_control ? 'Yes' : 'No'} · GitHub: ${ss.technology_sustainability.github_connected ? 'connected' : '—'} · ${ss.technology_sustainability.status}</p>
    <ul class="mc-deliverables">${ss.technology_sustainability.requirements.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ss.leadership_sustainability.title}</h2>
    <p class="mc-bar-note">No single point of failure: ${ss.leadership_sustainability.no_single_point_of_failure ? 'Yes' : 'No'} · ${ss.leadership_sustainability.status}</p>
    <ul class="mc-deliverables">${ss.leadership_sustainability.elements.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ss.annual_sustainability_review.title}</h2>
    <p class="mc-bar-note">Auto-generated: ${ss.annual_sustainability_review.auto_generated ? 'Yes' : 'No'} · live: ${ss.annual_sustainability_review.live ? 'Yes' : 'No'} · ${ss.annual_sustainability_review.status}</p>
    <ul class="mc-deliverables">${ss.annual_sustainability_review.sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ss.sustainability_dashboard.title}</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${dashboardRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">Monitored with same rigor as: ${ss.integration.monitored_with_same_rigor_as}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${ss.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ss.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ss.recommended_next_build.number} — ${ss.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ss.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_SUSTAINABILITY_STEWARDSHIP.md">MASTER_SUSTAINABILITY_STEWARDSHIP.md</a> ·
      <a href="/data/sustainability-stewardship.json">JSON</a> ·
      <a href="/mission-control/governance.html">Governance</a> ·
      <a href="/mission-control/pmo.html">PMO</a> ·
      <a href="/mission-control/civic-intelligence-command-center.html">Command Center</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initImpactMeasurement() {
  const root = document.getElementById('mc-impact-measurement-root');
  if (!root) return;

  const [imRes, mcRes] = await Promise.all([
    fetch('/data/impact-measurement.json'),
    fetch('/data/mission-control.json')
  ]);
  const im = await imRes.json();
  const mc = await mcRes.json();
  const s = im.summary;
  const scorecard = im.arkansas_civic_scorecard;

  const pillarRows = im.five_impact_pillars.map(p => `
    <tr><td>${p.number}</td><td><code>${p.id}</code></td><td>${p.pillar}</td>
      <td>${p.primary_kpi}</td><td>${p.current}${p.unit ? ` ${p.unit}` : ''}</td><td>${p.status}</td>
      <td>${p.route ? `<a href="${p.route}">→</a>` : '—'}</td></tr>`).join('');

  const scoreRows = scorecard.indicators.map(ind => `
    <tr><td><code>${ind.id}</code></td><td>${ind.indicator}</td><td>${ind.current}${ind.unit ? ` ${ind.unit}` : ''}</td>
      <td>${ind.target ?? '—'}</td><td>${ind.status}</td></tr>`).join('');

  const widgetRows = im.impact_dashboard.widgets.map(w => `
    <tr><td><code>${w.id}</code></td><td>${w.widget}</td><td>${w.current}${w.unit ? ` ${w.unit}` : ''}</td><td>${w.status}</td></tr>`).join('');

  const systemRows = im.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Impact Measurement</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #67 · ${im.title}</p>
      <h1>Measuring What Actually Matters</h1>
      <p class="mc-header__question">${im.governing_principle}</p>
      <p class="mc-bar-note">${im.purpose}</p>
      <p class="mc-bar-note"><strong>Core philosophy:</strong> ${im.core_philosophy}</p>
      <p class="mc-bar-note"><strong>Measures understanding:</strong> ${im.measures_understanding_not_traffic ? 'Yes — not traffic' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Impact readiness</div><div class="mc-stat__value">${s.impact_measurement_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Arkansas Civic Score</div><div class="mc-stat__value">${s.overall_arkansas_civic_score}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pillars</div><div class="mc-stat__value">${s.pillars_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Leaders</div><div class="mc-stat__value">${s.education_leaders}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties</div><div class="mc-stat__value">${s.counties_represented}/75</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Connected</div><div class="mc-stat__value">${s.connected_arkansans}/${s.connected_target}</div></div>
    </div>
    <h2 class="mc-section-title">Five Impact Pillars</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Pillar</th><th>Primary KPI</th><th>Current</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${pillarRows}</tbody></table>
    ${im.five_impact_pillars.map(p => `
      <h3 class="mc-subsection-title">${p.pillar}</h3>
      <p class="mc-bar-note"><strong>Question:</strong> ${p.question}</p>
      <ul class="mc-deliverables">${p.tracks.map(t => `<li>${t}</li>`).join('')}</ul>`).join('')}
    <h2 class="mc-section-title">${scorecard.title}</h2>
    <p class="mc-bar-note">Overall score: <strong>${scorecard.overall_score}</strong> · published: ${scorecard.published ? 'Yes' : 'No'} · ${scorecard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Target</th><th>Status</th></tr></thead>
      <tbody>${scoreRows}</tbody></table>
    <h2 class="mc-section-title">${im.county_scorecards.title}</h2>
    <p class="mc-bar-note">${im.county_scorecards.scorecards_live}/${im.county_scorecards.counties_total} live · <a href="${im.county_scorecards.route}">Civic Atlas</a></p>
    <ul class="mc-deliverables">${im.county_scorecards.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${im.city_scorecards.title}</h2>
    <p class="mc-bar-note">${im.city_scorecards.scorecards_live}/${im.city_scorecards.cities_target} · compare over time: ${im.city_scorecards.compare_over_time_not_between ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${im.city_scorecards.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${im.leadership_scorecards.title}</h2>
    <p class="mc-bar-note">Personal growth, not competition: ${im.leadership_scorecards.personal_growth_not_competition ? 'Yes' : 'No'} · ${im.leadership_scorecards.scorecards_live} live</p>
    <ul class="mc-deliverables">${im.leadership_scorecards.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${im.annual_institutional_benchmarks.title}</h2>
    <ul class="mc-deliverables">${im.annual_institutional_benchmarks.periods.map(p => `<li>${p.period} — ${p.status}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${im.outcomes_over_outputs.title}</h2>
    <p class="mc-bar-note">${im.outcomes_over_outputs.principle}</p>
    ${im.outcomes_over_outputs.examples.map(e => `
      <p class="mc-bar-note"><strong>Output:</strong> ${e.output}<br><strong>Outcome:</strong> ${e.outcome}</p>`).join('')}
    <h2 class="mc-section-title">${im.community_feedback.title}</h2>
    <p class="mc-bar-note">${im.community_feedback.collected} collected · ${im.community_feedback.status}</p>
    <ul class="mc-deliverables">${im.community_feedback.types.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${im.impact_dashboard.title}</h2>
    <p class="mc-bar-note">Institutional report card: ${im.impact_dashboard.institutional_report_card ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Widget</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${widgetRows}</tbody></table>
    <h2 class="mc-section-title">${im.public_accountability.title}</h2>
    <p class="mc-bar-note">Live: ${im.public_accountability.live ? 'Yes' : 'No'} · ${im.public_accountability.status}</p>
    <ul class="mc-deliverables">${im.public_accountability.sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">ECS from: ${im.integration.ecs_from}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${im.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${im.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${im.recommended_next_build.number} — ${im.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${im.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_IMPACT_MEASUREMENT.md">MASTER_IMPACT_MEASUREMENT.md</a> ·
      <a href="/data/impact-measurement.json">JSON</a> ·
      <a href="/mission-control/civic-atlas.html">Civic Atlas</a> ·
      <a href="/mission-control/arkansas-action-network.html">Action Network</a> ·
      <a href="/mission-control/visitor-journey.html">Visitor Journey</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initCitizenLeadershipAcademy() {
  const root = document.getElementById('mc-citizen-leadership-academy-root');
  if (!root) return;

  const [claRes, mcRes] = await Promise.all([
    fetch('/data/citizen-leadership-academy.json'),
    fetch('/data/mission-control.json')
  ]);
  const cla = await claRes.json();
  const mc = await mcRes.json();
  const s = cla.summary;

  const levelRows = cla.six_certification_levels.map(l => `
    <tr><td>${l.level}</td><td><code>${l.id}</code></td><td>${l.title}</td>
      <td>${l.outcome}</td><td>${l.enrolled}</td><td>${l.status}</td>
      <td>${l.route ? `<a href="${l.route}">→</a>` : '—'}</td></tr>`).join('');

  const stageRows = cla.academy_philosophy.stages.map(st => `
    <tr><td>${st.stage}</td><td>${st.status}</td></tr>`).join('');

  const metricRows = cla.academy_dashboard.metrics.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td><td>${m.current}${m.unit ? ` ${m.unit}` : ''}</td><td>${m.status}</td></tr>`).join('');

  const systemRows = cla.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Citizen Leadership Academy</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #68 · ${cla.title}</p>
      <h1>Developing Arkansas's Civic Education Leaders</h1>
      <p class="mc-header__question">${cla.governing_principle}</p>
      <p class="mc-bar-note">${cla.purpose}</p>
      <p class="mc-bar-note"><strong>Human engine:</strong> ${cla.human_engine ? 'Yes' : 'No'} · <strong>Highest priority:</strong> ${cla.highest_strategic_priority ? 'Yes' : 'No'} · <strong>Teachers not spokespeople:</strong> ${cla.produces_teachers_not_spokespeople ? 'Yes' : 'No'}</p>
      <p class="mc-bar-note"><a href="${cla.legacy_academy_route}">Community Education Academy (#28) →</a></p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Academy readiness</div><div class="mc-stat__value">${s.citizen_leadership_academy_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Levels</div><div class="mc-stat__value">${s.certification_levels}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Learners</div><div class="mc-stat__value">${s.current_learners}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Graduates</div><div class="mc-stat__value">${s.graduates_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Education Leaders</div><div class="mc-stat__value">${s.education_leaders}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Mentorships</div><div class="mc-stat__value">${s.mentorship_relationships}</div></div>
    </div>
    <h2 class="mc-section-title">Academy Mission</h2>
    <ul class="mc-deliverables">${cla.academy_mission.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Academy Philosophy</h2>
    <p class="mc-bar-note">${cla.academy_philosophy.progression} · Every graduate develops future leaders: ${cla.academy_philosophy.every_graduate_develops_future_leaders ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>Stage</th><th>Status</th></tr></thead>
      <tbody>${stageRows}</tbody></table>
    <h2 class="mc-section-title">Six Certification Levels</h2>
    <table class="mc-table"><thead><tr><th>Level</th><th>ID</th><th>Title</th><th>Outcome</th><th>Enrolled</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${levelRows}</tbody></table>
    ${cla.six_certification_levels.map(l => `
      <h3 class="mc-subsection-title">Level ${l.level}: ${l.title}</h3>
      <p class="mc-bar-note">${l.purpose}</p>
      <ul class="mc-deliverables">${(l.topics || l.skills || []).map(t => `<li>${t}</li>`).join('')}</ul>
      <p class="mc-bar-note"><strong>Outcome:</strong> ${l.outcome}</p>`).join('')}
    <h2 class="mc-section-title">${cla.learning_model.title}</h2>
    <p class="mc-bar-note">Active not passive: ${cla.learning_model.active_not_passive ? 'Yes' : 'No'} · ${cla.learning_model.status}</p>
    <ul class="mc-deliverables">${cla.learning_model.steps.map(step => `<li>${step}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cla.leadership_competencies.title}</h2>
    <p class="mc-bar-note">Tracked over time: ${cla.leadership_competencies.tracked_over_time ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${cla.leadership_competencies.competencies.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cla.leadership_portfolio.title}</h2>
    <p class="mc-bar-note">Living portfolio: ${cla.leadership_portfolio.living_portfolio ? 'Yes' : 'No'} · ${cla.leadership_portfolio.portfolios_live} live · ${cla.leadership_portfolio.status}</p>
    <ul class="mc-deliverables">${cla.leadership_portfolio.contents.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cla.leadership_mentorship.title}</h2>
    <p class="mc-bar-note">Every graduate mentors: ${cla.leadership_mentorship.every_graduate_mentors ? 'Yes' : 'No'} · ${cla.leadership_mentorship.relationships} relationships · ${cla.leadership_mentorship.status}</p>
    <h2 class="mc-section-title">${cla.continuing_education.title}</h2>
    <p class="mc-bar-note">Never ends: ${cla.continuing_education.never_ends ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${cla.continuing_education.offerings.map(o => `<li>${o}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${cla.academy_dashboard.title}</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">${cla.graduation_commitment.title}</h2>
    <p class="mc-bar-note">Voluntary: ${cla.graduation_commitment.voluntary ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${cla.graduation_commitment.statements.map(st => `<li>${st}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${cla.integration.chain}</p>
    <p class="mc-bar-note">Extends: ${cla.integration.extends}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${cla.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${cla.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${cla.recommended_next_build.number} — ${cla.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${cla.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_CITIZEN_LEADERSHIP_ACADEMY.md">MASTER_CITIZEN_LEADERSHIP_ACADEMY.md</a> ·
      <a href="/data/citizen-leadership-academy.json">JSON</a> ·
      <a href="/mission-control/education-academy.html">Education Academy (#28)</a> ·
      <a href="/mission-control/arkansas-action-network.html">Action Network</a> ·
      <a href="/mission-control/impact-measurement.html">Impact Measurement</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initRelationalOrganizingGrowthEngine() {
  const root = document.getElementById('mc-relational-organizing-growth-engine-root');
  if (!root) return;

  const [rogRes, mcRes] = await Promise.all([
    fetch('/data/relational-organizing-growth-engine.json'),
    fetch('/data/mission-control.json')
  ]);
  const rog = await rogRes.json();
  const mc = await mcRes.json();
  const s = rog.summary;

  const trustRows = rog.core_philosophy.trust_chain.map((t, i) => `
    <tr><td>${i + 1}</td><td>${t}</td></tr>`).join('');

  const shareRows = rog.share_hub.shareable_items.map(item => `
    <tr><td>${item}</td><td>${rog.share_hub.status}</td></tr>`).join('');

  const healthRows = rog.relationship_health.indicators.map(h => `
    <tr><td><code>${h.id}</code></td><td>${h.indicator}</td><td>${h.current}</td><td>${h.status}</td></tr>`).join('');

  const systemRows = rog.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Relational Organizing Growth Engine</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #69 · ${rog.title}</p>
      <h1>The Network Effect — Trusted Relationships to 200,000</h1>
      <p class="mc-header__question">${rog.governing_principle}</p>
      <p class="mc-bar-note">${rog.purpose}</p>
      <p class="mc-bar-note"><strong>Primary expansion strategy:</strong> ${rog.primary_expansion_strategy ? 'Yes' : 'No'} · <strong>Not ads/SEO/social:</strong> ${rog.not_advertising_seo_social ? 'Yes' : 'No'}</p>
      <p class="mc-bar-note"><strong>Arkansas Growth Formula:</strong> "${rog.arkansas_growth_formula.question}"</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Growth engine readiness</div><div class="mc-stat__value">${s.relational_organizing_growth_engine_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Relationship trees</div><div class="mc-stat__value">${s.relationship_trees}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Invitations</div><div class="mc-stat__value">${s.total_invitations}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Share hub pages</div><div class="mc-stat__value">${s.share_hub_pages_wired}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Learning circles</div><div class="mc-stat__value">${s.learning_circles}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Connected</div><div class="mc-stat__value">${s.connected_arkansans}/${s.connected_target.toLocaleString()}</div></div>
    </div>
    <h2 class="mc-section-title">Core Philosophy — Trust Chain</h2>
    <p class="mc-bar-note">Knowledge spreads through relationships. Platform supports relationships: ${rog.core_philosophy.platform_supports_relationships ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>Relationship</th></tr></thead>
      <tbody>${trustRows}</tbody></table>
    <h2 class="mc-section-title">Arkansas Growth Formula</h2>
    <p class="mc-bar-note">Suggested invitations: ${rog.arkansas_growth_formula.suggested_invitations} · No pressure: ${rog.arkansas_growth_formula.no_pressure ? 'Yes' : 'No'} · No quotas: ${rog.arkansas_growth_formula.no_quotas ? 'Yes' : 'No'}</p>
    <h2 class="mc-section-title">Relationship Tree</h2>
    <p class="mc-bar-note">Voluntary: ${rog.relationship_tree.voluntary ? 'Yes' : 'No'} · ${rog.relationship_tree.example_branch}</p>
    <p class="mc-bar-note">Visualizes education not recruitment: ${rog.relationship_tree.visualizes_education_not_recruitment ? 'Yes' : 'No'} · Trees active: ${rog.relationship_tree.trees_active} · ${rog.relationship_tree.status}</p>
    <h2 class="mc-section-title">${rog.share_hub.title}</h2>
    <p class="mc-bar-note">Per-page panel: ${rog.share_hub.per_page_panel ? 'Yes' : 'No'} · Pages wired: ${rog.share_hub.pages_wired} · ${rog.share_hub.status}</p>
    <p class="mc-bar-note"><strong>Emphasis:</strong> "${rog.share_hub.emphasis}" · <strong>Not:</strong> "${rog.share_hub.not_emphasis}"</p>
    <table class="mc-table"><thead><tr><th>Shareable</th><th>Status</th></tr></thead>
      <tbody>${shareRows}</tbody></table>
    <h2 class="mc-section-title">${rog.family_learning.title}</h2>
    <p class="mc-bar-note">Intergenerational: ${rog.family_learning.intergenerational ? 'Yes' : 'No'} · ${rog.family_learning.status}</p>
    <ul class="mc-deliverables">${rog.family_learning.resources.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${rog.friend_neighbor_circles.title}</h2>
    <p class="mc-bar-note">Active circles: ${rog.friend_neighbor_circles.active_circles} · Local conversations: ${rog.friend_neighbor_circles.local_conversations ? 'Yes' : 'No'} · ${rog.friend_neighbor_circles.status}</p>
    <ul class="mc-deliverables">${rog.friend_neighbor_circles.circle_types.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${rog.organizational_referrals.title}</h2>
    <p class="mc-bar-note">Coalition tools: ${rog.organizational_referrals.coalition_tools ? 'Yes' : 'No'} · Referrals tracked: ${rog.organizational_referrals.referrals_tracked} · Privacy respecting: ${rog.organizational_referrals.privacy_respecting ? 'Yes' : 'No'} · ${rog.organizational_referrals.status}</p>
    <h2 class="mc-section-title">${rog.education_leader_referral_dashboard.title}</h2>
    <p class="mc-bar-note">Mentorship not competition: ${rog.education_leader_referral_dashboard.mentorship_not_competition ? 'Yes' : 'No'} · ${rog.education_leader_referral_dashboard.status}</p>
    <ul class="mc-deliverables">${rog.education_leader_referral_dashboard.fields.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${rog.referral_recognition.title}</h2>
    <p class="mc-bar-note">Focus: ${rog.referral_recognition.focus} · Milestones achieved: ${rog.referral_recognition.milestones_achieved} · ${rog.referral_recognition.status}</p>
    <ul class="mc-deliverables">${rog.referral_recognition.milestones.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${rog.relationship_health.title}</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${healthRows}</tbody></table>
    <h2 class="mc-section-title">${rog.privacy_principles.title}</h2>
    <p class="mc-bar-note">Trust outweighs growth: ${rog.privacy_principles.trust_outweighs_growth ? 'Yes' : 'No'} · ${rog.privacy_principles.status}</p>
    <ul class="mc-deliverables">${rog.privacy_principles.principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${rog.mc_visualization.title}</h2>
    <p class="mc-bar-note">Private info protected: ${rog.mc_visualization.private_info_protected ? 'Yes' : 'No'} · ${rog.mc_visualization.status}</p>
    <ul class="mc-deliverables">${rog.mc_visualization.layers.map(l => `<li>${l}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${rog.integration.chain}</p>
    <p class="mc-bar-note"><strong>Unifies:</strong> ${rog.integration.unifies}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${rog.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${rog.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${rog.recommended_next_build.number} — ${rog.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${rog.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_RELATIONAL_ORGANIZING_GROWTH_ENGINE.md">MASTER_RELATIONAL_ORGANIZING_GROWTH_ENGINE.md</a> ·
      <a href="/data/relational-organizing-growth-engine.json">JSON</a> ·
      <a href="/mission-control/neighborhood-organizing.html">Neighborhood Organizing</a> ·
      <a href="/mission-control/relationship-os.html">Relationship OS</a> ·
      <a href="/mission-control/arkansas-action-network.html">Action Network</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCommandStrategy() {
  const root = document.getElementById('mc-arkansas-command-strategy-root');
  if (!root) return;

  const [acsRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-command-strategy.json'),
    fetch('/data/mission-control.json')
  ]);
  const acs = await acsRes.json();
  const mc = await mcRes.json();
  const s = acs.summary;

  const objRows = acs.statewide_objectives.map(o => `
    <tr><td>${o.number}</td><td><code>${o.id}</code></td><td>${o.title}</td>
      <td>${o.current}/${o.target.toLocaleString()}</td><td>${o.status}</td></tr>`).join('');

  const phaseRows = acs.execution_phases.phases.map(p => `
    <tr><td>${p.phase}</td><td><code>${p.id}</code></td><td>${p.title}</td>
      <td>${p.status}</td></tr>`).join('');

  const countyStageRows = acs.county_readiness_model.stages.map(st => `
    <tr><td>${st.stage}</td><td>${st.title}</td><td>${st.counties_at_stage}</td></tr>`).join('');

  const cityStageRows = acs.city_readiness_model.stages.map(st => `
    <tr><td>${st.stage}</td><td>${st.title}</td><td>${st.cities_at_stage}</td></tr>`).join('');

  const monthlyRows = acs.monthly_operational_targets.targets.map(t => `
    <tr><td><code>${t.id}</code></td><td>${t.metric}</td><td>${t.current}${t.target ? `/${t.target}` : ''}</td><td>${t.status}</td></tr>`).join('');

  const regionRows = acs.regional_strategy.regions.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.title}</td><td>${r.regional_mentor}</td>
      <td>${r.county_leaders}</td><td>${r.city_leaders}</td><td>${r.status}</td></tr>`).join('');

  const dashRows = acs.growth_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td>
      <td>${typeof d.current === 'number' ? d.current.toLocaleString() : d.current}${d.unit ? d.unit : ''}${d.target ? `/${d.target.toLocaleString()}` : ''}</td>
      <td>${d.status}</td></tr>`).join('');

  const systemRows = acs.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Command Strategy</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #70 · ${acs.title}</p>
      <h1>The Road to 75 Counties, 250 Cities & 200,000 Arkansans</h1>
      <p class="mc-header__question">${acs.governing_principle}</p>
      <p class="mc-bar-note">${acs.purpose}</p>
      <p class="mc-bar-note"><strong>Central question:</strong> ${acs.central_question}</p>
      <p class="mc-bar-note"><strong>Not advertising/pressure/campaigning:</strong> ${acs.not_advertising_pressure_campaigning ? 'Yes' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Command readiness</div><div class="mc-stat__value">${s.arkansas_command_strategy_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties</div><div class="mc-stat__value">${s.counties_with_leaders}/${s.counties_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Cities</div><div class="mc-stat__value">${s.cities_with_leaders}/${s.cities_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Connected</div><div class="mc-stat__value">${s.connected_arkansans}/${s.connected_target.toLocaleString()}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Execution phase</div><div class="mc-stat__value">${s.current_execution_phase}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Regional mentors</div><div class="mc-stat__value">${s.regional_mentors}/${s.regions_target}</div></div>
    </div>
    <h2 class="mc-section-title">Three Statewide Objectives</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Objective</th><th>Progress</th><th>Status</th></tr></thead>
      <tbody>${objRows}</tbody></table>
    <h2 class="mc-section-title">${acs.expansion_pyramid.title}</h2>
    <p class="mc-bar-note">${acs.expansion_pyramid.principle} · ${acs.expansion_pyramid.status}</p>
    <ul class="mc-deliverables">${acs.expansion_pyramid.layers.map(l => `<li>${l}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acs.execution_phases.title}</h2>
    <p class="mc-bar-note">Current: Phase ${acs.execution_phases.current_phase} — ${acs.execution_phases.current_phase_title}</p>
    <table class="mc-table"><thead><tr><th>Phase</th><th>ID</th><th>Title</th><th>Status</th></tr></thead>
      <tbody>${phaseRows}</tbody></table>
    ${acs.execution_phases.phases.map(p => `
      <h3 class="mc-subsection-title">Phase ${p.phase}: ${p.title}</h3>
      ${p.objectives ? `<ul class="mc-deliverables">${p.objectives.map(o => `<li>${o}</li>`).join('')}</ul>` : ''}
      ${p.goal ? `<p class="mc-bar-note"><strong>Goal:</strong> ${p.goal}</p>` : ''}
      ${p.priority ? `<p class="mc-bar-note"><strong>Priority:</strong> ${p.priority}</p>` : ''}
      ${p.focus ? `<ul class="mc-deliverables">${p.focus.map(f => `<li>${f}</li>`).join('')}</ul>` : ''}
      ${p.success_metric ? `<p class="mc-bar-note"><strong>Success:</strong> ${p.success_metric}</p>` : ''}`).join('')}
    <h2 class="mc-section-title">${acs.county_readiness_model.title}</h2>
    <p class="mc-bar-note">Past Awareness: ${acs.county_readiness_model.counties_past_awareness} · ${acs.county_readiness_model.status}</p>
    <table class="mc-table"><thead><tr><th>Stage</th><th>Title</th><th>Counties</th></tr></thead>
      <tbody>${countyStageRows}</tbody></table>
    <h2 class="mc-section-title">${acs.city_readiness_model.title}</h2>
    <p class="mc-bar-note">Sustained activity: ${acs.city_readiness_model.cities_with_sustained_activity} · ${acs.city_readiness_model.status}</p>
    <table class="mc-table"><thead><tr><th>Stage</th><th>Title</th><th>Cities</th></tr></thead>
      <tbody>${cityStageRows}</tbody></table>
    <h2 class="mc-section-title">${acs.participant_growth_model.title}</h2>
    <p class="mc-bar-note">${acs.participant_growth_model.current}/${acs.participant_growth_model.target.toLocaleString()} · No single channel: ${acs.participant_growth_model.no_single_channel ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${acs.participant_growth_model.channels.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acs.monthly_operational_targets.title}</h2>
    <p class="mc-bar-note">Targets tracked: ${acs.monthly_operational_targets.targets_tracked} · ${acs.monthly_operational_targets.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${monthlyRows}</tbody></table>
    <h2 class="mc-section-title">${acs.regional_strategy.title}</h2>
    <p class="mc-bar-note">${acs.regional_strategy.regional_mentors}/${acs.regional_strategy.regions_total} mentors · ${acs.regional_strategy.status}</p>
    <ul class="mc-deliverables">${acs.regional_strategy.components.map(c => `<li>${c}</li>`).join('')}</ul>
    <table class="mc-table"><thead><tr><th>ID</th><th>Region</th><th>Mentor</th><th>County</th><th>City</th><th>Status</th></tr></thead>
      <tbody>${regionRows}</tbody></table>
    <h2 class="mc-section-title">${acs.arkansas_flywheel.title}</h2>
    <p class="mc-bar-note">${acs.arkansas_flywheel.principle} · ${acs.arkansas_flywheel.status}</p>
    <ul class="mc-deliverables">${acs.arkansas_flywheel.cycle.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acs.growth_dashboard.title}</h2>
    <p class="mc-bar-note">Primary statewide dashboard: ${acs.growth_dashboard.primary_statewide_dashboard ? 'Yes' : 'No'} · Live: ${acs.growth_dashboard.live ? 'Yes' : 'No'} · ${acs.growth_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">${acs.annual_goals.title}</h2>
    <p class="mc-bar-note">Maturity over raw growth: ${acs.annual_goals.maturity_over_raw_growth ? 'Yes' : 'No'} · ${acs.annual_goals.status}</p>
    <ul class="mc-deliverables">${acs.annual_goals.goals.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${acs.integration.chain}</p>
    <p class="mc-bar-note"><strong>Extends:</strong> ${acs.integration.extends}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${acs.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${acs.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${acs.recommended_next_build.number} — ${acs.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${acs.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_COMMAND_STRATEGY.md">MASTER_ARKANSAS_COMMAND_STRATEGY.md</a> ·
      <a href="/data/arkansas-command-strategy.json">JSON</a> ·
      <a href="/mission-control/statewide-growth.html">Statewide Growth</a> ·
      <a href="/mission-control/civic-atlas.html">Civic Atlas</a> ·
      <a href="/mission-control/arkansas-action-network.html">Action Network</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCommunityListening() {
  const root = document.getElementById('mc-arkansas-community-listening-root');
  if (!root) return;

  const [aclRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-community-listening.json'),
    fetch('/data/mission-control.json')
  ]);
  const acl = await aclRes.json();
  const mc = await mcRes.json();
  const s = acl.summary;

  const sourceRows = acl.listening_sources.sources.map(src => `
    <tr><td>${src.number}</td><td><code>${src.id}</code></td><td>${src.title}</td>
      <td>${src.submissions ?? src.reports_submitted ?? src.items_received ?? src.analyses_completed ?? src.recommendations_received ?? 0}</td>
      <td>${src.status}</td></tr>`).join('');

  const observatoryRows = acl.question_observatory.categories.map(c => `
    <tr><td><code>${c.id}</code></td><td>${c.category}</td><td>${c.count}</td><td>${c.status}</td></tr>`).join('');

  const dashRows = acl.community_listening_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td><td>${d.current}</td><td>${d.status}</td></tr>`).join('');

  const workflowRows = acl.listening_to_action_workflow.steps.map(st => `
    <tr><td>${st.step}</td><td>${st.title}</td><td>${st.items}</td><td>${st.status}</td></tr>`).join('');

  const pulseRows = acl.community_pulse_reports.report_types.map(p => `
    <tr><td><code>${p.id}</code></td><td>${p.type}</td><td>${p.reports_generated}</td><td>${p.status}</td></tr>`).join('');

  const systemRows = acl.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Community Listening</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #71 · ${acl.title}</p>
      <h1>Listening Before Leading — The Statewide Civic Listening Network</h1>
      <p class="mc-header__question">${acl.governing_principle}</p>
      <p class="mc-bar-note">${acl.purpose}</p>
      <p class="mc-bar-note"><strong>Operating principle:</strong> ${acl.operating_principle}</p>
      <p class="mc-bar-note"><strong>Listening as important as publishing:</strong> ${acl.listening_as_important_as_publishing ? 'Yes' : 'No'} · <strong>Learn from Arkansas:</strong> ${acl.learn_from_arkansas ? 'Yes' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Listening readiness</div><div class="mc-stat__value">${s.arkansas_community_listening_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Questions</div><div class="mc-stat__value">${s.questions_received}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Leader reports</div><div class="mc-stat__value">${s.education_leader_reports}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Public feedback</div><div class="mc-stat__value">${s.public_feedback_submissions}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pulse reports</div><div class="mc-stat__value">${s.pulse_reports_generated}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Listening sessions</div><div class="mc-stat__value">${s.listening_sessions_hosted}</div></div>
    </div>
    <h2 class="mc-section-title">${acl.listening_sources.title}</h2>
    <p class="mc-bar-note">${acl.listening_sources.sources_total} primary sources</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Source</th><th>Submissions</th><th>Status</th></tr></thead>
      <tbody>${sourceRows}</tbody></table>
    ${acl.listening_sources.sources.map(src => `
      <h3 class="mc-subsection-title">Source ${src.number}: ${src.title}</h3>
      ${src.channels ? `<ul class="mc-deliverables">${src.channels.map(c => `<li>${c}</li>`).join('')}</ul>` : ''}
      ${src.reports ? `<ul class="mc-deliverables">${src.reports.map(r => `<li>${r}</li>`).join('')}</ul>` : ''}
      ${src.feedback_areas ? `<ul class="mc-deliverables">${src.feedback_areas.map(f => `<li>${f}</li>`).join('')}</ul>` : ''}
      ${src.outputs ? `<ul class="mc-deliverables">${src.outputs.map(o => `<li>${o}</li>`).join('')}</ul>` : ''}
      ${src.suggestions ? `<ul class="mc-deliverables">${src.suggestions.map(sg => `<li>${sg}</li>`).join('')}</ul>` : ''}
      ${src.submission_types ? `<ul class="mc-deliverables">${src.submission_types.map(t => `<li>${t}</li>`).join('')}</ul>` : ''}
      ${src.role ? `<p class="mc-bar-note">${src.role}</p>` : ''}`).join('')}
    <h2 class="mc-section-title">${acl.question_observatory.title}</h2>
    <p class="mc-bar-note">Live: ${acl.question_observatory.live ? 'Yes' : 'No'} · Total questions: ${acl.question_observatory.total_questions} · Questions become content: ${acl.question_observatory.questions_become_content ? 'Yes' : 'No'} · ${acl.question_observatory.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Category</th><th>Count</th><th>Status</th></tr></thead>
      <tbody>${observatoryRows}</tbody></table>
    <h2 class="mc-section-title">${acl.educational_needs_mapping.title}</h2>
    <p class="mc-bar-note">Prioritizes resources: ${acl.educational_needs_mapping.prioritizes_resources ? 'Yes' : 'No'} · ${acl.educational_needs_mapping.status}</p>
    <ul class="mc-deliverables">${acl.educational_needs_mapping.patterns.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acl.community_listening_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${acl.community_listening_dashboard.live ? 'Yes' : 'No'} · ${acl.community_listening_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">${acl.listening_to_action_workflow.title}</h2>
    <p class="mc-bar-note">${acl.listening_to_action_workflow.principle} · ${acl.listening_to_action_workflow.status}</p>
    <table class="mc-table"><thead><tr><th>Step</th><th>Stage</th><th>Items</th><th>Status</th></tr></thead>
      <tbody>${workflowRows}</tbody></table>
    <h2 class="mc-section-title">${acl.community_pulse_reports.title}</h2>
    <p class="mc-bar-note">Reports generated: ${acl.community_pulse_reports.reports_generated} · Guides planning: ${acl.community_pulse_reports.guides_planning ? 'Yes' : 'No'} · ${acl.community_pulse_reports.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Type</th><th>Generated</th><th>Status</th></tr></thead>
      <tbody>${pulseRows}</tbody></table>
    <ul class="mc-deliverables">${acl.community_pulse_reports.content_areas.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acl.arkansas_civic_listening_tour.title}</h2>
    <p class="mc-bar-note">${acl.arkansas_civic_listening_tour.purpose} · Hosted by: ${acl.arkansas_civic_listening_tour.hosted_by} · Sessions: ${acl.arkansas_civic_listening_tour.sessions_hosted} · ${acl.arkansas_civic_listening_tour.status}</p>
    <ul class="mc-deliverables">${acl.arkansas_civic_listening_tour.topics.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${acl.integration.chain}</p>
    <p class="mc-bar-note">Improves every system: ${acl.integration.improves_every_system ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${acl.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${acl.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${acl.recommended_next_build.number} — ${acl.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${acl.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_COMMUNITY_LISTENING.md">MASTER_ARKANSAS_COMMUNITY_LISTENING.md</a> ·
      <a href="/data/arkansas-community-listening.json">JSON</a> ·
      <a href="/mission-control/research-observatory.html">Research Observatory</a> ·
      <a href="/mission-control/evidence-ledger.html">Evidence Ledger</a> ·
      <a href="/mission-control/citizen-action-center.html">Citizen Action Center</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCommunications() {
  const root = document.getElementById('mc-arkansas-communications-root');
  if (!root) return;

  const [acomRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-communications.json'),
    fetch('/data/mission-control.json')
  ]);
  const acom = await acomRes.json();
  const mc = await mcRes.json();
  const s = acom.summary;

  const objRows = acom.communication_objectives.objectives.map(o => `
    <tr><td>${o.number}</td><td><code>${o.id}</code></td><td>${o.title}</td>
      <td>${o.description}</td><td>${o.status}</td></tr>`).join('');

  const channelRows = acom.communication_channels.channels.map(ch => `
    <tr><td><code>${ch.id}</code></td><td>${ch.channel}</td><td>${ch.status}</td>
      <td>${ch.route ? `<a href="${ch.route}">→</a>` : '—'}</td></tr>`).join('');

  const dashRows = acom.communications_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td>
      <td>${typeof d.current === 'number' ? d.current.toLocaleString() : d.current}</td><td>${d.status}</td></tr>`).join('');

  const reviewRows = acom.communications_review_process.steps.map(st => `
    <tr><td>${st.step}</td><td>${st.title}</td><td>${st.items_passed}</td><td>${st.status}</td></tr>`).join('');

  const presRows = acom.presentation_system.formats.map(p => `
    <tr><td>${p.format}</td><td>${p.status}</td></tr>`).join('');

  const systemRows = acom.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Communications</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #72 · ${acom.title}</p>
      <h1>One Voice, Thousands of Conversations</h1>
      <p class="mc-header__question">${acom.governing_principle}</p>
      <p class="mc-bar-note">${acom.purpose}</p>
      <p class="mc-bar-note"><strong>Education before persuasion:</strong> ${acom.communications_philosophy.education_before_persuasion ? 'Yes' : 'No'} · <strong>Increase understanding:</strong> ${acom.communications_philosophy.increase_understanding_not_win_arguments ? 'Yes' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Communications readiness</div><div class="mc-stat__value">${s.arkansas_communications_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Articles</div><div class="mc-stat__value">${s.articles_published}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Videos</div><div class="mc-stat__value">${s.videos_released}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Emails sent</div><div class="mc-stat__value">${s.emails_sent}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Presentations</div><div class="mc-stat__value">${s.presentation_requests}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Press inquiries</div><div class="mc-stat__value">${s.press_inquiries}</div></div>
    </div>
    <h2 class="mc-section-title">Communications Philosophy</h2>
    <p class="mc-bar-note">Every communication answers:</p>
    <ul class="mc-deliverables">${acom.communications_philosophy.questions_every_communication_answers.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.institutional_voice.title}</h2>
    <p class="mc-bar-note">Trust through consistency: ${acom.institutional_voice.trust_through_consistency ? 'Yes' : 'No'} · ${acom.institutional_voice.status}</p>
    <ul class="mc-deliverables">${acom.institutional_voice.traits.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.communication_objectives.title}</h2>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Objective</th><th>Description</th><th>Status</th></tr></thead>
      <tbody>${objRows}</tbody></table>
    <h2 class="mc-section-title">${acom.communication_channels.title}</h2>
    <p class="mc-bar-note">Coordinated mission: ${acom.communication_channels.coordinated_mission ? 'Yes' : 'No'} · ${acom.communication_channels.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Channel</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${channelRows}</tbody></table>
    <h2 class="mc-section-title">${acom.content_pyramid.title}</h2>
    <p class="mc-bar-note">Multiple formats per topic: ${acom.content_pyramid.multiple_formats_per_topic ? 'Yes' : 'No'} · ${acom.content_pyramid.status}</p>
    <ul class="mc-deliverables">${acom.content_pyramid.layers.map(l => `<li>${l}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.editorial_calendar.title}</h2>
    <p class="mc-bar-note">Live: ${acom.editorial_calendar.live ? 'Yes' : 'No'} · Statewide: ${acom.editorial_calendar.statewide_calendar ? 'Yes' : 'No'} · ${acom.editorial_calendar.status}</p>
    <ul class="mc-deliverables">${acom.editorial_calendar.event_types.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.social_media_strategy.title}</h2>
    <p class="mc-bar-note">Return to institution for context: ${acom.social_media_strategy.return_to_institution_for_context ? 'Yes' : 'No'} · ${acom.social_media_strategy.status}</p>
    <ul class="mc-deliverables">${acom.social_media_strategy.purposes.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.email_communications.title}</h2>
    <p class="mc-bar-note">Educate before ask: ${acom.email_communications.educate_before_ask ? 'Yes' : 'No'} · Sent: ${acom.email_communications.emails_sent} · ${acom.email_communications.status}</p>
    <ul class="mc-deliverables">${acom.email_communications.series.map(srs => `<li>${srs}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.presentation_system.title}</h2>
    <p class="mc-bar-note">Standardized for leaders: ${acom.presentation_system.standardized_for_leaders ? 'Yes' : 'No'} · Requests: ${acom.presentation_system.requests} · ${acom.presentation_system.status}</p>
    <table class="mc-table"><thead><tr><th>Format</th><th>Status</th></tr></thead>
      <tbody>${presRows}</tbody></table>
    <h2 class="mc-section-title">${acom.media_response_framework.title}</h2>
    <p class="mc-bar-note">Educational resource role: ${acom.media_response_framework.educational_resource_role ? 'Yes' : 'No'} · Inquiries: ${acom.media_response_framework.press_inquiries} · ${acom.media_response_framework.status}</p>
    <ul class="mc-deliverables">${acom.media_response_framework.principles.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.storytelling_framework.title}</h2>
    <p class="mc-bar-note">${acom.storytelling_framework.status}</p>
    <ul class="mc-deliverables">${acom.storytelling_framework.story_types.map(st => `<li>${st}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acom.communications_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${acom.communications_dashboard.live ? 'Yes' : 'No'} · Educational reach not marketing: ${acom.communications_dashboard.educational_reach_not_marketing ? 'Yes' : 'No'} · ${acom.communications_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">${acom.communications_review_process.title}</h2>
    <p class="mc-bar-note">Quality before speed: ${acom.communications_review_process.quality_before_speed ? 'Yes' : 'No'} · Operational: ${acom.communications_review_process.operational ? 'Yes' : 'No'} · ${acom.communications_review_process.status}</p>
    <table class="mc-table"><thead><tr><th>Step</th><th>Stage</th><th>Passed</th><th>Status</th></tr></thead>
      <tbody>${reviewRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${acom.integration.chain}</p>
    <p class="mc-bar-note">Every system contributes: ${acom.integration.every_system_contributes ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${acom.long_term_voice_recognition}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${acom.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${acom.recommended_next_build.number} — ${acom.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${acom.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_COMMUNICATIONS.md">MASTER_ARKANSAS_COMMUNICATIONS.md</a> ·
      <a href="/data/arkansas-communications.json">JSON</a> ·
      <a href="/mission-control/content-factory.html">Content Factory</a> ·
      <a href="/mission-control/media-studio.html">Media Studio</a> ·
      <a href="/mission-control/narrative.html">Narrative Architecture</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasResearchInstitute() {
  const root = document.getElementById('mc-arkansas-research-institute-root');
  if (!root) return;

  const [ariRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-research-institute.json'),
    fetch('/data/mission-control.json')
  ]);
  const ari = await ariRes.json();
  const mc = await mcRes.json();
  const s = ari.summary;

  const divRows = ari.research_divisions.divisions.map(d => `
    <tr><td>${d.number}</td><td><code>${d.id}</code></td><td>${d.title}</td>
      <td>${d.projects}</td><td>${d.status}</td></tr>`).join('');

  const dashRows = ari.research_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td><td>${d.current}</td><td>${d.status}</td></tr>`).join('');

  const reviewRows = ari.research_review.workflow.map(st => `
    <tr><td>${st.step}</td><td>${st.title}</td><td>${st.items}</td><td>${st.status}</td></tr>`).join('');

  const systemRows = ari.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Research Institute</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #73 · ${ari.title}</p>
      <h1>From Education to Better Ideas</h1>
      <p class="mc-header__question">${ari.governing_principle}</p>
      <p class="mc-bar-note">${ari.purpose}</p>
      <p class="mc-bar-note"><strong>Permanent pillar:</strong> ${ari.permanent_institutional_pillar ? 'Yes' : 'No'} · <strong>Not predetermined advocacy:</strong> ${ari.not_advocacy_predetermined_answers ? 'Yes' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Institute readiness</div><div class="mc-stat__value">${s.arkansas_research_institute_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Projects</div><div class="mc-stat__value">${s.research_projects_underway}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">White papers</div><div class="mc-stat__value">${s.completed_white_papers}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Divisions</div><div class="mc-stat__value">${s.divisions_operational}/${s.research_divisions}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Policy comparisons</div><div class="mc-stat__value">${s.policy_comparisons}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Repository</div><div class="mc-stat__value">${s.repository_projects}</div></div>
    </div>
    <h2 class="mc-section-title">${ari.mission.title}</h2>
    <p class="mc-bar-note">Distinguishes: ${ari.mission.distinguishes.join(' · ')}</p>
    <ul class="mc-deliverables">${ari.mission.topics.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ari.research_philosophy.title}</h2>
    <p class="mc-bar-note">Begins with questions: ${ari.research_philosophy.begins_with_questions ? 'Yes' : 'No'} · Teaches evidence evaluation: ${ari.research_philosophy.teaches_evidence_evaluation ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${ari.research_philosophy.starter_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ari.research_divisions.title}</h2>
    <p class="mc-bar-note">Operational: ${ari.research_divisions.divisions_operational}/${ari.research_divisions.divisions_total}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Division</th><th>Projects</th><th>Status</th></tr></thead>
      <tbody>${divRows}</tbody></table>
    ${ari.research_divisions.divisions.map(d => `
      <h3 class="mc-subsection-title">Division ${d.number}: ${d.title}</h3>
      ${d.topics ? `<ul class="mc-deliverables">${d.topics.map(t => `<li>${t}</li>`).join('')}</ul>` : ''}
      ${d.work_types ? `<ul class="mc-deliverables">${d.work_types.map(w => `<li>${w}</li>`).join('')}</ul>` : ''}
      ${d.distinguishes ? `<p class="mc-bar-note"><strong>Distinguishes:</strong> ${d.distinguishes.join(' · ')}</p>` : ''}
      ${d.comparison_not_endorsement ? `<p class="mc-bar-note">Comparison, not endorsement</p>` : ''}
      ${d.educational_context ? `<p class="mc-bar-note">Educational context only</p>` : ''}
      ${d.improves_curriculum ? `<p class="mc-bar-note">Results improve curriculum</p>` : ''}`).join('')}
    <h2 class="mc-section-title">${ari.research_standards.title}</h2>
    <p class="mc-bar-note">Transparency strengthens credibility: ${ari.research_standards.transparency_strengthens_credibility ? 'Yes' : 'No'} · ${ari.research_standards.status}</p>
    <ul class="mc-deliverables">${ari.research_standards.required_elements.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ari.research_review.title}</h2>
    <p class="mc-bar-note">MC tracks every stage: ${ari.research_review.mc_tracks_every_stage ? 'Yes' : 'No'} · Operational: ${ari.research_review.operational ? 'Yes' : 'No'} · ${ari.research_review.status}</p>
    <table class="mc-table"><thead><tr><th>Step</th><th>Stage</th><th>Items</th><th>Status</th></tr></thead>
      <tbody>${reviewRows}</tbody></table>
    <h2 class="mc-section-title">${ari.research_repository.title}</h2>
    <p class="mc-bar-note">Permanent archive: ${ari.research_repository.permanent_archive ? 'Yes' : 'No'} · Projects: ${ari.research_repository.projects_archived} · ${ari.research_repository.status}</p>
    <ul class="mc-deliverables">${ari.research_repository.features.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${ari.research_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${ari.research_dashboard.live ? 'Yes' : 'No'} · ${ari.research_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${ari.integration.chain}</p>
    <p class="mc-bar-note">Supports every function: ${ari.integration.supports_every_function ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${ari.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${ari.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${ari.recommended_next_build.number} — ${ari.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${ari.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_RESEARCH_INSTITUTE.md">MASTER_ARKANSAS_RESEARCH_INSTITUTE.md</a> ·
      <a href="/data/arkansas-research-institute.json">JSON</a> ·
      <a href="/mission-control/research-observatory.html">Research Observatory</a> ·
      <a href="/mission-control/campaign-finance-observatory.html">Campaign Finance Observatory</a> ·
      <a href="/mission-control/evidence-ledger.html">Evidence Ledger</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCivicInnovationReform() {
  const root = document.getElementById('mc-arkansas-civic-innovation-reform-root');
  if (!root) return;

  const [acirRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-civic-innovation-reform.json'),
    fetch('/data/mission-control.json')
  ]);
  const acir = await acirRes.json();
  const mc = await mcRes.json();
  const s = acir.summary;

  const libRows = acir.reform_libraries.libraries.map(lib => `
    <tr><td>${lib.number}</td><td><code>${lib.id}</code></td><td>${lib.title}</td>
      <td>${lib.analyses ?? lib.submissions ?? 0}</td><td>${lib.status}</td></tr>`).join('');

  const dashRows = acir.reform_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td><td>${d.current}</td><td>${d.status}</td></tr>`).join('');

  const systemRows = acir.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Civic Innovation & Reform Center</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #74 · ${acir.title}</p>
      <h1>From Research to Responsible Reform</h1>
      <p class="mc-header__question">${acir.governing_principle}</p>
      <p class="mc-bar-note">${acir.purpose}</p>
      <p class="mc-bar-note"><strong>Signature resource:</strong> ${acir.signature_educational_resource ? 'Yes' : 'No'} · <strong>Not single-solution advocacy:</strong> ${acir.not_single_solution_advocacy ? 'Yes' : 'No'}</p>
      <p class="mc-bar-note"><strong>Center explains, citizens decide:</strong> ${acir.center_explains_citizens_decide ? 'Yes' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Reform center readiness</div><div class="mc-stat__value">${s.arkansas_civic_innovation_reform_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Analyses</div><div class="mc-stat__value">${s.reform_analyses_completed}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Libraries</div><div class="mc-stat__value">${s.libraries_operational}/${s.reform_libraries}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Comparative studies</div><div class="mc-stat__value">${s.comparative_studies}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Citizen lab</div><div class="mc-stat__value">${s.citizen_lab_submissions}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Solution builder</div><div class="mc-stat__value">${s.civic_solution_builder_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">${acir.mission.title}</h2>
    <ul class="mc-deliverables">${acir.mission.explains.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acir.institutional_philosophy.title}</h2>
    <p class="mc-bar-note">Same framework for every proposal: ${acir.institutional_philosophy.same_educational_framework ? 'Yes' : 'No'}</p>
    <ol class="mc-deliverables">${acir.institutional_philosophy.questions.map(q => `<li>${q}</li>`).join('')}</ol>
    <h2 class="mc-section-title">${acir.reform_libraries.title}</h2>
    <p class="mc-bar-note">Operational: ${acir.reform_libraries.libraries_operational}/${acir.reform_libraries.libraries_total}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Library</th><th>Items</th><th>Status</th></tr></thead>
      <tbody>${libRows}</tbody></table>
    ${acir.reform_libraries.libraries.map(lib => `
      <h3 class="mc-subsection-title">Library ${lib.number}: ${lib.title}</h3>
      ${lib.topics ? `<ul class="mc-deliverables">${lib.topics.map(t => `<li>${t}</li>`).join('')}</ul>` : ''}
      ${lib.submission_types ? `<ul class="mc-deliverables">${lib.submission_types.map(st => `<li>${st}</li>`).join('')}</ul>` : ''}
      ${lib.note ? `<p class="mc-bar-note">${lib.note}</p>` : ''}
      ${lib.no_institutional_policy ? `<p class="mc-bar-note">No proposal presented as institutional policy</p>` : ''}
      ${lib.comparative_education ? `<p class="mc-bar-note">Comparative education emphasis</p>` : ''}
      ${lib.editorial_review_before_public ? `<p class="mc-bar-note">Editorial review before public consideration</p>` : ''}`).join('')}
    <h2 class="mc-section-title">${acir.proposal_framework.title}</h2>
    <p class="mc-bar-note">Consistent structure: ${acir.proposal_framework.consistent_structure ? 'Yes' : 'No'} · ${acir.proposal_framework.status}</p>
    <ul class="mc-deliverables">${acir.proposal_framework.standardized_sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acir.civic_solution_builder.title}</h2>
    <p class="mc-bar-note">Live: ${acir.civic_solution_builder.live ? 'Yes' : 'No'} · Education not advocacy: ${acir.civic_solution_builder.education_not_advocacy ? 'Yes' : 'No'} · ${acir.civic_solution_builder.status}</p>
    <ul class="mc-deliverables">${acir.civic_solution_builder.capabilities.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acir.reform_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${acir.reform_dashboard.live ? 'Yes' : 'No'} · ${acir.reform_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${acir.integration.chain}</p>
    <p class="mc-bar-note">Grounded in documented research: ${acir.integration.grounded_in_documented_research ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${acir.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${acir.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${acir.recommended_next_build.number} — ${acir.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${acir.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_CIVIC_INNOVATION_REFORM.md">MASTER_ARKANSAS_CIVIC_INNOVATION_REFORM.md</a> ·
      <a href="/data/arkansas-civic-innovation-reform.json">JSON</a> ·
      <a href="/mission-control/arkansas-research-institute.html">Research Institute</a> ·
      <a href="/mission-control/campaign-finance-observatory.html">Campaign Finance Observatory</a> ·
      <a href="/mission-control/citizen-action-center.html">Citizen Action Center</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initVolunteerFundingConstitution() {
  const root = document.getElementById('mc-volunteer-funding-constitution-root');
  if (!root) return;

  const [vfcRes, mcRes] = await Promise.all([
    fetch('/data/volunteer-funding-constitution.json'),
    fetch('/data/mission-control.json')
  ]);
  const vfc = await vfcRes.json();
  const mc = await mcRes.json();
  const s = vfc.summary;

  const dashRows = vfc.constitution_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td>
      <td>${typeof d.current === 'number' ? d.current : d.current}${d.target ? `/${d.target}` : ''}</td><td>${d.status}</td></tr>`).join('');

  const systemRows = vfc.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Volunteer & Funding Constitution</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #75 · ${vfc.title}</p>
      <h1>The Institutional Independence Charter</h1>
      <p class="mc-header__question">${vfc.governing_principle}</p>
      <p class="mc-bar-note">${vfc.purpose}</p>
      <p class="mc-bar-note"><strong>All-volunteer institution:</strong> ${vfc.founding_principle.all_volunteer_arkansas_institution ? 'Yes' : 'No'} · <strong>Educate first and always:</strong> ${vfc.founding_principle.educate_first_and_always ? 'Yes' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Constitution readiness</div><div class="mc-stat__value">${s.volunteer_funding_constitution_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Active volunteers</div><div class="mc-stat__value">${s.active_volunteers}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Volunteer hours</div><div class="mc-stat__value">${s.volunteer_hours_reported}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Funding sources</div><div class="mc-stat__value">${s.funding_sources}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">County coverage</div><div class="mc-stat__value">${s.county_leadership_coverage}/${s.counties_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Adherence monitoring</div><div class="mc-stat__value">${s.adherence_monitoring_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">${vfc.volunteer_first.title}</h2>
    <p class="mc-bar-note">Designed for trained volunteers: ${vfc.volunteer_first.designed_for_trained_volunteers ? 'Yes' : 'No'} · Active: ${vfc.volunteer_first.active_volunteers} · ${vfc.volunteer_first.status}</p>
    <ul class="mc-deliverables">${vfc.volunteer_first.functions.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.financial_independence.title}</h2>
    <p class="mc-bar-note">Neutrality protected: ${vfc.financial_independence.neutrality_protected ? 'Yes' : 'No'} · Stewardship supports mission: ${vfc.financial_independence.stewardship_supports_mission_not_defines ? 'Yes' : 'No'}</p>
    <h2 class="mc-section-title">${vfc.arkansas_citizen_support.title}</h2>
    <p class="mc-bar-note"><strong>Preferred model:</strong> ${vfc.arkansas_citizen_support.preferred_model}</p>
    <p class="mc-bar-note">Funding sources: ${vfc.arkansas_citizen_support.funding_sources} · ${vfc.arkansas_citizen_support.status}</p>
    <ul class="mc-deliverables">${vfc.arkansas_citizen_support.when_necessary_for.map(u => `<li>${u}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.organizational_contributions.title}</h2>
    <p class="mc-bar-note">Distinguish collaboration from financial: ${vfc.organizational_contributions.distinguish_collaboration_from_financial ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${vfc.organizational_contributions.contribution_types.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.transparency.title}</h2>
    <p class="mc-bar-note">Public transparency: ${vfc.transparency.public_transparency ? 'Yes' : 'No'} · Revenue tracked: ${vfc.transparency.revenue_tracked}</p>
    <ul class="mc-deliverables">${vfc.transparency.internal_records.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.no_special_access.title}</h2>
    <p class="mc-bar-note">Integrity independent of support: ${vfc.no_special_access.integrity_independent_of_support ? 'Yes' : 'No'} · ${vfc.no_special_access.status}</p>
    <ul class="mc-deliverables">${vfc.no_special_access.contributions_never_purchase.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.stewardship_philosophy.title}</h2>
    <p class="mc-bar-note"><strong>Every dollar answers:</strong> "${vfc.stewardship_philosophy.question}"</p>
    <ul class="mc-deliverables">${vfc.stewardship_philosophy.examples.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.volunteer_recognition.title}</h2>
    <p class="mc-bar-note">Honors service not status: ${vfc.volunteer_recognition.honors_service_not_status ? 'Yes' : 'No'} · Milestones: ${vfc.volunteer_recognition.milestones_awarded} · ${vfc.volunteer_recognition.status}</p>
    <ul class="mc-deliverables">${vfc.volunteer_recognition.recognition_types.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.sustainability.title}</h2>
    <p class="mc-bar-note">Operate during limited resources: ${vfc.sustainability.operate_during_limited_resources ? 'Yes' : 'No'} · Resilience by design: ${vfc.sustainability.resilience_by_design ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${vfc.sustainability.requirements.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${vfc.constitution_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${vfc.constitution_dashboard.live ? 'Yes' : 'No'} · Adherence monitoring: ${vfc.constitution_dashboard.adherence_monitoring ? 'Yes' : 'No'} · ${vfc.constitution_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${vfc.integration.chain}</p>
    <p class="mc-bar-note"><strong>Extends:</strong> ${vfc.integration.extends}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${vfc.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${vfc.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${vfc.recommended_next_build.number} — ${vfc.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${vfc.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_VOLUNTEER_FUNDING_CONSTITUTION.md">MASTER_VOLUNTEER_FUNDING_CONSTITUTION.md</a> ·
      <a href="/data/volunteer-funding-constitution.json">JSON</a> ·
      <a href="/mission-control/sustainability-stewardship.html">Sustainability (#66)</a> ·
      <a href="/mission-control/governance.html">Governance</a> ·
      <a href="/mission-control/coalition-network.html">Coalition Network</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initOrganizationalConstitution() {
  const root = document.getElementById('mc-organizational-constitution-root');
  if (!root) return;

  const [ocRes, mcRes] = await Promise.all([
    fetch('/data/organizational-constitution.json'),
    fetch('/data/mission-control.json')
  ]);
  const oc = await ocRes.json();
  const mc = await mcRes.json();
  const s = oc.summary;

  const articleRows = oc.articles.items.map(a => `
    <tr><td>${a.article}</td><td><code>${a.id}</code></td><td>${a.title}</td>
      <td>${a.status}</td></tr>`).join('');

  const valueRows = oc.core_values.values.map(v => `
    <tr><td><code>${v.id}</code></td><td>${v.value}</td><td>${v.principle}</td></tr>`).join('');

  const deptRows = oc.organizational_structure.departments.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.department}</td>
      <td>${d.status}</td><td>${d.route ? `<a href="${d.route}">→</a>` : '—'}</td></tr>`).join('');

  const systemRows = oc.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  const mottoLines = oc.institutional_motto.lines.map(l => `<li><strong>${l}</strong></li>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Organizational Constitution</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #76 · ${oc.title}</p>
      <h1>${oc.subtitle}</h1>
      <p class="mc-header__question">${oc.purpose}</p>
      <p class="mc-bar-note"><strong>Platform:</strong> ${oc.platform} · <strong>Permanent founding framework:</strong> ${oc.permanent_founding_framework ? 'Yes' : 'No'}</p>
      <p class="mc-bar-note"><strong>Founder's principle:</strong> ${oc.founders_principle}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Constitution readiness</div><div class="mc-stat__value">${s.organizational_constitution_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Articles ratified</div><div class="mc-stat__value">${s.articles_ratified}/${s.articles_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Departments</div><div class="mc-stat__value">${s.departments_operational}/${s.departments_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Amendments</div><div class="mc-stat__value">${s.constitutional_amendments}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Core values</div><div class="mc-stat__value">${s.core_values}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Adherence monitoring</div><div class="mc-stat__value">${s.adherence_monitoring_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">Institutional Motto</h2>
    <ul class="mc-deliverables">${mottoLines}</ul>
    <h2 class="mc-section-title">Institutional Creed</h2>
    <ul class="mc-deliverables">${oc.institutional_creed.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.articles.title}</h2>
    <p class="mc-bar-note">Ratified: ${oc.articles.ratified}/${oc.articles.total}</p>
    <table class="mc-table"><thead><tr><th>#</th><th>ID</th><th>Article</th><th>Status</th></tr></thead>
      <tbody>${articleRows}</tbody></table>
    ${oc.articles.items.map(a => `
      <h3 class="mc-subsection-title">Article ${a.article}: ${a.title}</h3>
      <p class="mc-bar-note">${a.text}</p>`).join('')}
    <h2 class="mc-section-title">${oc.core_values.title}</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Value</th><th>Principle</th></tr></thead>
      <tbody>${valueRows}</tbody></table>
    <h2 class="mc-section-title">${oc.educational_commitment.title}</h2>
    <p class="mc-bar-note">Reduce confusion, not inflame controversy: ${oc.educational_commitment.reduce_confusion_not_inflame ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${oc.educational_commitment.commitments.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.organizational_structure.title}</h2>
    <p class="mc-bar-note">Operational: ${oc.organizational_structure.departments_operational}/${oc.organizational_structure.departments_total} · Additional departments allowed: ${oc.organizational_structure.additional_departments_allowed ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Department</th><th>Status</th><th>Route</th></tr></thead>
      <tbody>${deptRows}</tbody></table>
    <h2 class="mc-section-title">${oc.leadership.title}</h2>
    <p class="mc-bar-note">Leadership is stewardship: ${oc.leadership.stewardship ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${oc.leadership.responsibilities.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.volunteer_foundation.title}</h2>
    <p class="mc-bar-note">All-volunteer institution: ${oc.volunteer_foundation.all_volunteer_institution ? 'Yes' : 'No'} · Aligns with: ${oc.volunteer_foundation.aligns_with}</p>
    <ul class="mc-deliverables">${oc.volunteer_foundation.domains.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.financial_principles.title}</h2>
    <p class="mc-bar-note">Arkansas citizen contributions preferred: ${oc.financial_principles.arkansas_citizen_contributions_preferred ? 'Yes' : 'No'} · Independence preserved: ${oc.financial_principles.independence_preserved ? 'Yes' : 'No'} · Aligns with: ${oc.financial_principles.aligns_with}</p>
    <h2 class="mc-section-title">${oc.coalition.title}</h2>
    <p class="mc-bar-note">Organizations retain identity: ${oc.coalition.organizations_retain_identity ? 'Yes' : 'No'} · Evidence-based collaboration: ${oc.coalition.evidence_based_collaboration ? 'Yes' : 'No'}</p>
    <h2 class="mc-section-title">${oc.mission_control_article.title}</h2>
    <p class="mc-bar-note">Executive operating system: ${oc.mission_control_article.executive_operating_system ? 'Yes' : 'No'} · Enables informed stewardship: ${oc.mission_control_article.enables_informed_stewardship ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${oc.mission_control_article.monitors.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.research_standards.title}</h2>
    <p class="mc-bar-note">Continual improvement: ${oc.research_standards.continual_improvement ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${oc.research_standards.requirements.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.community_leadership.title}</h2>
    <p class="mc-bar-note">Multiplies civic education: ${oc.community_leadership.multiplies_civic_education ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${oc.community_leadership.ladder.map(l => `<li>${l}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.public_trust.title}</h2>
    <p class="mc-bar-note">Greatest asset: ${oc.public_trust.greatest_asset ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${oc.public_trust.pillars.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${oc.amendment_process.title}</h2>
    <p class="mc-bar-note">MC documents revisions: ${oc.amendment_process.mc_documents_revisions ? 'Yes' : 'No'} · Amendments recorded: ${oc.amendment_process.amendments_recorded} · ${oc.amendment_process.status}</p>
    <ul class="mc-deliverables">${oc.amendment_process.criteria.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${oc.integration.chain}</p>
    <p class="mc-bar-note"><strong>Everything flows from constitution:</strong> ${oc.integration.everything_flows_from_constitution ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${oc.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${oc.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${oc.recommended_next_build.number} — ${oc.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${oc.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ORGANIZATIONAL_CONSTITUTION.md">MASTER_ORGANIZATIONAL_CONSTITUTION.md</a> ·
      <a href="/data/organizational-constitution.json">JSON</a> ·
      <a href="/mission-control/governance.html">Governance (#49)</a> ·
      <a href="/mission-control/volunteer-funding-constitution.html">Volunteer & Funding (#75)</a> ·
      <a href="/mission-control/master-plan.html">Master Plan (#55)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCountyOperatingSystem() {
  const root = document.getElementById('mc-arkansas-county-operating-system-root');
  if (!root) return;

  const [acosRes, cciRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-county-operating-system.json'),
    fetch('/data/county-coalition-index.json'),
    fetch('/data/mission-control.json')
  ]);
  const acos = await acosRes.json();
  const cci = await cciRes.json();
  const mc = await mcRes.json();
  const s = acos.summary;

  const readinessRows = acos.county_readiness_levels.levels.map(l => `
    <tr><td>${l.level}</td><td><code>${l.id}</code></td><td>${l.title}</td>
      <td>${l.counties_at_level}</td></tr>`).join('');

  const profileRows = acos.county_profile.sections.map(sec => `
    <tr><td><code>${sec.id}</code></td><td>${sec.section}</td><td>${sec.status}</td></tr>`).join('');

  const roleRows = acos.county_leadership_team.roles.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.role}</td><td>${r.filled}</td><td>${r.status}</td></tr>`).join('');

  const dashRows = acos.county_dashboard.domains.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.domain}</td>
      <td>${d.indicators.join(', ')}</td><td>${d.status}</td></tr>`).join('');

  const systemRows = acos.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  const countySample = (cci.counties || []).slice(0, 12).map(c => `
    <tr><td>${c.name}</td><td><a href="${c.route}">${c.slug}</a></td>
      <td>${c.education_leaders}</td><td>${c.organizations}</td>
      <td>${c.completeness_pct}%</td><td>${c.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas County Operating System</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #77 · ${acos.title}</p>
      <h1>${acos.subtitle}</h1>
      <p class="mc-header__question">${acos.governing_principle}</p>
      <p class="mc-bar-note">${acos.purpose}</p>
      <p class="mc-bar-note"><strong>Extends:</strong> ${acos.integration.extends}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">ACOS readiness</div><div class="mc-stat__value">${s.arkansas_county_operating_system_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties</div><div class="mc-stat__value">${s.counties_scaffolded}/${s.counties_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Digital twins</div><div class="mc-stat__value">${s.counties_with_digital_twin}/${s.counties_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Past Awareness</div><div class="mc-stat__value">${s.counties_past_awareness}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Dashboards live</div><div class="mc-stat__value">${s.county_dashboards_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Health index</div><div class="mc-stat__value">${s.county_health_index_computed ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">${acos.county_philosophy.title}</h2>
    <p class="mc-bar-note">Every county a living system: ${acos.county_philosophy.every_county_living_system ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${acos.county_philosophy.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acos.county_digital_twin.title}</h2>
    <p class="mc-bar-note">${acos.county_digital_twin.description}</p>
    <p class="mc-bar-note">Operational: ${acos.county_digital_twin.digital_twins_operational}/${acos.county_digital_twin.counties_total} · MC generates all: ${acos.county_digital_twin.mc_generates_all ? 'Yes' : 'No'} · ${acos.county_digital_twin.status}</p>
    <h2 class="mc-section-title">${acos.county_profile.title} (${acos.county_profile.sections_total} sections)</h2>
    <table class="mc-table"><thead><tr><th>ID</th><th>Section</th><th>Status</th></tr></thead>
      <tbody>${profileRows}</tbody></table>
    <h2 class="mc-section-title">${acos.county_leadership_team.title}</h2>
    <p class="mc-bar-note">One volunteer, multiple roles initially: ${acos.county_leadership_team.one_volunteer_multiple_roles_initially ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Role</th><th>Filled</th><th>Status</th></tr></thead>
      <tbody>${roleRows}</tbody></table>
    <h2 class="mc-section-title">${acos.county_goals.title}</h2>
    <p class="mc-bar-note">Annual goals · MC tracks: ${acos.county_goals.mc_tracks_progress ? 'Yes' : 'No'} · ${acos.county_goals.status}</p>
    <ul class="mc-deliverables">${acos.county_goals.examples.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acos.county_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${acos.county_dashboard.live ? 'Yes' : 'No'} · ${acos.county_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Domain</th><th>Indicators</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">${acos.county_resource_library.title}</h2>
    <p class="mc-bar-note">Live: ${acos.county_resource_library.live ? 'Yes' : 'No'} · ${acos.county_resource_library.status}</p>
    <ul class="mc-deliverables">${acos.county_resource_library.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acos.county_event_calendar.title}</h2>
    <p class="mc-bar-note">Statewide sync: ${acos.county_event_calendar.statewide_calendar_sync ? 'Yes' : 'No'} · Live: ${acos.county_event_calendar.live ? 'Yes' : 'No'} · ${acos.county_event_calendar.status}</p>
    <ul class="mc-deliverables">${acos.county_event_calendar.event_types.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acos.county_listening_reports.title}</h2>
    <p class="mc-bar-note">Submitted: ${acos.county_listening_reports.reports_submitted} · MC aggregates statewide: ${acos.county_listening_reports.mc_aggregates_statewide ? 'Yes' : 'No'} · ${acos.county_listening_reports.status}</p>
    <ul class="mc-deliverables">${acos.county_listening_reports.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acos.county_readiness_levels.title}</h2>
    <p class="mc-bar-note">Past Awareness: ${acos.county_readiness_levels.counties_past_awareness} · MC visualizes all: ${acos.county_readiness_levels.mc_visualizes_all_counties ? 'Yes' : 'No'}</p>
    <p class="mc-bar-note">${acos.county_readiness_levels.note ?? ''}</p>
    <table class="mc-table"><thead><tr><th>Level</th><th>ID</th><th>Stage</th><th>Counties</th></tr></thead>
      <tbody>${readinessRows}</tbody></table>
    <h2 class="mc-section-title">${acos.county_health_index.title}</h2>
    <p class="mc-bar-note">Computed: ${acos.county_health_index.computed ? 'Yes' : 'No'} · ${acos.county_health_index.status}</p>
    <ul class="mc-deliverables">${acos.county_health_index.factors.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${acos.county_mentorship.title}</h2>
    <p class="mc-bar-note">Pairs active: ${acos.county_mentorship.pairs_active} · Collaboration not competition: ${acos.county_mentorship.collaboration_not_competition ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${acos.county_mentorship.types.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">75 Counties <a href="/coalition/counties.html" class="mc-inline-link">County map →</a></h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:280px;overflow-y:auto">
      <table class="mc-table"><thead><tr><th>County</th><th>Slug</th><th>Leaders</th><th>Orgs</th><th>Complete</th><th>Status</th></tr></thead>
        <tbody>${countySample}</tbody></table>
    </div>
    <p class="mc-bar-note">Showing 12 of ${s.counties_scaffolded} — full index in county-coalition-index.json</p>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${acos.integration.chain}</p>
    <p class="mc-bar-note"><strong>Each county operational node:</strong> ${acos.integration.each_county_operational_node ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${acos.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${acos.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${acos.recommended_next_build.number} — ${acos.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${acos.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_COUNTY_OPERATING_SYSTEM.md">MASTER_ARKANSAS_COUNTY_OPERATING_SYSTEM.md</a> ·
      <a href="/data/arkansas-county-operating-system.json">JSON</a> ·
      <a href="/mission-control/county-os.html">County OS (#31)</a> ·
      <a href="/mission-control/arkansas-command-strategy.html">Command Strategy (#70)</a> ·
      <a href="/mission-control/civic-atlas.html">Civic Atlas (#58)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCityOperatingSystem() {
  const root = document.getElementById('mc-arkansas-city-operating-system-root');
  if (!root) return;

  const [arcityRes, citiesRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-city-operating-system.json'),
    fetch('/data/arkansas-cities.json'),
    fetch('/data/mission-control.json')
  ]);
  const arcity = await arcityRes.json();
  const cities = await citiesRes.json();
  const mc = await mcRes.json();
  const s = arcity.summary;

  const readinessRows = arcity.city_readiness_levels.levels.map(l => `
    <tr><td>${l.level}</td><td><code>${l.id}</code></td><td>${l.title}</td>
      <td>${l.cities_at_level}</td></tr>`).join('');

  const twinRows = arcity.city_digital_twin.sections.map(sec => `
    <tr><td><code>${sec.id}</code></td><td>${sec.section}</td><td>${sec.status}</td></tr>`).join('');

  const roleRows = arcity.city_leadership_team.roles.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.role}</td><td>${r.filled}</td><td>${r.status}</td></tr>`).join('');

  const dashRows = arcity.city_dashboard.domains.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.domain}</td>
      <td>${d.indicators.join(', ')}</td><td>${d.status}</td></tr>`).join('');

  const systemRows = arcity.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  const citySample = (cities.cities || []).slice(0, 12).map(c => `
    <tr><td>${c.rank}</td><td>${c.name}</td><td>${c.population_estimate?.toLocaleString() ?? '—'}</td>
      <td>${c.education_leaders}</td><td>${c.coalition_orgs}</td><td>${c.status}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas City Operating System</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #78 · ${arcity.title}</p>
      <h1>${arcity.subtitle}</h1>
      <p class="mc-header__question">${arcity.governing_principle}</p>
      <p class="mc-bar-note">${arcity.purpose}</p>
      <p class="mc-bar-note"><strong>Bridge:</strong> county leadership ↔ neighborhood relationships</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">ArCOS readiness</div><div class="mc-stat__value">${s.arkansas_city_operating_system_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Cities</div><div class="mc-stat__value">${s.cities_scaffolded}/${s.cities_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Digital twins</div><div class="mc-stat__value">${s.cities_with_digital_twin}/${s.cities_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Past initial interest</div><div class="mc-stat__value">${s.cities_past_initial_interest}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Dashboards live</div><div class="mc-stat__value">${s.city_dashboards_live}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Health index</div><div class="mc-stat__value">${s.city_health_index_computed ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">${arcity.city_philosophy.title}</h2>
    <p class="mc-bar-note">Active learning community: ${arcity.city_philosophy.every_city_active_learning_community ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${arcity.city_philosophy.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${arcity.city_digital_twin.title}</h2>
    <p class="mc-bar-note">${arcity.city_digital_twin.description}</p>
    <p class="mc-bar-note">Operational: ${arcity.city_digital_twin.digital_twins_operational}/${arcity.city_digital_twin.cities_total} · ${arcity.city_digital_twin.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Section</th><th>Status</th></tr></thead>
      <tbody>${twinRows}</tbody></table>
    <h2 class="mc-section-title">${arcity.city_leadership_team.title}</h2>
    <p class="mc-bar-note">One person, multiple roles initially: ${arcity.city_leadership_team.one_person_multiple_roles_initially ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Role</th><th>Filled</th><th>Status</th></tr></thead>
      <tbody>${roleRows}</tbody></table>
    <h2 class="mc-section-title">${arcity.city_goals.title}</h2>
    <p class="mc-bar-note">Annual measurable objectives · MC tracks: ${arcity.city_goals.mc_tracks_progress ? 'Yes' : 'No'} · ${arcity.city_goals.status}</p>
    <ul class="mc-deliverables">${arcity.city_goals.examples.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${arcity.city_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${arcity.city_dashboard.live ? 'Yes' : 'No'} · ${arcity.city_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Domain</th><th>Indicators</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">${arcity.city_resource_center.title}</h2>
    <p class="mc-bar-note">Statewide consistent, local customization: ${arcity.city_resource_center.statewide_consistent_local_customization ? 'Yes' : 'No'} · Live: ${arcity.city_resource_center.live ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${arcity.city_resource_center.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${arcity.city_calendar.title}</h2>
    <p class="mc-bar-note">County/statewide sync: ${arcity.city_calendar.syncs_with_county_and_statewide ? 'Yes' : 'No'} · Live: ${arcity.city_calendar.live ? 'Yes' : 'No'} · ${arcity.city_calendar.status}</p>
    <ul class="mc-deliverables">${arcity.city_calendar.event_types.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${arcity.neighborhood_integration.title}</h2>
    <p class="mc-bar-note">Cities as neighborhood hubs: ${arcity.neighborhood_integration.cities_as_neighborhood_hubs ? 'Yes' : 'No'} · ${arcity.neighborhood_integration.status}</p>
    <ul class="mc-deliverables">${arcity.neighborhood_integration.visualizations.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${arcity.city_listening_reports.title}</h2>
    <p class="mc-bar-note">Submitted: ${arcity.city_listening_reports.reports_submitted} · MC aggregates statewide: ${arcity.city_listening_reports.mc_aggregates_statewide ? 'Yes' : 'No'} · ${arcity.city_listening_reports.status}</p>
    <ul class="mc-deliverables">${arcity.city_listening_reports.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${arcity.city_readiness_levels.title}</h2>
    <p class="mc-bar-note">Past initial interest: ${arcity.city_readiness_levels.cities_past_initial_interest} · MC displays all: ${arcity.city_readiness_levels.mc_displays_all_cities ? 'Yes' : 'No'}</p>
    <p class="mc-bar-note">${arcity.city_readiness_levels.note ?? ''}</p>
    <table class="mc-table"><thead><tr><th>Level</th><th>ID</th><th>Stage</th><th>Cities</th></tr></thead>
      <tbody>${readinessRows}</tbody></table>
    <h2 class="mc-section-title">${arcity.city_health_index.title}</h2>
    <p class="mc-bar-note">Computed: ${arcity.city_health_index.computed ? 'Yes' : 'No'} · ${arcity.city_health_index.status}</p>
    <ul class="mc-deliverables">${arcity.city_health_index.factors.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${arcity.city_collaboration.title}</h2>
    <p class="mc-bar-note">Pairs active: ${arcity.city_collaboration.pairs_active} · Horizontal spread: ${arcity.city_collaboration.horizontal_spread ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${arcity.city_collaboration.types.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">250 Largest Cities</h2>
    <div class="mc-card mc-inv-table-wrap" style="max-height:280px;overflow-y:auto">
      <table class="mc-table"><thead><tr><th>Rank</th><th>City</th><th>Population</th><th>Leaders</th><th>Orgs</th><th>Status</th></tr></thead>
        <tbody>${citySample}</tbody></table>
    </div>
    <p class="mc-bar-note">Showing 12 of ${s.cities_scaffolded} — full index in arkansas-cities.json</p>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${arcity.integration.chain}</p>
    <p class="mc-bar-note"><strong>Practical center of activity:</strong> ${arcity.integration.cities_practical_center_of_activity ? 'Yes' : 'No'} · <strong>County↔neighborhood bridge:</strong> ${arcity.integration.bridge_county_to_neighborhood ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${arcity.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${arcity.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${arcity.recommended_next_build.number} — ${arcity.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${arcity.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_CITY_OPERATING_SYSTEM.md">MASTER_ARKANSAS_CITY_OPERATING_SYSTEM.md</a> ·
      <a href="/data/arkansas-city-operating-system.json">JSON</a> ·
      <a href="/data/arkansas-cities.json">Cities Index</a> ·
      <a href="/mission-control/arkansas-county-operating-system.html">ACOS (#77)</a> ·
      <a href="/mission-control/neighborhood-organizing.html">Neighborhood (#57)</a> ·
      <a href="/mission-control/arkansas-command-strategy.html">Command Strategy (#70)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasNeighborhoodOperatingSystem() {
  const root = document.getElementById('mc-arkansas-neighborhood-operating-system-root');
  if (!root) return;

  const [anosRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-neighborhood-operating-system.json'),
    fetch('/data/mission-control.json')
  ]);
  const anos = await anosRes.json();
  const mc = await mcRes.json();
  const s = anos.summary;

  const profileRows = anos.neighborhood_profile.sections.map(sec => `
    <tr><td><code>${sec.id}</code></td><td>${sec.section}</td><td>${sec.status}</td></tr>`).join('');

  const roleRows = anos.neighborhood_leadership_team.roles.map(r => `
    <tr><td><code>${r.id}</code></td><td>${r.role}</td><td>${r.filled}</td><td>${r.status}</td></tr>`).join('');

  const growthRows = anos.neighborhood_growth_cycle.steps.map(step => `
    <tr><td>${step.step}</td><td><code>${step.id}</code></td><td>${step.title}</td>
      <td>${step.neighborhoods_at_step}</td></tr>`).join('');

  const systemRows = anos.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Neighborhood Operating System</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #79 · ${anos.title}</p>
      <h1>${anos.subtitle}</h1>
      <p class="mc-header__question">${anos.governing_principle}</p>
      <p class="mc-bar-note">${anos.purpose}</p>
      <p class="mc-bar-note"><strong>Final institutional layer:</strong> ${anos.final_institutional_layer ? 'Yes' : 'No'} · <strong>Extends:</strong> ${anos.integration.extends}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">ANOS readiness</div><div class="mc-stat__value">${s.arkansas_neighborhood_operating_system_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Profiles</div><div class="mc-stat__value">${s.neighborhood_profiles_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Digital twins</div><div class="mc-stat__value">${s.neighborhoods_with_digital_twin}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">With leaders</div><div class="mc-stat__value">${s.neighborhoods_with_leader}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Connected</div><div class="mc-stat__value">${s.connected_arkansans}/${s.participants_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Health score</div><div class="mc-stat__value">${s.neighborhood_health_score_computed ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">${anos.institutional_philosophy.title}</h2>
    <p class="mc-bar-note">Life happens in neighborhoods: ${anos.institutional_philosophy.life_happens_in_neighborhoods ? 'Yes' : 'No'} · Designed around trust: ${anos.institutional_philosophy.designed_around_trust ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${anos.institutional_philosophy.trusted_relationships.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_mission.title}</h2>
    <ul class="mc-deliverables">${anos.neighborhood_mission.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_profile.title}</h2>
    <p class="mc-bar-note">Private residential never public: ${anos.neighborhood_profile.private_residential_never_public ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Section</th><th>Status</th></tr></thead>
      <tbody>${profileRows}</tbody></table>
    <h2 class="mc-section-title">${anos.neighborhood_leadership_team.title}</h2>
    <p class="mc-bar-note">One volunteer, multiple roles: ${anos.neighborhood_leadership_team.one_volunteer_multiple_roles_initially ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Role</th><th>Filled</th><th>Status</th></tr></thead>
      <tbody>${roleRows}</tbody></table>
    <h2 class="mc-section-title">${anos.neighborhood_conversation_model.title}</h2>
    <p class="mc-bar-note">Intentionally small: ${anos.neighborhood_conversation_model.intentionally_small ? 'Yes' : 'No'} · Thoughtful discussion, not rallies: ${anos.neighborhood_conversation_model.thoughtful_discussion_not_rallies ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${anos.neighborhood_conversation_model.ideal_environments.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_learning_circles.title}</h2>
    <p class="mc-bar-note">Connected to verified resources: ${anos.neighborhood_learning_circles.connected_to_verified_resources ? 'Yes' : 'No'} · ${anos.neighborhood_learning_circles.status}</p>
    <ul class="mc-deliverables">${anos.neighborhood_learning_circles.resources.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_growth_cycle.title}</h2>
    <p class="mc-bar-note">MC visualizes growth: ${anos.neighborhood_growth_cycle.mc_visualizes_growth ? 'Yes' : 'No'} · ${anos.neighborhood_growth_cycle.status}</p>
    <table class="mc-table"><thead><tr><th>Step</th><th>ID</th><th>Stage</th><th>Neighborhoods</th></tr></thead>
      <tbody>${growthRows}</tbody></table>
    <h2 class="mc-section-title">${anos.neighborhood_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${anos.neighborhood_dashboard.live ? 'Yes' : 'No'} · Local operating center: ${anos.neighborhood_dashboard.local_operating_center ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${anos.neighborhood_dashboard.sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_health_score.title}</h2>
    <p class="mc-bar-note">Computed: ${anos.neighborhood_health_score.computed ? 'Yes' : 'No'} · ${anos.neighborhood_health_score.status}</p>
    <ul class="mc-deliverables">${anos.neighborhood_health_score.factors.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_resource_center.title}</h2>
    <ul class="mc-deliverables">${anos.neighborhood_resource_center.items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_mentorship.title}</h2>
    <p class="mc-bar-note">Trees live: ${anos.neighborhood_mentorship.trees_live ? 'Yes' : 'No'} · Pairs: ${anos.neighborhood_mentorship.pairs_active} · Multiplication growth: ${anos.neighborhood_mentorship.multiplication_growth ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${anos.neighborhood_mentorship.visualizations.map(v => `<li>${v}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.neighborhood_recognition.title}</h2>
    <p class="mc-bar-note">Milestones awarded: ${anos.neighborhood_recognition.milestones_awarded} · Service not competition: ${anos.neighborhood_recognition.reinforces_service_not_competition ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${anos.neighborhood_recognition.milestones.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${anos.two_hundred_k_strategy.title}</h2>
    <p class="mc-bar-note">Connected: ${anos.two_hundred_k_strategy.current_connected}/${anos.two_hundred_k_strategy.target} · Growth at neighborhood level: ${anos.two_hundred_k_strategy.growth_at_neighborhood_level ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${anos.two_hundred_k_strategy.leader_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${anos.integration.chain}</p>
    <p class="mc-bar-note"><strong>Every neighborhood connected node:</strong> ${anos.integration.every_neighborhood_connected_node ? 'Yes' : 'No'} · <strong>Final layer:</strong> ${anos.integration.final_layer_of_architecture ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${anos.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${anos.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${anos.recommended_next_build.number} — ${anos.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${anos.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_NEIGHBORHOOD_OPERATING_SYSTEM.md">MASTER_ARKANSAS_NEIGHBORHOOD_OPERATING_SYSTEM.md</a> ·
      <a href="/data/arkansas-neighborhood-operating-system.json">JSON</a> ·
      <a href="/data/neighborhood-profiles.json">Profiles Registry</a> ·
      <a href="/mission-control/neighborhood-organizing.html">Neighborhood Organizing (#57)</a> ·
      <a href="/mission-control/arkansas-city-operating-system.html">ArCOS (#78)</a> ·
      <a href="/mission-control/relational-organizing-growth-engine.html">Growth Engine (#69)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCivicInstitutionRoadmap() {
  const root = document.getElementById('mc-arkansas-civic-institution-roadmap-root');
  if (!root) return;

  const [legRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-civic-institution-roadmap.json'),
    fetch('/data/mission-control.json')
  ]);
  const leg = await legRes.json();
  const mc = await mcRes.json();
  const s = leg.summary;

  const goalRows = leg.twenty_year_goals.goals.map(g => `
    <tr><td><code>${g.id}</code></td><td>${g.goal}</td>
      <td>${g.current}${g.target ? `/${g.target}` : ''}</td><td>${g.status}</td></tr>`).join('');

  const eraCards = leg.four_eras.eras.map(e => `
    <div class="mc-card"><h3>Era ${e.era}: ${e.title}</h3>
      <p class="mc-bar-note"><strong>Focus:</strong> ${e.focus} · Status: ${e.status}</p>
      <ul class="mc-deliverables">${e.objectives.map(o => `<li>${o}</li>`).join('')}</ul></div>`).join('');

  const milestoneRows = leg.institutional_milestones.milestones.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.milestone}</td>
      <td>${m.achieved ? 'Yes' : 'No'}</td><td>${m.status}</td></tr>`).join('');

  const systemRows = leg.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Civic Institution Roadmap</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #80 · ${leg.title}</p>
      <h1>${leg.subtitle}</h1>
      <p class="mc-header__question">${leg.governing_principle}</p>
      <p class="mc-bar-note">${leg.purpose}</p>
      <p class="mc-bar-note"><strong>80 builds complete:</strong> ${leg.eighty_builds_blueprint_complete ? 'Yes' : 'No'} · <strong>Plans for legacy:</strong> ${leg.plans_for_legacy_not_launch ? 'Yes' : 'No'}</p>
      <p class="mc-bar-note"><strong>Founding vision:</strong> ${leg.founding_vision}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Legacy readiness</div><div class="mc-stat__value">${s.arkansas_civic_institution_roadmap_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Builds</div><div class="mc-stat__value">${s.builds_complete}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Current era</div><div class="mc-stat__value">${s.current_era} — ${s.current_era_title}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Milestones</div><div class="mc-stat__value">${s.milestones_achieved}/${s.milestones_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Connected</div><div class="mc-stat__value">${s.connected_arkansans}/${s.participants_target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Legacy map</div><div class="mc-stat__value">${s.legacy_map_live ? 'Live' : 'Planned'}</div></div>
    </div>
    <h2 class="mc-section-title">${leg.twenty_year_goals.title}</h2>
    <p class="mc-bar-note">Direction, not rigid deadlines: ${leg.twenty_year_goals.direction_not_rigid_deadlines ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Goal</th><th>Progress</th><th>Status</th></tr></thead>
      <tbody>${goalRows}</tbody></table>
    <h2 class="mc-section-title">${leg.four_eras.title}</h2>
    <p class="mc-bar-note">Current era: ${leg.four_eras.current_era}</p>
    <div class="mc-grid-2">${eraCards}</div>
    <h2 class="mc-section-title">${leg.institutional_milestones.title}</h2>
    <p class="mc-bar-note">Achieved: ${leg.institutional_milestones.achieved_count} · MC celebrates: ${leg.institutional_milestones.mc_celebrates ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Milestone</th><th>Achieved</th><th>Status</th></tr></thead>
      <tbody>${milestoneRows}</tbody></table>
    <h2 class="mc-section-title">${leg.legacy_projects.title}</h2>
    <p class="mc-bar-note">Started: ${leg.legacy_projects.projects_started} · Preserve knowledge: ${leg.legacy_projects.preserve_knowledge_for_future_generations ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${leg.legacy_projects.projects.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${leg.leadership_legacy.title}</h2>
    <p class="mc-bar-note">Every generation prepares next: ${leg.leadership_legacy.every_generation_prepares_next ? 'Yes' : 'No'} · Never one individual: ${leg.leadership_legacy.never_depend_on_one_individual ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${leg.leadership_legacy.practices.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${leg.research_legacy.title}</h2>
    <p class="mc-bar-note">Future scholars build upon work: ${leg.research_legacy.future_scholars_build_upon_work ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${leg.research_legacy.future_collections.map(c => `<li>${c}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${leg.community_legacy.title}</h2>
    <p class="mc-bar-note">Woven into civic life: ${leg.community_legacy.woven_into_arkansas_civic_life ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${leg.community_legacy.partners.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${leg.technology_legacy.title}</h2>
    <p class="mc-bar-note">Mission constant: ${leg.technology_legacy.educational_mission_constant ? 'Yes' : 'No'} · Adaptable: ${leg.technology_legacy.remain_adaptable ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${leg.technology_legacy.mc_regularly_reviews.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${leg.annual_institutional_reflection.title}</h2>
    <p class="mc-bar-note">Conducted: ${leg.annual_institutional_reflection.conducted ? 'Yes' : 'No'} · ${leg.annual_institutional_reflection.status}</p>
    <ul class="mc-deliverables">${leg.annual_institutional_reflection.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${leg.arkansas_civic_legacy_map.title}</h2>
    <p class="mc-bar-note">Live: ${leg.arkansas_civic_legacy_map.live ? 'Yes' : 'No'} · ${leg.arkansas_civic_legacy_map.status}</p>
    <ul class="mc-deliverables">${leg.arkansas_civic_legacy_map.sections.map(sec => `<li>${sec}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${leg.measure_of_success.title}</h2>
    <p class="mc-bar-note"><strong>Not judged by:</strong></p>
    <ul class="mc-deliverables">${leg.measure_of_success.not_judged_by.map(n => `<li>${n}</li>`).join('')}</ul>
    <p class="mc-bar-note"><strong>True measures:</strong></p>
    <ul class="mc-deliverables">${leg.measure_of_success.true_measures.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Founder's Reflection</h2>
    <p class="mc-bar-note">${leg.founders_reflection}</p>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${leg.integration.chain}</p>
    <p class="mc-bar-note"><strong>MC compares to vision:</strong> ${leg.integration.mc_compares_current_to_vision ? 'Yes' : 'No'} · <strong>Extends:</strong> ${leg.integration.extends}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${leg.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${leg.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${leg.recommended_next_build.number} — ${leg.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${leg.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_CIVIC_INSTITUTION_ROADMAP.md">MASTER_ARKANSAS_CIVIC_INSTITUTION_ROADMAP.md</a> ·
      <a href="/data/arkansas-civic-institution-roadmap.json">JSON</a> ·
      <a href="/mission-control/institutional-roadmap.html">Institutional Roadmap (#44)</a> ·
      <a href="/mission-control/organizational-constitution.html">Constitution (#76)</a> ·
      <a href="/mission-control/master-plan.html">Master Plan (#55)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initInstitutionalDigitalTwin() {
  const root = document.getElementById('mc-institutional-digital-twin-root');
  if (!root) return;

  const [dtRes, mcRes] = await Promise.all([
    fetch('/data/institutional-digital-twin.json'),
    fetch('/data/mission-control.json')
  ]);
  const dt = await dtRes.json();
  const mc = await mcRes.json();
  const s = dt.summary;

  const questionRows = dt.institutional_philosophy.questions.map(q => `
    <tr><td>${q.question}</td><td>${q.intelligence}</td><td>${q.status}</td></tr>`).join('');

  const systemRows = dt.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Institutional Digital Twin</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #81 · ${dt.title}</p>
      <h1>${dt.subtitle}</h1>
      <p class="mc-header__question">${dt.governing_principle}</p>
      <p class="mc-bar-note">${dt.purpose}</p>
      <p class="mc-bar-note"><strong>Reporting → Planning:</strong> ${dt.transforms_mc_to_planning_system ? 'Yes' : 'No'}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Twin readiness</div><div class="mc-stat__value">${s.institutional_digital_twin_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Twin live</div><div class="mc-stat__value">${s.digital_twin_live ? 'Yes' : 'No'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Simulations</div><div class="mc-stat__value">${s.simulations_run}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Heat map</div><div class="mc-stat__value">${s.heat_map_live ? 'Live' : 'Planned'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Decision support</div><div class="mc-stat__value">${s.decision_support_live ? 'Live' : 'Planned'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Real-time mirror</div><div class="mc-stat__value">${s.realtime_mirror ? 'Yes' : 'No'}</div></div>
    </div>
    <h2 class="mc-section-title">${dt.institutional_philosophy.title}</h2>
    <table class="mc-table"><thead><tr><th>Question</th><th>Intelligence</th><th>Status</th></tr></thead>
      <tbody>${questionRows}</tbody></table>
    <h2 class="mc-section-title">${dt.institutional_model.title}</h2>
    <p class="mc-bar-note">${dt.institutional_model.chain}</p>
    <p class="mc-bar-note">Continuous updates: ${dt.institutional_model.continuous_updates ? 'Yes' : 'No'} · ${dt.institutional_model.status}</p>
    <ul class="mc-deliverables">${dt.institutional_model.systems.map(sys => `<li>${sys}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.executive_simulation.title}</h2>
    <p class="mc-bar-note">Run: ${dt.executive_simulation.simulations_run} · ${dt.executive_simulation.status}</p>
    <ul class="mc-deliverables">${dt.executive_simulation.what_if_scenarios.map(sc => `<li>${sc}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.county_simulation.title}</h2>
    <p class="mc-bar-note">Twins connected: ${dt.county_simulation.twins_connected} · ${dt.county_simulation.status}</p>
    <ul class="mc-deliverables">${dt.county_simulation.dimensions.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.city_simulation.title}</h2>
    <p class="mc-bar-note">Twins connected: ${dt.city_simulation.twins_connected} · Predictable: ${dt.city_simulation.predictable_not_reactive ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${dt.city_simulation.dimensions.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.neighborhood_simulation.title}</h2>
    <p class="mc-bar-note">Twins connected: ${dt.neighborhood_simulation.twins_connected}</p>
    <ul class="mc-deliverables">${dt.neighborhood_simulation.dimensions.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.leadership_pipeline_forecasting.title}</h2>
    <ul class="mc-deliverables">${dt.leadership_pipeline_forecasting.forecasts.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.research_forecasting.title}</h2>
    <ul class="mc-deliverables">${dt.research_forecasting.monitors.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.coalition_forecasting.title}</h2>
    <ul class="mc-deliverables">${dt.coalition_forecasting.models.map(m => `<li>${m}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.technology_forecasting.title}</h2>
    <ul class="mc-deliverables">${dt.technology_forecasting.tracks.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.institutional_health_forecast.title}</h2>
    <p class="mc-bar-note">${dt.institutional_health_forecast.status}</p>
    <ul class="mc-deliverables">${dt.institutional_health_forecast.indicators.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.arkansas_statewide_heat_map.title}</h2>
    <p class="mc-bar-note">Flagship view: ${dt.arkansas_statewide_heat_map.flagship_mc_view ? 'Yes' : 'No'} · Live: ${dt.arkansas_statewide_heat_map.live ? 'Yes' : 'No'} · ${dt.arkansas_statewide_heat_map.status}</p>
    <ul class="mc-deliverables">${dt.arkansas_statewide_heat_map.layers.map(l => `<li>${l}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.decision_support_engine.title}</h2>
    <p class="mc-bar-note">Live: ${dt.decision_support_engine.live ? 'Yes' : 'No'} · ${dt.decision_support_engine.status}</p>
    <ul class="mc-deliverables">${dt.decision_support_engine.factors.map(f => `<li>${f}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${dt.historical_replay.title}</h2>
    <p class="mc-bar-note">Live: ${dt.historical_replay.live ? 'Yes' : 'No'} · ${dt.historical_replay.status}</p>
    <ul class="mc-deliverables">${dt.historical_replay.examples.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${dt.integration.chain}</p>
    <p class="mc-bar-note"><strong>Connects everything:</strong> ${dt.integration.institutional_model_connects_everything ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${dt.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${dt.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${dt.recommended_next_build.number} — ${dt.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${dt.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_INSTITUTIONAL_DIGITAL_TWIN.md">MASTER_INSTITUTIONAL_DIGITAL_TWIN.md</a> ·
      <a href="/data/institutional-digital-twin.json">JSON</a> ·
      <a href="/mission-control/civic-atlas.html">Civic Atlas (#58)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initPublicTrustInstitutionalCredibility() {
  const root = document.getElementById('mc-public-trust-institutional-credibility-root');
  if (!root) return;

  const [ptRes, mcRes] = await Promise.all([
    fetch('/data/public-trust-institutional-credibility.json'),
    fetch('/data/mission-control.json')
  ]);
  const pt = await ptRes.json();
  const mc = await mcRes.json();
  const s = pt.summary;

  const pyramidCards = pt.trust_pyramid.layers.map(l => `
    <div class="mc-card"><h3>Layer ${l.layer}: ${l.title}</h3>
      <p class="mc-bar-note">Status: ${l.status}</p>
      <ul class="mc-deliverables">${l.principles.map(p => `<li>${p}</li>`).join('')}</ul></div>`).join('');

  const dashRows = pt.public_trust_dashboard.indicators.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.indicator}</td>
      <td>${typeof d.current === 'number' ? `${d.current}${d.unit ?? ''}` : d.current}</td><td>${d.status}</td></tr>`).join('');

  const systemRows = pt.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Public Trust Framework</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #82 · ${pt.title}</p>
      <h1>${pt.subtitle}</h1>
      <p class="mc-header__question">${pt.governing_principle}</p>
      <p class="mc-bar-note">${pt.purpose}</p>
      <p class="mc-bar-note"><strong>Trust is greatest asset:</strong> ${pt.trust_is_greatest_asset ? 'Yes' : 'No'} · <strong>Extends:</strong> ${pt.integration.extends}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Trust readiness</div><div class="mc-stat__value">${s.public_trust_institutional_credibility_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Pyramid layers</div><div class="mc-stat__value">${s.trust_pyramid_layers}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Dashboard live</div><div class="mc-stat__value">${s.trust_dashboard_live ? 'Yes' : 'No'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Corrections</div><div class="mc-stat__value">${s.corrections_completed}/${s.correction_requests}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Citations</div><div class="mc-stat__value">${s.citation_completeness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Annual audit</div><div class="mc-stat__value">${s.annual_trust_audit_conducted ? 'Done' : 'Pending'}</div></div>
    </div>
    <h2 class="mc-section-title">${pt.foundational_principle.title}</h2>
    <p class="mc-bar-note">Answer before asked: ${pt.foundational_principle.answer_before_asked ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${pt.foundational_principle.questions.map(q => `<li>${q}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${pt.trust_pyramid.title}</h2>
    <div class="mc-grid-2">${pyramidCards}</div>
    <h2 class="mc-section-title">${pt.public_trust_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${pt.public_trust_dashboard.live ? 'Yes' : 'No'} · ${pt.public_trust_dashboard.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Indicator</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${dashRows}</tbody></table>
    <h2 class="mc-section-title">${pt.page_trust_indicators.title}</h2>
    <p class="mc-bar-note">Quietly displayed: ${pt.page_trust_indicators.quietly_displayed ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${pt.page_trust_indicators.indicators.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${pt.trust_review_process.title}</h2>
    <ol class="mc-deliverables">${pt.trust_review_process.steps.map(step => `<li>${step}</li>`).join('')}</ol>
    <h2 class="mc-section-title">${pt.annual_trust_audit.title}</h2>
    <p class="mc-bar-note">Conducted: ${pt.annual_trust_audit.conducted ? 'Yes' : 'No'} · Public report: ${pt.annual_trust_audit.public_trust_report ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${pt.annual_trust_audit.domains.map(d => `<li>${d}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${pt.independent_review.title}</h2>
    <p class="mc-bar-note">Reviews: ${pt.independent_review.reviews_completed}</p>
    <ul class="mc-deliverables">${pt.independent_review.areas.map(a => `<li>${a}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${pt.public_questions.title}</h2>
    <p class="mc-bar-note">Logged: ${pt.public_questions.questions_logged} · Transparent log: ${pt.public_questions.transparent_log ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${pt.public_questions.log_types.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${pt.crisis_response.title}</h2>
    <p class="mc-bar-note">Documented: ${pt.crisis_response.responses_documented}</p>
    <ol class="mc-deliverables">${pt.crisis_response.steps.map(step => `<li>${step}</li>`).join('')}</ol>
    <h2 class="mc-section-title">${pt.founders_standard.title}</h2>
    <p class="mc-bar-note">${pt.founders_standard.text}</p>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${pt.integration.chain}</p>
    <p class="mc-bar-note"><strong>Connective tissue:</strong> ${pt.integration.trust_as_connective_tissue ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${pt.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${pt.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${pt.recommended_next_build.number} — ${pt.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${pt.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_PUBLIC_TRUST_INSTITUTIONAL_CREDIBILITY.md">MASTER_PUBLIC_TRUST_INSTITUTIONAL_CREDIBILITY.md</a> ·
      <a href="/data/public-trust-institutional-credibility.json">JSON</a> ·
      <a href="/mission-control/governance.html">Governance (#49)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasCivicEcosystem() {
  const root = document.getElementById('mc-arkansas-civic-ecosystem-root');
  if (!root) return;

  const [ecoRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-civic-ecosystem.json'),
    fetch('/data/mission-control.json')
  ]);
  const eco = await ecoRes.json();
  const mc = await mcRes.json();
  const s = eco.summary;

  const systemCards = eco.living_systems.systems.map(sys => `
    <div class="mc-card"><h3>System ${sys.system}: ${sys.title}</h3>
      <p class="mc-bar-note"><strong>Role:</strong> ${sys.role} · Status: ${sys.status}</p>
      <p class="mc-bar-note"><a href="${sys.route}">Dashboard →</a>${sys.note ? ` · ${sys.note}` : ''}</p>
      <p class="mc-bar-note"><strong>Feeds:</strong></p>
      <ul class="mc-deliverables">${sys.feeds.map(f => `<li>${f}</li>`).join('')}</ul></div>`).join('');

  const loopCards = eco.ecosystem_loops.loops.map(loop => `
    <div class="mc-card"><h3>${loop.title}</h3>
      <p class="mc-bar-note">${loop.outcome}</p>
      <ol class="mc-deliverables">${loop.steps.map(step => `<li>${step}</li>`).join('')}</ol></div>`).join('');

  const healthRows = eco.ecosystem_health_score.dimensions.map(d => `
    <tr><td><code>${d.id}</code></td><td>${d.dimension}</td>
      <td>${d.score}</td><td>${d.status}</td></tr>`).join('');

  const dashPanels = eco.executive_ecosystem_dashboard.panels.map(p => `<li>${p}</li>`).join('');

  const systemRows = eco.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td><td>${sys.note ?? '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Civic Ecosystem</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #83 · ${eco.title}</p>
      <h1>${eco.subtitle}</h1>
      <p class="mc-header__question">${eco.governing_principle}</p>
      <p class="mc-bar-note">${eco.purpose}</p>
      <p class="mc-bar-note"><strong>Core question:</strong> ${eco.ecosystem_philosophy.core_question}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Ecosystem readiness</div><div class="mc-stat__value">${s.arkansas_civic_ecosystem_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Living systems</div><div class="mc-stat__value">${s.living_systems_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Instrumented</div><div class="mc-stat__value">${s.living_systems_instrumented}/${s.living_systems_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Health score</div><div class="mc-stat__value">${s.ecosystem_health_score_live ? s.overall_ecosystem_health : 'Not live'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Participants</div><div class="mc-stat__value">${s.participants_connected.toLocaleString()}/${s.participants_target.toLocaleString()}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Imbalances</div><div class="mc-stat__value">${s.imbalances_detected}</div></div>
    </div>
    <h2 class="mc-section-title">${eco.ecosystem_philosophy.title}</h2>
    <p class="mc-bar-note">Departments → ecosystems: ${eco.ecosystem_philosophy.departments_to_ecosystems ? 'Yes' : 'No'}</p>
    <h2 class="mc-section-title">${eco.living_systems.title}</h2>
    <p class="mc-bar-note">Permanently connected: ${eco.living_systems.permanently_connected ? 'Yes' : 'No'} · Nothing in isolation: ${eco.living_systems.nothing_in_isolation ? 'Yes' : 'No'}</p>
    <div class="mc-grid-2">${systemCards}</div>
    <h2 class="mc-section-title">${eco.ecosystem_loops.title}</h2>
    <div class="mc-grid-2">${loopCards}</div>
    <h2 class="mc-section-title">${eco.arkansas_learning_loop.title}</h2>
    <ol class="mc-deliverables">${eco.arkansas_learning_loop.steps.map(step => `<li>${step}</li>`).join('')}</ol>
    <p class="mc-bar-note">Permanently adaptive: ${eco.arkansas_learning_loop.permanently_adaptive ? 'Yes' : 'No'}</p>
    <h2 class="mc-section-title">${eco.ecosystem_health_score.title}</h2>
    <p class="mc-bar-note">Live: ${eco.ecosystem_health_score.live ? 'Yes' : 'No'} · Computed: ${eco.ecosystem_health_score.computed ? 'Yes' : 'No'} · Overall: ${eco.ecosystem_health_score.overall_score}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Dimension</th><th>Score</th><th>Status</th></tr></thead>
      <tbody>${healthRows}</tbody></table>
    <h2 class="mc-section-title">${eco.positive_network_effects.title}</h2>
    <p class="mc-bar-note"><strong>Example:</strong> ${eco.positive_network_effects.example}</p>
    <ol class="mc-deliverables">${eco.positive_network_effects.chain.map(step => `<li>${step}</li>`).join('')}</ol>
    <h2 class="mc-section-title">${eco.ecosystem_balance.title}</h2>
    <p class="mc-bar-note">Imbalances detected: ${eco.ecosystem_balance.imbalances_detected}</p>
    <ul class="mc-deliverables">${eco.ecosystem_balance.examples.map(e => `<li>${e}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${eco.executive_ecosystem_dashboard.title}</h2>
    <p class="mc-bar-note">Live: ${eco.executive_ecosystem_dashboard.live ? 'Yes' : 'No'} · One screen: ${eco.executive_ecosystem_dashboard.one_screen_summarizes_institution ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${dashPanels}</ul>
    <h2 class="mc-section-title">${eco.founders_vision.title}</h2>
    <p class="mc-bar-note">${eco.founders_vision.text}</p>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">${eco.integration.chain}</p>
    <p class="mc-bar-note"><strong>Extends:</strong> ${eco.integration.extends} · <strong>Unifies:</strong> Builds ${eco.integration.unifies_builds}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Note</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${eco.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${eco.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${eco.recommended_next_build.number} — ${eco.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${eco.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_CIVIC_ECOSYSTEM.md">MASTER_ARKANSAS_CIVIC_ECOSYSTEM.md</a> ·
      <a href="/data/arkansas-civic-ecosystem.json">JSON</a> ·
      <a href="/mission-control/civic-ecosystem.html">Civic Ecosystem (#12)</a> ·
      <a href="/mission-control/systems-integration.html">Systems Integration (#45)</a> ·
      <a href="/mission-control/public-trust-institutional-credibility.html">Public Trust (#82)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}

async function initArkansasStrategicPlan2035() {
  const root = document.getElementById('mc-arkansas-strategic-plan-2035-root');
  if (!root) return;

  const [spRes, mcRes] = await Promise.all([
    fetch('/data/arkansas-strategic-plan-2035.json'),
    fetch('/data/mission-control.json')
  ]);
  const sp = await spRes.json();
  const mc = await mcRes.json();
  const s = sp.summary;

  const goalCards = sp.strategic_goals.goals.map(g => `
    <div class="mc-card"><h3>Goal ${g.goal}: ${g.title}</h3>
      <p class="mc-bar-note">${g.description} · Status: ${g.status}</p>
      <ul class="mc-deliverables">${g.initiatives.map(i => `<li>${i}</li>`).join('')}</ul></div>`).join('');

  const metricRows = sp.strategic_metrics.scorecard.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.metric}</td>
      <td>${typeof m.current === 'number' ? m.current.toLocaleString() : m.current}${m.target ? ` / ${m.target.toLocaleString()}` : ''}</td>
      <td>${m.status}</td></tr>`).join('');

  const fiveYearRows = sp.five_year_milestones.milestones.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.milestone}</td>
      <td>${m.achieved ? 'Yes' : 'No'}</td><td>${m.status}</td></tr>`).join('');

  const tenYearRows = sp.ten_year_milestones.milestones.map(m => `
    <tr><td><code>${m.id}</code></td><td>${m.milestone}</td>
      <td>${m.achieved ? 'Yes' : 'No'}</td><td>${m.status}</td></tr>`).join('');

  const systemRows = sp.integration.systems.map(sys => `
    <tr><td>${sys.system}</td><td>${sys.status}</td>
      <td><a href="${sys.route}">→</a></td>
      <td>${sys.goals ? `Goals ${sys.goals.join(', ')}` : '—'}</td></tr>`).join('');

  root.innerHTML = `
    <nav class="breadcrumb mc-breadcrumb"><a href="/mission-control/">Mission Control</a> → Arkansas Strategic Plan 2035</nav>
    <header class="mc-header">
      <p class="mc-header__eyebrow">Build #84 · ${sp.title}</p>
      <h1>${sp.subtitle}</h1>
      <p class="mc-header__question">${sp.governing_principle}</p>
      <p class="mc-bar-note">${sp.purpose}</p>
      <p class="mc-bar-note"><strong>Horizon:</strong> ${sp.horizon_year} · <strong>Tagline:</strong> ${sp.tagline}</p>
      <p class="mc-bar-note"><strong>Build Plan:</strong> ${sp.distinct_from_build_plan.build_plan_focus} · <strong>This plan:</strong> ${sp.distinct_from_build_plan.strategic_plan_focus}</p>
    </header>
    <div class="mc-executive mc-executive--hero">
      <div class="mc-stat"><div class="mc-stat__label">Strategic readiness</div><div class="mc-stat__value">${s.arkansas_strategic_plan_2035_readiness_pct}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Strategic goals</div><div class="mc-stat__value">${s.strategic_goals_total}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Scorecard live</div><div class="mc-stat__value">${s.strategic_scorecard_live ? 'Yes' : 'No'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Counties</div><div class="mc-stat__value">${s.counties_active}/75</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Participants</div><div class="mc-stat__value">${s.participants_connected.toLocaleString()}/${s.participants_target.toLocaleString()}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">5yr milestones</div><div class="mc-stat__value">${s.five_year_milestones_achieved}/${s.five_year_milestones_total}</div></div>
    </div>
    <h2 class="mc-section-title">${sp.strategic_vision.title}</h2>
    <p class="mc-bar-note">Horizon ${sp.strategic_vision.horizon}: ${sp.strategic_vision.aspiration}</p>
    <ul class="mc-deliverables">${sp.strategic_vision.topics.map(t => `<li>${t}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${sp.strategic_mission.title}</h2>
    <ul class="mc-deliverables">${sp.strategic_mission.pillars.map(p => `<li>${p}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${sp.strategic_goals.title}</h2>
    <div class="mc-grid-2">${goalCards}</div>
    <h2 class="mc-section-title">${sp.strategic_metrics.title}</h2>
    <p class="mc-bar-note">Live: ${sp.strategic_metrics.live ? 'Yes' : 'No'} · ${sp.strategic_metrics.status}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Metric</th><th>Current</th><th>Status</th></tr></thead>
      <tbody>${metricRows}</tbody></table>
    <h2 class="mc-section-title">${sp.five_year_milestones.title}</h2>
    <p class="mc-bar-note">Achieved: ${sp.five_year_milestones.achieved_count} · MC updates annually: ${sp.five_year_milestones.mc_updates_annually ? 'Yes' : 'No'}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Milestone</th><th>Achieved</th><th>Status</th></tr></thead>
      <tbody>${fiveYearRows}</tbody></table>
    <h2 class="mc-section-title">${sp.ten_year_milestones.title}</h2>
    <p class="mc-bar-note">Horizon: ${sp.ten_year_milestones.horizon} · Achieved: ${sp.ten_year_milestones.achieved_count}</p>
    <table class="mc-table"><thead><tr><th>ID</th><th>Milestone</th><th>Achieved</th><th>Status</th></tr></thead>
      <tbody>${tenYearRows}</tbody></table>
    <h2 class="mc-section-title">${sp.strategic_risks.title}</h2>
    <p class="mc-bar-note">MC monitors continually: ${sp.strategic_risks.mc_monitors_continually ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${sp.strategic_risks.risks.map(r => `<li>${r}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${sp.strategic_opportunities.title}</h2>
    <ul class="mc-deliverables">${sp.strategic_opportunities.opportunities.map(o => `<li>${o}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${sp.annual_strategic_review.title}</h2>
    <p class="mc-bar-note">Conducted: ${sp.annual_strategic_review.conducted ? 'Yes' : 'No'} · Living document: ${sp.annual_strategic_review.living_document ? 'Yes' : 'No'}</p>
    <ul class="mc-deliverables">${sp.annual_strategic_review.review_items.map(i => `<li>${i}</li>`).join('')}</ul>
    <h2 class="mc-section-title">${sp.founders_commitment.title}</h2>
    <p class="mc-bar-note">${sp.founders_commitment.text}</p>
    <h2 class="mc-section-title">System Integration</h2>
    <p class="mc-bar-note">Every major system advances at least one strategic goal.</p>
    <p class="mc-bar-note"><strong>Aligns with:</strong> ${sp.integration.aligns_with.join(' · ')}</p>
    <table class="mc-table"><thead><tr><th>System</th><th>Status</th><th>Route</th><th>Goals</th></tr></thead>
      <tbody>${systemRows}</tbody></table>
    <h2 class="mc-section-title">Long-Term Vision</h2>
    <p class="mc-bar-note">${sp.long_term_vision}</p>
    <h2 class="mc-section-title">Catalog Gaps</h2>
    <ul class="mc-deliverables">${sp.catalog_gaps.map(g => `<li>${g}</li>`).join('')}</ul>
    <h2 class="mc-section-title">Recommended: Build #${sp.recommended_next_build.number} — ${sp.recommended_next_build.title}</h2>
    <p class="mc-bar-note">${sp.recommended_next_build.note}</p>
    <p class="mc-bar-note">
      <a href="/docs/MASTER_ARKANSAS_STRATEGIC_PLAN_2035.md">MASTER_ARKANSAS_STRATEGIC_PLAN_2035.md</a> ·
      <a href="/data/arkansas-strategic-plan-2035.json">JSON</a> ·
      <a href="/BUILD_PLAN.md">Master Build Plan</a> ·
      <a href="/mission-control/arkansas-civic-ecosystem.html">Civic Ecosystem (#83)</a> ·
      <a href="/mission-control/arkansas-civic-institution-roadmap.html">Legacy Roadmap (#80)</a> ·
      <a href="/mission-control/">← Mission Control</a>
    </p>`;

  initDevConsole(mc);
}
