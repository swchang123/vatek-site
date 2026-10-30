import difflib,sys,re,ast,os,glob
T='.claude-s25-target/'
SKIP=re.compile(r'pexels|submenu-compare-equip|submenu-process')
FILES=['generate.py','products.py']
def enc_single(x): return x.replace('\\','\\\\').replace("'","\\'").replace('\n','\\n')
def load():
    return {f:open(f,encoding='utf-8').read() for f in FILES}
def const_spans(src):
    # spans of top-level string constants: NAME = '...' / """...""" (end = next top-level statement)
    spans=[]
    for m in re.finditer(r'\n([A-Z][A-Z0-9_]+) = (?=[\'"r])',src):
        a=m.end(); e=re.search(r'\n(?=[A-Za-z_#@])',src[a:]); b=a+(e.start() if e else len(src)-a)
        spans.append((a,b))
    return spans
def in_const(src,o,spans):
    i=src.find(o)
    return any(a<=i<b for a,b in spans)
def blocks(src):
    # top-level constants NAME = '...' or """..."""
    out=[]
    for m in re.finditer(r'\n([A-Z][A-Z0-9_]+) = ',src):
        a=m.start()+1; nm=re.search(r'\n[A-Za-z_@#][^\n]*',src[m.end():])
        # block end: next line starting at col 0 that is not continuation of string: approximate by next top-level stmt
        e=re.search(r'\n(?=[A-Za-z_#@])',src[m.end():])
        b=m.end()+(e.start() if e else len(src)-m.end())
        out.append((m.group(1),a,b))
    return out
def page_const(page,SRC):
    # DETAIL_PAGES entries: {"dir": "industries", "slug": "x", ... "body": NAME}
    d,slug=os.path.dirname(page),os.path.basename(page)[:-5]
    m=re.search(r'\{"dir": "%s", "slug": "%s",.*?"body": ([A-Z0-9_]+)'%(re.escape(d),re.escape(slug)),SRC['generate.py'],re.S)
    if not m: return None
    name=m.group(1); src=SRC['generate.py']
    a=src.index('\n'+name+' = ')+1; e=re.search(r'\n(?=[A-Za-z_#@])',src[a+len(name)+4:]); b=a+len(name)+4+(e.start() if e else 0)
    return (name,a,b)
def apply_page(page,SRC,pyfiles):
    pc=page_const(page,SRC)
    cur=open(page,encoding='utf-8').read().split('\n'); tgt=open(T+page,encoding='utf-8').read().split('\n')
    ops=[o for o in difflib.SequenceMatcher(None,cur,tgt,autojunk=False).get_opcodes() if o[0]!='equal']
    ops=[o for o in ops if o[1]>=100 and not any(SKIP.search(l) for l in cur[o[1]:o[2]]+tgt[o[3]:o[4]])]
    fails=[]
    for tag,i1,i2,j1,j2 in reversed(ops):
        done=False
        for tot in range(0,10):
            for kp in range(0,tot+1):
                kq=tot-kp
                if i1-kp<0 or i2+kq>len(cur): continue
                oldc='\n'.join(cur[i1-kp:i2+kq]); newc='\n'.join(cur[i1-kp:i1]+tgt[j1:j2]+cur[i2:i2+kq])
                if not oldc.strip(): continue
                # find in which file/constant (raw or single-escaped) it occurs exactly once overall
                hits=[]
                if pc:
                    name,a,b=pc; blk=SRC['generate.py'][a:b]
                    for o,n in [(oldc,newc),(enc_single(oldc),enc_single(newc))]:
                        if blk.count(o)==1:
                            SRC['generate.py']=SRC['generate.py'][:a]+blk.replace(o,n)+SRC['generate.py'][b:]; done=True; break
                    if done: break
                for f in pyfiles:
                    s=SRC[f]
                    for enc,o,n in [(False,oldc,newc),(True,enc_single(oldc),enc_single(newc))]:
                        c=s.count(o)
                        if c==1 and in_const(s,o,SPANS[f]): hits.append((f,o,n))
                        elif c>1: hits.append(None)
                hits=[h for h in hits if h is not None] if None not in hits else []
                if len(hits)==1:
                    f,o,n=hits[0]; SRC[f]=SRC[f].replace(o,n); done=True; break
            if done: break
        if not done: fails.append((tag,i1+1,i2,(cur[i1] if i1<len(cur) else '')[:100]))
    return len(ops),fails
if __name__=='__main__':
    pages=sys.argv[1:]
    SRC=load(); SPANS={f:const_spans(SRC[f]) for f in FILES}; total=0; allf={}
    for p in pages:
        n,f=apply_page(p,SRC,FILES); total+=n
        if f: allf[p]=f
    for f in FILES: open(f,'w',encoding='utf-8').write(SRC[f])
    print('ops applied',total,'| pages with failures',len(allf))
    for p,f in allf.items(): print(' ',p,f[:4])
