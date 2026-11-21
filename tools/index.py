#!/usr/bin/env python3
"""Static declaration index + approximate reference graph for a Lean source tree.

No Lean needed.  Pass 1 records every declaration's full name (namespace-aware),
file and line.  Pass 2 tokenises each declaration's text and resolves identifiers
against the index (current namespaces, `open`s, then root).  Output: pickle.
"""
import os, re, sys, pickle
from collections import defaultdict

SRC = sys.argv[1]
OUT = sys.argv[2]

DECL_KW = r'(?:theorem|lemma|def|abbrev|structure|class|instance|inductive|axiom|opaque)'
MODS = r'(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|scoped|local)\s+)*'
ATTR = r'(?:@\[[^\]]*\]\s*)*'
decl_re = re.compile(r'^' + ATTR + MODS + r'(?P<kw>' + DECL_KW + r'|class\s+inductive)\s+(?P<name>[^\s:({\[]+)?')
ns_re = re.compile(r'^namespace\s+(\S+)')
sec_re = re.compile(r'^(?:noncomputable\s+)?section\b\s*(\S+)?')
end_re = re.compile(r'^end\b\s*(\S+)?')
open_re = re.compile(r'^(?:open|export)\s+(.*)')
imp_re = re.compile(r'^import\s+(\S+)')
ident_re = re.compile(r'[A-Za-z_Ͱ-Ͽἀ-῿][A-Za-z0-9_\'!?Ͱ-Ͽ₀-ₜἀ-῿]*(?:\.[A-Za-z_Ͱ-Ͽ][A-Za-z0-9_\'!?Ͱ-Ͽ₀-ₜ]*)*')

files = []
for d, _, fs in os.walk(SRC):
    for f in fs:
        if f.endswith('.lean'):
            files.append(os.path.relpath(os.path.join(d, f), SRC))
files.sort()
mod_of = {f: f[:-5].replace('/', '.') for f in files}

def parse(path):
    """yield (kind, fullname, line, text, nsstack, opens) for each decl"""
    with open(os.path.join(SRC, path), encoding='utf-8', errors='replace') as fh:
        lines = fh.read().split('\n')
    stack = []  # list of (type, name) type in ns/sec
    opens = []
    imports = []
    decls = []
    cur = None
    def flush(endline):
        nonlocal cur
        if cur:
            cur['text'] = '\n'.join(lines[cur['line']:endline])
            decls.append(cur)
            cur = None
    for i, ln in enumerate(lines):
        if not ln or ln[0] in ' \t)':
            continue
        m = imp_re.match(ln)
        if m:
            imports.append(m.group(1)); continue
        m = ns_re.match(ln)
        if m:
            flush(i); stack.append(('ns', m.group(1))); continue
        m = sec_re.match(ln)
        if m:
            flush(i); stack.append(('sec', m.group(1) or '')); continue
        m = end_re.match(ln)
        if m:
            flush(i)
            if stack: stack.pop()
            continue
        m = open_re.match(ln)
        if m:
            flush(i)
            body = re.sub(r'\bin\b.*', '', m.group(1))
            body = re.sub(r'\(.*?\)|hiding.*|renaming.*', '', body)
            for tok in body.split():
                if tok in ('scoped', 'Classical'):
                    pass
                prefix = '.'.join(n for t, n in stack if t == 'ns')
                opens.append((prefix, tok))
            continue
        m = decl_re.match(ln)
        if m:
            flush(i)
            kw = m.group('kw').split()[-1]
            name = m.group('name')
            ns = '.'.join(n for t, n in stack if t == 'ns')
            if name is None or kw == 'instance' and (name.startswith(':') or name.startswith('(') or name.startswith('[')):
                name = None
            if name:
                if name.startswith('_root_.'):
                    full = name[7:]
                else:
                    full = (ns + '.' + name) if ns else name
            else:
                full = None
            cur = {'kind': kw, 'name': full, 'line': i, 'ns': ns, 'opens': list(opens)}
            continue
        if re.match(r'^(set_option|attribute|variable|universe|@\[|#|open|local|scoped|notation|macro|syntax|elab|instance|deriving)', ln):
            flush(i)
    flush(len(lines))
    return imports, decls

index = {}     # fullname -> (fileidx, line, kind)
imports = {}
alldecls = {}
print('pass 1', len(files), file=sys.stderr)
for fi, f in enumerate(files):
    imps, decls = parse(f)
    imports[fi] = imps
    alldecls[fi] = decls
    for d in decls:
        if d['name']:
            index.setdefault(d['name'], (fi, d['line'], d['kind']))
            # structures: record fields/ctor loosely via 'mk'
    if fi % 20000 == 0:
        print(fi, len(index), file=sys.stderr)

print('pass 2', file=sys.stderr)
names = sorted(index)
nid = {n: i for i, n in enumerate(names)}
deps = [None] * len(names)
stmt_deps = [None] * len(names)
sig = [None] * len(names)

W = r"[A-Za-z_Ͱ-Ͽ][A-Za-z0-9_'!?Ͱ-Ͽ₀-ₜ]*"
word_re = re.compile(W)
# (a b : T), {a : T}, [inst : C], ⦃a : T⦄ : only runs of plain words
BIND1 = re.compile(r'[(\{\[⦃]\s*((?:' + W + r'\s+)*' + W + r')\s*:(?!=)')
# fun/λ/intro/rintro/∀/∃ x y z  (up to => , : or end)
BIND2 = re.compile(r'(?:\bfun\b|λ|\bintros?\b|\brintro\b|∀|∃|\brename_i\b|\bgeneralizing\b|\bnext\b|\bcase\b|\bat\b)\s+([^\n=:,↦]*)')
# have/let/set/obtain/suffices name
BIND3 = re.compile(r'\b(?:have|let|set|obtain|suffices|show|by_contra!?|by_cases|replace|choose)\s+(' + W + r')')
# with h1 | h2, ⟨a, b, -⟩ patterns: items that are single words
BIND4 = re.compile(r'\bwith\s+([^\n]*)')
BIND5 = re.compile(r'⟨([^⟨⟩]*)⟩')
def local_names(text):
    out = {'this', 'h', 'x', 'y', 'z', 'n', 'm', 'k', 'i', 'j', 's', 't', 'a', 'b', 'c', 'e', 'f', 'g', 'p', 'q', 'r', 'u', 'v', 'w'}
    for rx in (BIND1, BIND2, BIND3):
        for mm in rx.finditer(text):
            out.update(word_re.findall(mm.group(1)))
    for rx in (BIND4, BIND5):
        for mm in rx.finditer(text):
            for item in re.split(r'[,|⟨⟩()]', mm.group(1)):
                item = item.strip()
                if re.fullmatch(W, item):
                    out.add(item)
    return out

def resolve(tok, ns, opens, cache):
    r = cache.get(tok)
    if r is not None:
        return r
    cands = []
    parts = ns.split('.') if ns else []
    for k in range(len(parts), -1, -1):
        cands.append('.'.join(parts[:k] + [tok]))
    for pre, o in opens:
        cands.append(o + '.' + tok)
        if pre:
            cands.append(pre + '.' + o + '.' + tok)
    res = -1
    for c in cands:
        j = nid.get(c)
        if j is not None:
            res = j; break
    if res == -1:
        # try stripping trailing components (dot projections like foo.1 or foo.mp)
        if '.' in tok:
            head = tok.rsplit('.', 1)[0]
            res = resolve(head, ns, opens, cache)
    cache[tok] = res
    return res

for fi, decls in alldecls.items():
    for d in decls:
        if not d['name']:
            continue
        me = nid[d['name']]
        if index[d['name']][0] != fi or index[d['name']][1] != d['line']:
            continue
        text = d['text']
        # split statement (before first ':=' or '| ' or 'where') from body
        m = re.search(r':=|\bwhere\b|^\s*\|', text, re.M)
        cut = m.start() if m else len(text)
        cache = {}
        ds, ss = set(), set()
        locs = local_names(text)
        ns = d['ns']
        own = d['name'].rsplit('.', 1)[0] if '.' in d['name'] else ''
        if own and own != ns:
            ns_opens = d['opens'] + [('', own)]
        else:
            ns_opens = d['opens']
        for mm in ident_re.finditer(text):
            tok = mm.group(0)
            if tok.startswith('_root_.'):
                tok = tok[7:]
                j = nid.get(tok, -1)
                if j < 0 and '.' in tok:
                    j = nid.get(tok.rsplit('.', 1)[0], -1)
            else:
                if tok.split('.')[0] in locs:
                    continue
                j = resolve(tok, ns, ns_opens, cache)
            if j >= 0 and j != me:
                ds.add(j)
                if mm.start() < cut:
                    ss.add(j)
        deps[me] = sorted(ds)
        stmt_deps[me] = sorted(ss)
        sig[me] = text[:cut].strip()[:1500]
    if fi % 20000 == 0:
        print(fi, file=sys.stderr)

with open(OUT, 'wb') as fh:
    pickle.dump({'files': files, 'names': names, 'index': [index[n] for n in names],
                 'deps': deps, 'stmt_deps': stmt_deps, 'sig': sig, 'imports': imports}, fh, protocol=4)
print('done', len(names), file=sys.stderr)
