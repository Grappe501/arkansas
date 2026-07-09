"""
Generate data/research-observatory.json — Build #29 Research Observatory v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

ev_path = root / 'data/evidence-registry.json'
ev_summary = {}
gaps = []
if ev_path.exists():
    with open(ev_path) as f:
        ev = json.load(f)
    ev_summary = ev.get('summary', {})
    gaps = ev_summary.get('research_gaps', [])

mc_path = root / 'data/mission-control.json'
research_cats = []
if mc_path.exists():
    with open(mc_path) as f:
        mc = json.load(f)
    research_cats = mc.get('research_readiness', [])

DIVISIONS = [
    {
        'id': 'OBS-DIV-A', 'letter': 'A', 'title': 'Supreme Court Monitor',
        'tracks': ['New Supreme Court decisions', 'Petitions accepted for review', 'Campaign finance litigation', 'Constitutional developments'],
        'outputs': ['Educational summaries', 'Timeline updates', 'Related lesson updates', 'Source additions'],
        'status': 'partial', 'route': '/mission-control/research.html', 'notes': '1 CU opinion in evidence registry; monitor not automated',
    },
    {
        'id': 'OBS-DIV-B', 'letter': 'B', 'title': 'Federal Legislative Monitor',
        'tracks': ['Congress', 'Campaign finance legislation', 'Disclosure proposals', 'Constitutional amendment proposals', 'FEC oversight'],
        'outputs': ['Educational explainers', 'Legislative comparison pages', 'Status dashboards', 'Historical tracking'],
        'status': 'planned',
    },
    {
        'id': 'OBS-DIV-C', 'letter': 'C', 'title': 'Arkansas Legislative Monitor',
        'tracks': ['Bills introduced', 'Committee activity', 'Floor votes', 'Campaign finance legislation', 'Ethics legislation', 'Election administration'],
        'outputs': ['Arkansas legislative summaries', 'Bill explainers', 'Educational timelines', 'Resource updates'],
        'status': 'planned', 'notes': 'No live bill tracking feed',
    },
    {
        'id': 'OBS-DIV-D', 'letter': 'D', 'title': 'Ballot Initiative Observatory',
        'tracks': ['Arkansas', 'Montana', 'Hawaii', 'Other states with notable developments'],
        'outputs': ['Plain-language summary', 'Current status', 'Historical context', 'Educational analysis', 'Official material links'],
        'status': 'partial', 'route': '/halls/montana-hawaii.html', 'notes': 'MT/HI content live; AR initiative monitor not built',
    },
    {
        'id': 'OBS-DIV-E', 'letter': 'E', 'title': 'Academic Research Monitor',
        'tracks': ['Peer-reviewed scholarship', 'Law review articles', 'University publications', 'Government research', 'Empirical studies'],
        'outputs': ['Research summaries', 'Citation updates', 'Evidence reviews'],
        'status': 'planned', 'notes': f'{ev_summary.get("academic_sources", 0)} academic sources cataloged',
    },
    {
        'id': 'OBS-DIV-F', 'letter': 'F', 'title': 'Campaign Spending Observatory',
        'tracks': ['Independent expenditures', 'Outside spending', 'Super PAC activity', 'Disclosure trends', 'Election spending statistics'],
        'outputs': ['Data stories with context', 'Chart updates', 'Source transparency notes'],
        'status': 'planned', 'notes': 'FEC/OpenSecrets datasets not integrated',
    },
]

WORKFLOW_STAGES = [
    {'stage': 1, 'title': 'Identified', 'status': 'defined'},
    {'stage': 2, 'title': 'Collected', 'status': 'partial'},
    {'stage': 3, 'title': 'Verified', 'status': 'partial'},
    {'stage': 4, 'title': 'Reviewed', 'status': 'partial'},
    {'stage': 5, 'title': 'Categorized', 'status': 'defined'},
    {'stage': 6, 'title': 'Educational summary drafted', 'status': 'planned'},
    {'stage': 7, 'title': 'Source documentation completed', 'status': 'partial'},
    {'stage': 8, 'title': 'Mission Control updated', 'status': 'partial'},
    {'stage': 9, 'title': 'Published when ready', 'status': 'partial'},
]

PRIORITY_LEVELS = [
    {
        'id': 'OBS-P1', 'level': 1, 'title': 'Educational accuracy',
        'examples': ['New Supreme Court rulings', 'Significant federal legislation', 'Arkansas statutory changes'],
        'status': 'defined',
    },
    {
        'id': 'OBS-P2', 'level': 2, 'title': 'Major public developments',
        'examples': ['Significant ballot initiatives', 'Large empirical studies', 'Major regulatory actions'],
        'status': 'defined',
    },
    {
        'id': 'OBS-P3', 'level': 3, 'title': 'Long-term educational improvements',
        'examples': ['New books', 'Historical discoveries', 'Additional datasets'],
        'status': 'defined',
    },
]

LEGISLATIVE_PAGE_SECTIONS = [
    'Overview', 'Current status', 'Key provisions', 'Historical context',
    'Related constitutional issues', 'Related educational resources', 'Official source documents'
]

RESEARCH_GAPS = [
    {'topic': gap, 'source': 'evidence-registry', 'status': 'tracked'}
    for gap in gaps
] + [
    {'topic': 'Charts requiring refreshed data', 'source': 'content-factory', 'status': 'planned'},
    {'topic': 'Counties lacking Arkansas-specific resources', 'source': 'county-coalition-index', 'status': 'planned'},
    {'topic': 'FAQs without sufficient coverage', 'source': 'ai-knowledge-engine', 'status': 'planned'},
    {'topic': 'Articles needing citation review', 'source': 'content-inventory', 'status': 'planned'},
]

DASHBOARD_PANELS = [
    {'id': 'OBS-DB-01', 'title': 'Supreme Court developments', 'current': 1, 'status': 'partial'},
    {'id': 'OBS-DB-02', 'title': 'Federal legislation monitored', 'current': 0, 'status': 'planned'},
    {'id': 'OBS-DB-03', 'title': 'Arkansas legislation monitored', 'current': 0, 'status': 'planned'},
    {'id': 'OBS-DB-04', 'title': 'Ballot initiatives under review', 'current': 2, 'status': 'partial'},
    {'id': 'OBS-DB-05', 'title': 'New research publications', 'current': ev_summary.get('total', 14), 'status': 'partial'},
    {'id': 'OBS-DB-06', 'title': 'Data updates pending', 'current': ev_summary.get('needing_updates', 4), 'status': 'partial'},
    {'id': 'OBS-DB-07', 'title': 'Articles awaiting revision', 'current': 0, 'status': 'planned'},
    {'id': 'OBS-DB-08', 'title': 'Scheduled review dates', 'current': 0, 'status': 'planned'},
]

COMMUNITY_CONTRIBUTIONS = [
    'Additional sources', 'Historical documents', 'Academic research',
    'Arkansas legislative developments', 'Public records'
]

FUTURE_ALERTS = [
    {'alert': 'New campaign finance case accepted by Supreme Court', 'status': 'defined', 'automated': False},
    {'alert': 'Arkansas bill related to campaign finance advanced', 'status': 'defined', 'automated': False},
    {'alert': 'Major academic study published', 'status': 'defined', 'automated': False},
    {'alert': 'Political spending data updated', 'status': 'defined', 'automated': False},
]

by_div = {}
for d in DIVISIONS:
    by_div[d['status']] = by_div.get(d['status'], 0) + 1

status_weights = {'live': 100, 'partial': 42, 'defined': 28, 'planned': 8}
div_readiness = round(sum(status_weights.get(d['status'], 5) for d in DIVISIONS) / len(DIVISIONS))
observatory_readiness = min(div_readiness, 18)

out = {
    'version': '1.0',
    'build': 29,
    'updated': today,
    'title': 'Research Observatory v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/research-observatory.html',
    'legacy_route': '/mission-control/research.html',
    'constitution': '/docs/RESEARCH_OBSERVATORY.md',
    'purpose': 'Early warning system — monitor, verify, explain, educate. Never become a static website.',
    'mission': 'Most current, transparent, evidence-based resource on Citizens United for Arkansas citizens.',
    'governing_principle': 'Thoughtfully monitor developments and verify evidence — not react to every headline.',
    'divisions': DIVISIONS,
    'division_count': len(DIVISIONS),
    'workflow_stages': WORKFLOW_STAGES,
    'priority_levels': PRIORITY_LEVELS,
    'legislative_page_sections': LEGISLATIVE_PAGE_SECTIONS,
    'research_gaps': RESEARCH_GAPS,
    'dashboard_panels': DASHBOARD_PANELS,
    'community_contributions': COMMUNITY_CONTRIBUTIONS,
    'future_alerts': FUTURE_ALERTS,
    'mc_integration': [
        {'use': 'Content requiring revision', 'status': 'planned'},
        {'use': 'Research priorities', 'status': 'partial', 'source': 'research_gaps'},
        {'use': 'New educational opportunities', 'status': 'planned'},
        {'use': 'Emerging Arkansas topics', 'status': 'planned'},
        {'use': 'Primary source documentation gaps', 'status': 'partial', 'source': 'evidence-registry'},
    ],
    'related_registries': [
        {'title': 'Evidence Registry', 'route': '/data/evidence-registry.json', 'build': 10, 'records': ev_summary.get('total', 14)},
        {'title': 'Research Framework', 'route': '/data/research-framework.json', 'build': 10},
        {'title': 'Facts Framework', 'route': '/data/facts-registry.json', 'build': 18},
        {'title': 'Content Production Factory', 'route': '/data/content-production-factory.json', 'build': 27},
        {'title': 'AI Knowledge Engine', 'route': '/data/ai-knowledge-engine.json', 'build': 26},
    ],
    'research_readiness_categories': len(research_cats),
    'summary': {
        'divisions': len(DIVISIONS),
        'workflow_stages': len(WORKFLOW_STAGES),
        'priority_levels': len(PRIORITY_LEVELS),
        'research_gaps_tracked': len(RESEARCH_GAPS),
        'dashboard_panels': len(DASHBOARD_PANELS),
        'future_alerts_defined': len(FUTURE_ALERTS),
        'future_alerts_automated': 0,
        'evidence_records': ev_summary.get('total', 14),
        'evidence_needing_updates': ev_summary.get('needing_updates', 4),
        'citation_coverage_pct': ev_summary.get('citation_coverage_pct', 12),
        'divisions_partial': by_div.get('partial', 0),
        'divisions_planned': by_div.get('planned', 0),
        'automated_monitoring_live': False,
        'legislative_tracking_live': False,
        'observatory_readiness_pct': observatory_readiness,
    },
    'catalog_gaps': [
        'No automated monitoring feeds for SCOTUS, Congress, or Arkansas legislature',
        'Legislative tracking pages not built',
        'Campaign spending data not integrated',
        'Academic research monitor has 0 cataloged academic sources',
        'Future alerts defined but not automated — human review required',
        'Scheduled review dates not tracked in MC',
        'Community contribution review queue not operational',
        'Only 14 evidence records vs 500 v1 target',
    ],
    'recommended_next_build': {
        'number': 30,
        'title': 'Component Specifications with Props/States',
        'note': 'Map legislative tracking page structure to components; wire observatory dashboard to evidence registry.',
    },
}

path = root / 'data/research-observatory.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Research Observatory: {len(DIVISIONS)} divisions, {observatory_readiness}% readiness')
