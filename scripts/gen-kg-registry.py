"""Refresh kg-registry summary stats from nodes and edges."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'data/kg-registry.json'

with open(path) as f:
    reg = json.load(f)

nodes = reg['nodes']
edges = reg['edges']
by_type = {}
by_cluster = {}
for n in nodes:
    by_type[n['type']] = by_type.get(n['type'], 0) + 1
    if n.get('cluster'):
        by_cluster[n['cluster']] = by_cluster.get(n['cluster'], 0) + 1

connected = set()
for e in edges:
    connected.add(e['from'])
    connected.add(e['to'])
orphans = sum(1 for n in nodes if n['kg_id'] not in connected)

pcts = [n.get('completion_pct', 0) for n in nodes if n.get('completion_pct') is not None]
avg = round(sum(pcts) / len(pcts)) if pcts else 0

reg['summary'].update({
    'total_nodes': len(nodes),
    'total_edges': len(edges),
    'by_type': by_type,
    'by_cluster': by_cluster,
    'avg_completion_pct': avg,
    'orphan_nodes': orphans,
    'fully_connected_hub': reg.get('hub_node') in connected,
})

with open(path, 'w', newline='\n') as f:
    json.dump(reg, f, indent=2)
    f.write('\n')
print(f'{len(nodes)} nodes, {len(edges)} edges, {orphans} orphans')
