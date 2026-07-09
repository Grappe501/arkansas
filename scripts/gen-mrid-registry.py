"""
Generate mrid-registry.json — Build #7
Master Requirement ID System & Traceability Framework
"""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

with open(root / 'data/content-inventory.json') as f:
    content = json.load(f)
with open(root / 'data/phase-registry.json') as f:
    phases = json.load(f)
with open(root / 'data/site-architecture.json') as f:
    arch = json.load(f)

# Content ID prefix → MRID domain
PREFIX_MAP = {
    'LAND': 'HOME',
    'HIST': 'HIST',
    'CASE': 'CASE',
    'CONST': 'CONST',
    'IMPACT': 'IMPACT',
    'MONEY': 'MONEY',
    'DEBATE': 'DEBATE',
    'REFORM': 'REFORM',
    'CIVIC': 'EDUCATE',
    'SOURCE': 'SOURCE',
    'ACTION': 'ACTION',
    'CROSS-TIME': 'DATA',
    'CROSS-GLOS': 'DATA',
    'CROSS-FAQ': 'DATA',
    'CROSS-CHART': 'DATA',
    'CROSS-DATA': 'DATA',
    'CROSS-DL': 'DATA',
    'CROSS-VID': 'DATA',
    'CROSS-GUIDE': 'EDUCATE',
}

# Map content status → MRID lifecycle
STATUS_TO_LIFECYCLE = {
    'planned': 'planned',
    'researching': 'researching',
    'outlined': 'planned',
    'drafting': 'building',
    'partial': 'building',
    'published': 'published',
    'monitoring': 'monitoring',
    'revision_needed': 'revision_required',
    'archived': 'retired',
}

DOMAIN_CODES = [
    {'code': 'GOV', 'title': 'Governance', 'purpose': 'Project governance, standards, planning documents.'},
    {'code': 'NAV', 'title': 'Navigation', 'purpose': 'Entire navigation system.'},
    {'code': 'HOME', 'title': 'Landing Experience', 'purpose': 'Homepage and orientation.'},
    {'code': 'HIST', 'title': 'Historical Foundation', 'purpose': 'Path to Citizens United.'},
    {'code': 'CASE', 'title': 'Citizens United Case', 'purpose': 'The Supreme Court case.'},
    {'code': 'CONST', 'title': 'Constitutional Principles', 'purpose': 'Legal doctrines behind the decision.'},
    {'code': 'IMPACT', 'title': 'Impact Analysis', 'purpose': 'Changes after 2010.'},
    {'code': 'MONEY', 'title': 'Money Flow', 'purpose': 'How political money moves.'},
    {'code': 'DEBATE', 'title': 'Perspectives', 'purpose': 'Competing viewpoints.'},
    {'code': 'REFORM', 'title': 'Reform', 'purpose': 'Modern reform efforts.'},
    {'code': 'EDUCATE', 'title': 'Community Education', 'purpose': 'Volunteer and educator resources.'},
    {'code': 'ACTION', 'title': 'Civic Action', 'purpose': 'Participation infrastructure.'},
    {'code': 'DATA', 'title': 'Research & Visualization', 'purpose': 'Datasets, charts, interactive modules.'},
    {'code': 'SOURCE', 'title': 'Source Library', 'purpose': 'Primary source archive.'},
    {'code': 'TECH', 'title': 'Technical Platform', 'purpose': 'GitHub, Netlify, search, analytics.'},
    {'code': 'DASH', 'title': 'Mission Control', 'purpose': 'Project operating system dashboards.'},
]

requirements = []
counters = {d['code']: 0 for d in DOMAIN_CODES}
content_mrid_map = {}


def next_mrid(domain):
    counters[domain] = counters.get(domain, 0) + 1
    return f"{domain}-{counters[domain]:03d}"


def add_req(domain, title, rtype, status='planned', pct=0, phase=1, **extra):
    mrid = next_mrid(domain)
    lifecycle = extra.get('lifecycle') or STATUS_TO_LIFECYCLE.get(status, 'planned')
    req = {
        'mrid': mrid,
        'domain': domain,
        'title': title,
        'type': rtype,
        'status': lifecycle,
        'completion_pct': pct,
        'phase': phase,
        'builds': extra.get('builds', []),
        'content_id': extra.get('content_id'),
        'url': extra.get('url'),
        'dependencies': extra.get('dependencies', []),
        'related': extra.get('related', []),
        'traceability': {
            'parent_phase': phase,
            'content_pages': [extra['content_id']] if extra.get('content_id') else [],
            'research_sources': extra.get('research_sources', []),
            'charts': extra.get('charts', []),
            'downloads': extra.get('downloads', []),
            'volunteer_resources': extra.get('volunteer_resources', []),
            'builds': extra.get('builds', []),
            'commits': extra.get('commits', []),
            'deployments': extra.get('deployments', []),
        },
        'last_modified': extra.get('last_modified', today),
        'review_status': extra.get('review_status', 'none'),
        'source_coverage': extra.get('source_coverage', 'none'),
        'public_readiness': extra.get('public_readiness', 0),
        'outstanding_tasks': extra.get('outstanding_tasks', []),
        'mission_control': f"/mission-control/mrid.html#{mrid}",
    }
    requirements.append(req)
    return mrid


# --- GOV: Governance ---
gov_items = [
    ('Project Constitution v1.0', 'document', 'published', 100, 1, [2], 'docs/CONSTITUTION.md'),
    ('Project Mission Statement', 'document', 'published', 100, 1, [1], '/builds/001-mission-statement.html'),
    ('Master Phase Registry v1.0', 'document', 'published', 100, 1, [4], '/mission-control/phases.html'),
    ('Master Site Architecture v1.0', 'document', 'published', 100, 2, [5], '/mission-control/architecture.html'),
    ('Master Content Inventory v1.0', 'document', 'published', 100, 2, [6], '/mission-control/inventory.html'),
    ('Master Requirement ID System v1.0', 'document', 'building', 80, 1, [7], '/mission-control/mrid.html'),
    ('Editorial Standards', 'document', 'published', 90, 1, [2], '/docs/EDITORIAL_CHECKLIST.md'),
    ('Citation Guide', 'document', 'published', 85, 1, [2], '/docs/CITATION_GUIDE.md'),
]
gov_mrids = {}
for title, rtype, st, pct, phase, builds, url in gov_items:
    gov_mrids[title] = add_req('GOV', title, rtype, st, pct, phase, builds=builds, url=url,
                               review_status='complete' if pct >= 100 else 'internal_review',
                               source_coverage='complete' if pct >= 100 else 'partial')

# --- NAV: Navigation ---
nav_items = [
    ('Primary Navigation', 'navigation', 'published', 70, 2, [5], '/', ['HOME-001']),
    ('Footer Navigation', 'navigation', 'published', 65, 2, [5], None, []),
    ('Breadcrumbs', 'navigation', 'partial', 40, 2, [5], None, []),
    ('Floating Action Hub', 'navigation', 'partial', 35, 10, [4, 5], '/action/share.html', ['ACTION-001']),
    ('Reader Journey Indicator', 'navigation', 'planned', 0, 2, [], None, []),
    ('Site Map / Explore', 'navigation', 'published', 60, 2, [5], '/explore/', ['HOME-010']),
    ('Secondary Navigation', 'navigation', 'planned', 5, 2, [5], None, []),
]
nav_mrids = {}
for title, rtype, st, pct, phase, builds, url, related in nav_items:
    nav_mrids[title] = add_req('NAV', title, rtype, st, pct, phase, builds=builds, url=url, related=related)

# --- TECH: Technical Platform ---
tech_items = [
    ('GitHub Repository', 'infrastructure', 'published', 85, 12, [1, 9], 'https://github.com/Grappe501/arkansas'),
    ('Netlify Deployment', 'infrastructure', 'published', 80, 12, [1, 11], 'https://arkansas-facts.netlify.app'),
    ('Netlify Forms', 'infrastructure', 'partial', 50, 12, [8], '/educate/'),
    ('Static Site Architecture', 'infrastructure', 'published', 90, 12, [1], '/'),
    ('Search', 'feature', 'planned', 0, 12, [], '/search'),
    ('Analytics', 'feature', 'planned', 0, 15, [], None),
    ('Accessibility Audit', 'feature', 'planned', 0, 14, [], None),
    ('URL Redirect Strategy', 'infrastructure', 'published', 75, 12, [5], '/netlify.toml'),
]
for title, rtype, st, pct, phase, builds, url in tech_items:
    add_req('TECH', title, rtype, st, pct, phase, builds=builds, url=url)

# --- DASH: Mission Control ---
dash_items = [
    ('Executive Summary', 'dashboard', 'published', 100, 0, [3], '/mission-control/'),
    ('Phase Dashboard', 'dashboard', 'published', 100, 0, [4], '/mission-control/phases.html'),
    ('Site Architecture Blueprint', 'dashboard', 'published', 100, 0, [5], '/mission-control/architecture.html'),
    ('Content Inventory Dashboard', 'dashboard', 'published', 100, 0, [6], '/mission-control/inventory.html'),
    ('MRID Traceability Dashboard', 'dashboard', 'building', 80, 0, [7], '/mission-control/mrid.html'),
    ('Progress Bars', 'dashboard', 'published', 100, 0, [3], '/mission-control/'),
    ('Living Build Map', 'dashboard', 'published', 90, 0, [3], '/mission-control/'),
    ('Deployment Monitor', 'dashboard', 'partial', 60, 0, [3], '/mission-control/'),
    ('Public Readiness Tracker', 'dashboard', 'published', 90, 0, [3], '/mission-control/'),
    ('Build DNA Records', 'dashboard', 'published', 95, 0, [3], '/mission-control/build.html'),
]
for title, rtype, st, pct, phase, builds, url in dash_items:
    add_req('DASH', title, rtype, st, pct, phase, builds=builds, url=url)

# --- Map content inventory items to MRIDs ---
def content_prefix(cid):
    for p in sorted(PREFIX_MAP.keys(), key=len, reverse=True):
        if cid.startswith(p + '-'):
            return p
    return None


def content_to_phase(item):
    domain = item.get('domain', 0)
    phase_map = {1000: 2, 2000: 3, 3000: 4, 4000: 5, 5000: 6, 6000: 6, 7000: 8,
                 8000: 9, 9000: 11, 10000: 13, 0: 7}
    return phase_map.get(domain, 2)


for item in content['items']:
    cid = item['id']
    prefix = content_prefix(cid)

    # System pages → DASH not HOME
    if item.get('category') == 'system':
        domain = 'DASH'
    elif prefix:
        domain = PREFIX_MAP[prefix]
    else:
        domain = 'DATA'

    # Skip duplicate depth slots for MRID v1 — register L1 and live items only
    if item.get('category') == 'depth' and item.get('status') == 'planned':
        continue

    st = item.get('status', 'planned')
    lifecycle = STATUS_TO_LIFECYCLE.get(st, 'planned')
    phase = content_to_phase(item)

    mrid = next_mrid(domain)
    content_mrid_map[cid] = mrid

    builds = []
    if st in ('published', 'partial', 'outlined'):
        builds = [1, 3, 4, 5, 6]

    req = {
        'mrid': mrid,
        'domain': domain,
        'title': item['title'],
        'type': item.get('category', 'content'),
        'status': lifecycle,
        'completion_pct': item.get('completion_pct', 0),
        'phase': phase,
        'builds': builds,
        'content_id': cid,
        'url': item.get('url'),
        'dependencies': [],
        'related': item.get('related', []),
        'traceability': {
            'parent_phase': phase,
            'content_pages': [cid],
            'research_sources': [],
            'charts': [],
            'downloads': [],
            'volunteer_resources': [],
            'builds': builds,
            'commits': [],
            'deployments': ['https://arkansas-facts.netlify.app'] if item.get('url') else [],
        },
        'last_modified': item.get('updated', today),
        'review_status': item.get('review_status', 'none'),
        'source_coverage': item.get('source_status', 'none'),
        'public_readiness': item.get('completion_pct', 0) if st == 'published' else 0,
        'outstanding_tasks': [] if st == 'published' else ['Draft content'],
        'mission_control': f"/mission-control/mrid.html#{mrid}",
        'reader_level': item.get('reader_level'),
        'parent_section': item.get('parent_section'),
    }
    requirements.append(req)

# Wire key dependencies
mrid_index = {r['mrid']: r for r in requirements}
for r in requirements:
    if r['domain'] == 'CASE' and r.get('reader_level') == 'L1' and 'Overview' in r['title']:
        r['dependencies'] = [x for x in [mrid_index.get(k, {}).get('mrid') for k in []] if x]
    if r['content_id'] == 'REFORM-034':
        r['related'] = [content_mrid_map.get('REFORM-014'), content_mrid_map.get('REFORM-018')]
        r['traceability']['research_sources'] = ['content/entries/001-montana-hawaii-citizens-united.json']

# Link NAV-004 to action hub
if 'Floating Action Hub' in nav_mrids:
    hub = nav_mrids['Floating Action Hub']
    if hub in mrid_index:
        mrid_index[hub]['dependencies'] = [r['mrid'] for r in requirements if r['domain'] == 'ACTION' and r.get('completion_pct', 0) > 0][:3]

# Summary stats
published = sum(1 for r in requirements if r['status'] == 'published')
building = sum(1 for r in requirements if r['status'] in ('building', 'planned', 'designing'))
total = len(requirements)

registry = {
    'version': '1.0',
    'build': 7,
    'updated': today,
    'title': 'Master Requirement Identification System v1.0',
    'route': '/mission-control/mrid.html',
    'data_file': '/data/mrid-registry.json',
    'principle': 'If it cannot be identified, it cannot be measured. If it cannot be measured, it cannot be managed.',
    'id_rules': [
        'Permanent', 'Unique', 'Human-readable', 'Searchable',
        'Stable across versions', 'Never reused after retirement', 'Traceable to parent domain'
    ],
    'domain_codes': DOMAIN_CODES,
    'lifecycle': [
        'proposed', 'approved', 'planned', 'researching', 'designing', 'building',
        'internal_review', 'testing', 'published', 'monitoring', 'revision_required', 'retired'
    ],
    'traceability_fields': [
        'parent_phase', 'content_pages', 'research_sources', 'charts', 'downloads',
        'volunteer_resources', 'builds', 'commits', 'deployments', 'testing_records'
    ],
    'content_id_map': content_mrid_map,
    'summary': {
        'total_requirements': total,
        'published': published,
        'building_or_planned': building,
        'domains_active': len([d for d in DOMAIN_CODES if counters.get(d['code'], 0) > 0]),
        'content_items_linked': len(content_mrid_map),
    },
    'requirements': requirements,
}

out = root / 'data/mrid-registry.json'
with open(out, 'w', newline='\n') as f:
    json.dump(registry, f, indent=2)
    f.write('\n')

# Add mrid field to content inventory items
for item in content['items']:
    if item['id'] in content_mrid_map:
        item['mrid'] = content_mrid_map[item['id']]
content['mrid_system'] = '/data/mrid-registry.json'
content['updated'] = today
with open(root / 'data/content-inventory.json', 'w', newline='\n') as f:
    json.dump(content, f, indent=2)
    f.write('\n')

print(f"MRIDs: {total}, linked content: {len(content_mrid_map)}")
for code in DOMAIN_CODES:
    c = counters.get(code['code'], 0)
    if c:
        print(f"  {code['code']}: {c}")
