"""
Generate data/knowledge-atlas.json — Build #19 Knowledge Atlas & Learning Path System v1.0.
Maps seven learning worlds to honest page/route status.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

STATUS_WEIGHT = {'live': 1.0, 'partial': 0.45, 'stub': 0.15, 'planned': 0.0, 'redirect': 0.35}


def district(did, title, status, routes=None, pages=None, note=None):
    routes = routes or []
    pages = pages or []
    return {
        'id': did,
        'title': title,
        'status': status,
        'completion_pct': int(STATUS_WEIGHT.get(status, 0) * 100),
        'routes': routes,
        'pages': pages,
        'note': note
    }


def world(wid, number, title, purpose, districts):
    live = sum(1 for d in districts if d['status'] == 'live')
    partial = sum(1 for d in districts if d['status'] in ('partial', 'redirect'))
    planned = sum(1 for d in districts if d['status'] in ('planned', 'stub'))
    avg = round(sum(d['completion_pct'] for d in districts) / max(len(districts), 1))
    return {
        'id': wid,
        'number': number,
        'title': title,
        'purpose': purpose,
        'district_count': len(districts),
        'districts_live': live,
        'districts_partial': partial,
        'districts_planned': planned,
        'completion_pct': avg,
        'districts': districts
    }


worlds = [
    world('WORLD-01', 1, 'The World Before Citizens United',
          'Help visitors understand the decades of history leading to the case.',
          [
              district('W1-D01', 'Early Campaign Finance', 'planned', note='Pre-20th century regulation — content not yet written'),
              district('W1-D02', 'Progressive Era', 'planned'),
              district('W1-D03', 'Watergate', 'planned'),
              district('W1-D04', 'Reform Movement', 'partial', ['/halls/story-before.html'], ['HIST overview in story-before hall']),
              district('W1-D05', 'Supreme Court History', 'partial', ['/halls/story-before.html'], ['Buckley and precedent references']),
              district('W1-D06', 'McCain-Feingold', 'partial', ['/halls/story-before.html'], ['BCRA context in story-before']),
              district('W1-D07', 'The Political Climate Before 2010', 'partial', ['/halls/story-before.html', '/start-here/'], ['Orientation + story-before L1']),
          ]),
    world('WORLD-02', 2, 'Inside the Case',
          'Allow visitors to experience the case from beginning to end.',
          [
              district('W2-D01', 'The Movie', 'partial', ['/halls/the-case.html'], ['Hillary: The Movie context']),
              district('W2-D02', 'Citizens United', 'partial', ['/halls/the-case.html']),
              district('W2-D03', 'The Federal Election Commission', 'partial', ['/halls/the-case.html']),
              district('W2-D04', 'Lower Courts', 'planned'),
              district('W2-D05', 'Supreme Court', 'partial', ['/halls/what-court-decided.html']),
              district('W2-D06', 'Oral Arguments', 'planned', note='Transcripts not yet in Evidence Registry'),
              district('W2-D07', 'Majority Opinion', 'partial', ['/halls/what-court-decided.html'], ['L1–L2 holding summary']),
              district('W2-D08', 'Dissents', 'partial', ['/halls/what-court-decided.html', '/halls/debate.html']),
              district('W2-D09', 'Immediate Reactions', 'partial', ['/halls/after-2010.html']),
          ]),
    world('WORLD-03', 3, 'Constitutional Foundations',
          'Teach constitutional concepts without assuming legal training.',
          [
              district('W3-D01', 'First Amendment', 'partial', ['/halls/what-court-decided.html', '/halls/debate.html']),
              district('W3-D02', 'Political Speech', 'partial', ['/halls/debate.html']),
              district('W3-D03', 'Corporate Speech', 'partial', ['/halls/debate.html', '/halls/what-court-decided.html']),
              district('W3-D04', 'Associations', 'planned'),
              district('W3-D05', 'Judicial Review', 'planned'),
              district('W3-D06', 'Constitutional Interpretation', 'partial', ['/halls/debate.html']),
              district('W3-D07', 'Important Precedents', 'partial', ['/halls/story-before.html'], ['KG-CASE-000001 Buckley referenced']),
          ]),
    world('WORLD-04', 4, 'What Changed?',
          'Document measurable consequences after 2010.',
          [
              district('W4-D01', 'Campaign Spending', 'partial', ['/halls/money-map.html', '/halls/after-2010.html']),
              district('W4-D02', 'Independent Expenditures', 'partial', ['/halls/money-map.html']),
              district('W4-D03', 'Super PACs', 'partial', ['/halls/after-2010.html']),
              district('W4-D04', 'Disclosure', 'planned'),
              district('W4-D05', 'Election Trends', 'planned', note='FEC datasets not yet integrated'),
              district('W4-D06', 'State Impacts', 'partial', ['/halls/montana-hawaii.html']),
              district('W4-D07', 'Public Debate', 'partial', ['/halls/debate.html', '/halls/after-2010.html']),
          ]),
    world('WORLD-05', 5, 'The National Conversation',
          'Present the strongest ideas from across the public debate.',
          [
              district('W5-D01', 'Arguments Supporting the Decision', 'partial', ['/halls/debate.html']),
              district('W5-D02', 'Arguments Criticizing the Decision', 'partial', ['/halls/debate.html']),
              district('W5-D03', 'Constitutional Perspectives', 'partial', ['/halls/debate.html']),
              district('W5-D04', 'Public Policy Perspectives', 'partial', ['/halls/debate.html', '/solutions/']),
              district('W5-D05', 'Academic Perspectives', 'planned'),
              district('W5-D06', 'Frequently Misunderstood Issues', 'planned', note='FAQ route planned in Route Registry'),
          ]),
    world('WORLD-06', 6, 'Arkansas Solutions Center',
          'Connect national understanding with Arkansas civic education.',
          [
              district('W6-D01', 'Federal Legislative Options', 'partial', ['/solutions/', '/halls/reform.html']),
              district('W6-D02', 'Arkansas Legislative Options', 'planned', ['/arkansas/']),
              district('W6-D03', 'Educational Policy Concepts', 'planned'),
              district('W6-D04', 'Model Law Workspace', 'stub', ['/solutions/'], note='Stub — workspace not built'),
              district('W6-D05', 'Ballot Initiative Lab', 'stub', ['/solutions/'], note='Stub — lab not built'),
              district('W6-D06', 'Community Education', 'live', ['/educate/', '/start-here/']),
              district('W6-D07', 'Coalition Building', 'live', ['/coalition/', '/join/']),
          ]),
    world('WORLD-07', 7, 'Arkansas Education Network',
          'Grow a statewide civic education movement.',
          [
              district('W7-D01', 'Become an Education Leader', 'live', ['/educate/']),
              district('W7-D02', 'Join the Contact Network', 'live', ['/educate/', '/action/']),
              district('W7-D03', 'Coalition Partners', 'partial', ['/coalition/', '/coalition/join.html']),
              district('W7-D04', 'County Education Teams', 'partial', ['/coalition/counties.html', '/coalition/county.html'], ['75 county scaffold pages']),
              district('W7-D05', 'Community Conversations', 'live', ['/educate/', '/action/']),
              district('W7-D06', 'Educational Events', 'stub', ['/coalition/events.html']),
              district('W7-D07', 'Resource Library', 'partial', ['/coalition/resources.html', '/library/']),
              district('W7-D08', 'Mission Control', 'live', ['/mission-control/']),
          ]),
]

trails = [
    {
        'id': 'TRAIL-BEGINNER',
        'title': 'The Beginner Trail',
        'duration': '20–30 minutes',
        'audience': 'First-time visitors',
        'stops': [
            {'order': 1, 'title': 'Start Here', 'route': '/start-here/', 'world': 'WORLD-01'},
            {'order': 2, 'title': 'What Is Citizens United?', 'route': '/explore/', 'world': 'WORLD-02'},
            {'order': 3, 'title': 'The Story Before', 'route': '/halls/story-before.html', 'world': 'WORLD-01'},
            {'order': 4, 'title': 'The Case', 'route': '/halls/the-case.html', 'world': 'WORLD-02'},
            {'order': 5, 'title': 'What the Court Decided', 'route': '/halls/what-court-decided.html', 'world': 'WORLD-02'},
            {'order': 6, 'title': 'Why It Still Matters', 'route': '/halls/after-2010.html', 'world': 'WORLD-04'},
        ]
    },
    {
        'id': 'TRAIL-HISTORY',
        'title': 'The History Trail',
        'focus': 'Campaign finance history before 2010',
        'stops': [
            {'order': 1, 'route': '/halls/story-before.html', 'world': 'WORLD-01'},
            {'order': 2, 'route': '/library/', 'world': 'WORLD-01'},
            {'order': 3, 'route': '/mission-control/knowledge-graph.html', 'world': 'WORLD-01', 'note': 'KG history cluster'},
        ]
    },
    {
        'id': 'TRAIL-LEGAL',
        'title': 'The Legal Trail',
        'focus': 'Supreme Court doctrine and constitutional reasoning',
        'stops': [
            {'order': 1, 'route': '/halls/the-case.html', 'world': 'WORLD-02'},
            {'order': 2, 'route': '/halls/what-court-decided.html', 'world': 'WORLD-02'},
            {'order': 3, 'route': '/halls/debate.html', 'world': 'WORLD-03'},
            {'order': 4, 'route': '/mission-control/facts.html', 'world': 'WORLD-03', 'note': 'FACT-1000 series'},
        ]
    },
    {
        'id': 'TRAIL-DATA',
        'title': 'The Data Trail',
        'focus': 'Political spending and measurable impacts',
        'stops': [
            {'order': 1, 'route': '/halls/after-2010.html', 'world': 'WORLD-04'},
            {'order': 2, 'route': '/halls/money-map.html', 'world': 'WORLD-04'},
            {'order': 3, 'route': '/mission-control/facts.html', 'world': 'WORLD-04', 'note': 'FACT-4000 series'},
        ]
    },
    {
        'id': 'TRAIL-ARKANSAS',
        'title': 'The Arkansas Trail',
        'focus': 'Education, coalition building, and state civic engagement',
        'stops': [
            {'order': 1, 'route': '/arkansas/', 'world': 'WORLD-06'},
            {'order': 2, 'route': '/educate/', 'world': 'WORLD-07'},
            {'order': 3, 'route': '/coalition/', 'world': 'WORLD-07'},
            {'order': 4, 'route': '/join/', 'world': 'WORLD-06'},
            {'order': 5, 'route': '/coalition/counties.html', 'world': 'WORLD-07'},
        ]
    },
    {
        'id': 'TRAIL-RESEARCH',
        'title': 'The Research Trail',
        'focus': 'Primary sources, datasets, and academic materials',
        'stops': [
            {'order': 1, 'route': '/library/', 'world': 'WORLD-01'},
            {'order': 2, 'route': '/mission-control/research.html', 'world': 'WORLD-02'},
            {'order': 3, 'route': '/mission-control/facts.html', 'world': 'WORLD-02'},
            {'order': 4, 'route': '/mission-control/knowledge-graph.html', 'world': 'WORLD-03'},
        ]
    },
]

all_districts = [d for w in worlds for d in w['districts']]
unique_routes = sorted({r for d in all_districts for r in d['routes']})

def world_completion(wid):
    w = next(x for x in worlds if x['id'] == wid)
    return w['completion_pct']

educational_completion = {
    'historical_coverage': world_completion('WORLD-01'),
    'case_coverage': world_completion('WORLD-02'),
    'constitutional_coverage': world_completion('WORLD-03'),
    'impact_coverage': world_completion('WORLD-04'),
    'debate_coverage': world_completion('WORLD-05'),
    'solutions_coverage': world_completion('WORLD-06'),
    'arkansas_content': round((world_completion('WORLD-06') + world_completion('WORLD-07')) / 2),
    'coalition_resources': world_completion('WORLD-07'),
    'research_completeness': 18,
    'overall_educational_readiness': 0
}
dims = [v for k, v in educational_completion.items() if k != 'overall_educational_readiness' and k != 'research_completeness']
educational_completion['overall_educational_readiness'] = round(sum(dims) / len(dims))

summary = {
    'worlds': len(worlds),
    'districts': len(all_districts),
    'districts_live': sum(1 for d in all_districts if d['status'] == 'live'),
    'districts_partial': sum(1 for d in all_districts if d['status'] in ('partial', 'redirect')),
    'districts_stub': sum(1 for d in all_districts if d['status'] == 'stub'),
    'districts_planned': sum(1 for d in all_districts if d['status'] == 'planned'),
    'mapped_routes': len(unique_routes),
    'trails': len(trails),
    'atlas_completion_pct': educational_completion['overall_educational_readiness'],
    'pages_lit': sum(1 for d in all_districts if d['status'] == 'live'),
    'pages_partial': sum(1 for d in all_districts if d['status'] == 'partial'),
    'v1_target_districts': 49,
    'v1_target_pages': 825,
}

atlas = {
    'version': '1.0',
    'build': 19,
    'updated': today,
    'title': 'Citizens United Knowledge Atlas & Learning Path System v1.0',
    'organization': 'Arkansas Civic Education Initiative',
    'platform': 'The Citizens United Education Platform',
    'route': '/mission-control/atlas.html',
    'constitution': '/docs/KNOWLEDGE_ATLAS.md',
    'facts_framework': '/data/facts-framework.json',
    'knowledge_graph': '/data/kg-registry.json',
    'route_registry': '/data/route-registry.json',
    'ux_journey': '/data/ux-journey.json',
    'core_question': 'How did one Supreme Court decision reshape the conversation about money and politics in America?',
    'principle': 'The platform should feel like exploring a living knowledge atlas — not a website with menus.',
    'governing_principle': 'Every path leads to greater understanding; every topic connects; every visitor can become an informed educator in their Arkansas community.',
    'learning_compass': {
        'component_id': 'COMP-NAV-004',
        'fields': [
            {'id': 'current_world', 'label': 'Current World'},
            {'id': 'current_district', 'label': 'Current District'},
            {'id': 'reading_time', 'label': 'Estimated Reading Time'},
            {'id': 'learning_level', 'label': 'Learning Level', 'values': ['L1', 'L2', 'L3', 'L4']},
            {'id': 'evidence_strength', 'label': 'Evidence Strength', 'source': 'facts-registry'},
            {'id': 'related_topics', 'label': 'Related Topics', 'source': 'kg-registry'},
            {'id': 'next_destination', 'label': 'Next Recommended Destination'},
        ],
        'status': 'partial',
        'note': 'Schema defined; UI not yet on all pages'
    },
    'checkpoints': [
        {'id': 'takeaways', 'title': 'Key Takeaways'},
        {'id': 'misconceptions', 'title': 'Common Misconceptions'},
        {'id': 'faq', 'title': 'Frequently Asked Questions'},
        {'id': 'reflection', 'title': 'Reflection Questions'},
        {'id': 'resources', 'title': 'Related Resources'},
    ],
    'atlas_map_hierarchy': [
        {'level': 1, 'title': 'Seven Learning Worlds', 'count': 7},
        {'level': 2, 'title': 'Major Districts', 'count': summary['districts']},
        {'level': 3, 'title': 'Individual Pages', 'count': summary['mapped_routes'], 'v1_target': summary['v1_target_pages']},
        {'level': 4, 'title': 'Primary Sources', 'source': 'evidence-registry'},
        {'level': 5, 'title': 'Educational Resources', 'source': 'content-inventory'},
        {'level': 6, 'title': 'Community Action Opportunities', 'source': 'civic-ecosystem'},
    ],
    'worlds': worlds,
    'trails': trails,
    'educational_completion': educational_completion,
    'summary': summary,
    'integrations': [
        {'system': 'Facts Framework', 'build': 18, 'route': '/mission-control/facts.html'},
        {'system': 'Knowledge Graph', 'build': 11, 'route': '/mission-control/knowledge-graph.html'},
        {'system': 'Route Registry', 'build': 16, 'route': '/mission-control/routes.html'},
        {'system': 'UX Journey', 'build': 8, 'route': '/mission-control/journey.html'},
        {'system': 'Component Registry', 'build': 17, 'route': '/mission-control/components.html'},
    ],
    'recommended_next_build': {
        'number': 20,
        'title': 'Brand & Identity System',
        'note': 'Logo, color, typography, voice, messaging — before mass district content.'
    },
    'catalog_gaps': [
        'Learning Compass UI not deployed on public pages',
        '34 districts still planned or stub',
        'Academic Perspectives district (W5-D05) unwritten',
        'FEC data districts (W4-D04, W4-D05) need datasets',
        'Oral Arguments district needs transcript EV-IDs',
        'Interactive atlas map visualization planned',
    ],
}

out = root / 'data/knowledge-atlas.json'
with open(out, 'w', newline='\n') as f:
    json.dump(atlas, f, indent=2)
    f.write('\n')
print(f'Atlas: {summary["worlds"]} worlds, {summary["districts"]} districts, {summary["atlas_completion_pct"]}% readiness')
