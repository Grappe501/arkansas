"""
Generate data/evidence-ledger.json — Build #41 Master Evidence Ledger & Claims Registry v1.0.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'


def load_json(path):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


claims_legacy = load_json(root / 'data/claims-ledger.json')
facts = load_json(root / 'data/facts-registry.json')
evidence = load_json(root / 'data/evidence-registry.json')
trust = load_json(root / 'data/trust-framework.json')

facts_summary = facts.get('summary', {})
ev_summary = evidence.get('summary', {})
legacy_claims = claims_legacy.get('claims', [])

EVIDENCE_STRENGTH_LEVELS = [
    {
        'id': 'EVL-A', 'level': 'A', 'title': 'Primary legal authority',
        'description': 'Supreme Court opinions, statutes, constitutional text.',
        'status': 'live', 'claims_at_level': 1,
    },
    {
        'id': 'EVL-B', 'level': 'B', 'title': 'Official government publications',
        'description': 'Government reports, public records, official datasets.',
        'status': 'live', 'claims_at_level': 1,
    },
    {
        'id': 'EVL-C', 'level': 'C', 'title': 'Peer-reviewed academic literature',
        'description': 'Law review articles, academic journals, university publications.',
        'status': 'planned', 'claims_at_level': 0,
    },
    {
        'id': 'EVL-D', 'level': 'D', 'title': 'Multiple reliable secondary sources',
        'description': 'Educational organizations, major news, verified secondary references.',
        'status': 'partial', 'claims_at_level': 0,
    },
    {
        'id': 'EVL-E', 'level': 'E', 'title': 'Educational synthesis',
        'description': 'Context-dependent synthesis — methodology must be documented.',
        'status': 'partial', 'claims_at_level': 1,
    },
]

REVIEW_WORKFLOW = [
    {'id': 'WF-01', 'stage': 'Draft', 'status': 'defined'},
    {'id': 'WF-02', 'stage': 'Source Collection', 'status': 'partial'},
    {'id': 'WF-03', 'stage': 'Verification', 'status': 'partial'},
    {'id': 'WF-04', 'stage': 'Editorial Review', 'status': 'partial'},
    {'id': 'WF-05', 'stage': 'Publication', 'status': 'partial'},
    {'id': 'WF-06', 'stage': 'Scheduled Review', 'status': 'planned'},
    {'id': 'WF-07', 'stage': 'Revision', 'status': 'planned'},
]

EVIDENCE_LINK_TYPES = [
    'Primary Sources', 'Court Opinions', 'Statutes', 'Government Reports',
    'Academic Research', 'Historical Records', 'Verified Data Sets', 'Supporting Educational Resources',
]

CLAIM_RELATIONSHIP_TYPES = [
    'Articles', 'Lessons', 'Encyclopedia entries', 'Timeline events',
    'Charts', 'Videos', 'Community education resources', 'Frequently asked questions',
]

CHANGE_HISTORY_FIELDS = [
    'What changed', 'Why it changed', 'Who reviewed it',
    'Supporting evidence added', 'Sources removed', 'Date of change',
]

PUBLIC_TRANSPARENCY = [
    'Evidence strength', 'Review date', 'Supporting source count',
    'Related documents', 'Version history',
]

CONTRADICTORY_EVIDENCE_POLICY = [
    'Describe the differing evidence',
    'Explain the nature of the disagreement',
    'Identify the strongest available support',
    'Encourage readers to consult primary materials',
]

FUTURE_AI = [
    'Cite evidence precisely', 'Recommend additional sources',
    'Detect outdated claims', 'Identify unsupported statements',
    'Build educational summaries grounded in verified information',
]

# Seed canonical CLAIM records from legacy claims-ledger
CLAIMS = [
    {
        'claim_id': 'CLAIM-000001',
        'legacy_id': 'claim-001',
        'fact_id': 'FACT-1001',
        'claim_statement': 'Citizens United held that government may not restrict independent political spending by corporations and unions.',
        'plain_language': 'The Supreme Court ruled that independent political spending by corporations and unions is protected speech.',
        'expanded_explanation': 'In Citizens United v. FEC (2010), the Court held that the First Amendment prohibits government restriction of independent expenditures by corporations and associations.',
        'topic_category': 'Supreme Court holding',
        'date_created': '2026-07-09',
        'date_last_reviewed': '2026-07-09',
        'review_status': 'published',
        'workflow_stage': 'Publication',
        'evidence_strength': 'A',
        'evidence_ids': ['EV-000001'],
        'evidence_count': 1,
        'related_hall': '/halls/what-court-decided.html',
        'related_kg_id': 'KG-CASE-000003',
        'educational_context': 'Foundation for understanding corporate independent expenditure doctrine after 2010.',
        'learn_next': 'SpeechNow.org v. FEC and Super PAC development',
        'audit_history': [],
        'conflicting_evidence': False,
        'scheduled_review': None,
        'status': 'verified',
    },
    {
        'claim_id': 'CLAIM-000002',
        'legacy_id': 'claim-002',
        'fact_id': 'FACT-5001',
        'claim_statement': 'Montana Initiative 194 would prohibit artificial persons from contributing to campaigns, ballot measures, or political parties.',
        'plain_language': 'Montana voters may consider a ballot measure restricting corporate and organizational political contributions.',
        'expanded_explanation': 'Initiative 194 seeks to exclude artificial persons from contributing to campaigns, ballot measures, or political parties in Montana.',
        'topic_category': 'State reform',
        'date_created': '2026-07-09',
        'date_last_reviewed': '2026-07-09',
        'review_status': 'published',
        'workflow_stage': 'Publication',
        'evidence_strength': 'B',
        'evidence_ids': ['EV-000004', 'EV-000005'],
        'evidence_count': 2,
        'related_hall': '/halls/montana-hawaii.html',
        'educational_context': 'Example of state-level response to Citizens United through ballot initiative.',
        'learn_next': 'Compare with Hawaii Act 11 legislative approach',
        'audit_history': [],
        'conflicting_evidence': False,
        'scheduled_review': None,
        'status': 'verified',
    },
    {
        'claim_id': 'CLAIM-000003',
        'legacy_id': 'claim-003',
        'fact_id': 'FACT-5002',
        'claim_statement': 'Hawaii Act 11 restricts corporate election spending; effective July 1, 2027.',
        'plain_language': 'Hawaii passed legislation restricting certain corporate election spending, with a future effective date.',
        'expanded_explanation': 'Hawaii Act 11 addresses corporate influence in elections; legislative text confirmation pending full primary source review.',
        'topic_category': 'State reform',
        'date_created': '2026-07-09',
        'date_last_reviewed': '2026-07-09',
        'review_status': 'requires_review',
        'workflow_stage': 'Verification',
        'evidence_strength': 'E',
        'evidence_ids': ['EV-000006', 'EV-000014'],
        'evidence_count': 2,
        'related_hall': '/halls/montana-hawaii.html',
        'educational_context': 'Illustrates legislative (not ballot) path to corporate spending restrictions.',
        'learn_next': 'Obtain Hawaii legislative text as Level A/B evidence',
        'audit_history': [],
        'conflicting_evidence': False,
        'scheduled_review': None,
        'status': 'awaiting_review',
        'note': 'Journalism source — legislative text not yet primary-confirmed',
    },
]

verified = sum(1 for c in CLAIMS if c['status'] == 'verified')
awaiting = sum(1 for c in CLAIMS if c['status'] == 'awaiting_review')
with_audit = sum(1 for c in CLAIMS if c.get('audit_history'))
conflicting = sum(1 for c in CLAIMS if c.get('conflicting_evidence'))

MC_METRICS = [
    {'id': 'EL-M01', 'title': 'Total claims', 'status': 'partial', 'current': len(CLAIMS), 'target': 500},
    {'id': 'EL-M02', 'title': 'Claims fully verified', 'status': 'partial', 'current': verified},
    {'id': 'EL-M03', 'title': 'Claims awaiting review', 'status': 'partial', 'current': awaiting},
    {'id': 'EL-M04', 'title': 'Claims requiring updated sources', 'status': 'partial', 'current': 1},
    {'id': 'EL-M05', 'title': 'Newly added claims', 'status': 'partial', 'current': len(CLAIMS)},
    {'id': 'EL-M06', 'title': 'Claims with conflicting evidence', 'status': 'planned', 'current': conflicting},
    {'id': 'EL-M07', 'title': 'Claims nearing scheduled review', 'status': 'planned', 'current': 0},
    {'id': 'EL-M08', 'title': 'Facts registry (FACT-*)', 'status': 'partial', 'current': facts_summary.get('total', 0)},
    {'id': 'EL-M09', 'title': 'Evidence items (EV-*)', 'status': 'partial', 'current': ev_summary.get('total', 0)},
]

claims_with_full_record = sum(
    1 for c in CLAIMS
    if c.get('plain_language') and c.get('expanded_explanation') and c.get('educational_context')
)
avg_record_completeness = round(claims_with_full_record / len(CLAIMS) * 100) if CLAIMS else 0

evidence_ledger_readiness = min(
    round(
        (len(CLAIMS) / 500 * 100) * 0.2
        + (verified / max(len(CLAIMS), 1) * 100) * 0.25
        + avg_record_completeness * 0.15
        + (ev_summary.get('total', 0) / 500 * 100) * 0.1
        + 12
    ),
    22,
)

out = {
    'version': '1.0',
    'build': 41,
    'updated': today,
    'title': 'Master Evidence Ledger & Claims Registry v1.0',
    'subtitle': 'Institutional Truth Architecture',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/evidence-ledger.html',
    'canonical_claim_route': '/claims/[claim-id]',
    'current_claim_route': 'claims-ledger.json + facts-registry — no public claim pages',
    'constitution': '/docs/MASTER_EVIDENCE_LEDGER.md',
    'purpose': 'Every meaningful factual claim traceable to evidence.',
    'core_philosophy': 'Every meaningful factual claim can be traced back to evidence.',
    'governing_principle': 'Authority from evidence quality and transparent review — not institutional assertion alone.',
    'long_term_vision': 'Visitors explore the chain of evidence behind every important claim.',
    'id_format': 'CLAIM-{6-digit}',
    'legacy_id_format': 'claim-{NNN}',
    'fact_id_format': 'FACT-{NNNN}',
    'evidence_id_format': 'EV-{6-digit}',
    'evidence_strength_levels': EVIDENCE_STRENGTH_LEVELS,
    'review_workflow': REVIEW_WORKFLOW,
    'evidence_link_types': EVIDENCE_LINK_TYPES,
    'claim_relationship_types': CLAIM_RELATIONSHIP_TYPES,
    'change_history_fields': CHANGE_HISTORY_FIELDS,
    'contradictory_evidence_policy': CONTRADICTORY_EVIDENCE_POLICY,
    'public_transparency': PUBLIC_TRANSPARENCY,
    'future_ai_integration': FUTURE_AI,
    'claims': CLAIMS,
    'mc_integration': {
        'title': 'Mission Control Evidence Ledger Metrics',
        'status': 'partial',
        'metrics': MC_METRICS,
        'public_transparency_live': False,
        'audit_trail_live': False,
    },
    'foundations': {
        'claims_ledger': {'route': '/data/claims-ledger.json', 'build': 10, 'legacy_claims': len(legacy_claims)},
        'facts_registry': {'route': '/data/facts-registry.json', 'build': 18, 'facts': facts_summary.get('total', 0)},
        'evidence_registry': {'route': '/data/evidence-registry.json', 'build': 10, 'items': ev_summary.get('total', 0)},
        'trust_framework': {'route': '/data/trust-framework.json', 'build': 36, 'evidence_levels': 4},
    },
    'related_systems': [
        {'title': 'Evidence Registry', 'route': '/data/evidence-registry.json', 'build': 10},
        {'title': 'Facts Framework', 'route': '/data/facts-registry.json', 'build': 18},
        {'title': 'Trust Framework', 'route': '/data/trust-framework.json', 'build': 36},
        {'title': 'Research Library', 'route': '/data/master-research-library.json', 'build': 37},
        {'title': 'Civic Intelligence', 'route': '/data/civic-intelligence.json', 'build': 40},
        {'title': 'AI Knowledge Engine', 'route': '/data/ai-knowledge-engine.json', 'build': 26},
    ],
    'summary': {
        'claims_total': len(CLAIMS),
        'claims_verified': verified,
        'claims_awaiting_review': awaiting,
        'claims_requiring_sources': 1,
        'claims_with_conflicting_evidence': conflicting,
        'claims_with_audit_history': with_audit,
        'facts_registry_total': facts_summary.get('total', 0),
        'facts_migrated_from_claims': facts_summary.get('migrated_from_claims', 0),
        'evidence_items_total': ev_summary.get('total', 0),
        'evidence_awaiting_review': ev_summary.get('awaiting_review', 0),
        'strength_levels_defined': len(EVIDENCE_STRENGTH_LEVELS),
        'workflow_stages': len(REVIEW_WORKFLOW),
        'avg_claim_record_completeness_pct': avg_record_completeness,
        'v1_target_claims': 500,
        'claims_growth_pct': round(len(CLAIMS) / 500 * 100),
        'public_claim_pages_live': False,
        'audit_trail_live': False,
        'scheduled_review_live': False,
        'evidence_ledger_readiness_pct': evidence_ledger_readiness,
    },
    'catalog_gaps': [
        f'Only {len(CLAIMS)}/500 claims — vast majority of platform sentences not CLAIM-linked',
        f'{facts_summary.get("total", 0)} FACT-* records — not all migrated to CLAIM-* format',
        'No public /claims/[id] pages — transparency panels not built',
        'Audit trail defined — 0 change history records',
        'Scheduled review workflow planned — no automation',
        'Level C (academic) — 0 peer-reviewed sources in evidence registry',
        'Contradictory evidence policy defined — no live conflict records',
        '10 facts awaiting sources per facts-registry',
        'Claim-to-lesson/encyclopedia/video relationships not wired',
        'Trust framework has A–D levels — ledger adds Level E synthesis',
    ],
    'recommended_next_build': {
        'number': 45,
        'title': 'Component Specifications with Props/States',
        'note': 'Map claim panels, evidence strength badges, audit history viewers, and transparency widgets to COMP-* from Build #17.',
    },
}

path = root / 'data/evidence-ledger.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f'Evidence Ledger: {len(CLAIMS)} claims, {verified} verified, {evidence_ledger_readiness}% readiness')
