"""Generate content-inventory.json — Build #6"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/site-architecture.json') as f:
    arch = json.load(f)

today = '2026-07-09'
items = []
counters = {}


def add_item(prefix, domain, category, title, parent, level='L1', stage='discover',
             status='planned', pct=0, source='none', review='none', url=None, **extra):
    counters[prefix] = counters.get(prefix, 0) + 1
    cid = f"{prefix}-{counters[prefix]:03d}"
    item = {
        'id': cid,
        'domain': domain,
        'category': category,
        'title': title,
        'parent_section': parent,
        'reader_level': level,
        'reader_stage': stage,
        'status': status,
        'completion_pct': pct,
        'source_status': source,
        'review_status': review,
        'url': url,
        'reading_time': {'L1': '1 min', 'L2': '5 min', 'L3': '20 min', 'L4': 'research'}.get(level, '—'),
        'difficulty': 'intro' if level == 'L1' else 'intermediate',
        'audience': 'general',
        'sources_required': extra.get('sources_required', 0),
        'sources_complete': extra.get('sources_complete', 0),
        'version': extra.get('version', '0.0'),
        'updated': today,
        'mission_control': f"/mission-control/inventory.html#{cid}"
    }
    if extra.get('related'):
        item['related'] = extra['related']
    items.append(item)
    return cid


# Domain 1000 — Landing
add_item('LAND', 1000, 'page', 'Homepage', 'home', 'L1', 'discover', 'published', 45, 'partial', 'editorial', '/')
add_item('LAND', 1000, 'section', 'Why It Matters', 'home', 'L1', 'discover', 'published', 40, 'partial', 'none', '/#why-it-matters')
add_item('LAND', 1000, 'section', 'Hero Story', 'home', 'L1', 'discover', 'published', 50, 'partial', 'none', '/')
add_item('LAND', 1000, 'section', 'Platform Overview', 'home', 'L1', 'discover', 'partial', 25, 'none', 'none', '/explore/')
add_item('LAND', 1000, 'section', 'Interactive Timeline Preview', 'home', 'L1', 'discover', 'partial', 10, 'none', 'none', '/')
add_item('LAND', 1000, 'section', 'Money in Politics Preview', 'home', 'L1', 'discover', 'partial', 10, 'none', 'none', '/')
add_item('LAND', 1000, 'section', 'Current Reform Preview', 'home', 'L1', 'discover', 'partial', 15, 'partial', 'none', '/')
add_item('LAND', 1000, 'section', 'Leadership Invitation', 'home', 'L1', 'lead', 'published', 55, 'none', 'editorial', '/educate/')
add_item('LAND', 1000, 'section', 'Quick Facts', 'home', 'L1', 'discover', 'planned', 0)
add_item('LAND', 1000, 'page', 'Site Orientation / Explore Map', 'home', 'L1', 'discover', 'published', 60, 'none', 'none', '/explore/')
add_item('LAND', 1000, 'page', 'Frequently Asked Questions', 'home', 'L1', 'discuss', 'planned', 0, url='/faq')

domain_map = {
    'the-story': (2000, 'HIST', 'explore'),
    'the-case': (3000, 'CASE', 'understand'),
    'the-constitution': (4000, 'CONST', 'understand'),
    'the-impact': (5000, 'IMPACT', 'explore'),
    'follow-the-money': (6000, 'MONEY', 'explore'),
    'the-debate': (7000, 'DEBATE', 'discuss'),
    'reform': (8000, 'REFORM', 'evaluate'),
    'teach': (9000, 'CIVIC', 'teach'),
    'sources': (10000, 'SOURCE', 'explore'),
}

for section in arch['primary_navigation']:
    sid = section['id']
    if sid == 'home':
        continue
    dom, prefix, stage = domain_map[sid]
    hall_status = section.get('status', 'planned')
    st = 'published' if hall_status == 'live' else 'partial' if hall_status == 'partial' else 'outlined' if hall_status == 'stub' else 'planned'
    pct = 15 if st == 'outlined' else 35 if st == 'partial' else 50 if st == 'published' else 0
    url = section.get('current_url')
    add_item(prefix, dom, 'hall-overview', f"{section['title']} — Overview", sid, 'L1', stage, st, pct, 'partial' if st != 'planned' else 'none', 'none', url)
    for sub in section.get('subsections', []):
        sub_st = sub.get('status', 'planned')
        status = 'published' if sub_st == 'live' else 'partial' if sub_st == 'partial' else 'planned'
        sub_pct = 70 if sub_st == 'live' else 15 if sub_st == 'partial' else 0
        sub_url = sub.get('url') or f"{section['canonical_url']}/{sub['slug']}"
        src = 'complete' if sub_st == 'live' else 'partial' if sub_st == 'partial' else 'none'
        rev = 'fact-check' if sub_st == 'live' else 'none'
        add_item(prefix, dom, 'article', sub['title'], sid, 'L1', stage, status, sub_pct, src, rev,
                 sub_url if status != 'planned' else None,
                 sources_required=8 if sub_st == 'live' else 5, sources_complete=6 if sub_st == 'live' else 0,
                 version='1.0' if sub_st == 'live' else '0.0')
        for lvl in ['L2', 'L3', 'L4']:
            add_item(prefix, dom, 'depth', f"{sub['title']} ({lvl})", sid, lvl, stage, 'planned', 0)

add_item('REFORM', 8000, 'research-entry', 'Montana & Hawaii: Two Paths (Ernie Entry 001)', 'reform', 'L4', 'evaluate',
         'published', 75, 'complete', 'fact-check', '/halls/montana-hawaii.html',
         sources_required=12, sources_complete=10, version='1.0.0', related=['REFORM-002', 'REFORM-003'])

action_modules = [
    ('Education Leader Program', '/educate/', 'published', 50),
    ('Contact Network', '/action/join-network.html', 'partial', 35),
    ('Share Toolkit', '/action/share.html', 'partial', 30),
    ('Relational Organizing Guide', '/action/share.html#invite', 'partial', 20),
    ('Community Conversation Guide', None, 'planned', 0),
    ('Ballot Initiative Lab', '/action/ballot-lab.html', 'outlined', 10),
    ('Model Law Workspace', '/action/draft-laws.html', 'outlined', 10),
    ('Legislative Outreach Toolkit', '/action/contact-legislators.html', 'outlined', 10),
    ('Community Ideas Portal', '/action/ideas.html', 'partial', 35),
]
for title, url, st, pct in action_modules:
    add_item('ACTION', 9000, 'civic-module', title, 'civic-action', 'L2', 'lead', st, pct,
             'partial' if pct > 0 else 'none', 'none', url)

cross_types = [
    ('CROSS-TIME', 'Interactive Timeline', 250),
    ('CROSS-GLOS', 'Interactive Glossary', 500),
    ('CROSS-FAQ', 'Frequently Asked Questions', 300),
    ('CROSS-CHART', 'Charts & Infographics', 200),
    ('CROSS-DATA', 'Interactive Data Visualizations', 50),
    ('CROSS-DL', 'Downloadable Resources', 75),
    ('CROSS-VID', 'Educational Videos', 100),
    ('CROSS-GUIDE', 'Community Discussion Guides', 40),
]
cross = []
for prefix, title, estimate in cross_types:
    cross.append({'prefix': prefix, 'title': title, 'estimated_assets': estimate, 'status': 'planned', 'completion_pct': 0})
    for i in range(3):
        add_item(prefix, 0, 'cross-domain', f"{title} — Slot {i + 1}", 'cross-domain', 'L1', 'explore', 'planned', 0)

for title, url in [
    ('Mission Control Dashboard', '/mission-control/'),
    ('Phase Registry', '/mission-control/phases.html'),
    ('Site Architecture Blueprint', '/mission-control/architecture.html'),
    ('Content Inventory', '/mission-control/inventory.html'),
    ('Build Registry', '/builds/'),
]:
    add_item('LAND', 1000, 'system', title, 'mission-control', 'L1', 'discover', 'published', 100, 'n/a', 'complete', url)

for c in cross:
    c['registered_items'] = len([i for i in items if i['id'].startswith(c['prefix'])])

published = sum(1 for i in items if i['status'] == 'published')
partial = sum(1 for i in items if i['status'] in ('partial', 'outlined'))
planned = sum(1 for i in items if i['status'] == 'planned')
avg_pct = round(sum(i['completion_pct'] for i in items) / len(items), 1)

v1_targets = {
    'educational_pages': 825,
    'timeline_entries': 250,
    'glossary_terms': 500,
    'charts_infographics': 200,
    'interactive_visualizations': 50,
    'downloadable_resources': 75,
    'faq_questions': 300,
    'primary_source_records': 500,
    'total_estimated': 2700
}

domains = [
    {'id': 1000, 'code': 'LAND', 'title': 'Landing Experience', 'purpose': 'Introduce the issue and orient new visitors.', 'estimated_assets': 25, 'registered': len([i for i in items if i['domain'] == 1000]), 'content_types': ['pages', 'sections', 'orientation']},
    {'id': 2000, 'code': 'HIST', 'title': 'Historical Foundation', 'purpose': 'Historical development leading to Citizens United.', 'estimated_assets': 80, 'registered': len([i for i in items if i['domain'] == 2000]), 'content_types': ['articles', 'timeline', 'legislation', 'biographies', 'charts']},
    {'id': 3000, 'code': 'CASE', 'title': 'The Case', 'purpose': 'Every aspect of Citizens United v. FEC.', 'estimated_assets': 90, 'registered': len([i for i in items if i['domain'] == 3000]), 'content_types': ['narrative', 'timeline', 'opinions', 'glossary']},
    {'id': 4000, 'code': 'CONST', 'title': 'Constitutional Principles', 'purpose': 'Constitutional doctrines behind the decision.', 'estimated_assets': 75, 'registered': len([i for i in items if i['domain'] == 4000]), 'content_types': ['articles', 'explainers', 'comparisons']},
    {'id': 5000, 'code': 'IMPACT', 'title': 'Impact', 'purpose': 'Measurable changes after 2010.', 'estimated_assets': 120, 'registered': len([i for i in items if i['domain'] == 5000]), 'content_types': ['reports', 'analysis', 'data stories']},
    {'id': 6000, 'code': 'MONEY', 'title': 'Money in Politics', 'purpose': 'How political money moves.', 'estimated_assets': 85, 'registered': len([i for i in items if i['domain'] == 6000]), 'content_types': ['diagrams', 'pathways', 'definitions']},
    {'id': 7000, 'code': 'DEBATE', 'title': 'Debate & Perspectives', 'purpose': 'Competing viewpoints fairly presented.', 'estimated_assets': 70, 'registered': len([i for i in items if i['domain'] == 7000]), 'content_types': ['arguments', 'myth-vs-fact', 'FAQ']},
    {'id': 8000, 'code': 'REFORM', 'title': 'Reform', 'purpose': 'Efforts to change campaign finance law.', 'estimated_assets': 100, 'registered': len([i for i in items if i['domain'] == 8000]), 'content_types': ['amendments', 'state initiatives', 'litigation']},
    {'id': 9000, 'code': 'CIVIC', 'title': 'Civic Leadership', 'purpose': 'Help visitors become educators.', 'estimated_assets': 80, 'registered': len([i for i in items if i['domain'] == 9000]), 'content_types': ['guides', 'toolkits', 'curriculum']},
    {'id': 10000, 'code': 'SOURCE', 'title': 'Source Library', 'purpose': 'Complete transparency.', 'estimated_assets': 500, 'registered': len([i for i in items if i['domain'] == 10000]), 'content_types': ['opinions', 'briefs', 'datasets', 'books']},
]

inventory = {
    'version': '1.0',
    'build': 6,
    'updated': today,
    'title': 'Content Master Registry v1.0',
    'route': '/mission-control/inventory.html',
    'data_file': '/data/content-inventory.json',
    'principle': 'Does this help someone understand Citizens United more clearly, more accurately, or more deeply?',
    'id_standard': 'Stable IDs: DOMAIN-NNN (e.g. CASE-001, HIST-014, IMPACT-037). Nothing is created without first existing here.',
    'status_lifecycle': [
        'planned', 'researching', 'outlined', 'drafting', 'technical_review',
        'fact_check', 'citation_review', 'editorial_review', 'ready_for_publication',
        'published', 'monitoring', 'revision_needed', 'archived'
    ],
    'metadata_standard': [
        'id', 'title', 'domain', 'parent_section', 'reader_level', 'reader_stage',
        'reading_time', 'difficulty', 'audience', 'sources_required', 'sources_complete',
        'status', 'completion_pct', 'source_status', 'review_status', 'version', 'updated',
        'url', 'related', 'mission_control'
    ],
    'v1_targets': v1_targets,
    'domains': domains,
    'cross_domain': cross,
    'summary': {
        'registered_items': len(items),
        'published': published,
        'partial_or_outlined': partial,
        'planned': planned,
        'average_completion_pct': avg_pct,
        'v1_target_total': v1_targets['total_estimated'],
        'registry_coverage_pct': round(len(items) / v1_targets['total_estimated'] * 100, 1)
    },
    'items': items
}

out = root / 'data/content-inventory.json'
with open(out, 'w', newline='\n') as f:
    json.dump(inventory, f, indent=2)
    f.write('\n')
print(f"Wrote {len(items)} items")
