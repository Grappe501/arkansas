import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]

def slugify(name):
    s = name.lower().replace('.', '').replace("'", '')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

with open(root / 'data/arkansas-counties.json') as f:
    counties = json.load(f)

entries = []
for c in counties['counties']:
    slug = slugify(c['name'])
    entries.append({
        'fips': c['fips'],
        'name': c['name'],
        'slug': slug,
        'route': f'/coalition/county.html?county={slug}',
        'organizations': 0,
        'education_leaders': 0,
        'community_educators': 0,
        'upcoming_events': 0,
        'resource_requests': 0,
        'volunteer_opportunities': 0,
        'community_conversations': 0,
        'local_partnerships': 0,
        'completeness_pct': 0,
        'status': 'needs_partner',
        'vision': 'At least one active educational partner in every Arkansas county.'
    })

out = {
    'version': '1.0',
    'build': 14,
    'acucos': 'Arkansas Citizens United Coalition Operating System',
    'updated': '2026-07-09',
    'counties_total': len(entries),
    'summary': {
        'counties_with_partner': 0,
        'counties_complete': 0,
        'average_completeness_pct': 0,
        'needs_outreach': 'All 75 counties — goal is one active educational partner per county.'
    },
    'counties': entries
}

with open(root / 'data/county-coalition-index.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'wrote {len(entries)} county coalition entries')
