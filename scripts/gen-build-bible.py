"""
Generate data/build-bible.json — Build #50 Master Build Bible v1.0.
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
exec_e = mc.get('executive', {})

PHASE_I_FOUNDATION = [
    {'id': 'FND-01', 'title': 'Vision and Mission', 'build': 2, 'route': '/builds/002-project-constitution.md', 'status': 'designed'},
    {'id': 'FND-02', 'title': 'Information Architecture', 'build': 5, 'route': '/mission-control/architecture.html', 'status': 'designed'},
    {'id': 'FND-03', 'title': 'Master Build Plan', 'build': None, 'route': '/BUILD_PLAN.md', 'status': 'designed'},
    {'id': 'FND-04', 'title': 'Technical Architecture', 'build': 48, 'route': '/mission-control/technical-architecture.html', 'status': 'designed'},
    {'id': 'FND-05', 'title': 'Mission Control', 'build': 4, 'route': '/mission-control/', 'status': 'partial'},
    {'id': 'FND-06', 'title': 'Contact Intelligence', 'build': 24, 'route': '/mission-control/contact-intelligence.html', 'status': 'designed'},
    {'id': 'FND-07', 'title': 'Coalition Framework', 'build': 14, 'route': '/mission-control/coalition.html', 'status': 'designed'},
    {'id': 'FND-08', 'title': 'Community Education Academy', 'build': 28, 'route': '/mission-control/education-academy.html', 'status': 'designed'},
    {'id': 'FND-09', 'title': 'Research Observatory', 'build': 29, 'route': '/mission-control/research-observatory.html', 'status': 'designed'},
    {'id': 'FND-10', 'title': 'Civic Action Lab', 'build': 42, 'route': '/mission-control/civic-action-lab.html', 'status': 'designed'},
    {'id': 'FND-11', 'title': 'Knowledge Graph', 'build': 40, 'route': '/mission-control/civic-intelligence.html', 'status': 'partial'},
    {'id': 'FND-12', 'title': 'Evidence Ledger', 'build': 41, 'route': '/mission-control/evidence-ledger.html', 'status': 'partial'},
    {'id': 'FND-13', 'title': 'Research Library', 'build': 37, 'route': '/mission-control/research-library.html', 'status': 'designed'},
    {'id': 'FND-14', 'title': 'Encyclopedia', 'build': 33, 'route': '/mission-control/encyclopedia.html', 'status': 'designed'},
    {'id': 'FND-15', 'title': 'Curriculum', 'build': 35, 'route': '/mission-control/curriculum.html', 'status': 'designed'},
    {'id': 'FND-16', 'title': 'Media Studio', 'build': 39, 'route': '/mission-control/media-studio.html', 'status': 'designed'},
    {'id': 'FND-17', 'title': 'Interactive Learning Laboratory', 'build': 38, 'route': '/mission-control/learning-lab.html', 'status': 'designed'},
    {'id': 'FND-18', 'title': 'Storytelling Architecture', 'build': 34, 'route': '/mission-control/narrative.html', 'status': 'designed'},
    {'id': 'FND-19', 'title': 'Outreach Engine', 'build': 30, 'route': '/mission-control/outreach.html', 'status': 'designed'},
    {'id': 'FND-20', 'title': 'County Operating System', 'build': 31, 'route': '/mission-control/county-os.html', 'status': 'designed'},
    {'id': 'FND-21', 'title': 'Institutional Governance', 'build': 49, 'route': '/mission-control/governance.html', 'status': 'designed'},
    {'id': 'FND-22', 'title': 'Institutional Roadmap', 'build': 44, 'route': '/mission-control/institutional-roadmap.html', 'status': 'designed'},
    {'id': 'FND-23', 'title': 'Systems Integration', 'build': 45, 'route': '/mission-control/systems-integration.html', 'status': 'designed'},
    {'id': 'FND-24', 'title': 'Production Matrix', 'build': 46, 'route': '/mission-control/content-production-matrix.html', 'status': 'designed'},
    {'id': 'FND-25', 'title': 'Visitor Journey', 'build': 47, 'route': '/mission-control/visitor-journey.html', 'status': 'designed'},
    {'id': 'FND-26', 'title': 'Research Methodology', 'build': 43, 'route': '/mission-control/research-methodology.html', 'status': 'designed'},
    {'id': 'FND-27', 'title': 'Trust Framework', 'build': 36, 'route': '/mission-control/trust.html', 'status': 'designed'},
    {'id': 'FND-28', 'title': 'Technical Constitution', 'build': 48, 'route': '/docs/MASTER_TECHNICAL_ARCHITECTURE.md', 'status': 'designed'},
]

PILLARS = [
    {'number': 1, 'id': 'research', 'title': 'Research', 'purpose': 'Discover and verify knowledge', 'systems': ['Research Observatory', 'Research Library', 'Research Methodology']},
    {'number': 2, 'id': 'evidence', 'title': 'Evidence', 'purpose': 'Support every factual claim', 'systems': ['Evidence Ledger', 'Trust Framework', 'Source Library']},
    {'number': 3, 'id': 'education', 'title': 'Education', 'purpose': 'Teach complex subjects clearly', 'systems': ['Public Education Platform', 'Halls', 'Explore Map']},
    {'number': 4, 'id': 'encyclopedia', 'title': 'Encyclopedia', 'purpose': 'Organize institutional knowledge', 'systems': ['Encyclopedia Knowledge Library']},
    {'number': 5, 'id': 'curriculum', 'title': 'Curriculum', 'purpose': 'Guide structured learning', 'systems': ['Master Curriculum', 'Learning Ladder']},
    {'number': 6, 'id': 'community', 'title': 'Community', 'purpose': 'Develop Arkansas Education Leaders', 'systems': ['Education Academy', 'Contact Intelligence']},
    {'number': 7, 'id': 'coalition', 'title': 'Coalition', 'purpose': 'Expand educational partnerships', 'systems': ['Coalition Network', 'Outreach Engine']},
    {'number': 8, 'id': 'media', 'title': 'Media', 'purpose': 'Teach through multiple formats', 'systems': ['Media Studio', 'Narrative Architecture']},
    {'number': 9, 'id': 'solutions', 'title': 'Solutions', 'purpose': 'Educate about legislative and ballot processes', 'systems': ['Civic Action Lab', 'Solutions Center']},
    {'number': 10, 'id': 'mission-control', 'title': 'Mission Control', 'purpose': 'Operate the institution', 'systems': ['MC Executive', 'Build Registry', 'Progress Dashboards']},
    {'number': 11, 'id': 'knowledge-graph', 'title': 'Knowledge Graph', 'purpose': 'Connect every idea, document, lesson, relationship', 'systems': ['Civic Intelligence', 'KG Registry']},
    {'number': 12, 'id': 'governance', 'title': 'Governance', 'purpose': "Protect the institution's integrity", 'systems': ['Governance Constitution', 'Institutional Roadmap']},
]

ENGINES = [
    {
        'id': 'ENG-K', 'title': 'Knowledge Engine',
        'components': ['Research', 'Evidence', 'Encyclopedia', 'Claims Registry', 'Source Library', 'Knowledge Graph'],
        'readiness_pct': round((exec_e.get('research_readiness', 0) + exec_e.get('evidence_ledger_readiness', 0) + exec_e.get('encyclopedia_readiness', 0) + exec_e.get('civic_intelligence_readiness', 0) + exec_e.get('library_readiness', 0)) / 5),
    },
    {
        'id': 'ENG-L', 'title': 'Learning Engine',
        'components': ['Curriculum', 'Academy', 'Media', 'Interactive Laboratory', 'Storytelling', 'Presentations'],
        'readiness_pct': round((exec_e.get('curriculum_readiness', 0) + exec_e.get('education_academy_readiness', 0) + exec_e.get('media_studio_readiness', 0) + exec_e.get('learning_lab_readiness', 0) + exec_e.get('narrative_readiness', 0)) / 5),
    },
    {
        'id': 'ENG-C', 'title': 'Community Engine',
        'components': ['Education Leaders', 'Coalition', 'County Network', 'Community Conversations', 'Events', 'Contact Network'],
        'readiness_pct': round((exec_e.get('education_academy_readiness', 0) + exec_e.get('coalition_readiness', 0) + exec_e.get('county_os_readiness', 0) + exec_e.get('outreach_readiness', 0) + exec_e.get('contact_intelligence_readiness', 0)) / 5),
    },
    {
        'id': 'ENG-I', 'title': 'Institutional Engine',
        'components': ['Mission Control', 'Publishing', 'Governance', 'Technology', 'Analytics', 'Planning'],
        'readiness_pct': round((exec_e.get('mc2_readiness', 0) + exec_e.get('content_factory_readiness', 0) + exec_e.get('governance_readiness', 0) + exec_e.get('technical_architecture_readiness', 0) + exec_e.get('institutional_maturity_pct', 0)) / 5),
    },
]

WORKSTREAMS = [
    {'id': 'WS-R', 'title': 'Research', 'focus': 'Collect, verify, and organize evidence', 'readiness_pct': exec_e.get('research_readiness', 0), 'status': 'partial'},
    {'id': 'WS-C', 'title': 'Content', 'focus': 'Write educational materials', 'readiness_pct': exec_e.get('content_readiness', 0), 'status': 'partial'},
    {'id': 'WS-D', 'title': 'Design', 'focus': 'Create visual experiences and multimedia', 'readiness_pct': exec_e.get('wireframe_readiness', 0), 'status': 'partial'},
    {'id': 'WS-E', 'title': 'Engineering', 'focus': 'Build the software platform', 'readiness_pct': exec_e.get('technical_architecture_readiness', 0), 'status': 'partial'},
    {'id': 'WS-CO', 'title': 'Community', 'focus': 'Recruit Education Leaders and coalition partners', 'readiness_pct': exec_e.get('coalition_readiness', 0), 'status': 'planned'},
    {'id': 'WS-O', 'title': 'Operations', 'focus': 'Run Mission Control, governance, and planning', 'readiness_pct': exec_e.get('governance_readiness', 0), 'status': 'partial'},
]

DEV_PHASES = [
    {
        'id': 'PHA', 'letter': 'A', 'title': 'Core Platform',
        'items': ['Public website', 'Mission Control', 'Authentication', 'Content framework', 'Search', 'Knowledge Graph foundation'],
        'status': 'partial', 'note': 'Static site + MC live — auth/search/KG foundation not built',
    },
    {
        'id': 'PHB', 'letter': 'B', 'title': 'Knowledge Expansion',
        'items': ['Research Library', 'Encyclopedia', 'Claims Registry', 'Evidence Ledger', 'Curriculum'],
        'status': 'partial', 'note': 'Blueprints live — 3 claims, 15 pages published',
    },
    {
        'id': 'PHC', 'letter': 'C', 'title': 'Community Growth',
        'items': ['Education Academy', 'Coalition Network', 'County Pages', 'Contact Network', 'Community Conversations'],
        'status': 'planned', 'note': '0 leaders, 0 coalition orgs, 0 county participation',
    },
    {
        'id': 'PHD', 'letter': 'D', 'title': 'Interactive Experience',
        'items': ['Learning Laboratory', 'Media Studio', 'Knowledge Explorer', 'Timeline Explorer', 'Presentation Builder'],
        'status': 'planned', 'note': '0 videos, 0 interactive experiences',
    },
    {
        'id': 'PHE', 'letter': 'E', 'title': 'Institutional Maturity',
        'items': ['Research Observatory', 'AI Educational Guide', 'Advanced Mission Control', 'Long-term governance', 'Annual institutional reporting'],
        'status': 'planned', 'note': 'AI 14% — annual report not generated',
    },
]

MC_RESPONSIBILITIES = [
    'Development progress', 'Content production', 'Research verification', 'Evidence quality',
    'Coalition growth', 'County coverage', 'Education Leader development', 'Community conversations',
    'Media production', 'Technology health', 'Accessibility', 'Institutional readiness',
]

VISITOR_JOURNEY = [
    'Discover', 'Learn', 'Understand', 'Verify', 'Explore', 'Discuss', 'Teach', 'Lead', 'Mentor',
    'Strengthen Arkansas civic education',
]

WHAT_COMES_NEXT = [
    'Design system implementation', 'Data model execution', 'Database schema provisioning',
    'Component library (COMP-* specs)', 'GitHub repository structure migration',
    'Netlify deployment hardening', 'Development roadmap', 'Sprint planning',
    'Technical execution', 'Initial content production',
]

foundation_designed = sum(1 for f in PHASE_I_FOUNDATION if f['status'] in ('designed', 'partial'))
foundation_partial = sum(1 for f in PHASE_I_FOUNDATION if f['status'] == 'partial')
avg_engine_readiness = round(sum(e['readiness_pct'] for e in ENGINES) / len(ENGINES))
avg_workstream = round(sum(w['readiness_pct'] for w in WORKSTREAMS) / len(WORKSTREAMS))
phases_partial = sum(1 for p in DEV_PHASES if p['status'] == 'partial')
phases_planned = sum(1 for p in DEV_PHASES if p['status'] == 'planned')

MC_METRICS = [
    {'id': 'BB-01', 'title': 'Planning builds complete', 'status': 'live', 'current': '50/50'},
    {'id': 'BB-02', 'title': 'Foundation systems indexed', 'status': 'live', 'current': f'{len(PHASE_I_FOUNDATION)}/28'},
    {'id': 'BB-03', 'title': 'Institutional pillars defined', 'status': 'live', 'current': f'{len(PILLARS)}/12'},
    {'id': 'BB-04', 'title': 'Operating engines mapped', 'status': 'live', 'current': f'{len(ENGINES)}/4'},
    {'id': 'BB-05', 'title': 'Workstreams active', 'status': 'partial', 'current': f'{avg_workstream}% avg readiness'},
    {'id': 'BB-06', 'title': 'Implementation phases defined', 'status': 'live', 'current': f'{len(DEV_PHASES)} phases'},
    {'id': 'BB-07', 'title': 'Phase A (Core Platform)', 'status': 'partial', 'current': 'Static v1 — auth/search pending'},
    {'id': 'BB-08', 'title': 'Avg engine operational readiness', 'status': 'partial', 'current': f'{avg_engine_readiness}%'},
    {'id': 'BB-09', 'title': 'Build Bible master index', 'status': 'live', 'current': 'All major blueprints linked'},
    {'id': 'BB-10', 'title': 'Implementation phase started', 'status': 'planned', 'current': 'Sprint Zero not begun'},
]

readiness_factors = [
    100,  # 50 planning builds
    100,  # foundation indexed
    100,  # pillars/engines defined
    avg_engine_readiness,
    avg_workstream,
    phases_partial / len(DEV_PHASES) * 100 * 0.5,
    0,    # implementation not started
    foundation_partial / len(PHASE_I_FOUNDATION) * 100,
]
build_bible_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 50,
    'updated': today,
    'title': 'Master Build Bible v1.0',
    'subtitle': 'The Institutional Blueprint — The First Complete Architecture',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/build-bible.html',
    'constitution': '/docs/MASTER_BUILD_BIBLE.md',
    'purpose': 'Master index integrating every blueprint — shift from designing to building the institution.',
    'governing_principle': 'Does this strengthen evidence-based civic education for Arkansans? If yes, it belongs. If not, it waits.',
    'milestone': {
        'planning_phase': 'Complete',
        'implementation_phase': 'Beginning',
        'builds_in_planning': 50,
        'shift': 'Design → Engineering',
    },
    'phase_i_foundation': {
        'title': 'Phase I — Institutional Foundation',
        'status': 'complete',
        'systems_total': len(PHASE_I_FOUNDATION),
        'systems_designed': foundation_designed,
        'systems_partial': foundation_partial,
        'systems': PHASE_I_FOUNDATION,
    },
    'institutional_pillars': {
        'title': 'Twelve Institutional Pillars',
        'pillars_total': len(PILLARS),
        'pillars': PILLARS,
    },
    'operating_engines': {
        'title': 'Four Operating Engines',
        'engines_total': len(ENGINES),
        'engines': ENGINES,
        'avg_readiness_pct': avg_engine_readiness,
    },
    'workstreams': {
        'title': 'Permanent Workstreams',
        'workstreams_total': len(WORKSTREAMS),
        'streams': WORKSTREAMS,
        'avg_readiness_pct': avg_workstream,
    },
    'development_phases': {
        'title': 'Implementation Development Phases',
        'phases_total': len(DEV_PHASES),
        'phases': DEV_PHASES,
        'partial': phases_partial,
        'planned': phases_planned,
    },
    'mission_control_responsibilities': MC_RESPONSIBILITIES,
    'arkansas_focus': {
        'principle': 'National context — Arkansas purpose',
        'question': 'How does this help educate Arkansans?',
        'pilot_state': 'Arkansas',
    },
    'ultimate_visitor_journey': VISITOR_JOURNEY,
    'what_comes_next': {
        'title': 'Implementation Priorities',
        'phase': 'Engineering — no longer conceptual planning',
        'priorities': WHAT_COMES_NEXT,
    },
    'long_term_vision': {
        'institution': 'Permanent Arkansas civic education institution',
        'combines': [
            'Constitutional law library', 'Historical museum', 'University curriculum',
            'Public research institute', 'Documentary studio', 'Statewide coalition',
            'Civic leadership academy', 'Modern digital platform',
        ],
    },
    'mc_integration': {
        'title': 'Build Bible Metrics',
        'status': 'live',
        'metrics': MC_METRICS,
        'authoritative_reference': True,
    },
    'master_index': {
        'title': 'Blueprint Cross-Reference',
        'recent_builds': [
            {'build': 49, 'title': 'Governance Constitution', 'route': '/data/governance-constitution.json'},
            {'build': 48, 'title': 'Technical Architecture', 'route': '/data/technical-architecture.json'},
            {'build': 47, 'title': 'Visitor Journey', 'route': '/data/visitor-journey.json'},
            {'build': 46, 'title': 'Production Matrix', 'route': '/data/content-production-matrix.json'},
            {'build': 45, 'title': 'Systems Integration', 'route': '/data/systems-integration.json'},
            {'build': 44, 'title': 'Institutional Roadmap', 'route': '/data/institutional-roadmap.json'},
        ],
        'build_registry': '/builds/',
        'mission_control': '/data/mission-control.json',
        'build_plan': '/BUILD_PLAN.md',
    },
    'summary': {
        'planning_builds_complete': 50,
        'foundation_systems': len(PHASE_I_FOUNDATION),
        'pillars_total': len(PILLARS),
        'engines_total': len(ENGINES),
        'workstreams_total': len(WORKSTREAMS),
        'implementation_phases': len(DEV_PHASES),
        'avg_engine_readiness_pct': avg_engine_readiness,
        'avg_workstream_readiness_pct': avg_workstream,
        'institutional_maturity_pct': exec_e.get('institutional_maturity_pct', 32),
        'public_launch_readiness_pct': exec_e.get('public_launch_readiness', 8),
        'planning_phase_complete': True,
        'implementation_phase_started': False,
        'build_bible_readiness_pct': build_bible_readiness,
    },
    'catalog_gaps': [
        'Planning complete — operational implementation minimal across all engines',
        f'Avg engine readiness {avg_engine_readiness}% — blueprints ≠ working systems',
        'Phase C–E entirely planned — 0 leaders, 0 videos, 0 interactive tools',
        'Component library (Build #17) never spec\'d with props/states — blocks UI implementation',
        'Neon/Prisma/Next.js migration not started — static v1 remains production',
        '15 educational assets published of ~2045 target — content workstream early',
        'Build Bible indexes 28 systems — many share overlapping MC dashboards',
        'Sprint Zero and implementation roadmap not yet formalized as Build #51',
        'Annual institutional report and steward assignments still at zero',
        'Honest rule: 50 design builds ≠ institution ready for public launch (8%)',
    ],
    'recommended_next_build': {
        'number': 51,
        'title': 'Master Implementation Roadmap & Sprint Zero',
        'note': 'Data model execution, COMP-* component specs, database provisioning plan, repo migration, and first engineering sprint backlog.',
    },
}

path = root / 'data/build-bible.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Build Bible: 50 planning builds, {avg_engine_readiness}% avg engine readiness, {build_bible_readiness}% bible readiness')
