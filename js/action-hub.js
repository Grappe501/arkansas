/**
 * Citizens Facts — Floating Action Hub v1.16.1
 * Arkansas Education Ladder-aware — Build #12
 */

function getReferralCode() {
  let code = localStorage.getItem('cf_referral_code');
  if (!code) {
    code = 'CF-' + Math.random().toString(36).substring(2, 8).toUpperCase();
    localStorage.setItem('cf_referral_code', code);
  }
  return code;
}

function getShareUrl() {
  const code = getReferralCode();
  const url = new URL(window.location.href);
  url.searchParams.set('ref', code);
  return url.toString();
}

function trackHallVisit() {
  const path = window.location.pathname;
  if (!path.includes('/halls/')) return;
  const visited = JSON.parse(localStorage.getItem('cf_halls_visited') || '[]');
  const hall = path.split('/').pop().replace('.html', '');
  if (hall && !visited.includes(hall)) {
    visited.push(hall);
    localStorage.setItem('cf_halls_visited', JSON.stringify(visited));
  }
}

function getVisitorStage() {
  if (window.CitizenJourney?.estimateStage) return window.CitizenJourney.estimateStage();
  const stage = localStorage.getItem('cf_journey_stage');
  if (stage) return stage;
  const halls = JSON.parse(localStorage.getItem('cf_halls_visited') || '[]');
  if (halls.length >= 3) return 'explore';
  if (halls.length >= 1) return 'understand';
  return 'discover';
}

function getCivicLevel() {
  if (window.CivicProfile?.estimateCivicLevel) return window.CivicProfile.estimateCivicLevel();
  return 'visitor';
}

function getCivicLevelNum() {
  if (window.CivicProfile?.civicLevelNumber) return window.CivicProfile.civicLevelNumber(getCivicLevel());
  return 1;
}

function isEarlyStage(stage) {
  return stage === 'discover' || stage === 'understand';
}

function renderCivicHubActions(ecosystem, civicLevelNum) {
  const actions = ecosystem?.action_hub?.actions || [];
  return actions
    .filter(a => (a.min_level || 1) <= civicLevelNum)
    .map(a => {
      const primary = (a.primary_from_level && civicLevelNum >= a.primary_from_level) ||
        (a.primary_until_level && civicLevelNum < a.primary_until_level);
      const cls = primary ? ' action-hub__link--primary' : '';
      if (a.id === 'share-page') {
        return `<a href="${a.url}" class="action-hub__link${cls}" data-track-share>${a.icon} ${a.title}</a>`;
      }
      return `<a href="${a.url}" class="action-hub__link${cls}">${a.icon} ${a.title}</a>`;
    }).join('');
}

function renderHubLinks(stage, config, ecosystem) {
  const civicLevelNum = getCivicLevelNum();
  if (ecosystem?.action_hub?.actions) {
    const bookmark = `<button type="button" class="action-hub__link action-hub__link--bookmark" data-bookmark>★ Save This Page</button>`;
    return renderCivicHubActions(ecosystem, civicLevelNum) + bookmark;
  }

  const early = isEarlyStage(stage);
  const block = early ? config?.action_hub_stages?.early : config?.action_hub_stages?.advanced;
  if (!block) return renderDefaultLinks(stage);

  const links = block.primary_actions.map(a => {
    if (a.action === 'bookmark') {
      return `<button type="button" class="action-hub__link action-hub__link--bookmark" data-bookmark>★ Save This Page</button>`;
    }
    const primary = a.primary ? ' action-hub__link--primary' : '';
    return `<a href="${a.url}" class="action-hub__link${primary}">${a.icon} ${a.title}</a>`;
  }).join('');

  const secondary = early ? `
    <a href="/educate/" class="action-hub__link">★ Become an Education Leader</a>
    <a href="/action/ideas.html" class="action-hub__link">? Ask a Question</a>
  ` : `
    <a href="/action/share.html" class="action-hub__link">↗ Share This Page</a>
    <a href="/action/join-network.html" class="action-hub__link">◎ Join the Network</a>
    <a href="/action/community-conversation.html" class="action-hub__link">🗣 Host a Conversation</a>
    <a href="/action/ideas.html" class="action-hub__link">💡 Community Ideas</a>
  `;

  return links + secondary;
}

function renderDefaultLinks(stage) {
  const early = isEarlyStage(stage);
  if (early) {
    return `
      <a href="/action/share.html" class="action-hub__link action-hub__link--primary">↗ Share This Page</a>
      <button type="button" class="action-hub__link action-hub__link--bookmark" data-bookmark>★ Save This Page</button>
      <a href="/action/join-network.html" class="action-hub__link">◎ Join the Contact Network</a>
      <a href="/educate/" class="action-hub__link">Become an Education Leader</a>
    `;
  }
  return `
    <a href="/educate/" class="action-hub__link action-hub__link--primary">★ Become an Education Leader</a>
    <a href="/action/community-conversation.html" class="action-hub__link">🗣 Host a Conversation</a>
    <a href="/action/draft-laws.html" class="action-hub__link">§ Draft a Model Law</a>
    <a href="/action/ballot-lab.html" class="action-hub__link">✓ Ballot Initiative Lab</a>
    <a href="/action/contact-legislators.html" class="action-hub__link">🏛 Share with Officials</a>
    <a href="/action/share.html" class="action-hub__link">↗ Share</a>
  `;
}

async function renderActionHub() {
  if (document.getElementById('action-hub')) return;

  let config = null;
  let ecosystem = null;
  try {
    const [uxRes, civicRes] = await Promise.all([
      fetch('/data/ux-journey.json'),
      fetch('/data/civic-ecosystem.json')
    ]);
    config = await uxRes.json();
    ecosystem = await civicRes.json();
  } catch { /* use defaults */ }

  const stage = getVisitorStage();
  const civicLevel = getCivicLevel();
  const civicNum = getCivicLevelNum();
  const early = isEarlyStage(stage);
  const ladderTitle = ecosystem?.arkansas_education_ladder?.find(l => l.id === civicLevel)?.title
    || ecosystem?.civic_growth_ladder?.find(l => l.id === civicLevel)?.title
    || civicLevel;
  const label = early
    ? (config?.action_hub_stages?.early?.label || 'Learn & Share')
    : (config?.action_hub_stages?.advanced?.label || 'Take Action');

  const hub = document.createElement('div');
  hub.id = 'action-hub';
  hub.className = 'action-hub';
  hub.innerHTML = `
    <button type="button" class="action-hub__toggle" aria-expanded="false" aria-controls="action-hub-panel" aria-label="Open civic action menu">
      <span class="action-hub__toggle-icon">✦</span>
      <span class="action-hub__toggle-label">${label}</span>
    </button>
    <div id="action-hub-panel" class="action-hub__panel" hidden>
      <p class="action-hub__title">Arkansas Action Hub</p>
      <p class="action-hub__subtitle">Arkansas · Journey: ${stage} · Level ${civicNum}: ${ladderTitle}</p>
      <nav class="action-hub__nav" aria-label="Civic actions">
        ${renderHubLinks(stage, config, ecosystem)}
      </nav>
    </div>`;

  document.body.appendChild(hub);

  hub.querySelector('[data-bookmark]')?.addEventListener('click', () => {
    if (window.CitizenJourney?.toggleBookmark) {
      const saved = window.CitizenJourney.toggleBookmark();
      const btn = hub.querySelector('[data-bookmark]');
      if (btn) btn.textContent = saved ? '★ Saved!' : '★ Save This Page';
    }
  });

  hub.querySelector('[data-track-share]')?.addEventListener('click', () => {
    if (window.CivicProfile?.trackShare) window.CivicProfile.trackShare();
  });

  const toggle = hub.querySelector('.action-hub__toggle');
  const panel = hub.querySelector('.action-hub__panel');

  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !open);
    panel.hidden = open;
    hub.classList.toggle('action-hub--open', !open);
  });

  document.addEventListener('click', (e) => {
    if (!hub.contains(e.target) && hub.classList.contains('action-hub--open')) {
      toggle.setAttribute('aria-expanded', 'false');
      panel.hidden = true;
      hub.classList.remove('action-hub--open');
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  trackHallVisit();
  renderActionHub();
});

window.CivicAction = { getReferralCode, getShareUrl, trackHallVisit, getVisitorStage, getCivicLevel, getCivicLevelNum };
