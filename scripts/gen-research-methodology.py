"""
Generate data/research-methodology.json — Build #43 Master Research Methodology & Standards Manual v1.0.
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


rf = load_json(root / 'data/research-framework.json')
ev = load_json(root / 'data/evidence-registry.json')
ledger = load_json(root / 'data/evidence-ledger.json')
obs = load_json(root / 'data/research-observatory.json')

ev_summary = ev.get('summary', {})
ledger_summary = ledger.get('summary', {})
rf_philosophy = rf.get('philosophy', [])

PRINCIPLES = [
    {
        'id': 'RM-P01', 'number': 1, 'title': 'Primary Sources First',
        'description': 'Begin with original materials — opinions, statutes, constitutional text, government reports, official data.',
        'examples': ['Supreme Court opinions', 'Court filings', 'Federal statutes', 'Arkansas statutes',
                     'Constitutional text', 'Government reports', 'Official election data'],
        'status': 'live', 'readiness_pct': 32,
        'legacy_id': 'primary-first', 'in_build_10': True,
    },
    {
        'id': 'RM-P02', 'number': 2, 'title': 'Transparency',
        'description': 'Readers identify origin, publication date, producer, and verification method.',
        'status': 'partial', 'readiness_pct': 28,
        'legacy_id': 'transparency', 'in_build_10': True,
    },
    {
        'id': 'RM-P03', 'number': 3, 'title': 'Distinguish Facts from Interpretation',
        'description': 'Separate documented facts, holdings, interpretation, analysis, proposals, and debated questions.',
        'status': 'partial', 'readiness_pct': 26,
        'legacy_id': 'fact-vs-interpretation', 'in_build_10': True,
    },
    {
        'id': 'RM-P04', 'number': 4, 'title': 'Multiple Reliable Sources',
        'description': 'Important claims supported by more than one reliable source when feasible.',
        'status': 'partial', 'readiness_pct': 22,
        'legacy_id': 'multiple-sources', 'in_build_10': True,
    },
    {
        'id': 'RM-P05', 'number': 5, 'title': 'Historical Context',
        'description': 'Explain before, after, why it mattered, and connections to other developments.',
        'status': 'partial', 'readiness_pct': 24,
        'legacy_id': None, 'in_build_10': False,
    },
    {
        'id': 'RM-P06', 'number': 6, 'title': 'Plain Language',
        'description': 'Complex legal topics in citizen-accessible language without sacrificing accuracy.',
        'status': 'partial', 'readiness_pct': 30,
        'legacy_id': None, 'in_build_10': False,
    },
    {
        'id': 'RM-P07', 'number': 7, 'title': 'Continuous Review',
        'description': 'Published review schedules — MC identifies resources requiring updates.',
        'status': 'planned', 'readiness_pct': 12,
        'legacy_id': 'continuous-review', 'in_build_10': True,
    },
    {
        'id': 'RM-P08', 'number': 8, 'title': 'Intellectual Humility',
        'description': 'Acknowledge incomplete, conflicting, or uncertain evidence.',
        'status': 'partial', 'readiness_pct': 20,
        'legacy_id': None, 'in_build_10': False,
    },
    {
        'id': 'RM-P09', 'number': 9, 'title': 'Educational Neutrality',
        'description': 'Explain competing interpretations without presenting contested questions as settled.',
        'status': 'partial', 'readiness_pct': 28,
        'legacy_id': None, 'in_build_10': False,
    },
    {
        'id': 'RM-P10', 'number': 10, 'title': 'Documentation',
        'description': 'Documented trail for source selection, exclusion, and revision decisions.',
        'status': 'planned', 'readiness_pct': 14,
        'legacy_id': None, 'in_build_10': False,
    },
]

RESEARCH_WORKFLOW = [
    {'id': 'RW-01', 'stage': 1, 'title': 'Topic identified', 'status': 'partial'},
    {'id': 'RW-02', 'stage': 2, 'title': 'Research plan prepared', 'status': 'planned'},
    {'id': 'RW-03', 'stage': 3, 'title': 'Primary sources collected', 'status': 'partial'},
    {'id': 'RW-04', 'stage': 4, 'title': 'Secondary sources reviewed', 'status': 'partial'},
    {'id': 'RW-05', 'stage': 5, 'title': 'Evidence evaluated', 'status': 'partial'},
    {'id': 'RW-06', 'stage': 6, 'title': 'Educational outline created', 'status': 'planned'},
    {'id': 'RW-07', 'stage': 7, 'title': 'Draft prepared', 'status': 'partial'},
    {'id': 'RW-08', 'stage': 8, 'title': 'Fact verification completed', 'status': 'partial'},
    {'id': 'RW-09', 'stage': 9, 'title': 'Editorial review completed', 'status': 'partial'},
    {'id': 'RW-10', 'stage': 10, 'title': 'Published', 'status': 'partial'},
    {'id': 'RW-11', 'stage': 11, 'title': 'Scheduled for future review', 'status': 'planned'},
]

SOURCE_EVALUATION_CHECKLIST = [
    'Authority', 'Authenticity', 'Publication date', 'Relevance', 'Completeness', 'Potential limitations',
]

CITATION_STANDARDS = [
    'Primary legal authority', 'Government publications', 'Academic scholarship',
    'Historical materials', 'Public datasets',
]

RESEARCH_DOCUMENTATION = [
    'Research plan', 'Source inventory', 'Claims ledger', 'Review notes', 'Publication record', 'Revision history',
]

QUALITY_ASSURANCE = [
    'Factual accuracy', 'Citation completeness', 'Contextual accuracy',
    'Plain-language clarity', 'Internal consistency', 'Accessibility',
]

INSTITUTIONAL_RESPONSIBILITY = [
    'Careful documentation', 'Honest revision', 'Transparent sourcing',
    'Respect for evidence', 'Willingness to correct mistakes',
]

MC_METRICS = [
    {'id': 'RM-M01', 'title': 'Research projects underway', 'status': 'planned', 'current': 0},
    {'id': 'RM-M02', 'title': 'Sources reviewed', 'status': 'partial', 'current': ev_summary.get('total', 0), 'target': 500},
    {'id': 'RM-M03', 'title': 'Claims verified', 'status': 'partial', 'current': ledger_summary.get('claims_verified', 0)},
    {'id': 'RM-M04', 'title': 'Articles awaiting review', 'status': 'partial', 'current': ev_summary.get('awaiting_review', 0)},
    {'id': 'RM-M05', 'title': 'Scheduled updates', 'status': 'planned', 'current': 0},
    {'id': 'RM-M06', 'title': 'Research gaps', 'status': 'partial', 'current': len(ev_summary.get('research_gaps', []))},
    {'id': 'RM-M07', 'title': 'Citation completion', 'status': 'partial', 'current': ev_summary.get('citation_coverage_pct', 0), 'unit': '%'},
    {'id': 'RM-M08', 'title': 'Editorial workload', 'status': 'planned', 'current': 0},
]

FUTURE_CAPACITY = [
    'Expanded Arkansas content', 'New Supreme Court decisions', 'Additional datasets',
    'Comparative state studies', 'Multimedia research',
    'AI-assisted evidence discovery subject to human verification',
]

principles_live = sum(1 for p in PRINCIPLES if p['status'] == 'live')
principles_partial = sum(1 for p in PRINCIPLES if p['status'] == 'partial')
avg_principle_readiness = round(sum(p['readiness_pct'] for p in PRINCIPLES) / len(PRINCIPLES))
workflow_partial = sum(1 for w in RESEARCH_WORKFLOW if w['status'] == 'partial')

research_methodology_readiness = min(
    round(avg_principle_readiness * 0.35 + (principles_partial / 10 * 100) * 0.2 + (workflow_partial / 11 * 100) * 0.15 + 12),
    25,
)

out = {
    'version': '1.0',
    'build': 43,
    'updated': today,
    'title': 'Master Research Methodology & Standards Manual v1.0',
    'subtitle': 'Institutional Research Constitution',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/research-methodology.html',
    'constitution': '/docs/MASTER_RESEARCH_METHODOLOGY.md',
    'purpose': 'How do we know what we know? — published research methodology for public trust.',
    'mission': 'Accurate, transparent, verifiable, current, understandable, consistent civic education.',
    'governing_principle': 'Readers understand the process by which conclusions were reached — transparency as highly as accuracy.',
    'core_question': 'How do we know what we know?',
    'principles': PRINCIPLES,
    'research_workflow': RESEARCH_WORKFLOW,
    'source_evaluation_checklist': SOURCE_EVALUATION_CHECKLIST,
    'citation_standards': CITATION_STANDARDS,
    'research_documentation': RESEARCH_DOCUMENTATION,
    'quality_assurance': QUALITY_ASSURANCE,
    'institutional_responsibility': INSTITUTIONAL_RESPONSIBILITY,
    'future_capacity': FUTURE_CAPACITY,
    'mc_integration': {
        'title': 'Mission Control Research Methodology Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'adherence_tracking_live': False,
    },
    'foundations': {
        'research_framework': {
            'route': '/data/research-framework.json', 'build': 10,
            'dashboard': '/mission-control/research.html',
            'principles_in_build_10': len(rf_philosophy),
            'note': 'Build #10 Research Constitution — extended not replaced',
        },
        'evidence_registry': {'route': '/data/evidence-registry.json', 'items': ev_summary.get('total', 0)},
        'evidence_ledger': {'route': '/data/evidence-ledger.json', 'build': 41, 'claims': ledger_summary.get('claims_total', 0)},
        'research_observatory': {'route': '/data/research-observatory.json', 'build': 29},
        'citation_guide': {'route': '/docs/CITATION_GUIDE.md'},
    },
    'related_systems': [
        {'title': 'Research Framework (Build #10)', 'route': '/data/research-framework.json'},
        {'title': 'Evidence Registry', 'route': '/data/evidence-registry.json'},
        {'title': 'Evidence Ledger', 'route': '/data/evidence-ledger.json', 'build': 41},
        {'title': 'Research Observatory', 'route': '/data/research-observatory.json', 'build': 29},
        {'title': 'Research Library', 'route': '/data/master-research-library.json', 'build': 37},
        {'title': 'Trust Framework', 'route': '/data/trust-framework.json', 'build': 36},
    ],
    'summary': {
        'principles_total': len(PRINCIPLES),
        'principles_live': principles_live,
        'principles_partial': principles_partial,
        'principles_planned': sum(1 for p in PRINCIPLES if p['status'] == 'planned'),
        'principles_from_build_10': sum(1 for p in PRINCIPLES if p.get('in_build_10')),
        'workflow_stages': len(RESEARCH_WORKFLOW),
        'workflow_stages_partial': workflow_partial,
        'avg_principle_readiness_pct': avg_principle_readiness,
        'evidence_items': ev_summary.get('total', 0),
        'evidence_v1_target': ev_summary.get('v1_target', 500),
        'claims_verified': ledger_summary.get('claims_verified', 0),
        'citation_coverage_pct': ev_summary.get('citation_coverage_pct', 0),
        'evidence_completeness_pct': ev_summary.get('evidence_completeness_pct', 0),
        'research_gaps_count': len(ev_summary.get('research_gaps', [])),
        'adherence_tracking_live': False,
        'scheduled_review_live': False,
        'research_methodology_readiness_pct': research_methodology_readiness,
    },
    'catalog_gaps': [
        f'Only {ev_summary.get("total", 0)}/{ev_summary.get("v1_target", 500)} evidence items — methodology ahead of corpus',
        '5 of 10 principles new in Build #43 — not yet enforced across all content',
        '11-stage workflow defined — MC project tracking not built',
        'Source evaluation checklist — no per-source evaluation records',
        'Research documentation template — no project folders with full trail',
        'Scheduled review automation planned — continuous review at 12%',
        'Documentation principle at 14% — revision history sparse',
        f'Citation coverage at {ev_summary.get("citation_coverage_pct", 0)}% — far from complete',
        'Editorial workload metric at 0 — no assignment system',
        'Adherence to methodology not measured per article',
    ],
    'recommended_next_build': {
        'number': 44,
        'title': 'Component Specifications with Props/States',
        'note': 'Map research workflow panels, source evaluation forms, citation widgets, and QA checklists to COMP-* from Build #17.',
    },
}

path = root / 'data/research-methodology.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Research Methodology: {principles_partial}/10 partial, {research_methodology_readiness}% readiness')
