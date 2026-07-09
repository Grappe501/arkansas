"""
Generate data/content-production-factory.json — Build #27 Content Production Factory v1.0.
Aligns with content-inventory.json lifecycle where applicable.
"""
import json
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

inv_path = root / 'data/content-inventory.json'
inv = {}
assets = []
if inv_path.exists():
    with open(inv_path) as f:
        inv = json.load(f)
    assets = inv.get('items', inv.get('assets', []))

status_counts = Counter(a.get('status', 'unknown') for a in assets)
published = status_counts.get('published', 0)
drafting = sum(status_counts.get(s, 0) for s in ('drafting', 'outlined', 'researching'))
review = sum(status_counts.get(s, 0) for s in (
    'technical_review', 'fact_check', 'citation_review', 'editorial_review', 'ready_for_publication'
))
planned = status_counts.get('planned', 0)

CONTENT_TYPES = [
    {
        'id': 'CPF-CT-01', 'title': 'Educational Articles', 'template_id': 'TPL-EDU',
        'examples': ['What is Citizens United?', 'What is a Super PAC?', 'Understanding Independent Expenditures'],
        'status': 'partial', 'notes': 'Start-here and hall pages serve as interim L1',
    },
    {
        'id': 'CPF-CT-02', 'title': 'Historical Articles', 'template_id': 'TPL-HIST',
        'examples': ['Watergate', 'The Tillman Act', 'The Bipartisan Campaign Reform Act'],
        'status': 'partial', 'notes': 'Hall 1 scaffold; deep historical articles not written',
    },
    {
        'id': 'CPF-CT-03', 'title': 'Supreme Court Case Guides', 'template_id': 'TPL-CASE',
        'sections': ['Background', 'Facts', 'Questions Presented', 'Holding', 'Majority Opinion', 'Dissents', 'Long-Term Impact'],
        'examples': ['Citizens United v. FEC'],
        'status': 'planned',
    },
    {
        'id': 'CPF-CT-04', 'title': 'Constitutional Explainers', 'template_id': 'TPL-CONST',
        'examples': ['Political Speech', 'Corporate Speech', 'Judicial Review', 'Strict Scrutiny'],
        'status': 'planned',
    },
    {
        'id': 'CPF-CT-05', 'title': 'Data Stories', 'template_id': 'TPL-DATA',
        'examples': ['Political spending trends', 'Independent expenditures', 'Disclosure requirements'],
        'status': 'planned', 'notes': 'No interactive charts yet',
    },
    {
        'id': 'CPF-CT-06', 'title': 'FAQ Articles', 'template_id': 'TPL-FAQ',
        'examples': ['Did Citizens United create Super PACs?', 'Can corporations contribute directly?', 'What is dark money?'],
        'status': 'partial', 'notes': 'FAQ growth tracked in MC; dedicated FAQ pages sparse',
    },
    {
        'id': 'CPF-CT-07', 'title': 'Arkansas Education Guides', 'template_id': 'TPL-AR',
        'examples': ['Host a community conversation', 'Arkansas legislative process', 'Ballot initiative basics'],
        'status': 'partial', 'notes': 'Teach/educate pages partial; not full article factory output',
    },
]

ARTICLE_STRUCTURE = [
    'Plain-language summary', 'Why it matters', 'Historical context', 'Detailed explanation',
    'Supporting evidence', 'Common misconceptions', 'Frequently asked questions',
    'Related topics', 'Primary sources', 'Community education suggestions'
]

READING_LEVELS = [
    {'level': 1, 'title': 'One-minute explanation', 'facts_depth': 'L1', 'status': 'partial'},
    {'level': 2, 'title': 'Five-minute explanation', 'facts_depth': 'L2', 'status': 'partial'},
    {'level': 3, 'title': 'Full educational article', 'facts_depth': 'L3', 'status': 'planned'},
    {'level': 4, 'title': 'Research and primary sources', 'facts_depth': 'L4', 'status': 'planned'},
]

WORKFLOW_STAGES = [
    {'stage': 1, 'title': 'Topic Approved', 'inventory_status': 'planned', 'status': 'defined'},
    {'stage': 2, 'title': 'Research Assigned', 'inventory_status': 'researching', 'status': 'defined'},
    {'stage': 3, 'title': 'Source Collection', 'inventory_status': 'researching', 'status': 'defined'},
    {'stage': 4, 'title': 'Outline Complete', 'inventory_status': 'outlined', 'status': 'defined'},
    {'stage': 5, 'title': 'First Draft', 'inventory_status': 'drafting', 'status': 'defined'},
    {'stage': 6, 'title': 'Fact Verification', 'inventory_status': 'fact_check', 'status': 'partial'},
    {'stage': 7, 'title': 'Citation Review', 'inventory_status': 'citation_review', 'status': 'partial'},
    {'stage': 8, 'title': 'Editorial Review', 'inventory_status': 'editorial_review', 'status': 'defined'},
    {'stage': 9, 'title': 'Accessibility Review', 'inventory_status': 'technical_review', 'status': 'planned'},
    {'stage': 10, 'title': 'Published', 'inventory_status': 'published', 'status': 'partial'},
    {'stage': 11, 'title': 'Scheduled Review', 'inventory_status': 'monitoring', 'status': 'planned'},
]

SOURCE_REQUIREMENTS = [
    'Primary sources used', 'Government sources used', 'Academic sources used',
    'Supporting journalism when appropriate', 'Last verification date'
]

VISUAL_TYPES = [
    'Timelines', 'Charts', 'Infographics', 'Flow diagrams', 'Comparison tables', 'Maps'
]

INTERNAL_LINK_TARGETS = [
    'Related history', 'Relevant Supreme Court cases', 'Constitutional principles',
    'Data', 'Source documents', 'Community education resources'
]

QUALITY_GATES = [
    'Is it understandable?', 'Is it accurate?', 'Are the sources visible?',
    'Does it distinguish fact from interpretation?', 'Does it explain why the topic matters?',
    'Does it help readers continue learning?'
]

DASHBOARD_METRICS = [
    {'id': 'CPF-DM-01', 'title': 'Planned articles', 'source': 'content-inventory', 'current': planned, 'status': 'partial'},
    {'id': 'CPF-DM-02', 'title': 'Articles in research', 'source': 'content-inventory', 'current': status_counts.get('researching', 0), 'status': 'partial'},
    {'id': 'CPF-DM-03', 'title': 'Articles being written', 'source': 'content-inventory', 'current': drafting, 'status': 'partial'},
    {'id': 'CPF-DM-04', 'title': 'Articles under review', 'source': 'content-inventory', 'current': review, 'status': 'partial'},
    {'id': 'CPF-DM-05', 'title': 'Published articles', 'source': 'content-inventory', 'current': published, 'status': 'partial'},
    {'id': 'CPF-DM-06', 'title': 'Articles needing updates', 'source': 'content-inventory', 'current': status_counts.get('revision_needed', 0), 'status': 'planned'},
    {'id': 'CPF-DM-07', 'title': 'Citation completeness', 'source': 'computed', 'current': None, 'status': 'planned'},
    {'id': 'CPF-DM-08', 'title': 'Reading-level coverage', 'source': 'facts-framework', 'current': None, 'status': 'partial'},
    {'id': 'CPF-DM-09', 'title': 'Visual coverage', 'source': 'computed', 'current': None, 'status': 'planned'},
]

EVERGREEN_REVIEW = [
    {'topic': 'Core constitutional topics', 'interval_months': 24, 'status': 'defined'},
    {'topic': 'Historical articles', 'interval_months': 36, 'status': 'defined'},
    {'topic': 'Current legal developments', 'interval_months': 12, 'status': 'defined'},
    {'topic': 'Arkansas legislative content', 'interval': 'After each regular session', 'status': 'defined'},
    {'topic': 'Spending data', 'interval': 'When updated datasets available', 'status': 'defined'},
]

INSTITUTIONAL_VOICE = [
    'Calm', 'Clear', 'Respectful', 'Evidence-based', 'Accessible', 'Thorough', 'Transparent'
]

by_type_status = Counter(ct['status'] for ct in CONTENT_TYPES)
status_weights = {'live': 100, 'partial': 50, 'defined': 30, 'planned': 10}
type_readiness = round(sum(status_weights.get(ct['status'], 5) for ct in CONTENT_TYPES) / max(len(CONTENT_TYPES), 1))
workflow_defined = len([w for w in WORKFLOW_STAGES if w['status'] in ('defined', 'partial')])
factory_readiness = min(round((type_readiness * 0.4 + workflow_defined / len(WORKFLOW_STAGES) * 100 * 0.35 + (published / max(len(assets), 1) * 100) * 0.25)), 28)

out = {
    'version': '1.0',
    'build': 27,
    'updated': today,
    'title': 'Content Production Factory v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/content-factory.html',
    'constitution': '/docs/CONTENT_PRODUCTION_FACTORY.md',
    'purpose': 'One institution, one voice — structured production for hundreds of educational assets.',
    'editorial_mission': [
        'Increase understanding', 'Increase trust', 'Encourage continued learning'
    ],
    'governing_principle': 'Build a permanent educational library — never chase attention.',
    'content_types': CONTENT_TYPES,
    'content_type_count': len(CONTENT_TYPES),
    'article_structure': ARTICLE_STRUCTURE,
    'reading_levels': READING_LEVELS,
    'workflow_stages': WORKFLOW_STAGES,
    'source_requirements': SOURCE_REQUIREMENTS,
    'visual_types': VISUAL_TYPES,
    'internal_link_targets': INTERNAL_LINK_TARGETS,
    'quality_gates': QUALITY_GATES,
    'dashboard_metrics': DASHBOARD_METRICS,
    'evergreen_review': EVERGREEN_REVIEW,
    'institutional_voice': INSTITUTIONAL_VOICE,
    'inventory_alignment': {
        'registry': '/data/content-inventory.json',
        'dashboard': '/mission-control/inventory.html',
        'build': 6,
        'lifecycle_stages': inv.get('status_lifecycle', []),
        'total_assets_registered': len(assets),
        'status_breakdown': dict(status_counts),
    },
    'related_registries': [
        {'title': 'Content Inventory', 'route': '/mission-control/inventory.html', 'build': 6},
        {'title': 'Facts Framework', 'route': '/mission-control/facts.html', 'build': 18},
        {'title': 'Research Framework', 'route': '/mission-control/research.html', 'build': 10},
        {'title': 'Knowledge Atlas', 'route': '/mission-control/atlas.html', 'build': 19},
        {'title': 'MRID System', 'route': '/mission-control/mrid.html', 'build': 7},
    ],
    'summary': {
        'content_types': len(CONTENT_TYPES),
        'article_structure_sections': len(ARTICLE_STRUCTURE),
        'workflow_stages': len(WORKFLOW_STAGES),
        'reading_levels': len(READING_LEVELS),
        'quality_gates': len(QUALITY_GATES),
        'dashboard_metrics': len(DASHBOARD_METRICS),
        'evergreen_policies': len(EVERGREEN_REVIEW),
        'assets_registered': len(assets),
        'assets_published': published,
        'assets_in_pipeline': drafting + review,
        'by_content_type_status': dict(by_type_status),
        'factory_readiness_pct': factory_readiness,
        'automated_review_scheduling': False,
        'workflow_dashboard_live': False,
    },
    'catalog_gaps': [
        'No unified factory dashboard tracking all workflow stages per article',
        'Most registered assets remain planned or L1 stub',
        'Case guide and constitutional explainer templates not implemented',
        'Citation completeness not computed automatically',
        'Evergreen review scheduling not automated',
        'Visual coverage tracking not built',
        'L3/L4 reading levels sparse across content',
        'Accessibility review stage not operational',
    ],
    'recommended_next_build': {
        'number': 28,
        'title': 'Component Specifications with Props/States',
        'note': 'Map article structure sections to COMP-* components; wire factory dashboard to inventory.',
    },
}

path = root / 'data/content-production-factory.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Content Factory: {len(CONTENT_TYPES)} types, {len(assets)} assets, {factory_readiness}% readiness')
