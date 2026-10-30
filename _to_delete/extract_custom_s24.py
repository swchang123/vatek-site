import sys,os,re,glob
sys.path.insert(0,'.')
import generate as G
T=".claude-s25-target/"
NAV_END='    <button class="peek-toggle" aria-label="메뉴 열기">☰</button>\n  </div>\n'
MAINJS='assets/js/main.js"></script>\n'
pages=sys.argv[1:]
out=[]
for rel in pages:
    t=open(T+rel,encoding='utf-8').read()
    depth=rel.count('/'); cur_dir=os.path.dirname(rel)
    title=re.search(r'<title>(.*?) \| VATEK</title>',t,re.S).group(1)
    desc=re.search(r'<meta name="description" content="(.*?)" />\n',t,re.S).group(1)
    i=t.index('style.css" />')+len('style.css" />'); j=t.index('\n</head>'); extra_head=t[i:j]
    m=re.search(r'<body( class="([^"]*)")?>\n',t); body_class=m.group(2)
    nav_start=m.end()
    ne=t.index(NAV_END)+len(NAV_END); nav=t[nav_start:ne]
    assert t[ne]=='\n'; bs=ne+1
    k=t.rindex('\n  <div class="footer-reveal-wrap">'); body=t[bs:k-1]; assert t[k-1]=='\n'
    fe=t.index(MAINJS,k)+len(MAINJS); footer=t[k:fe]
    pre=''
    mj=t.rfind('  <script src=',k,fe); fs=t.find('  </footer>\n  </div>\n',k)+len('  </footer>\n  </div>\n')
    if mj>fs: pre=t[fs:mj]; footer=t[k:fs]+t[mj:fe]
    tail=t[fe:]; assert tail.endswith('\n</body>\n</html>\n'),rel; extra_script=tail[:-len('\n</body>\n</html>\n')]
    # active code
    active=None
    for cand in [None]+[mm['code'] for mm in G.MENU]:
        for hub in (False,True):
            if G.nav_html(depth,cand,hub,cur_dir)+'\n'==nav or G.nav_html(depth,cand,hub,cur_dir)==nav:
                active=(cand,hub); break
        if active: break
    if active is None:
        # try matching nav ignoring my local pexels fix
        print('NAV MISMATCH',rel); 
        gn=G.nav_html(depth,'products',False,cur_dir)
        import difflib
        for l in difflib.unified_diff(gn.split('\n'),nav.split('\n'),lineterm='',n=0): print('   ',l[:160])
        continue
    hero_p=None
    if G.footer_html(depth,None,cur_dir)!=footer:
        pm=re.search(r'<div class="footer-hero-main">\s*<p>(.*?)</p>',footer,re.S)
        cand=pm.group(1) if pm else None
        if cand and G.footer_html(depth,cand,cur_dir)==footer: hero_p=cand
        else:
            print('FOOTER MISMATCH',rel); import difflib
            for l in difflib.unified_diff(G.footer_html(depth,None,cur_dir).split('\n'),footer.split('\n'),lineterm='',n=0): print('   ',l[:160])
            continue
    out.append(dict(path=rel,pre_main_script=pre,active=active[0],is_products_hub=active[1],title=title,desc=desc,extra_head=extra_head,body_class=body_class,body=body,extra_script=extra_script,footer_hero_p=hero_p))
    print('OK',rel,'active',active,'head',len(extra_head),'body',len(body),'script',len(extra_script),'hero_p',bool(hero_p),'class',body_class)
with open('custom_pages.py','w',encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n"""\n(2026-10-19, 24차 핸드오프 §54–§57) 제품 상세 페이지 — 핸드오프 HTML을 그대로 보관하는 커스텀 페이지 목록.\n각 항목은 <head> 추가분(인라인 style 등) · 본문(헤더 아래 ~ 푸터 위) · 하단 인라인 스크립트를 담고,\n상단 메뉴·푸터는 generate.py가 공용 로직으로 붙인다. generate.py의 build_custom_pages()가 사용.\n이 파일은 핸드오프 HTML에서 기계적으로 추출한 것이므로 손으로 고치기보다 다음 핸드오프 때 다시 추출한다.\n"""\n\nCUSTOM_PAGES = [\n')
    for d in out:
        f.write('    {\n')
        for k in ['path','active','is_products_hub','title','desc','body_class','footer_hero_p','extra_head','body','pre_main_script','extra_script']:
            f.write(f'        {k!r}: {d[k]!r},\n')
        f.write('    },\n')
    f.write(']\n')
print('written',len(out))
