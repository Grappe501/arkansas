"""
Generate data/educational-campaign-operating-system.json — Build #32 Educational Campaign OS v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

mc_path = root / 'data/mission-control.json'
cci_path = root / 'data/county-coalition-index.json'
mc = {}
cci = {}
if mc_path.exists():
    with open(mc_path) as f:
        mc = json.load(f)
if cci_path.exists():
    with open(cci_path) as f:
        cci = json.load(f)

exec_data = mc.get('executive', {})
civic = mc.get('civic_action', {})
cci_summary = cci.get('summary', {})

education_leaders = civic.get('education_leader_signups', 0)
coalition_orgs = cci_summary.get('counties_with_partner', 0)
counties_scaffolded = cci_summary.get('counties_registered', len(cci.get('counties', [])))
overall_completion = exec_data.get('overall_completion', 31)

HORIZONS = [
    {
        'id': 'ECOS-H1',
        'number': 1,
        'title': 'Build the Institution',
        'mission': "Create Arkansas's most trusted educational resource on Citizens United.",
        'status': 'active',
        'objectives': [
            {'title': 'Complete the educational platform', 'status': 'partial', 'pct': 35},
            {'title': 'Build Mission Control', 'status': 'partial', 'pct': 88},
            {'title': 'Publish the research library', 'status': 'partial', 'pct': 42},
            {'title': 'Launch the Source Library', 'status': 'partial', 'pct': 28},
            {'title': 'Launch coalition sign-on', 'status': 'partial', 'pct': 32},
            {'title': 'Launch Education Leader program', 'status': 'partial', 'pct': 30},
            {'title': 'Launch Community Education Academy', 'status': 'partial', 'pct': 52},
            {'title': 'Build the first Arkansas county pages', 'status': 'partial', 'pct': 38},
        ],
        'success_indicators': [
            {'title': 'Educational platform launched', 'status': 'live', 'met': True},
            {'title': 'Research framework operational', 'status': 'live', 'met': True},
            {'title': 'Mission Control operational', 'status': 'live', 'met': True},
            {'title': 'First coalition organizations participating', 'status': 'planned', 'met': coalition_orgs > 0},
            {'title': 'First Education Leaders enrolled', 'status': 'planned', 'met': education_leaders > 0},
        ],
        'mc_indicators': [],
    },
    {
        'id': 'ECOS-H2',
        'number': 2,
        'title': 'Build the Arkansas Network',
        'mission': 'Expand educational participation throughout Arkansas.',
        'status': 'planned',
        'objectives': [
            {'title': 'Education Leaders in every region', 'status': 'planned', 'pct': 5},
            {'title': 'Coalition partners across the state', 'status': 'planned', 'pct': 8},
            {'title': 'County education pages for all 75 counties', 'status': 'partial', 'pct': 35},
            {'title': 'Community conversation program', 'status': 'planned', 'pct': 12},
            {'title': 'Regional educational events', 'status': 'planned', 'pct': 5},
            {'title': 'Expanded research contributors', 'status': 'planned', 'pct': 10},
        ],
        'success_indicators': [],
        'mc_indicators': [
            'Counties represented', 'Coalition growth', 'Community conversations',
            'Educational events', 'Resource usage',
        ],
    },
    {
        'id': 'ECOS-H3',
        'number': 3,
        'title': "Build Arkansas's Knowledge Institution",
        'mission': "Become the state's leading public educational resource on Citizens United.",
        'status': 'planned',
        'objectives': [
            {'title': 'Comprehensive research library', 'status': 'planned', 'pct': 18},
            {'title': 'Interactive learning experiences', 'status': 'planned', 'pct': 8},
            {'title': 'Advanced Mission Control', 'status': 'partial', 'pct': 40},
            {'title': 'AI educational assistant', 'status': 'partial', 'pct': 14},
            {'title': 'Complete educational curriculum', 'status': 'partial', 'pct': 24},
            {'title': 'Expanded source archive', 'status': 'planned', 'pct': 15},
            {'title': 'Advanced county dashboards', 'status': 'partial', 'pct': 28},
        ],
        'success_indicators': [],
        'mc_indicators': [
            'Research completeness', 'Educational pathway completion', 'Source verification',
            'Public resource usage', 'Returning learners',
        ],
    },
    {
        'id': 'ECOS-H4',
        'number': 4,
        'title': 'Sustain the Institution',
        'mission': 'Ensure the platform remains useful, accurate, and trusted for years to come.',
        'status': 'planned',
        'objectives': [
            {'title': 'Regular research updates', 'status': 'planned', 'pct': 10},
            {'title': 'Legislative monitoring', 'status': 'partial', 'pct': 18},
            {'title': 'Court decision updates', 'status': 'planned', 'pct': 8},
            {'title': 'Coalition renewal', 'status': 'planned', 'pct': 5},
            {'title': 'Continuing education', 'status': 'partial', 'pct': 22},
            {'title': 'Content modernization', 'status': 'planned', 'pct': 12},
            {'title': 'Technology refresh', 'status': 'planned', 'pct': 15},
        ],
        'success_indicators': [],
        'mc_indicators': [
            'Review schedules met', 'Content freshness', 'Coalition retention',
            'Educational engagement', 'Technical health',
        ],
    },
]

ANNUAL_CYCLE = [
    {'season': 'Winter', 'focus': 'Research and planning',
     'activities': ['Review research', 'Update legislative materials', 'Improve educational resources', 'Prepare annual roadmap']},
    {'season': 'Spring', 'focus': 'Education and outreach',
     'activities': ['Community conversations', 'Coalition growth', 'Public presentations', 'Educational campaigns']},
    {'season': 'Summer', 'focus': 'Regional engagement',
     'activities': ['Conferences', 'Workshops', 'County outreach', 'Education Leader development']},
    {'season': 'Fall', 'focus': 'Evaluation and improvement',
     'activities': ['Mission Control assessment', 'Research updates', 'Platform improvements', 'Strategic planning']},
]

QUARTERLY_TOPICS = [
    'Research', 'Education', 'Coalition', 'County activity', 'Community conversations',
    'Technology', 'Mission Control', 'Growth priorities',
]

SUMMIT_AGENDA = [
    'Research updates', 'Educational presentations', 'Coalition networking',
    'Community conversation workshops', 'Arkansas legislative updates', 'Future planning',
]

INNOVATION_CATEGORIES = [
    {'id': 'ECOS-IP-01', 'title': 'Educational improvements', 'status': 'defined'},
    {'id': 'ECOS-IP-02', 'title': 'Research improvements', 'status': 'defined'},
    {'id': 'ECOS-IP-03', 'title': 'Technology improvements', 'status': 'defined'},
    {'id': 'ECOS-IP-04', 'title': 'Community outreach', 'status': 'defined'},
    {'id': 'ECOS-IP-05', 'title': 'Coalition expansion', 'status': 'defined'},
    {'id': 'ECOS-IP-06', 'title': 'Learning experiences', 'status': 'defined'},
    {'id': 'ECOS-IP-07', 'title': 'Accessibility improvements', 'status': 'defined'},
]

STRATEGIC_RISKS = [
    {'id': 'ECOS-RK-01', 'title': 'Outdated research', 'status': 'monitoring', 'severity': 'medium'},
    {'id': 'ECOS-RK-02', 'title': 'Incomplete citations', 'status': 'monitoring', 'severity': 'medium'},
    {'id': 'ECOS-RK-03', 'title': 'Technical debt', 'status': 'monitoring', 'severity': 'low'},
    {'id': 'ECOS-RK-04', 'title': 'Limited county participation', 'status': 'active', 'severity': 'high'},
    {'id': 'ECOS-RK-05', 'title': 'Coalition inactivity', 'status': 'active', 'severity': 'high'},
    {'id': 'ECOS-RK-06', 'title': 'Accessibility gaps', 'status': 'monitoring', 'severity': 'medium'},
    {'id': 'ECOS-RK-07', 'title': 'Resource limitations', 'status': 'monitoring', 'severity': 'medium'},
]

SUCCESS_MEASURES = [
    {'id': 'ECOS-SM-01', 'title': 'Learning path completion', 'status': 'planned', 'current': 0},
    {'id': 'ECOS-SM-02', 'title': 'Community conversations hosted', 'status': 'planned', 'current': 0},
    {'id': 'ECOS-SM-03', 'title': 'Education Leaders developed', 'status': 'partial', 'current': education_leaders},
    {'id': 'ECOS-SM-04', 'title': 'Coalition organizations participating', 'status': 'partial', 'current': coalition_orgs},
    {'id': 'ECOS-SM-05', 'title': 'Counties with active educational activity', 'status': 'partial', 'current': coalition_orgs},
    {'id': 'ECOS-SM-06', 'title': 'Research completeness', 'status': 'partial', 'current': exec_data.get('research_readiness', 22)},
    {'id': 'ECOS-SM-07', 'title': 'Public resource usage', 'status': 'planned', 'current': 0},
    {'id': 'ECOS-SM-08', 'title': 'Returning learners', 'status': 'planned', 'current': 0},
]

INSTITUTIONAL_MEMORY = [
    {'id': 'ECOS-IM-01', 'title': 'Build history', 'status': 'live', 'route': '/builds/'},
    {'id': 'ECOS-IM-02', 'title': 'Major decisions', 'status': 'partial', 'route': '/mission-control/'},
    {'id': 'ECOS-IM-03', 'title': 'Research milestones', 'status': 'partial', 'route': '/mission-control/research.html'},
    {'id': 'ECOS-IM-04', 'title': 'Coalition milestones', 'status': 'partial', 'route': '/mission-control/coalition.html'},
    {'id': 'ECOS-IM-05', 'title': 'Educational milestones', 'status': 'partial', 'route': '/mission-control/education-academy.html'},
    {'id': 'ECOS-IM-06', 'title': 'Annual reports', 'status': 'planned', 'route': None},
    {'id': 'ECOS-IM-07', 'title': 'Strategic plans', 'status': 'live', 'route': '/docs/EDUCATIONAL_CAMPAIGN_OPERATING_SYSTEM.md'},
]

h1 = HORIZONS[0]
h1_obj_avg = round(sum(o['pct'] for o in h1['objectives']) / len(h1['objectives']))
h1_ind_met = sum(1 for i in h1['success_indicators'] if i['met'])
h1_ind_total = len(h1['success_indicators'])

# Honest readiness: active horizon progress + roadmap structure + institutional memory partial
structure_score = 28  # 4 horizons, cycle, quarterly, summit, innovation, risks defined
h1_score = round(h1_obj_avg * 0.55 + (h1_ind_met / h1_ind_total * 100) * 0.45)
memory_live = sum(1 for m in INSTITUTIONAL_MEMORY if m['status'] == 'live')
memory_score = round(memory_live / len(INSTITUTIONAL_MEMORY) * 100 * 0.4 + 20)
campaign_os_readiness = min(round(h1_score * 0.5 + structure_score * 0.35 + memory_score * 0.15), 34)

out = {
    'version': '1.0',
    'build': 32,
    'updated': today,
    'title': 'Educational Campaign Operating System v1.0',
    'subtitle': 'Multi-Year Strategic Growth Blueprint',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/campaign-os.html',
    'constitution': '/docs/EDUCATIONAL_CAMPAIGN_OPERATING_SYSTEM.md',
    'purpose': 'Long-term civic education institution growing through deliberate, measurable phases.',
    'governing_principle': 'Built as an institution rather than a project — institutions have missions.',
    'current_horizon': {
        'id': 'ECOS-H1',
        'number': 1,
        'title': 'Build the Institution',
        'objectives_complete_pct': h1_obj_avg,
        'success_indicators_met': h1_ind_met,
        'success_indicators_total': h1_ind_total,
    },
    'horizons': HORIZONS,
    'annual_operating_cycle': ANNUAL_CYCLE,
    'quarterly_review_topics': QUARTERLY_TOPICS,
    'annual_summit': {
        'title': 'Annual Educational Summit',
        'status': 'planned',
        'agenda': SUMMIT_AGENDA,
    },
    'innovation_pipeline': {
        'title': 'Innovation Pipeline',
        'status': 'defined',
        'categories': INNOVATION_CATEGORIES,
        'queue_live': False,
    },
    'risk_management': {
        'title': 'Strategic Risk Management',
        'status': 'partial',
        'risks': STRATEGIC_RISKS,
        'active_risks': sum(1 for r in STRATEGIC_RISKS if r['status'] == 'active'),
    },
    'success_measurements': SUCCESS_MEASURES,
    'institutional_memory': INSTITUTIONAL_MEMORY,
    'future_readiness': {
        'title': 'Future Topic Expansion',
        'status': 'defined',
        'note': 'Framework allows additional civic education topics beyond Citizens United without platform rebuild.',
        'current_focus': 'Citizens United only',
    },
    'platform_snapshot': {
        'overall_completion_pct': overall_completion,
        'counties_scaffolded': counties_scaffolded,
        'counties_with_partner': coalition_orgs,
        'education_leader_signups': education_leaders,
        'builds_complete': len([b for b in mc.get('builds', []) if b.get('status') == 'complete']),
    },
    'related_systems': [
        {'title': 'Mission Control 2.0', 'route': '/mission-control/executive.html', 'build': 25},
        {'title': 'County Operating System', 'route': '/mission-control/county-os.html', 'build': 31},
        {'title': 'Outreach Engine', 'route': '/mission-control/outreach.html', 'build': 30},
        {'title': 'Education Academy', 'route': '/mission-control/education-academy.html', 'build': 28},
        {'title': 'Research Observatory', 'route': '/mission-control/research-observatory.html', 'build': 29},
        {'title': 'Phase Registry', 'route': '/mission-control/phases.html', 'build': 4},
    ],
    'summary': {
        'horizons_total': len(HORIZONS),
        'current_horizon': 1,
        'horizon_one_objectives_pct': h1_obj_avg,
        'success_indicators_met': h1_ind_met,
        'success_indicators_total': h1_ind_total,
        'annual_seasons': len(ANNUAL_CYCLE),
        'quarterly_topics': len(QUARTERLY_TOPICS),
        'innovation_categories': len(INNOVATION_CATEGORIES),
        'strategic_risks': len(STRATEGIC_RISKS),
        'success_measures': len(SUCCESS_MEASURES),
        'institutional_memory_items': len(INSTITUTIONAL_MEMORY),
        'quarterly_reports_live': False,
        'innovation_queue_live': False,
        'annual_summit_live': False,
        'campaign_os_readiness_pct': campaign_os_readiness,
    },
    'catalog_gaps': [
        'Horizon One incomplete — 0 coalition orgs, 0 Education Leaders enrolled',
        'Quarterly review reports not automated in Mission Control',
        'Innovation pipeline queue not implemented — categories defined only',
        'Annual Educational Summit page and registration not built',
        'Success measurements not tracked live — schema only',
        'Horizons Two–Four remain planned — no transition criteria automated',
        'Annual operating cycle not scheduled in MC calendar',
        'Risk management partial — no automated risk dashboard',
    ],
    'recommended_next_build': {
        'number': 34,
        'title': 'Component Specifications with Props/States',
        'note': 'Map strategic growth dashboards and horizon indicators to COMP-* components from Build #17.',
    },
}

path = root / 'data/educational-campaign-operating-system.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Campaign OS: horizon 1 at {h1_obj_avg}%, {campaign_os_readiness}% readiness')
