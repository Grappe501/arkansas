import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with open(root / 'data/mission-control.json') as f:
    mc = json.load(f)

title = 'Citizens United Facts Documentary Experience & Media Studio'

with open(root / 'data/media-studio.json') as f:
    media = json.load(f)

s = media['summary']

mc['version'] = '1.43.0'
mc['build'] = 39
mc['updated'] = '2026-07-09'
mc['media_studio'] = '/data/media-studio.json'
mc['media_studio_dashboard'] = '/mission-control/media-studio.html'

mc['executive'] = {
    'overall_completion': 39,
    'current_build': {'number': 39, 'title': title},
    'active_phase': 'Multimedia Learning — Documentary Experience & Media Studio',
    'last_completed': 'Interactive Learning Laboratory',
    'next_build': {'number': 40, 'title': 'Component specifications with props/states'},
    'github_status': 'connected',
    'netlify_status': 'production_healthy',
    'content_readiness': 26,
    'research_readiness': 28,
    'data_viz_readiness': 6,
    'signup_funnel_readiness': 22,
    'civic_action_readiness': 32,
    'coalition_readiness': 18,
    'data_model_readiness': 38,
    'route_inventory_readiness': 18,
    'component_registry_readiness': 22,
    'facts_framework_readiness': 14,
    'knowledge_atlas_readiness': 20,
    'platform_architecture_readiness': 20,
    'repository_structure_readiness': 28,
    'database_schema_readiness': 36,
    'wireframe_readiness': 38,
    'contact_intelligence_readiness': 31,
    'mc2_readiness': 33,
    'ai_engine_readiness': 14,
    'content_factory_readiness': 28,
    'education_academy_readiness': 26,
    'observatory_readiness': 20,
    'outreach_readiness': 22,
    'county_os_readiness': 28,
    'campaign_os_readiness': 34,
    'encyclopedia_readiness': 19,
    'narrative_readiness': 24,
    'curriculum_readiness': 26,
    'trust_readiness': 24,
    'library_readiness': 22,
    'learning_lab_readiness': 22,
    'media_studio_readiness': s['media_studio_readiness_pct'],
    'public_launch_readiness': 8,
    'public_launch_label': 'Early Foundation'
}

mc['media_studio_inventory'] = {
    'readiness_score': s['media_studio_readiness_pct'],
    'divisions_total': s['divisions_total'],
    'divisions_partial': s['divisions_partial'],
    'videos_published': s['videos_published'],
    'chapters_with_video': s['chapters_with_video'],
    'avg_division_readiness_pct': s['avg_division_readiness_pct'],
    'engagement_tracking_live': s['engagement_tracking_live'],
}

for bar in mc['progress_bars']:
    if bar['id'] == 'overall':
        bar['value'] = 39
        bar['note'] = f"Media Studio live — 8 divisions, {s['videos_published']} videos published."
    if bar['id'] == 'learning_lab':
        bar['value'] = 22
        bar['note'] = 'Learning Lab architecture — 0 interactive experiences deployed.'

if not any(b.get('id') == 'media_studio' for b in mc['progress_bars']):
    mc['progress_bars'].append({
        'id': 'media_studio',
        'label': 'Documentary Experience & Media Studio',
        'value': s['media_studio_readiness_pct'],
        'max': 100,
        'note': f"{s['divisions_partial']}/8 divisions partial — 0 videos published."
    })
else:
    for bar in mc['progress_bars']:
        if bar['id'] == 'media_studio':
            bar['value'] = s['media_studio_readiness_pct']
            bar['note'] = f"{s['divisions_partial']}/8 divisions partial — 0 videos published."

mc['builds'].insert(0, {
    'number': 39,
    'title': title,
    'version': '1.43.0',
    'status': 'complete',
    'started': '2026-07-09',
    'completed': '2026-07-09',
    'purpose': 'Multimedia Learning Architecture v1.0 — documentary experience as educational pillar',
    'summary': f"8 divisions, 6 documentary chapters, avg {s['avg_division_readiness_pct']}% division readiness; {s['media_studio_readiness_pct']}% overall.",
    'files_created': [
        'data/media-studio.json', 'docs/DOCUMENTARY_EXPERIENCE_MEDIA_STUDIO.md',
        'builds/039-documentary-experience-media-studio.md', 'mission-control/media-studio.html',
        'scripts/gen-media-studio.py', 'scripts/update-mc-build39.py'
    ],
    'files_modified': ['js/mission-control.js', 'data/site.json', 'BUILD_PLAN.md', 'netlify.toml'],
    'pages_created': ['/mission-control/media-studio.html'],
    'decisions_made': [
        '8 media divisions — documentary through classroom resources',
        '6 documentary chapters aligned to narrative acts',
        '7 media standards + 5 accessibility requirements per asset',
        'Halls/educate/narrative as interim — 0 videos published',
        'Presentation toolkit on educate/ — no packet generator',
        f"{s['media_studio_readiness_pct']}% honest readiness — architecture only"
    ],
    'open_questions': ['First documentary chapter to produce?', 'Video hosting platform?', 'Infographic download library?'],
    'risks': ['0 videos published', 'No transcript/caption workflow', 'Engagement not tracked'],
    'next_recommended': 40,
    'branch': 'main',
    'git_commit': 'pending',
    'netlify_deploy': 'https://arkansas-facts.netlify.app/mission-control/media-studio.html',
    'review_status': 'complete'
})

mc['briefing'] = {
    'what_built': 'Media Studio v1.0 — 8 divisions, 6 documentary chapters, media standards, MC metrics',
    'building_now': 'Multimedia architecture — halls and educate as interim static media',
    'blocked': ['No video production', 'Transcript/caption workflow', 'Media engagement tracking'],
    'ready_public': ['Media Studio MC dashboard', '8-division taxonomy', 'Documentary chapter mapping'],
    'next': 'Build #40 — Component specifications with props/states'
}

if not any(n.get('id') == 'media_studio' for n in mc['build_map']):
    mc['build_map'].append({
        'id': 'media_studio', 'label': 'Documentary Experience & Media Studio', 'href': '/mission-control/media-studio.html', 'status': 'complete'
    })

with open(root / 'data/mission-control.json', 'w', newline='\n') as f:
    json.dump(mc, f, indent=2)
    f.write('\n')
print('done')
