import difflib,sys,re,ast,os
T='.claude-s24-target/'
def enc_single(x): return x.replace('\\','\\\\').replace("'","\\'").replace('\n','\\n')
def run(page,const,single,write=False,pyfile='generate.py'):
    src=open(pyfile,encoding='utf-8').read()
    a=src.index('\n'+const+' = ')+1
    m=re.search(r'\n[A-Z_]+ = ',src[a+5:]); b=a+5+m.start()
    blk=src[a:b]
    if single:
        lit=blk[blk.index(' = ')+3:].rstrip('\n'); val=ast.literal_eval(lit); text=val
    else:
        i=blk.index('"""')+3; j=blk.rindex('"""'); text=blk[i:j]
    cur=open(page,encoding='utf-8').read().split('\n'); tgt=open(T+page,encoding='utf-8').read().split('\n')
    ops=[o for o in difflib.SequenceMatcher(None,cur,tgt,autojunk=False).get_opcodes() if o[0]!='equal']
    LO=int(os.environ.get('LO','100')); HI=int(os.environ.get('HI','99999999'))
    SKIP=os.environ.get('SKIP','pexels|submenu-compare-equip|submenu-process|data-i="1b"')
    def skip(o): return any(re.search(SKIP,l) for l in cur[o[1]:o[2]]+tgt[o[3]:o[4]])
    body=[o for o in ops if LO<=o[1]<HI and not skip(o)]
    print(page,'ops',len(body))
    for tag,i1,i2,j1,j2 in reversed(body):
        done=False
        for tot in range(0,12):
            for kp in range(0,tot+1):
                kq=tot-kp
                if i1-kp<0: continue
                oldc='\n'.join(cur[i1-kp:i2+kq]); newc='\n'.join(cur[i1-kp:i1]+tgt[j1:j2]+cur[i2:i2+kq])
                if not oldc: continue
                if text.count(oldc)==1:
                    text=text.replace(oldc,newc); done=True; break
            if done: break
        if not done: print('FAIL',tag,i1+1,i2); return False
    if write:
        if single: new=blk[:blk.index(' = ')+3]+"'"+enc_single(text)+"'"+blk[len(blk.rstrip('\n')):]
        else: new=blk[:i]+text+blk[j:]
        open(pyfile,'w',encoding='utf-8').write(src[:a]+new+src[b:]); print('written',const)
    return True
if __name__=='__main__':
    page,const,single=sys.argv[1],sys.argv[2],sys.argv[3]=='1'
    run(page,const,single,write=len(sys.argv)>4 and sys.argv[4]=='w',pyfile=(sys.argv[5] if len(sys.argv)>5 else 'generate.py'))
