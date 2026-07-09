/**
 * Citizens Facts — Floating Action Hub v1.4.0
 * Learn → Participate → Organize → Build Solutions
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

function renderActionHub() {
  if (document.getElementById('action-hub')) return;

  const hub = document.createElement('div');
  hub.id = 'action-hub';
  hub.className = 'action-hub';
  hub.innerHTML = `
    <button type="button" class="action-hub__toggle" aria-expanded="false" aria-controls="action-hub-panel" aria-label="Open civic action menu">
      <span class="action-hub__toggle-icon">✦</span>
      <span class="action-hub__toggle-label">Take Action</span>
    </button>
    <div id="action-hub-panel" class="action-hub__panel" hidden>
      <p class="action-hub__title">Civic Action Hub</p>
      <p class="action-hub__subtitle">Education → Participation</p>
      <nav class="action-hub__nav" aria-label="Civic actions">
        <a href="/educate/" class="action-hub__link action-hub__link--primary">★ Become an Education Leader</a>
        <a href="/action/join-network.html" class="action-hub__link">◎ Join the Education Network</a>
        <a href="/action/share.html" class="action-hub__link">↗ Share This Page</a>
        <a href="/action/share.html#invite" class="action-hub__link">👥 Invite Friends and Family</a>
        <a href="/action/join-network.html" class="action-hub__link">📋 Contact List Signup</a>
        <a href="/action/draft-laws.html" class="action-hub__link">§ Draft a Law</a>
        <a href="/action/ballot-lab.html" class="action-hub__link">✓ Ballot Initiative Lab</a>
        <a href="/action/ideas.html" class="action-hub__link">💡 Community Ideas</a>
        <a href="/action/ideas.html" class="action-hub__link">? Ask a Question</a>
        <a href="/action/ideas.html#feedback" class="action-hub__link">💬 Give Feedback</a>
      </nav>
    </div>`;

  document.body.appendChild(hub);

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

// Export for share page
window.CivicAction = { getReferralCode, getShareUrl, trackHallVisit };
