"""
Generate data/county-operating-system.json — Build #31 Arkansas County Operating System v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

cci_path = root / 'data/county-coalition-index.json'
cci = {}
counties = []
if cci_path.exists():
    with open(cci_path) as f:
        cci = json.load(f)
    counties = cci.get('counties', [])

COUNTY_PROFILE_SECTIONS = [
    'County overview', 'Population snapshot', 'Legislative districts', 'Congressional district',
    'State Senate districts', 'State House districts', 'Major communities', 'Coalition partners',
    'Education Leaders', 'Upcoming educational events', 'Community conversations', 'Available resources'
]

EDUCATION_SCORE_CATEGORIES = [
    {
        'id': 'COS-ES-L', 'title': 'Learning',
        'indicators': ['Registered learners', 'Returning learners', 'Learning path completion'],
        'status': 'planned',
    },
    {
        'id': 'COS-ES-LD', 'title': 'Leadership',
        'indicators': ['Education Leaders', 'Community conversation hosts', 'Research volunteers'],
        'status': 'partial',
    },
    {
        'id': 'COS-ES-C', 'title': 'Coalition',
        'indicators': ['Partner organizations', 'New organizations', 'Organization activity'],
        'status': 'partial',
    },
    {
        'id': 'COS-ES-CM', 'title': 'Community',
        'indicators': ['Educational events', 'Presentations delivered', 'Resource downloads'],
        'status': 'planned',
    },
    {
        'id': 'COS-ES-R', 'title': 'Research',
        'indicators': ['Arkansas-specific resources', 'Local educational content', 'County profile completeness'],
        'status': 'planned',
    },
]

LEADERSHIP_ROLES = [
    'County Education Leader', 'Coalition Coordinator', 'Event Coordinator',
    'Research Contributor', 'Community Conversation Facilitator', 'Organization Liaison'
]

ORG_DIRECTORY_TYPES = [
    'Civic clubs', 'Libraries', 'Educational institutions', 'Faith communities',
    'Community nonprofits', 'Neighborhood associations', 'Veteran organizations', 'Professional associations'
]

PUBLIC_OFFICIAL_CATEGORIES = [
    'Arkansas House members', 'Arkansas Senators', 'Arkansas constitutional officers (where relevant)',
    "Arkansas's U.S. Representative for the district", "Arkansas's U.S. Senators"
]

RESOURCE_LIBRARY = [
    'Downloadable educational materials', 'Presentation slides', 'Community conversation guides',
    'Frequently asked questions', 'Arkansas legislative resources', 'Relevant research summaries'
]

EVENT_CALENDAR_TYPES = [
    'Educational events', 'Community conversations', 'Coalition meetings',
    'Workshops', 'Presentations', 'Webinars'
]

OUTREACH_GAPS = [
    'No Education Leaders', 'No coalition organizations', 'Few community conversations',
    'Limited resource usage', 'No scheduled events'
]

REGIONS = [
    {'id': 'COS-RG-01', 'title': 'Northwest Arkansas', 'status': 'defined'},
    {'id': 'COS-RG-02', 'title': 'North Central Arkansas', 'status': 'defined'},
    {'id': 'COS-RG-03', 'title': 'Central Arkansas', 'status': 'defined'},
    {'id': 'COS-RG-04', 'title': 'River Valley', 'status': 'defined'},
    {'id': 'COS-RG-05', 'title': 'Delta', 'status': 'defined'},
    {'id': 'COS-RG-06', 'title': 'Southwest Arkansas', 'status': 'defined'},
    {'id': 'COS-RG-07', 'title': 'Southeast Arkansas', 'status': 'defined'},
]

STORYTELLING_TYPES = [
    'Community conversations hosted', 'Coalition organizations joining',
    'New educational initiatives', 'Research contributions', 'Volunteer accomplishments'
]

COUNTY_METRICS = [
    {'id': 'COS-CM-01', 'title': 'Active learners', 'status': 'planned'},
    {'id': 'COS-CM-02', 'title': 'Education Leaders', 'status': 'partial'},
    {'id': 'COS-CM-03', 'title': 'Coalition partners', 'status': 'partial'},
    {'id': 'COS-CM-04', 'title': 'Educational events', 'status': 'planned'},
    {'id': 'COS-CM-05', 'title': 'Toolkit downloads', 'status': 'planned'},
    {'id': 'COS-CM-06', 'title': 'Research volunteers', 'status': 'planned'},
    {'id': 'COS-CM-07', 'title': 'Community conversations', 'status': 'planned'},
    {'id': 'COS-CM-08', 'title': 'Public official educational outreach', 'status': 'planned'},
    {'id': 'COS-CM-09', 'title': 'Learning path completion', 'status': 'planned'},
]

FUTURE_EXPANSION = [
    'County newsletters', 'County resource collections', 'Local educational campaigns',
    'Regional conferences', 'County-specific dashboards', 'Community-generated educational content (after review)'
]

# Aggregate from county-coalition-index
total_orgs = sum(c.get('organizations', 0) for c in counties)
total_leaders = sum(c.get('education_leaders', 0) for c in counties)
total_events = sum(c.get('upcoming_events', 0) for c in counties)
total_conversations = sum(c.get('community_conversations', 0) for c in counties)
avg_completeness = cci.get('summary', {}).get('average_completeness_pct', 0)
counties_with_partner = cci.get('summary', {}).get('counties_with_partner', 0)

status_weights = {'live': 100, 'partial': 48, 'defined': 30, 'planned': 10}
cat_readiness = round(sum(status_weights.get(c['status'], 5) for c in EDUCATION_SCORE_CATEGORIES) / len(EDUCATION_SCORE_CATEGORIES))
# 75 county scaffold = significant partial credit for structure
scaffold_score = min(len(counties) / 75 * 35, 35)
county_os_readiness = min(round(cat_readiness * 0.35 + scaffold_score + 8), 28)

out = {
    'version': '1.0',
    'build': 31,
    'updated': today,
    'title': 'Arkansas County Operating System v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/county-os.html',
    'canonical_county_route': '/arkansas/[county-name]',
    'current_county_route': '/coalition/county.html?county={slug}',
    'constitution': '/docs/COUNTY_OPERATING_SYSTEM.md',
    'purpose': 'Transform statewide website into 75 locally relevant educational presences.',
    'county_philosophy': 'Grow one county at a time — meaningful engagement, not just coverage.',
    'governing_principle': 'Strong statewide civic education is built from strong local communities.',
    'counties_total': 75,
    'county_profile_sections': COUNTY_PROFILE_SECTIONS,
    'education_score_categories': EDUCATION_SCORE_CATEGORIES,
    'leadership_roles': LEADERSHIP_ROLES,
    'organization_directory_types': ORG_DIRECTORY_TYPES,
    'public_official_categories': PUBLIC_OFFICIAL_CATEGORIES,
    'resource_library': RESOURCE_LIBRARY,
    'event_calendar_types': EVENT_CALENDAR_TYPES,
    'outreach_gap_signals': OUTREACH_GAPS,
    'regions': REGIONS,
    'storytelling_types': STORYTELLING_TYPES,
    'county_metrics': COUNTY_METRICS,
    'future_expansion': FUTURE_EXPANSION,
    'county_index_alignment': {
        'registry': '/data/county-coalition-index.json',
        'arkansas_counties': '/data/arkansas-counties.json',
        'build': 14,
        'counties_registered': len(counties),
        'counties_with_partner': counties_with_partner,
        'average_completeness_pct': avg_completeness,
    },
    'statewide_totals': {
        'organizations': total_orgs,
        'education_leaders': total_leaders,
        'upcoming_events': total_events,
        'community_conversations': total_conversations,
    },
    'related_systems': [
        {'title': 'County Coalition Index', 'route': '/data/county-coalition-index.json', 'build': 14},
        {'title': 'Civic Ecosystem', 'route': '/mission-control/civic-ecosystem.html', 'build': 12},
        {'title': 'Outreach Engine', 'route': '/mission-control/outreach.html', 'build': 30},
        {'title': 'Education Academy', 'route': '/mission-control/education-academy.html', 'build': 28},
        {'title': 'Contact Intelligence', 'route': '/mission-control/contact-intelligence.html', 'build': 24},
    ],
    'summary': {
        'counties_total': 75,
        'counties_scaffolded': len(counties),
        'profile_sections': len(COUNTY_PROFILE_SECTIONS),
        'education_score_categories': len(EDUCATION_SCORE_CATEGORIES),
        'leadership_roles': len(LEADERSHIP_ROLES),
        'regions': len(REGIONS),
        'county_metrics': len(COUNTY_METRICS),
        'counties_with_partner': counties_with_partner,
        'statewide_education_leaders': total_leaders,
        'statewide_organizations': total_orgs,
        'canonical_route_live': False,
        'education_score_live': False,
        'public_officials_per_county': False,
        'county_event_calendar_live': False,
        'county_os_readiness_pct': county_os_readiness,
    },
    'catalog_gaps': [
        'Canonical /arkansas/[county] routes not built — uses coalition/county.html?county=',
        'County Education Score not computed per county',
        'Public officials not mapped per county',
        'Population and district data not on county profiles',
        'County event calendar not per-county',
        'Regional dashboards not built',
        'All 75 counties at 0% completeness — no live partners yet',
        'County storytelling section not implemented',
    ],
    'recommended_next_build': {
        'number': 32,
        'title': 'Component Specifications with Props/States',
        'note': 'Map county profile sections to COMP-* components; wire education score to county-coalition-index.',
    },
}

path = root / 'data/county-operating-system.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'County OS: {len(counties)} counties, {county_os_readiness}% readiness')
