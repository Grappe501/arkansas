/**
 * Citizen Journey System v1.0 — Build #8
 * Session memory, learning panel, adaptive recommendations
 */

const JOURNEY_PREFIX = 'cf_journey_';

const STAGE_ORDER = ['discover', 'understand', 'explore', 'evaluate', 'discuss', 'teach', 'lead'];

const PATH_STAGE_HINTS = {
  '/': 'discover',
  '/the-story': 'explore',
  '/halls/story-before.html': 'explore',
  '/the-case': 'understand',
  '/halls/the-case.html': 'understand',
  '/the-constitution': 'understand',
  '/halls/what-court-decided.html': 'understand',
  '/the-impact': 'explore',
  '/follow-the-money': 'explore',
  '/the-debate': 'discuss',
  '/solutions': 'evaluate',
  '/solutions/': 'evaluate',
  '/reform': 'evaluate',
  '/teach': 'teach',
  '/educate/': 'lead',
  '/sources': 'explore',
  '/library/': 'explore',
  '/action/share.html': 'discuss',
  '/action/ideas.html': 'discuss',
  '/action/join-network.html': 'lead',
};

const HALL_MILESTONES = {
  'story-before': 'story-complete',
  'the-case': 'case-complete',
  'what-court-decided': 'constitution-complete',
  'after-2010': 'impact-complete',
  'reform': 'reform-complete',
  'montana-hawaii': 'reform-complete',
};

function journeyGet(key, fallback = null) {
  try {
    const v = localStorage.getItem(JOURNEY_PREFIX + key);
    return v === null ? fallback : JSON.parse(v);
  } catch {
    return fallback;
  }
}

function journeySet(key, value) {
  localStorage.setItem(JOURNEY_PREFIX + key, JSON.stringify(value));
}

function journeyGetRaw(key, fallback = '') {
  return localStorage.getItem(JOURNEY_PREFIX + key) || fallback;
}

function journeySetRaw(key, value) {
  localStorage.setItem(JOURNEY_PREFIX + key, value);
}

function getVisitedPages() {
  return journeyGet('pages_visited', []) || [];
}

function getHallsVisited() {
  return JSON.parse(localStorage.getItem('cf_halls_visited') || '[]');
}

function getMilestones() {
  return journeyGet('milestones', []) || [];
}

function getBookmarks() {
  return journeyGet('bookmarks', []) || [];
}

function estimateStage() {
  const saved = journeyGetRaw('stage');
  if (saved && STAGE_ORDER.includes(saved)) return saved;

  const pages = getVisitedPages();
  const halls = getHallsVisited();
  const milestones = getMilestones();

  if (pages.some(p => p.includes('/educate'))) return 'lead';
  if (pages.some(p => p.includes('/action/share') || p.includes('/action/ideas'))) return 'discuss';
  if (milestones.includes('community-education') || pages.some(p => p.includes('/teach') || p.includes('/educate'))) return 'teach';
  if (halls.includes('solutions') || halls.includes('reform') || halls.includes('debate') || halls.includes('montana-hawaii')) return 'evaluate';
  if (halls.length >= 3 || pages.some(p => p.includes('/library') || p.includes('/sources'))) return 'explore';
  if (halls.length >= 1) return 'understand';
  return 'discover';
}

function stageIndex(id) {
  return STAGE_ORDER.indexOf(id);
}

function trackPageVisit() {
  const path = window.location.pathname;
  const pages = getVisitedPages();
  if (!pages.includes(path)) {
    pages.push(path);
    journeySet('pages_visited', pages);
  }
  journeySetRaw('last_page', path);

  const visits = parseInt(journeyGetRaw('visit_count', '0'), 10) + (pages.length === 1 ? 1 : 0);
  if (!journeyGetRaw('first_visit')) journeySetRaw('first_visit', new Date().toISOString());
  if (pages.length === 1) journeySetRaw('visit_count', String(visits + 1));

  const halls = getHallsVisited();
  halls.forEach(h => {
    const mid = HALL_MILESTONES[h];
    if (mid) {
      const ms = getMilestones();
      if (!ms.includes(mid)) {
        ms.push(mid);
        journeySet('milestones', ms);
      }
    }
  });

  const hint = PATH_STAGE_HINTS[path];
  const current = estimateStage();
  if (hint && stageIndex(hint) > stageIndex(current)) {
    journeySetRaw('stage', hint);
  } else {
    journeySetRaw('stage', estimateStage());
  }
}

function toggleBookmark() {
  const path = window.location.pathname;
  const title = document.title.split('|')[0].trim();
  const bookmarks = getBookmarks();
  const idx = bookmarks.findIndex(b => b.path === path);
  if (idx >= 0) {
    bookmarks.splice(idx, 1);
  } else {
    bookmarks.push({ path, title, saved: new Date().toISOString() });
  }
  journeySet('bookmarks', bookmarks);
  return idx < 0;
}

function renderLearningPanel(data) {
  if (document.getElementById('journey-panel') || !data?.learning_panel?.enabled) return;
  if (window.location.pathname.includes('/mission-control') || window.location.pathname.includes('/admin/')) return;

  const stage = estimateStage();
  const stageInfo = data.learning_ladder.find(s => s.id === stage) || data.learning_ladder[0];
  const bookmarks = getBookmarks().slice(-3).reverse();
  const lastPage = journeyGetRaw('last_page', '/');
  const milestones = getMilestones();

  const ladderHtml = data.learning_ladder.map(s => {
    const idx = stageIndex(s.id);
    const cur = stageIndex(stage);
    const cls = idx < cur ? 'done' : idx === cur ? 'active' : '';
    return `<span class="journey-ladder__step journey-ladder__step--${cls}">${s.title}</span>`;
  }).join('');

  const panel = document.createElement('aside');
  panel.id = 'journey-panel';
  panel.className = 'journey-panel journey-panel--collapsed';
  panel.setAttribute('aria-label', 'Learning progress panel');
  panel.innerHTML = `
    <button type="button" class="journey-panel__tab" aria-expanded="false" aria-controls="journey-panel-body">Learning</button>
    <div id="journey-panel-body" class="journey-panel__body" hidden>
      <p class="journey-panel__title">${data.learning_panel.title}</p>
      <div class="journey-panel__stage">
        <strong>Current stage</strong>
        ${stageInfo.title} — ${stageInfo.description}
      </div>
      <div class="journey-ladder" aria-label="Learning ladder">${ladderHtml}</div>
      ${milestones.length ? `<p style="font-size:0.75rem;margin:0 0 0.5rem"><strong>Milestones:</strong> ${milestones.length}</p>` : ''}
      ${bookmarks.length ? `<ul class="journey-panel__list">${bookmarks.map(b => `<li><a href="${b.path}">${b.title}</a></li>`).join('')}</ul>` : '<p style="font-size:0.75rem;color:#5a6a7a">No bookmarks yet.</p>'}
      <p style="font-size:0.75rem;margin:0"><a href="${lastPage}">Continue →</a></p>
    </div>`;

  document.body.appendChild(panel);

  const tab = panel.querySelector('.journey-panel__tab');
  const body = panel.querySelector('.journey-panel__body');
  tab.addEventListener('click', () => {
    const open = tab.getAttribute('aria-expanded') === 'true';
    tab.setAttribute('aria-expanded', !open);
    body.hidden = open;
    panel.classList.toggle('journey-panel--collapsed', open);
  });
}

function renderNextSteps(data) {
  if (document.querySelector('.journey-next-steps')) return;
  if (window.location.pathname.includes('/mission-control')) return;

  const path = window.location.pathname;
  const stage = estimateStage();
  const byPage = data.recommendations?.by_page?.[path] || [];
  const byStage = data.recommendations?.by_stage?.[stage] || [];
  const recs = byPage.length ? byPage : byStage.slice(0, 3);
  if (!recs.length) return;

  const main = document.querySelector('.site-main, .mc-main, main');
  if (!main) return;

  const block = document.createElement('section');
  block.className = 'journey-next-steps';
  block.setAttribute('aria-label', 'Suggested next steps');
  block.innerHTML = `
    <span class="journey-stage-badge">Stage: ${stage}</span>
    <h2>Continue Your Journey</h2>
    <p>Based on where you are in the learning ladder.</p>
    <ul>
      ${recs.map(r => `<li><a href="${r.url}">${r.title}</a>${r.reason ? ` <span style="color:#5a6a7a;font-size:0.85em">— ${r.reason}</span>` : ''}</li>`).join('')}
    </ul>`;
  main.appendChild(block);
}

function renderContinuePrompt(data) {
  if (window.location.pathname !== '/' && window.location.pathname !== '/index.html') return;
  if (document.querySelector('.journey-continue')) return;

  const last = journeyGetRaw('last_page');
  const visits = parseInt(journeyGetRaw('visit_count', '0'), 10);
  const pages = getVisitedPages();
  if (visits < 1 && pages.length < 2) return;
  if (!last || last === '/') return;

  const main = document.querySelector('.site-main');
  if (!main) return;

  const stage = estimateStage();
  const stageTitle = data.learning_ladder.find(s => s.id === stage)?.title || stage;

  const el = document.createElement('div');
  el.className = 'journey-continue';
  el.innerHTML = `
    <p><strong>Welcome back.</strong> You were exploring at the <em>${stageTitle}</em> stage.</p>
    <p><a href="${last}">Continue learning where you left off →</a></p>`;
  main.insertBefore(el, main.firstChild?.nextSibling || main.firstChild);
}

async function initJourney() {
  trackPageVisit();

  let data = null;
  try {
    const res = await fetch('/data/ux-journey.json');
    data = await res.json();
  } catch {
    return;
  }

  renderLearningPanel(data);
  renderNextSteps(data);
  renderContinuePrompt(data);
}

document.addEventListener('DOMContentLoaded', initJourney);

window.CitizenJourney = {
  estimateStage,
  getMilestones,
  getBookmarks,
  toggleBookmark,
  trackPageVisit,
  journeyGetRaw,
  STAGE_ORDER,
};
