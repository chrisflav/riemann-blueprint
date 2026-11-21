import os,re,collections
hits=collections.defaultdict(list)
pats={'backtick':r'`','lean':r'\bLean\b','formalis':r'[Ff]ormali[sz]','source':r'\bthe source\b','record':r'\brecords?\b','prop':r'\bProp\b','field-of-structure':r'\bfield of\b','coinage':r'\b(rows?|windows?|hosts?|slots?|bundles?|pages?|ties?|charts?|prints?|leaves|carrier)\b','metaphor':r'(heart of|key role|heavy lifting|machinery|crucial|fundamental|powerful|plays a)'}
for d,_,fs in os.walk('blueprint'):
    for f in fs:
        if not f.endswith('.md') or (d=='blueprint' and f=='intro.md'): continue
        p=os.path.join(d,f); t=open(p).read().split('+++',2)
        body=t[2] if len(t)==3 else ''
        title=re.search(r'^title\s*=\s*"(.*)"',t[1] if len(t)>1 else '',re.M)
        text=body+'\n'+(title.group(1) if title else '')
        text=re.sub(r'\$\$.*?\$\$|\$[^$]*\$','',text,flags=re.S)
        for k,rx in pats.items():
            for m in re.finditer(rx,text): hits[k].append((p,m.group(0)))
for k,v in hits.items():
    print(k,len(v),collections.Counter(x[1].lower() for x in v).most_common(8))
