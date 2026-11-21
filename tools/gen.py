"""nodes.json -> per-chapter work packets with stable ids and uses edges as ids."""
import json, re, collections, os
nodes = json.load(open('nodes.json'))

# Lean names already owned by hand-written nodes -> their ids
import tomllib, glob
BP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'blueprint')
hand_of = {}
HAND = set()
for f in glob.glob(BP + '/**/*.md', recursive=True):
    txt = open(f).read()
    if not txt.startswith('+++'): continue
    fm = tomllib.loads(txt.split('+++')[1])
    base = os.path.basename(f)[:-3]
    oid = fm.get('id') or (os.path.basename(os.path.dirname(f)) if base == '_section' else base)
    HAND.add(oid)
    for n in fm.get('lean', []):
        hand_of[n] = oid

def kebab(s):
    s = re.sub(r'[₀-₉]', lambda m: str(ord(m.group(0)) - 0x2080), s)
    s = re.sub(r"[^A-Za-z0-9_]", '', s)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', s)
    return re.sub(r'[-_]+', '-', s).strip('-').lower()

used = set(HAND)
idof = {}
for o in sorted(nodes, key=lambda o: -o['size']):
    key = o['key']
    if key in hand_of or all(x in hand_of for x in o['decls']):
        idof[key] = hand_of.get(key) or hand_of[o['decls'][0]]; continue
    parts = key.split('.')
    for k in range(1, len(parts) + 1):
        cand = kebab('-'.join(parts[-k:]))
        if cand and cand not in used:
            break
    used.add(cand); idof[key] = cand

TOP = {'UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter': 'galois',
       'UpperTheory.FinalTheorems.everyCharacter_of_row': 'reduction'}
def chapter(o):
    if o['origin'] == 'top':
        return 'architecture'
    if o['origin'] == 'lit':
        return 'literature'
    for a in o['ancestors']:
        if a in TOP:
            return TOP[a]
    return 'shared'

packets = collections.defaultdict(list)
for o in nodes:
    if idof[o['key']] in HAND:
        continue
    o['decls'] = [x for x in o['decls'] if x not in hand_of]
    ch = chapter(o)
    packets[ch].append({
        'id': idof[o['key']], 'lean': o['decls'], 'kinds': o['kinds'],
        'file': o['file'], 'line': o['line'], 'size': o['size'],
        'signature': o['sig'],
        'uses': sorted({idof[u] for u in o['stmt_uses'] if u in idof} - {idof[o['key']]}),
        'proof_uses': sorted({idof[u] for u in o['uses'] if u in idof} - {idof[u] for u in o['stmt_uses'] if u in idof} - {idof[o['key']]}),
        'parent': next((idof[a] for a in o['ancestors'] if a in idof), None),
    })
os.makedirs('packets', exist_ok=True)
for ch, ps in packets.items():
    ps.sort(key=lambda p: -p['size'])
    json.dump(ps, open(f'packets/{ch}.json', 'w'), indent=1, ensure_ascii=False)
    print(ch, len(ps))
json.dump(idof, open('packets/idmap.json', 'w'), indent=1, ensure_ascii=False)
