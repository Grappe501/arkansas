"""
Generate data/arkansas-communications.json — Build #72.
Master Arkansas Communications & Public Education System v1.0.
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
ex = mc.get('executive', {})

# Honest zeros
articles_published = 0
videos_released = 0
emails_sent = 0
presentation_requests = 0
community_events = 0
social_media_reach = 0
resource_downloads = 0
press_inquiries = 0
editorial_calendar_live = False
communications_dashboard_live = False
review_workflow_operational = False

COMMUNICATION_QUESTIONS = [
    'What happened?',
    'Why does it matter?',
    'What does the evidence show?',
    'Where can I learn more?',
    'How can I help educate others?',
]

INSTITUTIONAL_VOICE = [
    'Calm', 'Respectful', 'Evidence-based', 'Patient', 'Curious',
    'Transparent', 'Welcoming', 'Hopeful', 'Confident without being arrogant',
]

COMMUNICATION_OBJECTIVES = [
    {'id': 'ACOM-O1', 'number': 1, 'title': 'Explain', 'description': 'Help Arkansans understand complex ideas', 'status': 'specified'},
    {'id': 'ACOM-O2', 'number': 2, 'title': 'Connect', 'description': 'Show relationships between history, law, campaign finance, and Arkansas', 'status': 'specified'},
    {'id': 'ACOM-O3', 'number': 3, 'title': 'Invite', 'description': 'Encourage continued learning and participation', 'status': 'specified'},
    {'id': 'ACOM-O4', 'number': 4, 'title': 'Equip', 'description': 'Provide resources that help others teach', 'status': 'specified'},
    {'id': 'ACOM-O5', 'number': 5, 'title': 'Strengthen', 'description': 'Build lasting relationships with communities across Arkansas', 'status': 'specified'},
]

COMMUNICATION_CHANNELS = [
    {'id': 'ACOM-CH1', 'channel': 'Website', 'status': 'partial', 'route': '/'},
    {'id': 'ACOM-CH2', 'channel': 'Email', 'status': 'planned'},
    {'id': 'ACOM-CH3', 'channel': 'Social media', 'status': 'planned'},
    {'id': 'ACOM-CH4', 'channel': 'Community presentations', 'status': 'planned'},
    {'id': 'ACOM-CH5', 'channel': 'Educational videos', 'status': 'planned', 'route': '/mission-control/media-studio.html'},
    {'id': 'ACOM-CH6', 'channel': 'Podcasts', 'status': 'planned'},
    {'id': 'ACOM-CH7', 'channel': 'Printable resources', 'status': 'planned'},
    {'id': 'ACOM-CH8', 'channel': 'Community conversations', 'status': 'planned'},
    {'id': 'ACOM-CH9', 'channel': 'Coalition newsletters', 'status': 'planned', 'route': '/coalition/'},
    {'id': 'ACOM-CH10', 'channel': 'Press materials', 'status': 'planned'},
]

CONTENT_PYRAMID = [
    'Research Paper', 'Comprehensive Article', 'Lesson', 'Infographic',
    'Video', 'Presentation', 'Social Media Graphic', 'One-Page Fact Sheet', 'Shareable Quote',
]

EDITORIAL_CALENDAR_TYPES = [
    'Research releases', 'Historical anniversaries', 'Supreme Court milestones',
    'Educational campaigns', 'Community conversations', 'Academy announcements',
    'Coalition updates', 'Arkansas legislative education (when relevant)',
]

SOCIAL_MEDIA_PURPOSES = [
    'Introduce ideas', 'Share educational resources', 'Highlight new research',
    'Celebrate Education Leaders', 'Promote community events', 'Invite deeper learning',
]

EMAIL_SERIES = [
    'Welcome sequence', 'Learning pathways', 'Research updates', 'Academy news',
    'Community stories', 'Coalition highlights', 'Mission Control updates', 'Annual reports',
]

PRESENTATION_FORMATS = [
    {'format': '30-minute overview', 'status': 'planned'},
    {'format': '60-minute workshop', 'status': 'planned'},
    {'format': 'Community discussion', 'status': 'planned'},
    {'format': 'Library presentation', 'status': 'planned'},
    {'format': 'College presentation', 'status': 'planned'},
    {'format': 'Civic organization presentation', 'status': 'planned'},
]

MEDIA_RESPONSE_PRINCIPLES = [
    'Providing verified information', 'Sharing primary sources',
    'Explaining historical context', 'Directing people to educational resources',
    'Maintaining a respectful tone',
]

STORYTELLING_TYPES = [
    'Historical stories', 'Supreme Court history', 'Arkansas stories',
    'Community success stories', 'Education Leader stories', 'Research discoveries',
]

COMMUNICATIONS_DASHBOARD = [
    {'id': 'ACOM-D1', 'indicator': 'Articles published', 'current': articles_published, 'status': 'planned'},
    {'id': 'ACOM-D2', 'indicator': 'Videos released', 'current': videos_released, 'status': 'planned'},
    {'id': 'ACOM-D3', 'indicator': 'Emails sent', 'current': emails_sent, 'status': 'planned'},
    {'id': 'ACOM-D4', 'indicator': 'Presentation requests', 'current': presentation_requests, 'status': 'planned'},
    {'id': 'ACOM-D5', 'indicator': 'Community events', 'current': community_events, 'status': 'planned'},
    {'id': 'ACOM-D6', 'indicator': 'Social media reach', 'current': social_media_reach, 'status': 'planned'},
    {'id': 'ACOM-D7', 'indicator': 'Resource downloads', 'current': resource_downloads, 'status': 'planned'},
    {'id': 'ACOM-D8', 'indicator': 'Press inquiries', 'current': press_inquiries, 'status': 'planned'},
    {'id': 'ACOM-D9', 'indicator': 'Communication effectiveness', 'current': 'not_measured', 'status': 'planned'},
]

REVIEW_WORKFLOW = [
    {'step': 1, 'id': 'research_review', 'title': 'Research Review', 'items_passed': 0, 'status': 'planned'},
    {'step': 2, 'id': 'editorial_review', 'title': 'Editorial Review', 'items_passed': 0, 'status': 'planned'},
    {'step': 3, 'id': 'evidence_verification', 'title': 'Evidence Verification', 'items_passed': 0, 'status': 'planned'},
    {'step': 4, 'id': 'accessibility_review', 'title': 'Accessibility Review', 'items_passed': 0, 'status': 'planned'},
    {'step': 5, 'id': 'publication', 'title': 'Publication', 'items_passed': 0, 'status': 'planned'},
    {'step': 6, 'id': 'performance_review', 'title': 'Performance Review', 'items_passed': 0, 'status': 'planned'},
]

SYSTEM_CONNECTIONS = [
    {'system': 'Master Research Library (#37)', 'route': '/mission-control/research-library.html', 'status': 'live'},
    {'system': 'Master Curriculum (#35)', 'route': '/mission-control/curriculum.html', 'status': 'live'},
    {'system': 'Media Studio (#39)', 'route': '/mission-control/media-studio.html', 'status': 'live'},
    {'system': 'Content Production Factory (#27)', 'route': '/mission-control/content-factory.html', 'status': 'live'},
    {'system': 'Narrative Architecture (#34)', 'route': '/mission-control/narrative.html', 'status': 'live'},
    {'system': 'Citizen Action Center (#62)', 'route': '/mission-control/citizen-action-center.html', 'status': 'live'},
    {'system': 'Community Education Academy (#28)', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Coalition Network (#61)', 'route': '/mission-control/coalition-network.html', 'status': 'live'},
    {'system': 'Community Listening (#71)', 'route': '/mission-control/arkansas-community-listening.html', 'status': 'live', 'note': 'Informs communications'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

arkansas_communications_readiness = min(
    42,
    10 + len(COMMUNICATION_OBJECTIVES) * 3 + len(COMMUNICATION_CHANNELS) * 2 + len(REVIEW_WORKFLOW) * 2,
)

out = {
    'version': '1.0',
    'build': 72,
    'updated': today,
    'title': 'Master Arkansas Communications & Public Education System v1.0',
    'subtitle': 'One Voice, Thousands of Conversations — The Institutional Communications Framework',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/arkansas-communications.html',
    'constitution': '/docs/MASTER_ARKANSAS_COMMUNICATIONS.md',
    'purpose': (
        'Permanent communications system — one consistent institutional voice across every '
        'article, video, presentation, post, email, interview, conversation, and campaign.'
    ),
    'governing_principle': (
        'Communicate to help Arkansas understand. Every communication leaves people better '
        'informed. Public service becomes trusted institution.'
    ),
    'communications_philosophy': {
        'increase_understanding_not_win_arguments': True,
        'education_before_persuasion': True,
        'questions_every_communication_answers': COMMUNICATION_QUESTIONS,
    },
    'institutional_voice': {
        'title': 'Institutional Voice',
        'traits': INSTITUTIONAL_VOICE,
        'trust_through_consistency': True,
        'status': 'specified',
    },
    'communication_objectives': {
        'title': 'Five Communication Objectives',
        'objectives': COMMUNICATION_OBJECTIVES,
    },
    'communication_channels': {
        'title': 'Communication Channels',
        'channels': COMMUNICATION_CHANNELS,
        'coordinated_mission': True,
        'status': 'partial',
    },
    'content_pyramid': {
        'title': 'The Content Pyramid',
        'layers': CONTENT_PYRAMID,
        'multiple_formats_per_topic': True,
        'status': 'specified',
    },
    'editorial_calendar': {
        'title': 'Editorial Calendar',
        'statewide_calendar': True,
        'live': editorial_calendar_live,
        'event_types': EDITORIAL_CALENDAR_TYPES,
        'status': 'planned',
    },
    'social_media_strategy': {
        'title': 'Social Media Strategy',
        'purposes': SOCIAL_MEDIA_PURPOSES,
        'return_to_institution_for_context': True,
        'status': 'planned',
    },
    'email_communications': {
        'title': 'Email Communications',
        'educate_before_ask': True,
        'series': EMAIL_SERIES,
        'informed_not_marketed': True,
        'emails_sent': emails_sent,
        'status': 'planned',
    },
    'presentation_system': {
        'title': 'Presentation System',
        'standardized_for_leaders': True,
        'formats': PRESENTATION_FORMATS,
        'evidence_based': True,
        'requests': presentation_requests,
        'status': 'planned',
    },
    'media_response_framework': {
        'title': 'Media Response Framework',
        'educational_resource_role': True,
        'principles': MEDIA_RESPONSE_PRINCIPLES,
        'press_inquiries': press_inquiries,
        'status': 'planned',
    },
    'storytelling_framework': {
        'title': 'Storytelling Framework',
        'story_types': STORYTELLING_TYPES,
        'makes_complex_memorable': True,
        'status': 'specified',
    },
    'communications_dashboard': {
        'title': 'Mission Control Communications Dashboard',
        'live': communications_dashboard_live,
        'educational_reach_not_marketing': True,
        'indicators': COMMUNICATIONS_DASHBOARD,
        'status': 'planned',
    },
    'communications_review_process': {
        'title': 'Communications Review Process',
        'quality_before_speed': True,
        'operational': review_workflow_operational,
        'steps': REVIEW_WORKFLOW,
        'status': 'planned',
    },
    'integration': {
        'chain': (
            'Research Library → Curriculum → Media Studio → Citizen Action Center → '
            'Education Academy → Coalition Network → Mission Control'
        ),
        'systems': SYSTEM_CONNECTIONS,
        'every_system_contributes': True,
    },
    'long_term_voice_recognition': (
        'Arkansans recognize the voice immediately — not loud, reliable. Researched carefully, '
        'documented transparently, explained clearly, presented respectfully.'
    ),
    'summary': {
        'communication_objectives': len(COMMUNICATION_OBJECTIVES),
        'communication_channels': len(COMMUNICATION_CHANNELS),
        'content_pyramid_layers': len(CONTENT_PYRAMID),
        'articles_published': articles_published,
        'videos_released': videos_released,
        'emails_sent': emails_sent,
        'presentation_requests': presentation_requests,
        'community_events': community_events,
        'social_media_reach': social_media_reach,
        'resource_downloads': resource_downloads,
        'press_inquiries': press_inquiries,
        'editorial_calendar_live': editorial_calendar_live,
        'communications_dashboard_live': communications_dashboard_live,
        'review_workflow_operational': review_workflow_operational,
        'arkansas_communications_readiness_pct': arkansas_communications_readiness,
        'content_factory_readiness_pct': ex.get('content_factory_readiness', 30),
        'media_studio_readiness_pct': ex.get('media_studio_readiness', 18),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        '0 articles tracked in communications registry — no publish pipeline',
        '0 videos released — Media Studio not wired to communications dashboard',
        '0 emails sent — no email series or welcome sequence built',
        '0 presentation requests — leader presentation kit not distributed',
        'Editorial calendar specified — not live in Mission Control',
        'Communications dashboard planned — not live',
        'Review workflow specified — 0 items passed through 6-step process',
        'Content pyramid specified — no multi-format generation workflow',
        'Social media strategy specified — no coordinated posting system',
        'Build #72 vs Content Factory (#27) — reconcile communications vs production?',
        'Build #72 vs Narrative Architecture (#34) — unify voice specs?',
        'Communication effectiveness not measured — educational reach metrics undefined',
        'Press inquiry workflow not built — 0 inquiries handled',
    ],
    'recommended_next_build': {
        'number': 73,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Editorial calendar UI, content pyramid workflow, review queue, presentation kit, '
            'email series templates, communications dashboard, COMP-* specs, GitHub backlog.'
        ),
    },
}

with open(root / 'data/arkansas-communications.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Arkansas Communications: {articles_published} articles, {videos_released} videos, '
    f'{emails_sent} emails, {arkansas_communications_readiness}% readiness'
)
