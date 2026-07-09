"""
Generate data/trust-framework.json — Build #36 Evidence, Transparency & Trust Framework v1.0.
Also refreshes v2 database decision in database-schema.json.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

facts_path = root / 'data/facts-registry.json'
evidence_path = root / 'data/evidence-registry.json'
facts_fw_path = root / 'data/facts-framework.json'
db_path = root / 'data/database-schema.json'

facts = {}
evidence = {}
facts_fw = {}
if facts_path.exists():
    with open(facts_path) as f:
        facts = json.load(f)
if evidence_path.exists():
    with open(evidence_path) as f:
        evidence = json.load(f)
if facts_fw_path.exists():
    with open(facts_fw_path) as f:
        facts_fw = json.load(f)

fs = facts.get('summary', {})
es = evidence.get('summary', {})

TRUST_PYRAMID = [
    {'id': 'TRUST-P1', 'level': 1, 'title': 'Clear Language', 'status': 'partial',
     'requirements': ['Plain-language explanations', 'Jargon accompanied by definitions']},
    {'id': 'TRUST-P2', 'level': 2, 'title': 'Transparent Sources', 'status': 'partial',
     'requirements': ['Source origin', 'Publication date', 'Producer', 'Primary vs secondary']},
    {'id': 'TRUST-P3', 'level': 3, 'title': 'Evidence Before Conclusions', 'status': 'partial',
     'requirements': ['Historical record first', 'Court opinions', 'Datasets', 'Statutes', 'Then explanation']},
    {'id': 'TRUST-P4', 'level': 4, 'title': 'Honest Context', 'status': 'partial',
     'requirements': ['Established facts', 'Legal holdings', 'Interpretations', 'Empirical findings', 'Disagreement areas']},
    {'id': 'TRUST-P5', 'level': 5, 'title': 'Continuous Review', 'status': 'planned',
     'requirements': ['Scheduled review cycles', 'MC identifies materials due for review']},
]

SOURCE_TRANSPARENCY = [
    'Last reviewed date', 'Primary sources used', 'Supporting references',
    'Citation count', 'Related documents', 'Version history',
]

EVIDENCE_LEVELS = [
    {'id': 'TRUST-EV-A', 'level': 'A', 'title': 'Primary legal materials', 'status': 'partial',
     'examples': ['Supreme Court opinions', 'Federal statutes', 'Arkansas statutes', 'Official government publications'],
     'count': es.get('primary_sources', 0) + es.get('by_type', {}).get('court', 0)},
    {'id': 'TRUST-EV-B', 'level': 'B', 'title': 'Official public records and datasets', 'status': 'partial',
     'examples': ['Election spending reports', 'Government statistics', 'Court filings'],
     'count': es.get('government_sources', 0)},
    {'id': 'TRUST-EV-C', 'level': 'C', 'title': 'Peer-reviewed academic scholarship', 'status': 'planned',
     'examples': ['Law review articles', 'Academic journals', 'University publications'],
     'count': es.get('academic_sources', 0)},
    {'id': 'TRUST-EV-D', 'level': 'D', 'title': 'Reputable explanatory sources', 'status': 'partial',
     'examples': ['Educational organizations', 'Major news organizations', 'Think tank reports'],
     'count': es.get('journalism_sources', 0) + es.get('by_type', {}).get('ngo', 0),
     'note': 'Supplement, not replace, primary sources'},
]

FACT_REVIEW_STAGES = [
    {'stage': 1, 'title': 'Drafted', 'status': 'partial'},
    {'stage': 2, 'title': 'Supported by evidence', 'status': 'partial'},
    {'stage': 3, 'title': 'Source reviewed', 'status': 'partial'},
    {'stage': 4, 'title': 'Editorial reviewed', 'status': 'planned'},
    {'stage': 5, 'title': 'Published', 'status': 'partial'},
    {'stage': 6, 'title': 'Scheduled for future review', 'status': 'planned'},
]

TRANSPARENCY_PANELS = [
    {'id': 'TRUST-TP-01', 'title': 'How We Know This', 'status': 'planned',
     'purpose': 'Explains the evidence supporting the page'},
    {'id': 'TRUST-TP-02', 'title': 'What This Page Does Not Claim', 'status': 'planned',
     'purpose': 'Clarifies misunderstandings and limits'},
    {'id': 'TRUST-TP-03', 'title': 'Questions Still Being Studied', 'status': 'planned',
     'purpose': 'Highlights ongoing research or debate'},
]

TRUST_DASHBOARD_METRICS = [
    {'id': 'TRUST-M01', 'title': 'Pages fully sourced', 'status': 'planned', 'current': 0},
    {'id': 'TRUST-M02', 'title': 'Pages under review', 'status': 'partial', 'current': es.get('awaiting_review', 0)},
    {'id': 'TRUST-M03', 'title': 'Facts verified', 'status': 'partial', 'current': fs.get('verified', 0)},
    {'id': 'TRUST-M04', 'title': 'Sources added', 'status': 'partial', 'current': es.get('total', 0)},
    {'id': 'TRUST-M05', 'title': 'Broken citations', 'status': 'planned', 'current': 0},
    {'id': 'TRUST-M06', 'title': 'Scheduled reviews completed', 'status': 'planned', 'current': 0},
    {'id': 'TRUST-M07', 'title': 'Reader feedback received', 'status': 'planned', 'current': 0},
    {'id': 'TRUST-M08', 'title': 'Corrections published', 'status': 'planned', 'current': 0},
]

PUBLIC_ACCOUNTABILITY = [
    {'title': 'Editorial standards', 'status': 'partial', 'route': '/builds/002-project-constitution.md'},
    {'title': 'Research methodology', 'status': 'partial', 'route': '/mission-control/research.html'},
    {'title': 'Citation policy', 'status': 'partial', 'route': '/docs/FACTS_CONSTITUTION.md'},
    {'title': 'Review process', 'status': 'partial', 'route': '/mission-control/facts.html'},
    {'title': 'Correction policy', 'status': 'planned', 'route': None},
    {'title': 'Privacy policy', 'status': 'planned', 'route': None},
    {'title': 'Accessibility commitment', 'status': 'partial', 'route': '/mission-control/design.html'},
]

DATABASE_DECISION = {
    'build': 36,
    'decided': '2026-07-09',
    'v1_current': {
        'storage': 'static_json_netlify_forms',
        'status': 'live',
        'note': 'No database deployed — honest metrics from JSON registries.',
    },
    'v2_trial_recommended': [
        {
            'provider': 'Netlify Database',
            'type': 'managed_postgres',
            'status': 'recommended_trial',
            'rationale': 'Already on Netlify; Postgres fits Build #22 schema; preview DB branches; free tier with credit limits.',
            'caveats': ['DB sleeps on free tier after ~5 min', '300 monthly credits shared across all Netlify usage'],
        },
        {
            'provider': 'Neon',
            'type': 'serverless_postgres',
            'status': 'recommended_alternative',
            'rationale': 'Pure Postgres; scale-to-zero; branching; does not consume Netlify credits.',
            'caveats': ['Auth and admin built separately', '~512 MB free storage'],
        },
    ],
    'v2_full_when_needed': {
        'provider': 'Supabase',
        'type': 'postgres_baas',
        'status': 'deferred_until_auth_rls',
        'rationale': 'Best when participant profiles, Education Leader signups, coalition accounts, and RLS become priority.',
        'triggers': ['Authenticated admin dashboard', 'Person/org tables live', 'Privacy-first row-level security'],
    },
    'not_recommended': [
        {'provider': 'Turso', 'reason': 'SQLite — diverges from Postgres ERD in Build #22'},
    ],
    'governing_rule': 'Stay on v1 until real signups; trial Postgres via Netlify Database or Neon; adopt Supabase when auth/RLS required.',
}

pyramid_partial = sum(1 for p in TRUST_PYRAMID if p['status'] == 'partial')
panels_live = sum(1 for p in TRANSPARENCY_PANELS if p['status'] == 'live')
accountability_partial = sum(1 for a in PUBLIC_ACCOUNTABILITY if a['status'] == 'partial')

trust_readiness = min(
    round(
        (fs.get('fact_completeness_pct', 0) or 12) * 0.2
        + (es.get('citation_coverage_pct', 0) or 12) * 0.2
        + pyramid_partial / 5 * 100 * 0.25
        + accountability_partial / 7 * 100 * 0.2
        + 18  # architecture defined
    ),
    24,
)

out = {
    'version': '1.0',
    'build': 36,
    'updated': today,
    'title': 'Evidence, Transparency & Trust Framework v1.0',
    'subtitle': 'Public Trust Operating System',
    'platform': 'Citizens United Facts',
    'organization': 'Arkansas Civic Education Initiative',
    'route': '/mission-control/trust.html',
    'constitution': '/docs/PUBLIC_TRUST_OPERATING_SYSTEM.md',
    'purpose': 'Public trust as measurable objective — accuracy, transparency, intellectual honesty.',
    'trust_philosophy': "Don't ask readers to trust us. Show them why they can verify what we present.",
    'governing_principle': 'Earn trust through transparency — tools to investigate, not pressure to believe.',
    'long_term_goal': 'Every claim on the platform — readers can examine evidence, context, and reasoning.',
    'trust_pyramid': TRUST_PYRAMID,
    'source_transparency_standards': SOURCE_TRANSPARENCY,
    'evidence_levels': EVIDENCE_LEVELS,
    'fact_review_process': FACT_REVIEW_STAGES,
    'transparency_panels': TRANSPARENCY_PANELS,
    'version_history': {
        'title': 'Version History',
        'status': 'planned',
        'fields': ['Publication date', 'Major updates', 'Reason for updates', 'Research revisions'],
    },
    'editorial_independence': {
        'title': 'Editorial Independence',
        'status': 'partial',
        'note': 'Changes documented; significant revisions note why.',
    },
    'reader_feedback': {
        'title': 'Reader Feedback',
        'status': 'planned',
        'channels': ['Report factual errors', 'Suggest sources', 'Recommend clarifications', 'Ask educational questions'],
        'workflow': 'Editorial review before changes published',
    },
    'trust_dashboard_metrics': TRUST_DASHBOARD_METRICS,
    'public_accountability': PUBLIC_ACCOUNTABILITY,
    'database_decision': DATABASE_DECISION,
    'related_systems': [
        {'title': 'Facts Framework', 'route': '/data/facts-framework.json', 'build': 18},
        {'title': 'Facts Registry', 'route': '/data/facts-registry.json', 'build': 18},
        {'title': 'Evidence Registry', 'route': '/data/evidence-registry.json', 'build': 10},
        {'title': 'Research Framework', 'route': '/mission-control/research.html', 'build': 10},
        {'title': 'Content Production Factory', 'route': '/mission-control/content-factory.html', 'build': 27},
        {'title': 'Database Schema', 'route': '/data/database-schema.json', 'build': 22},
    ],
    'registry_snapshot': {
        'facts_total': fs.get('total', 0),
        'facts_verified': fs.get('verified', 0),
        'facts_under_review': fs.get('under_review', 0),
        'facts_awaiting_sources': fs.get('awaiting_sources', 0),
        'evidence_total': es.get('total', 0),
        'evidence_published': es.get('published', 0),
        'evidence_awaiting_review': es.get('awaiting_review', 0),
        'citation_coverage_pct': es.get('citation_coverage_pct', 0),
        'fact_completeness_pct': fs.get('fact_completeness_pct', 0),
    },
    'summary': {
        'trust_pyramid_levels': len(TRUST_PYRAMID),
        'evidence_levels': len(EVIDENCE_LEVELS),
        'fact_review_stages': len(FACT_REVIEW_STAGES),
        'transparency_panels': len(TRANSPARENCY_PANELS),
        'trust_metrics': len(TRUST_DASHBOARD_METRICS),
        'accountability_pages': len(PUBLIC_ACCOUNTABILITY),
        'transparency_panels_live': panels_live,
        'trust_dashboard_live': True,
        'page_sourcing_live': False,
        'trust_readiness_pct': trust_readiness,
    },
    'catalog_gaps': [
        'Transparency panels (How We Know This, etc.) not on major pages',
        'Last reviewed date and version history not uniform across halls',
        'Level C academic sources: 0 in evidence registry',
        'Correction policy and privacy policy pages not published',
        'Reader feedback workflow not implemented',
        'Broken citation monitoring not automated',
        'Scheduled review cycles not in MC calendar',
        f'Only {fs.get("verified", 0)}/{fs.get("total", 0)} facts verified — {es.get("citation_coverage_pct", 0)}% citation coverage',
    ],
    'recommended_next_build': {
        'number': 38,
        'title': 'Component Specifications with Props/States',
        'note': 'Map trust panels, evidence levels, and transparency standards to COMP-* from Build #17.',
    },
}

path = root / 'data/trust-framework.json'
with open(path, 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')

# Update database-schema.json with v2 decision
if db_path.exists():
    with open(db_path) as f:
        db = json.load(f)
    db['storage_strategy']['v2_future'] = [
        {'method': 'Netlify Database', 'status': 'recommended_trial', 'type': 'managed_postgres',
         'note': 'Build #36 decision — same vendor as site; Postgres; preview branches'},
        {'method': 'Neon', 'status': 'recommended_alternative', 'type': 'serverless_postgres',
         'note': 'Build #36 decision — pure Postgres without Netlify credit limits'},
        {'method': 'Supabase', 'status': 'deferred_until_auth_rls', 'type': 'postgres_baas',
         'note': 'When participant profiles, RLS, and admin auth become priority'},
        {'method': 'Postgres', 'status': 'planned', 'note': 'Generic target — provider per decision above'},
        {'method': 'Serverless API routes', 'status': 'planned'},
        {'method': 'Authenticated admin dashboard', 'status': 'planned'},
    ]
    db['summary']['migration_target'] = 'postgres_v2_netlify_or_neon'
    db['summary']['v2_database_decision'] = DATABASE_DECISION['governing_rule']
    db['catalog_gaps'] = [
        g for g in db.get('catalog_gaps', [])
        if 'Supabase instance' not in g and 'Postgres/Supabase' not in g
    ] + [
        'No Postgres instance deployed — v2 trial: Netlify Database or Neon (Build #36)',
        'Supabase deferred until auth/RLS required',
    ]
    if 'open_questions' not in db:
        db['open_questions'] = []
    db['database_decision'] = DATABASE_DECISION
    db['updated'] = today
    with open(db_path, 'w', newline='\n') as f:
        json.dump(db, f, indent=2)
        f.write('\n')

print(f'Trust Framework: {trust_readiness}% readiness; database decision recorded')
