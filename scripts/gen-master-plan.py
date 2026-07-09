"""
Generate data/master-plan.json — Build #55 Master Master Plan v1.0.
The Complete Institutional Blueprint & Execution Constitution.
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
bb = load_json(root / 'data/build-bible.json')
pmo = load_json(root / 'data/pmo.json')
ls = load_json(root / 'data/launch-strategy.json')
da = load_json(root / 'data/data-architecture.json')
vj = load_json(root / 'data/visitor-journey.json')
coalition = load_json(root / 'data/coalition-directory.json')
content = load_json(root / 'data/content-inventory.json')
kg = load_json(root / 'data/kg-registry.json')

ex = mc.get('executive', {})
bb_sum = bb.get('summary', {})
published = content.get('summary', {}).get('published', 15)
orgs = coalition.get('summary', {}).get('total_organizations', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
kg_nodes = kg.get('summary', {}).get('total_nodes', 38)
builds_logged = len(mc.get('builds', []))

WHY_GAPS = [
    'What the case actually involved',
    'What the Court actually held',
    'What changed and what did not change',
    'How campaign finance law evolved before and after',
    'What options exist for Congress, states, and citizens',
]

INSTITUTIONAL_MODEL = [
    {'facet': 'Research institute', 'status': 'partial', 'route': '/mission-control/research-observatory.html'},
    {'facet': 'Constitutional law library', 'status': 'partial', 'route': '/library/'},
    {'facet': 'Digital museum', 'status': 'planned', 'route': '/halls/'},
    {'facet': 'University curriculum', 'status': 'partial', 'route': '/mission-control/curriculum.html'},
    {'facet': 'Documentary studio', 'status': 'planned', 'route': '/mission-control/media-studio.html'},
    {'facet': 'Statewide civic education network', 'status': 'planned', 'route': '/educate/'},
    {'facet': 'Coalition hub', 'status': 'planned', 'route': '/coalition/'},
    {'facet': 'Community leadership academy', 'status': 'partial', 'route': '/mission-control/education-academy.html'},
    {'facet': 'Public knowledge archive', 'status': 'partial', 'route': '/mission-control/research-library.html'},
    {'facet': 'Mission Control operating system', 'status': 'live', 'route': '/mission-control/'},
]

PILLARS = [
    {'number': 1, 'id': 'research', 'title': 'Research', 'route': '/mission-control/research-observatory.html'},
    {'number': 2, 'id': 'evidence', 'title': 'Evidence', 'route': '/mission-control/evidence-ledger.html'},
    {'number': 3, 'id': 'education', 'title': 'Education', 'route': '/educate/'},
    {'number': 4, 'id': 'encyclopedia', 'title': 'Encyclopedia', 'route': '/mission-control/encyclopedia.html'},
    {'number': 5, 'id': 'curriculum', 'title': 'Curriculum', 'route': '/mission-control/curriculum.html'},
    {'number': 6, 'id': 'community', 'title': 'Community', 'route': '/mission-control/education-academy.html'},
    {'number': 7, 'id': 'coalition', 'title': 'Coalition', 'route': '/mission-control/coalition.html'},
    {'number': 8, 'id': 'media', 'title': 'Media', 'route': '/mission-control/media-studio.html'},
    {'number': 9, 'id': 'solutions', 'title': 'Solutions', 'route': '/solutions/'},
    {'number': 10, 'id': 'mission_control', 'title': 'Mission Control', 'route': '/mission-control/'},
    {'number': 11, 'id': 'knowledge_graph', 'title': 'Knowledge Graph', 'route': '/mission-control/civic-intelligence.html'},
    {'number': 12, 'id': 'governance', 'title': 'Governance', 'route': '/mission-control/governance.html'},
]

ENGINES = [
    {
        'id': 'knowledge', 'title': 'Knowledge Engine',
        'components': ['Research', 'Evidence', 'Claims', 'Sources', 'Knowledge Graph'],
        'readiness_pct': round((ex.get('research_readiness', 25) + ex.get('evidence_ledger_readiness', 22) +
                                ex.get('civic_intelligence_readiness', 24)) / 3),
    },
    {
        'id': 'learning', 'title': 'Learning Engine',
        'components': ['Curriculum', 'Academy', 'Media', 'Interactive Learning', 'Storytelling'],
        'readiness_pct': round((ex.get('curriculum_readiness', 26) + ex.get('education_academy_readiness', 26) +
                                ex.get('media_studio_readiness', 18) + ex.get('narrative_readiness', 24)) / 4),
    },
    {
        'id': 'community', 'title': 'Community Engine',
        'components': ['Education Leaders', 'Coalition', 'Counties', 'Events', 'Contact Network'],
        'readiness_pct': round((ex.get('coalition_readiness', 18) + ex.get('county_os_readiness', 28) +
                                ex.get('signup_funnel_readiness', 22)) / 3),
    },
    {
        'id': 'institution', 'title': 'Institution Engine',
        'components': ['Mission Control', 'Publishing', 'Technology', 'Governance', 'Operations'],
        'readiness_pct': round((ex.get('governance_readiness', 44) + ex.get('technical_architecture_readiness', 38) +
                                ex.get('pmo_readiness', 46)) / 3),
    },
]

VISITOR_JOURNEY = [
    {'stage': 1, 'id': 'curiosity', 'title': 'Curiosity', 'status': 'partial'},
    {'stage': 2, 'id': 'discovery', 'title': 'Discovery', 'status': 'partial'},
    {'stage': 3, 'id': 'understanding', 'title': 'Understanding', 'status': 'planned'},
    {'stage': 4, 'id': 'confidence', 'title': 'Confidence', 'status': 'planned'},
    {'stage': 5, 'id': 'connection', 'title': 'Connection', 'status': 'planned'},
    {'stage': 6, 'id': 'participation', 'title': 'Participation', 'status': 'planned'},
    {'stage': 7, 'id': 'leadership', 'title': 'Leadership', 'status': 'planned'},
    {'stage': 8, 'id': 'legacy', 'title': 'Legacy', 'status': 'planned'},
]

EDUCATION_LEVELS = [
    {'level': 1, 'title': 'Simple explanation', 'status': 'partial'},
    {'level': 2, 'title': 'Expanded lesson', 'status': 'partial'},
    {'level': 3, 'title': 'Complete article', 'status': 'partial'},
    {'level': 4, 'title': 'Primary sources', 'status': 'partial'},
    {'level': 5, 'title': 'Research archive', 'status': 'partial'},
]

PHILOSOPHIES = {
    'trust': ['Evidence', 'Transparency', 'Documentation', 'Primary sources', 'Version history', 'Corrections', 'Intellectual honesty'],
    'technology': ['Technology invisible', 'Institution is the product', 'Maintainability', 'Documentation', 'Accessibility', 'Performance', 'Institutional continuity'],
    'research': ['Documented', 'Verified', 'Reviewed', 'Cited', 'Connected', 'Revisited', 'Never finished'],
    'community': ['Education Leaders', 'Community conversations', 'Coalition organizations', 'County networks', 'Public understanding', 'Shared knowledge'],
}

GROWTH_DIMENSIONS = [
    {'dimension': 'Knowledge', 'focus': 'More research, sources, lessons', 'readiness_pct': ex.get('content_readiness', 28)},
    {'dimension': 'Community', 'focus': 'More leaders, counties, coalition orgs', 'readiness_pct': ex.get('coalition_readiness', 18)},
    {'dimension': 'Institution', 'focus': 'Better technology, governance, transparency, curriculum', 'readiness_pct': ex.get('institutional_maturity_pct', 40)},
]

SUCCESS_FIVE_YEAR = [
    {'goal': 'Every Arkansas county has educational presence', 'status': 'planned', 'current': '0/75 counties with participation'},
    {'goal': 'Thousands complete learning paths', 'status': 'planned', 'current': 'No path completion tracking'},
    {'goal': 'Hundreds of active Education Leaders', 'status': 'planned', 'current': f'{edu_leaders} leaders'},
    {'goal': 'Strong coalition supports civic education', 'status': 'planned', 'current': f'{orgs} organizations'},
    {'goal': 'Widely recognized trusted educational resource', 'status': 'planned', 'current': '8% public launch readiness'},
    {'goal': 'MC demonstrates measurable educational growth', 'status': 'planned', 'current': 'No analytics store'},
    {'goal': 'Part of Arkansas civic infrastructure', 'status': 'planned', 'current': 'V1 foundation only'},
]

NEXT_PHASE = [
    {'id': 'IMPL-01', 'workstream': 'Database schema', 'status': 'partial', 'route': '/mission-control/database.html'},
    {'id': 'IMPL-02', 'workstream': 'Repository architecture', 'status': 'partial', 'route': '/mission-control/repository.html'},
    {'id': 'IMPL-03', 'workstream': 'Route map', 'status': 'partial', 'route': '/mission-control/routes.html'},
    {'id': 'IMPL-04', 'workstream': 'Component library', 'status': 'partial', 'route': '/mission-control/components.html'},
    {'id': 'IMPL-05', 'workstream': 'Design system', 'status': 'partial', 'route': '/design-system/'},
    {'id': 'IMPL-06', 'workstream': 'Mission Control implementation', 'status': 'partial', 'route': '/mission-control/'},
    {'id': 'IMPL-07', 'workstream': 'Knowledge Graph implementation', 'status': 'partial', 'route': '/mission-control/knowledge-graph.html'},
    {'id': 'IMPL-08', 'workstream': 'Evidence Ledger implementation', 'status': 'partial', 'route': '/mission-control/evidence-ledger.html'},
    {'id': 'IMPL-09', 'workstream': 'Content production', 'status': 'partial', 'route': '/mission-control/content-production-matrix.html'},
    {'id': 'IMPL-10', 'workstream': 'County framework', 'status': 'partial', 'route': '/mission-control/county-os.html'},
    {'id': 'IMPL-11', 'workstream': 'Educational curriculum production', 'status': 'partial', 'route': '/mission-control/curriculum.html'},
]

CONSTITUTION_INDEX = [
    {'build': 55, 'title': 'Master Master Plan', 'role': 'North Star — read first', 'route': '/docs/MASTER_MASTER_PLAN.md', 'status': 'live'},
    {'build': 50, 'title': 'Master Build Bible', 'role': 'System index', 'route': '/docs/MASTER_BUILD_BIBLE.md', 'status': 'live'},
    {'build': 54, 'title': 'Master PMO', 'role': 'Execution system', 'route': '/docs/MASTER_PMO.md', 'status': 'live'},
    {'build': 53, 'title': 'Launch Strategy', 'role': 'Arkansas rollout', 'route': '/docs/MASTER_LAUNCH_STRATEGY.md', 'status': 'live'},
    {'build': 52, 'title': 'UX Architecture', 'role': 'Experience blueprint', 'route': '/docs/MASTER_UX_ARCHITECTURE.md', 'status': 'live'},
    {'build': 51, 'title': 'Data Architecture', 'role': 'Data constitution', 'route': '/docs/MASTER_DATA_ARCHITECTURE.md', 'status': 'live'},
    {'build': 49, 'title': 'Governance Constitution', 'role': 'Institutional rules', 'route': '/docs/MASTER_GOVERNANCE_CONSTITUTION.md', 'status': 'live'},
    {'build': 48, 'title': 'Technical Architecture', 'role': 'Engineering blueprint', 'route': '/docs/MASTER_TECHNICAL_ARCHITECTURE.md', 'status': 'live'},
    {'build': 47, 'title': 'Visitor Journey', 'role': 'Behavioral architecture', 'route': '/docs/MASTER_VISITOR_JOURNEY.md', 'status': 'live'},
    {'build': 2, 'title': 'Project Constitution', 'role': 'Original charter', 'route': '/builds/002-project-constitution.md', 'status': 'live'},
]

KG_ENTITIES = [
    'Person', 'Court case', 'Law', 'Timeline', 'Claim', 'Source', 'Lesson', 'County',
    'Organization', 'Event', 'Presentation', 'Video', 'Research paper',
]

model_live = sum(1 for m in INSTITUTIONAL_MODEL if m['status'] == 'live')
model_partial = sum(1 for m in INSTITUTIONAL_MODEL if m['status'] == 'partial')
avg_engine = round(sum(e['readiness_pct'] for e in ENGINES) / len(ENGINES))
impl_partial = sum(1 for w in NEXT_PHASE if w['status'] == 'partial')

MC_METRICS = [
    {'id': 'MP-01', 'title': 'Master Plan constitution live', 'status': 'live', 'current': 'Build #55 North Star'},
    {'id': 'MP-02', 'title': 'Planning builds complete', 'status': 'live', 'current': f'{builds_logged} builds'},
    {'id': 'MP-03', 'title': 'Constitution documents indexed', 'status': 'live', 'current': f'{len(CONSTITUTION_INDEX)} master docs'},
    {'id': 'MP-04', 'title': 'Twelve pillars defined', 'status': 'live', 'current': f'{len(PILLARS)}/12'},
    {'id': 'MP-05', 'title': 'Four engines operational', 'status': 'planned', 'current': f'{avg_engine}% avg readiness'},
    {'id': 'MP-06', 'title': 'Institutional model facets live', 'status': 'partial', 'current': f'{model_live} live, {model_partial} partial'},
    {'id': 'MP-07', 'title': 'Knowledge graph connected', 'status': 'partial', 'current': f'{kg_nodes}/500 nodes'},
    {'id': 'MP-08', 'title': 'Educational content published', 'status': 'partial', 'current': f'{published} assets'},
    {'id': 'MP-09', 'title': 'Implementation phase active', 'status': 'partial', 'current': f'{impl_partial}/{len(NEXT_PHASE)} workstreams partial'},
    {'id': 'MP-10', 'title': 'Translation layer to engineering', 'status': 'planned', 'current': 'Build #56 recommended'},
    {'id': 'MP-11', 'title': 'Five-year success criteria met', 'status': 'planned', 'current': '0/7 goals achieved'},
    {'id': 'MP-12', 'title': 'Master plan readiness score', 'status': 'partial', 'current': 'See summary'},
]

readiness_factors = [
    100,  # north star document
    100,  # pillars/engines/journey defined
    len(CONSTITUTION_INDEX) / 10 * 100,
    avg_engine,
    ex.get('public_launch_readiness', 8),
    (model_live * 100 + model_partial * 50) / len(INSTITUTIONAL_MODEL),
    impl_partial / len(NEXT_PHASE) * 50,
    0,  # translation layer
    ex.get('institutional_maturity_pct', 40),
    100,  # MC dashboard after build
]
master_plan_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 55,
    'updated': today,
    'title': 'Master Master Plan v1.0',
    'subtitle': 'The Complete Institutional Blueprint & Execution Constitution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/master-plan.html',
    'constitution': '/docs/MASTER_MASTER_PLAN.md',
    'purpose': 'Ties together Builds #1–54 — first document for any new steward ten years from now.',
    'governing_principle': (
        'Not built to win an election cycle — built to strengthen civic understanding across Arkansas '
        'for generations. This is the permanent North Star; future builds expand, never contradict.'
    ),
    'milestone': {
        'number': 55,
        'title': 'Planning Constitution Complete',
        'planning_builds': builds_logged,
        'shift': 'Constitution → Engineering Translation',
        'note': 'Digital civic education institution specified — next: implementation artifacts',
    },
    'institutional_motto': 'Understand First. Verify Always. Teach Others.',
    'the_why': {
        'context': 'Citizens United changed national conversation on campaign finance and the First Amendment',
        'gaps': WHY_GAPS,
        'arkansas_purpose': 'Close the educational gap for Arkansas',
    },
    'mission': 'Build Arkansas\'s most trusted, transparent, evidence-based educational institution devoted to understanding Citizens United v. FEC.',
    'mission_rule': 'The institution exists to educate. Everything else supports education.',
    'vision': {
        'capabilities': ['Discover', 'Learn', 'Research', 'Verify', 'Teach', 'Lead', 'Build community', 'Strengthen civic understanding'],
        'outcome': 'Public educational utility — not a temporary website',
    },
    'institutional_model': {
        'title': 'Ten Simultaneous Facets',
        'facets': INSTITUTIONAL_MODEL,
        'live': model_live,
        'partial': model_partial,
        'planned': sum(1 for m in INSTITUTIONAL_MODEL if m['status'] == 'planned'),
    },
    'arkansas_model': {
        'principle': 'Everything begins and ends with Arkansas',
        'question': 'How does this help educate Arkansans?',
        'pilot_state': 'Arkansas',
    },
    'twelve_pillars': {
        'title': 'Permanent Institutional Organization',
        'pillars': PILLARS,
        'pillars_total': len(PILLARS),
        'source': 'Aligned with Build #50 Build Bible',
    },
    'four_engines': {
        'title': 'Operating Engines',
        'engines': ENGINES,
        'avg_readiness_pct': avg_engine,
        'source': 'Build #50 + Build #55 synthesis',
    },
    'visitor_journey': {
        'title': 'Eight-Stage Journey',
        'stages': VISITOR_JOURNEY,
        'flow': 'Curiosity → Discovery → Understanding → Confidence → Connection → Participation → Leadership → Legacy',
    },
    'educational_philosophy': {
        'title': 'Five Learning Layers',
        'levels': EDUCATION_LEVELS,
        'principle': 'Visitors choose depth',
    },
    'philosophies': PHILOSOPHIES,
    'mission_control': {
        'role': 'Executive brain of the institution',
        'questions': ['Where are we?', "What's healthy?", "What's missing?", "What's next?"],
        'route': '/mission-control/',
        'status': 'live',
    },
    'knowledge_graph': {
        'entity_types': KG_ENTITIES,
        'nodes_current': kg_nodes,
        'nodes_target': 500,
        'principle': 'Nothing stands alone',
        'route': '/data/kg-registry.json',
    },
    'institutional_growth': {
        'dimensions': GROWTH_DIMENSIONS,
        'principle': 'Every year more valuable than the year before',
    },
    'success_five_year': {
        'title': 'What Success Looks Like',
        'goals': SUCCESS_FIVE_YEAR,
        'goals_achieved': 0,
    },
    'next_major_phase': {
        'title': 'Execution Dominates',
        'planning_status': 'Largely complete',
        'workstreams': NEXT_PHASE,
        'dominant_activities': ['Engineering', 'Content production'],
    },
    'institutional_promise': [
        'Every visitor leaves knowing more than when they arrived',
        'Every contributor leaves the institution stronger',
        'Every future steward inherits better documentation, research, resources, and relationships',
    ],
    'constitution_index': {
        'title': 'Master Documents — Read Order',
        'documents': CONSTITUTION_INDEX,
        'read_first': '/docs/MASTER_MASTER_PLAN.md',
    },
    'synthesis': {
        'title': 'Builds #1–54 Integrated',
        'key_blueprints': [
            {'build': 51, 'title': 'Data Architecture', 'route': '/data/data-architecture.json'},
            {'build': 52, 'title': 'UX Architecture', 'route': '/data/ux-architecture.json'},
            {'build': 53, 'title': 'Launch Strategy', 'route': '/data/launch-strategy.json'},
            {'build': 54, 'title': 'PMO', 'route': '/data/pmo.json'},
            {'build': 50, 'title': 'Build Bible', 'route': '/data/build-bible.json'},
        ],
        'foundation_systems': bb_sum.get('foundation_systems', 28),
        'planning_builds_at_bible': bb_sum.get('planning_builds_complete', 50),
    },
    'mc_integration': {
        'title': 'Master Plan Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'north_star_document': True,
    },
    'summary': {
        'planning_builds_total': builds_logged,
        'pillars_total': len(PILLARS),
        'engines_total': len(ENGINES),
        'avg_engine_readiness_pct': avg_engine,
        'constitution_docs': len(CONSTITUTION_INDEX),
        'institutional_model_live': model_live,
        'knowledge_graph_nodes': kg_nodes,
        'content_published': published,
        'education_leaders': edu_leaders,
        'coalition_orgs': orgs,
        'implementation_workstreams': len(NEXT_PHASE),
        'five_year_goals_achieved': 0,
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
        'institutional_maturity_pct': ex.get('institutional_maturity_pct', 40),
        'planning_constitution_complete': True,
        'implementation_translation_started': False,
        'master_plan_readiness_pct': master_plan_readiness,
    },
    'catalog_gaps': [
        '55 planning builds ≠ working institution — constitution complete, execution minimal',
        f'Avg engine readiness {avg_engine}% — blueprints dominate over operational systems',
        f'{published} published of ~2700 content target — production workstream early',
        f'{kg_nodes}/500 KG nodes · 0 relationship edges — graph theoretical',
        f'0 Education Leaders · {orgs} coalition orgs — community engine empty',
        'Translation layer not built — no unified API contracts or GitHub issue backlog from constitution',
        'Component library (Build #17) never fully spec\'d — blocks direct Cursor implementation',
        'Neon/Prisma/Next.js migration documented not started',
        'Build #50 Build Bible and Build #55 Master Plan coexist — #55 is North Star, #50 is index',
        'Three journey models (Build #8, #47, #55) — emotional, behavioral, master plan stages',
        'Five-year success criteria 0/7 — aspirational only',
    ],
    'recommended_next_build': {
        'number': 56,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Turn constitutional documents into engineering artifacts: Neon schema migration, '
            'route inventory enforcement, COMP-* props/states, API contracts, GitHub issue backlog — '
            'so Cursor builds directly from blueprint without reinterpretation.'
        ),
    },
}

path = root / 'data/master-plan.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Master Plan: {builds_logged} builds synthesized, {avg_engine}% avg engines, {master_plan_readiness}% readiness')
