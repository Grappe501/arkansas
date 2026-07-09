"""
Generate data/learning-laboratory.json — Build #38 Interactive Learning Laboratory v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

kg_path = root / 'data/kg-registry.json'
ev_path = root / 'data/evidence-registry.json'

kg = {}
evidence = {}
if kg_path.exists():
    with open(kg_path) as f:
        kg = json.load(f)
if ev_path.exists():
    with open(ev_path) as f:
        evidence = json.load(f)

kg_summary = kg.get('summary', {})

LABORATORIES = [
    {
        'id': 'LAB-01', 'number': 1, 'title': 'Timeline Explorer', 'slug': 'timeline',
        'purpose': 'Move through campaign finance history interactively.',
        'features': ['Scrollable timeline', 'Historical eras', 'Supreme Court decisions', 'Major legislation',
                     'Election cycles', 'Political milestones', 'Arkansas-specific events'],
        'event_opens': ['Historical explanation', 'Related documents', 'Encyclopedia entries', 'Educational lessons', 'Primary sources'],
        'interim_route': '/halls/story-before.html',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 28,
    },
    {
        'id': 'LAB-02', 'number': 2, 'title': 'Money Flow Explorer', 'slug': 'money-flow',
        'purpose': 'Visualize how political spending forms operate.',
        'features': ['Candidates', 'Political parties', 'PACs', 'Super PACs', 'Independent expenditures',
                     'Nonprofit organizations', 'Disclosure systems'],
        'interim_route': '/halls/money-map.html',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 22,
        'note': 'Hall 4 drill-down topics — no interactive flow diagram yet',
    },
    {
        'id': 'LAB-03', 'number': 3, 'title': 'Supreme Court Decision Explorer', 'slug': 'scotus-decision',
        'purpose': 'Examine Citizens United interactively.',
        'features': ['Timeline', 'Legal questions', 'Majority reasoning', 'Dissenting opinions',
                     'Constitutional provisions', 'Related precedents'],
        'interim_route': '/halls/what-court-decided.html',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 32,
    },
    {
        'id': 'LAB-04', 'number': 4, 'title': 'Constitutional Explorer', 'slug': 'constitutional',
        'purpose': 'Interactive map of constitutional concepts.',
        'features': ['First Amendment', 'Political speech', 'Corporate speech', 'Freedom of association',
                     'Judicial review', 'Constitutional precedent'],
        'interim_route': '/halls/debate.html',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 25,
    },
    {
        'id': 'LAB-05', 'number': 5, 'title': 'Campaign Finance Explorer', 'slug': 'campaign-finance',
        'purpose': 'Compare campaign finance structures across historical periods.',
        'features': ['Before 1971', 'After FECA', 'After BCRA', 'After Citizens United', 'Later developments'],
        'interim_route': '/halls/after-2010.html',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 24,
    },
    {
        'id': 'LAB-06', 'number': 6, 'title': 'Arkansas Civic Process Explorer', 'slug': 'arkansas-process',
        'purpose': 'Interactive guide to Arkansas legislative and ballot processes.',
        'features': ['How a bill becomes law', 'Ballot initiatives', 'Legislative committees', 'Public participation'],
        'interim_route': '/solutions/#arkansas',
        'status': 'planned', 'interactive_live': False, 'readiness_pct': 12,
    },
    {
        'id': 'LAB-07', 'number': 7, 'title': 'Source Explorer', 'slug': 'source',
        'purpose': 'Investigate supporting evidence directly.',
        'features': ['Browse by topic', 'Browse by court case', 'Browse by date', 'Browse by document type', 'Browse by source level'],
        'interim_route': '/library/',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 30,
    },
    {
        'id': 'LAB-08', 'number': 8, 'title': 'Debate Explorer', 'slug': 'debate',
        'purpose': 'Compare documented perspectives on important questions.',
        'features': ['Supporting arguments', 'Critical arguments', 'Constitutional reasoning',
                     'Policy considerations', 'Related empirical research'],
        'interim_route': '/halls/debate.html',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 26,
    },
    {
        'id': 'LAB-09', 'number': 9, 'title': 'Knowledge Graph', 'slug': 'knowledge-graph',
        'purpose': 'Visual map of how topics connect.',
        'features': ['Court cases', 'Laws', 'Historical events', 'Constitutional principles',
                     'People', 'Organizations', 'Educational resources'],
        'interim_route': '/mission-control/knowledge-graph.html',
        'status': 'partial', 'interactive_live': False, 'readiness_pct': 35,
        'kg_nodes': kg_summary.get('total_nodes', 0),
        'kg_edges': kg_summary.get('total_edges', 0),
    },
    {
        'id': 'LAB-10', 'number': 10, 'title': 'Community Education Builder', 'slug': 'education-builder',
        'purpose': 'Assemble customized presentation packets for Education Leaders.',
        'features': ['Audience type', 'Lesson length', 'Historical topics', 'Constitutional topics', 'Arkansas topics',
                     'Charts', 'Handouts', 'Discussion questions'],
        'interim_route': '/educate/',
        'status': 'planned', 'interactive_live': False, 'readiness_pct': 10,
    },
]

ACCESSIBILITY_STANDARDS = [
    'Keyboard navigation', 'Descriptive text alternatives', 'Accessible color contrast',
    'Reduced-motion preferences', 'Non-interactive text alternatives',
]

MC_METRICS = [
    {'id': 'LAB-M01', 'title': 'Laboratory usage', 'status': 'planned', 'current': 0},
    {'id': 'LAB-M02', 'title': 'Most explored topics', 'status': 'planned', 'current': 0},
    {'id': 'LAB-M03', 'title': 'Knowledge graph activity', 'status': 'planned', 'current': 0},
    {'id': 'LAB-M04', 'title': 'Timeline interactions', 'status': 'planned', 'current': 0},
    {'id': 'LAB-M05', 'title': 'Source Explorer usage', 'status': 'planned', 'current': 0},
    {'id': 'LAB-M06', 'title': 'Presentation builder usage', 'status': 'planned', 'current': 0},
    {'id': 'LAB-M07', 'title': 'Learning path progression', 'status': 'planned', 'current': 0},
]

FUTURE_EXPANSION = [
    'Interactive constitutional amendment timelines', 'Advanced campaign finance datasets',
    'AI-guided exploration', 'Multimedia exhibits', 'Virtual museum experiences',
    'Additional civic education subjects',
]

labs_partial = sum(1 for l in LABORATORIES if l['status'] == 'partial')
avg_readiness = round(sum(l['readiness_pct'] for l in LABORATORIES) / len(LABORATORIES))
interactive_live = sum(1 for l in LABORATORIES if l['interactive_live'])

learning_lab_readiness = min(
    round(avg_readiness * 0.45 + (labs_partial / 10 * 100) * 0.25 + 15),
    22,
)

out = {
    'version': '1.0',
    'build': 38,
    'updated': today,
    'title': 'Interactive Learning Laboratory v1.0',
    'subtitle': 'Civic Discovery & Simulation System',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/learning-lab.html',
    'canonical_lab_route': '/lab/[laboratory-slug]',
    'current_lab_route': 'Hall pages and MC dashboards — interim static content',
    'constitution': '/docs/INTERACTIVE_LEARNING_LABORATORY.md',
    'purpose': 'Deeper comprehension through interaction — discovery, not entertainment.',
    'learning_philosophy': 'Explore, compare, build, visualize, ask questions, discover patterns.',
    'governing_principle': 'Make difficult ideas understandable through thoughtful interaction and transparent evidence.',
    'laboratories': LABORATORIES,
    'accessibility_standards': ACCESSIBILITY_STANDARDS,
    'mc_integration': {
        'title': 'Mission Control Learning Lab Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'engagement_tracking_live': False,
    },
    'future_expansion': FUTURE_EXPANSION,
    'related_systems': [
        {'title': 'Knowledge Graph', 'route': '/data/kg-registry.json', 'build': 11},
        {'title': 'Narrative Architecture', 'route': '/data/narrative-architecture.json', 'build': 34},
        {'title': 'Master Curriculum', 'route': '/data/master-curriculum.json', 'build': 35},
        {'title': 'Research Library', 'route': '/data/master-research-library.json', 'build': 37},
        {'title': 'Education Academy', 'route': '/mission-control/education-academy.html', 'build': 28},
        {'title': 'UX Journey', 'route': '/data/ux-journey.json', 'build': 8},
    ],
    'summary': {
        'laboratories_total': len(LABORATORIES),
        'laboratories_partial': labs_partial,
        'laboratories_planned': sum(1 for l in LABORATORIES if l['status'] == 'planned'),
        'interactive_experiences_live': interactive_live,
        'avg_lab_readiness_pct': avg_readiness,
        'accessibility_standards': len(ACCESSIBILITY_STANDARDS),
        'mc_metrics': len(MC_METRICS),
        'engagement_tracking_live': False,
        'data_viz_readiness_note': 'Chart definitions only — no interactive labs deployed',
        'learning_lab_readiness_pct': learning_lab_readiness,
    },
    'catalog_gaps': [
        'Canonical /lab/[slug] routes not built — halls used as interim',
        '0/10 laboratories have true interactive experiences',
        'Money Flow Explorer — no interactive visualization (money-map is static)',
        'Timeline Explorer — no scrollable interactive timeline',
        'Knowledge Graph — registry exists, no public interactive node map',
        'Community Education Builder — no packet generator',
        'Arkansas Civic Process Explorer not built',
        'Laboratory usage metrics not tracked — no analytics integration',
        'Accessibility standards defined but not verified per lab',
    ],
    'recommended_next_build': {
        'number': 43,
        'title': 'Component Specifications with Props/States',
        'note': 'Map laboratory shells, interactive widgets, and accessibility patterns to COMP-* from Build #17.',
    },
}

path = root / 'data/learning-laboratory.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Learning Lab: {labs_partial}/10 partial, {learning_lab_readiness}% readiness')
