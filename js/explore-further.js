/**
 * Explore Further — Knowledge Graph connections (Build #11)
 * Injects related nodes from kg-registry.json at end of content pages.
 */

const EXPLORE_CSS = '/css/explore-further.css';

const EDGE_GROUPS = {
  precursor: 'historical',
  influenced_by: 'historical',
  overturned_by: 'historical',
  aftermath: 'later',
  enables: 'later',
  influenced: 'later',
  cited_by: 'later',
  challenges: 'reforms',
  supports: 'reforms',
  addresses: 'principles',
  applies: 'principles',
  interprets: 'principles',
  measures: 'data',
  related_to: 'also',
  implements: 'historical',
  upheld_by: 'cases',
  decided_by: 'cases',
  authored_by: 'cases'
};

const GROUP_LABELS = {
  also: 'People also explored…',
  principles: 'Related constitutional principles…',
  cases: 'Related Supreme Court cases…',
  historical: 'Historical events that led here…',
  later: 'Later events influenced by this…',
  reforms: 'Current reform efforts…',
  data: 'Relevant spending data…',
  sources: 'Primary sources…',
  teach: 'Educational toolkit…',
  lead: 'Become an Education Leader…'
};

function ensureExploreFurtherCss() {
  if (!document.querySelector(`link[href="${EXPLORE_CSS}"]`)) {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = EXPLORE_CSS;
    document.head.appendChild(link);
  }
}

function normalizePath(path) {
  if (!path) return '/';
  const p = path.replace(/index\.html$/, '').replace(/\.html$/, match => match === 'index.html' ? '' : match);
  if (p.endsWith('/') && p.length > 1) return p;
  if (!p.includes('.') && !p.endsWith('/')) return p + '/';
  return p;
}

function resolveNodeId(registry, path) {
  const bindings = registry.page_bindings || {};
  if (bindings[path]) return bindings[path];
  const norm = normalizePath(path);
  if (bindings[norm]) return bindings[norm];
  const slug = path.split('/').pop()?.replace('.html', '');
  if (slug) {
    const bySlug = registry.nodes.find(n => n.url && n.url.includes(slug));
    if (bySlug) return bySlug.kg_id;
  }
  return null;
}

function nodeLink(node) {
  if (!node.url) return node.title;
  const ext = node.url.startsWith('http');
  return ext
    ? `<a href="${node.url}" target="_blank" rel="noopener">${node.title}</a>`
    : `<a href="${node.url}">${node.title}</a>`;
}

function buildGroups(registry, nodeId) {
  const nodeMap = Object.fromEntries(registry.nodes.map(n => [n.kg_id, n]));
  const edges = registry.edges.filter(e => e.from === nodeId || e.to === nodeId);
  const groups = {};

  edges.forEach(edge => {
    const otherId = edge.from === nodeId ? edge.to : edge.from;
    const other = nodeMap[otherId];
    if (!other) return;
    const bucket = EDGE_GROUPS[edge.type] || (other.type === 'case' ? 'cases' : other.type === 'reform' ? 'reforms' : 'also');
    if (!groups[bucket]) groups[bucket] = [];
    if (!groups[bucket].some(n => n.kg_id === other.kg_id)) groups[bucket].push(other);
  });

  const hub = nodeMap[registry.hub_node];
  if (nodeId !== registry.hub_node && hub && !groups.cases?.some(n => n.kg_id === hub.kg_id)) {
    if (!groups.cases) groups.cases = [];
    groups.cases.unshift(hub);
  }

  return groups;
}

function renderExploreFurther(registry, nodeId) {
  const nodeMap = Object.fromEntries(registry.nodes.map(n => [n.kg_id, n]));
  const current = nodeMap[nodeId];
  const groups = buildGroups(registry, nodeId);
  const order = ['also', 'principles', 'cases', 'historical', 'later', 'reforms', 'data'];

  const groupHtml = order
    .filter(key => groups[key]?.length)
    .map(key => `
      <div class="explore-further__group">
        <h3>${GROUP_LABELS[key]}</h3>
        <ul class="explore-further__list">
          ${groups[key].slice(0, 5).map(n => `
            <li>${nodeLink(n)}${n.year ? ` <span class="explore-further__meta">(${n.year})</span>` : ''}</li>`).join('')}
        </ul>
      </div>`).join('');

  const staticBlocks = `
    <div class="explore-further__group">
      <h3>${GROUP_LABELS.sources}</h3>
      <ul class="explore-further__list">
        <li><a href="/library/">Source Library</a></li>
        ${(current?.evidence_ids || []).map(id => `<li><a href="/mission-control/research.html#${id}">${id}</a></li>`).join('')}
      </ul>
    </div>
    <div class="explore-further__group">
      <h3>${GROUP_LABELS.teach}</h3>
      <ul class="explore-further__list">
        <li><a href="/educate/">Teach This Locally</a></li>
        <li><a href="/action/share.html">Share resources</a></li>
      </ul>
    </div>`;

  return `
    <section class="explore-further" aria-labelledby="explore-further-heading">
      <h2 class="explore-further__title" id="explore-further-heading">Explore Further</h2>
      <p class="explore-further__subtitle">Connected knowledge — ${current ? current.title : 'this topic'} is part of a larger graph. Keep exploring.</p>
      <div class="explore-further__grid">${groupHtml}${staticBlocks}</div>
      <div class="explore-further__cta">
        <a href="/educate/" class="ds-civic-chip">Become an Education Leader</a>
        <a href="/solutions/" class="ds-civic-chip">Policy Options</a>
      </div>
      <p class="explore-further__hub"><a href="/mission-control/knowledge-graph.html">Knowledge graph dashboard →</a> · <code>${nodeId || '—'}</code></p>
    </section>`;
}

async function initExploreFurther() {
  if (document.body.classList.contains('mc-body')) return;
  const main = document.querySelector('.site-main');
  if (!main || main.querySelector('.explore-further')) return;

  ensureExploreFurtherCss();

  try {
    const res = await fetch('/data/kg-registry.json');
    const registry = await res.json();
    const path = window.location.pathname;
    const nodeId = resolveNodeId(registry, path) || registry.hub_node;
    main.insertAdjacentHTML('beforeend', renderExploreFurther(registry, nodeId));
  } catch {
    /* silent — graph optional on early pages */
  }
}

document.addEventListener('DOMContentLoaded', initExploreFurther);
