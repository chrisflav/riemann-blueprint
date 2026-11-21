import pickle
d=pickle.load(open('full.pkl','rb')); names=d['names']; idx=d['index']; files=d['files']
OK=('Supplements/','Main.lean','Statements.lean','BuildAid/','Lemmata/')
bad=set(i for i,n in enumerate(names) if '.' not in n and not files[idx[i][0]].startswith(OK))
print('dropping targets', len(bad))
for k in ('deps','stmt_deps'):
    d[k]=[None if ds is None else [y for y in ds if y not in bad] for ds in d[k]]
pickle.dump(d, open('full.pkl','wb'), protocol=4)
