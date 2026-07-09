"""Generate data/component-registry.json — Build #17 Master Component Registry v1.0"""
import json
from pathlib import Path

def comp(cid, title, category, purpose, status='scaffold', css_class=None, design_ref=None, a11y='WCAG 2.1 AA', mobile='Responsive stack'):
    return {
        'id': cid,
        'title': title,
        'category': category,
        'purpose': purpose,
        'status': status,
        'css_class': css_class,
        'design_system_ref': design_ref,
        'accessibility': a11y,
        'mobile_behavior': mobile,
        'mission_control': 'tracked'
    }

categories = [
    {'id': 'A', 'code': 'NAV', 'title': 'Navigation Components'},
    {'id': 'B', 'code': 'EDU', 'title': 'Educational Components'},
    {'id': 'C', 'code': 'DATA', 'title': 'Data Components'},
    {'id': 'D', 'code': 'CIVIC', 'title': 'Civic Participation Components'},
    {'id': 'E', 'code': 'COAL', 'title': 'Coalition Components'},
    {'id': 'F', 'code': 'MC', 'title': 'Mission Control Components'},
    {'id': 'G', 'code': 'TRUST', 'title': 'Trust Components'},
]

components = [
    # A Navigation
    comp('COMP-NAV-001', 'Global Header', 'A', 'Logo, primary nav, search, Mission Control, Action Hub toggle', 'live', 'site-header', None),
    comp('COMP-NAV-002', 'Primary Navigation', 'A', 'Question-based navigation rather than technical labels', 'partial', 'site-nav'),
    comp('COMP-NAV-003', 'Breadcrumb Navigation', 'A', 'Shows current learning path', 'live', 'breadcrumb'),
    comp('COMP-NAV-004', 'Learning Progress Bar', 'A', 'Visitor position within educational journey', 'partial', 'ladder-strip'),
    # B Educational
    comp('COMP-EDU-001', 'Educational Summary Card', 'B', 'One-minute explanation', 'live', 'lobby-question', 'DSGN-004'),
    comp('COMP-EDU-002', 'Deep Dive Card', 'B', 'Invite readers to explore additional detail', 'live', 'hall-card'),
    comp('COMP-EDU-003', 'Historical Timeline Card', 'B', 'Historical events with expandable detail', 'partial', 'ds-timeline-card', 'DSGN-002'),
    comp('COMP-EDU-004', 'Supreme Court Case Card', 'B', 'Standard format for legal cases', 'live', 'ds-case-card', 'DSGN-003'),
    comp('COMP-EDU-005', 'Constitutional Principle Card', 'B', 'Legal concepts in plain language', 'live', 'ds-concept-card', 'DSGN-004'),
    comp('COMP-EDU-006', 'Fact vs. Interpretation Panel', 'B', 'Distinguish documented facts from analysis', 'partial', 'ds-myth-fact', 'DSGN-006'),
    comp('COMP-EDU-007', 'Primary Source Panel', 'B', 'Highlight original supporting documents', 'live', 'ds-evidence-panel', 'DSGN-007'),
    comp('COMP-EDU-008', 'Related Topics Explorer', 'B', 'Encourage connected learning', 'live', 'explore-further', None),
    # C Data
    comp('COMP-DATA-001', 'Interactive Chart', 'C', 'Data visualization with source links', 'planned', 'ds-data-viz', 'DSGN-011'),
    comp('COMP-DATA-002', 'Timeline Explorer', 'C', 'Full interactive timeline', 'planned'),
    comp('COMP-DATA-003', 'Money Flow Diagram', 'C', 'Political money flow visualization', 'partial', 'money-flow-preview'),
    comp('COMP-DATA-004', 'Comparison Table', 'C', 'Side-by-side policy or argument comparison', 'live', 'ds-comparison', 'DSGN-010'),
    comp('COMP-DATA-005', 'Evidence Summary Panel', 'C', 'Summarize verified evidence with IDs', 'live', 'ds-evidence-panel', 'DSGN-007'),
    # D Civic
    comp('COMP-CIVIC-001', 'Floating Action Hub', 'D', 'Persistent civic actions across platform', 'live', 'action-hub', None),
    comp('COMP-CIVIC-002', 'Education Leader Signup Card', 'D', 'Recruit community educators', 'live', 'ds-leadership-invite', 'DSGN-012'),
    comp('COMP-CIVIC-003', 'Organization Partnership Invitation', 'D', 'ACEI coalition sign-on for Arkansas organizations', 'live', 'entry-pathway--coalition'),
    comp('COMP-CIVIC-004', 'Community Conversation Invitation', 'D', 'Host local education events', 'live', None),
    comp('COMP-CIVIC-005', 'Share With Friends & Family Panel', 'D', 'Relational organizing through educational sharing', 'live', None),
    comp('COMP-CIVIC-006', 'Share Resources With Public Officials', 'D', 'Educational packets for Congress and Arkansas General Assembly', 'stub'),
    comp('COMP-CIVIC-007', 'Model Law Workspace Entry', 'D', 'Educational draft legislation exploration', 'stub'),
    comp('COMP-CIVIC-008', 'Ballot Initiative Lab Entry', 'D', 'Educational ballot initiative workspace', 'stub'),
    # E Coalition
    comp('COMP-COAL-001', 'Coalition Partner Card', 'E', 'Display participating organizations', 'stub', 'proof-card'),
    comp('COMP-COAL-002', 'Organization Profile', 'E', 'Coalition member profile display', 'stub'),
    comp('COMP-COAL-003', 'Coalition Map', 'E', 'Arkansas county visualization', 'partial', None),
    comp('COMP-COAL-004', 'Event Calendar Card', 'E', 'Upcoming educational events', 'stub'),
    comp('COMP-COAL-005', 'Community Resource Library', 'E', 'Partner resource portal', 'partial'),
    # F Mission Control
    comp('COMP-MC-001', 'Executive Summary Panel', 'F', 'Overall project status', 'live', 'mc-executive'),
    comp('COMP-MC-002', 'Phase Progress Card', 'F', 'Phase registry progress', 'live', 'mc-card'),
    comp('COMP-MC-003', 'Build Progress Card', 'F', 'Build history and DNA', 'live', 'entry-card'),
    comp('COMP-MC-004', 'Research Progress Dashboard', 'F', 'Evidence and research readiness', 'live'),
    comp('COMP-MC-005', 'Coalition Growth Dashboard', 'F', 'ACEI coalition metrics', 'live'),
    comp('COMP-MC-006', 'Deployment Status Card', 'F', 'GitHub and Netlify health', 'partial', 'mc-card'),
    comp('COMP-MC-007', 'Educational Readiness Dashboard', 'F', 'Platform preparedness to educate', 'live', 'mc-readiness'),
    # G Trust
    comp('COMP-TRUST-001', 'Citation Panel', 'G', 'Source citations inline and footer', 'live', 'ds-citation', 'DSGN-009'),
    comp('COMP-TRUST-002', 'Source Count Badge', 'G', 'Number of sources supporting content', 'partial', 'ds-trust-bar', 'DSGN-001'),
    comp('COMP-TRUST-003', 'Last Updated Indicator', 'G', 'Content freshness signal', 'partial'),
    comp('COMP-TRUST-004', 'Research Verification Badge', 'G', 'Evidence ID verification status', 'partial'),
    comp('COMP-TRUST-005', 'Page Completeness Indicator', 'G', 'Mission Control completeness per page', 'planned'),
]

by_status = {}
for c in components:
    by_status[c['status']] = by_status.get(c['status'], 0) + 1

out = {
    'version': '1.0',
    'build': 17,
    'updated': '2026-07-09',
    'title': 'Master Component Registry v1.0',
    'scope': 'arkansas',
    'organization': 'Arkansas Civic Education Initiative',
    'platform': 'The Citizens United Education Platform',
    'route': '/mission-control/components.html',
    'constitution': '/docs/COMPONENT_REGISTRY.md',
    'design_system': '/data/design-system.json',
    'brand': '/data/brand-identity.json',
    'principles': [
        'Educate before persuading',
        'Reinforce credibility',
        'Reusable across the platform',
        'Fully responsive',
        'Meet accessibility standards',
        'Integrate with Mission Control',
        'Support future expansion without redesign'
    ],
    'governing_principle': 'The platform should feel like one cohesive educational institution, regardless of how many pages or features are added.',
    'summary': {
        'total_components': len(components),
        'categories': len(categories),
        'live': by_status.get('live', 0),
        'partial': by_status.get('partial', 0),
        'stub': by_status.get('stub', 0),
        'planned': by_status.get('planned', 0),
        'design_system_linked': sum(1 for c in components if c.get('design_system_ref'))
    },
    'categories': categories,
    'components': components,
    'recommended_next_build': {
        'number': 18,
        'title': 'Brand & Identity System',
        'items': ['Permanent project name', 'Logo philosophy', 'Color system', 'Typography', 'Voice', 'Messaging']
    }
}

root = Path(__file__).resolve().parents[1]
with open(root / 'data/component-registry.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f"components: {len(components)} live={by_status.get('live',0)} partial={by_status.get('partial',0)} stub={by_status.get('stub',0)} planned={by_status.get('planned',0)}")
