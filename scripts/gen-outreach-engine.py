"""
Generate data/outreach-engine.json — Build #30 Arkansas Outreach Engine v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

mc_path = root / 'data/mission-control.json'
mc = {}
civic = {}
coalition = {}
if mc_path.exists():
    with open(mc_path) as f:
        mc = json.load(f)
    civic = mc.get('civic_action', {})
    coalition = mc.get('coalition_outreach', {})

OUTREACH_SEQUENCE = [
    'Discover', 'Learn', 'Understand', 'Share', 'Discuss', 'Teach', 'Build Community'
]

PILLARS = [
    {
        'id': 'OUT-P1', 'number': 1, 'title': 'Digital Education',
        'purpose': 'Website as permanent authoritative educational library',
        'destinations': ['Educational articles', 'Interactive timelines', 'Research library', 'Source documents', 'Learning paths'],
        'status': 'partial', 'route': '/',
    },
    {
        'id': 'OUT-P2', 'number': 2, 'title': 'Social Media Education',
        'purpose': 'Introduce ideas — not replace learning',
        'content_types': [
            'Short educational videos', 'Historical facts', 'Timeline graphics', 'FAQs',
            'Myth-versus-fact posts', 'Supreme Court excerpts', 'Arkansas legislative updates', 'Research highlights'
        ],
        'status': 'planned', 'route': '/coalition/resources.html',
    },
    {
        'id': 'OUT-P3', 'number': 3, 'title': 'Community Conversations',
        'purpose': 'Education grows through discussion',
        'venues': [
            'Library presentations', 'Civic clubs', 'Neighborhood meetings', 'Community centers',
            'Faith community discussions', 'Campus organizations', 'Local educational events'
        ],
        'status': 'partial', 'route': '/action/community-conversation.html',
    },
    {
        'id': 'OUT-P4', 'number': 4, 'title': 'Coalition Outreach',
        'purpose': 'Partners multiply civic education reach',
        'activities': [
            'Share resources', 'Host events', 'Invite speakers', 'Promote learning paths',
            'Introduce new participants', 'Connect additional organizations'
        ],
        'status': 'partial', 'route': '/coalition/',
    },
    {
        'id': 'OUT-P5', 'number': 5, 'title': 'Public Official Education',
        'purpose': 'Share organized educational resources with lawmakers',
        'audiences': ['Arkansas U.S. Representatives', 'Arkansas U.S. Senators', 'Arkansas General Assembly'],
        'status': 'planned', 'route': '/action/contact-legislators.html',
    },
]

CAMPAIGNS = [
    {'id': 'OUT-C01', 'title': 'Educational Awareness Campaign', 'focus': 'Introduce the platform', 'status': 'planned'},
    {'id': 'OUT-C02', 'title': 'Learn the History Campaign', 'focus': 'Campaign finance history', 'status': 'planned', 'world': 'WORLD-01'},
    {'id': 'OUT-C03', 'title': 'Understanding the Decision Campaign', 'focus': 'Supreme Court case', 'status': 'planned', 'world': 'WORLD-02'},
    {'id': 'OUT-C04', 'title': 'Understanding the Constitution Campaign', 'focus': 'Constitutional principles', 'status': 'planned', 'world': 'WORLD-03'},
    {'id': 'OUT-C05', 'title': 'Follow the Money Campaign', 'focus': 'Political spending and data', 'status': 'planned', 'world': 'WORLD-04'},
    {'id': 'OUT-C06', 'title': 'Arkansas Solutions Campaign', 'focus': 'Federal, state, ballot options', 'status': 'partial', 'world': 'WORLD-06', 'route': '/solutions/'},
    {'id': 'OUT-C07', 'title': 'Community Education Campaign', 'focus': 'Recruit Education Leaders and coalition partners', 'status': 'partial', 'route': '/educate/'},
]

RESOURCE_FORMATS = [
    'Printable PDFs', 'Presentation slides', 'One-page summaries', 'Infographics',
    'Short videos', 'Community discussion guides', 'Frequently asked questions', 'Source packets'
]

SHARE_TOOLKIT = [
    'Copyable summaries', 'Downloadable graphics', 'Printable handouts',
    'QR codes linking to full lesson', 'Suggested social media captions'
]

ANALYTICS_METRICS = [
    {'id': 'OUT-AM-01', 'title': 'Website visits', 'status': 'planned'},
    {'id': 'OUT-AM-02', 'title': 'Returning visitors', 'status': 'planned'},
    {'id': 'OUT-AM-03', 'title': 'Learning path completion', 'status': 'planned'},
    {'id': 'OUT-AM-04', 'title': 'Resource downloads', 'current': civic.get('toolkit_requests', 0), 'status': 'planned'},
    {'id': 'OUT-AM-05', 'title': 'Social media referrals', 'status': 'planned'},
    {'id': 'OUT-AM-06', 'title': 'Coalition referrals', 'current': coalition.get('organizational_referrals', 0), 'status': 'planned'},
    {'id': 'OUT-AM-07', 'title': 'Friend and family invitations', 'current': civic.get('referrals', 0), 'status': 'partial', 'route': '/action/share.html'},
    {'id': 'OUT-AM-08', 'title': 'Event attendance', 'status': 'planned'},
    {'id': 'OUT-AM-09', 'title': 'Education Leader signups', 'current': civic.get('education_leader_signups', 0), 'status': 'partial', 'route': '/educate/'},
    {'id': 'OUT-AM-10', 'title': 'Organization sign-ons', 'current': coalition.get('organizations_signed', 0) if coalition else 0, 'status': 'partial', 'route': '/coalition/join.html'},
]

COUNTY_OUTREACH_PROFILE = [
    'Counties with active Education Leaders', 'Counties with coalition partners',
    'Counties hosting events', 'Counties needing outreach', 'Counties with growing participation'
]

CONTINUOUS_IMPROVEMENT = [
    'Which resources are most frequently shared?',
    'Which learning paths are most often completed?',
    'Which questions are people asking?',
    'Which counties need additional resources?',
    'Which coalition partnerships produce educational activity?'
]

DASHBOARD_PANELS = [
    {'id': 'OUT-DB-01', 'title': 'Active outreach campaigns', 'current': 0, 'status': 'planned'},
    {'id': 'OUT-DB-02', 'title': 'Educational reach by county', 'current': 75, 'status': 'partial', 'note': '75 county scaffold'},
    {'id': 'OUT-DB-03', 'title': 'Community conversation activity', 'current': mc.get('relationship_health', {}).get('community_conversations', 0), 'status': 'planned'},
    {'id': 'OUT-DB-04', 'title': 'Coalition growth', 'current': coalition.get('organizations_signed', 0) if coalition else 0, 'status': 'partial'},
    {'id': 'OUT-DB-05', 'title': 'Public official educational outreach', 'current': 0, 'status': 'planned'},
    {'id': 'OUT-DB-06', 'title': 'Resource distribution', 'current': civic.get('share_actions', 0), 'status': 'partial', 'route': '/action/share.html'},
    {'id': 'OUT-DB-07', 'title': 'Social media performance', 'current': coalition.get('social_followers', 0) if coalition else 0, 'status': 'planned'},
    {'id': 'OUT-DB-08', 'title': 'Referral activity', 'current': civic.get('referrals', 0), 'status': 'partial'},
    {'id': 'OUT-DB-09', 'title': 'Upcoming events', 'current': 0, 'status': 'partial', 'route': '/coalition/events.html'},
]

by_pillar = {}
for p in PILLARS:
    by_pillar[p['status']] = by_pillar.get(p['status'], 0) + 1

status_weights = {'live': 100, 'partial': 45, 'planned': 10}
pillar_readiness = round(sum(status_weights.get(p['status'], 5) for p in PILLARS) / len(PILLARS))
campaign_partial = sum(1 for c in CAMPAIGNS if c['status'] == 'partial')
outreach_readiness = min(round(pillar_readiness * 0.5 + campaign_partial / len(CAMPAIGNS) * 100 * 0.2 + 6), 22)

out = {
    'version': '1.0',
    'build': 30,
    'updated': today,
    'title': 'Public Engagement & Education Campaign System v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/outreach.html',
    'constitution': '/docs/OUTREACH_ENGINE.md',
    'purpose': 'Help more Arkansans understand Citizens United — not rely on accidental discovery.',
    'outreach_philosophy': 'Discover → Learn → Understand → Share → Discuss → Teach → Build Community',
    'governing_principle': 'Expand understanding—not attention. Informed communities over popularity metrics.',
    'outreach_sequence': OUTREACH_SEQUENCE,
    'pillars': PILLARS,
    'pillar_count': len(PILLARS),
    'campaigns': CAMPAIGNS,
    'campaign_count': len(CAMPAIGNS),
    'resource_formats': RESOURCE_FORMATS,
    'share_toolkit': SHARE_TOOLKIT,
    'analytics_metrics': ANALYTICS_METRICS,
    'county_outreach_profile': COUNTY_OUTREACH_PROFILE,
    'continuous_improvement': CONTINUOUS_IMPROVEMENT,
    'dashboard_panels': DASHBOARD_PANELS,
    'event_promotion': {
        'supports': ['Educational events', 'Community conversations', 'Coalition partner events', 'Online sessions'],
        'county_discovery': True,
        'status': 'partial',
        'route': '/coalition/events.html',
    },
    'related_systems': [
        {'title': 'Share Page', 'route': '/action/share.html', 'build': 12},
        {'title': 'Coalition Hub', 'route': '/coalition/', 'build': 13},
        {'title': 'Education Academy', 'route': '/mission-control/education-academy.html', 'build': 28},
        {'title': 'Contact Intelligence', 'route': '/mission-control/contact-intelligence.html', 'build': 24},
        {'title': 'County Coalition Index', 'route': '/data/county-coalition-index.json', 'build': 14},
    ],
    'summary': {
        'pillars': len(PILLARS),
        'campaigns': len(CAMPAIGNS),
        'resource_formats': len(RESOURCE_FORMATS),
        'share_toolkit_items': len(SHARE_TOOLKIT),
        'analytics_metrics': len(ANALYTICS_METRICS),
        'dashboard_panels': len(DASHBOARD_PANELS),
        'pillars_partial': by_pillar.get('partial', 0),
        'pillars_planned': by_pillar.get('planned', 0),
        'campaigns_partial': campaign_partial,
        'analytics_live': 0,
        'campaign_management_live': False,
        'outreach_readiness_pct': outreach_readiness,
    },
    'catalog_gaps': [
        'No analytics integration (GA/Netlify Analytics not connected to MC)',
        'Campaign management system not built — 7 campaigns defined only',
        'Social media content library mostly planned',
        'Share toolkit on major pages incomplete',
        'QR codes and downloadable graphics not standardized',
        'County outreach profiles not interactive',
        'Public official share flow stub only',
        'Referral tracking not integrated with share page',
    ],
    'recommended_next_build': {
        'number': 31,
        'title': 'Component Specifications with Props/States',
        'note': 'Map share toolkit and campaign cards to COMP-* components; wire outreach dashboard to county index.',
    },
}

path = root / 'data/outreach-engine.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Outreach Engine: {len(PILLARS)} pillars, {outreach_readiness}% readiness')
