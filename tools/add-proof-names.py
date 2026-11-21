"""Add to each published-result node the theorems that prove its statement
(sweep/pub.txt: '<A|B> <n> <theorem> :: <statement>  propnode=<id>  <file>')."""
import os, re, tomllib
T = '/home/christian/.claude/jobs/61974794/tmp/'
B = '/home/christian/riemann-hypothesis-blueprint/.claude/worktrees/github-publish/blueprint'

files, used = {}, set()
for d, _, fs in os.walk(B):
    for f in fs:
        if not f.endswith('.md') or f.endswith('.proof.md'):
            continue
        p = os.path.join(d, f)
        parts = open(p).read().split('+++')
        if len(parts) < 3:
            continue
        fm = tomllib.loads(parts[1])
        oid = fm.get('id') or (os.path.basename(d) if f == '_section.md' else f[:-3])
        files[oid] = p
        used.update(fm.get('lean', []))

add = {}
for line in open(T + 'sweep/pub.txt'):
    m = re.match(r'^\S+ \d+ (\S+) :: \S+\s+propnode=(\S+)', line)
    if not m or m.group(2) == 'None':
        continue
    name, node = m.group(1), m.group(2)
    if name in used or node not in files:
        continue
    add.setdefault(node, []).append(name)
    used.add(name)

n = 0
for node, names in sorted(add.items()):
    p = files[node]
    text = open(p).read()
    head, rest = text[3:].split('+++', 1)
    m = re.search(r'^lean\s*=\s*\[(.*?)\]', head, re.M | re.S)
    if not m:
        continue
    extra = ''.join(f',\n         "{x}"' for x in names)
    head = head[:m.end() - 1] + extra + head[m.end() - 1:]
    open(p, 'w').write('+++' + head + '+++' + rest)
    n += len(names)
print(f'added {n} names to {len(add)} nodes')
