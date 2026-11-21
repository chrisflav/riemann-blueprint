"""Derive a provenance label for every statement from its `source` attribute.

published: a plain source (the statement is the published theorem), or "classical"
modified:  a source starting "after" or "special case"
new:       no source, outside the published-results chapter
(none):    sections, chapters, matter, remarks, references, proofs

Run with --apply to write `provenance = "..."` after the `title` line.
"""
import os, re, sys, collections, tomllib

ROOT = 'blueprint'
STATEMENT = {'theorem', 'proposition', 'lemma', 'corollary', 'definition'}
apply = '--apply' in sys.argv

# Judged by hand: known statements without a citable proof, and weakened or
# reformulated forms of published results that carry no `source`.
OVERRIDE = {
    'def-zero-free-primitive': 'published',
    'thm-primitive-suffice': 'published',
    'def-local-parameters': 'modified',
    'def-galois-reps-polarized': 'modified',
    'def-theta-tower-step': 'modified',
    'thm-discrete-series-frame-independent': 'modified',
    'thm-hecke-character-local-parameter-above-l': 'modified',
}
SKIP = {'def-trivial-statement'}
count = collections.Counter()
border = []

for d, _, fs in os.walk(ROOT):
    for f in sorted(fs):
        if not f.endswith('.md') or f.endswith('.proof.md'):
            continue
        p = os.path.join(d, f)
        text = open(p).read()
        parts = text.split('+++', 2)
        if len(parts) < 3:
            continue
        fm = tomllib.loads(parts[1])
        kind = fm.get('kind', '')
        if kind not in STATEMENT:
            continue
        src = fm.get('source')
        in_lit = '/chap-literature/' in p
        oid = fm.get('id') or (os.path.basename(d) if f == '_section.md' else f[:-3])
        if oid in SKIP:
            continue
        if oid in OVERRIDE:
            label = OVERRIDE[oid]
        elif isinstance(src, str) and src.strip():
            s = src.strip().lower()
            label = 'modified' if s.startswith(('after', 'special case')) else 'published'
        else:
            label = 'new'
            if in_lit:
                border.append(('literature chapter without source', p))
        if label == 'new' and kind == 'definition':
            border.append(('definition marked new', p))
        count[label] += 1
        if apply and 'provenance' not in fm:
            head = parts[1]
            line = f'provenance = "{label}"\n'
            m = re.search(r'^title\s*=.*\n', head, re.M)
            head = head[:m.end()] + line + head[m.end():] if m else head.rstrip('\n') + '\n' + line
            open(p, 'w').write('+++' + head + '+++' + parts[2])

print(dict(count))
for why, p in border:
    print(f'{why}: {p}')
