#!/usr/bin/env python3
"""Live Netlify forensic audit — priority paths + HTML crawl sample."""
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = 'https://arkansas-facts.netlify.app'
STALE = 'https://arkansas-citizens-facts.netlify.app'
UA = 'CUF-NetlifyAudit/2.0'

LINK = re.compile(r'''(?:href|src)\s*=\s*["']([^"'#?]+)["']''')


def head(base, path):
    url = base.rstrip('/') + path
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status, r.headers.get('Location', ''), r.headers.get('Content-Type', '')
    except urllib.error.HTTPError as e:
        loc = e.headers.get('Location', '') if e.headers else ''
        return e.code, loc, ''
    except Exception as e:
        return -1, '', str(e)


def get(base, path, n=8000):
    url = base.rstrip('/') + path
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return r.status, r.read(n).decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception:
        return -1, ''


def priority_paths():
    paths = {'/', '/index.html', '/mission-control/', '/mission-control/cursor-implementation-package.html',
             '/builds/', '/explore/', '/data/site.json', '/data/cursor-implementation-package.json'}
    for mf in ROOT.glob('data/*-manifest.json'):
        try:
            data = json.loads(mf.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            continue
        c = data.get('constitution')
        if c:
            paths.add(c)
    pkg = ROOT / 'data/cursor-implementation-package.json'
    if pkg.exists():
        data = json.loads(pkg.read_text(encoding='utf-8'))
        for v in data.values():
            if isinstance(v, dict):
                for k in ('route', 'manifest', 'doc', 'constitution'):
                    if v.get(k):
                        paths.add(v[k])
    for html in ROOT.glob('mission-control/*.html'):
        paths.add('/' + html.relative_to(ROOT).as_posix())
    for html in ROOT.glob('**/*.html'):
        if 'node_modules' in html.parts:
            continue
        paths.add('/' + html.relative_to(ROOT).as_posix())
    return sorted(paths)


def crawl_from_home(base, max_links=120):
    code, html = get(base, '/')
    if code != 200:
        return []
    found = set()
    for link in LINK.findall(html):
        if link.startswith('/') and not link.startswith('//'):
            found.add(link.split('#')[0].split('?')[0])
    # MC package page
    code2, html2 = get(base, '/mission-control/cursor-implementation-package.html')
    if code2 == 200:
        for link in LINK.findall(html2):
            if link.startswith('/') and not link.startswith('//'):
                found.add(link.split('#')[0].split('?')[0])
    return sorted(found)[:max_links]


def audit_domain(base, label, paths):
    ok = fail = redirect = 0
    failures = []
    for p in paths:
        code, loc, ctype = head(base, p)
        if code in (200, 206):
            ok += 1
        elif code in (301, 302, 307, 308):
            redirect += 1
        else:
            fail += 1
            failures.append((p, code, loc))
    print(f'\n=== {label}: {base} ===')
    print(f'Paths checked: {len(paths)} | OK: {ok} | Redirect: {redirect} | FAIL: {fail}')
    for p, code, loc in failures[:60]:
        extra = f' -> {loc}' if loc else ''
        print(f'  {code:4} {p}{extra}')
    if len(failures) > 60:
        print(f'  ... +{len(failures)-60} more failures')
    return fail


def main():
    priority = priority_paths()
    print(f'Priority path count: {len(priority)}')

    crawl = crawl_from_home(CANONICAL)
    print(f'Crawl sample from homepage+MC: {len(crawl)} links')

    all_paths = sorted(set(priority + crawl))
    print(f'Total unique paths to check: {len(all_paths)}')

    f1 = audit_domain(CANONICAL, 'CANONICAL', all_paths)
    f2 = audit_domain(STALE, 'STALE DOMAIN', all_paths)

    print('\n=== CROSS-DOMAIN SPOT CHECK ===')
    spots = [
        '/docs/IMPLEMENTATION_PACKAGE_17_TIME_INTELLIGENCE.md',
        '/data/time-intelligence-manifest.json',
        '/mission-control/cursor-implementation-package.html',
        '/prisma/schema.prisma',
        '/the-story', '/teach', '/sources',
    ]
    for p in spots:
        c1, l1, _ = head(CANONICAL, p)
        c2, l2, _ = head(STALE, p)
        print(f'{p}')
        print(f'  canonical: {c1} {l1}')
        print(f'  stale:     {c2} {l2}')

    return 1 if f1 else (2 if f2 else 0)


if __name__ == '__main__':
    raise SystemExit(main())
