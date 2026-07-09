"""
Generate data/institutional-roadmap.json — Build #44 Master Institutional Roadmap v1.0.
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
exec_summary = mc.get('executive', {})
civic = mc.get('civic_action', {})

VERSIONS = [
    {
        'id': 'IR-V01', 'version': 1, 'slug': 'foundation', 'title': 'Foundation',
        'primary_goal': 'Launch a trustworthy educational platform.',
        'deliverables': [
            'Public website', 'Learning paths', 'Source Library', 'Mission Control',
            'Coalition sign-on', 'Education Leader signup', 'Contact Network',
            'Research Library', 'Community Education Academy',
        ],
        'success_measures': [
            'Platform operational', 'Core content published',
            'First Education Leaders enrolled', 'First coalition organizations participating',
        ],
        'status': 'partial', 'maturity_pct': 68,
        'current_phase': 'active',
        'routes': ['/mission-control/', '/library/', '/educate/', '/coalition/'],
        'builds_aligned': [1, 2, 4, 5, 8, 10, 13, 28, 37],
        'note': 'Platform live — content and enrollment partial',
    },
    {
        'id': 'IR-V02', 'version': 2, 'slug': 'arkansas-expansion', 'title': 'Arkansas Expansion',
        'primary_goal': 'Establish statewide educational presence.',
        'deliverables': [
            'County pages for all 75 counties', 'Regional outreach tools', 'Coalition growth',
            'Community conversations', 'Event calendar', 'Presentation toolkit expansion',
        ],
        'success_measures': [
            'Statewide county coverage', 'Active Education Leaders across multiple regions',
            'Growing coalition participation',
        ],
        'status': 'partial', 'maturity_pct': 28,
        'current_phase': 'early',
        'routes': ['/mission-control/county-os.html', '/mission-control/outreach.html', '/coalition/'],
        'builds_aligned': [30, 31],
        'note': '75 county profiles scaffolded — 0 county participation tracked',
    },
    {
        'id': 'IR-V03', 'version': 3, 'slug': 'research-institution', 'title': 'Research Institution',
        'primary_goal': 'Strengthen scholarship and transparency.',
        'deliverables': [
            'Expanded encyclopedia', 'Evidence Ledger growth', 'Claims Registry',
            'Additional primary sources', 'Comparative state studies', 'Enhanced Research Observatory',
        ],
        'success_measures': [
            'Research completeness', 'Citation quality', 'Public trust indicators',
        ],
        'status': 'partial', 'maturity_pct': 30,
        'current_phase': 'early',
        'routes': ['/mission-control/research-methodology.html', '/mission-control/evidence-ledger.html',
                   '/mission-control/encyclopedia.html', '/mission-control/research-observatory.html'],
        'builds_aligned': [10, 11, 29, 33, 36, 41, 43],
        'note': '14 EV-* items, 3 CLAIM-* — far from research completeness',
    },
    {
        'id': 'IR-V04', 'version': 4, 'slug': 'interactive-learning', 'title': 'Interactive Learning',
        'primary_goal': 'Transform learning through exploration.',
        'deliverables': [
            'Knowledge Graph', 'Interactive laboratories', 'Visual data explorer',
            'Constitutional explorer', 'Timeline explorer', 'Guided learning experiences',
        ],
        'success_measures': [
            'Learning engagement', 'Curriculum completion', 'Educational effectiveness',
        ],
        'status': 'partial', 'maturity_pct': 16,
        'current_phase': 'architecture',
        'routes': ['/mission-control/learning-lab.html', '/mission-control/knowledge-graph.html',
                   '/mission-control/civic-intelligence.html'],
        'builds_aligned': [11, 38, 40],
        'note': '0/10 true interactive experiences — architecture only',
    },
    {
        'id': 'IR-V05', 'version': 5, 'slug': 'community-education', 'title': 'Community Education',
        'primary_goal': "Build Arkansas's civic education network.",
        'deliverables': [
            'Expanded Community Education Academy', 'County Education Teams', 'Coalition development',
            'Community conversation program', 'Volunteer coordination',
        ],
        'success_measures': [
            'Community events', 'Education Leaders', 'Coalition partnerships', 'County participation',
        ],
        'status': 'partial', 'maturity_pct': 22,
        'current_phase': 'architecture',
        'routes': ['/mission-control/education-academy.html', '/mission-control/civic-ecosystem.html', '/coalition/'],
        'builds_aligned': [12, 28],
        'note': '0 education leader signups — forms not integrated',
    },
    {
        'id': 'IR-V06', 'version': 6, 'slug': 'multimedia-institution', 'title': 'Multimedia Institution',
        'primary_goal': 'Develop a comprehensive educational media library.',
        'deliverables': [
            'Documentary series', 'Video library', 'Audio lessons',
            'Interactive presentations', 'Downloadable teaching resources',
        ],
        'success_measures': [
            'Media usage', 'Classroom adoption', 'Community presentation support',
        ],
        'status': 'partial', 'maturity_pct': 14,
        'current_phase': 'architecture',
        'routes': ['/mission-control/media-studio.html'],
        'builds_aligned': [39],
        'note': '0 videos published — media taxonomy only',
    },
    {
        'id': 'IR-V07', 'version': 7, 'slug': 'institutional-intelligence', 'title': 'Institutional Intelligence',
        'primary_goal': 'Strengthen knowledge management.',
        'deliverables': [
            'AI educational guide', 'Intelligent search', 'Personalized learning recommendations',
            'Knowledge gap detection', 'Mission Control intelligence',
        ],
        'success_measures': [
            'Improved navigation', 'Faster discovery', 'Research efficiency',
        ],
        'status': 'partial', 'maturity_pct': 18,
        'current_phase': 'architecture',
        'routes': ['/mission-control/ai-knowledge.html', '/mission-control/civic-intelligence.html',
                   '/mission-control/executive.html'],
        'builds_aligned': [25, 26, 40],
        'note': 'AI engine planned — question engine not live; human review required',
    },
    {
        'id': 'IR-V08', 'version': 8, 'slug': 'educational-partnerships', 'title': 'Educational Partnerships',
        'primary_goal': 'Expand collaboration throughout Arkansas.',
        'deliverables': [
            'Library partnerships', 'Educational institution partnerships', 'Civic organization partnerships',
            'Professional association partnerships', 'Expanded coalition resources',
        ],
        'success_measures': [
            'Partnership growth', 'Resource adoption', 'Community reach',
        ],
        'status': 'planned', 'maturity_pct': 6,
        'current_phase': 'planned',
        'routes': ['/coalition/'],
        'builds_aligned': [13, 14],
        'note': 'Coalition scaffold — no formal partnership registry',
    },
    {
        'id': 'IR-V09', 'version': 9, 'slug': 'institutional-excellence', 'title': 'Institutional Excellence',
        'primary_goal': 'Refine every system.',
        'deliverables': [
            'Accessibility improvements', 'Editorial refinements', 'Technical modernization',
            'Research modernization', 'Archive expansion',
        ],
        'success_measures': [
            'Platform quality', 'Accessibility compliance', 'User satisfaction', 'Institutional sustainability',
        ],
        'status': 'planned', 'maturity_pct': 10,
        'current_phase': 'planned',
        'routes': ['/mission-control/trust.html', '/design-system/'],
        'builds_aligned': [9, 36],
        'note': 'Trust framework + design system — accessibility not verified per feature',
    },
    {
        'id': 'IR-V10', 'version': 10, 'slug': 'permanent-institution', 'title': 'Permanent Civic Institution',
        'primary_goal': 'Operate as a mature public civic education institution.',
        'deliverables': [
            'Fully integrated Knowledge Graph', 'Comprehensive Research Library', 'Complete curriculum',
            'Statewide Education Network', 'Mature Mission Control', 'Long-term governance framework',
        ],
        'success_measures': [
            'Public trust', 'Educational impact', 'Research quality',
            'Coalition stability', 'Institutional continuity',
        ],
        'status': 'planned', 'maturity_pct': 5,
        'current_phase': 'vision',
        'routes': [],
        'builds_aligned': [],
        'note': 'Long-term aspiration — all prior versions must mature first',
    },
]

CROSS_VERSION_PRIORITIES = [
    'Research', 'Education', 'Technology', 'Accessibility', 'Transparency',
    'Coalition development', 'Community education', 'Mission Control',
]

ANNUAL_REVIEW_AREAS = [
    'Educational progress', 'Research quality', 'Coalition development',
    'County participation', 'Technology health', 'User feedback', 'Emerging legal developments',
]

PRESERVATION_STRATEGY = [
    'Research history', 'Build history', 'Editorial history', 'Major decisions',
    'Version milestones', 'Educational resources', 'Source archives',
]

SUSTAINABILITY_PLANNING = [
    'Leadership succession', 'Documentation', 'Editorial governance',
    'Technology maintenance', 'Research continuity', 'Community partnerships',
]

INSTITUTIONAL_VISION = [
    "Arkansas's definitive educational resource on Citizens United",
    'Trusted public archive of campaign finance history',
    'Statewide network of civic educators',
    'Research institution grounded in transparent evidence',
    'Model for explaining complex constitutional issues to the public',
]

MC_METRICS = [
    {'id': 'IR-M01', 'title': 'Institutional maturity (overall)', 'status': 'partial', 'current': 0},
    {'id': 'IR-M02', 'title': 'Current institutional version', 'status': 'partial', 'current': 'V1→V2'},
    {'id': 'IR-M03', 'title': 'Software builds complete', 'status': 'partial', 'current': 44},
    {'id': 'IR-M04', 'title': 'Versions partial or better', 'status': 'partial', 'current': 0},
    {'id': 'IR-M05', 'title': 'Education Leaders enrolled', 'status': 'partial', 'current': civic.get('education_leader_signups', 0)},
    {'id': 'IR-M06', 'title': 'Counties with participation', 'status': 'partial', 'current': civic.get('counties', 0)},
    {'id': 'IR-M07', 'title': 'Annual review completed', 'status': 'planned', 'current': 0},
    {'id': 'IR-M08', 'title': 'Preservation milestones logged', 'status': 'partial', 'current': 44},
]

versions_partial = sum(1 for v in VERSIONS if v['status'] == 'partial')
avg_maturity = round(sum(v['maturity_pct'] for v in VERSIONS) / len(VERSIONS))

# Weight V1 higher for current position — institution is in Foundation completing, early V2
institutional_maturity_pct = min(
    round(VERSIONS[0]['maturity_pct'] * 0.35 + avg_maturity * 0.25 + (versions_partial / 10 * 100) * 0.15 + 8),
    32,
)

MC_METRICS[0]['current'] = institutional_maturity_pct
MC_METRICS[3]['current'] = versions_partial

out = {
    'version': '1.0',
    'build': 44,
    'updated': today,
    'title': 'Master Institutional Roadmap v1.0',
    'subtitle': 'Version 1 Through Version 10 Strategic Evolution Plan',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/institutional-roadmap.html',
    'constitution': '/docs/MASTER_INSTITUTIONAL_ROADMAP.md',
    'purpose': 'Measure institutional maturity — not merely software completion.',
    'institutional_vision': INSTITUTIONAL_VISION,
    'governing_principle': 'Outlast election cycles — institution first, technology serves the mission.',
    'success_definition': 'An Arkansan can explore evidence, understand context, discover perspectives, and find civic education opportunities in their community.',
    'current_institutional_version': 'V1',
    'current_institutional_phase': 'Foundation completing — early Arkansas Expansion',
    'next_institutional_version': 'V2',
    'software_build': 44,
    'software_version': '1.48.0',
    'versions': VERSIONS,
    'cross_version_priorities': CROSS_VERSION_PRIORITIES,
    'annual_strategic_review': ANNUAL_REVIEW_AREAS,
    'preservation_strategy': PRESERVATION_STRATEGY,
    'sustainability_planning': SUSTAINABILITY_PLANNING,
    'mc_integration': {
        'title': 'Mission Control Institutional Maturity Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'annual_review_live': False,
    },
    'related_systems': [
        {'title': 'Educational Campaign OS', 'route': '/data/educational-campaign-operating-system.json', 'build': 32},
        {'title': 'BUILD_PLAN', 'route': '/BUILD_PLAN.md'},
        {'title': 'Phase Registry', 'route': '/mission-control/phases.html', 'build': 4},
        {'title': 'Executive Command Center', 'route': '/mission-control/executive.html', 'build': 25},
    ],
    'summary': {
        'institutional_versions_total': len(VERSIONS),
        'versions_partial': versions_partial,
        'versions_planned': sum(1 for v in VERSIONS if v['status'] == 'planned'),
        'avg_version_maturity_pct': avg_maturity,
        'current_institutional_version': 'V1',
        'next_institutional_version': 'V2',
        'v1_maturity_pct': VERSIONS[0]['maturity_pct'],
        'v10_maturity_pct': VERSIONS[9]['maturity_pct'],
        'software_builds_complete': 44,
        'institutional_maturity_pct': institutional_maturity_pct,
        'annual_review_live': False,
        'governance_framework_live': False,
    },
    'catalog_gaps': [
        'Institutional maturity 32% max — software builds ≠ institutional maturity',
        'V1 Foundation 68% — content, leaders, coalition enrollment incomplete',
        'V2 at 28% — 0 counties with tracked participation',
        'V3–V7 architecture-heavy — deliverables scaffolded, not operational',
        'V8–V10 planned — partnerships, excellence, permanence not started',
        'Annual strategic review process not built in MC',
        'No governance/succession framework — sustainability planning only',
        '44 software builds vs V1 success measures — honest gap documented',
        'Component specifications still deferred — UI shells unmapped',
        'Public launch readiness 8% — early foundation only',
    ],
    'recommended_next_build': {
        'number': 45,
        'title': 'Component Specifications with Props/States',
        'note': 'Map version milestone panels, maturity dashboards, annual review workflows, and preservation archives to COMP-* from Build #17.',
    },
}

path = root / 'data/institutional-roadmap.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Institutional Roadmap: V1 at {VERSIONS[0]["maturity_pct"]}%, {institutional_maturity_pct}% overall maturity')
