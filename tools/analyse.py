import pickle, re, sys, collections
d = pickle.load(open(sys.argv[1], 'rb'))
names, idx, deps, sdeps, sig, files = d['names'], d['index'], d['deps'], d['stmt_deps'], d['sig'], d['files']
nid = {n: i for i, n in enumerate(names)}
roots = [nid[n] for n in ('rhOfAll','critAll','claimAll','allChi')]
seen = set(roots); st = list(roots)
while st:
    x = st.pop()
    for y in deps[x] or ():
        if y not in seen:
            seen.add(y); st.append(y)
print('closure size', len(seen), 'of', len(names))
# closed named Props
closed = []
pat = re.compile(r'^(?:@\[[^\]]*\]\s*)*(?:noncomputable\s+)?(?:def|abbrev)\s+\S+\s*:\s*Prop\s*$', re.S)
for i in seen:
    s = sig[i] or ''
    if idx[i][2] in ('def', 'abbrev') and pat.match(s.replace('\n', ' ')):
        closed.append(i)
print('closed named Props in closure', len(closed))
cs = set(closed)
# theorems whose statement is exactly a closed Prop
proves = collections.defaultdict(list)
tpat = re.compile(r'^(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+)?(?:theorem|lemma)\s+\S+\s*:\s*(\S+)\s*$')
for i in seen:
    if idx[i][2] in ('theorem', 'lemma'):
        m = tpat.match((sig[i] or '').replace('\n', ' '))
        if m and sdeps[i] and len(sdeps[i]) == 1 and sdeps[i][0] in cs:
            proves[sdeps[i][0]].append(i)
print('closed Props with a direct proof theorem', len(proves))
pickle.dump({'closure': seen, 'closed': closed, 'proves': dict(proves)}, open(sys.argv[2], 'wb'))
by_lib = collections.Counter(files[idx[i][0]].split('/')[0] for i in closed)
print(by_lib)
