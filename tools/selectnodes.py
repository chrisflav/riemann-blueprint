"""Choose blueprint nodes and compute abstracted uses edges between them."""
import pickle, re, json, collections
d = pickle.load(open('full.pkl', 'rb'))
a = pickle.load(open('ana.pkl', 'rb'))
D = pickle.load(open('dom.pkl', 'rb'))
names, idx, deps, sdeps, sig, files = d['names'], d['index'], d['deps'], d['stmt_deps'], d['sig'], d['files']
nid = {n: i for i, n in enumerate(names)}
size, idom, children = D['size'], D['idom'], D['children']
closure = a['closure']
proves = a['proves']                      # closed Prop -> [theorems]
prop_of = {t: p for p, ts in proves.items() for t in ts}
T = 1000

# 1. dominator nodes, chain-merged: group[v] = representative
sel = [v for v, s in size.items() if s >= T and v != -1]
rep = {}
for v in sorted(sel, key=lambda v: -size[v]):
    p = idom[v]
    if p != -1 and p in rep and size[p] - size[v] < max(30, 0.03 * size[p]):
        rep[v] = rep[p]
    else:
        rep[v] = v
groups = collections.defaultdict(list)
for v, r in rep.items():
    groups[r].append(v)

# 2. literature results: RHS head of each UpperTheory.LiteratureTheorems.* theorem
lit = [i for i in closure if names[i].startswith('UpperTheory.LiteratureTheorems.') and idx[i][2] == 'theorem']
lit_nodes = []
for i in lit:
    s = sig[i] or ''
    m = re.search(r'\)\s*:\s*(\S+)\s*$', s.replace('\n', ' '))
    if not m:
        continue
    target = m.group(1).lstrip('_root_.').replace('_root_.', '')
    lit_nodes.append((i, target))

# 3. assemble node table: key -> set of decl ids
nodes = {}          # key decl -> dict
member = {}         # decl -> key
def add(key, decls, origin):
    if key in member:
        k = member[key]
        for x in decls:
            if x not in member:
                member[x] = k; nodes[k]['decls'].add(x)
        return k
    nodes[key] = {'decls': set(), 'origin': origin}
    for x in [key] + list(decls):
        if x not in member:
            member[x] = key; nodes[key]['decls'].add(x)
    return key

top = ['rhOfAll', 'critAll', 'claimAll', 'allChi',
       'UpperTheory.riemannHypothesis_of_everyCharacter', 'UpperTheory.zeta_ne_zero_of_everyCharacter',
       'Formalism.VW.rh_of_every', 'Formalism.VW.critLine', 'Claim.strip', 'Claim.zeta',
       'UpperTheory.FinalTheorems.everyCharacter', 'UpperTheory.FinalTheorems.everyCharacter_of_row',
       'UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin',
       'UpperTheory.One.vwin_of_row', 'UpperTheory.One.Join.automorphic_window_of_inputs',
       'UpperTheory.Zero.LLC.recTExists', 'UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter',
       'UpperTheory.Lit.every_character_of_theta_integrals_local_matching',
       'UpperTheory.BaseChangeIdentities.baseChangeN']
for n in top:
    if n in nid:
        add(nid[n], [], 'top')
    else:
        print('missing top', n)
for r, vs in groups.items():
    add(r, vs, 'dom')
for i, target in lit_nodes:
    # map literature wrapper to the head constant of its proof term
    extra = []
    if target in nid: extra.append(nid[target])
    for y in set(deps[i] or ()) - set(sdeps[i] or ()):
        if not names[y].startswith('UpperTheory.LiteratureTheorems.'):
            extra.append(y)
    if not extra:
        continue
    hit = next((member[x] for x in extra if x in member), None)
    if hit is not None:
        add(hit, extra, 'lit')
    else:
        add(extra[0], extra[1:], 'lit')
# attach closed Props proved by member theorems
for k in list(nodes):
    for x in list(nodes[k]['decls']):
        p = prop_of.get(x)
        if p is not None and p not in member:
            member[p] = k; nodes[k]['decls'].add(p)

# 4. abstracted uses: walk deps from each member decl, stop at other nodes' members
mapped = member
edges = collections.defaultdict(set)
sedges = collections.defaultdict(set)
THM = ('theorem', 'lemma')
def walk(k, starts, stmt=False):
    out = set(); stack = list(starts); seen = set(nodes[k]['decls'])
    while stack:
        y = stack.pop()
        if y in seen: continue
        seen.add(y)
        if y in mapped:
            if mapped[y] != k:
                out.add(mapped[y])
            continue
        if y in closure:
            if stmt and idx[y][2] in THM:
                stack.extend(sdeps[y] or ())
            else:
                stack.extend(deps[y] or ())
    return out
for k, nd in nodes.items():
    allst = [y for x in nd['decls'] for y in (deps[x] or ())]
    stst = [y for x in nd['decls'] for y in ((sdeps[x] or ()) if idx[x][2] in ('theorem', 'lemma') else (deps[x] or ()))]
    edges[k] = walk(k, allst)
    sedges[k] = walk(k, stst, stmt=True) & edges[k]
print('nodes', len(nodes), 'edges', sum(len(v) for v in edges.values()))
out = []
for k, nd in nodes.items():
    out.append({'key': names[k], 'origin': nd['origin'], 'size': size.get(k, 0),
                'decls': sorted(names[x] for x in nd['decls']),
                'kinds': {names[x]: idx[x][2] for x in nd['decls']},
                'file': files[idx[k][0]], 'line': idx[k][1] + 1,
                'sig': sig[k],
                'uses': sorted(names[e] for e in edges[k]),
                'stmt_uses': sorted(names[e] for e in sedges[k]),
                'idom_chain': None})
# dominator ancestry (nearest selected ancestor) for grouping
for o in out:
    k = nid[o['key']]; p = idom.get(k)
    anc = []
    while p is not None and p != -1:
        if p in member and member[p] != k and names[member[p]] not in anc:
            anc.append(names[member[p]])
        p = idom.get(p) if idom.get(p) != p else None
    o['ancestors'] = anc
json.dump(out, open('nodes.json', 'w'), indent=1, ensure_ascii=False)
