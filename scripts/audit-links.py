#!/usr/bin/env python3
"""Forensic link audit — local filesystem + optional live Netlify check."""
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parents[1]
BASES = [
    'https://arkansas-facts.netlify.app',
    'https://arkansas-citizens-facts.netlify.app',
]

LINK_RE = re.compile(
    r'(?:href|src|action)\s*=\s*["\']([^"\']+)["\']'
    r'|(?:\[[^\]]*\]\(([^)]+)\))'
)

SKIP_PREFIXES = ('http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:', '{{', '${')
SKIP_EXACT = {'', '/'}

# Paths that netlify.toml serves via 301 (no local file required)
NETLIFY_REDIRECTS = {
    '/the-story', '/the-case', '/teach', '/sources', '/what-is-citizens-united',
    '/why-it-matters', '/join/education-leader', '/join/contact-network',
    '/join/event-host', '/join/research-volunteer', '/coalition/sign-on',
}


def collect_files():
    files = []
    for pat in ('**/*.html', 'js/**/*.js', 'data/*.json'):
        for p in root.glob(pat):
            rel = p.relative_to(root).as_posix()
            if rel.startswith('node_modules/'):
                continue
            files.append(p)
    return sorted(set(files))


def extract_links(text):
    links = set()
    for m in LINK_RE.finditer(text):
        for g in m.groups():
            if g:
                links.add(g.strip())
    # manifest constitution paths
    for m in re.finditer(r'"(/[^"]+)"', text):
        v = m.group(1)
        if v.startswith('/') and not v.startswith('//'):
            links.add(v)
    return links


def normalize_path(link):
    if link in SKIP_EXACT or any(link.startswith(p) for p in SKIP_PREFIXES):
        return None
    if link.startswith('//'):
        return None
    path = link.split('#')[0].split('?')[0]
    if not path.startswith('/'):
        return None
    return path


def local_target(path):
    """Map URL path to filesystem path; return exists bool + note."""
    if path in NETLIFY_REDIRECTS:
        return root / path, True, 'netlify-redirect'
    rel = path.lstrip('/')
    if not rel:
        return root / 'index.html', True, 'root'
    candidates = [root / rel]
    if path.endswith('/'):
        candidates = [root / rel / 'index.html', root / (rel.rstrip('/') + '.html')]
    elif not Path(rel).suffix:
        candidates = [
            root / rel / 'index.html',
            root / f'{rel}.html',
            root / rel,
        ]
    for c in candidates:
        if c.is_file():
            return c, True, 'ok'
    # check directory index
    if (root / rel).is_dir() and (root / rel / 'index.html').is_file():
        return root / rel / 'index.html', True, 'dir-index'
    return candidates[0], False, 'missing'


def fetch_status(base, path):
    url = base.rstrip('/') + path
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'CUF-LinkAudit/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.headers.get('Content-Type', '')
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception as e:
        return -1, str(e)


def main():
    live = '--live' in sys.argv
    base = BASES[0]
    for arg in sys.argv[1:]:
        if arg.startswith('http'):
            base = arg.rstrip('/')

    all_links = {}
    for fp in collect_files():
        try:
            text = fp.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        for link in extract_links(text):
            path = normalize_path(link)
            if path:
                all_links.setdefault(path, []).append(fp.relative_to(root).as_posix())

    local_missing = {}
    for path, sources in sorted(all_links.items()):
        target, ok, note = local_target(path)
        if not ok:
            local_missing[path] = {'sources': sources[:5], 'count': len(sources)}

    print(f'=== Link Audit ===')
    print(f'Root: {root}')
    print(f'Unique internal paths: {len(all_links)}')
    print(f'Local missing: {len(local_missing)}')

    if local_missing:
        print('\n--- LOCAL MISSING (top 80) ---')
        for i, (path, info) in enumerate(sorted(local_missing.items())[:80]):
            print(f'404 LOCAL  {path}')
            print(f'           cited from: {info["sources"][0]} (+{info["count"]-1} more)' if info['count'] > 1 else f'           cited from: {info["sources"][0]}')

    # Priority paths from IMP manifests
    priority = []
    for mf in sorted(root.glob('data/*-manifest.json')):
        data = json.loads(mf.read_text(encoding='utf-8'))
        c = data.get('constitution')
        if c:
            priority.append(c)
    for mf in ['data/cursor-implementation-package.json']:
        p = root / mf
        if p.exists():
            data = json.loads(p.read_text(encoding='utf-8'))
            for key in data:
                if isinstance(data[key], dict) and data[key].get('route'):
                    priority.append(data[key]['route'])
                if isinstance(data[key], dict) and data[key].get('manifest'):
                    priority.append(data[key]['manifest'])

    print('\n--- IMP MANIFEST PRIORITY PATHS ---')
    pri_missing = []
    for path in sorted(set(priority)):
        _, ok, _ = local_target(path)
        status = 'OK' if ok else 'MISSING'
        print(f'{status:7} {path}')
        if not ok:
            pri_missing.append(path)

    if live:
        print(f'\n--- LIVE CHECK: {base} ---')
        live_fail = []
        check_paths = sorted(set(list(local_missing.keys()) + priority))[:200]
        for path in check_paths:
            code, ctype = fetch_status(base, path)
            mark = 'OK' if code == 200 else f'FAIL({code})'
            if code != 200:
                live_fail.append((path, code))
            if code != 200 or path in pri_missing:
                print(f'{mark:10} {path}  [{ctype}]')
        print(f'\nLive failures sampled: {len(live_fail)}')

        print(f'\n--- BOTH NETLIFY DOMAINS (homepage + IMP-17) ---')
        for b in BASES:
            for p in ['/', '/mission-control/cursor-implementation-package.html', '/docs/IMPLEMENTATION_PACKAGE_17_TIME_INTELLIGENCE.md', '/data/time-intelligence-manifest.json']:
                code, _ = fetch_status(b, p)
                print(f'{code:4} {b}{p}')

    return 1 if local_missing or pri_missing else 0


if __name__ == '__main__':
    raise SystemExit(main())
