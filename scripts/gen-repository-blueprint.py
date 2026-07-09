"""
Generate data/repository-blueprint.json — Build #21 Repository Architecture v1.0.
Maps target structure to current v0 flat layout honestly.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

workstreams = [
    {'id': 'education', 'title': 'Public education website', 'current_paths': ['/', 'halls/', 'explore/', 'start-here/'], 'status': 'live'},
    {'id': 'mission_control', 'title': 'Mission Control dashboard', 'current_paths': ['mission-control/', 'data/mission-control.json'], 'status': 'live'},
    {'id': 'civic', 'title': 'Arkansas civic action and coalition tools', 'current_paths': ['action/', 'educate/', 'coalition/', 'arkansas/', 'join/'], 'status': 'partial'},
    {'id': 'research', 'title': 'Research/source library', 'current_paths': ['library/', 'data/evidence-registry.json', 'docs/RESEARCH_CONSTITUTION.md'], 'status': 'partial'},
]

branches = [
    {'name': 'main', 'purpose': 'Production branch — deploys to live Netlify site', 'status': 'live'},
    {'name': 'develop', 'purpose': 'Working integration branch — Netlify preview', 'status': 'recommended'},
    {'name': 'feature/*', 'purpose': 'Individual feature branches', 'examples': ['feature/mission-control', 'feature/floating-action-hub', 'feature/source-library', 'feature/coalition-signup'], 'status': 'recommended'},
    {'name': 'content/*', 'purpose': 'Content-only branches', 'examples': ['content/history-section', 'content/case-overview', 'content/spending-data'], 'status': 'recommended'},
]

target_root = [
    'README.md', 'CONTRIBUTING.md', 'netlify.toml', 'package.json', '.gitignore', '.env.example',
    'docs/', 'src/', 'public/', 'scripts/', 'tests/'
]

docs_folders = [
    {'path': 'docs/build-plan/', 'purpose': 'Numbered build documents', 'target_examples': ['BUILD_001_MISSION_STATEMENT.md', 'BUILD_020_PLATFORM_ARCHITECTURE.md'], 'current_mapping': 'builds/*.md', 'status': 'partial'},
    {'path': 'docs/governance/', 'purpose': 'Project-wide governing standards', 'target_examples': ['PROJECT_CONSTITUTION.md', 'EDITORIAL_STANDARDS.md', 'CITATION_POLICY.md', 'BRAND_GUIDE.md'], 'current_mapping': 'docs/CONSTITUTION.md, builds/002-project-constitution.md', 'status': 'partial'},
    {'path': 'docs/research-standards/', 'purpose': 'Research and evidence rules', 'target_examples': ['RESEARCH_CONSTITUTION.md', 'FACT_FRAMEWORK.md', 'SOURCE_TIERS.md'], 'current_mapping': 'docs/RESEARCH_CONSTITUTION.md, docs/FACTS_CONSTITUTION.md', 'status': 'partial'},
    {'path': 'docs/deployment/', 'purpose': 'GitHub and Netlify instructions', 'target_examples': ['NETLIFY_SETUP.md', 'GITHUB_WORKFLOW.md', 'ENVIRONMENT_VARIABLES.md'], 'current_mapping': 'netlify.toml, CONTRIBUTING.md', 'status': 'planned'},
    {'path': 'docs/mission-control/', 'purpose': 'MC structure and dashboard rules', 'target_examples': ['MISSION_CONTROL_SPEC.md', 'PROGRESS_MODEL.md'], 'current_mapping': 'data/mission-control.json, mission-control/', 'status': 'partial'},
]

src_folders = [
    {'path': 'src/app/', 'purpose': 'Route-level application pages', 'target_examples': ['start-here/', 'the-case/', 'mission-control/'], 'current_mapping': 'halls/, explore/, start-here/, mission-control/ at root', 'status': 'planned'},
    {'path': 'src/components/', 'purpose': 'Reusable UI components', 'target_subdirs': ['navigation', 'education', 'data', 'civic-action', 'coalition', 'mission-control', 'trust', 'layout'], 'current_mapping': 'js/layout.js, css/components.css, design-system/', 'status': 'planned'},
    {'path': 'src/content/', 'purpose': 'Educational content files', 'target_subdirs': ['story', 'case', 'impact', 'debate', 'solutions', 'arkansas', 'coalition'], 'current_mapping': 'content/entries/, halls/*.html inline', 'status': 'planned'},
    {'path': 'src/data/', 'purpose': 'Structured JSON/TS data', 'target_subdirs': ['mission-control', 'fact-registry', 'route-registry', 'coalition', 'counties'], 'current_mapping': 'data/*.json at repository root', 'status': 'partial'},
    {'path': 'src/lib/', 'purpose': 'Shared logic', 'target_subdirs': ['mission-control', 'citations', 'forms', 'search', 'validation'], 'current_mapping': 'js/*.js at repository root', 'status': 'planned'},
    {'path': 'src/styles/', 'purpose': 'Global styling and tokens', 'target_examples': ['globals.css', 'tokens.css', 'typography.css'], 'current_mapping': 'css/*.css at repository root', 'status': 'planned'},
    {'path': 'src/types/', 'purpose': 'Shared TypeScript types', 'target_examples': ['content.ts', 'mission-control.ts', 'coalition.ts'], 'current_mapping': 'None — no TypeScript yet', 'status': 'planned'},
]

public_folders = [
    {'path': 'public/images/', 'purpose': 'Public images and graphics', 'status': 'planned'},
    {'path': 'public/downloads/', 'purpose': 'PDFs, handouts, guides', 'status': 'planned'},
    {'path': 'public/source-documents/', 'purpose': 'Shareable source documents', 'status': 'planned'},
]

target_scripts = [
    {'name': 'validate-content.mjs', 'purpose': 'Content metadata, MRIDs, reading levels', 'current_equivalent': None, 'status': 'planned'},
    {'name': 'validate-sources.mjs', 'purpose': 'Citation completeness and source IDs', 'current_equivalent': None, 'status': 'planned'},
    {'name': 'generate-mission-control.mjs', 'purpose': 'Build MC data from registries', 'current_equivalent': 'scripts/update-mc-build*.py', 'status': 'partial'},
    {'name': 'build-route-registry.mjs', 'purpose': 'Route inventory and missing pages', 'current_equivalent': 'scripts/gen-route-registry.py', 'status': 'partial'},
]

package_scripts_target = {
    'dev': 'next dev',
    'build': 'next build',
    'check': 'npm run lint && npm run typecheck',
    'typecheck': 'tsc --noEmit',
    'lint': 'next lint',
    'mission-control': 'node scripts/generate-mission-control.mjs',
    'content:validate': 'node scripts/validate-content.mjs',
    'sources:validate': 'node scripts/validate-sources.mjs',
    'routes:validate': 'node scripts/build-route-registry.mjs'
}

package_scripts_current = {
    'start': 'npx --yes serve . -l 8080'
}

netlify_target = {
    'command': 'npm run build',
    'publish': '.next',
    'node_version': '20'
}

netlify_current = {
    'command': "echo 'Static site — no build step'",
    'publish': '.',
    'note': 'Static HTML deploy — 80+ redirects in netlify.toml'
}

github_labels = [
    'governance', 'content', 'research', 'design', 'frontend', 'mission-control',
    'forms', 'coalition', 'data', 'accessibility', 'deployment', 'bug', 'blocked', 'review-needed'
]

github_milestones = [
    {'number': 1, 'title': 'Foundation', 'status': 'complete'},
    {'number': 2, 'title': 'Mission Control v1', 'status': 'complete'},
    {'number': 3, 'title': 'Public Education Core', 'status': 'partial'},
    {'number': 4, 'title': 'Source Library v1', 'status': 'partial'},
    {'number': 5, 'title': 'Arkansas Civic Action Layer', 'status': 'partial'},
    {'number': 6, 'title': 'Coalition Layer', 'status': 'partial'},
    {'number': 7, 'title': 'Netlify Launch', 'status': 'complete'},
    {'number': 8, 'title': 'Public Beta', 'status': 'planned'},
    {'number': 9, 'title': 'Full Version 1', 'status': 'planned'},
]

current_layout = {
    'pattern': 'flat_static_v0',
    'description': 'Static HTML site with registries at repository root — no src/ framework',
    'root_folders': [
        'action', 'admin', 'arkansas', 'builds', 'coalition', 'content', 'css', 'data',
        'design-system', 'docs', 'educate', 'explore', 'halls', 'join', 'js', 'library',
        'mission-control', 'scripts', 'solutions', 'start-here', '.github'
    ],
    'data_location': 'data/',
    'scripts_language': 'python',
    'script_count': 15,
    'has_src': False,
    'has_tests': False,
    'has_env_example': True,
}

migration_map = [
    {'from': 'builds/', 'to': 'docs/build-plan/', 'status': 'planned'},
    {'from': 'data/', 'to': 'src/data/', 'status': 'planned'},
    {'from': 'js/', 'to': 'src/lib/', 'status': 'planned'},
    {'from': 'css/', 'to': 'src/styles/', 'status': 'planned'},
    {'from': 'halls/, mission-control/, etc.', 'to': 'src/app/', 'status': 'planned'},
    {'from': 'scripts/*.py', 'to': 'scripts/*.mjs', 'status': 'planned'},
]

planned = sum(1 for d in docs_folders if d['status'] == 'planned') + sum(1 for s in src_folders if s['status'] == 'planned')
partial = sum(1 for d in docs_folders if d['status'] == 'partial') + sum(1 for s in src_folders if s['status'] == 'partial')

out = {
    'version': '1.0',
    'build': 21,
    'updated': today,
    'title': 'GitHub Repository & Folder Structure Blueprint v1.0',
    'route': '/mission-control/repository.html',
    'constitution': '/docs/REPOSITORY_ARCHITECTURE.md',
    'philosophy': 'The repository itself should teach the project.',
    'governing_principle': 'A new contributor should immediately understand what the project is, where everything lives, and what is safe to edit.',
    'repository_names': {
        'recommended': 'citizens-united-facts',
        'alternative': 'citizens-united-education-platform',
        'current_remote': 'Grappe501/arkansas',
        'current_local': 'arkansas-citizens-facts',
        'rename_status': 'optional'
    },
    'workstreams': workstreams,
    'branch_structure': branches,
    'target_root_structure': target_root,
    'current_layout': current_layout,
    'docs_folders': docs_folders,
    'src_folders': src_folders,
    'public_folders': public_folders,
    'target_scripts': target_scripts,
    'package_scripts': {
        'target': package_scripts_target,
        'current': package_scripts_current,
        'status': 'planned'
    },
    'netlify': {
        'target': netlify_target,
        'current': netlify_current
    },
    'environment_variables': {
        'file': '.env.example',
        'variables': [
            'NEXT_PUBLIC_SITE_URL',
            'NEXT_PUBLIC_SITE_NAME',
            'CONTACT_NOTIFICATION_EMAIL',
            'NETLIFY_FORMS_ENABLED'
        ],
        'status': 'live'
    },
    'github_labels': github_labels,
    'github_milestones': github_milestones,
    'migration_map': migration_map,
    'summary': {
        'workstreams': len(workstreams),
        'workstreams_live': sum(1 for w in workstreams if w['status'] == 'live'),
        'target_docs_folders': len(docs_folders),
        'target_src_folders': len(src_folders),
        'target_scripts': len(target_scripts),
        'folders_planned': planned,
        'folders_partial': partial,
        'migration_executed': False,
        'structure_readiness_pct': 28,
        'note': 'Blueprint defined — physical migration to src/ not yet executed'
    },
    'integrations': [
        {'system': 'Platform Architecture', 'build': 20, 'route': '/mission-control/platform.html'},
        {'system': 'Route Registry', 'build': 16, 'route': '/mission-control/routes.html'},
        {'system': 'Component Registry', 'build': 17, 'route': '/mission-control/components.html'},
    ],
    'catalog_gaps': [
        'No src/ directory — flat v0 layout',
        'No tests/ directory',
        'Python scripts instead of target .mjs validators',
        'docs/ not organized into build-plan, governance, deployment subfolders',
        'GitHub labels and milestones not yet created in remote',
        'develop branch not yet standard workflow',
    ],
    'recommended_next_build': {
        'number': 22,
        'title': 'Database schema and entity-relationship model',
        'note': 'ERD before framework migration.'
    },
}

path = root / 'data/repository-blueprint.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Repository blueprint: {out["summary"]["structure_readiness_pct"]}% — migration not executed')
