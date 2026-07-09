"""Generate data/route-registry.json — Build #16 Route Registry v1.0"""
import json
from pathlib import Path

def r(path, title, question, purposes, status, current, priority='must_launch', group=None):
    return {
        'path': path,
        'title': title,
        'reader_question': question,
        'purposes': purposes,
        'status': status,
        'current_destination': current,
        'launch_priority': priority,
        'group': group
    }

# purposes: educate | trust | civic | mission_control
groups = []

# 1 Public Education
g1 = {
    'id': 'public_education', 'number': 1, 'title': 'Public Education Routes',
    'routes': [
        r('/', 'Homepage', 'How did one Supreme Court decision change American politics?', ['educate', 'civic'], 'live', '/'),
        r('/start-here', 'Start Here', 'Where should I begin?', ['educate'], 'live', '/start-here/', 'must_launch'),
        r('/what-is-citizens-united', 'What Is Citizens United', 'What is Citizens United?', ['educate'], 'redirect', '/start-here/'),
        r('/why-it-matters', 'Why It Matters', 'Why does this still matter?', ['educate'], 'redirect', '/'),
        r('/the-story', 'The Story', 'How did we get here?', ['educate', 'trust'], 'redirect', '/halls/story-before.html'),
        r('/the-case', 'The Case', 'What actually happened?', ['educate', 'trust'], 'redirect', '/halls/the-case.html'),
        r('/the-constitution', 'The Constitution', 'Why did the Court rule this way?', ['educate', 'trust'], 'redirect', '/halls/what-court-decided.html'),
        r('/the-impact', 'The Impact', 'What changed after 2010?', ['educate', 'trust'], 'redirect', '/halls/after-2010.html'),
        r('/follow-the-money', 'Follow the Money', 'How does political money flow?', ['educate', 'trust'], 'redirect', '/halls/money-map.html'),
        r('/the-debate', 'The Debate', 'What are the strongest arguments?', ['educate', 'trust'], 'redirect', '/halls/debate.html'),
        r('/solutions', 'Solutions', 'What can be done?', ['educate', 'civic'], 'redirect', '/solutions/'),
        r('/arkansas', 'Arkansas Hub', 'What does this mean for Arkansas?', ['educate', 'civic'], 'live', '/arkansas/', 'must_launch'),
    ]
}
groups.append(g1)

# 2 Deep-Dive
g2 = {
    'id': 'deep_dive', 'number': 2, 'title': 'Deep-Dive Routes',
    'routes': [
        r('/the-story/timeline', 'Full Timeline', 'What is the full historical timeline?', ['educate', 'trust'], 'planned', None, 'later'),
        r('/the-story/before-2010', 'Before 2010', 'What was political spending like before 2010?', ['educate'], 'redirect', '/halls/story-before.html', 'stub_ok'),
        r('/the-case/majority-opinion', 'Majority Opinion', 'What did the majority say?', ['educate', 'trust'], 'planned', '/halls/what-court-decided.html', 'stub_ok'),
        r('/the-case/dissent', 'Dissent', 'What did the dissent argue?', ['educate', 'trust'], 'planned', '/halls/what-court-decided.html', 'stub_ok'),
        r('/the-case/oral-arguments', 'Oral Arguments', 'What happened at oral argument?', ['educate'], 'planned', '/halls/the-case.html', 'stub_ok'),
        r('/the-constitution/first-amendment', 'First Amendment', 'How does the First Amendment apply?', ['educate'], 'planned', '/halls/what-court-decided.html', 'stub_ok'),
        r('/the-constitution/corporate-speech', 'Corporate Speech', 'What is corporate political speech?', ['educate'], 'planned', '/halls/what-court-decided.html', 'stub_ok'),
        r('/the-impact/spending-data', 'Spending Data', 'What do the numbers show?', ['educate', 'trust'], 'planned', '/halls/after-2010.html', 'later'),
        r('/the-impact/super-pacs', 'Super PACs', 'How did Super PACs grow?', ['educate'], 'redirect', '/halls/after-2010.html', 'stub_ok'),
        r('/the-impact/dark-money', 'Dark Money', 'What is dark money?', ['educate'], 'redirect', '/halls/money-map.html', 'stub_ok'),
        r('/follow-the-money/money-flow-map', 'Money Flow Map', 'How does money move in politics?', ['educate'], 'redirect', '/halls/money-map.html', 'stub_ok'),
    ]
}
groups.append(g2)

# 3 Solutions
g3 = {
    'id': 'solutions_policy', 'number': 3, 'title': 'Solutions & Policy Routes',
    'routes': [
        r('/solutions/federal', 'Federal Options', 'What federal reforms exist?', ['educate'], 'stub', '/solutions/#federal', 'stub_ok'),
        r('/solutions/congress', 'Congress', 'What could Congress do?', ['educate', 'civic'], 'stub', '/action/contact-legislators.html#federal', 'stub_ok'),
        r('/solutions/state', 'State Options', 'What can states do?', ['educate'], 'stub', '/solutions/#state', 'stub_ok'),
        r('/solutions/arkansas-general-assembly', 'Arkansas Legislature', 'What can Arkansas do?', ['educate', 'civic'], 'stub', '/solutions/#arkansas', 'must_launch'),
        r('/solutions/model-laws', 'Model Law Workspace', 'How do we explore model legislation?', ['educate', 'civic'], 'stub', '/action/draft-laws.html', 'stub_ok'),
        r('/solutions/ballot-initiative-lab', 'Ballot Initiative Lab', 'How do ballot initiatives work?', ['educate', 'civic'], 'stub', '/action/ballot-lab.html', 'stub_ok'),
        r('/solutions/montana', 'Montana Case Study', 'What is Montana doing?', ['educate', 'trust'], 'redirect', '/halls/montana-hawaii.html', 'stub_ok'),
        r('/solutions/hawaii', 'Hawaii Case Study', 'What is Hawaii doing?', ['educate', 'trust'], 'redirect', '/halls/montana-hawaii.html', 'stub_ok'),
    ]
}
groups.append(g3)

# 4 Arkansas Civic Action
g4 = {
    'id': 'civic_action', 'number': 4, 'title': 'Arkansas Civic Action Routes',
    'routes': [
        r('/teach', 'Teach Your Community', 'How can I teach my community?', ['educate', 'civic'], 'redirect', '/educate/'),
        r('/teach/conversation-guide', 'Conversation Guide', 'How do I host a conversation?', ['civic'], 'redirect', '/action/community-conversation.html'),
        r('/teach/presentation-toolkit', 'Presentation Toolkit', 'Where are presentation materials?', ['civic'], 'redirect', '/educate/#toolkit'),
        r('/teach/faith-community-toolkit', 'Faith Community Toolkit', 'Resources for faith communities?', ['civic'], 'planned', '/educate/', 'stub_ok'),
        r('/teach/campus-toolkit', 'Campus Toolkit', 'Resources for campuses?', ['civic'], 'planned', '/educate/', 'stub_ok'),
        r('/teach/civic-org-toolkit', 'Civic Org Toolkit', 'Resources for civic organizations?', ['civic'], 'planned', '/educate/', 'stub_ok'),
        r('/join', 'Join Hub', 'How do I get involved?', ['civic'], 'live', '/join/', 'must_launch'),
        r('/join/education-leader', 'Education Leader', 'How do I become an education leader?', ['civic'], 'redirect', '/educate/'),
        r('/join/contact-network', 'Contact Network', 'How do I join the network?', ['civic'], 'redirect', '/action/join-network.html'),
        r('/join/research-volunteer', 'Research Volunteer', 'How do I help with research?', ['civic'], 'planned', '/action/ideas.html', 'stub_ok'),
        r('/join/event-host', 'Event Host', 'How do I host an event?', ['civic'], 'redirect', '/coalition/events.html#submit'),
    ]
}
groups.append(g4)

# 5 Coalition
g5 = {
    'id': 'coalition', 'number': 5, 'title': 'Coalition Routes',
    'routes': [
        r('/coalition', 'Coalition Landing', 'How can my organization partner?', ['civic'], 'redirect', '/coalition/'),
        r('/coalition/sign-on', 'Organization Sign-On', 'How do we sign on?', ['civic'], 'redirect', '/coalition/join.html'),
        r('/coalition/partners', 'Partner Directory', 'Who is in the coalition?', ['civic', 'trust'], 'stub', '/coalition/', 'stub_ok'),
        r('/coalition/resources', 'Resource Portal', 'What resources do partners get?', ['civic'], 'redirect', '/coalition/resources.html'),
        r('/coalition/events', 'Event Calendar', 'What events are happening?', ['civic'], 'redirect', '/coalition/events.html'),
        r('/coalition/county-map', 'County Coalition Map', 'Where are partners across Arkansas?', ['civic', 'mission_control'], 'redirect', '/coalition/counties.html', 'stub_ok'),
    ]
}
groups.append(g5)

# 6 Relational
g6 = {
    'id': 'relational', 'number': 6, 'title': 'Relational Organizing Routes',
    'routes': [
        r('/share', 'Share Hub', 'How do I share this with others?', ['civic'], 'redirect', '/action/share.html'),
        r('/share/friends-family', 'Friends & Family', 'How do I share with people I know?', ['civic'], 'redirect', '/action/share.html#invite'),
        r('/share/resources', 'Shareable Resources', 'What can I share?', ['civic'], 'redirect', '/action/share.html'),
        r('/invite', 'Invite', 'How do I invite someone to learn?', ['civic'], 'redirect', '/action/share.html#invite'),
        r('/referrals', 'Referral Progress', 'How are my referrals doing?', ['civic'], 'stub', '/action/share.html', 'stub_ok'),
    ]
}
groups.append(g6)

# 7 Sources
g7 = {
    'id': 'sources_research', 'number': 7, 'title': 'Source & Research Routes',
    'routes': [
        r('/sources', 'Source Library', 'Where are the primary sources?', ['educate', 'trust'], 'redirect', '/library/'),
        r('/sources/supreme-court', 'Supreme Court Docs', 'Where are court documents?', ['trust'], 'stub', '/library/', 'stub_ok'),
        r('/sources/fec', 'FEC Materials', 'Where is FEC data?', ['trust'], 'planned', '/library/', 'later'),
        r('/sources/spending-data', 'Spending Data', 'Where is spending data?', ['trust'], 'planned', '/halls/money-map.html', 'later'),
        r('/sources/academic', 'Academic Research', 'Where is academic research?', ['trust'], 'planned', '/library/', 'later'),
        r('/sources/state-reforms', 'State Reforms', 'Where are state reform documents?', ['trust'], 'stub', '/solutions/#state', 'stub_ok'),
        r('/glossary', 'Glossary', 'What do these terms mean?', ['educate'], 'planned', None, 'stub_ok'),
        r('/faq', 'FAQ', 'Frequently asked questions?', ['educate'], 'planned', None, 'stub_ok'),
    ]
}
groups.append(g7)

# 8 Mission Control
g8 = {
    'id': 'mission_control', 'number': 8, 'title': 'Mission Control Routes',
    'routes': [
        r('/mission-control', 'Mission Control', 'How is the project progressing?', ['mission_control'], 'live', '/mission-control/'),
        r('/mission-control/phases', 'Phases', 'What phases are complete?', ['mission_control'], 'live', '/mission-control/phases.html'),
        r('/mission-control/builds', 'Builds', 'What has been built?', ['mission_control'], 'redirect', '/builds/'),
        r('/mission-control/research', 'Research Progress', 'How is research progressing?', ['mission_control'], 'live', '/mission-control/research.html'),
        r('/mission-control/content', 'Content Progress', 'What content exists?', ['mission_control'], 'redirect', '/mission-control/inventory.html'),
        r('/mission-control/civic-action', 'Civic Action Progress', 'How is civic action progressing?', ['mission_control'], 'redirect', '/mission-control/civic-ecosystem.html'),
        r('/mission-control/coalition', 'Coalition Progress', 'How is the coalition growing?', ['mission_control'], 'live', '/mission-control/coalition.html'),
        r('/mission-control/deployment', 'Deployment', 'Is the site deployed?', ['mission_control'], 'stub', '/mission-control/', 'stub_ok'),
        r('/mission-control/routes', 'Route Registry', 'What routes exist?', ['mission_control'], 'live', '/mission-control/routes.html', 'must_launch'),
        r('/mission-control/data-model', 'Data Model', 'How is data connected?', ['mission_control'], 'live', '/mission-control/data-model.html'),
    ]
}
groups.append(g8)

# 9 Admin
g9 = {
    'id': 'admin', 'number': 9, 'title': 'Admin Routes',
    'routes': [
        r('/admin', 'Admin Home', 'Internal administration', ['mission_control'], 'redirect', '/admin/mission-control/'),
        r('/admin/mission-control', 'Internal MC', 'Internal mission control', ['mission_control'], 'live', '/admin/mission-control/'),
        r('/admin/signups', 'Signup Review', 'Review signups', ['mission_control'], 'planned', None, 'stub_ok'),
        r('/admin/coalition', 'Coalition Review', 'Review coalition applications', ['mission_control'], 'planned', None, 'stub_ok'),
        r('/admin/events', 'Event Review', 'Review events', ['mission_control'], 'planned', None, 'stub_ok'),
        r('/admin/resources', 'Resource Management', 'Manage resources', ['mission_control'], 'planned', None, 'stub_ok'),
        r('/admin/model-laws', 'Model Law Submissions', 'Review model laws', ['mission_control'], 'planned', '/action/draft-laws.html', 'stub_ok'),
        r('/admin/ballot-lab', 'Ballot Lab Submissions', 'Review ballot concepts', ['mission_control'], 'planned', '/action/ballot-lab.html', 'stub_ok'),
        r('/admin/content', 'Content Registry', 'Content administration', ['mission_control'], 'redirect', '/mission-control/inventory.html', 'stub_ok'),
        r('/admin/research', 'Research Registry', 'Research administration', ['mission_control'], 'redirect', '/mission-control/research.html', 'stub_ok'),
    ]
}
groups.append(g9)

all_routes = [rt for g in groups for rt in g['routes']]
summary = {
    'total_routes': len(all_routes),
    'live': sum(1 for x in all_routes if x['status'] == 'live'),
    'redirect': sum(1 for x in all_routes if x['status'] == 'redirect'),
    'stub': sum(1 for x in all_routes if x['status'] == 'stub'),
    'planned': sum(1 for x in all_routes if x['status'] == 'planned'),
    'must_launch': sum(1 for x in all_routes if x['launch_priority'] == 'must_launch'),
    'stub_ok': sum(1 for x in all_routes if x['launch_priority'] == 'stub_ok'),
    'later': sum(1 for x in all_routes if x['launch_priority'] == 'later'),
}

action_hub_links = [
    {'title': 'Become an Education Leader', 'path': '/educate/', 'status': 'live'},
    {'title': 'Join the Contact Network', 'path': '/action/join-network.html', 'status': 'live'},
    {'title': 'Share This Page', 'path': '/action/share.html', 'status': 'live'},
    {'title': 'Invite Friends & Family', 'path': '/action/share.html#invite', 'status': 'live'},
    {'title': 'Organization Sign-On', 'path': '/coalition/join.html', 'status': 'live'},
    {'title': 'Draft a Model Law', 'path': '/action/draft-laws.html', 'status': 'stub'},
    {'title': 'Explore the Ballot Initiative Lab', 'path': '/action/ballot-lab.html', 'status': 'stub'},
    {'title': 'Share With Public Officials', 'path': '/action/contact-legislators.html', 'status': 'stub'},
    {'title': 'Ask a Question', 'path': '/action/ideas.html', 'status': 'live'},
    {'title': 'Give Feedback', 'path': '/action/ideas.html#feedback', 'status': 'live'},
]

out = {
    'version': '1.0',
    'build': 16,
    'updated': '2026-07-09',
    'title': 'Route Registry v1.0',
    'scope': 'arkansas',
    'route': '/mission-control/routes.html',
    'constitution': '/docs/ROUTE_REGISTRY.md',
    'principle': 'Every route should answer one clear reader question. If a page does not educate, build trust, support civic participation, or help manage the project, it should not exist in Version 1.',
    'purposes': [
        {'id': 'educate', 'title': 'Educate the public'},
        {'id': 'trust', 'title': 'Build trust through evidence'},
        {'id': 'civic', 'title': 'Move readers into community education'},
        {'id': 'mission_control', 'title': 'Track project progress'}
    ],
    'launch_priorities': {
        'must_launch': ['Homepage', 'Start Here', 'What Is Citizens United', 'Why It Matters', 'The Story', 'The Case', 'The Impact', 'Solutions', 'Arkansas', 'Teach', 'Join', 'Coalition', 'Mission Control', 'Source Library'],
        'stub_ok': ['Model Law Workspace', 'Ballot Initiative Lab', 'Partner Directory', 'Referral Progress', 'Advanced Spending Data', 'Admin Dashboards'],
        'later': ['Full interactive data tools', 'AI learning assistant', 'Live GitHub/Netlify dashboard', 'Full county coalition map', 'Public official sharing automation']
    },
    'summary': summary,
    'groups': groups,
    'action_hub_links': action_hub_links
}

root = Path(__file__).resolve().parents[1]
with open(root / 'data/route-registry.json', 'w', newline='\n') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(f"routes: {summary['total_routes']} live={summary['live']} redirect={summary['redirect']} stub={summary['stub']} planned={summary['planned']}")
