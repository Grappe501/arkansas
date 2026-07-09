"""
Generate data/launch-strategy.json — Build #53 Master Launch Strategy & Arkansas Rollout Blueprint v1.0.
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
content = load_json(root / 'data/content-inventory.json')
coalition = load_json(root / 'data/coalition-directory.json')
vj = load_json(root / 'data/visitor-journey.json')
kg = load_json(root / 'data/kg-registry.json')
claims = load_json(root / 'data/claims-ledger.json')

ex = mc.get('executive', {})
published = content.get('summary', {}).get('published', 15)
orgs = coalition.get('summary', {}).get('total_organizations', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
contact_signups = vj.get('summary', {}).get('contact_network_signups', 0)
kg_nodes = kg.get('summary', {}).get('total_nodes', 38)
claims_count = len(claims.get('claims', []))
public_launch_pct = ex.get('public_launch_readiness', 8)

LAUNCH_PHASES = [
    {
        'id': 'PHASE-0', 'number': 0, 'title': 'Private Development',
        'audience': 'Project team only',
        'objectives': [
            'Build core architecture', 'Populate initial content', 'Test Mission Control',
            'Verify citations', 'Complete accessibility review', 'Test every workflow',
        ],
        'mc_indicators': ['Engineering readiness', 'Research readiness', 'Content readiness', 'System health'],
        'public_visibility': 'None (institutional target)',
        'status': 'active',
        'readiness_pct': 42,
        'note': 'Netlify production URL exists — treated as dev/staging until Phase 3 gate',
    },
    {
        'id': 'PHASE-1', 'number': 1, 'title': 'Trusted Review Circle',
        'audience': 'Invitation-only: attorneys, historians, educators, researchers, librarians, coalition reps',
        'objectives': [
            'Test educational clarity', 'Identify factual issues', 'Evaluate navigation',
            'Improve explanations', 'Review trust signals',
        ],
        'mc_indicators': ['Review Feedback dashboard', 'Issue triage', 'Citation verification queue'],
        'public_visibility': 'Invite-only URL',
        'status': 'planned',
        'readiness_pct': 5,
        'note': 'Review Feedback dashboard not built',
    },
    {
        'id': 'PHASE-2', 'number': 2, 'title': 'Arkansas Pilot',
        'audience': 'Limited Arkansas learners',
        'objectives': [
            'Observe real learning behavior', 'Test Education Academy', 'Test Contact Network',
            'Test Coalition sign-on', 'Evaluate community conversations',
        ],
        'mc_indicators': ['Learning progression', 'Signup funnels', 'Pilot cohort metrics'],
        'public_visibility': 'Pilot cohort',
        'status': 'planned',
        'readiness_pct': 8,
        'note': f'0 Education Leaders · {orgs} coalition orgs · no pilot cohort defined',
    },
    {
        'id': 'PHASE-3', 'number': 3, 'title': 'Public Arkansas Launch',
        'audience': 'Anyone in Arkansas',
        'objectives': [
            'Introduce platform publicly', 'Statewide educational outreach', 'Recruit Education Leaders',
            'Expand coalition', 'Publish Research Library',
        ],
        'mc_indicators': ['Public institutional reporting', 'Outreach metrics', 'Launch readiness score'],
        'public_visibility': 'Full public',
        'status': 'planned',
        'readiness_pct': public_launch_pct,
        'note': 'Launch checklist 2/12 complete — not ready for recommendation',
    },
    {
        'id': 'PHASE-4', 'number': 4, 'title': 'Institutional Growth',
        'audience': 'Arkansas public + partners',
        'objectives': [
            'County pages', 'Expand Academy', 'Publish documentaries', 'Expand encyclopedia',
            'Grow coalition', 'Increase educational events',
        ],
        'mc_indicators': ['County coverage', 'Media assets', 'Event calendar', 'Encyclopedia depth'],
        'public_visibility': 'Full public',
        'status': 'planned',
        'readiness_pct': 3,
        'note': '75 counties indexed — 0 with participation',
    },
    {
        'id': 'PHASE-5', 'number': 5, 'title': 'Long-Term Stewardship',
        'audience': 'Arkansas + institutional stewards',
        'objectives': [
            'Maintain research', 'Update resources', 'Review evidence', 'Train Education Leaders',
            'Preserve institutional knowledge', 'Continue serving Arkansas',
        ],
        'mc_indicators': ['Annual review', 'Succession planning', 'Evidence refresh cycle'],
        'public_visibility': 'Full public',
        'status': 'planned',
        'readiness_pct': 10,
        'note': 'Governance annual report not generated — stewardship planned in roadmap',
    },
]

READINESS_CHECKLIST = [
    {'id': 'CHK-01', 'item': 'Research verified', 'status': 'partial', 'current': f'{ex.get("research_readiness", 25)}% research readiness'},
    {'id': 'CHK-02', 'item': 'Core curriculum published', 'status': 'partial', 'current': f'{published} published / ~2700 target'},
    {'id': 'CHK-03', 'item': 'Evidence Ledger operational', 'status': 'partial', 'current': f'{claims_count} claims in ledger'},
    {'id': 'CHK-04', 'item': 'Mission Control operational', 'status': 'live', 'current': f'{len(mc.get("builds", []))} builds logged'},
    {'id': 'CHK-05', 'item': 'Accessibility review completed', 'status': 'planned', 'current': 'WCAG audit not performed'},
    {'id': 'CHK-06', 'item': 'Privacy policy published', 'status': 'planned', 'current': 'Not published — governance gap'},
    {'id': 'CHK-07', 'item': 'Editorial standards published', 'status': 'partial', 'current': 'Content factory partial — no public standards page'},
    {'id': 'CHK-08', 'item': 'Source Library available', 'status': 'partial', 'current': '/library/ live — 14 evidence IDs'},
    {'id': 'CHK-09', 'item': 'Knowledge Graph functioning', 'status': 'partial', 'current': f'{kg_nodes}/500 KG nodes'},
    {'id': 'CHK-10', 'item': 'Education Leader signup operational', 'status': 'partial', 'current': f'{edu_leaders} signups — form exists'},
    {'id': 'CHK-11', 'item': 'Coalition signup operational', 'status': 'partial', 'current': f'{orgs} orgs joined'},
    {'id': 'CHK-12', 'item': 'Contact Network operational', 'status': 'partial', 'current': f'{contact_signups} contact signups'},
]

LAUNCH_METRICS = [
    {'id': 'MET-01', 'metric': 'Learning path completion', 'status': 'planned', 'tracking': 'None'},
    {'id': 'MET-02', 'metric': 'Returning learners', 'status': 'planned', 'tracking': 'No analytics'},
    {'id': 'MET-03', 'metric': 'Education Leader applications', 'status': 'partial', 'tracking': f'{edu_leaders} total'},
    {'id': 'MET-04', 'metric': 'Coalition organizations joining', 'status': 'partial', 'tracking': f'{orgs} total'},
    {'id': 'MET-05', 'metric': 'Community conversation requests', 'status': 'planned', 'tracking': 'No intake log'},
    {'id': 'MET-06', 'metric': 'Toolkit downloads', 'status': 'planned', 'tracking': 'Not measured'},
    {'id': 'MET-07', 'metric': 'Source Library usage', 'status': 'planned', 'tracking': 'No analytics'},
]

COMMUNICATION_PILLARS = [
    'Education', 'Transparency', 'Historical understanding', 'Constitutional literacy',
    'Primary sources', 'Arkansas civic engagement',
]

FEEDBACK_CATEGORIES = [
    {'category': 'Educational clarity', 'status': 'planned', 'mc_route': None},
    {'category': 'Navigation', 'status': 'planned', 'mc_route': None},
    {'category': 'Missing topics', 'status': 'planned', 'mc_route': None},
    {'category': 'Source requests', 'status': 'planned', 'mc_route': None},
    {'category': 'Accessibility concerns', 'status': 'planned', 'mc_route': None},
    {'category': 'Suggested improvements', 'status': 'planned', 'mc_route': None},
]

ARKANSAS_GROWTH = {
    'strategy': 'County-by-county expansion',
    'counties_total': 75,
    'counties_with_participation': 0,
    'priorities': [
        'Recruit Education Leaders', 'Build coalition partnerships', 'Host community conversations',
        'Develop local resource collections', 'Support libraries and civic organizations',
    ],
    'status': 'planned',
}

ANNUAL_RELAUNCH = {
    'title': 'Annual Institutional Renewal',
    'activities': [
        'Annual research updates', 'New educational resources', 'State of the Institution report',
        'Academy updates', 'Coalition recognition', 'Community education highlights',
    ],
    'status': 'planned',
    'first_annual': None,
}

SUCCESS_CRITERIA = [
    'Arkansans trust the platform',
    'Educators recommend it',
    'Libraries reference it',
    'Students learn from it',
    'Community organizations use it',
    'Public officials recognize it as reliable educational resource',
]

LAUNCH_COMMAND_CENTER = {
    'title': 'Launch Command Center',
    'route': '/mission-control/launch-strategy.html',
    'readiness_dimensions': [
        {'id': 'LCC-01', 'dimension': 'Overall launch readiness', 'pct': public_launch_pct, 'status': 'early'},
        {'id': 'LCC-02', 'dimension': 'Research readiness', 'pct': ex.get('research_readiness', 25), 'status': 'partial'},
        {'id': 'LCC-03', 'dimension': 'Technology readiness', 'pct': ex.get('technical_architecture_readiness', 38), 'status': 'partial'},
        {'id': 'LCC-04', 'dimension': 'Content readiness', 'pct': ex.get('content_readiness', 28), 'status': 'partial'},
        {'id': 'LCC-05', 'dimension': 'Accessibility readiness', 'pct': 15, 'status': 'planned'},
        {'id': 'LCC-06', 'dimension': 'Coalition readiness', 'pct': ex.get('coalition_readiness', 18), 'status': 'planned'},
        {'id': 'LCC-07', 'dimension': 'County readiness', 'pct': ex.get('county_os_readiness', 28), 'status': 'partial'},
        {'id': 'LCC-08', 'dimension': 'Education Leader readiness', 'pct': ex.get('education_academy_readiness', 26), 'status': 'partial'},
        {'id': 'LCC-09', 'dimension': 'Institutional readiness', 'pct': ex.get('institutional_maturity_pct', 38), 'status': 'partial'},
        {'id': 'LCC-10', 'dimension': 'UX / experience readiness', 'pct': ex.get('ux_architecture_readiness', 39), 'status': 'partial'},
    ],
}

chk_live = sum(1 for c in READINESS_CHECKLIST if c['status'] == 'live')
chk_partial = sum(1 for c in READINESS_CHECKLIST if c['status'] == 'partial')
chk_planned = sum(1 for c in READINESS_CHECKLIST if c['status'] == 'planned')
checklist_score = round((chk_live * 100 + chk_partial * 45) / len(READINESS_CHECKLIST))

MC_METRICS = [
    {'id': 'LCH-01', 'title': 'Launch phases defined', 'status': 'live', 'current': f'{len(LAUNCH_PHASES)}/6'},
    {'id': 'LCH-02', 'title': 'Current rollout phase', 'status': 'live', 'current': 'Phase 0 — Private Development'},
    {'id': 'LCH-03', 'title': 'Launch checklist complete', 'status': 'planned', 'current': f'{chk_live} live, {chk_partial} partial, {chk_planned} planned'},
    {'id': 'LCH-04', 'title': 'Public launch recommended', 'status': 'blocked', 'current': f'No — {public_launch_pct}% public launch readiness'},
    {'id': 'LCH-05', 'title': 'Review Feedback dashboard', 'status': 'planned', 'current': 'Phase 1 requirement — not built'},
    {'id': 'LCH-06', 'title': 'Educational launch metrics tracked', 'status': 'planned', 'current': '0/7 metrics instrumented'},
    {'id': 'LCH-07', 'title': 'Feedback categorization in MC', 'status': 'planned', 'current': 'No feedback intake pipeline'},
    {'id': 'LCH-08', 'title': 'County growth visualization', 'status': 'partial', 'current': '75 counties — 0 participation'},
    {'id': 'LCH-09', 'title': 'Annual relaunch scheduled', 'status': 'planned', 'current': 'Not scheduled'},
    {'id': 'LCH-10', 'title': 'Launch Command Center live', 'status': 'live', 'current': 'This dashboard'},
]

readiness_factors = [
    100,  # constitution
    42,   # phase 0 active progress
    checklist_score,
    public_launch_pct,
    20,   # feedback architecture
    15,   # launch metrics tracking
    75,   # command center after this build
    ex.get('outreach_readiness', 22) * 0.5,  # communication partial
]
launch_strategy_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 53,
    'updated': today,
    'title': 'Master Launch Strategy & Arkansas Rollout Blueprint v1.0',
    'subtitle': 'From Internal Build to Public Institution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/launch-strategy.html',
    'constitution': '/docs/MASTER_LAUNCH_STRATEGY.md',
    'purpose': 'How Citizens United Facts is introduced to Arkansas — quality, trust, and sustainable growth over publicity.',
    'governing_principle': (
        'Never rush to become public. Launch only when the institution is ready to earn public trust — '
        'readiness over deadlines.'
    ),
    'launch_philosophy': {
        'wrong_question': 'When can we launch?',
        'right_question': 'When is the institution ready to earn public trust?',
        'tone': 'Deliberate, confident, well prepared',
    },
    'extends': [
        {'title': 'Master Build Bible', 'build': 50, 'route': '/data/build-bible.json'},
        {'title': 'Institutional Roadmap', 'build': 44, 'route': '/data/institutional-roadmap.json'},
        {'title': 'Visitor Journey', 'build': 47, 'route': '/data/visitor-journey.json'},
        {'title': 'UX Architecture', 'build': 52, 'route': '/data/ux-architecture.json'},
        {'title': 'Governance Constitution', 'build': 49, 'route': '/data/governance-constitution.json'},
    ],
    'launch_phases': {
        'title': 'Six Launch Phases',
        'phases': LAUNCH_PHASES,
        'current_phase': 0,
        'current_phase_title': 'Private Development',
        'phases_total': len(LAUNCH_PHASES),
    },
    'readiness_checklist': {
        'title': 'Public Launch Gate',
        'principle': 'Readiness, not deadlines',
        'items': READINESS_CHECKLIST,
        'items_live': chk_live,
        'items_partial': chk_partial,
        'items_planned': chk_planned,
        'checklist_score_pct': checklist_score,
        'public_launch_recommended': False,
    },
    'launch_metrics': {
        'principle': 'Educational indicators over page views',
        'metrics': LAUNCH_METRICS,
        'instrumented': sum(1 for m in LAUNCH_METRICS if m['status'] == 'live'),
    },
    'communication_strategy': {
        'pillars': COMMUNICATION_PILLARS,
        'framing': 'Public educational resource — not advocacy',
        'status': 'partial',
        'current': 'Messaging in site copy — no launch communications plan',
    },
    'feedback_architecture': {
        'principle': 'Every phase actively collects feedback',
        'categories': FEEDBACK_CATEGORIES,
        'mc_triage': 'planned',
        'phase_1_dashboard': 'Review Feedback — not built',
    },
    'arkansas_growth_strategy': ARKANSAS_GROWTH,
    'annual_relaunch': ANNUAL_RELAUNCH,
    'success_definition': {
        'criteria': SUCCESS_CRITERIA,
        'measure': 'Steady growth in understanding — not short-lived publicity',
    },
    'launch_command_center': LAUNCH_COMMAND_CENTER,
    'long_term_vision': (
        'Public launch is the opening chapter — decades of Arkansas civic education ahead. '
        'Every year: more complete, trustworthy, connected, useful, understandable, valuable.'
    ),
    'mc_integration': {
        'title': 'Mission Control Launch Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'authoritative_reference': True,
    },
    'related_blueprints': [
        {'title': 'Institutional Roadmap (#44)', 'route': '/mission-control/institutional-roadmap.html', 'build': 44},
        {'title': 'Outreach Engine', 'route': '/mission-control/outreach.html', 'build': 30},
        {'title': 'Education Academy', 'route': '/mission-control/education-academy.html', 'build': 28},
        {'title': 'County OS', 'route': '/mission-control/county-os.html', 'build': 31},
        {'title': 'Trust Framework', 'route': '/mission-control/trust.html', 'build': 36},
    ],
    'summary': {
        'phases_total': len(LAUNCH_PHASES),
        'current_phase': 0,
        'checklist_items': len(READINESS_CHECKLIST),
        'checklist_live': chk_live,
        'checklist_partial': chk_partial,
        'checklist_planned': chk_planned,
        'checklist_score_pct': checklist_score,
        'public_launch_readiness_pct': public_launch_pct,
        'public_launch_recommended': False,
        'education_leaders': edu_leaders,
        'coalition_orgs': orgs,
        'knowledge_published': published,
        'launch_metrics_instrumented': 0,
        'feedback_pipeline_live': False,
        'annual_relaunch_scheduled': False,
        'launch_strategy_readiness_pct': launch_strategy_readiness,
    },
    'catalog_gaps': [
        'Site publicly reachable on Netlify — institutional phase model treats as Phase 0 dev',
        'Review Feedback dashboard (Phase 1) not built',
        '0/7 educational launch metrics instrumented',
        'No feedback categorization pipeline in Mission Control',
        'Privacy policy not published — blocks launch checklist',
        'WCAG accessibility audit not completed',
        f'{public_launch_pct}% public launch readiness — 10/12 checklist items incomplete',
        f'0 Education Leaders · {orgs} coalition orgs — Phase 2 pilot impossible today',
        'Annual relaunch / State of Institution report not scheduled',
        'County-by-county growth visualization not live',
        'Learning progression tracking not server-side — Phase 2 requirement unmet',
    ],
    'recommended_next_build': {
        'number': 54,
        'title': 'Master Implementation Roadmap & Sprint Zero',
        'note': 'Review Feedback dashboard, privacy policy, accessibility audit sprint, Neon/Prisma, first pilot cohort criteria.',
    },
}

path = root / 'data/launch-strategy.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(
    f'Launch Strategy: Phase 0 active, {chk_live}+{chk_partial} checklist partial, '
    f'{public_launch_pct}% public launch, {launch_strategy_readiness}% blueprint readiness'
)
