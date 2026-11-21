import pickle, sys, collections
import networkx as nx
d = pickle.load(open('full.pkl', 'rb'))
a = pickle.load(open('ana.pkl', 'rb'))
names, idx, deps, sig, files = d['names'], d['index'], d['deps'], d['sig'], d['files']
nid = {n: i for i, n in enumerate(names)}
seen = a['closure']
G = nx.DiGraph()
ROOT = -1
for r in ('rhOfAll', 'critAll', 'claimAll', 'allChi'):
    G.add_edge(ROOT, nid[r])
for x in seen:
    for y in deps[x] or ():
        G.add_edge(x, y)
print('graph', G.number_of_nodes(), G.number_of_edges(), file=sys.stderr)
idom = nx.immediate_dominators(G, ROOT)
children = collections.defaultdict(list)
for v, p in idom.items():
    if v != p:
        children[p].append(v)
# subtree sizes (iterative post-order)
size = {}
order = []
st = [ROOT]
while st:
    v = st.pop(); order.append(v); st.extend(children[v])
for v in reversed(order):
    size[v] = 1 + sum(size[c] for c in children[v])
# own source lines in subtree: approximate by count
pickle.dump({'idom': idom, 'children': dict(children), 'size': size}, open('dom.pkl', 'wb'))
def show(v, depth, maxdepth, thr):
    if depth > maxdepth: return
    kids = sorted(children[v], key=lambda c: -size[c])
    for c in kids:
        if size[c] < thr: break
        print('  ' * depth + f'{size[c]:6d} {idx[c][2]:8s} {names[c]}  [{files[idx[c][0]]}]')
        show(c, depth + 1, maxdepth, thr)
show(ROOT, 0, 12, 2000)
