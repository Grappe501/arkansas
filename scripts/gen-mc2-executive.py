"""
Generate data/mc2-executive.json — Build #25 Mission Control 2.0 & Executive Command Center v1.0.
Pulls live readiness from mission-control.json where available.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

mc_path = root / 'data/mission-control.json'
mc = {}
if mc_path.exists():
    with open(mc_path) as f:
        mc = json.load(f)

ex = mc.get('executive', {})
dep = mc.get('deployment', {})
civic = mc.get('civic_action', {})
facts = mc.get('facts_inventory', {})
route_inv = mc.get('route_inventory', {})
rel_health = mc.get('relationship_health', {})


def workspace(wid, title, purpose, tracks, route, status, data_source=None, notes=None):
    return {
        'id': wid,
        'title': title,
        'purpose': purpose,
        'track_count': len(tracks),
        'tracks': tracks,
        'route': route,
        'implementation_status': status,
        'data_source': data_source,
        'notes': notes,
    }


workspaces = [
    workspace('MC2-WS-01', 'Executive Overview', 'High-level project status snapshot', [
        'Platform completion', 'Current build', 'Active development', 'Public readiness', 'Arkansas readiness map'
    ], '/mission-control/executive.html', 'partial', '/data/mission-control.json',
        'MC2 executive command center — this build'),
    workspace('MC2-WS-02', 'Development Center', 'Phases, builds, components, routes, features', [
        'Phases', 'Builds', 'Components', 'Routes', 'Features', 'Bugs', 'Enhancements'
    ], '/mission-control/phases.html', 'partial', '/data/mission-control.json',
        'Phases + builds live; bugs/features tracking not formalized'),
    workspace('MC2-WS-03', 'Research Center', 'Sources, facts, citations, gaps, review schedule', [
        'Sources collected', 'Facts verified', 'Pages needing citations',
        'Research gaps', 'Review schedule'
    ], '/mission-control/research.html', 'partial', '/data/evidence-registry.json',
        '14 Evidence IDs; automated citation gap scan not built'),
    workspace('MC2-WS-04', 'Education Center', 'Lessons, resources, downloads, learning paths', [
        'Lessons completed', 'Resources published', 'Downloads',
        'Popular learning paths', 'FAQ growth', 'Toolkit usage'
    ], '/mission-control/atlas.html', 'partial', '/data/knowledge-atlas.json',
        'Atlas tracks worlds/districts; download analytics not integrated'),
    workspace('MC2-WS-05', 'Coalition Center', 'Organizations, counties, sign-ons, partnerships', [
        'Organizations', 'Counties represented', 'New sign-ons',
        'Partnership levels', 'Organization referrals'
    ], '/mission-control/coalition.html', 'partial', '/data/county-coalition-index.json',
        'ACUCOS dashboard live; sign-on queue not automated'),
    workspace('MC2-WS-06', 'Community Education Center', 'Events, conversations, speakers, presentations', [
        'Events', 'Community conversations', 'Speakers',
        'Presentations', 'Resource requests'
    ], '/mission-control/civic-ecosystem.html', 'partial', '/data/contact-intelligence.json',
        'County map scaffold; event capture form not built'),
    workspace('MC2-WS-07', 'Public Official Education Center', 'Educational outreach to federal and state officials', [
        'Packets prepared', 'Packets shared', 'Resource requests', 'Follow-up reminders',
        'U.S. House', 'U.S. Senate', 'Arkansas General Assembly'
    ], '/action/contact-legislators.html', 'planned', None,
        'Share-with-officials screen planned (WF-018); no tracking backend'),
    workspace('MC2-WS-08', 'Communications Center', 'Newsletter, traffic, social, referrals, shares', [
        'Newsletter growth', 'Website traffic', 'Social media performance',
        'Referral activity', 'Share rates', 'Returning visitors'
    ], None, 'planned', None,
        'No analytics integration; Netlify/GA not connected to MC'),
    workspace('MC2-WS-09', 'Command Center', 'Private admin operational headquarters', [
        'Review queues', 'Coalition approvals', 'Event management',
        'Research assignments', 'Content publishing', 'Build approvals',
        'Dashboard configuration', 'User management'
    ], '/admin/mission-control/', 'stub', None,
        'Admin view exists; queues and approvals not operational'),
]

executive_panels = [
    {'id': 'MC2-EP-01', 'title': 'Platform Completion', 'metric': 'overall_completion',
     'value': ex.get('overall_completion', 24), 'unit': 'percent', 'status': 'live'},
    {'id': 'MC2-EP-02', 'title': 'Current Build', 'metric': 'current_build',
     'value': ex.get('current_build', {}), 'status': 'live'},
    {'id': 'MC2-EP-03', 'title': 'Active Development', 'metric': 'active_phase',
     'value': ex.get('active_phase', ''), 'status': 'live'},
    {'id': 'MC2-EP-04', 'title': 'Public Readiness', 'metric': 'readiness_scores',
     'value': {
         'educational': ex.get('content_readiness', 18),
         'technical': ex.get('repository_structure_readiness', 28),
         'research': ex.get('research_readiness', 20),
         'coalition': ex.get('coalition_readiness', 14),
         'launch': ex.get('public_launch_readiness', 8),
     }, 'status': 'partial'},
    {'id': 'MC2-EP-05', 'title': 'Arkansas Readiness Map', 'metric': 'county_coverage',
     'value': {
         'counties_total': 75,
         'counties_active': rel_health.get('counties_active', 0),
         'education_leaders': civic.get('approved_local_leads', 0),
         'coalition_orgs': rel_health.get('organizations_connected', 0),
         'events': rel_health.get('events_hosted', 0),
         'conversations': rel_health.get('community_conversations', 0),
     }, 'route': '/mission-control/civic-ecosystem.html', 'status': 'partial'},
]

health_indicators = [
    {'id': 'MC2-HI-01', 'title': 'Research Health', 'score': ex.get('research_readiness', 20), 'status': 'partial',
     'source': 'research_readiness + evidence registry'},
    {'id': 'MC2-HI-02', 'title': 'Content Health', 'score': ex.get('content_readiness', 18), 'status': 'partial',
     'source': 'content inventory + knowledge atlas'},
    {'id': 'MC2-HI-03', 'title': 'Technical Health', 'score': ex.get('repository_structure_readiness', 28), 'status': 'partial',
     'source': 'platform + repository blueprints'},
    {'id': 'MC2-HI-04', 'title': 'Coalition Health', 'score': ex.get('coalition_readiness', 14), 'status': 'partial',
     'source': 'county-coalition-index + ACUCOS'},
    {'id': 'MC2-HI-05', 'title': 'County Coverage', 'score': round(rel_health.get('counties_active', 0) / 75 * 100) if rel_health else 0,
     'status': 'planned', 'source': 'relationship_health.counties_active / 75'},
    {'id': 'MC2-HI-06', 'title': 'Volunteer Capacity', 'score': ex.get('contact_intelligence_readiness', 31), 'status': 'partial',
     'source': 'contact-intelligence.json'},
    {'id': 'MC2-HI-07', 'title': 'Source Verification', 'score': facts.get('fact_completeness_pct', 62) if facts else 12,
     'status': 'partial', 'source': 'facts_inventory'},
    {'id': 'MC2-HI-08', 'title': 'Deployment Health', 'score': 85 if dep.get('production_status') == 'healthy' else 50,
     'status': 'live', 'source': 'deployment dashboard'},
    {'id': 'MC2-HI-09', 'title': 'Overall Project Health', 'score': 0, 'status': 'partial',
     'source': 'weighted average of health indicators'},
]

scores = [h['score'] for h in health_indicators[:-1] if h['id'] != 'MC2-HI-08']
health_indicators[-1]['score'] = round(sum(scores) / len(scores)) if scores else 0

smart_alerts = [
    {'id': 'MC2-SA-01', 'title': 'Counties without education leaders', 'status': 'defined', 'automated': False},
    {'id': 'MC2-SA-02', 'title': 'Pages needing citation review', 'status': 'defined', 'automated': False},
    {'id': 'MC2-SA-03', 'title': 'Coalition applications awaiting review', 'status': 'defined', 'automated': False},
    {'id': 'MC2-SA-04', 'title': 'Research nearing scheduled updates', 'status': 'defined', 'automated': False},
    {'id': 'MC2-SA-05', 'title': 'Broken links', 'status': 'defined', 'automated': False},
    {'id': 'MC2-SA-06', 'title': 'Incomplete learning paths', 'status': 'defined', 'automated': False},
    {'id': 'MC2-SA-07', 'title': 'Upcoming educational events', 'status': 'defined', 'automated': False},
    {'id': 'MC2-SA-08', 'title': 'Pending public official resource requests', 'status': 'defined', 'automated': False},
]

executive_reports = [
    {'id': 'MC2-ER-01', 'title': 'Weekly progress report', 'status': 'planned'},
    {'id': 'MC2-ER-02', 'title': 'Monthly coalition report', 'status': 'planned'},
    {'id': 'MC2-ER-03', 'title': 'County activity report', 'status': 'planned'},
    {'id': 'MC2-ER-04', 'title': 'Research status report', 'status': 'planned'},
    {'id': 'MC2-ER-05', 'title': 'Mission Control snapshot', 'status': 'partial', 'note': 'Manual via mission-control.json export'},
    {'id': 'MC2-ER-06', 'title': 'Launch readiness assessment', 'status': 'partial', 'note': 'public_readiness score in MC v1'},
]

success_metrics = {
    'education': [
        {'metric': 'Learning paths completed', 'status': 'planned'},
        {'metric': 'Toolkit downloads', 'status': 'planned'},
        {'metric': 'Source library usage', 'status': 'planned'},
    ],
    'community': [
        {'metric': 'Community conversations', 'status': 'planned', 'current': rel_health.get('community_conversations', 0)},
        {'metric': 'Counties with active education leaders', 'status': 'partial', 'current': rel_health.get('counties_active', 0)},
        {'metric': 'Coalition organizations', 'status': 'partial', 'current': rel_health.get('organizations_connected', 0)},
    ],
    'research': [
        {'metric': 'Verified facts', 'status': 'partial', 'current': facts.get('verified', 8) if facts else 0},
        {'metric': 'Sources cataloged', 'status': 'partial', 'current': 14},
        {'metric': 'Pages fully cited', 'status': 'planned'},
    ],
    'growth': [
        {'metric': 'Returning visitors', 'status': 'planned'},
        {'metric': 'Volunteer signups', 'status': 'partial', 'current': civic.get('education_leader_signups', 0) + civic.get('contact_network_signups', 0)},
        {'metric': 'Organization partnerships', 'status': 'partial', 'current': rel_health.get('organizations_connected', 0)},
    ],
}

future_intelligence = [
    {'capability': 'Recommend next development priorities', 'status': 'planned'},
    {'capability': 'Identify research gaps', 'status': 'partial', 'note': 'research_readiness gaps listed manually'},
    {'capability': 'Suggest counties for outreach', 'status': 'planned'},
    {'capability': 'Recommend coalition partners', 'status': 'planned'},
    {'capability': 'Detect outdated content', 'status': 'planned'},
    {'capability': 'Build launch checklists', 'status': 'partial', 'note': 'public_readiness questions exist'},
    {'capability': 'Forecast project readiness', 'status': 'planned'},
]

executive_principles = [
    {'principle': 'Visibility', 'description': 'Nothing important is hidden.'},
    {'principle': 'Transparency', 'description': 'Progress and gaps are visible.'},
    {'principle': 'Accountability', 'description': 'Every major initiative has an owner and status.'},
    {'principle': 'Evidence', 'description': 'Metrics are grounded in verifiable information.'},
    {'principle': 'Continuous Improvement', 'description': 'Mission Control evolves alongside the platform.'},
]

build_timeline_schema = [
    'build_number', 'summary', 'phase', 'status', 'completion_date',
    'related_files', 'github_commit', 'netlify_deployment', 'notes', 'future_dependencies'
]

builds = mc.get('builds', [])
timeline_live = len([b for b in builds if b.get('status') == 'complete'])

by_ws_status = {}
for w in workspaces:
    by_ws_status[w['implementation_status']] = by_ws_status.get(w['implementation_status'], 0) + 1

status_weights = {'live': 100, 'partial': 55, 'stub': 25, 'planned': 12, 'defined': 15}
ws_readiness = round(sum(status_weights.get(w['implementation_status'], 10) for w in workspaces) / max(len(workspaces), 1))
reports_live = len([r for r in executive_reports if r['status'] == 'live'])
reports_partial = len([r for r in executive_reports if r['status'] == 'partial'])
reports_score = round((reports_live * 100 + reports_partial * 40) / max(len(executive_reports), 1))
alerts_automated = len([a for a in smart_alerts if a.get('automated')])
# Honest MC2: workspace implementation weighted; excludes pre-v1 deployment credit
overall_mc2 = round(ws_readiness * 0.55 + health_indicators[-1]['score'] * 0.30 + reports_score * 0.15)

out = {
    'version': '1.0',
    'build': 25,
    'updated': today,
    'title': 'Mission Control 2.0 & Executive Command Center v1.0',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/executive.html',
    'legacy_route': '/mission-control/',
    'constitution': '/docs/MISSION_CONTROL_2.md',
    'purpose': 'If it matters, it is visible. Mission Control as the operating system for the entire initiative.',
    'executive_philosophy': 'Answer within seconds: where are we, what is complete, what needs attention, where succeeding, where behind, what to build next.',
    'governing_principle': 'Help the team understand what should happen next — not merely what has happened.',
    'executive_panels': executive_panels,
    'workspaces': workspaces,
    'workspace_count': len(workspaces),
    'health_indicators': health_indicators,
    'smart_alerts': smart_alerts,
    'executive_reports': executive_reports,
    'success_metrics': success_metrics,
    'future_intelligence': future_intelligence,
    'executive_principles': executive_principles,
    'build_timeline': {
        'schema': build_timeline_schema,
        'builds_recorded': len(builds),
        'builds_complete': timeline_live,
        'data_source': '/data/mission-control.json',
        'status': 'live',
    },
    'command_center': {
        'route': '/admin/mission-control/',
        'capabilities': workspaces[-1]['tracks'],
        'status': 'stub',
    },
    'arkansas_readiness_map': {
        'title': 'Arkansas Readiness Map',
        'route': '/mission-control/civic-ecosystem.html',
        'counties_total': 75,
        'layers': [
            'Education leaders', 'Coalition organizations', 'Community conversations',
            'Events', 'Counties with no activity', 'Counties needing outreach'
        ],
        'status': 'partial',
        'signature_visualization': True,
    },
    'related_dashboards': [
        {'title': 'MC v1 Dashboard', 'route': '/mission-control/'},
        {'title': 'Contact Intelligence', 'route': '/mission-control/contact-intelligence.html', 'build': 24},
        {'title': 'Wireframes', 'route': '/mission-control/wireframes.html', 'build': 23},
        {'title': 'Database Schema', 'route': '/mission-control/database.html', 'build': 22},
    ],
    'summary': {
        'workspaces': len(workspaces),
        'executive_panels': len(executive_panels),
        'health_indicators': len(health_indicators),
        'smart_alerts_defined': len(smart_alerts),
        'smart_alerts_automated': alerts_automated,
        'executive_reports': len(executive_reports),
        'future_intelligence_capabilities': len(future_intelligence),
        'builds_in_timeline': len(builds),
        'workspace_live': by_ws_status.get('live', 0),
        'workspace_partial': by_ws_status.get('partial', 0),
        'workspace_stub': by_ws_status.get('stub', 0),
        'workspace_planned': by_ws_status.get('planned', 0),
        'overall_project_health': health_indicators[-1]['score'],
        'mc2_readiness_pct': overall_mc2,
    },
    'catalog_gaps': [
        'Smart alerts defined but not automated',
        'Executive reports not generatable on demand',
        'Communications Center has no analytics integration',
        'Public Official Education Center not operational',
        'Command Center queues/approvals not built',
        'Arkansas map layers not fully interactive',
        'Future intelligence layer mostly planned',
        'Success metrics lack live data feeds',
    ],
    'recommended_next_build': {
        'number': 26,
        'title': 'Component Specifications with Props/States',
        'note': 'Map wireframe sections to component props; wire MC2 alerts to real data sources.',
    },
}

path = root / 'data/mc2-executive.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'MC2 Executive: {len(workspaces)} workspaces, {overall_mc2}% readiness')
