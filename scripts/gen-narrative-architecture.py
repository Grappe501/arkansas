"""
Generate data/narrative-architecture.json — Build #34 Storytelling & Narrative Architecture v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

mc_path = root / 'data/mission-control.json'
kg_path = root / 'data/kg-registry.json'
facts_path = root / 'data/facts-registry.json'

mc = {}
kg = {}
facts = {}
if mc_path.exists():
    with open(mc_path) as f:
        mc = json.load(f)
if kg_path.exists():
    with open(kg_path) as f:
        kg = json.load(f)
if facts_path.exists():
    with open(facts_path) as f:
        facts = json.load(f)

kg_summary = kg.get('summary', {})
facts_summary = facts.get('summary', {})

MASTER_NARRATIVE = (
    'How did one Supreme Court decision become one of the most influential and debated '
    'rulings in modern American campaign finance law, and what does it mean for citizens today?'
)

ACTS = [
    {
        'id': 'NARR-ACT-01', 'number': 1, 'title': 'Before the Case', 'roman': 'I',
        'question': 'What kind of campaign finance system existed before Citizens United?',
        'topics': ['Early American elections', 'Progressive Era reforms', 'Federal campaign finance laws',
                   'Watergate', 'Federal Election Campaign Act', 'Bipartisan Campaign Reform Act'],
        'reader_outcome': 'Understand that the case emerged from a long legal and political history.',
        'primary_route': '/halls/story-before.html',
        'related_routes': ['/halls/story-before.html', '/library/'],
        'status': 'partial', 'narrative_pct': 38, 'layers_live': ['L1', 'L2'],
    },
    {
        'id': 'NARR-ACT-02', 'number': 2, 'title': 'The Conflict', 'roman': 'II',
        'question': 'How did Citizens United reach the Supreme Court?',
        'topics': ['Citizens United', 'Hillary: The Movie', 'FEC enforcement',
                   'Lower court proceedings', 'Constitutional questions presented'],
        'reader_outcome': 'Understand the facts that gave rise to the litigation.',
        'primary_route': '/halls/the-case.html',
        'related_routes': ['/halls/the-case.html'],
        'status': 'partial', 'narrative_pct': 32, 'layers_live': ['L1', 'L2'],
    },
    {
        'id': 'NARR-ACT-03', 'number': 3, 'title': 'The Decision', 'roman': 'III',
        'question': 'What did the Supreme Court actually decide?',
        'topics': ['Oral arguments', 'Majority opinion', 'Dissenting opinions',
                   'Vote breakdown', 'Constitutional reasoning'],
        'reader_outcome': 'Understand the holding and the reasoning without needing legal training.',
        'primary_route': '/halls/what-court-decided.html',
        'related_routes': ['/halls/what-court-decided.html'],
        'status': 'partial', 'narrative_pct': 42, 'layers_live': ['L1', 'L2', 'L3'],
    },
    {
        'id': 'NARR-ACT-04', 'number': 4, 'title': 'The Immediate Aftermath', 'roman': 'IV',
        'question': 'What happened next?',
        'topics': ['Public reaction', 'Legal consequences', 'Development of Super PACs',
                   'Early election cycles', 'Changes in campaign finance practices'],
        'reader_outcome': 'See how the decision influenced subsequent developments.',
        'primary_route': '/halls/after-2010.html',
        'related_routes': ['/halls/after-2010.html', '/halls/money-map.html'],
        'status': 'partial', 'narrative_pct': 30, 'layers_live': ['L1', 'L2'],
    },
    {
        'id': 'NARR-ACT-05', 'number': 5, 'title': 'The Continuing Debate', 'roman': 'V',
        'question': 'Why do thoughtful people disagree about the decision?',
        'topics': ['Supporting arguments', 'Critical arguments', 'Academic perspectives',
                   'Frequently misunderstood issues'],
        'reader_outcome': 'Recognize the complexity of the debate.',
        'primary_route': '/halls/debate.html',
        'related_routes': ['/halls/debate.html'],
        'status': 'partial', 'narrative_pct': 28, 'layers_live': ['L1', 'L2'],
    },
    {
        'id': 'NARR-ACT-06', 'number': 6, 'title': 'Arkansas Today', 'roman': 'VI',
        'question': 'Why does this matter in Arkansas?',
        'topics': ['Arkansas campaign finance context', 'Arkansas legislative process',
                   'Ballot initiative process', 'Community education opportunities'],
        'reader_outcome': 'Connect national issues to local civic education.',
        'primary_route': '/solutions/#arkansas',
        'related_routes': ['/halls/montana-hawaii.html', '/coalition/', '/coalition/counties.html'],
        'status': 'partial', 'narrative_pct': 22, 'layers_live': ['L1'],
    },
    {
        'id': 'NARR-ACT-07', 'number': 7, 'title': 'Possible Paths Forward', 'roman': 'VII',
        'question': 'What options are available?',
        'topics': ['Congressional proposals', 'Arkansas legislative options', 'Ballot initiative concepts',
                   'Transparency measures', 'Other reform ideas discussed on the platform'],
        'reader_outcome': 'Understand the range of proposals without confusing them with current law.',
        'primary_route': '/solutions/',
        'related_routes': ['/solutions/', '/halls/montana-hawaii.html'],
        'status': 'partial', 'narrative_pct': 25, 'layers_live': ['L1', 'L2'],
    },
    {
        'id': 'NARR-ACT-08', 'number': 8, 'title': 'The Next Chapter', 'roman': 'VIII',
        'question': 'What role can citizens play?',
        'topics': ['Learning', 'Teaching', 'Coalition participation', 'Community conversations',
                   'Education Leader program', 'Research contributions'],
        'reader_outcome': 'See civic education as an ongoing responsibility rather than the end of the story.',
        'primary_route': '/educate/',
        'related_routes': ['/educate/', '/coalition/join.html', '/mission-control/education-academy.html'],
        'status': 'partial', 'narrative_pct': 20, 'layers_live': ['L1'],
    },
]

NARRATIVE_LAYERS = [
    {'id': 'NARR-L1', 'layer': 1, 'title': 'Headline explanation', 'duration': '~1 minute', 'status': 'partial'},
    {'id': 'NARR-L2', 'layer': 2, 'title': 'Short educational story', 'duration': '~5 minutes', 'status': 'partial'},
    {'id': 'NARR-L3', 'layer': 3, 'title': 'Complete narrative', 'duration': '~15–20 minutes', 'status': 'planned'},
    {'id': 'NARR-L4', 'layer': 4, 'title': 'Research archive', 'duration': 'Primary sources & datasets', 'status': 'partial'},
]

STORYTELLING_STANDARDS = [
    'What happened?', 'Who was involved?', 'Why did it happen?', 'What changed?',
    "Why should today's reader care?", 'Where can this be verified?',
]

STORY_COMPONENTS = [
    {'id': 'NARR-SC-01', 'title': 'Historical scene setters', 'status': 'partial'},
    {'id': 'NARR-SC-02', 'title': 'Timeline moments', 'status': 'partial'},
    {'id': 'NARR-SC-03', 'title': 'Courtroom moments', 'status': 'planned'},
    {'id': 'NARR-SC-04', 'title': 'Decision summaries', 'status': 'partial'},
    {'id': 'NARR-SC-05', 'title': 'Data stories', 'status': 'partial'},
    {'id': 'NARR-SC-06', 'title': 'Personal impact examples', 'status': 'planned'},
    {'id': 'NARR-SC-07', 'title': 'Constitutional explainers', 'status': 'partial'},
    {'id': 'NARR-SC-08', 'title': 'Reflection questions', 'status': 'planned'},
]

VISUAL_STORYTELLING = [
    {'id': 'NARR-VS-01', 'title': 'Historical timelines', 'status': 'partial', 'route': '/halls/story-before.html'},
    {'id': 'NARR-VS-02', 'title': 'Courtroom diagrams', 'status': 'planned', 'route': None},
    {'id': 'NARR-VS-03', 'title': 'Money flow graphics', 'status': 'partial', 'route': '/halls/money-map.html'},
    {'id': 'NARR-VS-04', 'title': 'Constitutional relationship maps', 'status': 'planned', 'route': '/mission-control/knowledge-graph.html'},
    {'id': 'NARR-VS-05', 'title': 'Before-and-after comparisons', 'status': 'planned', 'route': None},
    {'id': 'NARR-VS-06', 'title': 'Arkansas legislative process diagrams', 'status': 'planned', 'route': '/solutions/#arkansas'},
]

MC_METRICS = [
    {'id': 'NARR-MC-01', 'title': 'Narrative acts completed', 'status': 'partial'},
    {'id': 'NARR-MC-02', 'title': 'Historical coverage', 'status': 'partial'},
    {'id': 'NARR-MC-03', 'title': 'Story continuity', 'status': 'planned'},
    {'id': 'NARR-MC-04', 'title': 'Visual storytelling completion', 'status': 'planned'},
    {'id': 'NARR-MC-05', 'title': 'Source integration', 'status': 'partial'},
    {'id': 'NARR-MC-06', 'title': 'Reading-level coverage', 'status': 'partial'},
    {'id': 'NARR-MC-07', 'title': 'Community education adaptations', 'status': 'planned'},
]

CONTINUITY_REQUIREMENTS = [
    'What has already been learned',
    'Where the current topic fits within the larger narrative',
    'Which chapters come next',
]

acts_with_pages = sum(1 for a in ACTS if a['primary_route'])
acts_complete = sum(1 for a in ACTS if a['narrative_pct'] >= 80)
avg_act_pct = round(sum(a['narrative_pct'] for a in ACTS) / len(ACTS))
layers_partial = sum(1 for l in NARRATIVE_LAYERS if l['status'] == 'partial')
components_partial = sum(1 for c in STORY_COMPONENTS if c['status'] == 'partial')
visual_partial = sum(1 for v in VISUAL_STORYTELLING if v['status'] == 'partial')

narrative_completion = {
    'acts_total': len(ACTS),
    'acts_with_primary_page': acts_with_pages,
    'acts_narratively_complete': acts_complete,
    'avg_act_narrative_pct': avg_act_pct,
    'layers_defined': len(NARRATIVE_LAYERS),
    'layers_partial': layers_partial,
    'story_components_partial': components_partial,
    'visual_elements_partial': visual_partial,
    'visual_elements_planned': sum(1 for v in VISUAL_STORYTELLING if v['status'] == 'planned'),
    'continuity_live': False,
    'act_navigation_live': False,
    'facts_linked': facts_summary.get('total', 0),
    'kg_nodes_linked': kg_summary.get('total_nodes', 0),
}

structure_score = 28
narrative_readiness = min(
    round(avg_act_pct * 0.45 + structure_score * 0.3 + (layers_partial / 4 * 100) * 0.15 + (visual_partial / 6 * 100) * 0.1),
    24,
)

out = {
    'version': '1.0',
    'build': 34,
    'updated': today,
    'title': 'Storytelling & Narrative Architecture v1.0',
    'subtitle': 'Educational Narrative System',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/narrative.html',
    'canonical_act_route': '/story/act-[n]/[slug]',
    'current_act_route': 'Hall pages and solutions — act mapping in registry',
    'constitution': '/docs/NARRATIVE_ARCHITECTURE.md',
    'purpose': 'Teach through narrative — documentary museum, not isolated encyclopedia pages.',
    'master_narrative': MASTER_NARRATIVE,
    'governing_principle': 'Guide readers through a coherent story from history through consequences to civic participation.',
    'acts': ACTS,
    'narrative_layers': NARRATIVE_LAYERS,
    'storytelling_standards': STORYTELLING_STANDARDS,
    'story_components': STORY_COMPONENTS,
    'visual_storytelling': VISUAL_STORYTELLING,
    'narrative_continuity': {
        'title': 'Narrative Continuity',
        'status': 'planned',
        'requirements': CONTINUITY_REQUIREMENTS,
        'related': '/data/ux-journey.json',
    },
    'mc_integration': MC_METRICS,
    'educational_integrity': {
        'title': 'Educational Integrity',
        'principle': 'Stories anchored to documented evidence — uncertainty explained openly.',
        'status': 'partial',
    },
    'related_systems': [
        {'title': 'UX Journey Blueprint', 'route': '/data/ux-journey.json', 'build': 8},
        {'title': 'Encyclopedia & Knowledge Library', 'route': '/data/encyclopedia-knowledge-library.json', 'build': 33},
        {'title': 'Knowledge Graph', 'route': '/data/kg-registry.json', 'build': 11},
        {'title': 'Facts Registry', 'route': '/data/facts-registry.json', 'build': 18},
        {'title': 'Content Production Factory', 'route': '/mission-control/content-factory.html', 'build': 27},
        {'title': 'Wireframe Blueprint', 'route': '/mission-control/wireframes.html', 'build': 23},
    ],
    'narrative_completion': narrative_completion,
    'summary': {
        'acts_total': len(ACTS),
        'narrative_layers': len(NARRATIVE_LAYERS),
        'story_components': len(STORY_COMPONENTS),
        'visual_elements': len(VISUAL_STORYTELLING),
        'storytelling_standards': len(STORYTELLING_STANDARDS),
        'mc_metrics': len(MC_METRICS),
        'avg_act_narrative_pct': avg_act_pct,
        'acts_with_primary_page': acts_with_pages,
        'continuity_live': False,
        'act_navigation_live': False,
        'layer_four_archive_live': False,
        'narrative_readiness_pct': narrative_readiness,
    },
    'catalog_gaps': [
        'Canonical /story/act-[n]/[slug] routes not built — halls used as interim acts',
        'Act-aware continuity (prior learning, next chapter) not on all pages',
        'Layer 3 complete narratives (~15–20 min) not written for most acts',
        'Layer 4 research archives not unified per act',
        'Acts VI and VIII weakest — Arkansas and civic participation thin',
        '4/6 visual storytelling elements planned only',
        'Courtroom moments and personal impact story components not built',
        'Narrative completion not tracked live in page templates',
    ],
    'recommended_next_build': {
        'number': 35,
        'title': 'Component Specifications with Props/States',
        'note': 'Map narrative acts, layers, and story components to COMP-* from Build #17.',
    },
}

path = root / 'data/narrative-architecture.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Narrative: {acts_with_pages}/{len(ACTS)} acts mapped, {narrative_readiness}% readiness')
