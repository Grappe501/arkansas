"""
Generate data/master-curriculum.json — Build #35 Master Curriculum & Learning Standards v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

mc_path = root / 'data/mission-control.json'
academy_path = root / 'data/education-academy.json'
narr_path = root / 'data/narrative-architecture.json'

mc = {}
academy = {}
narr = {}
if mc_path.exists():
    with open(mc_path) as f:
        mc = json.load(f)
if academy_path.exists():
    with open(academy_path) as f:
        academy = json.load(f)
if narr_path.exists():
    with open(narr_path) as f:
        narr = json.load(f)

civic = mc.get('civic_action', {})
education_leaders = civic.get('education_leader_signups', 0)

TIERS = [
    {
        'id': 'CURR-T01', 'tier': 1, 'title': 'Foundations',
        'learning_goal': 'Understand the basic facts.',
        'core_lessons': ['What is Citizens United?', 'Why is it important?', 'Key vocabulary', 'Basic campaign finance concepts'],
        'estimated_time': '30–45 minutes',
        'completion_outcome': 'Participants can accurately explain the basic facts to another person.',
        'primary_route': '/start-here/',
        'related_routes': ['/start-here/', '/'],
        'status': 'partial', 'completion_pct': 35, 'lessons_live': 2, 'lessons_total': 4,
    },
    {
        'id': 'CURR-T02', 'tier': 2, 'title': 'Historical Development',
        'learning_goal': 'Understand how campaign finance law evolved.',
        'core_lessons': ['Early campaign finance history', 'Progressive Era reforms', 'Watergate',
                        'Federal Election Campaign Act', 'Bipartisan Campaign Reform Act', 'Events leading to the lawsuit'],
        'estimated_time': '2–3 hours',
        'completion_outcome': 'Participants understand that Citizens United developed within a broader historical context.',
        'primary_route': '/halls/story-before.html',
        'related_routes': ['/halls/story-before.html', '/halls/the-case.html'],
        'status': 'partial', 'completion_pct': 32, 'lessons_live': 3, 'lessons_total': 6,
    },
    {
        'id': 'CURR-T03', 'tier': 3, 'title': 'Constitutional & Legal Analysis',
        'learning_goal': 'Understand the legal reasoning.',
        'core_lessons': ['First Amendment', 'Political speech', 'Corporate speech', 'Judicial review',
                        'Supreme Court precedent', 'Majority opinion', 'Dissenting opinions'],
        'estimated_time': '4–6 hours',
        'completion_outcome': "Participants can explain the Court's reasoning and the principal legal arguments.",
        'primary_route': '/halls/what-court-decided.html',
        'related_routes': ['/halls/what-court-decided.html', '/halls/the-case.html'],
        'status': 'partial', 'completion_pct': 38, 'lessons_live': 4, 'lessons_total': 7,
    },
    {
        'id': 'CURR-T04', 'tier': 4, 'title': 'Impact & Data',
        'learning_goal': 'Understand what changed after the decision.',
        'core_lessons': ['Campaign spending', 'Independent expenditures', 'Super PACs', 'Disclosure',
                        'Election trends', 'Empirical research'],
        'estimated_time': '3–5 hours',
        'completion_outcome': 'Participants can interpret data trends and distinguish documented changes from debates.',
        'primary_route': '/halls/after-2010.html',
        'related_routes': ['/halls/after-2010.html', '/halls/money-map.html'],
        'status': 'partial', 'completion_pct': 28, 'lessons_live': 3, 'lessons_total': 6,
    },
    {
        'id': 'CURR-T05', 'tier': 5, 'title': 'Public Discussion',
        'learning_goal': 'Understand the range of viewpoints.',
        'core_lessons': ['Arguments supporting the decision', 'Arguments criticizing the decision',
                        'Academic perspectives', 'Frequently misunderstood claims', 'Media narratives'],
        'estimated_time': '3–4 hours',
        'completion_outcome': 'Participants can summarize multiple perspectives fairly.',
        'primary_route': '/halls/debate.html',
        'related_routes': ['/halls/debate.html'],
        'status': 'partial', 'completion_pct': 26, 'lessons_live': 2, 'lessons_total': 5,
    },
    {
        'id': 'CURR-T06', 'tier': 6, 'title': 'Arkansas Civic Education',
        'learning_goal': 'Apply knowledge within Arkansas.',
        'core_lessons': ['Arkansas legislative process', 'Arkansas ballot initiative process',
                        'Community conversations', 'Education Leader program', 'Coalition participation',
                        'Community resource development'],
        'estimated_time': '2–3 hours',
        'completion_outcome': 'Participants are prepared to help educate others using platform resources.',
        'primary_route': '/educate/',
        'related_routes': ['/educate/', '/coalition/', '/solutions/#arkansas'],
        'status': 'partial', 'completion_pct': 22, 'lessons_live': 2, 'lessons_total': 6,
    },
]

LEARNING_PATHS = [
    {'id': 'CURR-LP-01', 'title': 'Quick Understanding', 'duration': '~1 hour', 'audience': 'First-time visitors',
     'tiers': [1], 'status': 'partial', 'route': '/start-here/'},
    {'id': 'CURR-LP-02', 'title': 'Community Educator', 'duration': 'Complete curriculum', 'audience': 'Education Leaders',
     'tiers': [1, 2, 3, 4, 5, 6], 'status': 'partial', 'route': '/educate/'},
    {'id': 'CURR-LP-03', 'title': 'Journalist & Researcher', 'duration': 'Variable', 'audience': 'Journalists, researchers',
     'tiers': [2, 3, 4], 'focus': ['Primary sources', 'Timelines', 'Data'], 'status': 'partial', 'route': '/library/'},
    {'id': 'CURR-LP-04', 'title': 'Student', 'duration': 'Balanced', 'audience': 'Students',
     'tiers': [1, 2, 3, 5], 'focus': ['History', 'Law', 'Constitutional principles'], 'status': 'partial', 'route': '/start-here/'},
    {'id': 'CURR-LP-05', 'title': 'Coalition Partner', 'duration': 'Variable', 'audience': 'Coalition organizations',
     'tiers': [1, 5, 6], 'focus': ['Educational resources', 'Presentations', 'Community engagement'], 'status': 'partial', 'route': '/coalition/'},
    {'id': 'CURR-LP-06', 'title': 'Public Official Resource Path', 'duration': 'Variable', 'audience': 'Legislators and staff',
     'tiers': [2, 3, 4, 5], 'focus': ['Historical background', 'Constitutional framework', 'Current legal landscape',
               'Educational resource packets', 'Research summaries'], 'status': 'planned', 'route': '/solutions/'},
]

READING_LEVELS = [
    {'id': 'CURR-RL-01', 'level': 1, 'title': 'Introductory', 'status': 'partial'},
    {'id': 'CURR-RL-02', 'level': 2, 'title': 'General public', 'status': 'partial'},
    {'id': 'CURR-RL-03', 'level': 3, 'title': 'Advanced', 'status': 'planned'},
    {'id': 'CURR-RL-04', 'level': 4, 'title': 'Research archive', 'status': 'partial'},
]

ASSESSMENTS = [
    {'id': 'CURR-AS-01', 'title': 'Knowledge checks', 'status': 'planned'},
    {'id': 'CURR-AS-02', 'title': 'Timeline sequencing', 'status': 'planned'},
    {'id': 'CURR-AS-03', 'title': 'Vocabulary review', 'status': 'planned'},
    {'id': 'CURR-AS-04', 'title': 'Reflection questions', 'status': 'partial'},
    {'id': 'CURR-AS-05', 'title': 'Source identification exercises', 'status': 'planned'},
]

EDUCATIONAL_OUTCOMES = [
    {'id': 'CURR-EO-01', 'title': 'Curriculum enrollment', 'status': 'planned', 'current': 0},
    {'id': 'CURR-EO-02', 'title': 'Lesson completion', 'status': 'planned', 'current': 0},
    {'id': 'CURR-EO-03', 'title': 'Learning path completion', 'status': 'planned', 'current': 0},
    {'id': 'CURR-EO-04', 'title': 'Resource downloads', 'status': 'planned', 'current': 0},
    {'id': 'CURR-EO-05', 'title': 'Community Educator participation', 'status': 'partial', 'current': education_leaders},
    {'id': 'CURR-EO-06', 'title': 'Coalition participation', 'status': 'partial', 'current': 0},
    {'id': 'CURR-EO-07', 'title': 'Continuing education activity', 'status': 'planned', 'current': 0},
]

MAINTENANCE_TRIGGERS = [
    'Supreme Court decisions', 'Federal legislation', 'Arkansas legislation',
    'Ballot initiative developments', 'New research', 'Updated datasets',
]

INTEGRATION = [
    {'title': 'Encyclopedia', 'route': '/mission-control/encyclopedia.html', 'build': 33, 'status': 'partial'},
    {'title': 'Source Library', 'route': '/library/', 'build': 10, 'status': 'partial'},
    {'title': 'Community Education Academy', 'route': '/mission-control/education-academy.html', 'build': 28, 'status': 'partial'},
    {'title': 'Coalition resources', 'route': '/coalition/resources.html', 'build': 14, 'status': 'partial'},
    {'title': 'Mission Control', 'route': '/mission-control/', 'build': 25, 'status': 'live'},
    {'title': 'Community conversations', 'route': '/action/community-conversation.html', 'build': 13, 'status': 'partial'},
    {'title': 'Research Observatory', 'route': '/mission-control/research-observatory.html', 'build': 29, 'status': 'partial'},
    {'title': 'Solutions Center', 'route': '/solutions/', 'build': 9, 'status': 'partial'},
    {'title': 'Narrative Architecture', 'route': '/mission-control/narrative.html', 'build': 34, 'status': 'partial'},
]

LONG_TERM_VISION = [
    'Independent learners', 'Community organizations', 'Libraries', 'Colleges',
    'Journalists', 'Public officials', 'Education Leaders',
]

avg_tier_pct = round(sum(t['completion_pct'] for t in TIERS) / len(TIERS))
lessons_live = sum(t['lessons_live'] for t in TIERS)
lessons_total = sum(t['lessons_total'] for t in TIERS)
paths_partial = sum(1 for p in LEARNING_PATHS if p['status'] == 'partial')
academy_modules = academy.get('module_count', 8)

curriculum_completion = {
    'tiers_total': len(TIERS),
    'tiers_with_primary_route': len(TIERS),
    'avg_tier_completion_pct': avg_tier_pct,
    'lessons_live': lessons_live,
    'lessons_total': lessons_total,
    'lesson_coverage_pct': round(lessons_live / lessons_total * 100),
    'learning_paths': len(LEARNING_PATHS),
    'learning_paths_partial': paths_partial,
    'reading_levels_partial': sum(1 for r in READING_LEVELS if r['status'] == 'partial'),
    'assessments_live': sum(1 for a in ASSESSMENTS if a['status'] != 'planned'),
    'enrollment_tracking_live': False,
    'path_progress_live': False,
    'academy_modules_aligned': academy_modules,
}

structure_score = 30
curriculum_readiness = min(
    round(avg_tier_pct * 0.4 + structure_score * 0.35 + (lessons_live / lessons_total * 100) * 0.15 + (paths_partial / 6 * 100) * 0.1),
    26,
)

out = {
    'version': '1.0',
    'build': 35,
    'updated': today,
    'title': 'Master Curriculum & Learning Standards v1.0',
    'subtitle': 'Educational Framework',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/curriculum.html',
    'canonical_lesson_route': '/learn/tier-[n]/[lesson-slug]',
    'current_lesson_route': 'Halls, start-here, educate — tier mapping in registry',
    'constitution': '/docs/MASTER_CURRICULUM.md',
    'purpose': 'Complete educational curriculum — success measured by knowledge gained, not pages read.',
    'educational_philosophy': 'Understanding comes before opinion.',
    'governing_principle': 'Equip Arkansans with historical knowledge, constitutional understanding, and research skills.',
    'tiers': TIERS,
    'learning_paths': LEARNING_PATHS,
    'reading_levels': READING_LEVELS,
    'assessments': ASSESSMENTS,
    'educational_outcomes': EDUCATIONAL_OUTCOMES,
    'curriculum_maintenance': {
        'title': 'Curriculum Maintenance',
        'status': 'partial',
        'triggers': MAINTENANCE_TRIGGERS,
        'review_schedule_live': False,
    },
    'curriculum_integration': INTEGRATION,
    'long_term_vision': LONG_TERM_VISION,
    'academy_alignment': {
        'registry': '/data/education-academy.json',
        'modules': academy_modules,
        'stages': len(academy.get('learning_stages', [])),
        'note': 'Academy 4 stages map to curriculum tiers 1–6 and learning paths.',
    },
    'narrative_alignment': {
        'registry': '/data/narrative-architecture.json',
        'acts': narr.get('summary', {}).get('acts_total', 8),
        'note': 'Narrative acts I–VI align to tiers 2–6; Tier 1 precedes Act I.',
    },
    'curriculum_completion': curriculum_completion,
    'summary': {
        'tiers_total': len(TIERS),
        'learning_paths': len(LEARNING_PATHS),
        'reading_levels': len(READING_LEVELS),
        'assessments': len(ASSESSMENTS),
        'educational_outcomes': len(EDUCATIONAL_OUTCOMES),
        'integration_systems': len(INTEGRATION),
        'avg_tier_completion_pct': avg_tier_pct,
        'lessons_live': lessons_live,
        'lessons_total': lessons_total,
        'enrollment_tracking_live': False,
        'assessments_live': False,
        'curriculum_readiness_pct': curriculum_readiness,
    },
    'catalog_gaps': [
        'Canonical /learn/tier-[n]/[lesson-slug] routes not built',
        'Curriculum enrollment and lesson completion not tracked',
        'Learning path progress not persisted — no learner accounts',
        '5/5 assessment types planned or partial only — no interactive checks',
        'Reading Level 3 (Advanced) not uniform across lessons',
        'Public Official Resource Path planned only',
        f'{lessons_live}/{lessons_total} core lessons have interim content',
        'Curriculum maintenance review schedule not automated in MC',
        '0 coalition participants — Tier 6 civic application untested',
    ],
    'recommended_next_build': {
        'number': 36,
        'title': 'Component Specifications with Props/States',
        'note': 'Map curriculum tiers, learning paths, and reading levels to COMP-* from Build #17.',
    },
}

path = root / 'data/master-curriculum.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Curriculum: {lessons_live}/{lessons_total} lessons, {curriculum_readiness}% readiness')
