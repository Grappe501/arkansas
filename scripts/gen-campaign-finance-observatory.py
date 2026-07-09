"""
Generate data/campaign-finance-observatory.json — Build #63.
Master Campaign Finance Data Observatory v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def load_json(path):
    if path.exists():
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}


mc = load_json(root / 'data/mission-control.json')
el = load_json(root / 'data/evidence-ledger.json')
lib = load_json(root / 'data/master-research-library.json')
cac = load_json(root / 'data/citizen-action-center.json')

ex = mc.get('executive', {})
evidence_items = el.get('summary', {}).get('evidence_items_total', 0)
library_docs = lib.get('summary', {}).get('documents_archived', 0)

# Honest zeros — no FEC/API feeds, no charts live
datasets_published = 0
charts_completed = 0
research_notes_completed = 0
methodology_reviews = 0
broken_data_links = 0
scheduled_updates = 0
arkansas_charts = 0

EIGHT_DIVISIONS = [
    {
        'id': 'CFO-DIV-1', 'number': 1, 'title': 'Historical Spending Explorer',
        'focus': 'Long-term spending trends and campaign finance milestones',
        'topics': [
            'Election cycles', 'Federal campaign spending', 'Historical comparisons',
            'Inflation-adjusted views', 'Major campaign finance milestones',
        ],
        'goal': 'Place Citizens United within a broader historical timeline',
        'status': 'planned',
    },
    {
        'id': 'CFO-DIV-2', 'number': 2, 'title': 'Independent Expenditure Explorer',
        'focus': 'Educational explanations supported by publicly available data',
        'topics': [
            'Independent expenditures', 'Reported spending over time',
            'Reporting requirements', 'Major trends', 'Frequently asked questions',
        ],
        'note': 'Distinguish publicly reported expenditures from other legal reporting frameworks',
        'status': 'planned',
    },
    {
        'id': 'CFO-DIV-3', 'number': 3, 'title': 'Political Committee Explorer',
        'focus': 'Organizational structures in campaign finance',
        'topics': [
            'Candidate committees', 'Party committees', 'Political action committees (PACs)',
            'Super PACs', 'Other organizations involved in campaign finance',
        ],
        'per_page': 'Legal concepts, reporting requirements, historical development',
        'status': 'planned',
    },
    {
        'id': 'CFO-DIV-4', 'number': 4, 'title': 'Election Cycle Dashboard',
        'focus': 'Compare election cycles with sourced methodologies',
        'topics': [
            'Presidential elections', 'Midterm elections', 'Spending trends',
            'Participation trends', 'Historical context',
        ],
        'status': 'planned',
    },
    {
        'id': 'CFO-DIV-5', 'number': 5, 'title': 'Arkansas Campaign Finance Center',
        'focus': 'Arkansas-focused civic education on state campaign finance',
        'topics': [
            'Arkansas campaign finance reporting', 'Relevant state agencies',
            'Arkansas election finance laws', 'Public reporting systems',
            'Historical Arkansas developments',
        ],
        'note': 'Connects national concepts to Arkansas civic education',
        'status': 'planned',
    },
    {
        'id': 'CFO-DIV-6', 'number': 6, 'title': 'Data Visualization Studio',
        'focus': 'Interactive educational graphics with methodology links',
        'topics': [
            'Spending timelines', 'Comparative charts', 'Flow diagrams',
            'Geographic maps', 'Trend analyses', 'Historical comparisons',
        ],
        'status': 'planned',
    },
    {
        'id': 'CFO-DIV-7', 'number': 7, 'title': 'Research Notes',
        'focus': 'Data quality and civic literacy for every major dataset',
        'fields': [
            'Data source', 'Collection methodology', 'Date range',
            'Definitions', 'Limitations', 'Frequently asked questions',
        ],
        'status': 'planned',
    },
    {
        'id': 'CFO-DIV-8', 'number': 8, 'title': 'Frequently Asked Questions',
        'focus': 'Evidence-linked answers to common campaign finance questions',
        'examples': [
            'Did campaign spending increase after Citizens United?',
            'What is an independent expenditure?',
            'Where does this data come from?',
            'What data is publicly available?',
            'What questions remain debated among researchers?',
        ],
        'status': 'planned',
    },
]

BEFORE_AFTER_STAGES = [
    {'stage': 'Before Citizens United', 'status': 'planned'},
    {'stage': 'Immediately After', 'status': 'planned'},
    {'stage': 'Subsequent Election Cycles', 'status': 'planned'},
    {'stage': 'Current Trends', 'status': 'planned'},
]

METHODOLOGY_QUESTIONS = [
    'What is being measured?',
    'Where did the data originate?',
    'How was it collected?',
    'What does the chart not show?',
    'What are the known limitations?',
]

DATA_INTEGRITY_FIELDS = [
    'Source', 'Date', 'Review status', 'Methodology',
    'Version', 'Related research', 'Related lessons',
]

MC_OBSERVATORY_METRICS = [
    {'id': 'CFO-M1', 'metric': 'Datasets published', 'current': datasets_published, 'status': 'live'},
    {'id': 'CFO-M2', 'metric': 'Charts completed', 'current': charts_completed, 'status': 'live'},
    {'id': 'CFO-M3', 'metric': 'Research notes completed', 'current': research_notes_completed, 'status': 'live'},
    {'id': 'CFO-M4', 'metric': 'Historical coverage', 'current': 'partial', 'status': 'partial'},
    {'id': 'CFO-M5', 'metric': 'Arkansas coverage', 'current': arkansas_charts, 'status': 'live'},
    {'id': 'CFO-M6', 'metric': 'Methodology reviews', 'current': methodology_reviews, 'status': 'live'},
    {'id': 'CFO-M7', 'metric': 'Broken data links', 'current': broken_data_links, 'status': 'live'},
    {'id': 'CFO-M8', 'metric': 'Scheduled dataset updates', 'current': scheduled_updates, 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Research Library (#37)', 'route': '/mission-control/research-library.html', 'status': 'partial', 'note': f'{library_docs} documents archived'},
    {'system': 'Evidence Ledger (#41)', 'route': '/mission-control/evidence-ledger.html', 'status': 'partial', 'note': f'{evidence_items} evidence records'},
    {'system': 'Claims Registry', 'route': '/mission-control/evidence-ledger.html', 'status': 'partial'},
    {'system': 'Knowledge Graph', 'route': '/mission-control/knowledge-graph.html', 'status': 'planned'},
    {'system': 'Curriculum (#33)', 'route': '/mission-control/curriculum.html', 'status': 'planned'},
    {'system': 'Media Studio (#36)', 'route': '/mission-control/media-studio.html', 'status': 'planned'},
    {'system': 'Learning Laboratory (#38)', 'route': '/mission-control/learning-lab.html', 'status': 'planned'},
    {'system': 'Research Observatory (#29)', 'route': '/mission-control/research-observatory.html', 'status': 'partial', 'note': 'Monitor vs data — complementary'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

divisions_defined = len(EIGHT_DIVISIONS)
campaign_finance_observatory_readiness = min(
    40,
    12 + divisions_defined * 3 + datasets_published * 5 + charts_completed * 3,
)

out = {
    'version': '1.0',
    'build': 63,
    'updated': today,
    'title': 'Master Campaign Finance Data Observatory v1.0',
    'subtitle': 'The Arkansas Campaign Finance Intelligence Center — Following the Money Through Facts, Data & Transparency',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/campaign-finance-observatory.html',
    'constitution': '/docs/MASTER_CAMPAIGN_FINANCE_OBSERVATORY.md',
    'purpose': (
        'Answer "What actually changed?" using publicly available information, '
        'historical records, documented research, and transparent data visualizations.'
    ),
    'governing_principle': (
        'Replace speculation with understanding. Teach citizens how to read the data — '
        'not merely how to react to it.'
    ),
    'flagship_system': True,
    'distinct_from': {
        'system': 'Research Observatory (#29)',
        'route': '/mission-control/research-observatory.html',
        'difference': 'Research Observatory monitors developments; Campaign Finance Observatory explains spending data',
    },
    'mission_questions': [
        'How has campaign spending changed over time?',
        'What trends appear before and after Citizens United?',
        'What types of political spending exist?',
        'Where does publicly reported campaign finance information come from?',
        'What are the limitations of the available data?',
    ],
    'eight_divisions': EIGHT_DIVISIONS,
    'before_after_explorer': {
        'title': 'Before & After Explorer',
        'stages': BEFORE_AFTER_STAGES,
        'emphasis': 'Educational comparison — not unsupported causal conclusions',
        'status': 'planned',
    },
    'methodology_pages': {
        'title': 'Methodology Transparency',
        'questions': METHODOLOGY_QUESTIONS,
        'required_per_chart': True,
        'status': 'planned',
    },
    'data_integrity_standards': {
        'title': 'Data Integrity Standards',
        'required_fields': DATA_INTEGRITY_FIELDS,
        'status': 'specified',
    },
    'mc_observatory_dashboard': {
        'title': 'Mission Control Observatory Dashboard',
        'metrics': MC_OBSERVATORY_METRICS,
        'living_research_program': True,
        'status': 'partial',
    },
    'integration': {
        'chain': 'Research Library → Evidence Ledger → Claims Registry → Knowledge Graph → Curriculum → Media Studio → Learning Laboratory → Mission Control',
        'systems': SYSTEM_CONNECTIONS,
        'principle': 'Every chart becomes part of the larger educational ecosystem',
    },
    'long_term_vision': (
        "Arkansas's most comprehensive public educational resource for understanding "
        'campaign finance through documented evidence — confidence in reading reports, '
        'interpreting trends, and recognizing data limits.'
    ),
    'summary': {
        'divisions_total': divisions_defined,
        'divisions_partial_or_live': 0,
        'datasets_published': datasets_published,
        'charts_completed': charts_completed,
        'research_notes_completed': research_notes_completed,
        'methodology_reviews': methodology_reviews,
        'broken_data_links': broken_data_links,
        'scheduled_updates': scheduled_updates,
        'arkansas_charts': arkansas_charts,
        'evidence_foundation_items': evidence_items,
        'library_documents': library_docs,
        'campaign_finance_observatory_readiness_pct': campaign_finance_observatory_readiness,
        'data_viz_readiness_pct': max(ex.get('data_viz_readiness', 8), campaign_finance_observatory_readiness // 3),
        'observatory_readiness_pct': ex.get('observatory_readiness', 20),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 datasets published — no FEC, OpenSecrets, or Arkansas SOS data feeds integrated',
        '0 charts completed — Data Visualization Studio not built',
        '0 research notes — methodology pages specified but not implemented',
        'Before & After Explorer not built — no interactive comparison views',
        'Arkansas Campaign Finance Center — 0 Arkansas-specific charts or datasets',
        'Political Committee Explorer pages not created — 0 committee type explainers live',
        'Build #63 Campaign Finance Observatory vs Build #29 Research Observatory — distinct roles, unify navigation?',
        'No automated dataset update schedule — scheduled_updates = 0',
        'Charts do not yet display required integrity fields (source, date, review, version)',
        'Knowledge Graph integration planned — campaign finance nodes not wired',
        f'Evidence foundation exists ({evidence_items} records) but not linked to observatory charts',
        'Public-facing /observatory/ route not built — MC dashboard only',
    ],
    'recommended_next_build': {
        'number': 64,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'FEC/OpenSecrets data pipeline spec, chart component library, methodology page '
            'templates, route inventory, COMP-* specs, GitHub issue backlog.'
        ),
    },
}

with open(root / 'data/campaign-finance-observatory.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Campaign Finance Observatory: {divisions_defined} divisions, '
    f'{datasets_published} datasets, {charts_completed} charts, '
    f'{campaign_finance_observatory_readiness}% readiness'
)
