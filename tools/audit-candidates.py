"""Candidates the dominator selection may have missed: declarations of the proof
that no blueprint node maps, ranked by how widely the proof uses them."""
import json, os, pickle, re, collections, tomllib
T = '/home/christian/.claude/jobs/61974794/tmp/'
BP = '/home/christian/riemann-hypothesis-blueprint/.claude/worktrees/github-publish/blueprint'
d = pickle.load(open(T + 'full.pkl', 'rb'))
names, idx, deps, sdeps, sig, files = d['names'], d['index'], d['deps'], d['stmt_deps'], d['sig'], d['files']
cl = pickle.load(open(T + 'ana.pkl', 'rb'))['closure']
dom = pickle.load(open(T + 'dom.pkl', 'rb'))
size = dom['size']
nid = {n: i for i, n in enumerate(names)}

mapped = set()
for dd, _, fs in os.walk(BP):
    for f in fs:
        if f.endswith('.md'):
            t = open(os.path.join(dd, f)).read().split('+++')
            if len(t) >= 3:
                for n in tomllib.loads(t[1]).get('lean', []):
                    if n in nid: mapped.add(nid[n])

def area(i):
    p = files[idx[i][0]].split('/')
    return '/'.join(p[:3])

indeg = collections.Counter()
spread = collections.defaultdict(set)
stmt_in = collections.Counter()
for x in cl:
    for y in deps[x] or ():
        if y in cl and y != x:
            indeg[y] += 1
            spread[y].add(area(x))
    for y in sdeps[x] or ():
        if y in cl and y != x:
            stmt_in[y] += 1

rows = []
for y in cl:
    if y in mapped: continue
    k = idx[y][2]
    if indeg[y] < 25: continue
    s = (sig[y] or '').replace('\n', ' ')
    rows.append({'name': names[y], 'kind': k, 'file': files[idx[y][0]], 'line': idx[y][1] + 1,
                 'uses': indeg[y], 'areas': len(spread[y]), 'stmt_uses': stmt_in[y],
                 'dominates': size.get(y, 0), 'sig': s[:300]})
rows.sort(key=lambda r: (-r['areas'], -r['uses']))
json.dump(rows[:400], open(T + 'audit-candidates.json', 'w'), indent=1, ensure_ascii=False)
print(len(rows), 'unmapped declarations used >= 25 times')
for r in rows[:40]:
    print(f"{r['areas']:4d} {r['uses']:6d} {r['stmt_uses']:6d} {r['dominates']:6d} {r['kind']:9s} {r['name'][:80]}")

# concepts named in the announcement
KEYS = ['Stepanov', 'Guinand', 'Behrend', 'Iwasawa', 'Vandiver', 'Bost', 'ChowlaSelberg', 'Chowla',
        'IterLift', 'IteratedLift', 'Seesaw', 'SeeSaw', 'Bessel', 'GanGrossPrasad', 'GGP', 'RelativeTrace',
        'Lichtenbaum', 'Mangoldt', 'Parseval', 'Bertini', 'Poincare', 'Mehta', 'Turan', 'Gabber', 'Rallis']
hits = collections.defaultdict(list)
for y in cl:
    n = names[y]
    for kw in KEYS:
        if kw.lower() in n.lower():
            hits[kw].append((size.get(y, 0), indeg[y], y in mapped, n))
summary = {kw: sorted(v, reverse=True)[:12] for kw, v in hits.items()}
json.dump(summary, open(T + 'audit-keywords.json', 'w'), indent=1, ensure_ascii=False)
print()
for kw, v in summary.items():
    print(kw, len(hits[kw]), 'in closure;', sum(1 for x in hits[kw] if x[2]), 'mapped; top:', v[0][3][:70])
