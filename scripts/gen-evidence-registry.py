"""
Seed / refresh evidence-registry summary stats from items array.
Run after adding evidence items manually.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'data/evidence-registry.json'

with open(path) as f:
    ev = json.load(f)

items = ev['items']
by_tier = {}
by_type = {}
for item in items:
    t = item['tier']
    by_tier[t] = by_tier.get(t, 0) + 1
    st = item['source_type']
    by_type[st] = by_type.get(st, 0) + 1

awaiting = sum(1 for i in items if i['review_status'] in ('requires_review', 'identified', 'under_revision'))
needing = sum(1 for i in items if i['verification'] in ('pending_update', 'requires_review'))
published = sum(1 for i in items if i['workflow_stage'] == 'published')

ev['summary'].update({
    'total': len(items),
    'by_tier': {str(k): v for k, v in sorted(by_tier.items())},
    'by_type': by_type,
    'primary_sources': by_tier.get(1, 0),
    'government_sources': by_type.get('government', 0),
    'academic_sources': by_type.get('academic', 0),
    'journalism_sources': by_type.get('journalism', 0),
    'awaiting_review': awaiting,
    'needing_updates': needing,
    'published': published,
})

with open(path, 'w', newline='\n') as f:
    json.dump(ev, f, indent=2)
    f.write('\n')
print(f'Updated {len(items)} evidence items')
