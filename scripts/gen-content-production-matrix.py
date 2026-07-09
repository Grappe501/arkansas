"""
Generate data/content-production-matrix.json — Build #46 Master Content Production Matrix v1.0.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


def inv_to_matrix_domain(item):
    """Map Build #6 content-inventory item to matrix domain 1000–14000."""
    prefix = item['id'].split('-')[0]
    inv = item.get('domain')
    cross_map = {
        'CROSS-TIME': 13000, 'CROSS-GLOS': 6000, 'CROSS-FAQ': 6000,
        'CROSS-CHART': 13000, 'CROSS-DATA': 13000, 'CROSS-DL': 9000,
        'CROSS-VID': 12000, 'CROSS-GUIDE': 9000,
    }
    if prefix in cross_map:
        return cross_map[prefix]
    inv_map = {
        1000: 1000,   # LAND → Citizens United orientation
        2000: 2000,   # HIST → Campaign Finance History
        3000: 1000,   # CASE → Citizens United
        4000: 3000,   # CONST → Constitutional Education
        5000: 4000,   # IMPACT → Concepts / post-decision analysis
        6000: 4000,   # MONEY → Campaign Finance Concepts
        7000: 6000,   # DEBATE → Encyclopedia perspectives
        8000: 8000,   # REFORM → Solutions Center
        9000: 9000,   # CIVIC → Coalition Resources
        10000: 11000, # SOURCE → Research Library
    }
    return inv_map.get(inv, 1000)


def inv_to_production_stage(status):
    return {
        'planned': 'not_started',
        'outlined': 'outline',
        'partial': 'writing',
        'drafting': 'writing',
        'researching': 'research',
        'published': 'published',
    }.get(status, 'not_started')


def prefix_to_production_id(item_id):
    prefix = item_id.split('-')[0]
    mapping = {
        'LAND': 'ARTICLE', 'HIST': 'ARTICLE', 'CASE': 'CASE', 'CONST': 'ARTICLE',
        'IMPACT': 'ARTICLE', 'MONEY': 'ARTICLE', 'DEBATE': 'ARTICLE', 'REFORM': 'ARTICLE',
        'CIVIC': 'LESSON', 'SOURCE': 'SOURCE', 'CROSS-TIME': 'TIMELINE',
        'CROSS-GLOS': 'ARTICLE', 'CROSS-FAQ': 'ARTICLE', 'CROSS-CHART': 'INFOGRAPHIC',
        'CROSS-DATA': 'INFOGRAPHIC', 'CROSS-DL': 'ARTICLE', 'CROSS-VID': 'VIDEO',
        'CROSS-GUIDE': 'LESSON',
    }
    return mapping.get(prefix, 'ARTICLE')


DOMAINS = [
    {
        'id': 1000, 'code': 'CU', 'title': 'Citizens United',
        'purpose': 'Core educational pages about the case and its significance.',
        'examples': ['What is Citizens United?', 'Why the case matters', 'Majority opinion', 'Dissents', 'Long-term significance'],
        'estimated_assets': 40, 'content_types': ['articles', 'explainers', 'case narrative'],
        'registry': '/data/content-inventory.json', 'related_build': 6,
    },
    {
        'id': 2000, 'code': 'CFH', 'title': 'Campaign Finance History',
        'purpose': 'Historical development of campaign finance law.',
        'examples': ['Tillman Act', 'Watergate', 'FECA', 'Buckley', 'McConnell', 'BCRA', 'Austin'],
        'estimated_assets': 80, 'content_types': ['articles', 'timeline', 'legislation'],
        'registry': '/data/content-inventory.json', 'related_build': 6,
    },
    {
        'id': 3000, 'code': 'CON', 'title': 'Constitutional Education',
        'purpose': 'Constitutional doctrines behind the decision.',
        'examples': ['First Amendment', 'Political speech', 'Corporate speech', 'Judicial review', 'Originalism'],
        'estimated_assets': 75, 'content_types': ['explainers', 'comparisons', 'principles'],
        'registry': '/data/content-inventory.json', 'related_build': 6,
    },
    {
        'id': 4000, 'code': 'CFC', 'title': 'Campaign Finance Concepts',
        'purpose': 'Definitions and mechanics of modern campaign finance.',
        'examples': ['PAC', 'Super PAC', 'Independent expenditures', 'Hard money', 'Disclosure', 'Coordination'],
        'estimated_assets': 100, 'content_types': ['concept pages', 'diagrams', 'glossary'],
        'registry': '/data/content-inventory.json', 'related_build': 6,
    },
    {
        'id': 5000, 'code': 'SCL', 'title': 'Supreme Court Library',
        'purpose': 'Significant cases with summary, holding, and impact.',
        'examples': ['Summary', 'Timeline', 'Holding', 'Majority', 'Dissent', 'Historical impact'],
        'estimated_assets': 75, 'content_types': ['case entries', 'opinions', 'precedent maps'],
        'registry': '/data/content-inventory.json', 'related_build': 6,
    },
    {
        'id': 6000, 'code': 'ENC', 'title': 'Encyclopedia',
        'purpose': 'People, organizations, events, terms, concepts, historical moments.',
        'examples': ['People', 'Organizations', 'Events', 'Terms', 'Concepts'],
        'estimated_assets': 300, 'content_types': ['encyclopedia entries', 'definitions'],
        'registry': '/data/encyclopedia-knowledge-library.json', 'related_build': 33,
    },
    {
        'id': 7000, 'code': 'ARK', 'title': 'Arkansas Education',
        'purpose': 'Arkansas-specific civic and constitutional education.',
        'examples': ['Arkansas Constitution', 'Legislative process', 'Ballot initiative', 'Campaign finance law', 'Public records'],
        'estimated_assets': 100, 'content_types': ['county pages', 'dashboards', 'state guides'],
        'registry': '/data/arkansas-counties.json', 'related_build': 31,
    },
    {
        'id': 8000, 'code': 'SOL', 'title': 'Solutions Center',
        'purpose': 'Federal, Arkansas, transparency, and reform education.',
        'examples': ['Federal reforms', 'Arkansas initiatives', 'Transparency', 'Ballot initiative education'],
        'estimated_assets': 75, 'content_types': ['comparisons', 'model laws', 'pathways'],
        'registry': '/data/civic-action-lab.json', 'related_build': 42,
    },
    {
        'id': 9000, 'code': 'COA', 'title': 'Coalition Resources',
        'purpose': 'Organization toolkits and community education materials.',
        'examples': ['Presentation guides', 'Volunteer handbook', 'Facilitator manual', 'Recruitment resources'],
        'estimated_assets': 100, 'content_types': ['toolkits', 'guides', 'packets'],
        'registry': '/data/civic-ecosystem.json', 'related_build': 14,
    },
    {
        'id': 10000, 'code': 'ACA', 'title': 'Community Education Academy',
        'purpose': 'Leader development curriculum and certification.',
        'examples': ['Modules', 'Exercises', 'Quizzes', 'Speaker notes', 'Lesson plans'],
        'estimated_assets': 150, 'content_types': ['modules', 'lesson plans', 'certification'],
        'registry': '/data/education-academy.json', 'related_build': 28,
    },
    {
        'id': 11000, 'code': 'RES', 'title': 'Research Library',
        'purpose': 'Primary sources, government reports, academic papers, court documents.',
        'examples': ['Primary sources', 'Government reports', 'Academic papers', 'Court documents', 'Research summaries'],
        'estimated_assets': 500, 'content_types': ['source records', 'summaries', 'reading lists'],
        'registry': '/data/evidence-registry.json', 'related_build': 37,
    },
    {
        'id': 12000, 'code': 'MED', 'title': 'Multimedia',
        'purpose': 'Videos, animations, documentaries, audio, interactive graphics.',
        'examples': ['Videos', 'Animations', 'Documentaries', 'Podcasts', 'Presentations'],
        'estimated_assets': 250, 'content_types': ['video', 'audio', 'documentary'],
        'registry': '/data/media-studio.json', 'related_build': 39,
    },
    {
        'id': 13000, 'code': 'VIZ', 'title': 'Data Visualization',
        'purpose': 'Interactive charts, timelines, maps, money flow diagrams.',
        'examples': ['Interactive charts', 'Timelines', 'Maps', 'Money flow', 'Election data'],
        'estimated_assets': 150, 'content_types': ['charts', 'timelines', 'maps', 'graphs'],
        'registry': '/data/content-inventory.json', 'related_build': 6,
    },
    {
        'id': 14000, 'code': 'MC', 'title': 'Mission Control',
        'purpose': 'Progress reports, executive dashboards, county and coalition dashboards.',
        'examples': ['Executive dashboards', 'County dashboards', 'Research dashboards', 'Coalition dashboards'],
        'estimated_assets': 50, 'content_types': ['dashboards', 'reports', 'readiness screens'],
        'registry': '/data/mission-control.json', 'related_build': 25,
    },
]

PRODUCTION_STAGES = [
    'not_started', 'research', 'outline', 'writing', 'fact_review',
    'citation_review', 'visual_design', 'editorial_review', 'accessibility_review',
    'published', 'scheduled_review',
]

PRODUCTION_ID_PREFIXES = [
    'ARTICLE', 'CASE', 'TIMELINE', 'VIDEO', 'INFOGRAPHIC', 'LESSON',
    'SOURCE', 'COUNTY', 'MODELLAW', 'CLAIM',
]

FUTURE_AUTOMATION = [
    'Automatic production reports', 'Research reminders', 'Editorial reminders',
    'Broken citation alerts', 'Content freshness alerts', 'Knowledge gap reports',
    'AI-assisted production planning',
]

# Load live data
ci = load_json(root / 'data/content-inventory.json')
items = ci.get('items', [])
el = load_json(root / 'data/evidence-ledger.json')
ev = load_json(root / 'data/evidence-registry.json')
ms = load_json(root / 'data/media-studio.json')
ac = load_json(root / 'data/arkansas-counties.json')
ea = load_json(root / 'data/education-academy.json')
mc = load_json(root / 'data/mission-control.json')

domain_stats = defaultdict(lambda: {
    'registered': 0, 'published': 0, 'in_pipeline': 0, 'planned': 0, 'stages': Counter(),
})

for item in items:
    md = inv_to_matrix_domain(item)
    st = item.get('status', 'planned')
    stage = inv_to_production_stage(st)
    domain_stats[md]['registered'] += 1
    domain_stats[md]['stages'][stage] += 1
    if st == 'published':
        domain_stats[md]['published'] += 1
    elif st in ('partial', 'outlined', 'drafting', 'researching'):
        domain_stats[md]['in_pipeline'] += 1
    else:
        domain_stats[md]['planned'] += 1

# Supplemental registrations not in content-inventory
domain_stats[7000]['registered'] += len(ac.get('counties', []))
domain_stats[7000]['planned'] += len(ac.get('counties', []))
domain_stats[11000]['registered'] += len(ev.get('items', ev.get('sources', [])))
domain_stats[11000]['in_pipeline'] += len(ev.get('items', ev.get('sources', [])))
domain_stats[12000]['registered'] += ms.get('summary', {}).get('videos_catalogued', 0)
domain_stats[14000]['registered'] += len(mc.get('build_map', []))
domain_stats[14000]['published'] += len([b for b in mc.get('build_map', []) if b.get('status') == 'complete'])
domain_stats[14000]['in_pipeline'] += len([b for b in mc.get('build_map', []) if b.get('status') != 'complete'])

academy_modules = len(ea.get('curriculum_modules', ea.get('modules', [])))
if academy_modules:
    domain_stats[10000]['registered'] += academy_modules
    domain_stats[10000]['planned'] += academy_modules

domains_out = []
for d in DOMAINS:
    stats = domain_stats[d['id']]
    est = d['estimated_assets']
    reg = stats['registered']
    pub = stats['published']
    domains_out.append({
        **d,
        'registered': reg,
        'published': pub,
        'in_pipeline': stats['in_pipeline'],
        'planned': stats['planned'],
        'queue_coverage_pct': round(min(100, reg / est * 100), 1) if est else 0,
        'completion_pct': round(min(100, pub / est * 100), 1) if est else 0,
        'production_stages': dict(stats['stages']),
        'status': 'live' if pub > 0 else 'partial' if reg > 0 else 'planned',
    })

total_estimated = sum(d['estimated_assets'] for d in DOMAINS)
total_registered = sum(d['registered'] for d in domains_out)
total_published = sum(d['published'] for d in domains_out)
mc_domain = next(d for d in domains_out if d['id'] == 14000)
educational_estimated = total_estimated - mc_domain['estimated_assets']
educational_registered = total_registered - mc_domain['registered']
educational_published = total_published - mc_domain['published']
total_pipeline = sum(d['in_pipeline'] for d in domains_out)

# Executive production dashboard counts
articles = [i for i in items if i.get('category') in ('article', 'depth', 'hall-overview')]
articles_pub = sum(1 for i in articles if i.get('status') == 'published')
cases_pub = sum(1 for i in items if i['id'].startswith('CASE') and i.get('status') == 'published')
encyclopedia_reg = domain_stats[6000]['registered']
videos_pub = ms.get('summary', {}).get('videos_published', 0)
county_pages = len(ac.get('counties', []))
sources_reg = len(ev.get('items', ev.get('sources', [])))
claims_verified = el.get('summary', {}).get('claims_verified', 0)
infographics_reg = domain_stats[13000]['registered']
lessons_reg = sum(1 for i in items if i['id'].startswith('CIVIC'))
presentation_kits = sum(1 for i in items if 'toolkit' in i.get('title', '').lower() or 'presentation' in i.get('title', '').lower())

overall_completion = round(educational_published / educational_estimated * 100, 1) if educational_estimated else 0

EXEC_DASHBOARD = [
    {'id': 'PROD-01', 'title': 'Articles Completed', 'current': articles_pub, 'target': '300–500', 'status': 'partial'},
    {'id': 'PROD-02', 'title': 'Encyclopedia Entries', 'current': 0, 'target': '200–400', 'status': 'planned', 'note': f'{encyclopedia_reg} registered in queue — 0 published'},
    {'id': 'PROD-03', 'title': 'Cases Completed', 'current': cases_pub, 'target': 75, 'status': 'partial'},
    {'id': 'PROD-04', 'title': 'Videos Produced', 'current': videos_pub, 'target': '100+', 'status': 'planned'},
    {'id': 'PROD-05', 'title': 'County Pages', 'current': 0, 'target': 75, 'status': 'planned', 'note': f'{county_pages} county stubs registered'},
    {'id': 'PROD-06', 'title': 'Research Sources', 'current': sources_reg, 'target': '500+', 'status': 'partial'},
    {'id': 'PROD-07', 'title': 'Claims Verified', 'current': claims_verified, 'target': 500, 'status': 'partial'},
    {'id': 'PROD-08', 'title': 'Infographics', 'current': 0, 'target': '200–300', 'status': 'planned', 'note': f'{infographics_reg} registered in queue'},
    {'id': 'PROD-09', 'title': 'Lesson Plans', 'current': 0, 'target': 150, 'status': 'planned', 'note': f'{lessons_reg} CIVIC items registered'},
    {'id': 'PROD-10', 'title': 'Presentation Kits', 'current': presentation_kits, 'target': '50+', 'status': 'partial'},
    {'id': 'PROD-11', 'title': 'Overall Institutional Completion', 'current': f'{overall_completion}%', 'target': '100%', 'status': 'planned'},
]

# Production queue sample — published + in-pipeline first
priority = {'published': 0, 'partial': 1, 'outlined': 2, 'planned': 3}
sorted_items = sorted(items, key=lambda i: (priority.get(i.get('status', 'planned'), 9), i['id']))
queue = []
for item in sorted_items[:40]:
    pid = prefix_to_production_id(item['id'])
    queue.append({
        'production_id': item['id'],
        'id_prefix': pid,
        'title': item['title'],
        'matrix_domain': inv_to_matrix_domain(item),
        'stage': inv_to_production_stage(item.get('status', 'planned')),
        'status': item.get('status', 'planned'),
        'completion_pct': item.get('completion_pct', 0),
        'url': item.get('url'),
        'inventory_link': f"/mission-control/inventory.html#{item['id']}",
    })

CAPACITY = {
    'remaining_assets': educational_estimated - educational_published,
    'registered_in_queue': educational_registered,
    'queue_coverage_pct': round(educational_registered / educational_estimated * 100, 1) if educational_estimated else 0,
    'published_assets': educational_published,
    'mc_dashboards_complete': mc_domain['published'],
    'in_pipeline': total_pipeline,
    'avg_production_speed': 'Not measured — no velocity tracking',
    'research_backlog': f"{domain_stats[11000]['planned']} source slots + {el.get('summary', {}).get('claims_awaiting_review', 0)} claims awaiting review",
    'editorial_workload': f"{total_pipeline} assets in writing/outline stages",
    'review_workload': f"{el.get('summary', {}).get('evidence_awaiting_review', 0)} evidence items awaiting review",
    'expected_completion': 'Not estimated — capacity model not built',
    'status': 'documented',
}

MC_METRICS = [
    {'id': 'CPM-01', 'title': 'Content domains defined', 'status': 'live', 'current': f'{len(DOMAINS)}/14'},
    {'id': 'CPM-02', 'title': 'Educational assets registered', 'status': 'partial', 'current': f'{educational_registered}/{educational_estimated}'},
    {'id': 'CPM-03', 'title': 'Educational assets published', 'status': 'partial', 'current': f'{educational_published}/{educational_estimated}'},
    {'id': 'CPM-04', 'title': 'Production stage workflow', 'status': 'live', 'current': f'{len(PRODUCTION_STAGES)} stages'},
    {'id': 'CPM-05', 'title': 'Production ID prefixes', 'status': 'live', 'current': f'{len(PRODUCTION_ID_PREFIXES)} prefixes'},
    {'id': 'CPM-06', 'title': 'Executive production dashboard', 'status': 'partial', 'current': 'MC dashboard live — counts from registries'},
    {'id': 'CPM-07', 'title': 'Per-asset status tracking', 'status': 'partial', 'current': f'{len(items)} items in content-inventory'},
    {'id': 'CPM-08', 'title': 'Capacity planning model', 'status': 'planned', 'current': 'Estimates documented — no velocity'},
    {'id': 'CPM-09', 'title': 'Production automation', 'status': 'planned', 'current': '0 automations live'},
    {'id': 'CPM-10', 'title': 'Build sequencing engine', 'status': 'partial', 'current': 'recommended_next_build in registries'},
]

readiness_factors = [
    min(100, len(DOMAINS) / 14 * 100),
    min(100, educational_registered / educational_estimated * 100 * 2) if educational_estimated else 0,
    min(100, educational_published / educational_estimated * 100 * 10) if educational_estimated else 0,
    50,
    0,
    30,
]
production_matrix_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 46,
    'updated': today,
    'title': 'Master Content Production Matrix v1.0',
    'subtitle': 'Complete Content Inventory & Build Sequencing System',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/content-production-matrix.html',
    'constitution': '/docs/MASTER_CONTENT_PRODUCTION_MATRIX.md',
    'purpose': 'Design everything the institution must eventually contain — every asset ID\'d and queued.',
    'governing_principle': 'Vision into execution — every asset has a place, workflow, and purpose.',
    'long_term_vision': 'One of the largest educational collections devoted to a single Supreme Court decision — connected, researched, transparent.',
    'extends': [
        {'title': 'Content Inventory', 'build': 6, 'route': '/data/content-inventory.json'},
        {'title': 'MRID Traceability', 'build': 7, 'route': '/data/mrid-registry.json'},
        {'title': 'Content Production Factory', 'build': 27, 'route': '/data/content-production-factory.json'},
    ],
    'master_library_targets': {
        'educational_articles': '300–500',
        'encyclopedia_entries': '200–400',
        'timeline_events': '150–250',
        'constitutional_explainers': '100–200',
        'campaign_finance_concepts': '100–150',
        'charts_visualizations': '200–300',
        'arkansas_county_pages': 75,
        'county_education_dashboards': 75,
        'educational_videos': '100+',
        'presentation_toolkits': '50+',
        'primary_source_summaries': 'hundreds',
    },
    'domains_total': len(DOMAINS),
    'domains': domains_out,
    'production_stages': PRODUCTION_STAGES,
    'production_id_prefixes': PRODUCTION_ID_PREFIXES,
    'executive_production_dashboard': {
        'title': 'Master Production Dashboard',
        'status': 'partial',
        'metrics': EXEC_DASHBOARD,
        'overall_completion_pct': overall_completion,
    },
    'capacity_planning': CAPACITY,
    'future_automation': {
        'title': 'Future Automation',
        'status': 'planned',
        'capabilities': FUTURE_AUTOMATION,
        'editorial_gate': 'Human editorial judgment remains central',
    },
    'production_queue': {
        'title': 'Production Queue (sample)',
        'status': 'partial',
        'total_registered': len(items),
        'sample_size': len(queue),
        'items': queue,
        'full_registry': '/mission-control/inventory.html',
    },
    'mc_integration': {
        'title': 'Mission Control Production Matrix Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
    },
    'related_blueprints': [
        {'title': 'Systems Integration', 'route': '/data/systems-integration.json', 'build': 45},
        {'title': 'Institutional Roadmap', 'route': '/data/institutional-roadmap.json', 'build': 44},
        {'title': 'Content Production Factory', 'route': '/data/content-production-factory.json', 'build': 27},
        {'title': 'Master Curriculum', 'route': '/data/master-curriculum.json', 'build': 35},
    ],
    'summary': {
        'domains_total': len(DOMAINS),
        'institutional_target_total': total_estimated,
        'educational_target_total': educational_estimated,
        'assets_registered': total_registered,
        'educational_assets_registered': educational_registered,
        'assets_published': educational_published,
        'educational_assets_published': educational_published,
        'mc_dashboards_complete': mc_domain['published'],
        'assets_in_pipeline': total_pipeline,
        'assets_planned': educational_estimated - educational_published - total_pipeline,
        'queue_coverage_pct': round(educational_registered / educational_estimated * 100, 1) if educational_estimated else 0,
        'overall_completion_pct': overall_completion,
        'production_stages': len(PRODUCTION_STAGES),
        'content_inventory_items': len(items),
        'production_automation_live': False,
        'capacity_model_live': False,
        'production_matrix_readiness_pct': production_matrix_readiness,
    },
    'catalog_gaps': [
        f'Only {educational_registered}/{educational_estimated} educational assets registered — {round(100 - educational_registered/educational_estimated*100, 1) if educational_estimated else 100}% of master library not queued',
        f'Only {educational_published} educational assets published — {overall_completion}% institutional completion',
        '0 videos produced — multimedia domain empty',
        '0 county pages published — 75 stubs only',
        '0 encyclopedia entries published — glossary/timeline cross-domains planned only',
        'Production stages defined — not enforced in CMS or workflow tooling',
        'Capacity planning documented — no velocity or completion date model',
        'No production automation — reminders, citation alerts, freshness checks planned',
        'Build #6 inventory domain IDs differ from matrix domain IDs — mapping manual in gen script',
        'Component specifications still deferred — production UI widgets unmapped',
    ],
    'recommended_next_build': {
        'number': 50,
        'title': 'Component Specifications with Props/States',
        'note': 'Map stack status panels, deployment pipeline viz, environment badges, and monitoring widgets to COMP-* from Build #17.',
    },
}

path = root / 'data/content-production-matrix.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Content Production Matrix: {educational_registered} edu queued, {educational_published} edu published, {production_matrix_readiness}% readiness')
