import os,re
B='blueprint'
def oid(p):
    t=open(p).read(); m=re.search(r'^id\s*=\s*"([^"]+)"',t,re.M)
    if m: return m.group(1)
    b=os.path.basename(p)[:-3]; return os.path.basename(os.path.dirname(p)) if b=='_section' else b
def kind(fm):
    m=re.search(r'^kind\s*=\s*"([^"]+)"',fm,re.M); return m.group(1) if m else ''
pub=set()
for root in ('chap-literature','chap-foundations'):
    for d,_,fs in os.walk(f'{B}/{root}'):
        for f in fs:
            if f.endswith('.md') and not f.endswith('.proof.md'):
                p=os.path.join(d,f); fm=open(p).read().split('+++')[1]
                if kind(fm) in ('theorem','lemma','proposition','corollary'): pub.add(oid(p))
CL=r"(Artin|Tate dualit|Euler characteristic|Chebotarev|Siegel–Weil formula|Howe dualit|Bernstein|Zelevinsky|Jacquet|Harish-Chandra|Casselman|Clozel|Green's|Bhatt|Fontaine|Hasse|Landherr|Kato's|Rallis|Flath|Dixmier|Poitou|Greenberg|Moriwaki|Poincaré–Lelong|Zarhin|Fargues|Bloch–Kato|published|literature|Labesse|Weber|Wach module|Herr|Kudla|Weil's convergence)"
HY=r"(Assume|assume|Suppose|Given|Under the hypotheses|provided that|If [^.]{0,80}(holds|hold)\b)"
for d,_,fs in os.walk(B):
    for f in fs:
        if not f.endswith('.md') or f.endswith('.proof.md'): continue
        p=os.path.join(d,f); parts=open(p).read().split('+++',2)
        if len(parts)<3: continue
        fm,body=parts[1],parts[2]
        if kind(fm) not in ('theorem','lemma','proposition','corollary','definition'): continue
        m=re.search(r'^uses\s*=\s*\[(.*?)\]',fm,re.M|re.S); su=set(re.findall(r'"([^"]+)"',m.group(1))) if m else set()
        bad_uses=sorted(su&pub)
        links=set(re.findall(r'\[([a-z0-9-]+)\]',body))|set(re.findall(r'\]\(@([a-z0-9-]+)\)',body))
        hyps=[]
        for sent in re.split(r'(?<=[.;:])\s+',body):
            if re.search(HY,sent) and (re.search(CL,sent) or (set(x for t in re.findall(r'\[([a-z0-9-]+)\]|\(@([a-z0-9-]+)\)',sent) for x in t if x)&pub)):
                hyps.append(sent.strip()[:150].replace('\n',' '))
        if bad_uses or hyps:
            print('==',p.replace(B+'/',''))
            if bad_uses: print('   stmt-uses:',bad_uses)
            for h in hyps: print('   hyp:',h)
