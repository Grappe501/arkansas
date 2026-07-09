"""
Generate data/facts-registry.json — Build #18 Citizens United Facts Framework v1.0.
Seeds facts from claims-ledger and platform knowledge; refreshes summary stats.
"""
import json
from pathlib import Path
from datetime import date

root = Path(__file__).resolve().parents[1]
today = '2026-07-09'

def fact(
    fact_id, category_id, short_statement, plain_explanation,
    review_status, philosophy_question, source_type='primary',
    evidence_ids=None, related_topics=None, related_cases=None,
    related_resources=None, legacy_claim_id=None,
    detailed_explanation=None, timeline_events=None, charts=None
):
    return {
        'fact_id': fact_id,
        'category_id': category_id,
        'short_statement': short_statement,
        'plain_explanation': plain_explanation,
        'detailed_explanation': detailed_explanation or plain_explanation,
        'source_type': source_type,
        'supporting_sources': [],
        'evidence_ids': evidence_ids or [],
        'related_topics': related_topics or [],
        'related_timeline_events': timeline_events or [],
        'related_cases': related_cases or [],
        'related_charts': charts or [],
        'related_educational_resources': related_resources or [],
        'philosophy_question': philosophy_question,
        'presentation_levels': ['L1', 'L2', 'L3', 'L4'],
        'last_verification_date': today,
        'review_status': review_status,
        'legacy_claim_id': legacy_claim_id
    }

items = [
    # FACT-1000 — The Case
    fact(
        'FACT-1001', 'FACT-1000',
        'Citizens United held that government may not restrict independent political spending by corporations and unions.',
        'The Supreme Court ruled that independent expenditures — spending not coordinated with a candidate — cannot be limited under the First Amendment, even when made by corporations or unions.',
        'confirmed', 'what',
        evidence_ids=['EV-000001'],
        related_topics=['KG-CASE-000003'],
        related_cases=['Citizens United v. FEC (2010)'],
        related_resources=['/halls/what-court-decided.html'],
        legacy_claim_id='claim-001',
        detailed_explanation='In Citizens United v. Federal Election Commission (558 U.S. 310), the Court addressed whether federal law could prohibit corporations and unions from making independent expenditures in elections. The majority held that such restrictions violate the First Amendment. This holding is central to understanding post-2010 campaign finance.'
    ),
    fact(
        'FACT-1002', 'FACT-1000',
        'The Supreme Court decided Citizens United on January 21, 2010.',
        'The opinion was released on January 21, 2010, during the January 2010 Term.',
        'confirmed', 'when',
        evidence_ids=['EV-000001'],
        related_topics=['KG-CASE-000003', 'KG-EVENT-000007'],
        related_cases=['Citizens United v. FEC (2010)'],
        related_resources=['/halls/the-case.html', '/halls/after-2010.html']
    ),
    fact(
        'FACT-1003', 'FACT-1000',
        'The Citizens United decision was decided by a 5–4 vote.',
        'Five justices joined the majority opinion; four dissented. The close vote reflects deep disagreement over corporate political speech and campaign finance regulation.',
        'strongly_supported', 'what',
        evidence_ids=['EV-000001'],
        related_topics=['KG-CASE-000003'],
        related_cases=['Citizens United v. FEC (2010)'],
        related_resources=['/halls/what-court-decided.html']
    ),
    fact(
        'FACT-1004', 'FACT-1000',
        'The case was brought by Citizens United, a nonprofit corporation, against the Federal Election Commission.',
        'Citizens United produced a film about Hillary Clinton and sought to distribute it; FEC restrictions on corporate electioneering communications were at issue.',
        'confirmed', 'what',
        evidence_ids=['EV-000001'],
        related_topics=['KG-CASE-000003', 'KG-ORG-000002'],
        related_cases=['Citizens United v. FEC (2010)'],
        related_resources=['/halls/the-case.html']
    ),
    # FACT-2000 — Historical Context
    fact(
        'FACT-2001', 'FACT-2000',
        'The Bipartisan Campaign Reform Act of 2002 (BCRA) restricted corporate and union electioneering communications.',
        'BCRA, often called McCain-Feingold, prohibited corporations and unions from funding electioneering communications close to elections — provisions later challenged and narrowed by Citizens United and related cases.',
        'context_dependent', 'why',
        source_type='government',
        related_topics=['KG-LAW-000002'],
        related_cases=['McConnell v. FEC', 'Citizens United v. FEC'],
        related_resources=['/halls/story-before.html'],
        detailed_explanation='BCRA built on earlier reforms including FECA amendments. Its corporate electioneering restrictions were a direct precursor to the legal questions in Citizens United.'
    ),
    fact(
        'FACT-2002', 'FACT-2000',
        'Buckley v. Valeo (1976) established that campaign spending is a form of protected political speech.',
        'The Court held that expenditure limits implicate First Amendment rights, while contribution limits may be regulated differently — a framework that shaped later campaign finance jurisprudence.',
        'context_dependent', 'why',
        evidence_ids=[],
        related_topics=['KG-CASE-000001'],
        related_cases=['Buckley v. Valeo (1976)'],
        related_resources=['/halls/story-before.html'],
        detailed_explanation='Buckley remains foundational. Citizens United extended expenditure protections to corporate and union independent spending. Primary opinion not yet in Evidence Registry — under documentation.'
    ),
    # FACT-3000 — Constitutional Principles
    fact(
        'FACT-3001', 'FACT-3000',
        'The First Amendment was central to the Citizens United majority\'s reasoning.',
        'The majority framed independent political spending as protected speech; restrictions must survive strict scrutiny.',
        'confirmed', 'why',
        evidence_ids=['EV-000001'],
        related_topics=['KG-PRIN-000001', 'KG-CASE-000003'],
        related_resources=['/halls/what-court-decided.html', '/halls/debate.html']
    ),
    fact(
        'FACT-3002', 'FACT-3000',
        'The decision addressed independent expenditures separately from direct contributions to candidates.',
        'Independent spending — not coordinated with a campaign — received different constitutional treatment than contributions, following Buckley\'s expenditure/contribution distinction.',
        'confirmed', 'what',
        evidence_ids=['EV-000001'],
        related_topics=['KG-PRIN-000002'],
        related_resources=['/halls/what-court-decided.html']
    ),
    # FACT-4000 — Political Spending
    fact(
        'FACT-4001', 'FACT-4000',
        'Outside spending in federal elections increased substantially after 2010.',
        'Independent expenditure and outside-group spending grew in the decade following Citizens United, though causation involves multiple factors beyond a single decision.',
        'under_review', 'what_changed',
        source_type='government',
        related_topics=['KG-DATA-000001', 'KG-EVENT-000007'],
        charts=['money-map-preview'],
        related_resources=['/halls/after-2010.html', '/halls/money-map.html'],
        detailed_explanation='FEC and OpenSecrets data document spending trends. Platform requires verified datasets (EV-IDs) before upgrading to Confirmed status.'
    ),
    # FACT-5000 — Current Developments
    fact(
        'FACT-5001', 'FACT-5000',
        'Montana Initiative 194 would prohibit artificial persons from contributing to campaigns, ballot measures, or political parties.',
        'A 2026 Montana ballot measure seeks to restrict corporate and similar entity political contributions — part of ongoing state-level responses to Citizens United.',
        'strongly_supported', 'what',
        source_type='government',
        evidence_ids=['EV-000004', 'EV-000005'],
        related_topics=['KG-REFORM-000004'],
        related_resources=['/halls/montana-hawaii.html'],
        legacy_claim_id='claim-002'
    ),
    fact(
        'FACT-5002', 'FACT-5000',
        'Hawaii Act 11 restricts corporate election spending; effective July 1, 2027.',
        'Hawaii enacted legislation limiting corporate influence in state elections, with an effective date in 2027 — subject to ongoing verification and legal context.',
        'under_review', 'what',
        source_type='journalism',
        evidence_ids=['EV-000006', 'EV-000014'],
        related_topics=['KG-REFORM-000005'],
        related_resources=['/halls/montana-hawaii.html'],
        legacy_claim_id='claim-003'
    ),
    # FACT-6000 — Arkansas
    fact(
        'FACT-6001', 'FACT-6000',
        'The platform\'s Arkansas pilot covers all 75 counties.',
        'ACEI coalition infrastructure indexes all 75 Arkansas counties for educational partner outreach — Arkansas is the v1 geographic scope.',
        'confirmed', 'what',
        source_type='platform',
        related_resources=['/arkansas/', '/coalition/counties.html'],
        related_topics=[]
    ),
    fact(
        'FACT-6002', 'FACT-6000',
        'Arkansas campaign finance is governed by state statute and Arkansas Ethics Commission rules.',
        'Arkansas maintains its own disclosure and contribution framework for state elections, separate from federal FEC rules.',
        'under_review', 'how_we_know',
        source_type='government',
        related_resources=['/arkansas/'],
        detailed_explanation='Primary Arkansas statutes and Ethics Commission guidance must be cataloged in Evidence Registry before Confirmed status.'
    ),
]

# Compute summary
by_category = {}
by_status = {}
by_question = {}
awaiting_sources = 0
for item in items:
    cat = item['category_id']
    by_category[cat] = by_category.get(cat, 0) + 1
    st = item['review_status']
    by_status[st] = by_status.get(st, 0) + 1
    q = item['philosophy_question']
    by_question[q] = by_question.get(q, 0) + 1
    if not item['evidence_ids']:
        awaiting_sources += 1

verified = by_status.get('confirmed', 0) + by_status.get('strongly_supported', 0)
needing_review = by_status.get('under_review', 0)

registry = {
    'version': '1.0',
    'build': 18,
    'updated': today,
    'title': 'Citizens United Facts Registry',
    'framework': '/data/facts-framework.json',
    'constitution': '/docs/FACTS_CONSTITUTION.md',
    'id_format': 'FACT-{NNNN}',
    'principle': 'Every factual statement receives a permanent Fact ID. Nothing presented as fact without traceability.',
    'summary': {
        'total': len(items),
        'verified': verified,
        'confirmed': by_status.get('confirmed', 0),
        'strongly_supported': by_status.get('strongly_supported', 0),
        'context_dependent': by_status.get('context_dependent', 0),
        'under_review': needing_review,
        'awaiting_sources': awaiting_sources,
        'by_category': by_category,
        'by_philosophy_question': by_question,
        'arkansas_facts': by_category.get('FACT-6000', 0),
        'migrated_from_claims': sum(1 for i in items if i.get('legacy_claim_id')),
        'fact_completeness_pct': round(verified / max(len(items), 1) * 100),
        'v1_target': 200,
        'catalog_gaps': [
            'FEC spending datasets (2010–present) for FACT-4000 series',
            'Buckley v. Valeo primary opinion (EV-ID)',
            'Arkansas Ethics Commission primary sources',
            'Oral argument transcripts',
            'Super PAC formation timeline facts',
            'Congressional reform proposal facts'
        ]
    },
    'items': items
}

out = root / 'data/facts-registry.json'
with open(out, 'w', newline='\n') as f:
    json.dump(registry, f, indent=2)
    f.write('\n')
print(f'Wrote {len(items)} facts — {verified} verified, {needing_review} under review')
