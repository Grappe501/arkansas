"""
Generate data/media-studio.json — Build #39 Documentary Experience & Media Studio v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

DIVISIONS = [
    {
        'id': 'MED-D01', 'number': 1, 'title': 'Documentary Films', 'slug': 'documentary-films',
        'purpose': 'Feature-length educational documentaries divided into chapters.',
        'examples': ['Before Citizens United', 'The Case', 'The Supreme Court', 'The Aftermath',
                     'The Continuing Debate', 'Arkansas Today'],
        'interim_route': '/mission-control/narrative.html',
        'status': 'partial', 'video_live': False, 'readiness_pct': 20,
        'note': 'Narrative acts + hall pages as text chapters — no film production yet',
    },
    {
        'id': 'MED-D02', 'number': 2, 'title': 'Short Explainer Videos', 'slug': 'short-explainers',
        'purpose': 'Five to ten minute classroom-ready lessons.',
        'examples': ['What is an Independent Expenditure?', 'What is a Super PAC?', 'What is Political Speech?',
                     'Understanding the First Amendment', 'Why Watergate Changed Campaign Finance'],
        'interim_route': '/halls/money-map.html',
        'status': 'planned', 'video_live': False, 'readiness_pct': 8,
    },
    {
        'id': 'MED-D03', 'number': 3, 'title': 'Animated Explainers', 'slug': 'animated-explainers',
        'purpose': 'Animation to simplify court, legislative, and campaign finance concepts.',
        'examples': ['Court procedures', 'Legislative processes', 'Campaign finance concepts',
                     'Historical timelines', 'Money flow diagrams'],
        'interim_route': '/halls/money-map.html',
        'status': 'planned', 'video_live': False, 'readiness_pct': 6,
    },
    {
        'id': 'MED-D04', 'number': 4, 'title': 'Interactive Interviews', 'slug': 'interactive-interviews',
        'purpose': 'Scholar, historian, journalist, and official interviews with verifiable sources.',
        'examples': ['Legal scholars', 'Historians', 'Journalists', 'Former public officials', 'Researchers'],
        'interim_route': '/library/',
        'status': 'planned', 'video_live': False, 'readiness_pct': 5,
    },
    {
        'id': 'MED-D05', 'number': 5, 'title': 'Audio Library', 'slug': 'audio-library',
        'purpose': 'Educational audio for listening-first learners.',
        'examples': ['Lesson narration', 'Historical readings', 'Interview recordings', 'Educational discussions'],
        'interim_route': '/educate/',
        'status': 'planned', 'video_live': False, 'readiness_pct': 8,
    },
    {
        'id': 'MED-D06', 'number': 6, 'title': 'Infographic Studio', 'slug': 'infographic-studio',
        'purpose': 'Reusable downloadable educational graphics.',
        'examples': ['Timeline graphics', 'Court decision diagrams', 'Campaign finance flowcharts',
                     'Constitutional concept maps', 'Before-and-after comparisons'],
        'interim_route': '/halls/money-map.html',
        'status': 'partial', 'video_live': False, 'readiness_pct': 22,
        'note': 'Static hall diagrams — no downloadable infographic library yet',
    },
    {
        'id': 'MED-D07', 'number': 7, 'title': 'Presentation Studio', 'slug': 'presentation-studio',
        'purpose': 'Slide decks, speaker notes, handouts, and audience adaptations.',
        'examples': ['Slide decks', 'Speaker notes', 'Handouts', 'Discussion guides', 'Audience adaptations'],
        'interim_route': '/educate/#toolkit',
        'status': 'partial', 'video_live': False, 'readiness_pct': 30,
        'note': 'Education Academy presentation toolkit — no packet generator',
    },
    {
        'id': 'MED-D08', 'number': 8, 'title': 'Classroom Resources', 'slug': 'classroom-resources',
        'purpose': 'Materials for schools, colleges, libraries, and community organizations.',
        'examples': ['High school civics', 'Colleges', 'Universities', 'Adult education',
                     'Libraries', 'Community organizations'],
        'interim_route': '/educate/',
        'status': 'partial', 'video_live': False, 'readiness_pct': 24,
        'note': 'Master Curriculum tiers mapped — no audience-tagged resource packs',
    },
]

DOCUMENTARY_CHAPTERS = [
    {
        'id': 'DOC-CH-01', 'number': 1, 'title': 'Before Citizens United', 'slug': 'before-citizens-united',
        'interim_route': '/halls/story-before.html', 'narrative_act': 'NARR-ACT-01',
        'status': 'partial', 'video_live': False, 'readiness_pct': 25,
        'structure_elements': ['Opening narrative', 'Historical context', 'Evidence presentation',
                               'Primary source highlights', 'Related learning paths'],
        'structure_gaps': ['Interviews or commentary', 'Data visualizations', 'Reflection questions'],
    },
    {
        'id': 'DOC-CH-02', 'number': 2, 'title': 'The Case', 'slug': 'the-case',
        'interim_route': '/halls/the-case.html', 'narrative_act': 'NARR-ACT-02',
        'status': 'partial', 'video_live': False, 'readiness_pct': 22,
        'structure_elements': ['Opening narrative', 'Historical context', 'Evidence presentation',
                               'Primary source highlights'],
        'structure_gaps': ['Interviews or commentary', 'Data visualizations', 'Reflection questions', 'Related learning paths'],
    },
    {
        'id': 'DOC-CH-03', 'number': 3, 'title': 'The Supreme Court', 'slug': 'the-supreme-court',
        'interim_route': '/halls/what-court-decided.html', 'narrative_act': 'NARR-ACT-03',
        'status': 'partial', 'video_live': False, 'readiness_pct': 28,
        'structure_elements': ['Opening narrative', 'Historical context', 'Evidence presentation',
                               'Primary source highlights', 'Related learning paths'],
        'structure_gaps': ['Interviews or commentary', 'Data visualizations', 'Reflection questions'],
    },
    {
        'id': 'DOC-CH-04', 'number': 4, 'title': 'The Aftermath', 'slug': 'the-aftermath',
        'interim_route': '/halls/after-2010.html', 'narrative_act': 'NARR-ACT-04',
        'status': 'partial', 'video_live': False, 'readiness_pct': 24,
        'structure_elements': ['Opening narrative', 'Historical context', 'Evidence presentation',
                               'Related learning paths'],
        'structure_gaps': ['Interviews or commentary', 'Data visualizations', 'Primary source highlights', 'Reflection questions'],
    },
    {
        'id': 'DOC-CH-05', 'number': 5, 'title': 'The Continuing Debate', 'slug': 'the-continuing-debate',
        'interim_route': '/halls/debate.html', 'narrative_act': 'NARR-ACT-05',
        'status': 'partial', 'video_live': False, 'readiness_pct': 20,
        'structure_elements': ['Opening narrative', 'Evidence presentation', 'Related learning paths'],
        'structure_gaps': ['Historical context', 'Interviews or commentary', 'Data visualizations',
                           'Primary source highlights', 'Reflection questions'],
    },
    {
        'id': 'DOC-CH-06', 'number': 6, 'title': 'Arkansas Today', 'slug': 'arkansas-today',
        'interim_route': '/solutions/#arkansas', 'narrative_act': 'NARR-ACT-08',
        'status': 'planned', 'video_live': False, 'readiness_pct': 12,
        'structure_elements': ['Related learning paths'],
        'structure_gaps': ['Opening narrative', 'Historical context', 'Evidence presentation',
                           'Interviews or commentary', 'Data visualizations', 'Primary source highlights', 'Reflection questions'],
    },
]

CHAPTER_STRUCTURE = [
    'Opening narrative', 'Historical context', 'Evidence presentation', 'Interviews or commentary',
    'Data visualizations', 'Primary source highlights', 'Reflection questions', 'Related learning paths',
]

MEDIA_STANDARDS = [
    'Transcript', 'Closed captions', 'Source citations', 'Publication date',
    'Review date', 'Related lessons', 'Related encyclopedia entries',
]

ACCESSIBILITY_STANDARDS = [
    'Closed captions', 'Full transcripts', 'Audio descriptions when appropriate',
    'Downloadable text versions', 'Accessible playback controls',
]

COMMUNITY_MEDIA_LIBRARY = [
    'Downloadable presentation videos', 'Introductory clips', 'Discussion starters',
    'Promotional materials', 'Educational graphics', 'Printable companion guides',
]

MC_METRICS = [
    {'id': 'MED-M01', 'title': 'Videos published', 'status': 'planned', 'current': 0},
    {'id': 'MED-M02', 'title': 'Documentary chapters completed', 'status': 'planned', 'current': 0},
    {'id': 'MED-M03', 'title': 'Transcript completion', 'status': 'planned', 'current': 0},
    {'id': 'MED-M04', 'title': 'Caption completion', 'status': 'planned', 'current': 0},
    {'id': 'MED-M05', 'title': 'Infographics created', 'status': 'planned', 'current': 0},
    {'id': 'MED-M06', 'title': 'Presentation kits downloaded', 'status': 'planned', 'current': 0},
    {'id': 'MED-M07', 'title': 'Media engagement', 'status': 'planned', 'current': 0},
    {'id': 'MED-M08', 'title': 'Classroom resource usage', 'status': 'planned', 'current': 0},
]

FUTURE_EXPANSION = [
    'Educational podcasts', 'Interactive documentaries', 'Virtual exhibits',
    'Livestream educational events', 'Community-produced educational stories (editorial review)',
    'Additional civic education topics',
]

div_partial = sum(1 for d in DIVISIONS if d['status'] == 'partial')
div_planned = sum(1 for d in DIVISIONS if d['status'] == 'planned')
avg_division_readiness = round(sum(d['readiness_pct'] for d in DIVISIONS) / len(DIVISIONS))
chapters_partial = sum(1 for c in DOCUMENTARY_CHAPTERS if c['status'] == 'partial')
videos_live = sum(1 for d in DIVISIONS if d.get('video_live'))
chapters_with_video = sum(1 for c in DOCUMENTARY_CHAPTERS if c.get('video_live'))

media_studio_readiness = min(
    round(avg_division_readiness * 0.4 + (div_partial / 8 * 100) * 0.2 + (chapters_partial / 6 * 100) * 0.15 + 8),
    18,
)

out = {
    'version': '1.0',
    'build': 39,
    'updated': today,
    'title': 'Documentary Experience & Media Studio v1.0',
    'subtitle': 'Multimedia Learning Architecture',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/media-studio.html',
    'canonical_media_route': '/media/[division-slug]/[asset-slug]',
    'current_media_route': 'Hall pages, educate toolkit, narrative acts — interim static content',
    'constitution': '/docs/DOCUMENTARY_EXPERIENCE_MEDIA_STUDIO.md',
    'purpose': 'Transform the platform into a multimedia civic education institution.',
    'vision': 'Ken Burns history · PBS experience · presidential library archives · university curriculum · interactive museum exhibits.',
    'governing_principle': 'Accessible civic education without sacrificing depth — trustworthy evidence in every medium.',
    'long_term_vision': 'Read, watch, hear, explore evidence, and teach with professional-quality materials.',
    'divisions': DIVISIONS,
    'documentary_chapters': DOCUMENTARY_CHAPTERS,
    'chapter_structure': CHAPTER_STRUCTURE,
    'media_standards': MEDIA_STANDARDS,
    'community_media_library': COMMUNITY_MEDIA_LIBRARY,
    'accessibility_standards': ACCESSIBILITY_STANDARDS,
    'mc_integration': {
        'title': 'Mission Control Media Studio Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'engagement_tracking_live': False,
    },
    'future_expansion': FUTURE_EXPANSION,
    'related_systems': [
        {'title': 'Narrative Architecture', 'route': '/data/narrative-architecture.json', 'build': 34},
        {'title': 'Master Curriculum', 'route': '/data/master-curriculum.json', 'build': 35},
        {'title': 'Education Academy', 'route': '/data/education-academy.json', 'build': 28},
        {'title': 'Content Production Factory', 'route': '/data/content-production-factory.json', 'build': 27},
        {'title': 'Learning Laboratory', 'route': '/data/learning-laboratory.json', 'build': 38},
        {'title': 'Trust Framework', 'route': '/data/trust-framework.json', 'build': 36},
    ],
    'summary': {
        'divisions_total': len(DIVISIONS),
        'divisions_partial': div_partial,
        'divisions_planned': div_planned,
        'documentary_chapters_total': len(DOCUMENTARY_CHAPTERS),
        'documentary_chapters_partial': chapters_partial,
        'videos_published': 0,
        'videos_live': videos_live,
        'chapters_with_video': chapters_with_video,
        'transcripts_complete': 0,
        'captions_complete': 0,
        'infographics_created': 0,
        'avg_division_readiness_pct': avg_division_readiness,
        'media_standards_count': len(MEDIA_STANDARDS),
        'accessibility_standards_count': len(ACCESSIBILITY_STANDARDS),
        'mc_metrics': len(MC_METRICS),
        'engagement_tracking_live': False,
        'media_studio_readiness_pct': media_studio_readiness,
    },
    'catalog_gaps': [
        '0 videos published — no documentary film production pipeline',
        '0/6 documentary chapters have video — halls provide text-only interim',
        'No transcript or caption workflow — media standards defined only',
        'Short explainer and animated video divisions not started',
        'Interactive interviews division not started',
        'Audio library not built — no narration or podcast hosting',
        'Infographic Studio — static hall diagrams only, no downloadable library',
        'Presentation Studio — toolkit text on educate/, no slide deck generator',
        'Community media library — no downloadable clips or promotional assets',
        'Media engagement metrics not tracked — no analytics integration',
    ],
    'recommended_next_build': {
        'number': 45,
        'title': 'Component Specifications with Props/States',
        'note': 'Map media player shells, documentary chapter layouts, infographic widgets, and accessibility patterns to COMP-* from Build #17.',
    },
}

path = root / 'data/media-studio.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Media Studio: {div_partial}/8 partial, {chapters_partial}/6 chapters, {media_studio_readiness}% readiness')
