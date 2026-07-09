#!/usr/bin/env python3
"""Fast href/src audit for HTML and JS only."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
LINK = re.compile(r'''(?:href|src)\s*=\s*["']([^"'#?]+)["']''')
broken = {}
checked = 0

for fp in list(root.glob('**/*.html')) + list(root.glob('js/**/*.js')):
    if 'node_modules' in fp.parts:
        continue
    try:
        text = fp.read_text(encoding='utf-8', errors='replace')
    except OSError:
        continue
    base = fp.parent
    for link in LINK.findall(text):
        if link.startswith(('http', '//', 'mailto:', 'tel:', 'data:', '#', '${')):
            continue
        checked += 1
        if link.startswith('/'):
            target = root / link.lstrip('/')
        else:
            target = (base / link).resolve()
        candidates = [target, Path(str(target) + '.html'), target / 'index.html']
        ok = any(c.is_file() for c in candidates) or target.is_dir()
        if not ok:
            broken.setdefault(link, []).append(fp.relative_to(root).as_posix())

print(f'checked={checked} broken_unique={len(broken)}')
for link, srcs in sorted(broken.items(), key=lambda x: -len(x[1])):
    print(f'{len(srcs):4d}  {link}')
    print(f'       e.g. {srcs[0]}')
