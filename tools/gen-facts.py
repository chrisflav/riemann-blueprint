"""lean-facts.json from the static index, for source links and code snippets.

No Lean is run, so no status, axioms or dependencies are recorded: a
declaration's entry has its kind, its statement as written in the source, its
module and its source range. Names the index does not know (Mathlib's, say)
get no entry, so the blueprint does not report them as missing.

usage: gen-facts.py <full.pkl> <mirror src dir> <blueprint root> <out.json>
"""
import json, os, pickle, re, sys, tomllib

pkl, src, root, out = sys.argv[1:5]
PKG = '.lake/packages/tree/src/'     # where Lake puts the mirror's sources under the root

d = pickle.load(open(pkl, 'rb'))
names, idx, sig, files = d['names'], d['index'], d['sig'], d['files']
nid = {n: i for i, n in enumerate(names)}

KIND = {'theorem': 'theorem', 'lemma': 'theorem', 'def': 'definition', 'abbrev': 'definition',
        'structure': 'structure', 'class': 'structure', 'inductive': 'inductive',
        'instance': 'instance', 'axiom': 'axiom', 'opaque': 'opaque'}
# a line that starts the next top-level item ends the current declaration
NEXT = re.compile(r'^(@\[|theorem|lemma|def|abbrev|structure|class|inductive|instance|axiom|opaque|'
                  r'noncomputable|private|protected|partial|unsafe|namespace|section|end\b|open|'
                  r'variable|universe|attribute|set_option|example|#|macro|syntax|elab|notation|'
                  r'local|scoped|deriving|mutual)')

lines_cache = {}
def end_line(path, start):
    if path not in lines_cache:
        lines_cache[path] = open(os.path.join(src, path), encoding='utf-8', errors='replace').read().split('\n')
    ls = lines_cache[path]
    i = start + 1
    while i < len(ls) and not (ls[i] and not ls[i][0].isspace() and NEXT.match(ls[i])):
        i += 1
    while i - 1 > start and not ls[i - 1].strip():
        i -= 1
    return i  # 1-based last line = index of the line before the next item

wanted = set()
for dd, _, fs in os.walk(os.path.join(root, 'blueprint')):
    for f in fs:
        if f.endswith('.md'):
            t = open(os.path.join(dd, f)).read().split('+++')
            if len(t) >= 3:
                wanted.update(tomllib.loads(t[1]).get('lean', []))

# The main theorems and their statements are declared twice: as `sorry`s in
# Challenge.lean, which Main does not import, and for real in Main.lean and
# Statements.lean. The index kept the first copy it met; take Main's.
REAL = {}
for path in ('Main.lean', 'Statements.lean'):
    ls = open(os.path.join(src, path), encoding='utf-8').read().split('\n')
    for j, l in enumerate(ls):
        m = re.match(r'^(theorem|def) (\S+)', l)
        if m:
            REAL[m.group(2)] = (path, j, m.group(1), l.split(':=')[0].strip())

decls = {}
for n in sorted(wanted):
    i = nid.get(n)
    if n in REAL:
        path, line, kind, s = REAL[n]
    elif i is None:
        continue
    else:
        fi, line, kind = idx[i]
        path = files[fi]
        s = (sig[i] or '').strip()
    last = end_line(path, line)
    if KIND.get(kind) != 'theorem':
        # a definition's content is its body: show the whole declaration
        s = '\n'.join(lines_cache[path][line:last]).rstrip()
    s = '\n'.join(s.split('\n')[:40])
    decls[n] = {
        'exists': True,
        'kind': KIND.get(kind, 'other'),
        'signature': s,
        'module': path[:-5].replace('/', '.'),
        'range': {'file': PKG + path, 'startLine': line + 1, 'endLine': last},
        'doc': None,
    }
# Mathlib's declarations the blueprint names, read from Mathlib at the mirror's
# pin (lake-manifest.json lists Mathlib under .lake/packages/mathlib/).
MATHLIB = {
    'RiemannHypothesis': {
        'kind': 'definition',
        'module': 'Mathlib.NumberTheory.LSeries.RiemannZeta',
        'file': 'Mathlib/NumberTheory/LSeries/RiemannZeta.lean', 'startLine': 185, 'endLine': 186,
        'signature': 'def RiemannHypothesis : Prop :=\n'
                     '  ∀ (s : ℂ) (_ : riemannZeta s = 0) (_ : ¬∃ n : ℕ, s = -2 * (n + 1)) (_ : s ≠ 1), s.re = 1 / 2',
        'doc': 'A formal statement of the **Riemann hypothesis** – constructing a term of this type is '
               'worth a million dollars.',
    },
}
for n, m in MATHLIB.items():
    if n in wanted:
        decls[n] = {'exists': True, 'kind': m['kind'], 'signature': m['signature'], 'module': m['module'],
                    'range': {'file': '.lake/packages/mathlib/' + m['file'],
                              'startLine': m['startLine'], 'endLine': m['endLine']},
                    'doc': m['doc']}

json.dump({'version': 1, 'modules': ['Main'], 'attrMap': {}, 'decls': decls},
          open(out, 'w'), indent=1, ensure_ascii=False, sort_keys=True)
print(f'{len(decls)} of {len(wanted)} names have facts')
