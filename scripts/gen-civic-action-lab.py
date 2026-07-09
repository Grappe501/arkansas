"""
Generate data/civic-action-lab.json — Build #42 Master Civic Action Lab v1.0.
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


solutions = load_json(root / 'data/solutions-policy.json')
civic = load_json(root / 'data/civic-ecosystem.json')
mc_path = root / 'data/mission-control.json'
mc = load_json(mc_path)
mc_civic = mc.get('civic_action', {})

CORE_PHILOSOPHY = [
    'Learn', 'Research', 'Compare', 'Discuss', 'Draft', 'Review', 'Share',
]

DIVISIONS = [
    {
        'id': 'CAL-D01', 'number': 1, 'title': 'Federal Solutions Studio', 'slug': 'federal-solutions',
        'purpose': 'Educational exploration of federal-level proposals and reforms.',
        'examples': ['Disclosure proposals', 'Campaign finance legislation', 'Constitutional amendment proposals',
                     'FEC reforms', 'Transparency initiatives'],
        'interim_route': '/solutions/#federal',
        'status': 'partial', 'readiness_pct': 28,
        'note': 'Solutions hub federal section — proposal deep-dives not built',
    },
    {
        'id': 'CAL-D02', 'number': 2, 'title': 'Arkansas Legislative Studio', 'slug': 'arkansas-legislative',
        'purpose': 'Educational exploration of Arkansas General Assembly policy ideas.',
        'examples': ['Current Arkansas law', 'Statutory framework', 'Constitutional considerations',
                     'Historical background', 'Related research'],
        'interim_route': '/solutions/#arkansas',
        'status': 'partial', 'readiness_pct': 22,
        'note': 'Dedicated Arkansas section scaffold — no proposal library',
    },
    {
        'id': 'CAL-D03', 'number': 3, 'title': 'Arkansas Ballot Initiative Studio', 'slug': 'ballot-initiative',
        'purpose': 'Educational workspace for Arkansas initiative and referendum process.',
        'examples': ['Constitutional requirements', 'Signature requirements', 'Geographic distribution',
                     'Historical examples', 'Timeline planning', 'Draft language', 'Legal review checklist'],
        'interim_route': '/action/ballot-lab.html',
        'status': 'partial', 'readiness_pct': 26,
        'note': 'Ballot lab page exists — no guided draft builder workflow',
    },
    {
        'id': 'CAL-D04', 'number': 4, 'title': 'Comparative Reform Library', 'slug': 'comparative-reform',
        'purpose': 'Compare reform approaches across jurisdictions.',
        'examples': ['Montana developments', 'Hawaii developments', 'Other state reforms', 'Historical federal reforms'],
        'interim_route': '/halls/montana-hawaii.html',
        'status': 'partial', 'readiness_pct': 32,
        'live_comparisons': 2,
        'note': 'MT Initiative 194 + HI Act 11 live — comparison matrix partial',
    },
    {
        'id': 'CAL-D05', 'number': 5, 'title': 'Public Comment Workspace', 'slug': 'public-comment',
        'purpose': 'Submit questions, observations, research suggestions, and draft ideas.',
        'examples': ['Questions', 'Educational observations', 'Research suggestions', 'Draft ideas',
                     'Historical materials', 'Source recommendations'],
        'interim_route': '/action/ideas.html',
        'status': 'partial', 'readiness_pct': 24,
        'note': 'Community ideas form — editorial review workflow partial',
    },
    {
        'id': 'CAL-D06', 'number': 6, 'title': 'Community Review Panels', 'slug': 'community-review',
        'purpose': 'Structured educational review by subject-matter volunteers.',
        'examples': ['Attorneys', 'Historians', 'Political scientists', 'Civic educators',
                     'Coalition partners', 'Community volunteers'],
        'interim_route': '/coalition/',
        'status': 'planned', 'readiness_pct': 10,
        'note': 'Coalition hub exists — no review panel workflow',
    },
]

LEGISLATIVE_TRACKER = [
    'Current Status', 'Historical Timeline', 'Supporting Research', 'Related Court Decisions',
    'Related Constitutional Principles', 'Relevant Arkansas Information', 'Primary Sources',
]

DRAFT_BUILDER_WORKSPACES = [
    {'id': 'DB-01', 'title': 'Federal concepts', 'status': 'planned', 'route': '/action/draft-laws.html'},
    {'id': 'DB-02', 'title': 'Arkansas legislative concepts', 'status': 'planned', 'route': '/action/draft-laws.html'},
    {'id': 'DB-03', 'title': 'Ballot initiative concepts', 'status': 'partial', 'route': '/action/ballot-lab.html'},
]

DRAFT_BUILDER_STEPS = [
    'Define the problem', 'Research current law', 'Identify constitutional questions',
    'Gather supporting evidence', 'Consider implementation challenges', 'Record unanswered questions',
]

PUBLIC_OFFICIAL_CENTER = {
    'title': 'Public Official Education Center',
    'route': '/action/contact-legislators.html',
    'audiences': [
        'Arkansas U.S. Representatives', 'Arkansas U.S. Senators', 'Arkansas General Assembly members',
    ],
    'packet_includes': [
        'Historical background', 'Relevant legal context', 'Primary source references',
        'Research summaries', 'Related educational resources',
    ],
    'status': 'partial',
    'packets_prepared': 0,
}

MC_METRICS = [
    {'id': 'CAL-M01', 'title': 'Model law concepts', 'status': 'partial', 'current': mc_civic.get('model_law_submissions', 0)},
    {'id': 'CAL-M02', 'title': 'Ballot initiative concepts', 'status': 'partial', 'current': mc_civic.get('ballot_lab_submissions', 0)},
    {'id': 'CAL-M03', 'title': 'Federal proposal summaries', 'status': 'planned', 'current': 0},
    {'id': 'CAL-M04', 'title': 'Arkansas proposal summaries', 'status': 'planned', 'current': 0},
    {'id': 'CAL-M05', 'title': 'Comparative state studies', 'status': 'partial', 'current': 2},
    {'id': 'CAL-M06', 'title': 'Research citations', 'status': 'partial', 'current': 14},
    {'id': 'CAL-M07', 'title': 'Public comments awaiting review', 'status': 'partial', 'current': mc_civic.get('community_ideas', 0)},
    {'id': 'CAL-M08', 'title': 'Educational packets prepared', 'status': 'planned', 'current': 0},
]

FUTURE_EXPANSION = [
    'Structured public workshops', 'Collaborative drafting sessions', 'Additional state comparisons',
    'Expanded constitutional analysis', 'Educational simulations',
    'AI-assisted research navigation grounded in verified sources',
]

div_partial = sum(1 for d in DIVISIONS if d['status'] == 'partial')
div_planned = sum(1 for d in DIVISIONS if d['status'] == 'planned')
avg_division_readiness = round(sum(d['readiness_pct'] for d in DIVISIONS) / len(DIVISIONS))

civic_action_lab_readiness = min(
    round(avg_division_readiness * 0.4 + (div_partial / 6 * 100) * 0.25 + 14),
    26,
)

out = {
    'version': '1.0',
    'build': 42,
    'updated': today,
    'title': 'Master Civic Action Lab v1.0',
    'subtitle': 'Civic Solutions, Legislative Innovation & Ballot Initiative Architecture',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/civic-action-lab.html',
    'canonical_lab_route': '/civic-lab/[division-slug]',
    'current_lab_route': 'Solutions hub + action pages — interim static workspaces',
    'constitution': '/docs/MASTER_CIVIC_ACTION_LAB.md',
    'purpose': 'Bridge between civic understanding and civic participation — educate first.',
    'mission': 'Help Arkansans understand current law, proposals, constitutional constraints, and Arkansas processes.',
    'governing_principle': 'Educate first — illuminate options, preserve transparency, encourage evidence-based engagement.',
    'long_term_vision': "Arkansas's most comprehensive educational environment for how ideas become law or ballot initiatives.",
    'not_a_campaign': 'Not a campaign headquarters or lobbying platform — educational laboratory only.',
    'core_philosophy': CORE_PHILOSOPHY,
    'divisions': DIVISIONS,
    'legislative_tracker': LEGISLATIVE_TRACKER,
    'draft_builder': {
        'title': 'Draft Builder',
        'status': 'partial',
        'workspaces': DRAFT_BUILDER_WORKSPACES,
        'steps': DRAFT_BUILDER_STEPS,
        'guided_workflow_live': False,
    },
    'public_official_center': PUBLIC_OFFICIAL_CENTER,
    'mc_integration': {
        'title': 'Civic Action Lab Dashboard Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'submission_tracking_live': False,
    },
    'future_expansion': FUTURE_EXPANSION,
    'foundations': {
        'solutions_policy': {'route': '/data/solutions-policy.json', 'hub': '/solutions/'},
        'civic_ecosystem': {'route': '/data/civic-ecosystem.json', 'build': 12},
        'civic_action_mc': {'readiness_score': mc_civic.get('readiness_score', 22)},
    },
    'related_systems': [
        {'title': 'Solutions & Policy Options', 'route': '/data/solutions-policy.json', 'hub': '/solutions/'},
        {'title': 'Civic Ecosystem', 'route': '/data/civic-ecosystem.json', 'build': 12},
        {'title': 'Evidence Ledger', 'route': '/data/evidence-ledger.json', 'build': 41},
        {'title': 'Research Observatory', 'route': '/data/research-observatory.json', 'build': 29},
        {'title': 'Outreach Engine', 'route': '/data/outreach-engine.json', 'build': 30},
        {'title': 'County OS', 'route': '/data/arkansas-counties.json', 'build': 31},
    ],
    'summary': {
        'divisions_total': len(DIVISIONS),
        'divisions_partial': div_partial,
        'divisions_planned': div_planned,
        'avg_division_readiness_pct': avg_division_readiness,
        'comparative_studies_live': 2,
        'draft_builder_workspaces': len(DRAFT_BUILDER_WORKSPACES),
        'guided_draft_builder_live': False,
        'community_review_panels_live': False,
        'model_law_submissions': mc_civic.get('model_law_submissions', 0),
        'ballot_lab_submissions': mc_civic.get('ballot_lab_submissions', 0),
        'community_ideas_pending': mc_civic.get('community_ideas', 0),
        'educational_packets_prepared': 0,
        'submission_tracking_live': False,
        'civic_action_lab_readiness_pct': civic_action_lab_readiness,
    },
    'catalog_gaps': [
        'No canonical /civic-lab/[slug] routes — solutions/action pages interim',
        'Federal Solutions Studio — hub scaffold only, no proposal deep-dives',
        'Arkansas Legislative Studio — no Arkansas proposal library',
        'Ballot Initiative Studio — no guided draft builder or legal checklist automation',
        'Community Review Panels not built — coalition hub only',
        'Draft Builder — 2/3 workspaces planned, no guided workflow',
        'Legislative tracker elements defined — not wired per proposal',
        'Public Official packets — contact tool exists, packet generator not built',
        'MC submission counts at 0 — Netlify Forms not integrated',
        'Distinguish enacted law vs proposals — matrix partial only',
    ],
    'recommended_next_build': {
        'number': 44,
        'title': 'Component Specifications with Props/States',
        'note': 'Map lab division shells, draft builder workspaces, legislative tracker panels, and packet builders to COMP-* from Build #17.',
    },
}

path = root / 'data/civic-action-lab.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Civic Action Lab: {div_partial}/6 partial, {civic_action_lab_readiness}% readiness')
