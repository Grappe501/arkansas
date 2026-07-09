"""
Generate data/education-academy.json — Build #28 Community Education Academy v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

mc_path = root / 'data/mission-control.json'
mc = {}
if mc_path.exists():
    with open(mc_path) as f:
        mc = json.load(f)
civic = mc.get('civic_action', {})

LEARNING_STAGES = [
    {
        'id': 'ACAD-ST-01', 'stage': 1, 'title': 'Learn',
        'focus': 'History, law, and facts',
        'questions': ['What happened?', 'Why did it matter?', 'What changed?'],
        'status': 'partial', 'route': '/start-here/', 'notes': 'Start-here and halls provide interim L1 content',
    },
    {
        'id': 'ACAD-ST-02', 'stage': 2, 'title': 'Understand',
        'focus': 'Distinguish facts, principles, holdings, context, proposals, opinions',
        'distinctions': ['Facts', 'Constitutional principles', 'Court holdings', 'Historical context', 'Policy proposals', 'Personal opinions'],
        'status': 'partial', 'route': '/mission-control/facts.html', 'notes': 'Facts framework defines confidence levels',
    },
    {
        'id': 'ACAD-ST-03', 'stage': 3, 'title': 'Communicate',
        'focus': 'Explain complex ideas clearly',
        'topics': [
            'Explaining difficult legal concepts', 'Answering common questions',
            'Using charts and timelines', 'Guiding discussions respectfully',
            'Working with different viewpoints'
        ],
        'status': 'planned',
    },
    {
        'id': 'ACAD-ST-04', 'stage': 4, 'title': 'Lead',
        'focus': 'Educate others in the community',
        'activities': [
            'Hosting community conversations', 'Giving presentations',
            'Working with coalition organizations', 'Training new Education Leaders',
            'Contributing to educational resources'
        ],
        'status': 'partial', 'route': '/educate/', 'notes': 'Educate signup live; structured lead track not built',
    },
]

MODULE_MATERIALS = [
    'Reading assignments', 'Interactive graphics', 'Historical timelines', 'Source documents',
    'Videos', 'Reflection questions', 'Discussion prompts', 'Printable reference sheets'
]

CURRICULUM = [
    {'id': 'ACAD-M01', 'number': 1, 'title': 'Understanding Citizens United', 'world': 'WORLD-01', 'status': 'partial', 'route': '/start-here/'},
    {'id': 'ACAD-M02', 'number': 2, 'title': 'Campaign Finance History', 'world': 'WORLD-01', 'status': 'partial', 'route': '/halls/story-before.html'},
    {'id': 'ACAD-M03', 'number': 3, 'title': 'The Supreme Court Decision', 'world': 'WORLD-02', 'status': 'partial', 'route': '/halls/the-case.html'},
    {'id': 'ACAD-M04', 'number': 4, 'title': 'Constitutional Principles', 'world': 'WORLD-03', 'status': 'planned', 'route': '/halls/what-court-decided.html'},
    {'id': 'ACAD-M05', 'number': 5, 'title': 'Political Spending After 2010', 'world': 'WORLD-04', 'status': 'partial', 'route': '/halls/after-2010.html'},
    {'id': 'ACAD-M06', 'number': 6, 'title': 'Current Reform Discussions', 'world': 'WORLD-06', 'status': 'partial', 'route': '/solutions/'},
    {
        'id': 'ACAD-M07', 'number': 7, 'title': 'Arkansas Civic Education',
        'topics': ['Arkansas legislative process', 'Ballot initiative process', 'Community education strategies'],
        'world': 'WORLD-06', 'status': 'partial', 'route': '/arkansas/',
    },
    {
        'id': 'ACAD-M08', 'number': 8, 'title': 'Teaching Others',
        'topics': ['Adult learning principles', 'Community conversations', 'Presentation skills', 'Question facilitation', 'Handling disagreement'],
        'world': 'WORLD-07', 'status': 'partial', 'route': '/educate/',
    },
]

CERTIFICATION_COMPETENCIES = [
    'Understanding the material', 'Explaining concepts clearly',
    'Guiding respectful discussion', 'Directing participants to reliable sources'
]

PRESENTATION_TOOLKIT = [
    'Slide presentations', 'Speaker notes', 'Handouts', 'Frequently asked questions',
    'Discussion guides', 'Infographics', 'Historical timelines', 'Resource packets'
]

AUDIENCE_TOOLKITS = [
    {'audience': 'Civic organizations', 'status': 'planned'},
    {'audience': 'Faith communities', 'status': 'planned'},
    {'audience': 'Libraries', 'status': 'planned'},
    {'audience': 'College campuses', 'status': 'planned'},
    {'audience': 'Community colleges', 'status': 'planned'},
    {'audience': 'Neighborhood associations', 'status': 'planned'},
    {'audience': 'Community education events', 'status': 'partial', 'route': '/action/community-conversation.html'},
]

LEADERSHIP_METRICS = [
    {'id': 'ACAD-LM-01', 'title': 'Participants enrolled', 'current': civic.get('education_leader_signups', 0), 'status': 'partial'},
    {'id': 'ACAD-LM-02', 'title': 'Modules completed', 'current': 0, 'status': 'planned'},
    {'id': 'ACAD-LM-03', 'title': 'Resource downloads', 'current': civic.get('toolkit_requests', 0), 'status': 'planned'},
    {'id': 'ACAD-LM-04', 'title': 'Community conversations hosted', 'current': mc.get('relationship_health', {}).get('community_conversations', 0), 'status': 'planned'},
    {'id': 'ACAD-LM-05', 'title': 'Presentations delivered', 'current': 0, 'status': 'planned'},
    {'id': 'ACAD-LM-06', 'title': 'Coalition organizations participating', 'current': mc.get('relationship_health', {}).get('organizations_connected', 0), 'status': 'partial'},
    {'id': 'ACAD-LM-07', 'title': 'Counties with active Education Leaders', 'current': mc.get('relationship_health', {}).get('counties_active', 0), 'status': 'planned'},
]

CONTINUING_EDUCATION = [
    'New court decisions', 'Arkansas legislative developments',
    'New ballot initiative proposals', 'Updated spending data', 'Newly added platform resources'
]

FUTURE_EXPANSION = [
    'Live webinars', 'Regional workshops', 'Guest lectures',
    'Advanced research seminars', 'Specialized legal education modules', 'Topic-specific discussion series'
]

MC_INTEGRATION = [
    {'metric': 'Academy enrollment', 'status': 'partial', 'source': 'Netlify Forms / educate'},
    {'metric': 'Module completion rates', 'status': 'planned'},
    {'metric': 'Learning progress', 'status': 'planned'},
    {'metric': 'Community education activity', 'status': 'planned'},
    {'metric': 'County participation', 'status': 'partial', 'source': 'county-coalition-index'},
    {'metric': 'Toolkit usage', 'status': 'planned'},
    {'metric': 'New Education Leaders', 'status': 'partial', 'source': 'civic_action'},
    {'metric': 'Continuing education participation', 'status': 'planned'},
]

by_module = {}
for m in CURRICULUM:
    by_module[m['status']] = by_module.get(m['status'], 0) + 1

status_weights = {'live': 100, 'partial': 48, 'planned': 10, 'defined': 28}
stage_readiness = round(sum(status_weights.get(s['status'], 5) for s in LEARNING_STAGES) / len(LEARNING_STAGES))
module_readiness = round(sum(status_weights.get(m['status'], 5) for m in CURRICULUM) / len(CURRICULUM))
academy_readiness = min(round(stage_readiness * 0.35 + module_readiness * 0.45 + 8), 24)

out = {
    'version': '1.0',
    'build': 28,
    'updated': today,
    'title': 'Community Education Academy v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/education-academy.html',
    'public_route': '/educate/',
    'constitution': '/docs/COMMUNITY_EDUCATION_ACADEMY.md',
    'purpose': 'Develop Arkansas community educators who explain Citizens United accurately — not an advocacy program.',
    'academy_mission': 'Develop a statewide network of trusted educators using verified facts, primary sources, and respectful dialogue.',
    'governing_principle': 'Success measured by understanding quality and educator confidence — not persuasion.',
    'learning_stages': LEARNING_STAGES,
    'curriculum_modules': CURRICULUM,
    'module_count': len(CURRICULUM),
    'module_materials': MODULE_MATERIALS,
    'certification': {
        'title': 'Community Conversation Certification',
        'competencies': CERTIFICATION_COMPETENCIES,
        'disclaimer': 'Educational program completion — not a professional credential or government certification',
        'status': 'planned',
    },
    'presentation_toolkit': PRESENTATION_TOOLKIT,
    'audience_toolkits': AUDIENCE_TOOLKITS,
    'leadership_metrics': LEADERSHIP_METRICS,
    'continuing_education': CONTINUING_EDUCATION,
    'future_expansion': FUTURE_EXPANSION,
    'mc_integration': MC_INTEGRATION,
    'related_systems': [
        {'title': 'Educate / Signup', 'route': '/educate/', 'build': 3},
        {'title': 'Community Conversation', 'route': '/action/community-conversation.html', 'build': 12},
        {'title': 'Arkansas Civic Ecosystem', 'route': '/mission-control/civic-ecosystem.html', 'build': 12},
        {'title': 'Knowledge Atlas', 'route': '/mission-control/atlas.html', 'build': 19},
        {'title': 'Contact Intelligence', 'route': '/mission-control/contact-intelligence.html', 'build': 24},
    ],
    'summary': {
        'learning_stages': len(LEARNING_STAGES),
        'curriculum_modules': len(CURRICULUM),
        'module_materials_per_module': len(MODULE_MATERIALS),
        'certification_competencies': len(CERTIFICATION_COMPETENCIES),
        'presentation_toolkit_items': len(PRESENTATION_TOOLKIT),
        'audience_toolkits': len(AUDIENCE_TOOLKITS),
        'leadership_metrics': len(LEADERSHIP_METRICS),
        'continuing_education_topics': len(CONTINUING_EDUCATION),
        'future_expansion_items': len(FUTURE_EXPANSION),
        'modules_partial': by_module.get('partial', 0),
        'modules_planned': by_module.get('planned', 0),
        'enrollment_tracking_live': False,
        'module_progress_live': False,
        'academy_readiness_pct': academy_readiness,
    },
    'catalog_gaps': [
        'No structured academy enrollment or module progress tracking',
        '8 modules mapped to interim hall pages — not full curriculum',
        'Module materials (videos, graphics, reflection Qs) not built per module',
        'Community Conversation Certification not operational',
        'Audience-specific toolkits mostly planned',
        'Presentation toolkit partial — educate page scaffold only',
        'Continuing education update system not built',
        'No webinar/workshop infrastructure',
    ],
    'recommended_next_build': {
        'number': 29,
        'title': 'Component Specifications with Props/States',
        'note': 'Map academy modules and toolkit UI to components; wire enrollment to contact intelligence.',
    },
}

path = root / 'data/education-academy.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Education Academy: {len(CURRICULUM)} modules, {academy_readiness}% readiness')
