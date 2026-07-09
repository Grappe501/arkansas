"""
Generate data/ux-architecture.json — Build #52 Master User Experience Architecture v1.0.
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
vj = load_json(root / 'data/visitor-journey.json')
uxj = load_json(root / 'data/ux-journey.json')
atlas = load_json(root / 'data/knowledge-atlas.json')
coalition = load_json(root / 'data/coalition-directory.json')

vj_summary = vj.get('summary', {})
orgs = coalition.get('summary', {}).get('total_organizations', 0)
edu_leaders = vj_summary.get('education_leader_signups', 0)
learning_compass = atlas.get('learning_compass', {})
compass_fields = len(learning_compass.get('fields', []))

EMOTIONAL_JOURNEY = [
    {'order': 1, 'id': 'arrival', 'emotion': 'Arrival', 'visitor_thought': "I've come to the right place.", 'status': 'partial', 'implementation': 'Homepage + start-here — no arrival instrumentation'},
    {'order': 2, 'id': 'relief', 'emotion': 'Relief', 'visitor_thought': 'This is easier to understand than I expected.', 'status': 'partial', 'implementation': 'Plain-language halls — depth varies by page'},
    {'order': 3, 'id': 'curiosity', 'emotion': 'Curiosity', 'visitor_thought': "I didn't know that.", 'status': 'partial', 'implementation': '15 published assets — limited interactive discovery'},
    {'order': 4, 'id': 'discovery', 'emotion': 'Discovery', 'visitor_thought': "Now it's starting to make sense.", 'status': 'planned', 'implementation': 'Knowledge graph partial — connections not surfaced in UX'},
    {'order': 5, 'id': 'confidence', 'emotion': 'Confidence', 'visitor_thought': 'I think I can explain this.', 'status': 'planned', 'implementation': 'No completion or confidence tracking'},
    {'order': 6, 'id': 'ownership', 'emotion': 'Ownership', 'visitor_thought': 'I want to keep learning.', 'status': 'planned', 'implementation': 'localStorage journey only — no accounts'},
    {'order': 7, 'id': 'purpose', 'emotion': 'Purpose', 'visitor_thought': 'I want to help others understand.', 'status': 'planned', 'implementation': f'0 Education Leaders — teach funnel empty'},
]

FIRST_TIME_GOALS = [
    {'goal': 'What Citizens United is', 'status': 'partial', 'route': '/halls/the-case.html'},
    {'goal': 'Why it matters', 'status': 'partial', 'route': '/halls/after-2010.html'},
    {'goal': 'Why this website exists', 'status': 'partial', 'route': '/start-here/'},
    {'goal': 'How to begin learning', 'status': 'partial', 'route': '/explore/'},
]

NAVIGATION_PHILOSOPHY = [
    {'label': 'Learn', 'intent': 'Start understanding', 'status': 'partial', 'route': '/educate/'},
    {'label': 'Research', 'intent': 'Find sources and evidence', 'status': 'partial', 'route': '/library/'},
    {'label': 'Explore', 'intent': 'Browse the full map', 'status': 'live', 'route': '/explore/'},
    {'label': 'Watch', 'intent': 'Video and media learning', 'status': 'planned', 'route': '/mission-control/media-studio.html', 'note': '0 videos'},
    {'label': 'Teach', 'intent': 'Educate others', 'status': 'partial', 'route': '/educate/'},
    {'label': 'Arkansas', 'intent': 'Local civic context', 'status': 'partial', 'route': '/arkansas/'},
    {'label': 'Solutions', 'intent': 'Policy options', 'status': 'partial', 'route': '/solutions/'},
    {'label': 'Community', 'intent': 'Coalition and events', 'status': 'planned', 'route': '/coalition/', 'note': f'{orgs} orgs'},
    {'label': 'Mission Control', 'intent': 'Institutional operations', 'status': 'live', 'route': '/mission-control/'},
]

PROGRESSIVE_DISCLOSURE = [
    {'level': 1, 'id': 'sentence', 'title': 'One-sentence answer', 'status': 'partial'},
    {'level': 2, 'id': 'minute', 'title': 'One-minute explanation', 'status': 'partial'},
    {'level': 3, 'id': 'lesson', 'title': 'Five-minute lesson', 'status': 'planned'},
    {'level': 4, 'id': 'article', 'title': 'Complete article', 'status': 'partial'},
    {'level': 5, 'id': 'sources', 'title': 'Primary sources', 'status': 'partial'},
    {'level': 6, 'id': 'archive', 'title': 'Research archive', 'status': 'partial'},
]

LEARNING_COMPASS = {
    'title': 'Learning Compass',
    'component_id': learning_compass.get('component_id', 'COMP-NAV-004'),
    'questions': [
        {'id': 'where', 'question': 'Where am I?', 'status': 'partial', 'current': 'Journey panel on some pages'},
        {'id': 'learned', 'question': 'What have I learned?', 'status': 'planned', 'current': 'No learning ledger'},
        {'id': 'next', 'question': 'What comes next?', 'status': 'partial', 'current': 'Manual next-step links'},
        {'id': 'depth', 'question': 'How deep am I?', 'status': 'partial', 'current': 'Depth toggle on solutions only'},
        {'id': 'related', 'question': 'Related topics', 'status': 'planned', 'current': 'KG not surfaced in compass UI'},
        {'id': 'time', 'question': 'Estimated reading time', 'status': 'planned', 'current': 'Not calculated site-wide'},
        {'id': 'completion', 'question': 'Completion status', 'status': 'planned', 'current': 'No path completion tracking'},
    ],
    'schema_fields': compass_fields,
    'status': learning_compass.get('status', 'partial'),
    'route': '/data/knowledge-atlas.json',
}

CIVIC_COMPASS = {
    'title': 'Civic Compass',
    'principle': 'Separate from learning — participation without confusing education',
    'actions': [
        {'id': 'contact-network', 'title': 'Join Contact Network', 'status': 'partial', 'route': '/action/join-network.html'},
        {'id': 'education-leader', 'title': 'Become an Education Leader', 'status': 'partial', 'route': '/educate/'},
        {'id': 'coalition', 'title': 'Join Coalition', 'status': 'planned', 'route': '/coalition/join.html', 'note': f'{orgs} orgs'},
        {'id': 'share', 'title': 'Share this page', 'status': 'live', 'route': '/action/share.html'},
        {'id': 'events', 'title': 'Attend an event', 'status': 'planned', 'route': '/coalition/events.html'},
        {'id': 'legislative', 'title': 'Explore legislative resources', 'status': 'partial', 'route': '/action/draft-laws.html'},
        {'id': 'conversation', 'title': 'Host a conversation', 'status': 'partial', 'route': '/action/community-conversation.html'},
    ],
    'status': 'partial',
    'implementation': 'Merged into Action Hub — dedicated Civic Compass UI not built',
}

ACTION_HUB = {
    'title': 'Floating Action Hub',
    'version': 'v1.16.1',
    'status': 'live',
    'route': '/js/action-hub.js',
    'items': [
        {'id': 'ask-ai', 'title': 'Ask AI', 'status': 'planned', 'note': 'AI Knowledge Engine not public'},
        {'id': 'share', 'title': 'Share', 'status': 'live'},
        {'id': 'save', 'title': 'Save', 'status': 'live', 'note': 'Bookmark via localStorage'},
        {'id': 'print', 'title': 'Print', 'status': 'planned'},
        {'id': 'join', 'title': 'Join', 'status': 'partial'},
        {'id': 'teach', 'title': 'Teach', 'status': 'partial'},
        {'id': 'feedback', 'title': 'Give Feedback', 'status': 'planned'},
        {'id': 'learning-path', 'title': 'Return to Learning Path', 'status': 'partial', 'note': 'Journey panel — not all pages'},
    ],
    'context_aware': True,
    'pages_with_hub': 'Most public pages via layout.js',
}

READING_EXPERIENCE = {
    'principles': ['Wide margins', 'Comfortable spacing', 'Excellent contrast', 'Large headings', 'Readable citations', 'Minimal distractions'],
    'status': 'partial',
    'current': 'Design tokens v1.1 Institutional Authority — reading measure not universal',
    'design_route': '/design-system/',
}

VISUAL_IDENTITY = {
    'communicate': ['Integrity', 'Scholarship', 'Warmth', 'Curiosity', 'Precision', 'Transparency'],
    'never_feel_like': ['Campaign website', 'Law firm', 'Government portal', 'Corporate website'],
    'target_feel': 'Modern civic institution',
    'status': 'partial',
    'current': 'v1.1 cool institutional palette — warmth balance evolving',
    'brand_route': '/data/brand-identity.json',
}

TRUST_SIGNALS = [
    {'signal': 'Review date', 'status': 'partial', 'pages_with': 'design-system, solutions, library'},
    {'signal': 'Evidence score', 'status': 'partial', 'pages_with': 'facts framework partial'},
    {'signal': 'Primary sources', 'status': 'partial', 'pages_with': 'library, research halls'},
    {'signal': 'Citation count', 'status': 'planned'},
    {'signal': 'Related documents', 'status': 'planned'},
    {'signal': 'Authoring standards', 'status': 'partial'},
    {'signal': 'Version history', 'status': 'partial', 'pages_with': 'build registry, git'},
]

SEARCH_EXPERIENCE = {
    'status': 'planned',
    'principle': 'Conversational — never dead-end',
    'fallbacks': ['Related concepts', 'Suggested questions', 'Similar cases', 'Relevant laws', 'Learning paths'],
    'current': 'No site search — explore map only',
}

MOBILE_EXPERIENCE = {
    'status': 'partial',
    'principles': ['Thumb navigation', 'Quick lessons', 'Offline reading (future)', 'Audio playback', 'Shareable graphics', 'Community events'],
    'current': 'Responsive CSS — no mobile-specific lesson redesign',
}

ACCESSIBILITY_EXPERIENCE = {
    'status': 'partial',
    'principles': ['Readable layouts', 'Keyboard support', 'Captions', 'Transcripts', 'Reduced motion', 'Clear navigation'],
    'current': 'focus-visible tokens, prefers-reduced-motion — no WCAG audit, no captions',
    'route': '/mission-control/design.html',
}

COMMUNITY_EXPERIENCE = {
    'status': 'planned',
    'signals': ['County activity', 'Upcoming events', 'Coalition organizations', 'Education Leaders', 'Recently added resources', 'New research'],
    'current': f'0 county participation · {orgs} orgs · {edu_leaders} leaders — institution feels static',
}

MC_EXPERIENCE = {
    'status': 'live',
    'principle': 'Executive operations center — reduce cognitive load',
    'questions': ['Where are we?', "What's healthy?", "What's behind?", 'What needs attention?', 'What should we build next?'],
    'route': '/mission-control/',
    'builds_logged': len(mc.get('builds', [])),
}

DELIGHT_MOMENTS = [
    {'moment': 'Learning milestones', 'status': 'planned'},
    {'moment': 'Beautiful timeline transitions', 'status': 'planned'},
    {'moment': 'Knowledge graph animations', 'status': 'planned'},
    {'moment': 'Historical reveals', 'status': 'planned'},
    {'moment': 'Progress celebrations', 'status': 'planned'},
    {'moment': 'Handwritten archival notes', 'status': 'planned'},
    {'moment': 'Interactive document highlights', 'status': 'planned'},
]

PERSONALITY = [
    'Patient', 'Thoughtful', 'Curious', 'Well-read', 'Fair', 'Evidence-driven', 'Welcoming',
    'Never arrogant', 'Never sensational', 'Never dismissive', 'Always ready to teach',
]

emotion_partial = sum(1 for e in EMOTIONAL_JOURNEY if e['status'] == 'partial')
emotion_planned = sum(1 for e in EMOTIONAL_JOURNEY if e['status'] == 'planned')
nav_live = sum(1 for n in NAVIGATION_PHILOSOPHY if n['status'] == 'live')
nav_partial = sum(1 for n in NAVIGATION_PHILOSOPHY if n['status'] == 'partial')
hub_live = sum(1 for i in ACTION_HUB['items'] if i['status'] == 'live')
hub_partial = sum(1 for i in ACTION_HUB['items'] if i['status'] == 'partial')
trust_partial = sum(1 for t in TRUST_SIGNALS if t['status'] == 'partial')
compass_partial = sum(1 for q in LEARNING_COMPASS['questions'] if q['status'] == 'partial')
disclosure_partial = sum(1 for d in PROGRESSIVE_DISCLOSURE if d['status'] == 'partial')

MC_METRICS = [
    {'id': 'UX-01', 'title': 'Emotional journey defined', 'status': 'live', 'current': f'{len(EMOTIONAL_JOURNEY)} stages'},
    {'id': 'UX-02', 'title': 'Emotional journey instrumented', 'status': 'planned', 'current': f'{emotion_partial} partial, {emotion_planned} planned'},
    {'id': 'UX-03', 'title': 'First-time visitor goals', 'status': 'partial', 'current': f'{len(FIRST_TIME_GOALS)}/4 routes exist'},
    {'id': 'UX-04', 'title': 'Question-based navigation', 'status': 'partial', 'current': f'{nav_live} live, {nav_partial} partial nav intents'},
    {'id': 'UX-05', 'title': 'Progressive disclosure layers', 'status': 'partial', 'current': f'{disclosure_partial}/{len(PROGRESSIVE_DISCLOSURE)} partial'},
    {'id': 'UX-06', 'title': 'Learning Compass on all edu pages', 'status': 'planned', 'current': f'{compass_partial}/7 questions partial only'},
    {'id': 'UX-07', 'title': 'Civic Compass (separate UI)', 'status': 'planned', 'current': 'Merged into Action Hub'},
    {'id': 'UX-08', 'title': 'Floating Action Hub', 'status': 'live', 'current': f'{hub_live} live, {hub_partial} partial actions'},
    {'id': 'UX-09', 'title': 'Trust signals site-wide', 'status': 'partial', 'current': f'{trust_partial}/{len(TRUST_SIGNALS)} partial'},
    {'id': 'UX-10', 'title': 'Conversational search', 'status': 'planned', 'current': 'No search index'},
    {'id': 'UX-11', 'title': 'Mobile-first lesson design', 'status': 'planned', 'current': 'Responsive only'},
    {'id': 'UX-12', 'title': 'Accessibility WCAG audit', 'status': 'planned', 'current': 'Tokens only'},
    {'id': 'UX-13', 'title': 'Community vitality signals', 'status': 'planned', 'current': f'{orgs} orgs, {edu_leaders} leaders'},
    {'id': 'UX-14', 'title': 'Delight moments shipped', 'status': 'planned', 'current': '0/7 live'},
]

readiness_factors = [
    100,  # constitution defined
    (emotion_partial * 40) / len(EMOTIONAL_JOURNEY),
    sum(50 if g['status'] == 'partial' else 0 for g in FIRST_TIME_GOALS) / len(FIRST_TIME_GOALS),
    (nav_live * 100 + nav_partial * 50) / len(NAVIGATION_PHILOSOPHY),
    (disclosure_partial * 50) / len(PROGRESSIVE_DISCLOSURE),
    (compass_partial * 40) / len(LEARNING_COMPASS['questions']),
    45,  # civic compass partial via hub
    (hub_live * 100 + hub_partial * 50) / len(ACTION_HUB['items']),
    55 if READING_EXPERIENCE['status'] == 'partial' else 30,
    50 if VISUAL_IDENTITY['status'] == 'partial' else 30,
    (trust_partial * 50) / len(TRUST_SIGNALS),
    0,   # search
    40,  # mobile responsive
    35,  # accessibility partial
    5,   # community
    75,  # MC experience live
    0,   # delight
]
ux_architecture_readiness = round(sum(readiness_factors) / len(readiness_factors))

out = {
    'version': '1.0',
    'build': 52,
    'updated': today,
    'title': 'Master User Experience Architecture v1.0',
    'subtitle': 'The Institutional Experience Blueprint',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/ux-architecture.html',
    'constitution': '/docs/MASTER_UX_ARCHITECTURE.md',
    'purpose': 'How every visitor should feel — welcomed, respected, curious, and empowered to learn.',
    'governing_principle': (
        'Create one of the finest civic learning experiences ever built for a single Supreme Court decision — '
        'every interaction reduces confusion, increases confidence, and builds trust.'
    ),
    'experience_philosophy': {
        'metaphor': "Entering one of the world's great museums",
        'qualities': ['Invited not pressured', 'Every room teaches', 'Every exhibit connects', 'Every answer creates the next question'],
    },
    'extends': [
        {'title': 'Citizen Journey Blueprint', 'build': 8, 'route': '/data/ux-journey.json'},
        {'title': 'Visitor Journey & Behavioral Architecture', 'build': 47, 'route': '/data/visitor-journey.json'},
        {'title': 'Knowledge Atlas & Learning Paths', 'build': 19, 'route': '/data/knowledge-atlas.json'},
        {'title': 'Master Data Architecture', 'build': 51, 'route': '/data/data-architecture.json'},
        {'title': 'Design System', 'build': 9, 'route': '/design-system/'},
    ],
    'emotional_journey': {
        'title': 'Seven-Stage Emotional Arc',
        'stages': EMOTIONAL_JOURNEY,
        'stages_total': len(EMOTIONAL_JOURNEY),
        'note': 'Distinct from Build #47 behavioral stages — this is felt experience, not funnel metrics',
    },
    'first_time_visitor': {
        'title': '30-Second Orientation',
        'goals': FIRST_TIME_GOALS,
        'competing_goals_prohibited': True,
    },
    'navigation_philosophy': {
        'principle': 'Answer questions, not list software modules',
        'nav_intents': NAVIGATION_PHILOSOPHY,
    },
    'progressive_disclosure': {
        'principle': 'Never overwhelm — reveal complexity gradually',
        'layers': PROGRESSIVE_DISCLOSURE,
        'depth_toggle_live': 'solutions/index.html only',
    },
    'learning_compass': LEARNING_COMPASS,
    'civic_compass': CIVIC_COMPASS,
    'floating_action_hub': ACTION_HUB,
    'reading_experience': READING_EXPERIENCE,
    'visual_identity': VISUAL_IDENTITY,
    'trust_signals': {
        'principle': 'Quietly reinforce trust without dominating the page',
        'signals': TRUST_SIGNALS,
    },
    'search_experience': SEARCH_EXPERIENCE,
    'mobile_experience': MOBILE_EXPERIENCE,
    'accessibility_experience': ACCESSIBILITY_EXPERIENCE,
    'community_experience': COMMUNITY_EXPERIENCE,
    'mission_control_experience': MC_EXPERIENCE,
    'delight_moments': {
        'principle': 'Memorable without distracting from content',
        'moments': DELIGHT_MOMENTS,
        'delight_live': 0,
    },
    'institutional_personality': PERSONALITY,
    'long_term_vision': {
        'visitor_quotes': [
            'I came here because I had a question.',
            'I stayed because everything connected.',
            'I trusted it because I could verify it.',
            'I came back because nowhere else explains it this well.',
        ],
        'outcome': 'Experience becomes institutional reputation',
    },
    'mc_integration': {
        'title': 'Mission Control UX Architecture Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'authoritative_reference': True,
    },
    'related_blueprints': [
        {'title': 'Visitor Journey (#47)', 'route': '/mission-control/visitor-journey.html', 'build': 47},
        {'title': 'Citizen Journey (#8)', 'route': '/mission-control/journey.html', 'build': 8},
        {'title': 'Knowledge Atlas (#19)', 'route': '/mission-control/atlas.html', 'build': 19},
        {'title': 'Narrative Architecture (#34)', 'route': '/mission-control/narrative.html', 'build': 34},
        {'title': 'Design Blueprint', 'route': '/mission-control/design.html', 'build': 7},
    ],
    'summary': {
        'emotional_stages': len(EMOTIONAL_JOURNEY),
        'emotional_partial': emotion_partial,
        'emotional_planned': emotion_planned,
        'nav_intents': len(NAVIGATION_PHILOSOPHY),
        'nav_live': nav_live,
        'disclosure_layers': len(PROGRESSIVE_DISCLOSURE),
        'learning_compass_questions': len(LEARNING_COMPASS['questions']),
        'action_hub_items': len(ACTION_HUB['items']),
        'action_hub_live_items': hub_live,
        'trust_signals_partial': trust_partial,
        'search_live': False,
        'delight_moments_live': 0,
        'community_orgs': orgs,
        'education_leaders': edu_leaders,
        'visitor_journey_readiness_pct': vj_summary.get('visitor_journey_readiness_pct', 40),
        'ux_architecture_readiness_pct': ux_architecture_readiness,
    },
    'catalog_gaps': [
        'Learning Compass schema exists — UI not on all educational pages',
        'Civic Compass merged into Action Hub — no dedicated participation panel',
        'Ask AI, Print, Give Feedback not in Action Hub',
        'Progressive disclosure depth toggle only on Solutions page',
        'No site search — conversational fallbacks not built',
        '0 delight moments shipped — milestones and celebrations planned only',
        f'{orgs} coalition orgs, {edu_leaders} Education Leaders — community feels static',
        'Emotional journey (7 stages) vs behavioral journey (8 stages) — two models coexist',
        'Mobile responsive but not mobile-first lesson redesign',
        'WCAG audit not performed — accessibility tokens only',
        'Trust signals on handful of pages — not site-wide quiet reinforcement',
        '0 videos — Watch navigation intent leads to empty Media Studio',
    ],
    'recommended_next_build': {
        'number': 53,
        'title': 'Master Implementation Roadmap & Sprint Zero',
        'note': 'COMP-* Learning Compass + Civic Compass widgets, search MVP, first delight moment, Sprint backlog.',
    },
}

path = root / 'data/ux-architecture.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'UX Architecture: {hub_live} hub actions live, {ux_architecture_readiness}% readiness')
