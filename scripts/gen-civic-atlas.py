"""
Generate data/civic-atlas.json, community-profiles.json, community-assets.json — Build #58.
Arkansas Civic Intelligence & Community Mapping System — The Arkansas Civic Atlas v1.0.
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
cos = load_json(root / 'data/county-operating-system.json')
sg = load_json(root / 'data/statewide-growth.json')
no = load_json(root / 'data/neighborhood-organizing.json')
counties_data = load_json(root / 'data/arkansas-counties.json')
cities_data = load_json(root / 'data/arkansas-cities.json')
coalition = load_json(root / 'data/coalition-directory.json')
vj = load_json(root / 'data/visitor-journey.json')

ex = mc.get('executive', {})
orgs = coalition.get('summary', {}).get('total_organizations', 0)
edu_leaders = vj.get('summary', {}).get('education_leader_signups', 0)
participants = vj.get('summary', {}).get('contact_network_signups', 0)

counties = counties_data.get('counties', [])
counties_total = len(counties) or 75
cities_total = cities_data.get('cities_total', 250)
regions = cos.get('regions', [])
communities_joined = 0
neighborhoods = no.get('summary', {}).get('neighborhoods_represented', 0)
events_scheduled = 0
stories_documented = 0
assets_cataloged = 0

GEOGRAPHIC_HIERARCHY = [
    {'level': 1, 'id': 'state', 'title': 'State', 'scope': 'Arkansas', 'status': 'partial'},
    {'level': 2, 'id': 'region', 'title': 'Region', 'scope': f'{len(regions)} regions', 'status': 'defined'},
    {'level': 3, 'id': 'county', 'title': 'County', 'scope': f'{counties_total} counties', 'status': 'scaffolded'},
    {'level': 4, 'id': 'city', 'title': 'City', 'scope': f'{cities_total} largest cities', 'status': 'scaffolded'},
    {'level': 5, 'id': 'community', 'title': 'Community', 'scope': 'Participating communities', 'status': 'planned'},
    {'level': 6, 'id': 'neighborhood', 'title': 'Neighborhood', 'scope': 'Last mile', 'status': 'planned'},
    {'level': 7, 'id': 'education_leader', 'title': 'Education Leader', 'scope': 'Individual educators', 'status': 'planned'},
]

PROFILE_FIELDS = [
    'County', 'City', 'Population (public data)',
    'Education Leaders', 'Coalition partners',
    'Libraries', 'Schools and colleges', 'Community organizations',
    'Faith communities participating (opt-in listing)',
    'Community conversation history', 'Educational events',
    'Resource requests', 'Educational priorities (local)',
]

COVERAGE_SCORE_COMPONENTS = [
    {
        'id': 'ECS-LD', 'category': 'Leadership', 'weight_pct': 25,
        'indicators': ['Education Leaders present', 'Leadership depth'],
        'status': 'scaffolded',
    },
    {
        'id': 'ECS-LN', 'category': 'Learning', 'weight_pct': 20,
        'indicators': ['Active learners', 'Curriculum completion'],
        'status': 'planned',
    },
    {
        'id': 'ECS-CM', 'category': 'Community', 'weight_pct': 20,
        'indicators': ['Conversations held', 'Events hosted'],
        'status': 'planned',
    },
    {
        'id': 'ECS-CL', 'category': 'Coalition', 'weight_pct': 20,
        'indicators': ['Partner organizations', 'Organizational diversity'],
        'status': 'planned',
    },
    {
        'id': 'ECS-RS', 'category': 'Resources', 'weight_pct': 15,
        'indicators': ['Toolkit usage', 'Resource downloads'],
        'status': 'planned',
    },
]

ASSET_TYPES = [
    'Public libraries', 'Community colleges', 'Universities',
    'Museums', 'Historical societies', 'Civic clubs',
    'Veteran organizations', 'Community centers',
    'Nonprofit organizations', 'Other participating educational institutions',
]

NEEDS_SIGNALS = [
    {'id': 'NS-1', 'signal': 'Counties without Education Leaders', 'count': counties_total, 'status': 'active'},
    {'id': 'NS-2', 'signal': 'Cities without coalition partners', 'count': cities_total, 'status': 'active'},
    {'id': 'NS-3', 'signal': 'Communities requesting presentations', 'count': 0, 'status': 'planned'},
    {'id': 'NS-4', 'signal': 'Areas with limited resource usage', 'count': counties_total, 'status': 'active'},
    {'id': 'NS-5', 'signal': 'Communities seeking additional materials', 'count': 0, 'status': 'planned'},
]

CALENDAR_EVENT_TYPES = [
    'Educational events', 'Community conversations', 'Academy workshops',
    'Coalition meetings', 'Public presentations', 'Volunteer opportunities',
]

GROWTH_DASHBOARD_METRICS = [
    {'id': 'GD-1', 'metric': 'New communities joining', 'current': communities_joined, 'status': 'live'},
    {'id': 'GD-2', 'metric': 'New Education Leaders', 'current': edu_leaders, 'status': 'live'},
    {'id': 'GD-3', 'metric': 'New coalition organizations', 'current': orgs, 'status': 'live'},
    {'id': 'GD-4', 'metric': 'Educational events added', 'current': events_scheduled, 'status': 'live'},
    {'id': 'GD-5', 'metric': 'Neighborhood participation', 'current': neighborhoods, 'status': 'live'},
    {'id': 'GD-6', 'metric': 'Resource distribution', 'current': 0, 'status': 'planned'},
]

STORY_TYPES = [
    'First community conversation', 'New Education Leader',
    'Coalition milestones', 'Local partnerships',
    'Educational innovations', 'Community success stories',
]

ALLOCATION_QUESTIONS = [
    'Where should the next workshop be held?',
    'Which counties need additional Education Leaders?',
    'Which cities have requested presentations?',
    'Where should new printed materials be distributed?',
    'Which coalition partners may mentor nearby communities?',
]

MC_DASHBOARD_PANELS = [
    {'id': 'CAP-1', 'panel': 'County coverage', 'status': 'partial'},
    {'id': 'CAP-2', 'panel': 'City coverage', 'status': 'partial'},
    {'id': 'CAP-3', 'panel': 'Community coverage', 'status': 'planned'},
    {'id': 'CAP-4', 'panel': 'Neighborhood participation', 'status': 'planned'},
    {'id': 'CAP-5', 'panel': 'Education Leader density', 'status': 'planned'},
    {'id': 'CAP-6', 'panel': 'Coalition partner locations', 'status': 'planned'},
    {'id': 'CAP-7', 'panel': 'Upcoming events', 'status': 'planned'},
    {'id': 'CAP-8', 'panel': 'Educational Coverage Scores', 'status': 'partial'},
    {'id': 'CAP-9', 'panel': 'Growth trends over time', 'status': 'planned'},
]

FUTURE_CAPABILITIES = [
    'Regional collaboration networks',
    'Traveling educational exhibits',
    'Mobile learning events',
    'Resource distribution planning',
    'Historical education trails',
    'Community-generated educational content (after editorial review)',
]

SYSTEM_CONNECTIONS = [
    {'system': 'Statewide Growth (#56)', 'route': '/mission-control/statewide-growth.html', 'status': 'live'},
    {'system': 'Neighborhood Organizing (#57)', 'route': '/mission-control/neighborhood-organizing.html', 'status': 'live'},
    {'system': 'County Operating System (#31)', 'route': '/mission-control/county-os.html', 'status': 'partial'},
    {'system': 'Coalition Directory', 'route': '/coalition/', 'status': 'planned'},
    {'system': 'Education Academy', 'route': '/mission-control/education-academy.html', 'status': 'partial'},
    {'system': 'Outreach Engine', 'route': '/mission-control/outreach.html', 'status': 'partial'},
    {'system': 'Civic Intelligence / KG', 'route': '/mission-control/civic-intelligence.html', 'status': 'partial'},
    {'system': 'Mission Control', 'route': '/mission-control/', 'status': 'live'},
]

# County coverage scores — honest zeros
county_scores = []
for c in counties:
    county_scores.append({
        'fips': c.get('fips'),
        'name': c.get('name'),
        'education_coverage_score': 0,
        'components': {
            'leadership': 0, 'learning': 0, 'community': 0, 'coalition': 0, 'resources': 0,
        },
        'education_leaders': c.get('educators', 0),
        'participants': c.get('participants', 0),
        'conversations': c.get('conversations', 0),
        'status': 'no_coverage',
    })

region_coverage = [
    {
        'id': r['id'], 'title': r['title'], 'status': r.get('status', 'defined'),
        'counties_mapped': 0, 'education_leaders': 0, 'avg_coverage_score': 0,
    }
    for r in regions
]

map_layers = [
    {'id': 'leaders', 'layer': 'Education Leaders active', 'status': 'planned'},
    {'id': 'coalition', 'layer': 'Coalition partners', 'status': 'planned'},
    {'id': 'conversations', 'layer': 'Community conversations', 'status': 'planned'},
    {'id': 'libraries', 'layer': 'Libraries engaged', 'status': 'planned'},
    {'id': 'colleges', 'layer': 'Colleges participating', 'status': 'planned'},
    {'id': 'civic_orgs', 'layer': 'Civic organizations helping', 'status': 'planned'},
    {'id': 'gaps', 'layer': 'No educational infrastructure', 'status': 'planned'},
]

# Readiness
hierarchy_score = 35
score_model_score = 12
assets_score = 5
integration_score = 8
civic_atlas_readiness = min(52, hierarchy_score + score_model_score + assets_score + integration_score)

out_profiles = {
    'version': '1.0',
    'build': 58,
    'updated': today,
    'title': 'Community Profiles Registry',
    'summary': {
        'communities_total': communities_joined,
        'with_leaders': 0,
        'with_events': 0,
        'with_stories': stories_documented,
    },
    'profile_schema': {'fields': PROFILE_FIELDS},
    'communities': [],
}

out_assets = {
    'version': '1.0',
    'build': 58,
    'updated': today,
    'title': 'Community Assets Directory',
    'asset_types': ASSET_TYPES,
    'summary': {
        'assets_cataloged': assets_cataloged,
        'by_type': {t: 0 for t in ASSET_TYPES},
    },
    'assets': [],
}

out = {
    'version': '1.0',
    'build': 58,
    'updated': today,
    'title': 'Arkansas Civic Atlas v1.0',
    'subtitle': 'Civic Intelligence & Community Mapping System',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/civic-atlas.html',
    'constitution': '/docs/MASTER_CIVIC_ATLAS.md',
    'purpose': (
        'Living intelligence system mapping communities, civic institutions, educational opportunities, '
        'and outreach capacity — educational planning, not political targeting.'
    ),
    'governing_principle': (
        'Serve every part of Arkansas thoughtfully and equitably. Maps reveal where civic understanding '
        'is growing and where opportunities remain.'
    ),
    'not_political_targeting': True,
    'planning_questions': [
        'Where are we reaching people?',
        'Where are we missing people?',
        'Where should we invest educational resources next?',
    ],
    'vision': (
        'A map of Arkansas where every county, city, and community tells an educational story — '
        'leaders, partners, conversations, assets, and gaps visible at a glance.'
    ),
    'geographic_hierarchy': {
        'title': 'Arkansas Geographic Hierarchy',
        'flow': 'State → Region → County → City → Community → Neighborhood → Education Leader',
        'levels': GEOGRAPHIC_HIERARCHY,
    },
    'community_profiles': {
        'title': 'Living Community Profiles',
        'registry': '/data/community-profiles.json',
        'fields': PROFILE_FIELDS,
        'communities_count': communities_joined,
        'status': 'scaffolded',
    },
    'educational_coverage_score': {
        'title': 'Educational Coverage Score',
        'principle': 'Measures educational capacity — not political activity',
        'scale': '0–100 per county and community',
        'components': COVERAGE_SCORE_COMPONENTS,
        'statewide_avg': 0,
        'counties_scored': counties_total,
        'status': 'scaffolded',
    },
    'county_coverage': {
        'counties_total': counties_total,
        'counties_with_coverage': 0,
        'statewide_avg_score': 0,
        'counties': county_scores,
    },
    'region_coverage': region_coverage,
    'community_assets_directory': {
        'title': 'Civic Education Assets Inventory',
        'registry': '/data/community-assets.json',
        'asset_types': ASSET_TYPES,
        'assets_cataloged': assets_cataloged,
        'status': 'scaffolded',
    },
    'community_needs_assessment': {
        'title': 'Educational Opportunity Signals',
        'signals': NEEDS_SIGNALS,
        'priority': 'Outreach based on educational need',
    },
    'arkansas_civic_calendar': {
        'title': 'Statewide Civic Calendar',
        'event_types': CALENDAR_EVENT_TYPES,
        'events_scheduled': events_scheduled,
        'browse_by': ['County', 'City'],
        'status': 'planned',
    },
    'community_growth_dashboard': {
        'title': 'Geographic Growth Visualization',
        'metrics': GROWTH_DASHBOARD_METRICS,
        'geographic_visualization': 'planned',
        'status': 'partial',
    },
    'civic_story_archive': {
        'title': 'Community Educational Journey',
        'story_types': STORY_TYPES,
        'stories_documented': stories_documented,
        'status': 'planned',
    },
    'resource_allocation_engine': {
        'title': 'Planning Support',
        'questions': ALLOCATION_QUESTIONS,
        'status': 'planned',
        'note': 'Thoughtful planning rather than guesswork',
    },
    'map_layers': {
        'title': 'Educational Story Map Layers',
        'interactive_map_status': 'planned',
        'layers': map_layers,
    },
    'mc_integration': {
        'title': 'Geographic Heartbeat Dashboard',
        'panels': MC_DASHBOARD_PANELS,
        'panels_live': sum(1 for p in MC_DASHBOARD_PANELS if p['status'] in ('live', 'partial')),
        'status': 'partial',
    },
    'future_expansion': FUTURE_CAPABILITIES,
    'system_connections': SYSTEM_CONNECTIONS,
    'long_term_vision': [
        'Living portrait of civic education across Arkansas',
        'Where learning is flourishing and partnerships are forming',
        'Where additional support is needed',
        'How communities connect through shared educational purpose',
    ],
    'summary': {
        'regions_total': len(regions),
        'counties_total': counties_total,
        'cities_indexed': cities_total,
        'communities_joined': communities_joined,
        'neighborhoods_represented': neighborhoods,
        'education_leaders': edu_leaders,
        'coalition_orgs': orgs,
        'participants': participants,
        'assets_cataloged': assets_cataloged,
        'events_scheduled': events_scheduled,
        'stories_documented': stories_documented,
        'statewide_avg_coverage_score': 0,
        'counties_with_coverage': 0,
        'interactive_map_status': 'planned',
        'civic_atlas_readiness_pct': civic_atlas_readiness,
        'statewide_growth_readiness_pct': sg.get('summary', {}).get('statewide_growth_readiness_pct', 48),
        'neighborhood_organizing_readiness_pct': no.get('summary', {}).get('neighborhood_organizing_readiness_pct', 50),
        'public_launch_readiness_pct': ex.get('public_launch_readiness', 8),
    },
    'catalog_gaps': [
        f'0/{counties_total} counties with coverage — all ECS scores at 0',
        f'0 community profiles · {assets_cataloged} assets cataloged',
        'Interactive Arkansas map not built — MC tables only',
        'Civic calendar not implemented — 0 events scheduled',
        'Civic story archive empty — no community journeys documented',
        'Resource allocation engine planned — no query API',
        'Faith community listings require opt-in — no listing workflow',
        'County-to-region mapping incomplete in county scores',
        'Align ECS with County OS education score (#31) — two models coexist',
        'Community assets directory scaffold only — no library/college ingestion',
    ],
    'recommended_next_build': {
        'number': 59,
        'title': 'Implementation Translation Layer & Engineering Artifacts',
        'note': (
            'Neon schema for communities, assets, ECS scores, calendar events; map layer API; '
            'route inventory, COMP-* specs, API contracts, GitHub issue backlog.'
        ),
    },
}

with open(root / 'data/community-profiles.json', 'w', newline='\n') as f:
    json.dump(out_profiles, f, indent=2)
    f.write('\n')

with open(root / 'data/community-assets.json', 'w', newline='\n') as f:
    json.dump(out_assets, f, indent=2)
    f.write('\n')

with open(root / 'data/civic-atlas.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

print(
    f'Civic Atlas: {counties_total} counties scored, {len(regions)} regions, '
    f'{communities_joined} communities, {civic_atlas_readiness}% readiness'
)
