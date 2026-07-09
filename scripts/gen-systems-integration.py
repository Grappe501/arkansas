"""
Generate data/systems-integration.json — Build #45 Master Systems Integration Blueprint v1.0.
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
exec_e = mc.get('executive', {})
civic = mc.get('civic_action', {})

SYSTEMS = [
    {
        'id': 'SYS-01', 'number': 1, 'title': 'Public Education Platform', 'slug': 'public-education',
        'purpose': 'Teach visitors.',
        'produces': ['Learning activity', 'Resource usage', 'Frequently asked questions', 'Educational progress'],
        'consumes': ['Research', 'Sources', 'Encyclopedia entries', 'Videos', 'Infographics'],
        'route': '/educate/', 'mc_route': '/mission-control/curriculum.html',
        'registry': '/data/master-curriculum.json', 'build': 35,
        'status': 'partial', 'integration_pct': 32,
        'data_flow_live': False,
    },
    {
        'id': 'SYS-02', 'number': 2, 'title': 'Encyclopedia', 'slug': 'encyclopedia',
        'purpose': 'Provide authoritative reference material.',
        'produces': ['Encyclopedia entries', 'Definitions', 'Historical summaries'],
        'consumes': ['Research', 'Claims Registry', 'Source Library', 'Knowledge Graph'],
        'route': '/mission-control/encyclopedia.html', 'registry': '/data/encyclopedia-knowledge-library.json', 'build': 33,
        'status': 'partial', 'integration_pct': 28,
        'data_flow_live': False,
    },
    {
        'id': 'SYS-03', 'number': 3, 'title': 'Source Library', 'slug': 'source-library',
        'purpose': 'Preserve evidence.',
        'produces': ['Source collections', 'Primary documents', 'Citation references'],
        'consumes': ['Government publications', 'Court opinions', 'Academic research', 'Historical records'],
        'route': '/library/', 'registry': '/data/evidence-registry.json', 'build': 10,
        'status': 'partial', 'integration_pct': 30,
        'data_flow_live': True,
        'note': '14 EV-* items — EV/KG links partial',
    },
    {
        'id': 'SYS-04', 'number': 4, 'title': 'Evidence Ledger', 'slug': 'evidence-ledger',
        'purpose': 'Verify every factual claim.',
        'produces': ['Verified claims', 'Evidence ratings', 'Review history'],
        'consumes': ['Source Library', 'Research Observatory', 'Editorial review'],
        'route': '/mission-control/evidence-ledger.html', 'registry': '/data/evidence-ledger.json', 'build': 41,
        'status': 'partial', 'integration_pct': 26,
        'data_flow_live': True,
        'note': '3 CLAIM-* linked to EV-* — audit trail not live',
    },
    {
        'id': 'SYS-05', 'number': 5, 'title': 'Research Observatory', 'slug': 'research-observatory',
        'purpose': 'Monitor ongoing developments.',
        'produces': ['Research updates', 'Legislative monitoring', 'Court monitoring', 'Data updates'],
        'consumes': ['Government releases', 'Academic publications', 'Public datasets'],
        'route': '/mission-control/research-observatory.html', 'registry': '/data/research-observatory.json', 'build': 29,
        'status': 'partial', 'integration_pct': 22,
        'data_flow_live': False,
    },
    {
        'id': 'SYS-06', 'number': 6, 'title': 'Community Education Academy', 'slug': 'education-academy',
        'purpose': 'Develop Education Leaders.',
        'produces': ['Trained volunteers', 'Presentation activity', 'Community conversations'],
        'consumes': ['Curriculum', 'Videos', 'Presentation resources', 'Research updates'],
        'route': '/mission-control/education-academy.html', 'registry': '/data/education-academy.json', 'build': 28,
        'status': 'partial', 'integration_pct': 24,
        'data_flow_live': False,
    },
    {
        'id': 'SYS-07', 'number': 7, 'title': 'Coalition Network', 'slug': 'coalition',
        'purpose': 'Connect Arkansas organizations.',
        'produces': ['Partnerships', 'Community events', 'Resource distribution', 'Educational reach'],
        'consumes': ['Academy resources', 'Presentation materials', 'Event support', 'Mission Control analytics'],
        'route': '/coalition/', 'registry': '/data/civic-ecosystem.json', 'build': 12,
        'status': 'partial', 'integration_pct': 20,
        'data_flow_live': False,
    },
    {
        'id': 'SYS-08', 'number': 8, 'title': 'Civic Action Lab', 'slug': 'civic-action-lab',
        'purpose': 'Educational exploration of legislative and ballot processes.',
        'produces': ['Educational workspaces', 'Comparative analyses', 'Research questions'],
        'consumes': ['Research', 'Constitutional analysis', 'Historical materials', 'Source Library'],
        'route': '/mission-control/civic-action-lab.html', 'registry': '/data/civic-action-lab.json', 'build': 42,
        'status': 'partial', 'integration_pct': 24,
        'data_flow_live': False,
    },
    {
        'id': 'SYS-09', 'number': 9, 'title': 'Media Studio', 'slug': 'media-studio',
        'purpose': 'Teach through multimedia.',
        'produces': ['Videos', 'Infographics', 'Podcasts', 'Presentations', 'Documentaries'],
        'consumes': ['Curriculum', 'Encyclopedia', 'Source Library', 'Research'],
        'route': '/mission-control/media-studio.html', 'registry': '/data/media-studio.json', 'build': 39,
        'status': 'partial', 'integration_pct': 16,
        'data_flow_live': False,
        'note': '0 videos — consumes not wired',
    },
    {
        'id': 'SYS-10', 'number': 10, 'title': 'Knowledge Graph', 'slug': 'knowledge-graph',
        'purpose': 'Connect everything — institutional nervous system.',
        'produces': ['Learning recommendations', 'Relationship maps', 'Topic navigation'],
        'consumes': ['Every other system'],
        'route': '/mission-control/civic-intelligence.html', 'registry': '/data/civic-intelligence.json', 'build': 40,
        'status': 'partial', 'integration_pct': 22,
        'data_flow_live': False,
        'note': '38 KG nodes — does not yet consume all systems',
    },
    {
        'id': 'SYS-11', 'number': 11, 'title': 'Mission Control', 'slug': 'mission-control',
        'purpose': 'Monitor institutional health — executive cockpit.',
        'produces': ['Progress dashboards', 'Readiness reports', 'Growth metrics', 'Executive reports'],
        'consumes': ['Every operational system'],
        'route': '/mission-control/', 'registry': '/data/mission-control.json', 'build': 25,
        'status': 'partial', 'integration_pct': 42,
        'data_flow_live': True,
        'note': '44 builds tracked — not all systems feed live metrics',
    },
    {
        'id': 'SYS-12', 'number': 12, 'title': 'Contact & Relationship Network', 'slug': 'contact-network',
        'purpose': 'Support community education.',
        'produces': ['Education Leaders', 'Coalition growth', 'Event participation', 'Community conversations'],
        'consumes': ['Website forms', 'Academy participation', 'Coalition sign-ons', 'Outreach campaigns'],
        'route': '/mission-control/contact-intelligence.html', 'registry': '/data/contact-intelligence.json', 'build': 24,
        'status': 'partial', 'integration_pct': 18,
        'data_flow_live': False,
        'note': '0 signups tracked — forms not integrated',
    },
]

INFORMATION_FLOW = [
    'Research', 'Evidence Verification', 'Educational Content', 'Media', 'Learning',
    'Community Education', 'Coalition Growth', 'Mission Control', 'Research Priorities', 'Research',
]

EXECUTIVE_QUESTIONS = [
    'Which topics need additional research?',
    'Which counties need Education Leaders?',
    'Which resources are most used?',
    'Which questions remain unanswered?',
    'Which coalition partners are most active?',
    'Which curriculum modules need updating?',
]

USER_JOURNEY = [
    'Visit Homepage', 'Learn Basic Concepts', 'Explore Timeline', 'Read Encyclopedia',
    'View Sources', 'Watch Documentary', 'Join Contact Network', 'Complete Academy',
    'Host Community Conversation', 'Join Coalition', 'Contribute Research', 'Mentor New Education Leaders',
]

INSTITUTIONAL_MEMORY = [
    'Research history', 'Editorial history', 'Build history', 'Coalition history',
    'Community education history', 'Mission Control reports', 'Resource revisions',
]

FUTURE_MODULES = [
    'Additional civic education topics', 'Expanded Arkansas educational initiatives',
    'New research collections', 'Enhanced multimedia experiences', 'Advanced AI assistance',
]

SYSTEMS_HEALTH = [
    {'id': 'SH-01', 'title': 'Research Health', 'status': 'partial', 'score': exec_e.get('research_readiness', 25)},
    {'id': 'SH-02', 'title': 'Evidence Health', 'status': 'partial', 'score': exec_e.get('evidence_ledger_readiness', 22)},
    {'id': 'SH-03', 'title': 'Content Health', 'status': 'partial', 'score': exec_e.get('content_readiness', 26)},
    {'id': 'SH-04', 'title': 'Curriculum Health', 'status': 'partial', 'score': exec_e.get('curriculum_readiness', 26)},
    {'id': 'SH-05', 'title': 'Media Health', 'status': 'partial', 'score': exec_e.get('media_studio_readiness', 18)},
    {'id': 'SH-06', 'title': 'Coalition Health', 'status': 'partial', 'score': exec_e.get('coalition_readiness', 18)},
    {'id': 'SH-07', 'title': 'County Health', 'status': 'partial', 'score': exec_e.get('county_os_readiness', 28)},
    {'id': 'SH-08', 'title': 'Academy Health', 'status': 'partial', 'score': exec_e.get('education_academy_readiness', 26)},
    {'id': 'SH-09', 'title': 'Outreach Health', 'status': 'partial', 'score': exec_e.get('outreach_readiness', 22)},
    {'id': 'SH-10', 'title': 'Technical Health', 'status': 'partial', 'score': exec_e.get('platform_architecture_readiness', 20)},
]

MC_METRICS = [
    {'id': 'SI-M01', 'title': 'Systems integrated (taxonomy)', 'status': 'partial', 'current': len(SYSTEMS)},
    {'id': 'SI-M02', 'title': 'Systems with live data flow', 'status': 'partial', 'current': sum(1 for s in SYSTEMS if s.get('data_flow_live'))},
    {'id': 'SI-M03', 'title': 'Avg system integration', 'status': 'partial', 'current': 0},
    {'id': 'SI-M04', 'title': 'Information flow stages defined', 'status': 'live', 'current': len(INFORMATION_FLOW)},
    {'id': 'SI-M05', 'title': 'Systems health indicators', 'status': 'partial', 'current': len(SYSTEMS_HEALTH)},
    {'id': 'SI-M06', 'title': 'Executive questions trackable', 'status': 'planned', 'current': 0},
    {'id': 'SI-M07', 'title': 'Cross-system event bus', 'status': 'planned', 'current': 0},
    {'id': 'SI-M08', 'title': 'Institutional memory archives', 'status': 'partial', 'current': exec_e.get('overall_completion', 44)},
]

systems_partial = sum(1 for s in SYSTEMS if s['status'] == 'partial')
data_flow_live = sum(1 for s in SYSTEMS if s.get('data_flow_live'))
avg_integration = round(sum(s['integration_pct'] for s in SYSTEMS) / len(SYSTEMS))

systems_integration_readiness = min(
    round(avg_integration * 0.35 + (data_flow_live / 12 * 100) * 0.2 + (systems_partial / 12 * 100) * 0.15 + 10),
    28,
)

MC_METRICS[2]['current'] = avg_integration

out = {
    'version': '1.0',
    'build': 45,
    'updated': today,
    'title': 'Master Systems Integration Blueprint v1.0',
    'subtitle': 'Institutional Operating Model',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/systems-integration.html',
    'constitution': '/docs/MASTER_SYSTEMS_INTEGRATION.md',
    'purpose': 'How does everything work together? — one integrated institution, not unrelated features.',
    'governing_principle': 'Integration of all systems — greater than the sum of its parts.',
    'long_term_vision': 'Every system continuously supports every other — research strengthens education, education strengthens communities.',
    'systems_total': len(SYSTEMS),
    'systems': SYSTEMS,
    'information_flow': INFORMATION_FLOW,
    'executive_intelligence': {
        'title': 'Executive Intelligence Layer',
        'host': '/mission-control/executive.html',
        'questions': EXECUTIVE_QUESTIONS,
        'status': 'partial',
        'synthesis_live': False,
    },
    'unified_user_journey': USER_JOURNEY,
    'institutional_memory': INSTITUTIONAL_MEMORY,
    'scalability': {
        'principle': 'Well-defined relationships enable clean future module integration.',
        'future_modules': FUTURE_MODULES,
    },
    'systems_health_dashboard': {
        'title': 'Systems Health',
        'status': 'partial',
        'indicators': SYSTEMS_HEALTH,
        'avg_health_score': round(sum(h['score'] for h in SYSTEMS_HEALTH) / len(SYSTEMS_HEALTH)),
    },
    'mc_integration': {
        'title': 'Mission Control Systems Integration Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'conductor_role': 'Mission Control orchestrates all twelve systems',
    },
    'related_blueprints': [
        {'title': 'Institutional Roadmap', 'route': '/data/institutional-roadmap.json', 'build': 44},
        {'title': 'Platform Architecture', 'route': '/data/platform-architecture.json', 'build': 20},
        {'title': 'Canonical Data Model', 'route': '/data/canonical-data-model.json', 'build': 15},
        {'title': 'Civic Intelligence', 'route': '/data/civic-intelligence.json', 'build': 40},
    ],
    'summary': {
        'systems_total': len(SYSTEMS),
        'systems_partial': systems_partial,
        'systems_with_live_data_flow': data_flow_live,
        'avg_system_integration_pct': avg_integration,
        'information_flow_stages': len(INFORMATION_FLOW),
        'systems_health_indicators': len(SYSTEMS_HEALTH),
        'avg_systems_health_score': round(sum(h['score'] for h in SYSTEMS_HEALTH) / len(SYSTEMS_HEALTH)),
        'executive_synthesis_live': False,
        'cross_system_event_bus': False,
        'systems_integration_readiness_pct': systems_integration_readiness,
    },
    'catalog_gaps': [
        'Only 3/12 systems have live cross-system data flow',
        'No event bus or API — JSON registries linked manually in MC',
        'Knowledge Graph does not yet consume all 11 other systems',
        'Executive intelligence questions unanswered automatically',
        'User journey defined — no progress tracking across stages',
        'Media Studio produces nothing — integration consume-only via halls',
        'Contact network at 0 signups — journey breaks at Academy step',
        'Systems Health scores from MC executive — not live operational feeds',
        'Institutional memory partial — build history only, not editorial/coalition',
        'Component specifications still deferred — UI integration unmapped',
    ],
    'recommended_next_build': {
        'number': 46,
        'title': 'Component Specifications with Props/States',
        'note': 'Map system health panels, information flow viz, journey progress widgets, and cross-system link components to COMP-* from Build #17.',
    },
}

path = root / 'data/systems-integration.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Systems Integration: {data_flow_live}/12 live flows, {systems_integration_readiness}% readiness')
