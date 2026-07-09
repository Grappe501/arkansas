/**
 * Citizens Facts — Mission Control OS v1.6.0
 */

function pctBar(label, value, colorClass = 'green') {
  const blocks = Math.round(value / 5);
  const bar = '█'.repeat(Math.min(blocks, 20)) + '░'.repeat(Math.max(0, 20 - blocks));
  return `
    <div class="mc-bar-row">
      <div class="mc-bar-row__header">
        <span class="mc-bar-row__label">${label}</span>
        <span class="mc-bar-row__pct">${value}%</span>
      </div>
      <div class="mc-bar" title="${bar}">
        <div class="mc-bar__fill mc-bar__fill--${colorClass}" style="width:${value}%"></div>
      </div>
    </div>`;
}

function statusDot(status) {
  const map = { complete: 'complete', building: 'building', planning: 'planning', not_started: 'not_started', testing: 'building' };
  return `<span class="mc-status-dot mc-status-dot--${map[status] || 'not_started'}"></span>`;
}

function renderExecutive(ex) {
  return `
    <div class="mc-executive">
      <div class="mc-stat"><div class="mc-stat__label">Overall Completion</div><div class="mc-stat__value mc-stat__value--highlight">${ex.overall_completion}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Last Build</div><div class="mc-stat__value">#${ex.last_build.number} ${ex.last_build.title}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Repository</div><div class="mc-stat__value mc-stat__value--highlight">${ex.repository.status === 'connected' ? 'GitHub Connected' : '—'}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Deployment</div><div class="mc-stat__value mc-stat__value--highlight">Netlify ${ex.deployment.status}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Content Pages</div><div class="mc-stat__value">${ex.content_pages.complete} / ${ex.content_pages.target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Research Complete</div><div class="mc-stat__value">${ex.research_complete}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Data Visualizations</div><div class="mc-stat__value">${ex.data_visualizations.complete} / ${ex.data_visualizations.target}</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Action Platform</div><div class="mc-stat__value">${ex.action_platform}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Testing</div><div class="mc-stat__value mc-stat__value--warn">${ex.testing}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Volunteer Pipeline</div><div class="mc-stat__value">${ex.volunteer_pipeline}%</div></div>
      <div class="mc-stat"><div class="mc-stat__label">Today's Goal</div><div class="mc-stat__value" style="font-size:0.95rem">${ex.todays_goal}</div></div>
    </div>`;
}

function renderBriefing(b, ex) {
  return `
    <section class="mc-briefing">
      <h2>☀ Daily Mission Briefing — ${new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' })}</h2>
      <ul>
        <li><strong>Yesterday:</strong> ${b.yesterday_completed} tasks completed</li>
        <li><strong>Overall progress:</strong> ${ex.overall_completion}%</li>
        <li><strong>Biggest risk:</strong> ${b.biggest_risk}</li>
        <li><strong>Today's focus:</strong> ${b.today_focus}</li>
        <li><strong>Estimated completion:</strong> ${ex.estimated_days_remaining} days</li>
      </ul>
    </section>`;
}

function renderPhases(phases) {
  const sorted = [...phases].sort((a, b) => (a.id === 0 ? -1 : b.id === 0 ? 1 : a.id - b.id));
  return sorted
    .map(
      (p) => `
    <div class="mc-phase" data-phase>
      <button type="button" class="mc-phase__header" aria-expanded="false">
        <span class="mc-phase__toggle">▶</span>
        <span class="mc-phase__title">Phase ${p.id} — ${p.title}</span>
        <span class="mc-phase__pct">${p.completion}%</span>
      </button>
      <div class="mc-phase__body" hidden>
        ${pctBar('Completion', p.completion)}
        <div class="mc-phase__meta">
          <span>${p.tasks} tasks</span>
          ${p.started ? `<span>Started ${p.started}</span>` : ''}
          ${p.completed ? `<span>Completed ${p.completed}</span>` : ''}
        </div>
        ${(p.items || [])
          .map(
            (item) => `
          <div class="mc-phase-item">
            <span>${statusDot(item.status)}${item.name}</span>
            <span>${item.status.replace('_', ' ')}${item.note ? ` · ${item.note}` : ''}</span>
          </div>`
          )
          .join('')}
      </div>
    </div>`
    )
    .join('');
}

function renderBuildMap(nodes) {
  return `
    <div class="mc-build-map">
      ${nodes
        .map(
          (n, i) => `
        ${i > 0 ? '<span class="mc-build-map__arrow">↓</span>' : ''}
        <a href="${n.href}" class="mc-build-map__node mc-build-map__node--${n.status}">${n.label}</a>`
        )
        .join('')}
      <div class="mc-legend">
        <span style="--c:#22c55e">Complete</span>
        <span>Building</span>
        <span>Planning</span>
        <span>Not started</span>
      </div>
    </div>`;
}

function renderBuildsList(builds) {
  return `
    <ul class="mc-builds-list">
      ${[...builds]
        .reverse()
        .map(
          (b) => `
        <li><a href="/mission-control/build.html?b=${b.number}">
          <span>Build #${b.number} — ${b.title}</span>
          <span>v${b.version} · ${b.status}</span>
        </a></li>`
        )
        .join('')}
    </ul>`;
}

function initPhaseToggles() {
  document.querySelectorAll('[data-phase]').forEach((phase) => {
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

function initDevConsole(data) {
  const params = new URLSearchParams(window.location.search);
  if (!params.has('dev')) return;

  const el = document.createElement('div');
  el.className = 'mc-dev-console';
  el.innerHTML = `
    <span><strong>Dev Console</strong></span>
    <span>Build: #${data.executive.last_build.number}</span>
    <span>Next: #${(data.builds[data.builds.length - 1]?.next_builds || [4])[0]}</span>
    <span>Blocked: ${data.briefing.blocked_tasks.length}</span>
    <a href="${data.executive.repository.url}" target="_blank" rel="noopener">GitHub</a>
    <a href="${data.executive.deployment.url}" target="_blank" rel="noopener">Netlify</a>
    <a href="/data/mission-control.json">JSON</a>
    <a href="/BUILD_PLAN.md">Build Plan</a>`;
  document.body.appendChild(el);
}

async function initMissionControl() {
  const root = document.getElementById('mc-root');
  if (!root) return;

  const res = await fetch('/data/mission-control.json');
  const data = await res.json();

  const dims = data.dimensions;
  const readiness = data.public_readiness;

  root.innerHTML = `
    ${renderBriefing(data.briefing, data.executive)}
    ${renderExecutive(data.executive)}
    <div class="mc-progress-block">
      <h2>Build Dimensions</h2>
      ${pctBar('Research', dims.research, 'blue')}
      ${pctBar('Writing', dims.writing, 'blue')}
      ${pctBar('Design', dims.design, 'green')}
      ${pctBar('Development', dims.development, 'yellow')}
      ${pctBar('Testing', dims.testing, 'yellow')}
      ${pctBar('Deployment', dims.deployment, 'green')}
      ${pctBar('Volunteer System', dims.volunteer_system, 'purple')}
    </div>
    <div class="mc-progress-block">
      <h2>Public Readiness — Is the educational mission ready?</h2>
      ${Object.entries(readiness)
        .map(([k, v]) => pctBar(k.replace(/_/g, ' '), v, v > 50 ? 'green' : 'yellow'))
        .join('')}
    </div>
    <h2 class="mc-section-title">Phase Dashboard</h2>
    <div id="mc-phases">${renderPhases(data.phases)}</div>
    <h2 class="mc-section-title">Living Build Map</h2>
    ${renderBuildMap(data.build_map)}
    <div class="mc-grid-2" style="margin-top:2rem">
      <div class="mc-card">
        <h3>Repository Status</h3>
        <div class="mc-phase-item"><span>GitHub</span><span>${data.repository.connected ? 'Connected' : '—'}</span></div>
        <div class="mc-phase-item"><span>Branch</span><span>${data.repository.branch}</span></div>
        <div class="mc-phase-item"><span>Production</span><span>${data.repository.production}</span></div>
        <div class="mc-phase-item"><span>Deploy Preview</span><span>${data.repository.deploy_preview}</span></div>
      </div>
      <div class="mc-card">
        <h3>Research Dashboard</h3>
        ${Object.entries(data.research_inventory)
          .map(([k, v]) => `<div class="mc-phase-item"><span>${k.replace(/_/g, ' ')}</span><span>${v.collected} / ${v.target}</span></div>`)
          .join('')}
      </div>
      <div class="mc-card">
        <h3>Content Dashboard</h3>
        ${Object.entries(data.content_areas)
          .map(([k, v]) => `<div class="mc-phase-item"><span>${k.replace(/_/g, ' ')}</span><span>${v}%</span></div>`)
          .join('')}
      </div>
      <div class="mc-card">
        <h3>Leadership Pipeline</h3>
        ${Object.entries(data.leadership_pipeline)
          .map(([k, v]) => `<div class="mc-phase-item"><span>${k.replace(/_/g, ' ')}</span><span>${v}</span></div>`)
          .join('')}
        <p style="font-size:0.8rem;color:var(--mc-text-muted);margin:0.75rem 0 0">Grows as signups come in via Netlify Forms.</p>
      </div>
    </div>
    <h2 class="mc-section-title">Build Registry</h2>
    ${renderBuildsList(data.builds)}
    <p style="font-size:0.85rem;color:var(--mc-text-muted);margin-top:1rem">Add <code>?dev=1</code> for developer console. Data: <a href="/data/mission-control.json">mission-control.json</a></p>`;

  initPhaseToggles();
  initDevConsole(data);
}

async function initBuildDetail() {
  const root = document.getElementById('mc-build-detail');
  if (!root) return;

  const num = parseInt(new URLSearchParams(window.location.search).get('b'), 10);
  const res = await fetch('/data/mission-control.json');
  const data = await res.json();
  const build = data.builds.find((b) => b.number === num);

  if (!build) {
    root.innerHTML = '<p>Build not found.</p>';
    return;
  }

  root.innerHTML = `
    <nav class="breadcrumb" style="color:var(--mc-text-muted)"><a href="/mission-control/" style="color:var(--mc-accent)">Mission Control</a> → Build #${build.number}</nav>
    <header class="mc-header">
      <h1>Build #${build.number} — ${build.title}</h1>
      <p class="mc-header__question">Permanent institutional memory · Build DNA</p>
    </header>
    <div class="mc-dna">
      <div class="mc-dna__item"><strong>Status</strong>${build.status}</div>
      <div class="mc-dna__item"><strong>Version</strong>v${build.version}</div>
      <div class="mc-dna__item"><strong>Phase</strong>${build.phase}</div>
      <div class="mc-dna__item"><strong>Started</strong>${build.started || '—'}</div>
      <div class="mc-dna__item"><strong>Completed</strong>${build.completed || '—'}</div>
      <div class="mc-dna__item"><strong>Est. Hours</strong>${build.estimated_hours || '—'}</div>
      <div class="mc-dna__item"><strong>Actual Hours</strong>${build.actual_hours || '—'}</div>
      <div class="mc-dna__item"><strong>Review</strong>${build.review_status || '—'}</div>
      <div class="mc-dna__item"><strong>Documentation</strong>${build.documentation_status || '—'}</div>
      <div class="mc-dna__item"><strong>Testing</strong>${build.testing_status || '—'}</div>
      <div class="mc-dna__item"><strong>Git Commit</strong><code>${build.git_commit || '—'}</code></div>
      <div class="mc-dna__item"><strong>Netlify</strong>${build.netlify_deploy || '—'}</div>
    </div>
    <div class="mc-card" style="margin-top:1rem">
      <h3>Files</h3>
      <ul>${(build.files || []).map((f) => `<li><code>${f}</code></li>`).join('')}</ul>
    </div>
    <div class="mc-card" style="margin-top:1rem">
      <h3>Pages</h3>
      <ul>${(build.pages || []).map((p) => `<li><a href="${p}">${p}</a></li>`).join('')}</ul>
    </div>
    <div class="mc-grid-2" style="margin-top:1rem">
      <div class="mc-card"><h3>Dependencies</h3><p>Builds: ${(build.dependencies || []).join(', ') || 'None'}</p></div>
      <div class="mc-card"><h3>Next Builds</h3><p>${(build.next_builds || []).map((n) => `<a href="/mission-control/build.html?b=${n}">#${n}</a>`).join(', ') || 'TBD'}</p></div>
    </div>
    <div class="mc-card" style="margin-top:1rem"><h3>Notes</h3><p>${build.notes || '—'}</p></div>
    <div class="mc-card" style="margin-top:1rem"><h3>Lessons Learned</h3><p>${build.lessons || '—'}</p></div>
    ${build.cursor_prompt ? `<div class="mc-card" style="margin-top:1rem"><h3>Cursor Prompt</h3><pre style="white-space:pre-wrap;font-size:0.85rem">${build.cursor_prompt}</pre></div>` : ''}
    <p style="margin-top:1.5rem"><a href="/builds/00${build.number}-*.html">View build page →</a> · <a href="/mission-control/">← Mission Control</a></p>`;
}

document.addEventListener('DOMContentLoaded', () => {
  initMissionControl();
  initBuildDetail();
});
