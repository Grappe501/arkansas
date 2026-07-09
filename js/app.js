/**
 * Citizens Facts — Site utilities v1.0.0
 */

async function loadSiteData() {
  const response = await fetch('/data/site.json');
  if (!response.ok) throw new Error('Failed to load site data');
  return response.json();
}

function formatDate(dateStr) {
  const date = new Date(dateStr + 'T12:00:00');
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
}

function renderEntryCards(entries, container) {
  if (!container || !entries.length) return;

  container.innerHTML = entries
    .filter((e) => e.status === 'published')
    .map(
      (entry) => `
    <li>
      <article class="entry-card">
        <a href="/entries/${entry.slug}.html">
          <div class="entry-card__meta">
            <span class="version-badge">v${entry.version}</span>
            <span>Entry ${entry.id}</span>
            <span>${formatDate(entry.date)}</span>
          </div>
          <h3>${entry.title}</h3>
          <p>${entry.summary}</p>
          ${
            entry.states?.length
              ? `<div class="state-tags">${entry.states.map((s) => `<span class="state-tag">${s}</span>`).join('')}</div>`
              : ''
          }
        </a>
      </article>
    </li>`
    )
    .join('');
}

function renderTrackCards(tracks, container) {
  if (!container || !tracks.length) return;

  const labels = ['Track 1', 'Track 2', 'Track 3'];

  container.innerHTML = tracks
    .map(
      (track, i) => `
    <article class="track-card">
      <div class="track-card__number">${labels[i] || 'Track'}</div>
      <h3>${track.title}</h3>
      <p>${track.description}</p>
    </article>`
    )
    .join('');
}

function setVersionBadge() {
  const badge = document.querySelector('[data-site-version]');
  if (badge) {
    loadSiteData()
      .then((data) => {
        badge.textContent = `v${data.site.version}`;
      })
      .catch(() => {});
  }
}

document.addEventListener('DOMContentLoaded', () => {
  setVersionBadge();

  const entriesContainer = document.getElementById('entries-list');
  const tracksContainer = document.getElementById('tracks-grid');

  if (entriesContainer || tracksContainer) {
    loadSiteData()
      .then((data) => {
        if (tracksContainer) renderTrackCards(data.tracks, tracksContainer);
        if (entriesContainer) renderEntryCards(data.entries, entriesContainer);
      })
      .catch((err) => console.error(err));
  }
});
