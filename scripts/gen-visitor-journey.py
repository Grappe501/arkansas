"""
Generate data/visitor-journey.json — Build #47 Master Visitor Journey & Behavioral Architecture v1.0.
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


ux = load_json(root / 'data/ux-journey.json')
mc = load_json(root / 'data/mission-control.json')
si = load_json(root / 'data/systems-integration.json')
ea = load_json(root / 'data/education-academy.json')
civic = mc.get('civic_action', {})

STAGES = [
    {
        'number': 1, 'id': 'curiosity', 'title': 'Curiosity',
        'description': 'Visitor knows very little — may have heard Citizens United, dark money, Super PACs.',
        'platform_goal': 'Reduce intimidation. Answer: What is this?',
        'success_metric': 'Visitor begins learning',
        'indicator': 'Visited homepage or orientation',
        'routes': ['/', '/explore/', '/educate/'],
        'build_8_stage': 'discover',
        'status': 'partial',
        'tracking_live': True,
        'note': 'localStorage stage key — no server analytics',
    },
    {
        'number': 2, 'id': 'discovery', 'title': 'Discovery',
        'description': 'Explores articles, timelines, videos, glossary, interactive tools.',
        'platform_goal': 'Keep curiosity alive.',
        'success_metric': 'Multiple lessons completed',
        'indicator': 'Visited 2+ halls or learning sections',
        'routes': ['/the-story', '/the-case', '/library/', '/mission-control/learning-lab.html'],
        'build_8_stage': 'understand',
        'status': 'partial',
        'tracking_live': False,
        'note': '0 interactive experiences live — lesson completion not measured',
    },
    {
        'number': 3, 'id': 'understanding', 'title': 'Understanding',
        'description': 'Connects history, law, constitution, money, politics, Arkansas.',
        'platform_goal': 'Build understanding.',
        'success_metric': 'Learning path completion',
        'indicator': 'Completed 1+ learning path tier',
        'routes': ['/the-constitution', '/follow-the-money', '/solutions/'],
        'build_8_stage': 'explore',
        'status': 'planned',
        'tracking_live': False,
        'note': 'Master Curriculum paths designed — completion tracking not built',
    },
    {
        'number': 4, 'id': 'confidence', 'title': 'Confidence',
        'description': 'Feels capable of explaining the case, its impact, and disagreements.',
        'platform_goal': 'Develop confidence.',
        'success_metric': 'Downloads teaching materials',
        'indicator': 'Downloaded toolkit or presentation resource',
        'routes': ['/teach', '/educate/', '/mission-control/curriculum.html'],
        'build_8_stage': 'evaluate',
        'status': 'planned',
        'tracking_live': False,
        'note': 'Downloadable toolkits planned — no download tracking',
    },
    {
        'number': 5, 'id': 'connection', 'title': 'Connection',
        'description': 'Joins Contact Network, attends events, joins coalition, asks questions.',
        'platform_goal': 'Build relationships.',
        'success_metric': 'First meaningful participation',
        'indicator': 'Contact form or coalition interest submitted',
        'routes': ['/coalition/', '/mission-control/contact-intelligence.html'],
        'build_8_stage': 'discuss',
        'status': 'planned',
        'tracking_live': False,
        'note': f"0 contact signups · 0 coalition orgs — forms not integrated",
    },
    {
        'number': 6, 'id': 'participation', 'title': 'Participation',
        'description': 'Hosts discussions, shares resources, Academy participation.',
        'platform_goal': 'Support community education.',
        'success_metric': 'Educational activity recorded',
        'indicator': 'Hosted conversation or shared resource',
        'routes': ['/mission-control/education-academy.html'],
        'build_8_stage': 'teach',
        'status': 'planned',
        'tracking_live': False,
        'note': 'Academy modules designed — 0 enrollments',
    },
    {
        'number': 7, 'id': 'leadership', 'title': 'Leadership',
        'description': 'Becomes Education Leader — teaching, mentoring, research, presentations.',
        'platform_goal': 'Multiply educational capacity.',
        'success_metric': 'Leadership profile established',
        'indicator': 'Education Leader signup or certification progress',
        'routes': ['/educate/', '/mission-control/education-academy.html'],
        'build_8_stage': 'lead',
        'status': 'planned',
        'tracking_live': False,
        'note': f"{civic.get('education_leader_signups', 0)} Education Leaders — 0 county participation",
    },
    {
        'number': 8, 'id': 'legacy', 'title': 'Legacy',
        'description': 'Mentors leaders, improves resources, contributes research, builds county education.',
        'platform_goal': 'Create institutional continuity.',
        'success_metric': 'Long-term contributions',
        'indicator': 'Mentored leader or sustained county/coalition contribution',
        'routes': ['/mission-control/county-os.html', '/coalition/'],
        'build_8_stage': None,
        'status': 'planned',
        'tracking_live': False,
        'note': 'Long-term model documented — no legacy tracking',
    },
]

JOURNEY_MAP = [
    {'id': 'visitors', 'title': 'Visitors', 'stage': 1, 'description': 'First-time or casual browsers'},
    {'id': 'learners', 'title': 'Learners', 'stage': 2, 'description': 'Engaged with 1+ educational sections'},
    {'id': 'returning_learners', 'title': 'Returning Learners', 'stage': 3, 'description': 'Multiple visits, deepening understanding'},
    {'id': 'participants', 'title': 'Participants', 'stage': 5, 'description': 'Connected via forms, events, or coalition'},
    {'id': 'education_leaders', 'title': 'Education Leaders', 'stage': 7, 'description': 'Certified or active educator profile'},
    {'id': 'coalition_members', 'title': 'Coalition Members', 'stage': 5, 'description': 'Organization partnership active'},
    {'id': 'county_leaders', 'title': 'County Leaders', 'stage': 7, 'description': 'County education team established'},
    {'id': 'mentors', 'title': 'Mentors', 'stage': 8, 'description': 'Mentoring next generation of educators'},
]

DECISION_POINTS = [
    {'order': 1, 'invitation': 'Continue Learning', 'route': '/explore/', 'stage': 'curiosity'},
    {'order': 2, 'invitation': 'View Sources', 'route': '/library/', 'stage': 'discovery'},
    {'order': 3, 'invitation': 'Watch Documentary', 'route': '/mission-control/media-studio.html', 'stage': 'discovery', 'note': '0 videos live'},
    {'order': 4, 'invitation': 'Explore Timeline', 'route': '/the-story', 'stage': 'discovery'},
    {'order': 5, 'invitation': 'Join Contact Network', 'route': '/mission-control/contact-intelligence.html', 'stage': 'connection'},
    {'order': 6, 'invitation': 'Teach Others', 'route': '/teach', 'stage': 'confidence'},
    {'order': 7, 'invitation': 'Join Coalition', 'route': '/coalition/', 'stage': 'connection'},
    {'order': 8, 'invitation': 'Lead Community Conversation', 'route': '/educate/', 'stage': 'participation'},
]

BEHAVIORAL_PRINCIPLES = [
    'Curiosity', 'Reflection', 'Critical thinking', 'Evidence exploration',
    'Respectful discussion', 'Continued learning', 'Community engagement',
]

ANTI_PATTERNS = ['Outrage', 'Urgency', 'Fear']

MILESTONES = [
    {'id': 'MS-01', 'title': 'Completed first lesson', 'stage': 'discovery', 'status': 'planned'},
    {'id': 'MS-02', 'title': 'Completed first learning path', 'stage': 'understanding', 'status': 'planned'},
    {'id': 'MS-03', 'title': 'Downloaded toolkit', 'stage': 'confidence', 'status': 'planned'},
    {'id': 'MS-04', 'title': 'Hosted first community conversation', 'stage': 'participation', 'status': 'planned'},
    {'id': 'MS-05', 'title': 'Joined coalition', 'stage': 'connection', 'status': 'planned'},
    {'id': 'MS-06', 'title': 'Contributed research', 'stage': 'leadership', 'status': 'planned'},
    {'id': 'MS-07', 'title': 'Mentored another Education Leader', 'stage': 'legacy', 'status': 'planned'},
]

RECOMMENDATION_TYPES = [
    'Next lessons', 'Related history', 'Related court cases', 'Community events',
    'Coalition opportunities', 'Research materials', 'Presentation resources',
]

# Journey analytics — honest current values
ANALYTICS = [
    {'id': 'JA-01', 'title': 'Average learning depth', 'current': 'Not measured', 'target': 'Stage 3+ avg', 'status': 'planned'},
    {'id': 'JA-02', 'title': 'Lesson completion', 'current': '0 tracked', 'target': 'Path completion rate', 'status': 'planned'},
    {'id': 'JA-03', 'title': 'Return rate', 'current': 'No analytics', 'target': '30%+ returning learners', 'status': 'planned'},
    {'id': 'JA-04', 'title': 'Academy enrollment', 'current': 0, 'target': '100+ leaders Y1', 'status': 'planned'},
    {'id': 'JA-05', 'title': 'Leadership development', 'current': civic.get('education_leader_signups', 0), 'target': '50+ Education Leaders', 'status': 'planned'},
    {'id': 'JA-06', 'title': 'Coalition participation', 'current': 0, 'target': '25+ orgs', 'status': 'planned', 'note': '0 coalition orgs registered'},
    {'id': 'JA-07', 'title': 'County participation', 'current': 0, 'target': '10+ active counties', 'status': 'planned'},
    {'id': 'JA-08', 'title': 'Presentation activity', 'current': 0, 'target': 'Monthly presentations', 'status': 'planned'},
    {'id': 'JA-09', 'title': 'Community conversations', 'current': 0, 'target': 'Quarterly statewide', 'status': 'planned'},
]

LONG_TERM_MODEL = {
    'learners': 'Thousands',
    'education_leaders': 'Hundreds',
    'coalition_organizations': 'Dozens',
    'community_conversations': 'Across Arkansas',
    'county_leadership_teams': '75 counties',
    'research_contributors': 'Ongoing',
    'presentation_volunteers': 'Active network',
    'institution': 'Permanent civic education institution',
}

stages_partial = sum(1 for s in STAGES if s['status'] == 'partial')
stages_tracking = sum(1 for s in STAGES if s['tracking_live'])
build8_ladder = len(ux.get('learning_ladder', []))
personas = len(ux.get('personas', []))

MC_METRICS = [
    {'id': 'VJ-01', 'title': 'Transformation stages defined', 'status': 'live', 'current': f'{len(STAGES)}/8'},
    {'id': 'VJ-02', 'title': 'Build #8 ladder mapped', 'status': 'live', 'current': f'{build8_ladder} stages → 8 stages'},
    {'id': 'VJ-03', 'title': 'Journey map personas', 'status': 'live', 'current': f'{len(JOURNEY_MAP)} roles'},
    {'id': 'VJ-04', 'title': 'Decision points documented', 'status': 'live', 'current': f'{len(DECISION_POINTS)} invitations'},
    {'id': 'VJ-05', 'title': 'Motivation milestones', 'status': 'partial', 'current': f'{len(MILESTONES)} defined — 0 tracked'},
    {'id': 'VJ-06', 'title': 'Personalized recommendations', 'status': 'planned', 'current': 'KG recommendations partial'},
    {'id': 'VJ-07', 'title': 'Journey analytics live', 'status': 'planned', 'current': f'{stages_tracking}/8 stages tracked'},
    {'id': 'VJ-08', 'title': 'localStorage session memory', 'status': 'partial', 'current': 'Build #8 — no server sync'},
    {'id': 'VJ-09', 'title': 'Education Leaders', 'current': civic.get('education_leader_signups', 0), 'status': 'planned', 'target': '50+'},
    {'id': 'VJ-10', 'title': 'Transformation funnel visualization', 'status': 'partial', 'current': 'MC dashboard — no live visitor counts'},
]

readiness_factors = [
    100,  # 8 stages defined
    min(100, stages_partial / len(STAGES) * 100 * 2),
    min(100, stages_tracking / len(STAGES) * 100 * 3),
    40,   # decision points + principles live
    0,    # analytics
    20,   # milestones defined not tracked
    personas / 6 * 30 if personas else 0,
]
visitor_journey_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 47,
    'updated': today,
    'title': 'Master Visitor Journey & Behavioral Architecture v1.0',
    'subtitle': 'From Curious Visitor to Community Educator',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/visitor-journey.html',
    'constitution': '/docs/MASTER_VISITOR_JOURNEY.md',
    'purpose': 'How does a curious visitor become a trusted community educator? — transformation, not page views.',
    'governing_principle': 'Transform curiosity into civic understanding — success measured by equipped educators, not visits.',
    'institutional_philosophy': 'How do we help one more Arkansan move one step deeper into understanding?',
    'extends': [
        {'title': 'Citizen Journey Blueprint', 'build': 8, 'route': '/data/ux-journey.json'},
        {'title': 'Systems Integration', 'build': 45, 'route': '/data/systems-integration.json'},
        {'title': 'Education Academy', 'build': 28, 'route': '/data/education-academy.json'},
        {'title': 'Contact Intelligence', 'build': 24, 'route': '/data/contact-intelligence.json'},
    ],
    'transformation_stages': STAGES,
    'stages_total': len(STAGES),
    'journey_map': JOURNEY_MAP,
    'decision_points': DECISION_POINTS,
    'behavioral_design': {
        'encourage': BEHAVIORAL_PRINCIPLES,
        'avoid': ANTI_PATTERNS,
        'principle': 'Understanding comes first.',
    },
    'motivation_system': {
        'title': 'Educational Milestones',
        'status': 'planned',
        'milestones': MILESTONES,
        'recognition_style': 'Learning and service — not competition',
    },
    'personalized_recommendations': {
        'title': 'Journey-Aware Recommendations',
        'status': 'planned',
        'types': RECOMMENDATION_TYPES,
        'host': '/mission-control/civic-intelligence.html',
        'note': 'Knowledge Graph partial — 38 nodes, not journey-aware',
    },
    'journey_analytics': {
        'title': 'Transformation Analytics',
        'status': 'planned',
        'metrics': ANALYTICS,
        'measures': 'Educational transformation — not traffic',
    },
    'long_term_community_model': LONG_TERM_MODEL,
    'build_8_mapping': {
        'title': 'Build #8 Learning Ladder → 8-Stage Model',
        'ux_journey': '/data/ux-journey.json',
        'ladder_stages': build8_ladder,
        'personas': personas,
        'session_memory': ux.get('session_memory', {}),
        'mapping': [
            {'build_8': 'discover', 'build_47': 'curiosity'},
            {'build_8': 'understand', 'build_47': 'discovery'},
            {'build_8': 'explore', 'build_47': 'understanding'},
            {'build_8': 'evaluate', 'build_47': 'confidence'},
            {'build_8': 'discuss', 'build_47': 'connection'},
            {'build_8': 'teach', 'build_47': 'participation'},
            {'build_8': 'lead', 'build_47': 'leadership'},
            {'build_47_only': 'legacy'},
        ],
    },
    'mc_integration': {
        'title': 'Mission Control Visitor Journey Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
    },
    'related_blueprints': [
        {'title': 'UX Journey', 'route': '/data/ux-journey.json', 'build': 8},
        {'title': 'Content Production Matrix', 'route': '/data/content-production-matrix.json', 'build': 46},
        {'title': 'Master Curriculum', 'route': '/data/master-curriculum.json', 'build': 35},
        {'title': 'Narrative Architecture', 'route': '/data/narrative-architecture.json', 'build': 34},
    ],
    'summary': {
        'stages_total': len(STAGES),
        'stages_partial': stages_partial,
        'stages_planned': len(STAGES) - stages_partial,
        'stages_with_live_tracking': stages_tracking,
        'journey_map_roles': len(JOURNEY_MAP),
        'decision_points': len(DECISION_POINTS),
        'milestones_defined': len(MILESTONES),
        'milestones_achieved': 0,
        'education_leader_signups': civic.get('education_leader_signups', 0),
        'contact_network_signups': civic.get('contact_network_signups', 0),
        'coalition_orgs': 0,
        'county_participation': 0,
        'journey_analytics_live': False,
        'personalized_recommendations_live': False,
        'server_journey_sync': False,
        'visitor_journey_readiness_pct': visitor_journey_readiness,
    },
    'catalog_gaps': [
        'Only 1/8 stages has live tracking — localStorage only, no server analytics',
        '0 Education Leaders — leadership and legacy stages unreachable in practice',
        '0 contact signups — connection stage broken',
        '0 coalition orgs, 0 county participation — community funnel empty',
        '7 motivation milestones defined — none tracked or celebrated',
        'Personalized recommendations planned — KG not journey-aware',
        'Build #8 7-stage ladder and Build #47 8-stage model coexist — mapping documented',
        '0 videos — documentary decision point leads to empty Media Studio',
        'Lesson/path completion not measured — discovery and understanding stages unverified',
        'Component specifications still deferred — journey UI widgets unmapped',
    ],
    'recommended_next_build': {
        'number': 48,
        'title': 'Component Specifications with Props/States',
        'note': 'Map stage progress bars, milestone badges, decision-point CTAs, and journey funnel viz to COMP-* from Build #17.',
    },
}

path = root / 'data/visitor-journey.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Visitor Journey: {stages_tracking}/8 tracked, {visitor_journey_readiness}% readiness')
