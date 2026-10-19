# -*- coding: utf-8 -*-
"""
제품 상세 페이지 생성 모듈 (블라스터 / 펠렛타이저 / CO2 리커버리)
coldjet.com의 "카테고리 목록 → 모델 클릭 → Overview / Cold Jet 강점 / Features / Specifications / Accessories 상세"
페이지 구조를 그대로 재현한다.
generate.py의 main()에서 nav_html/footer_html/page_shell/asset 함수를 인자로 받아 사용한다.
"""
import os

# ---------------------------------------------------------------------------
# 블라스터 데이터
# ---------------------------------------------------------------------------

# (2026-10-14, 23차 핸드오프 §55) Aero2 PCS ULTRA · Aero2 PLT ULTRA 제품 상세 페이지 —
# Cold Jet 공식 제품 페이지 구성을 참고한 신규 디자인(au-* 접두, 공용 CSS는 style.css).
# build_model_page()의 데이터 기반 템플릿 대신 핸드오프 HTML 본문(히어로 갤러리~라인업)과
# 하단 인라인 스크립트(갤러리 전환 + 입자 다이얼/압력 게이지)를 그대로 보관해 출력한다.
AERO2_PCS_ULTRA_TITLE = 'Aero2 PCS&reg; ULTRA | 드라이아이스 세척기 (블라스터)'
AERO2_PCS_ULTRA_DESC = 'Aero2 PCS ULTRA — 0.3~3.0mm 28단계 입자 제어, 7인치 LCD, 레시피 저장, Cold Jet CONNECT IoT. 가장 다재다능한 스마트 드라이아이스 블라스터의 사양 · 강점 · 액세서리.'
AERO2_PCS_ULTRA_BODY = """
  <div class="wrap breadcrumb"><a href="../../index.html">홈</a> &gt;
    <a href="../../products/index.html">제품 · 자동화 · 공급</a> &gt;
    <a href="index.html">드라이아이스 세척기 (블라스터)</a> &gt; Aero2 PCS&reg; ULTRA</div>
  <style>
    .au-wrap{max-width:1360px;margin:0 auto;padding:0 clamp(20px,3vw,48px)}
    .au-eyebrow{display:block;font-size:12px;font-weight:800;letter-spacing:.14em;color:var(--blue);margin-bottom:8px}
    .au-sec{padding:48px 0 0;scroll-margin-top:92px}
    .au-sec h2{font-size:26px;color:var(--navy);margin:0 0 8px;letter-spacing:-.01em}
    .au-sec .sub{color:var(--text-muted);font-size:15px;margin:0 0 22px}
    .only{display:inline-block;margin-left:6px;font-size:11px;font-weight:800;color:var(--ice-dark);background:var(--ice-pale);padding:2px 7px;border-radius:999px;vertical-align:middle}
    /* 상단 — 갤러리 + 소개 */
    .au-top{display:grid;grid-template-columns:100px minmax(0,1.6fr) minmax(0,.9fr);gap:28px clamp(28px,3.4vw,56px);align-items:start;padding:40px 0 0}
    .au-thumbs{display:grid;gap:12px;align-content:start}
    .au-thumbs button{display:block;width:100px;height:100px;padding:0;border:1px solid var(--gray-line);border-radius:6px;background:#fff;cursor:pointer;overflow:hidden;transition:border-color .15s,box-shadow .15s}
    .au-thumbs button img{width:100%;height:100%;object-fit:contain;display:block;padding:6px;box-sizing:border-box}
    .au-thumbs button.is-on{border-color:var(--blue);box-shadow:0 0 0 2px var(--blue-light)}
    .au-thumbs button:hover{border-color:var(--blue)}
    .au-stage{position:relative;background:#fff;border-radius:12px;min-height:640px;display:flex;align-items:flex-start;justify-content:center;padding:0 0 28px}
    .au-stage img{width:100%;max-width:820px;height:auto;display:block;transition:opacity .2s}
    .au-stage .cap{position:absolute;left:0;right:0;bottom:6px;text-align:center;font-size:12px;color:var(--text-muted)}
    .au-titleblock{padding-top:32px}
    .au-title{font-size:clamp(34px,4.4vw,52px);line-height:1.1;color:var(--navy);margin:0;font-weight:800;letter-spacing:-.02em}
    .au-title sub{font-size:.5em;vertical-align:-.2em;margin-left:1px}
    .au-titleblock .tagline{font-size:clamp(22px,2.6vw,30px);line-height:1.2;color:var(--blue);margin:8px 0 0;font-weight:600;letter-spacing:-.01em}
    .au-titleblock .tagline b{font-weight:800}
    .au-copy p{font-size:15.5px;line-height:1.75;color:var(--text-body);margin:0 0 16px;text-wrap:pretty}
    .au-copy p a{color:var(--blue);font-weight:700;text-decoration:none}
    .au-copy p a:hover{text-decoration:underline}
    .au-dl{margin:26px 0 0;padding:22px 0 0;border-top:1px solid var(--gray-line)}
    .au-dl h4{font-size:13px;font-weight:800;letter-spacing:.12em;color:var(--navy);margin:0 0 12px}
    .au-dl ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
    .au-dl li a{display:inline-flex;align-items:center;gap:10px;font-size:14.5px;color:var(--navy);font-weight:600;text-decoration:none}
    .au-dl li a:hover{color:var(--blue)}
    .au-dl li a .ic{flex:none;width:30px;height:30px;border-radius:7px;background:var(--blue-light);color:var(--blue);display:grid;place-items:center;font-size:10px;font-weight:800;letter-spacing:.06em}
    .au-dl li a small{color:var(--text-muted);font-weight:500}
    .au-cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
    .au-cta a{display:inline-flex;align-items:center;gap:8px;padding:13px 22px;border-radius:999px;font-size:14.5px;font-weight:800;text-decoration:none}
    .au-cta .pri{background:var(--blue);color:#fff}
    .au-cta .pri:hover{background:var(--blue-dark)}
    .au-cta .sec{border:1.5px solid var(--gray-line);color:var(--navy);background:#fff}
    .au-cta .sec:hover{border-color:var(--blue);color:var(--blue)}
    .au-vsec{margin-top:56px;padding:clamp(48px,6vw,80px) 0}
    .au-vtitle{font-size:26px;font-weight:800;color:var(--navy);margin:0 0 8px;letter-spacing:-.01em}
    .au-video-frame{position:relative;aspect-ratio:16/9;border-radius:14px;overflow:hidden;background:var(--navy-deep);box-shadow:var(--shadow)}
    .au-video-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
    .au-jump{display:flex;flex-wrap:wrap;gap:8px;margin:32px 0 0;padding-top:22px;border-top:1px solid var(--gray-line)}
    .au-jump a{display:inline-flex;align-items:center;gap:6px;padding:9px 14px;border:1px solid var(--gray-line);border-radius:999px;font-size:13px;font-weight:700;color:var(--navy);text-decoration:none;background:#fff}
    .au-jump a:hover{border-color:var(--blue);color:var(--blue)}
    /* PCS 인터랙티브 */
    .au-pc{position:relative;color:#fff;background-color:var(--navy-deep);background-image:repeating-linear-gradient(135deg,rgba(255,255,255,.06) 0,rgba(255,255,255,.06) 1px,transparent 1px,transparent 14px);padding:clamp(64px,8vw,110px) 0;margin-top:56px}
    .au-pc-eyebrow{display:flex;align-items:center;gap:12px;font-size:12.5px;font-weight:800;letter-spacing:3px;color:var(--ice)}
    .au-pc-eyebrow::before{content:"";width:28px;height:2px;background:var(--ice)}
    .au-pc-h2{font-size:clamp(32px,4vw,52px);line-height:1.2;font-weight:800;letter-spacing:-.02em;color:#fff;margin:16px 0 14px;word-break:keep-all}
    .au-pc-sub{font-size:clamp(16px,1.4vw,19px);color:rgba(255,255,255,.75);margin:0 0 clamp(36px,4vw,56px);max-width:720px;line-height:1.7;word-break:keep-all}
    .au-pc-grid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(32px,5vw,80px);align-items:start}
    .au-pc-panel{position:relative}
    .au-pc-frame{position:relative}
    .au-pc-frame-img{display:block;width:100%;filter:drop-shadow(0 16px 30px rgba(0,0,0,.35))}
    .au-pc-num{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);font-size:clamp(18px,1.9vw,24px);font-weight:800;color:#17224d;letter-spacing:-.02em;text-shadow:0 0 5px rgba(255,255,255,.85),0 0 2px rgba(255,255,255,.85)}
    .au-pc-dial{position:absolute;left:50%;top:82%;width:15%;transform:translate(-50%,-50%) rotate(135deg);transform-origin:center;transition:transform .05s linear;touch-action:none;filter:drop-shadow(0 4px 8px rgba(0,0,0,.45))}
    /* 확대 다이얼(.au-pc-zoom/.au-pc-knob…) 규칙은 assets/css/style.css 공용 */
    .au-pc-cap{display:block;margin:18px auto 0;max-width:460px;text-align:center;font-size:14px;line-height:1.6;color:rgba(255,255,255,.8);word-break:keep-all}
    .au-pc-readout{border-top:1px solid rgba(255,255,255,.2);padding-top:22px}
    .au-pc-big{display:flex;align-items:baseline;gap:10px;line-height:1}
    .au-pc-big b{font-size:clamp(56px,7vw,96px);font-weight:800;letter-spacing:-.04em;color:#fff;font-variant-numeric:tabular-nums}
    .au-pc-big span{font-size:clamp(20px,2vw,28px);font-weight:700;color:var(--ice)}
    .au-pc-bar{margin-top:18px}
    .au-pc-line{position:relative;height:40px;display:flex;align-items:flex-end;justify-content:space-between}
    .au-pc-line::before{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:rgba(255,255,255,.18)}
    .au-pc-fill{position:absolute;left:0;bottom:0;top:0;width:100%;background:linear-gradient(90deg,rgba(255,255,255,.1),var(--ice));border-radius:2px 0 0 2px;transition:width .05s linear}
    .au-pc-line i{position:relative;z-index:1;display:block;width:1px;background:rgba(255,255,255,.55);height:14px}
    .au-pc-line i:nth-child(2),.au-pc-line i:nth-child(11),.au-pc-line i:nth-child(20),.au-pc-line i:nth-child(29){height:28px;background:#fff}
    .au-pc-ends{display:flex;justify-content:space-between;margin-top:12px;font-size:13.5px;font-weight:600;color:rgba(255,255,255,.75)}
    .au-pc-modes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:28px}
    .au-pc-modes div{border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:16px 18px;background:rgba(255,255,255,.04)}
    .au-pc-modes b{display:block;font-size:17px;color:#fff;margin-bottom:4px}
    .au-pc-modes span{font-size:14px;color:rgba(255,255,255,.75);line-height:1.5}
    .au-pc-demos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:20px}
    .au-pc-demo{position:relative;aspect-ratio:16/10;border-radius:12px;overflow:hidden;background:#0f1618}
    .au-pc-demo video{display:block;width:100%;height:100%;object-fit:cover}
    #pcVideo1{transform:scale(1.55);transform-origin:center}
    .au-pc-demo-ov{position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;text-align:center;background:rgba(10,16,18,.45);pointer-events:none;transition:opacity .3s}
    .au-pc-demo-ov b{font-size:clamp(18px,1.8vw,24px);font-weight:800}
    .au-pc-demo-ov span{font-size:clamp(16px,1.5vw,20px);font-weight:700;color:var(--ice-pale)}
    .au-pc-demo.is-playing .au-pc-demo-ov{opacity:0}
    .au-pc-play{position:absolute;right:12px;bottom:10px;z-index:2;display:inline-flex;align-items:center;gap:6px;padding:7px 14px 7px 16px;border:2px solid #fff;border-radius:999px;background:rgba(15,22,23,.45);color:#fff;font-size:12px;font-weight:700;cursor:pointer;font-family:inherit}
    .au-pc-play i{font-size:10px;color:var(--ice);font-style:normal}
    .au-pc-play:hover{background:rgba(79,173,184,.3)}
    /* 강점 — 2열 카드: 큰 이미지 + 큰 제목 + 작은 본문 */
    .au-adv-cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:1fr;align-items:stretch;gap:clamp(28px,3.5vw,56px) clamp(24px,3vw,48px);margin-top:8px}
    .au-adv-card{display:grid;grid-template-rows:auto 1fr;height:100%;background:#fff;border:1px solid var(--gray-line);border-radius:16px;overflow:hidden}
    .au-adv-media{aspect-ratio:4/3;width:100%;display:flex;align-items:center;justify-content:center;background:#fff;border-bottom:1px solid var(--gray-line)}
    .au-adv-media img{width:100%;height:100%;object-fit:contain;display:block;padding:6%;box-sizing:border-box}
    .au-adv-media.is-cover img{object-fit:cover;object-position:left top;padding:0}
    .au-adv-copy{padding:22px 26px 28px}
    .au-adv-num{display:block;font-size:12px;font-weight:800;letter-spacing:.14em;color:var(--blue);margin-bottom:10px}
    .au-adv-en{font-size:clamp(22px,2.1vw,30px);line-height:1.15;font-weight:500;letter-spacing:-.005em;color:var(--blue-dark);margin:0 0 8px;text-transform:uppercase;word-break:keep-all}
    .au-adv-ko{font-size:clamp(17px,1.4vw,20px);font-weight:800;color:var(--navy);margin:0 0 12px;line-height:1.4;word-break:keep-all}
    .au-adv-p{font-size:14.5px;line-height:1.75;color:var(--text-body);margin:0;text-wrap:pretty;word-break:keep-all}
    /* 전체 모델 + 필터 */
    .au-lineup{margin-top:clamp(64px,8vw,104px);padding:clamp(56px,7vw,88px) 0 clamp(48px,6vw,72px)}
    .au-lineup .au-model .pic{background:#fff}
    .au-lineup .au-model:hover .pic{background:var(--blue-pale)}
    .au-lineup .au-filter{background:rgba(255,255,255,.6);border-color:rgba(40,55,57,.12)}
    .au-lineup .cta-band{margin-top:clamp(40px,5vw,64px)}
    .au-filter{position:relative;display:inline-flex;flex-wrap:wrap;gap:4px;padding:5px;margin:4px 0 28px;border-radius:999px;background:#eef3f3;border:1px solid var(--gray-line)}
    .au-filter button{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:2px;min-width:118px;padding:10px 18px;border:0;border-radius:999px;background:transparent;cursor:pointer;color:var(--text-muted);font-family:inherit;transition:color .2s}
    .au-filter button b{font-size:12.5px;font-weight:800;letter-spacing:.12em}
    .au-filter button small{font-size:11.5px;font-weight:600;color:currentColor;opacity:.8}
    .au-filter button:hover{color:var(--navy)}
    .au-filter button.is-on{color:var(--navy)}
    .au-filter button.is-on b{color:var(--blue)}
    .au-filter-pill{position:absolute;z-index:0;top:5px;left:5px;height:calc(100% - 10px);width:118px;border-radius:999px;background:#fff;box-shadow:0 2px 10px rgba(40,55,57,.12);transition:left .3s cubic-bezier(.4,0,.2,1),width .3s cubic-bezier(.4,0,.2,1);pointer-events:none}
    .au-models{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:26px 20px;margin-top:8px}
    .au-model.is-hidden{display:none}
    .au-model{animation:auFade .35s ease both}
    @keyframes auFade{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
    .au-model .pic{position:relative}
    .au-model.is-current .pic{box-shadow:inset 0 0 0 2px var(--ice)}
    .au-model-now{position:absolute;left:10px;top:10px;font-size:11px;font-weight:800;letter-spacing:.06em;color:#fff;background:var(--ice-dark);padding:4px 9px;border-radius:999px}
    .au-model{display:flex;flex-direction:column;text-decoration:none;color:inherit}
    .au-model .pic{aspect-ratio:1;display:flex;align-items:center;justify-content:center;background:#f7f9f9;border-radius:14px;padding:10%;box-sizing:border-box;transition:background .2s}
    .au-model:hover .pic{background:var(--blue-pale)}
    .au-model .pic img{width:100%;height:100%;object-fit:contain;display:block;transition:transform .25s}
    .au-model:hover .pic img{transform:scale(1.05)}
    .au-model h3{font-size:16.5px;font-weight:800;color:var(--navy);margin:12px 0 2px}
    .au-model p{font-size:13.5px;color:var(--text-muted);margin:0 0 6px;line-height:1.5}
    .au-model .more{font-size:13px;font-weight:700;color:var(--blue)}
    .au-model:hover .more{text-decoration:underline}
    /* Features · Specs · Accessories 탭 */
    .au-tabs{margin-top:clamp(56px,7vw,96px);scroll-margin-top:92px}
    .au-tabbar{display:flex;justify-content:center;gap:4px;border-bottom:2px solid var(--navy);padding:0 16px}
    .au-tabbar button{position:relative;min-width:170px;padding:18px 28px 20px;border:0;border-radius:6px 6px 0 0;background:var(--blue-light);color:var(--blue-dark);font-size:15.5px;font-weight:700;line-height:1;font-family:inherit;cursor:pointer;transition:background .15s}
    .au-tabbar button:hover{background:#d4e7ea}
    .au-tabbar button.is-on{background:#fff;border:2px solid var(--navy);border-bottom-color:#fff;margin-bottom:-2px;color:var(--navy)}
    .au-tabbar button.is-on::after{content:"";position:absolute;left:50%;bottom:7px;width:0;height:0;margin-left:-5px;border-left:5px solid transparent;border-right:5px solid transparent;border-top:6px solid var(--ice)}
    .au-tabpanel{display:none;padding-top:clamp(28px,3.5vw,44px)}
    .au-tabpanel.is-on{display:block}
    .au-tab-h2{font-size:26px;font-weight:800;color:var(--navy);letter-spacing:-.01em;margin:0 0 8px}
    .au-tab-h2 sub{font-size:.55em;vertical-align:-.2em}
    .au-tab-sub{color:var(--text-muted);font-size:15px;margin:0 0 22px}
    .au-feat-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(28px,4vw,64px);align-items:start}
    .au-feat-pic{display:flex;align-items:center;justify-content:center}
    .au-feat-pic img{width:100%;max-width:560px;height:auto;display:block}
    .au-hotspot{position:relative;width:100%;max-width:560px;margin:0 auto}
    .au-hotspot img{max-width:none}
    .au-hs{position:absolute;width:30px;height:30px;margin:-15px 0 0 -15px;padding:0;border:3px solid #fff;border-radius:50%;background:var(--navy);box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 0 rgba(79,173,184,.55);cursor:pointer;animation:auHs 2.6s ease-out infinite}
    .au-hs:nth-child(odd){animation-delay:1.3s}
    .au-hs:hover,.au-hs.is-on,.au-hs:focus-visible{background:var(--ice);animation:none;outline:none;box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 6px rgba(79,173,184,.3)}
    .au-hs-tip{position:absolute;left:50%;bottom:calc(100% + 12px);transform:translateX(-50%) translateY(6px);width:max-content;max-width:240px;padding:10px 12px;border-radius:10px;background:var(--navy-deep);color:#fff;font-size:13px;line-height:1.5;text-align:left;opacity:0;pointer-events:none;transition:opacity .15s,transform .15s;z-index:3;word-break:keep-all}
    .au-hs-tip b{display:block;font-size:13.5px;color:#9fe3ea;margin-bottom:2px}
    .au-hs-tip::after{content:"";position:absolute;left:50%;top:100%;margin-left:-6px;border:6px solid transparent;border-top-color:var(--navy-deep)}
    .au-hs:hover .au-hs-tip,.au-hs.is-on .au-hs-tip,.au-hs:focus-visible .au-hs-tip{opacity:1;transform:translateX(-50%) translateY(0)}
    .au-hs.is-right .au-hs-tip{left:auto;right:-10px;transform:translateX(0) translateY(6px)}
    .au-hs.is-right:hover .au-hs-tip,.au-hs.is-right.is-on .au-hs-tip{transform:translateX(0) translateY(0)}
    .au-hs.is-right .au-hs-tip::after{left:auto;right:18px;margin-left:0}
    .au-hs.is-below .au-hs-tip{bottom:auto;top:calc(100% + 12px);transform:translateX(-50%) translateY(-6px)}
    .au-hs.is-below:hover .au-hs-tip,.au-hs.is-below.is-on .au-hs-tip,.au-hs.is-below:focus-visible .au-hs-tip{transform:translateX(-50%) translateY(0)}
    .au-hs.is-below .au-hs-tip::after{top:auto;bottom:100%;border-top-color:transparent;border-bottom-color:var(--navy-deep)}
    .au-hs.is-right.is-below .au-hs-tip{transform:translateX(0) translateY(-6px)}
    .au-hs.is-right.is-below:hover .au-hs-tip,.au-hs.is-right.is-below.is-on .au-hs-tip{transform:translateX(0) translateY(0)}
    .au-feat li{transition:color .2s}
    .au-feat li.is-hl{color:var(--navy);font-weight:700}
    .au-feat li.is-hl svg circle{fill:var(--ice-pale)}
    @keyframes auHs{0%{box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 0 rgba(79,173,184,.55)}70%,100%{box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 14px rgba(79,173,184,0)}}
    .au-feat{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px 28px;padding:0;margin:0;list-style:none}
    .au-feat li{display:grid;grid-template-columns:22px 1fr;gap:10px;align-items:start;font-size:15.5px;color:var(--text-body);line-height:1.6;word-break:keep-all}
    .au-feat li svg{width:22px;height:22px;margin-top:2px}
    .au-speclist{list-style:none;margin:0;padding:0;display:grid;gap:0}
    .au-speclist li{display:grid;grid-template-columns:190px 1fr;gap:16px;padding:12px 0;border-bottom:1px solid var(--gray-line);font-size:15px;line-height:1.55}
    .au-speclist li:first-child{border-top:1px solid var(--gray-line)}
    .au-speclist b{color:var(--navy);font-weight:800}
    .au-speclist span{color:var(--text-body)}
    .au-note{font-size:13px;color:var(--text-muted);margin:16px 0 0;line-height:1.6}
    .au-note a{color:var(--blue)}
    .au-tab-sub{font-size:15px;color:var(--text-body);line-height:1.7;margin:-10px 0 28px;max-width:860px;word-break:keep-all}
    .au-acc-h3{font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin:0 0 14px;padding-top:8px}
    .au-acc-h3 small{font-size:13px;font-weight:600;letter-spacing:0;color:var(--text-muted);margin-left:8px}
    .au-accgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px;margin-bottom:36px}
    .au-accgrid.is-3{grid-template-columns:repeat(3,minmax(0,1fr))}
    .au-accgrid article{background:transparent}
    .au-accgrid .pic{aspect-ratio:1;display:flex;align-items:center;justify-content:center}
    .au-accgrid .pic img{width:100%;height:100%;object-fit:contain;display:block;transition:transform .25s}
    .au-accgrid article:hover .pic img{transform:scale(1.04)}
    .au-accgrid h3{font-size:16.5px;color:var(--navy);font-weight:800;margin:0;padding:12px 0 2px}
    .au-accgrid p{margin:0;padding:0 0 6px;font-size:13.5px;color:var(--text-muted);line-height:1.5}
    @media (max-width:1100px){
      .au-top{grid-template-columns:84px minmax(0,1fr);}
      .au-thumbs button{width:84px;height:84px}
      .au-copy{grid-column:1 / -1}
      .au-stage{min-height:380px}
    }
    @media (max-width:960px){
      .au-pc-grid,.au-feat-grid{grid-template-columns:1fr}
      .au-feat-pic{order:-1}.au-feat-pic img{max-width:420px}.au-hotspot{max-width:420px}.au-hotspot img{max-width:none}
      .au-accgrid,.au-accgrid.is-3,.au-models{grid-template-columns:repeat(2,minmax(0,1fr))}
      .au-filter{border-radius:18px}.au-filter button{min-width:0;flex:1 1 30%;padding:9px 10px}.au-filter-pill{border-radius:14px}
      .au-pc-panel{max-width:520px}
      .au-adv-cards{gap:32px 20px}
    }
    @media (max-width:640px){
      .au-top{grid-template-columns:1fr}
      .au-thumbs{grid-auto-flow:column;grid-auto-columns:72px;overflow-x:auto;order:2}
      .au-thumbs button{width:72px;height:72px}
      .au-stage{order:1;min-height:0}
      .au-copy{order:3}
      .au-adv-cards,.au-feat,.au-accgrid,.au-accgrid.is-3{grid-template-columns:1fr}
      .au-tabbar{gap:2px;padding:0 8px}.au-tabbar button{min-width:0;flex:1;padding:14px 8px 16px;font-size:14px}
      .au-speclist li{grid-template-columns:1fr;gap:2px}
      .au-pc-modes,.au-pc-demos{grid-template-columns:1fr}
      .au-pc-knob-hint{display:none}
    }
  </style>

  <section>
    <div class="au-wrap">
      <div class="au-titleblock">
        <h1 class="au-title">The Aero<sub>2</sub> PCS&reg; ULTRA</h1>
        <p class="tagline"><b>ULTRA</b> Versatile Dry Ice Blaster.</p>
      </div>
      <div class="au-top">
        <div class="au-thumbs" id="auThumbs" role="tablist" aria-label="제품 이미지">
          <button type="button" class="is-on" data-src="../../assets/img/aero2-pcs-ultra-front.webp" data-cap="Aero2 PCS ULTRA" aria-label="제품 전면"><img src="../../assets/img/aero2-pcs-ultra-front.webp" alt="" /></button>
          <button type="button" data-src="../../assets/img/aero2-pcs-ultra-side.webp" data-cap="측면 · 호스 연결부" aria-label="제품 측면"><img src="../../assets/img/aero2-pcs-ultra-side.webp" alt="" /></button>
          <button type="button" data-src="../../assets/img/aero2-pcs-ultra-precision-kit.webp" data-cap="Precision Kit 구성" aria-label="Precision Kit"><img src="../../assets/img/aero2-pcs-ultra-precision-kit.webp" alt="" /></button>
          <button type="button" data-src="../../assets/img/aero2-pcs-ultra-performance-kit.webp" data-cap="Performance Kit 구성" aria-label="Performance Kit"><img src="../../assets/img/aero2-pcs-ultra-performance-kit.webp" alt="" /></button>
        </div>
        <div class="au-stage">
          <img id="auStageImg" src="../../assets/img/aero2-pcs-ultra-front.webp" alt="Aero2 PCS ULTRA 드라이아이스 블라스터" />
          <span class="cap" id="auStageCap">Aero2 PCS ULTRA</span>
        </div>
        <div class="au-copy">
          <p>Aero2 PCS ULTRA는 시장에서 가장 다재다능한 드라이아이스 블라스터입니다. 특허받은 입자 제어 시스템(PCS&reg;)을 탑재해 작업자가 분사되는 입자 크기를 완전히 제어하고, 작업마다 분사 조건을 세밀하게 맞출 수 있습니다.</p>
          <p>0.3mm부터 3.0mm까지 0.1mm 단위, 총 28가지 입자 크기 중에서 선택해 최적의 성능을 내는 조건을 찾습니다.</p>
          <p>섬세한 표면을 세척한다면? 0.4mm 같은 작은 입자를 고르고 낮은 압력으로 분사합니다.<br />고착된 오염을 제거해야 한다면? 2.8mm 같은 큰 입자를 고르고 높은 압력으로 분사합니다.</p>
          <p>7인치 LCD 화면과 디지털 컨트롤로 분사 파라미터와 기계 설정을 한눈에 확인하고 손쉽게 조정합니다. 분사 압력 · 입자 크기 · 공급량 같은 조건은 애플리케이션 레시피로 저장해 반복 사용할 수 있으며, 특허 출원 중인 디프로스트(제상) 사이클로 수분 관리와 코어 청소, 가동 시간 향상을 지원합니다.</p>
          <p>PCS ULTRA는 Cold Jet의 Industry 4.0 솔루션 <a href="../../support/techsupport.html">Cold Jet CONNECT&reg;</a>로 연결되는 IoT 장비입니다. 원격 모니터링 · 진단, 교육 영상, 장비 문서, 셀프 트러블슈팅을 제공하며, 추가 지원이 필요하면 채팅 · 서비스 티켓 · 음성/영상 통화로 서비스 기술자와 바로 연결됩니다.</p>
          <div class="au-dl">
            <h4>DOWNLOADS</h4>
            <ul>
              <li><a href="https://www.coldjet.com/wp-content/uploads/0911_SPEC-SHEET_AERO2_ULTRA_2026-06-05_pi_jt.pdf" target="_blank" rel="noopener"><span class="ic">PDF</span>Aero2 ULTRA Spec Sheet <small>· 영문</small></a></li>
              <li><a href="https://www.coldjet.com/wp-content/uploads/0919_CATALOG_AERO2-ULTRA_2026-06-12_jt.pdf" target="_blank" rel="noopener"><span class="ic">PDF</span>Aero2 ULTRA Product Book <small>· 영문</small></a></li>
            </ul>
          </div>
          <div class="au-cta">
            <a class="pri" href="../../products/quote.html">견적 요청</a>
            <a class="sec" href="../../rental/demo-apply.html">데모 테스트 신청</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="au-vsec tint-hatch" id="video">
    <div class="au-wrap">
      <span class="au-eyebrow">VIDEO</span>
      <h2 class="au-vtitle">Aero2 PCS&reg; ULTRA Video</h2>
      <p class="au-tab-sub">PCS ULTRA의 입자 제어와 세척 과정을 영상으로 확인하세요.</p>
      <div class="au-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/XNvx3QblfFk" title="Aero2 PCS ULTRA Video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>
    </div>
  </section>

  <section class="au-pc" id="pcs">
    <div class="au-wrap">
      <span class="au-pc-eyebrow">PARTICLE CONTROL</span>
      <h2 class="au-pc-h2">입자 크기를 바꾸면,<br />세척이 달라집니다.</h2>
      <p class="au-pc-sub">3mm 펠렛을 0.3–3.0mm, 0.1mm 단위 28단계로 — 노즐 교체 없이 다이얼로 조건을 맞춥니다.</p>
      <div class="au-pc-grid">
        <div class="au-pc-panel">
          <div class="au-pc-frame">
            <img class="au-pc-frame-img" src="../../assets/img/pcs-panel-frame.webp" alt="PCS ULTRA 7인치 LCD 컨트롤 패널" />
            <span class="au-pc-num" id="pcNum">3.0</span>
            <img class="au-pc-dial" id="pcDial" src="../../assets/img/pcs-dial-knob.webp" alt="PCS 조절 다이얼" />
          </div>
          <div class="au-pc-zoom">
            <svg class="au-pc-leader" viewBox="0 0 100 60" preserveAspectRatio="none" aria-hidden="true"><path d="M50,0 L50,60" stroke="rgba(255,255,255,.35)" stroke-width="1" stroke-dasharray="3 4" fill="none"></path></svg>
            <div class="au-pc-knob" id="pcKnob" role="slider" tabindex="0" aria-label="입자 크기 다이얼" aria-valuemin="0.3" aria-valuemax="3.0" aria-valuenow="3.0" aria-valuetext="3.0mm">
              <svg class="au-pc-ring" viewBox="0 0 300 300" aria-hidden="true">
                <defs><linearGradient id="pcArcGrad" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#4fadb8"></stop><stop offset="100%" stop-color="#9fe3ea"></stop></linearGradient></defs>
                <path d="M 62.9 237.1 A 125 125 0 1 1 237.1 237.1" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="8" stroke-linecap="round"></path>
                <path id="pcArc" d="M 62.9 237.1 A 125 125 0 1 1 237.1 237.1" fill="none" stroke="url(#pcArcGrad)" stroke-width="8" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="0"></path>
                <g id="pcTicks" stroke="rgba(255,255,255,.55)" stroke-width="1.5"></g>
              </svg>
              <div class="au-pc-knob-face" id="pcKnobFace"><img src="../../assets/img/pcs-dial-knob.webp" alt="" draggable="false" /><i class="au-pc-knob-mark"></i></div>
              <span class="au-pc-knob-min">0.3</span><span class="au-pc-knob-max">3.0</span>
              <span class="au-pc-knob-hint is-l">↺ 작게</span><span class="au-pc-knob-hint is-r">크게 ↻</span>
              <div class="au-pc-guide" aria-hidden="true">
                <div class="au-pc-orbit"><svg class="au-pc-hand" viewBox="0 0 24 24"><path d="M9 11.5V5.2a1.7 1.7 0 0 1 3.4 0V11m0-3.4a1.7 1.7 0 0 1 3.4 0v3.9m0-2.5a1.7 1.7 0 0 1 3.4 0v6.3c0 3.3-2.5 5.7-5.8 5.7h-1.2c-1.9 0-3.4-.7-4.5-2L4.3 15a1.6 1.6 0 0 1 2.4-2.1L9 15.3" fill="#fff" stroke="#1b2426" stroke-width="1.3" stroke-linejoin="round" stroke-linecap="round"/></svg></div>
                <span class="au-pc-guide-label">잡고 돌려보세요</span>
              </div>
            </div>
          </div>
          <span class="au-pc-cap">다이얼을 잡고 돌려보세요 — 시계방향으로 돌리면 입자가 커지고, 반시계방향으로 돌리면 작아집니다. (휠 · 방향키도 가능)</span>
        </div>
        <div class="au-pc-side">
          <div class="au-pc-readout" id="pcScale">
            <div class="au-pc-big"><b id="pcLive">3.0</b><span>mm</span></div>
            <div class="au-pc-bar">
              <div class="au-pc-line"><div class="au-pc-fill" id="pcFill"></div><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
              <div class="au-pc-ends"><span>0.3mm · Micro Particle</span><span>3.0mm · Full Pellet</span></div>
            </div>
          </div>
          <div class="au-pc-modes">
            <div><b>0.4mm · 낮은 압력</b><span>민감한 표면 · 정밀 부품 · 저소음</span></div>
            <div><b>2.8mm · 높은 압력</b><span>고착 오염 · 두꺼운 코팅 · 대형 설비</span></div>
          </div>
          <div class="au-pc-demos">
            <div class="au-pc-demo">
              <video id="pcVideo1" muted loop playsinline preload="none"><source src="../../assets/video/pcs-demo-namecard.mp4" type="video/mp4" /></video>
              <div class="au-pc-demo-ov"><b>Micro Particle</b><span>0.3mm</span></div>
              <button type="button" class="au-pc-play" data-v="pcVideo1" aria-label="영상 재생"><span>영상 재생</span><i>▶</i></button>
            </div>
            <div class="au-pc-demo">
              <video id="pcVideo2" muted loop playsinline preload="none"><source src="../../assets/video/pcs-demo-asphalt.mp4" type="video/mp4" /></video>
              <div class="au-pc-demo-ov"><b>Full Pellet</b><span>3.0mm</span></div>
              <button type="button" class="au-pc-play" data-v="pcVideo2" aria-label="영상 재생"><span>영상 재생</span><i>▶</i></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="au-sec" id="advantage">
    <div class="au-wrap">
      <span class="au-eyebrow">THE COLD JET DIFFERENCE</span>
      <h2>ULTRA TO THE CORE — PCS ULTRA의 강점</h2>
      <p class="sub">모터부터 피더, 제어 펌웨어, 어플리케이터까지 코어를 새로 설계했습니다.</p>
      <div class="au-adv-cards">
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-pcs-infographic.webp" alt="3mm 펠렛을 투입해 28가지 크기로 분사합니다" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">01</span>
            <h3 class="au-adv-en">PARTICLE CONTROL SYSTEM (PCS®)</h3>
            <p class="au-adv-ko">3mm 펠렛을 투입해<br />28가지 크기로 분사합니다</p>
            <p class="au-adv-p">특허받은 입자 제어 시스템(PCS®)은 3mm 드라이아이스 펠렛을 기계 내부에서 0.3~2.9mm로 잘라 분사합니다. 작업자는 0.3mm부터 3.0mm까지 0.1mm 단위, 총 28가지 입자 크기 중에서 작업에 맞는 조건을 선택할 수 있습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-motors.webp" alt="신형 모터 · 기어박스 · 케이블" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">02</span>
            <h3 class="au-adv-en">NEW, STATE-OF-THE-ART MOTORS, GEARBOXES, AND CABLING</h3>
            <p class="au-adv-ko">신형 모터 · 기어박스 · 케이블</p>
            <p class="au-adv-p">ULTRA 시리즈는 내부 부품을 완전히 새로 설계해 신뢰성과 효율을 끌어올렸습니다. 새 모터 어레이는 초저온 환경용 모터로 구성되어 장시간 분사 후에도 멈추지 않고 작동합니다. 여기에 Cold Jet 전용 제어 펌웨어와 모터 드라이버를 적용해 사용 경험을 개선하고 잠재적 오류를 최소화했습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-sureflow.webp" alt="SureFlow 피더 시스템" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">03</span>
            <h3 class="au-adv-en">SUREFLOW FEEDER SYSTEM</h3>
            <p class="au-adv-ko">SureFlow 피더 시스템</p>
            <p class="au-adv-p">특허받은 SureFlow 피더 시스템은 썸퍼 · 램로드 · 진동기와 단열 호퍼를 결합합니다. 호퍼를 최적으로 교반해 드라이아이스가 끊김 없이 시스템을 통과하도록 하여, 일정한 분사 흐름을 만듭니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-defrost.webp" alt="특허 출원 중인 디프로스트(제상) 사이클" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">04</span>
            <h3 class="au-adv-en">PATENT-PENDING DEFROST CYCLE</h3>
            <p class="au-adv-ko">특허 출원 중인 디프로스트(제상) 사이클</p>
            <p class="au-adv-p">PCS ULTRA에는 업계 최초, 특허 출원 중인 제상 사이클이 탑재되어 있습니다. 내부 부품이 얼거나 막혔을 때 자동 또는 수동으로 실행해 가동 중단 시간을 줄입니다. 어플리케이터나 HMI 화면에서 직관적으로 실행할 수 있으며, 최대 2분간 외부 공기를 기계 코어로 불어넣어 해동한 뒤 최소한의 중단으로 작업에 복귀시킵니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-core.webp" alt="코어 오염 제어" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">05</span>
            <h3 class="au-adv-en">CORE CONTAMINATION CONTROL</h3>
            <p class="au-adv-ko">코어 오염 제어</p>
            <p class="au-adv-p">가혹한 환경의 분진과 이물질 문제를 PCS ULTRA의 내부 구조 개선으로 해결했습니다. 입자 제어 시스템 주위에 내부 스커트를 추가해 아주 작은 이물질까지 코어 부품에 닿지 않도록 차단합니다. 그 결과 장비는 더 믿을 수 있게 되었고, 정기 유지보수는 줄었습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media is-cover"><img src="../../assets/img/adv-applicator.webp" alt="초내구성 어플리케이터" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">06</span>
            <h3 class="au-adv-en">ULTRA-DURABLE APPLICATORS</h3>
            <p class="au-adv-ko">초내구성 어플리케이터</p>
            <p class="au-adv-p">Precision · Performance 어플리케이터를 매우 견고하고 정비하기 쉽게 다시 설계했습니다. IP67 등급 부품과 방수 밀폐 커넥터를 적용해 수분 배출 성능을 높였습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-hmi.webp" alt="최대 9개 레시피를 저장하는 스마트 HMI" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">07</span>
            <h3 class="au-adv-en">ULTRA-SMART HMI</h3>
            <p class="au-adv-ko">최대 9개 레시피를 저장하는 스마트 HMI</p>
            <p class="au-adv-p">작업자는 기계에 최대 9개의 레시피를 저장해 특정 작업 · 소재 · 오염물에 맞춘 세척 조건을 바로 불러올 수 있습니다. HMI에는 비밀번호 잠금 기능이 있어, 관리자가 작업자의 설정 변경을 제한함으로써 드라이아이스 과다 사용이나 민감한 표면 손상을 예방할 수 있습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-automation.webp" alt="자동화 · 로봇 통합 대응" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">08</span>
            <h3 class="au-adv-en">AUTOMATION & INTEGRATION CAPABLE</h3>
            <p class="au-adv-ko">자동화 · 로봇 통합 대응</p>
            <p class="au-adv-p">Aero2 ULTRA 시리즈는 자동화 설비나 생산 라인에 통합하는 데 필요한 요소를 갖추고 있습니다. 통합 키트(Integration Kit)를 별도로 구매해 적용합니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-service.webp" alt="QR 코드로 바로 해결하는 서비스 편의성" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">09</span>
            <h3 class="au-adv-en">ULTRA-INTUITIVE SERVICEABILITY</h3>
            <p class="au-adv-ko">QR 코드로 바로 해결하는 서비스 편의성</p>
            <p class="au-adv-p">ULTRA 시리즈의 모든 개선은 최고의 신뢰성과 간결한 사용 경험을 목표로 했습니다. 오류로 기계가 멈추면 작업자가 HMI 화면의 QR 코드를 스캔해 해당 오류의 해결 방법에 바로 접근합니다. 직접 해결하기 어려우면 서비스 티켓을 즉시 제출할 수 있으며, 장비 시리얼 번호 · 펌웨어 버전 · 오류 코드 · 가동 시간 같은 정보가 서비스 부서에 함께 전달됩니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-connectivity.webp" alt="확장된 연결 옵션" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">10</span>
            <h3 class="au-adv-en">EXPANDED CONNECTIVITY OPTIONS</h3>
            <p class="au-adv-ko">확장된 연결 옵션</p>
            <p class="au-adv-p">무선 인터넷 사용이 제한된 현장을 위해 ULTRA 시리즈는 장비 데이터를 추출하는 방법을 넓혔습니다. 접근하기 쉬운 새 외부 패널에 microSD 카드 리더와 이더넷 포트를 두어, 분사 공정의 데이터를 확보하고 제어 · 분석할 수 있습니다.</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="au-tabs" id="details">
    <div class="au-tabbar" role="tablist" aria-label="제품 상세">
      <button type="button" role="tab" class="is-on" aria-selected="true" aria-controls="tabFeatures" id="tabBtnFeatures">Features</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="tabSpecs" id="tabBtnSpecs">Specifications</button>
    </div>
    <div class="au-wrap">
      <div class="au-tabpanel is-on" id="tabFeatures" role="tabpanel" aria-labelledby="tabBtnFeatures">
        <div class="au-feat-grid">
          <div>
            <span class="au-eyebrow">FEATURES</span>
            <h2 class="au-tab-h2">Aero<sub>2</sub> PCS ULTRA Features</h2>
            <p class="au-tab-sub">사진의 점 위에 마우스를 올리면 해당 기능의 위치와 설명을 확인할 수 있습니다.</p>
            <ul class="au-feat">
              <li data-feat="0"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Particle Control&reg; 시스템 — 0.3~3.0mm 28단계 입자 크기로 폭넓은 범용성</span></li>
              <li data-feat="1"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>7인치 LCD 디스플레이 + 디지털 컨트롤</span></li>
              <li data-feat="2"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>직선형(straight-through) 에어 시스템</span></li>
              <li data-feat="3"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>애플리케이션 레시피 저장</span></li>
              <li data-feat="4"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>공기역학적 저부하 에어락 피더(Advanced Aerodynamic Low Load Airlock Feeder)</span></li>
              <li data-feat="5"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>특허받은 고효율 흐름 개시 레귤레이터(Flow Initiation Regulator)</span></li>
              <li data-feat="6"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>특허받은 다이렉트 드라이브 피딩 시스템</span></li>
              <li data-feat="7"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>디프로스트(제상) 사이클 — 특허 출원</span></li>
              <li data-feat="8"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>코어 오염 제어 시스템</span></li>
              <li data-feat="9"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>신형 모터 · 기어박스 · 케이블</span></li>
              <li data-feat="10"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>코팅 공구강급 알루미늄 합금 + 스테인리스 + 폴리머 프레임</span></li>
              <li data-feat="11"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>이동성과 조작성을 고려한 설계</span></li>
              <li data-feat="12"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>IoT — Cold Jet CONNECT&reg;</span></li>
              <li data-feat="13"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>로봇 통합 · 자동화 대응</span></li>
            </ul>
          </div>
          <div class="au-feat-pic au-hotspot" id="auHotspot">
            <img src="../../assets/img/aero2-pcs-ultra-front.webp" alt="Aero2 PCS ULTRA" loading="lazy" />
            <button type="button" class="au-hs is-below" style="left:63.5%;top:12.5%" data-feat="1" aria-label="7인치 LCD · 디지털 컨트롤"><span class="au-hs-tip"><b>7인치 LCD · 디지털 컨트롤</b>입자 크기 · 압력 · 공급량을 한 화면에서 확인하고 레시피를 저장합니다.</span></button>
            <button type="button" class="au-hs is-right is-below" style="left:83.5%;top:27%" data-feat="11" aria-label="인체공학 핸들"><span class="au-hs-tip"><b>인체공학 핸들</b>무게와 크기를 줄인 설계로 이동과 조작이 쉽습니다.</span></button>
            <button type="button" class="au-hs" style="left:34%;top:41%" data-feat="6" aria-label="단열 호퍼 · SureFlow 피더"><span class="au-hs-tip"><b>단열 호퍼 · SureFlow 피더</b>썸퍼 · 램로드 · 진동기가 드라이아이스를 끊김 없이 공급합니다.</span></button>
            <button type="button" class="au-hs" style="left:67%;top:43%" data-feat="2" aria-label="직선형 에어 시스템"><span class="au-hs-tip"><b>직선형 에어 시스템</b>압력 손실과 승화를 최소화하는 straight-through 에어 경로.</span></button>
            <button type="button" class="au-hs" style="left:23%;top:54%" data-feat="10" aria-label="코팅 알루미늄 · 스테인리스 프레임"><span class="au-hs-tip"><b>코팅 알루미늄 · 스테인리스 프레임</b>가혹한 환경을 견디는 공구강급 합금 + 폴리머 프레임.</span></button>
            <button type="button" class="au-hs" style="left:47%;top:55%" data-feat="0" aria-label="Particle Control® 시스템 (PCS)"><span class="au-hs-tip"><b>Particle Control® 시스템 (PCS)</b>3mm 펠렛을 0.3~3.0mm, 28단계로 잘라 분사합니다.</span></button>
            <button type="button" class="au-hs" style="left:67%;top:69%" data-feat="12" aria-label="연결 패널 · 포트"><span class="au-hs-tip"><b>연결 패널 · 포트</b>이더넷 · microSD 포트로 Cold Jet CONNECT®와 연결합니다.</span></button>
            <button type="button" class="au-hs" style="left:43%;top:84%" data-feat="11" aria-label="대형 바퀴 · 기동성"><span class="au-hs-tip"><b>대형 바퀴 · 기동성</b>현장 이동을 고려한 바퀴와 범퍼 설계.</span></button>
          </div>
        </div>
      </div>
      <div class="au-tabpanel" id="tabSpecs" role="tabpanel" aria-labelledby="tabBtnSpecs" hidden>
        <div class="au-feat-grid">
          <div>
            <span class="au-eyebrow">SPECIFICATIONS</span>
            <h2 class="au-tab-h2">Aero<sub>2</sub> PCS ULTRA Specifications</h2>
            <p class="au-tab-sub">Cold Jet 공식 스펙시트(2026-06) 기준입니다.</p>
            <ul class="au-speclist">
              <li><b>크기 (L×W×H)</b><span>98 × 48 × 114 cm (38.5 × 19 × 45 in)</span></li>
              <li><b>무게</b><span>120.6 kg (266 lb)</span></li>
              <li><b>호퍼 용량</b><span>27 kg (60 lb)</span></li>
              <li><b>디스플레이</b><span>7인치 LCD</span></li>
              <li><b>전원</b><span>110/220 VAC (50/60 Hz) · 4.5 A</span></li>
              <li><b>가변 공급량</b><span>0–1.8 kg/min (0–4 lb/min)</span></li>
              <li><b>드라이아이스 입자</b><span>투입 3mm → 분사 0.3–3.0mm</span></li>
              <li><b>분사 압력</b><span>1.4–10 bar (20–145 psi)</span></li>
              <li><b>공급 압력</b><span>2.8–10 bar (40–145 psi)</span></li>
              <li><b>노즐 공기 소비량</b><span>0.3–2.8 m³/min @ 5.5 bar (12–100 cfm @ 80 psi)</span></li>
              <li><b>에어 경로</b><span>3/4 in (19 mm) 직선형 튜빙</span></li>
              <li><b>SureFlow</b><span>썸퍼 · 램로드 · 전동 진동기 · 상시 호퍼 교반 · 단열 호퍼</span></li>
            </ul>
            <p class="au-note">압축공기 조건은 사용 노즐에 따라 달라지며, 컴프레서 용량 검토는 <a href="../compare-equip.html">장비 비교·추천받기</a>에서 도와드립니다.</p>
          </div>
          <div class="au-feat-pic"><img src="../../assets/img/aero2-pcs-ultra-side.webp" alt="Aero2 PCS ULTRA 측면" loading="lazy" /></div>
        </div>
      </div>
    </div>
  </section>

  <section class="au-sec" id="accessories" style="padding-bottom:12px">
    <div class="au-wrap">
      <span class="au-eyebrow">ACCESSORIES</span>
      <h2 class="au-tab-h2">Aero<sub>2</sub> PCS ULTRA Accessories</h2>
      <p class="au-tab-sub">Performance Kit 또는 Precision Kit로 기본 구성하고, 노즐과 어플리케이터로 현장에 맞게 확장합니다.</p>
      <h3 class="au-acc-h3">Nozzles <small>노즐</small></h3>
      <div class="au-accgrid">
        <article><div class="pic"><img src="../../assets/img/acc-nozzles-all.webp" alt="PCS ULTRA 호환 전체 노즐" loading="lazy" /></div><h3>All Nozzles</h3><p>PCS ULTRA 호환 전체 노즐</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-nozzles-low.webp" alt="50–70 cfm · 저소음 · 소형 컴프레서" loading="lazy" /></div><h3>Low Flow Nozzles</h3><p>50–70 cfm · 저소음 · 소형 컴프레서</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-nozzles-standard.webp" alt="100 cfm · 범용 표준" loading="lazy" /></div><h3>Standard Flow Nozzles</h3><p>100 cfm · 범용 표준</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-nozzles-high.webp" alt="140–165 cfm · 최대 세척력" loading="lazy" /></div><h3>High Flow Nozzles</h3><p>140–165 cfm · 최대 세척력</p></article>
      </div>
      <h3 class="au-acc-h3">Applicators <small>어플리케이터</small></h3>
      <div class="au-accgrid">
        <article><div class="pic"><img src="../../assets/img/acc-applicators-all.webp" alt="PCS ULTRA 호환 전체 어플리케이터" loading="lazy" /></div><h3>All Applicators</h3><p>PCS ULTRA 호환 전체 어플리케이터</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-applicator-precision.webp" alt="정밀 세척용 · Precision Kit" loading="lazy" /></div><h3>1/2&quot; Precision Applicator</h3><p>정밀 세척용 · Precision Kit</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-applicator-34.webp" alt="Performance Kit · 4-Function" loading="lazy" /></div><h3>3/4&quot; Applicators</h3><p>Performance Kit · 4-Function</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-applicator-1.webp" alt="Performance Kit · 최대 유량" loading="lazy" /></div><h3>1&quot; Applicators</h3><p>Performance Kit · 최대 유량</p></article>
      </div>
      <p class="au-note">전체 노즐 · 어플리케이터 라인업은 <a href="../nozzle.html">노즐 · 액세서리</a> 페이지에서 확인하실 수 있습니다.</p>
    </div>
  </section>

  <section class="au-sec au-lineup tint-hatch">
    <div class="au-wrap">
      <span class="au-eyebrow">ALL MODELS</span>
      <h2>Cold Jet 블라스터 전체 라인업</h2>
      <p class="sub">세척 대상과 현장 조건에 따라 다른 블라스터도 검토해 보세요. 용도별로 걸러 볼 수 있습니다.</p>
      <div class="au-filter" id="auFilter" role="tablist" aria-label="모델 필터">
        <span class="au-filter-pill" aria-hidden="true"></span>
        <button type="button" data-filter="all" class="is-on" aria-selected="true" role="tab"><b>ALL</b><small>전체 모델</small></button>
        <button type="button" data-filter="core" aria-selected="false" role="tab"><b>CORE</b><small>핵심 모델</small></button>
        <button type="button" data-filter="smart" aria-selected="false" role="tab"><b>SMART</b><small>정밀 제어 · 자동화</small></button>
        <button type="button" data-filter="pellet" aria-selected="false" role="tab"><b>PELLET</b><small>산업 설비 · 고착 오염</small></button>
        <button type="button" data-filter="micro" aria-selected="false" role="tab"><b>MICRO PARTICLE</b><small>정밀 · 민감 표면</small></button>
        <button type="button" data-filter="specialty" aria-selected="false" role="tab"><b>SPECIALTY</b><small>특수 작업</small></button>
      </div>
      <div class="au-models" id="auModels">
        <a class="au-model is-current" href="aero2-ultra.html" data-cat="core smart pellet micro" aria-current="page"><div class="pic"><img src="../../assets/img/blaster-aero2-pcs-ultra-white.webp" alt="Aero2 PCS ULTRA" loading="lazy" /><span class="au-model-now">현재 페이지</span></div><h3>Aero2&reg; PCS ULTRA</h3><p>입자 크기까지 제어하는 스마트 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="aero2-plt-ultra.html" data-cat="smart pellet"><div class="pic"><img src="../../assets/img/blaster-aero2-plt-ultra-white.webp" alt="Aero2 PLT ULTRA" loading="lazy" /></div><h3>Aero2&reg; PLT ULTRA</h3><p>최대 250 psi 풀펠렛 스마트 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="i3-microclean-2.html" data-cat="core micro smart"><div class="pic"><img src="../../assets/img/blaster-i3-microclean-2-white.webp" alt="i MicroClean 2" loading="lazy" /></div><h3>i&sup3; MicroClean&reg; 2</h3><p>2세대 정밀 스마트 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="aero-series.html" data-cat="pellet"><div class="pic"><img src="../../assets/img/blaster-aero-40fp-white.webp" alt="Aero 40FP" loading="lazy" /></div><h3>Aero&reg; 40FP</h3><p>풀프레셔 전문가용 · 호퍼 40 lb</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="aero-series.html" data-cat="pellet"><div class="pic"><img src="../../assets/img/blaster-aero-80fp-white.webp" alt="Aero 80FP" loading="lazy" /></div><h3>Aero&reg; 80FP</h3><p>풀프레셔 전문가용 · 호퍼 80 lb</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="elite20-icerocket.html" data-cat="core pellet micro"><div class="pic"><img src="../../assets/img/blaster-elite-20-white.webp" alt="Elite 20" loading="lazy" /></div><h3>Elite 20</h3><p>실용형 펠렛 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="elite20-icerocket.html" data-cat="core pellet"><div class="pic"><img src="../../assets/img/blaster-icerocket-plt-white.webp" alt="IceRocket PLT" loading="lazy" /></div><h3>IceRocket PLT</h3><p>입문형 펠렛 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="i3-microclean.html" data-cat="micro"><div class="pic"><img src="../../assets/img/blaster-i3-microclean-white.webp" alt="i MicroClean" loading="lazy" /></div><h3>i&sup3; MicroClean&reg;</h3><p>탁상형 정밀 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="sdi-select-60.html" data-cat="micro pellet"><div class="pic"><img src="../../assets/img/blaster-sdi-select-60-white.webp" alt="SDI Select 60" loading="lazy" /></div><h3>SDI Select&trade; 60</h3><p>마이크로파티클 · 펠렛 겸용 범용 모델</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="c100.html" data-cat="specialty"><div class="pic"><img src="../../assets/img/blaster-c100-white.webp" alt="C100" loading="lazy" /></div><h3>C100</h3><p>완전 공압식 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="e-co2-150.html" data-cat="specialty"><div class="pic"><img src="../../assets/img/blaster-e-co2-150-white.webp" alt="E-CO2 150" loading="lazy" /></div><h3>E-CO2&trade; 150</h3><p>연마재 + 드라이아이스 복합 분사</p><span class="more">모델 상세 보기 →</span></a>
      </div>

      <div class="cta-band" style="margin-top:24px;">
        <div>
          <h3>Aero2 PCS&reg; ULTRA 도입을 검토 중이신가요?</h3>
          <p>현장 조건과 컴프레서 사양을 보고 노즐 · 키트 구성까지 함께 안내해 드립니다.</p>
        </div>
        <a class="cta-btn" href="../../products/quote.html">견적문의 하기</a>
      </div>
    </div>
  </section>
"""
AERO2_PCS_ULTRA_SCRIPT = """  <script>
    (function(){
      var rail=document.getElementById('auThumbs'),img=document.getElementById('auStageImg'),cap=document.getElementById('auStageCap');
      if(!rail||!img)return;
      rail.addEventListener('click',function(e){
        var b=e.target.closest('button[data-src]');if(!b)return;
        rail.querySelectorAll('button').forEach(function(x){x.classList.remove('is-on')});b.classList.add('is-on');
        img.style.opacity=0;setTimeout(function(){img.src=b.dataset.src;img.alt=b.dataset.cap;cap.textContent=b.dataset.cap;img.style.opacity=1},150);
      });
    })();
  </script>
  <script>
    (function(){
      var scaleEl=document.getElementById('pcScale'),fill=document.getElementById('pcFill'),live=document.getElementById('pcLive');
      var dial=document.getElementById('pcDial'),num=document.getElementById('pcNum'),knob=document.getElementById('pcKnob'),face=document.getElementById('pcKnobFace'),arc=document.getElementById('pcArc'),ticks=document.getElementById('pcTicks');
      if(!scaleEl||!fill||!live)return;
      var MIN=0.3,MAX=3.0,STEP=0.1,SWEEP=270,ticking=false,touched=false,value=MAX;
      var snap=function(v){return Math.round((v-MIN)/STEP)*STEP+MIN};
      // 눈금 28개 (-135° ~ +135°)
      if(ticks){var h='';for(var i=0;i<28;i++){var a=(-135+i*(SWEEP/27))*Math.PI/180,big=(i%9===0),r1=big?108:113,r2=118;h+='<line x1="'+(150+r1*Math.sin(a)).toFixed(1)+'" y1="'+(150-r1*Math.cos(a)).toFixed(1)+'" x2="'+(150+r2*Math.sin(a)).toFixed(1)+'" y2="'+(150-r2*Math.cos(a)).toFixed(1)+'"'+(big?' stroke="#fff" stroke-width="2"':'')+'></line>'}ticks.innerHTML=h}
      function setValue(v){
        v=snap(Math.min(Math.max(v,MIN),MAX));value=v;
        var f=(v-MIN)/(MAX-MIN),deg=-135+f*SWEEP;
        fill.style.width=(f*100)+'%';live.textContent=v.toFixed(1);if(num)num.textContent=v.toFixed(1);
        if(dial)dial.style.transform='translate(-50%,-50%) rotate('+deg.toFixed(1)+'deg)';
        if(face)face.style.transform='translate(-50%,-50%) rotate('+deg.toFixed(1)+'deg)';
        if(arc)arc.style.strokeDashoffset=(1-f).toFixed(4);
        if(knob){knob.setAttribute('aria-valuenow',v.toFixed(1));knob.setAttribute('aria-valuetext',v.toFixed(1)+'mm')}
      }
      // 스크롤 연동 — 사용자가 다이얼을 만지기 전까지만
      function onScrollUpdate(){
        ticking=false;if(touched)return;
        var r=scaleEl.getBoundingClientRect(),a=window.innerHeight*0.85,b=window.innerHeight*0.25;
        var p=Math.min(Math.max((a-r.top)/(a-b+r.height),0),1);
        setValue(MAX-p*(MAX-MIN));
      }
      function req(){if(!ticking){ticking=true;requestAnimationFrame(onScrollUpdate)}}
      window.addEventListener('scroll',req,{passive:true});window.addEventListener('resize',req);onScrollUpdate();
      // 다이얼 돌리기 — 포인터 각도 변화량 누적 (시계방향 = 커짐)
      if(knob){
        var turning=false,lastA=0,acc=0;
        var angleOf=function(e){var r=knob.getBoundingClientRect();return Math.atan2(e.clientY-(r.top+r.height/2),e.clientX-(r.left+r.width/2))*180/Math.PI};
        var markTouched=function(){touched=true;knob.classList.add('is-touched')};
        knob.addEventListener('pointerdown',function(e){markTouched();turning=true;knob.classList.add('is-turning');knob.setPointerCapture(e.pointerId);lastA=angleOf(e);acc=(value-MIN)/(MAX-MIN)*SWEEP;e.preventDefault()});
        knob.addEventListener('pointermove',function(e){
          if(!turning)return;var a=angleOf(e),d=a-lastA;if(d>180)d-=360;if(d<-180)d+=360;lastA=a;
          acc=Math.min(Math.max(acc+d,0),SWEEP);setValue(MIN+acc/SWEEP*(MAX-MIN));
        });
        var stop=function(e){if(!turning)return;turning=false;knob.classList.remove('is-turning');try{knob.releasePointerCapture(e.pointerId)}catch(x){}};
        knob.addEventListener('pointerup',stop);knob.addEventListener('pointercancel',stop);
        knob.addEventListener('wheel',function(e){markTouched();setValue(value+(e.deltaY<0?STEP:-STEP));e.preventDefault()},{passive:false});
        knob.addEventListener('keydown',function(e){var k=e.key;if(k==='ArrowRight'||k==='ArrowUp'){markTouched();setValue(value+STEP);e.preventDefault()}else if(k==='ArrowLeft'||k==='ArrowDown'){markTouched();setValue(value-STEP);e.preventDefault()}});
      }
      var hs=document.querySelectorAll('#auHotspot .au-hs'),fl=document.querySelectorAll('#tabFeatures .au-feat li');
      function hl(btn){hs.forEach(function(b){b.classList.toggle('is-on',b===btn)});fl.forEach(function(li){li.classList.toggle('is-hl',!!btn&&li.dataset.feat===btn.dataset.feat)})}
      hs.forEach(function(b){b.addEventListener('mouseenter',function(){hl(b)});b.addEventListener('mouseleave',function(){hl(null)});b.addEventListener('focus',function(){hl(b)});b.addEventListener('blur',function(){hl(null)});b.addEventListener('click',function(e){e.preventDefault()})});
      var hsBox=document.getElementById('auHotspot');if(hsBox)hsBox.addEventListener('mouseleave',function(){hl(null)});
      var fBox=document.getElementById('auFilter'),fPill=fBox&&fBox.querySelector('.au-filter-pill'),fBtns=fBox?fBox.querySelectorAll('button'):[],cards=document.querySelectorAll('#auModels .au-model');
      function movePill(b){if(!fPill)return;fPill.style.left=b.offsetLeft+'px';fPill.style.top=b.offsetTop+'px';fPill.style.width=b.offsetWidth+'px';fPill.style.height=b.offsetHeight+'px'}
      fBtns.forEach(function(b){b.addEventListener('click',function(){
        fBtns.forEach(function(x){x.classList.remove('is-on');x.setAttribute('aria-selected','false')});b.classList.add('is-on');b.setAttribute('aria-selected','true');movePill(b);
        var k=b.dataset.filter;cards.forEach(function(c){var show=k==='all'||(' '+c.dataset.cat+' ').indexOf(' '+k+' ')>-1;c.classList.toggle('is-hidden',!show);if(show){c.style.animation='none';void c.offsetWidth;c.style.animation=''}});
      })});
      if(fBtns.length){movePill(fBox.querySelector('.is-on'));window.addEventListener('resize',function(){movePill(fBox.querySelector('.is-on'))})}
      var tabs=document.querySelectorAll('.au-tabbar [role=tab]');
      tabs.forEach(function(b){b.addEventListener('click',function(){
        tabs.forEach(function(x){x.classList.remove('is-on');x.setAttribute('aria-selected','false');var p=document.getElementById(x.getAttribute('aria-controls'));if(p){p.classList.remove('is-on');p.hidden=true}});
        b.classList.add('is-on');b.setAttribute('aria-selected','true');var p=document.getElementById(b.getAttribute('aria-controls'));if(p){p.classList.add('is-on');p.hidden=false}
      })});
      document.querySelectorAll('.au-pc-play').forEach(function(btn){
        btn.addEventListener('click',function(){
          var v=document.getElementById(btn.dataset.v),box=btn.parentNode;if(!v)return;
          if(v.paused){v.play();box.classList.add('is-playing');btn.querySelector('span').textContent='일시정지';btn.querySelector('i').textContent='❚❚'}
          else{v.pause();box.classList.remove('is-playing');btn.querySelector('span').textContent='영상 재생';btn.querySelector('i').textContent='▶'}
        });
      });
    })();
  </script>
"""
AERO2_PLT_ULTRA_TITLE = 'Aero2 PLT&reg; ULTRA | 드라이아이스 세척기 (블라스터)'
AERO2_PLT_ULTRA_DESC = 'Aero2 PLT ULTRA — 최대 250 psi(17.2 bar), 분당 2.7kg 풀펠렛 분사. 7인치 LCD, 레시피 저장, Cold Jet CONNECT IoT. 가장 강력한 스마트 드라이아이스 블라스터의 사양 · 강점 · 액세서리.'
AERO2_PLT_ULTRA_BODY = """
  <div class="wrap breadcrumb"><a href="../../index.html">홈</a> &gt;
    <a href="../../products/index.html">제품 · 자동화 · 공급</a> &gt;
    <a href="index.html">드라이아이스 세척기 (블라스터)</a> &gt; Aero2 PLT&reg; ULTRA</div>
  <style>
    .au-wrap{max-width:1360px;margin:0 auto;padding:0 clamp(20px,3vw,48px)}
    .au-eyebrow{display:block;font-size:12px;font-weight:800;letter-spacing:.14em;color:var(--blue);margin-bottom:8px}
    .au-sec{padding:48px 0 0;scroll-margin-top:92px}
    .au-sec h2{font-size:26px;color:var(--navy);margin:0 0 8px;letter-spacing:-.01em}
    .au-sec .sub{color:var(--text-muted);font-size:15px;margin:0 0 22px}
    .only{display:inline-block;margin-left:6px;font-size:11px;font-weight:800;color:var(--ice-dark);background:var(--ice-pale);padding:2px 7px;border-radius:999px;vertical-align:middle}
    /* 상단 — 갤러리 + 소개 */
    .au-top{display:grid;grid-template-columns:100px minmax(0,1.6fr) minmax(0,.9fr);gap:28px clamp(28px,3.4vw,56px);align-items:start;padding:40px 0 0}
    .au-thumbs{display:grid;gap:12px;align-content:start}
    .au-thumbs button{display:block;width:100px;height:100px;padding:0;border:1px solid var(--gray-line);border-radius:6px;background:#fff;cursor:pointer;overflow:hidden;transition:border-color .15s,box-shadow .15s}
    .au-thumbs button img{width:100%;height:100%;object-fit:contain;display:block;padding:6px;box-sizing:border-box}
    .au-thumbs button.is-on{border-color:var(--blue);box-shadow:0 0 0 2px var(--blue-light)}
    .au-thumbs button:hover{border-color:var(--blue)}
    .au-stage{position:relative;background:#fff;border-radius:12px;min-height:640px;display:flex;align-items:flex-start;justify-content:center;padding:0 0 28px}
    .au-stage img{width:100%;max-width:820px;height:auto;display:block;transition:opacity .2s}
    .au-stage .cap{position:absolute;left:0;right:0;bottom:6px;text-align:center;font-size:12px;color:var(--text-muted)}
    .au-titleblock{padding-top:32px}
    .au-title{font-size:clamp(34px,4.4vw,52px);line-height:1.1;color:var(--navy);margin:0;font-weight:800;letter-spacing:-.02em}
    .au-title sub{font-size:.5em;vertical-align:-.2em;margin-left:1px}
    .au-titleblock .tagline{font-size:clamp(22px,2.6vw,30px);line-height:1.2;color:var(--blue);margin:8px 0 0;font-weight:600;letter-spacing:-.01em}
    .au-titleblock .tagline b{font-weight:800}
    .au-copy p{font-size:15.5px;line-height:1.75;color:var(--text-body);margin:0 0 16px;text-wrap:pretty}
    .au-copy p a{color:var(--blue);font-weight:700;text-decoration:none}
    .au-copy p a:hover{text-decoration:underline}
    .au-dl{margin:26px 0 0;padding:22px 0 0;border-top:1px solid var(--gray-line)}
    .au-dl h4{font-size:13px;font-weight:800;letter-spacing:.12em;color:var(--navy);margin:0 0 12px}
    .au-dl ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
    .au-dl li a{display:inline-flex;align-items:center;gap:10px;font-size:14.5px;color:var(--navy);font-weight:600;text-decoration:none}
    .au-dl li a:hover{color:var(--blue)}
    .au-dl li a .ic{flex:none;width:30px;height:30px;border-radius:7px;background:var(--blue-light);color:var(--blue);display:grid;place-items:center;font-size:10px;font-weight:800;letter-spacing:.06em}
    .au-dl li a small{color:var(--text-muted);font-weight:500}
    .au-cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
    .au-cta a{display:inline-flex;align-items:center;gap:8px;padding:13px 22px;border-radius:999px;font-size:14.5px;font-weight:800;text-decoration:none}
    .au-cta .pri{background:var(--blue);color:#fff}
    .au-cta .pri:hover{background:var(--blue-dark)}
    .au-cta .sec{border:1.5px solid var(--gray-line);color:var(--navy);background:#fff}
    .au-cta .sec:hover{border-color:var(--blue);color:var(--blue)}
    .au-vsec{margin-top:56px;padding:clamp(48px,6vw,80px) 0}
    .au-vtitle{font-size:26px;font-weight:800;color:var(--navy);margin:0 0 8px;letter-spacing:-.01em}
    .au-video-frame{position:relative;aspect-ratio:16/9;border-radius:14px;overflow:hidden;background:var(--navy-deep);box-shadow:var(--shadow)}
    .au-video-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
    .au-jump{display:flex;flex-wrap:wrap;gap:8px;margin:32px 0 0;padding-top:22px;border-top:1px solid var(--gray-line)}
    .au-jump a{display:inline-flex;align-items:center;gap:6px;padding:9px 14px;border:1px solid var(--gray-line);border-radius:999px;font-size:13px;font-weight:700;color:var(--navy);text-decoration:none;background:#fff}
    .au-jump a:hover{border-color:var(--blue);color:var(--blue)}
    /* 다크 섹션(ULTRA Powerful) */
    .au-pc{position:relative;color:#fff;background-color:var(--navy-deep);background-image:repeating-linear-gradient(135deg,rgba(255,255,255,.06) 0,rgba(255,255,255,.06) 1px,transparent 1px,transparent 14px);padding:clamp(64px,8vw,110px) 0;margin-top:56px}
    .au-pc-eyebrow{display:flex;align-items:center;gap:12px;font-size:12.5px;font-weight:800;letter-spacing:3px;color:var(--ice)}
    .au-pc-eyebrow::before{content:"";width:28px;height:2px;background:var(--ice)}
    .au-pc-h2{font-size:clamp(32px,4vw,52px);line-height:1.2;font-weight:800;letter-spacing:-.02em;color:#fff;margin:16px 0 14px;word-break:keep-all}
    .au-pc-sub{font-size:clamp(16px,1.4vw,19px);color:rgba(255,255,255,.75);margin:0 0 clamp(36px,4vw,56px);max-width:720px;line-height:1.7;word-break:keep-all}
    .au-pw-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,4vw,64px);align-items:start}
    .au-pw-right{display:grid;gap:18px}
    .au-gauge{position:relative;cursor:grab;touch-action:none;user-select:none;outline:none;border-radius:16px}
    .au-gauge:focus-visible{box-shadow:0 0 0 3px rgba(79,173,184,.6)}
    .au-gauge.is-turning{cursor:grabbing}
    .au-gauge svg{width:100%;height:auto;display:block}
    .au-gauge-read{position:absolute;left:50%;top:69%;transform:translateX(-50%);text-align:center;line-height:1;pointer-events:none;white-space:nowrap}
    .au-gauge-read b{font-size:clamp(30px,3.2vw,40px);font-weight:800;letter-spacing:-.04em;color:#fff;font-variant-numeric:tabular-nums}
    .au-gauge-read small{font-size:16px;font-weight:700;color:var(--ice);margin-left:6px}
    .au-gauge-read span{display:block;margin-top:6px;font-size:12.5px;color:rgba(255,255,255,.7)}
    .au-gauge{--over:0;--orbit:120px}
    .au-gauge-read b{transition:text-shadow .15s,color .3s;text-shadow:0 0 calc(var(--over) * 22px) var(--zone,rgba(159,227,234,.9));transform:scale(calc(1 + var(--over) * .1));display:inline-block;transform-origin:center bottom}
    .au-gauge-zone{display:inline-block;margin-top:10px;font-style:normal;font-size:calc(12px + var(--over) * 6px);font-weight:900;letter-spacing:.2em;color:#fff;background:var(--zone,#4fadb8);padding:6px 16px;border-radius:999px;opacity:var(--over);transform:translateY(calc((1 - var(--over)) * 6px)) scale(calc(.9 + var(--over) * .25));transition:opacity .2s,transform .2s,background .3s;box-shadow:0 0 calc(8px + var(--over) * 28px) var(--zone,#4fadb8)}
    .au-gauge.z3 .au-gauge-zone{animation:pwPulse .7s ease-in-out infinite alternate}
    @keyframes pwPulse{from{transform:scale(1.1)}to{transform:scale(1.22)}}
    .au-gauge-read b{color:var(--numc,#fff)}
    .au-gauge svg{filter:drop-shadow(0 0 calc(var(--over) * 26px) var(--zone,rgba(159,227,234,.5)))}
    .au-gauge-grip{transition:r .15s}
    .au-gauge-pin{stroke:var(--numc,#fff);transition:stroke .3s}
    .au-gauge:hover .au-gauge-grip{r:14;fill:rgba(79,173,184,.45)}
    .au-gauge.is-turning .au-gauge-grip{opacity:0}
    .au-gauge-hint{position:absolute;top:50%;transform:translateY(-50%);font-size:13px;font-weight:700;color:var(--ice);opacity:.9;pointer-events:none}
    .au-gauge-hint.is-l{left:-8px}.au-gauge-hint.is-r{right:-8px}
    .au-gauge-guide{position:absolute;inset:0;pointer-events:none;transition:opacity .3s}
    .au-gauge.is-touched .au-gauge-guide{opacity:0}
    .au-gauge-orbit{position:absolute;left:50%;top:65.4%;width:0;height:0;animation:pwOrbit 3.2s ease-in-out infinite alternate}
    .au-gauge-hand{position:absolute;width:30px;height:30px;left:-15px;top:-15px;transform:translateY(calc(-1 * var(--orbit,120px)));filter:drop-shadow(0 2px 6px rgba(0,0,0,.5))}
    @keyframes pwOrbit{0%{transform:rotate(-70deg)}100%{transform:rotate(70deg)}}
    .au-gauge-bubble{position:absolute;left:50%;top:-14px;transform:translateX(-50%);background:var(--ice);color:var(--navy-deep);font-size:13px;font-weight:800;padding:8px 14px;border-radius:999px;white-space:nowrap;animation:pwBob 1.6s ease-in-out infinite}
    .au-gauge-bubble::after{content:"";position:absolute;left:50%;bottom:-6px;transform:translateX(-50%);border:6px solid transparent;border-bottom:0;border-top-color:var(--ice)}
    @keyframes pwBob{0%,100%{transform:translate(-50%,0)}50%{transform:translate(-50%,-5px)}}
    .au-gauge-cap{display:block;margin-top:6px;text-align:center;font-size:13.5px;color:rgba(255,255,255,.75)}
    .au-pw-range{margin-top:26px;display:grid;gap:12px}
    .au-pw-range .row{display:grid;grid-template-columns:140px 1fr 86px;gap:12px;align-items:center;font-size:13px;color:rgba(255,255,255,.7)}
    .au-pw-range .row.is-plt{color:#fff;font-weight:700}
    .au-pw-range .track{position:relative;height:8px;border-radius:4px;background:rgba(255,255,255,.12)}
    .au-pw-range .track i{position:absolute;top:0;bottom:0;border-radius:4px;background:rgba(255,255,255,.35);transition:width .1s linear}
    .au-pw-range .row.is-plt .track i{background:linear-gradient(90deg,#228896,#9fe3ea)}
    .au-pw-range em{font-style:normal;text-align:right;font-variant-numeric:tabular-nums}
    .au-pw-stats{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
    .au-pw-stat{border:1px solid rgba(255,255,255,.2);border-radius:14px;padding:22px 20px 18px;background:rgba(255,255,255,.04)}
    .au-pw-stat b{display:block;font-size:clamp(40px,4.4vw,60px);font-weight:800;letter-spacing:-.04em;line-height:1;color:#fff}
    .au-pw-stat b small{font-size:.38em;font-weight:700;color:var(--ice);margin-left:6px;letter-spacing:0}
    .au-pw-stat > span{display:block;margin-top:10px;font-size:13.5px;color:rgba(255,255,255,.75)}
    .au-pw-stat b .au-count{font:inherit;color:inherit}
    .au-pw-demo{aspect-ratio:16/10}
    .au-pc-grid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(32px,5vw,80px);align-items:start}
    .au-pc-panel{position:relative}
    .au-pc-frame{position:relative}
    .au-pc-frame-img{display:block;width:100%;filter:drop-shadow(0 16px 30px rgba(0,0,0,.35))}
    .au-pc-num{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);font-size:clamp(18px,1.9vw,24px);font-weight:800;color:#17224d;letter-spacing:-.02em;text-shadow:0 0 5px rgba(255,255,255,.85),0 0 2px rgba(255,255,255,.85)}
    .au-pc-dial{position:absolute;left:50%;top:82%;width:15%;transform:translate(-50%,-50%) rotate(135deg);transform-origin:center;transition:transform .05s linear;touch-action:none;filter:drop-shadow(0 4px 8px rgba(0,0,0,.45))}
    /* 확대 다이얼(.au-pc-zoom/.au-pc-knob…) 규칙은 assets/css/style.css 공용 */
    .au-pc-cap{display:block;margin:18px auto 0;max-width:460px;text-align:center;font-size:14px;line-height:1.6;color:rgba(255,255,255,.8);word-break:keep-all}
    .au-pc-readout{border-top:1px solid rgba(255,255,255,.2);padding-top:22px}
    .au-pc-big{display:flex;align-items:baseline;gap:10px;line-height:1}
    .au-pc-big b{font-size:clamp(56px,7vw,96px);font-weight:800;letter-spacing:-.04em;color:#fff;font-variant-numeric:tabular-nums}
    .au-pc-big span{font-size:clamp(20px,2vw,28px);font-weight:700;color:var(--ice)}
    .au-pc-bar{margin-top:18px}
    .au-pc-line{position:relative;height:40px;display:flex;align-items:flex-end;justify-content:space-between}
    .au-pc-line::before{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:rgba(255,255,255,.18)}
    .au-pc-fill{position:absolute;left:0;bottom:0;top:0;width:100%;background:linear-gradient(90deg,rgba(255,255,255,.1),var(--ice));border-radius:2px 0 0 2px;transition:width .05s linear}
    .au-pc-line i{position:relative;z-index:1;display:block;width:1px;background:rgba(255,255,255,.55);height:14px}
    .au-pc-line i:nth-child(2),.au-pc-line i:nth-child(11),.au-pc-line i:nth-child(20),.au-pc-line i:nth-child(29){height:28px;background:#fff}
    .au-pc-ends{display:flex;justify-content:space-between;margin-top:12px;font-size:13.5px;font-weight:600;color:rgba(255,255,255,.75)}
    .au-pc-modes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:28px}
    .au-pc-modes div{border:1px solid rgba(255,255,255,.2);border-radius:12px;padding:16px 18px;background:rgba(255,255,255,.04)}
    .au-pc-modes b{display:block;font-size:17px;color:#fff;margin-bottom:4px}
    .au-pc-modes span{font-size:14px;color:rgba(255,255,255,.75);line-height:1.5}
    .au-pc-demos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:20px}
    .au-pc-demo{position:relative;aspect-ratio:16/10;border-radius:12px;overflow:hidden;background:#0f1618}
    .au-pc-demo video{display:block;width:100%;height:100%;object-fit:cover}
    #pcVideo1{transform:scale(1.55);transform-origin:center}
    .au-pc-demo-ov{position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;text-align:center;background:rgba(10,16,18,.45);pointer-events:none;transition:opacity .3s}
    .au-pc-demo-ov b{font-size:clamp(18px,1.8vw,24px);font-weight:800}
    .au-pc-demo-ov span{font-size:clamp(16px,1.5vw,20px);font-weight:700;color:var(--ice-pale)}
    .au-pc-demo.is-playing .au-pc-demo-ov{opacity:0}
    .au-pc-play{position:absolute;right:12px;bottom:10px;z-index:2;display:inline-flex;align-items:center;gap:6px;padding:7px 14px 7px 16px;border:2px solid #fff;border-radius:999px;background:rgba(15,22,23,.45);color:#fff;font-size:12px;font-weight:700;cursor:pointer;font-family:inherit}
    .au-pc-play i{font-size:10px;color:var(--ice);font-style:normal}
    .au-pc-play:hover{background:rgba(79,173,184,.3)}
    /* 강점 — 2열 카드: 큰 이미지 + 큰 제목 + 작은 본문 */
    .au-adv-cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:1fr;align-items:stretch;gap:clamp(28px,3.5vw,56px) clamp(24px,3vw,48px);margin-top:8px}
    .au-adv-card{display:grid;grid-template-rows:auto 1fr;height:100%;background:#fff;border:1px solid var(--gray-line);border-radius:16px;overflow:hidden}
    .au-adv-media{aspect-ratio:4/3;width:100%;display:flex;align-items:center;justify-content:center;background:#fff;border-bottom:1px solid var(--gray-line)}
    .au-adv-media img{width:100%;height:100%;object-fit:contain;display:block;padding:6%;box-sizing:border-box}
    .au-adv-media.is-cover img{object-fit:cover;object-position:left top;padding:0}
    .au-adv-copy{padding:22px 26px 28px}
    .au-adv-num{display:block;font-size:12px;font-weight:800;letter-spacing:.14em;color:var(--blue);margin-bottom:10px}
    .au-adv-en{font-size:clamp(22px,2.1vw,30px);line-height:1.15;font-weight:500;letter-spacing:-.005em;color:var(--blue-dark);margin:0 0 8px;text-transform:uppercase;word-break:keep-all}
    .au-adv-ko{font-size:clamp(17px,1.4vw,20px);font-weight:800;color:var(--navy);margin:0 0 12px;line-height:1.4;word-break:keep-all}
    .au-adv-p{font-size:14.5px;line-height:1.75;color:var(--text-body);margin:0;text-wrap:pretty;word-break:keep-all}
    /* 전체 모델 + 필터 */
    .au-lineup{margin-top:clamp(64px,8vw,104px);padding:clamp(56px,7vw,88px) 0 clamp(48px,6vw,72px)}
    .au-lineup .au-model .pic{background:#fff}
    .au-lineup .au-model:hover .pic{background:var(--blue-pale)}
    .au-lineup .au-filter{background:rgba(255,255,255,.6);border-color:rgba(40,55,57,.12)}
    .au-lineup .cta-band{margin-top:clamp(40px,5vw,64px)}
    .au-filter{position:relative;display:inline-flex;flex-wrap:wrap;gap:4px;padding:5px;margin:4px 0 28px;border-radius:999px;background:#eef3f3;border:1px solid var(--gray-line)}
    .au-filter button{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:2px;min-width:118px;padding:10px 18px;border:0;border-radius:999px;background:transparent;cursor:pointer;color:var(--text-muted);font-family:inherit;transition:color .2s}
    .au-filter button b{font-size:12.5px;font-weight:800;letter-spacing:.12em}
    .au-filter button small{font-size:11.5px;font-weight:600;color:currentColor;opacity:.8}
    .au-filter button:hover{color:var(--navy)}
    .au-filter button.is-on{color:var(--navy)}
    .au-filter button.is-on b{color:var(--blue)}
    .au-filter-pill{position:absolute;z-index:0;top:5px;left:5px;height:calc(100% - 10px);width:118px;border-radius:999px;background:#fff;box-shadow:0 2px 10px rgba(40,55,57,.12);transition:left .3s cubic-bezier(.4,0,.2,1),width .3s cubic-bezier(.4,0,.2,1);pointer-events:none}
    .au-models{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:26px 20px;margin-top:8px}
    .au-model.is-hidden{display:none}
    .au-model{animation:auFade .35s ease both}
    @keyframes auFade{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
    .au-model .pic{position:relative}
    .au-model.is-current .pic{box-shadow:inset 0 0 0 2px var(--ice)}
    .au-model-now{position:absolute;left:10px;top:10px;font-size:11px;font-weight:800;letter-spacing:.06em;color:#fff;background:var(--ice-dark);padding:4px 9px;border-radius:999px}
    .au-model{display:flex;flex-direction:column;text-decoration:none;color:inherit}
    .au-model .pic{aspect-ratio:1;display:flex;align-items:center;justify-content:center;background:#f7f9f9;border-radius:14px;padding:10%;box-sizing:border-box;transition:background .2s}
    .au-model:hover .pic{background:var(--blue-pale)}
    .au-model .pic img{width:100%;height:100%;object-fit:contain;display:block;transition:transform .25s}
    .au-model:hover .pic img{transform:scale(1.05)}
    .au-model h3{font-size:16.5px;font-weight:800;color:var(--navy);margin:12px 0 2px}
    .au-model p{font-size:13.5px;color:var(--text-muted);margin:0 0 6px;line-height:1.5}
    .au-model .more{font-size:13px;font-weight:700;color:var(--blue)}
    .au-model:hover .more{text-decoration:underline}
    /* Features · Specs · Accessories 탭 */
    .au-tabs{margin-top:clamp(56px,7vw,96px);scroll-margin-top:92px}
    .au-tabbar{display:flex;justify-content:center;gap:4px;border-bottom:2px solid var(--navy);padding:0 16px}
    .au-tabbar button{position:relative;min-width:170px;padding:18px 28px 20px;border:0;border-radius:6px 6px 0 0;background:var(--blue-light);color:var(--blue-dark);font-size:15.5px;font-weight:700;line-height:1;font-family:inherit;cursor:pointer;transition:background .15s}
    .au-tabbar button:hover{background:#d4e7ea}
    .au-tabbar button.is-on{background:#fff;border:2px solid var(--navy);border-bottom-color:#fff;margin-bottom:-2px;color:var(--navy)}
    .au-tabbar button.is-on::after{content:"";position:absolute;left:50%;bottom:7px;width:0;height:0;margin-left:-5px;border-left:5px solid transparent;border-right:5px solid transparent;border-top:6px solid var(--ice)}
    .au-tabpanel{display:none;padding-top:clamp(28px,3.5vw,44px)}
    .au-tabpanel.is-on{display:block}
    .au-tab-h2{font-size:26px;font-weight:800;color:var(--navy);letter-spacing:-.01em;margin:0 0 8px}
    .au-tab-h2 sub{font-size:.55em;vertical-align:-.2em}
    .au-tab-sub{color:var(--text-muted);font-size:15px;margin:0 0 22px}
    .au-feat-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(28px,4vw,64px);align-items:start}
    .au-feat-pic{display:flex;align-items:center;justify-content:center}
    .au-feat-pic img{width:100%;max-width:560px;height:auto;display:block}
    .au-hotspot{position:relative;width:100%;max-width:560px;margin:0 auto}
    .au-hotspot img{max-width:none}
    .au-hs{position:absolute;width:30px;height:30px;margin:-15px 0 0 -15px;padding:0;border:3px solid #fff;border-radius:50%;background:var(--navy);box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 0 rgba(79,173,184,.55);cursor:pointer;animation:auHs 2.6s ease-out infinite}
    .au-hs:nth-child(odd){animation-delay:1.3s}
    .au-hs:hover,.au-hs.is-on,.au-hs:focus-visible{background:var(--ice);animation:none;outline:none;box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 6px rgba(79,173,184,.3)}
    .au-hs-tip{position:absolute;left:50%;bottom:calc(100% + 12px);transform:translateX(-50%) translateY(6px);width:max-content;max-width:240px;padding:10px 12px;border-radius:10px;background:var(--navy-deep);color:#fff;font-size:13px;line-height:1.5;text-align:left;opacity:0;pointer-events:none;transition:opacity .15s,transform .15s;z-index:3;word-break:keep-all}
    .au-hs-tip b{display:block;font-size:13.5px;color:#9fe3ea;margin-bottom:2px}
    .au-hs-tip::after{content:"";position:absolute;left:50%;top:100%;margin-left:-6px;border:6px solid transparent;border-top-color:var(--navy-deep)}
    .au-hs:hover .au-hs-tip,.au-hs.is-on .au-hs-tip,.au-hs:focus-visible .au-hs-tip{opacity:1;transform:translateX(-50%) translateY(0)}
    .au-hs.is-right .au-hs-tip{left:auto;right:-10px;transform:translateX(0) translateY(6px)}
    .au-hs.is-right:hover .au-hs-tip,.au-hs.is-right.is-on .au-hs-tip{transform:translateX(0) translateY(0)}
    .au-hs.is-right .au-hs-tip::after{left:auto;right:18px;margin-left:0}
    .au-hs.is-below .au-hs-tip{bottom:auto;top:calc(100% + 12px);transform:translateX(-50%) translateY(-6px)}
    .au-hs.is-below:hover .au-hs-tip,.au-hs.is-below.is-on .au-hs-tip,.au-hs.is-below:focus-visible .au-hs-tip{transform:translateX(-50%) translateY(0)}
    .au-hs.is-below .au-hs-tip::after{top:auto;bottom:100%;border-top-color:transparent;border-bottom-color:var(--navy-deep)}
    .au-hs.is-right.is-below .au-hs-tip{transform:translateX(0) translateY(-6px)}
    .au-hs.is-right.is-below:hover .au-hs-tip,.au-hs.is-right.is-below.is-on .au-hs-tip{transform:translateX(0) translateY(0)}
    .au-feat li{transition:color .2s}
    .au-feat li.is-hl{color:var(--navy);font-weight:700}
    .au-feat li.is-hl svg circle{fill:var(--ice-pale)}
    @keyframes auHs{0%{box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 0 rgba(79,173,184,.55)}70%,100%{box-shadow:0 2px 10px rgba(0,0,0,.35),0 0 0 14px rgba(79,173,184,0)}}
    .au-feat{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px 28px;padding:0;margin:0;list-style:none}
    .au-feat li{display:grid;grid-template-columns:22px 1fr;gap:10px;align-items:start;font-size:15.5px;color:var(--text-body);line-height:1.6;word-break:keep-all}
    .au-feat li svg{width:22px;height:22px;margin-top:2px}
    .au-speclist{list-style:none;margin:0;padding:0;display:grid;gap:0}
    .au-speclist li{display:grid;grid-template-columns:190px 1fr;gap:16px;padding:12px 0;border-bottom:1px solid var(--gray-line);font-size:15px;line-height:1.55}
    .au-speclist li:first-child{border-top:1px solid var(--gray-line)}
    .au-speclist b{color:var(--navy);font-weight:800}
    .au-speclist span{color:var(--text-body)}
    .au-note{font-size:13px;color:var(--text-muted);margin:16px 0 0;line-height:1.6}
    .au-note a{color:var(--blue)}
    .au-tab-sub{font-size:15px;color:var(--text-body);line-height:1.7;margin:-10px 0 28px;max-width:860px;word-break:keep-all}
    .au-acc-h3{font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin:0 0 14px;padding-top:8px}
    .au-acc-h3 small{font-size:13px;font-weight:600;letter-spacing:0;color:var(--text-muted);margin-left:8px}
    .au-accgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px;margin-bottom:36px}
    .au-accgrid.is-3{grid-template-columns:repeat(3,minmax(0,1fr))}
    .au-accgrid article{background:transparent}
    .au-accgrid .pic{aspect-ratio:1;display:flex;align-items:center;justify-content:center}
    .au-accgrid .pic img{width:100%;height:100%;object-fit:contain;display:block;transition:transform .25s}
    .au-accgrid article:hover .pic img{transform:scale(1.04)}
    .au-accgrid h3{font-size:16.5px;color:var(--navy);font-weight:800;margin:0;padding:12px 0 2px}
    .au-accgrid p{margin:0;padding:0 0 6px;font-size:13.5px;color:var(--text-muted);line-height:1.5}
    @media (max-width:1100px){
      .au-top{grid-template-columns:84px minmax(0,1fr);}
      .au-thumbs button{width:84px;height:84px}
      .au-copy{grid-column:1 / -1}
      .au-stage{min-height:380px}
    }
    @media (max-width:960px){
      .au-pc-grid,.au-pw-grid,.au-feat-grid{grid-template-columns:1fr}
      .au-pw-range .row{grid-template-columns:110px 1fr 80px}
      .au-feat-pic{order:-1}.au-feat-pic img{max-width:420px}.au-hotspot{max-width:420px}.au-hotspot img{max-width:none}
      .au-accgrid,.au-accgrid.is-3,.au-models{grid-template-columns:repeat(2,minmax(0,1fr))}
      .au-filter{border-radius:18px}.au-filter button{min-width:0;flex:1 1 30%;padding:9px 10px}.au-filter-pill{border-radius:14px}
      .au-pc-panel{max-width:520px}
      .au-adv-cards{gap:32px 20px}
    }
    @media (max-width:640px){
      .au-top{grid-template-columns:1fr}
      .au-thumbs{grid-auto-flow:column;grid-auto-columns:72px;overflow-x:auto;order:2}
      .au-thumbs button{width:72px;height:72px}
      .au-stage{order:1;min-height:0}
      .au-copy{order:3}
      .au-adv-cards,.au-feat,.au-accgrid,.au-accgrid.is-3{grid-template-columns:1fr}
      .au-tabbar{gap:2px;padding:0 8px}.au-tabbar button{min-width:0;flex:1;padding:14px 8px 16px;font-size:14px}
      .au-speclist li{grid-template-columns:1fr;gap:2px}
      .au-pc-modes,.au-pc-demos{grid-template-columns:1fr}
      .au-pc-knob-hint{display:none}
    }
  </style>

  <section>
    <div class="au-wrap">
      <div class="au-titleblock">
        <h1 class="au-title">The Aero<sub>2</sub> PLT&reg; ULTRA</h1>
        <p class="tagline"><b>ULTRA</b> Powerful Dry Ice Blaster.</p>
      </div>
      <div class="au-top">
        <div class="au-thumbs" id="auThumbs" role="tablist" aria-label="제품 이미지">
          <button type="button" class="is-on" data-src="../../assets/img/aero2-plt-ultra-front.webp" data-cap="Aero2 PLT ULTRA" aria-label="제품 전면"><img src="../../assets/img/aero2-plt-ultra-front.webp" alt="" /></button>
          <button type="button" data-src="../../assets/img/aero2-plt-ultra-side.webp" data-cap="측면 · 호스 연결부" aria-label="제품 측면"><img src="../../assets/img/aero2-plt-ultra-side.webp" alt="" /></button>
          <button type="button" data-src="../../assets/img/aero2-plt-ultra-kit.webp" data-cap="Performance Kit 구성" aria-label="Performance Kit"><img src="../../assets/img/aero2-plt-ultra-kit.webp" alt="" /></button>
        </div>
        <div class="au-stage">
          <img id="auStageImg" src="../../assets/img/aero2-plt-ultra-front.webp" alt="Aero2 PLT ULTRA 드라이아이스 블라스터" />
          <span class="cap" id="auStageCap">Aero2 PLT ULTRA</span>
        </div>
        <div class="au-copy">
          <p>Aero2 PLT ULTRA는 3mm 펠렛을 그대로 분사하는 풀펠렛 드라이아이스 블라스터로, 더 높은 분사 압력을 제공합니다. 최대 250 psi(17.2 bar), 분당 최대 2.7kg(6 lb)의 공급량으로 가장 고착된 오염물도 충분히 제거하며, Cold Jet 전용 노즐을 조합해 시장 최고 수준의 성능으로 분사 조건을 최적화할 수 있습니다.</p>
          <p>PLT ULTRA는 Aero 시리즈의 기술 발전을 이어받아 가장 효율적인 드라이아이스 블라스터로 완성되었습니다. 직선형(straight-through) 에어 시스템과 새로 설계된 SureFlow&trade; 피딩 시스템이 기계 내부의 압력 손실과 드라이아이스 승화를 최소화해, 공급 공기를 최대로 활용하고 드라이아이스 낭비를 줄입니다.</p>
          <p>7인치 LCD 화면과 디지털 컨트롤로 분사 파라미터와 기계 설정을 한눈에 확인하고 손쉽게 조정합니다. 분사 압력과 공급량 조합은 애플리케이션 레시피로 저장해 반복 사용할 수 있습니다.</p>
          <p>PLT ULTRA는 Cold Jet의 Industry 4.0 솔루션 <a href="../../support/techsupport.html">Cold Jet CONNECT&reg;</a>로 연결되는 IoT 장비입니다. 원격 모니터링 · 진단, 교육 영상, 장비 문서, 셀프 트러블슈팅을 제공하며, 추가 지원이 필요하면 채팅 · 서비스 티켓 · 음성/영상 통화로 서비스 기술자와 바로 연결됩니다.</p>
          <div class="au-dl">
            <h4>DOWNLOADS</h4>
            <ul>
              <li><a href="https://www.coldjet.com/wp-content/uploads/0911_SPEC-SHEET_AERO2_ULTRA_2026-06-05_pi_jt.pdf" target="_blank" rel="noopener"><span class="ic">PDF</span>Aero2 ULTRA Spec Sheet <small>· 영문</small></a></li>
              <li><a href="https://www.coldjet.com/wp-content/uploads/0919_CATALOG_AERO2-ULTRA_2026-06-12_jt.pdf" target="_blank" rel="noopener"><span class="ic">PDF</span>Aero2 ULTRA Product Book <small>· 영문</small></a></li>
            </ul>
          </div>
          <div class="au-cta">
            <a class="pri" href="../../products/quote.html">견적 요청</a>
            <a class="sec" href="../../rental/demo-apply.html">데모 테스트 신청</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="au-vsec tint-hatch" id="video">
    <div class="au-wrap">
      <span class="au-eyebrow">VIDEO</span>
      <h2 class="au-vtitle">Aero2 PLT&reg; ULTRA Video</h2>
      <p class="au-tab-sub">Aero2 ULTRA 시리즈의 설계와 세척 과정을 영상으로 확인하세요.</p>
      <div class="au-video-frame"><iframe src="https://www.youtube-nocookie.com/embed/XNvx3QblfFk" title="Aero2 PLT ULTRA Video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>
    </div>
  </section>

  <section class="au-pc" id="power">
    <div class="au-wrap">
      <span class="au-pc-eyebrow">FULL PELLET · HIGH PRESSURE</span>
      <h2 class="au-pc-h2">더 높은 압력으로,<br />가장 고착된 오염까지.</h2>
      <p class="au-pc-sub">3mm 펠렛을 그대로 분사하는 풀펠렛 블라스터. 1인치 직선형 에어 경로와 새 SureFlow&trade; 피더가 압력 손실과 승화를 최소화해, 공급 공기를 최대로 활용합니다.</p>
      <div class="au-pw-grid">
        <div class="au-pw-left">
          <div class="au-gauge" id="pwGauge" role="slider" tabindex="0" aria-label="분사 압력" aria-valuemin="2.4" aria-valuemax="17.2" aria-valuenow="17.2" aria-valuetext="17.2 bar">
            <svg viewBox="0 0 320 260" aria-hidden="true">
              <defs><filter id="pwGlow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5" result="b"></feGaussianBlur><feMerge><feMergeNode in="b"></feMergeNode><feMergeNode in="SourceGraphic"></feMergeNode></feMerge></filter><linearGradient id="pwHotGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#9fe3ea"></stop><stop offset="45%" stop-color="#ffb347"></stop><stop offset="100%" stop-color="#ff3b30"></stop></linearGradient><linearGradient id="pwArc" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#4fadb8"></stop><stop offset="100%" stop-color="#c9f1f5"></stop></linearGradient></defs>
              <path d="M 56.1 230 A 120 120 0 1 1 263.9 230" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="14" stroke-linecap="round"></path>
              <path id="pwFill" d="M 56.1 230 A 120 120 0 1 1 263.9 230" fill="none" stroke="url(#pwArc)" stroke-width="14" stroke-linecap="butt" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="0"></path>
              <path id="pwHot" d="M 166.8 50.2 A 120 120 0 0 1 263.9 230" fill="none" stroke="url(#pwHotGrad)" stroke-width="18" stroke-linecap="butt" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="1" filter="url(#pwGlow)" style="opacity:0"></path>
              <g id="pwTicks" stroke="rgba(255,255,255,.5)" stroke-width="1.5"></g>
              <g id="pwPcs"><line x1="0" y1="0" x2="0" y2="0" stroke="#fff" stroke-width="2" stroke-dasharray="3 3"></line><text font-size="10" font-weight="800" fill="rgba(255,255,255,.75)" text-anchor="middle">PCS ULTRA 10 bar</text></g>
              <g id="pwNeedle" transform="rotate(120 160 170)"><line class="au-gauge-pin" x1="160" y1="170" x2="160" y2="78" stroke="#fff" stroke-width="3" stroke-linecap="round"></line><circle cx="160" cy="170" r="9" fill="#1b2426" stroke="#fff" stroke-width="3"></circle><circle class="au-gauge-grip" cx="160" cy="82" r="11" fill="rgba(79,173,184,.25)" stroke="#9fe3ea" stroke-width="2"></circle></g>
              <text x="52" y="254" font-size="12" font-weight="800" fill="rgba(255,255,255,.7)" text-anchor="middle">2.4 bar</text>
              <text x="268" y="254" font-size="12" font-weight="800" fill="rgba(255,255,255,.7)" text-anchor="middle">17.2 bar</text>
            </svg>
            <span class="au-gauge-hint is-l">↺ 낮게</span><span class="au-gauge-hint is-r">높게 ↻</span>
            <div class="au-gauge-guide" aria-hidden="true">
              <div class="au-gauge-orbit"><svg class="au-gauge-hand" viewBox="0 0 24 24"><path d="M9 11.5V5.2a1.7 1.7 0 0 1 3.4 0V11m0-3.4a1.7 1.7 0 0 1 3.4 0v3.9m0-2.5a1.7 1.7 0 0 1 3.4 0v6.3c0 3.3-2.5 5.9-5.9 5.9h-1.6c-1.9 0-3.6-.9-4.7-2.4l-3.1-4.3a1.6 1.6 0 0 1 2.5-2l1.9 2.2" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
              <span class="au-gauge-bubble">바늘을 잡고 돌려보세요</span>
            </div>
            <div class="au-gauge-read"><b id="pwPsi">17.2</b><small>bar</small><span id="pwBar">250 psi</span><em class="au-gauge-zone" id="pwZone">ULTRA ZONE</em></div>
            <span class="au-gauge-cap">바늘을 돌리거나 페이지를 스크롤하면 압력이 올라갑니다</span>
          </div>
          <div class="au-pw-range">
            <div class="row"><span>Aero2 PCS ULTRA</span><div class="track"><i style="left:0;width:58%"></i></div><em>1.4–10 bar</em></div>
            <div class="row is-plt"><span>Aero2 PLT ULTRA</span><div class="track"><i id="pwRangeFill" style="left:8%;width:92%"></i></div><em>2.4–17.2 bar</em></div>
          </div>
        </div>
        <div class="au-pw-right">
          <div class="au-pw-stats">
            <div class="au-pw-stat"><b><span class="au-count" data-to="17.2" data-dec="1">17.2</span><small>bar</small></b><span>최대 분사 압력 · 250 psi</span></div>
            <div class="au-pw-stat"><b><span class="au-count" data-to="2.7" data-dec="1">2.7</span><small>kg/min</small></b><span>최대 공급량 · 6 lb/min</span></div>
            <div class="au-pw-stat"><b><span class="au-count" data-to="25.4" data-dec="1">25.4</span><small>mm</small></b><span>직선형 에어 경로 · 1 in</span></div>
            <div class="au-pw-stat"><b><span class="au-count" data-to="4.7" data-dec="1">4.7</span><small>m³/min</small></b><span>고유량 노즐 대응 · 165 cfm</span></div>
          </div>
          <div class="au-pc-demo au-pw-demo">
            <video id="pcVideo2" muted loop playsinline preload="none"><source src="../../assets/video/pcs-demo-asphalt.mp4" type="video/mp4" /></video>
            <div class="au-pc-demo-ov"><b>Full Pellet</b><span>3.0mm · 고착 오염 제거</span></div>
            <button type="button" class="au-pc-play" data-v="pcVideo2" aria-label="영상 재생"><span>영상 재생</span><i>▶</i></button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="au-sec" id="advantage">
    <div class="au-wrap">
      <span class="au-eyebrow">THE COLD JET DIFFERENCE</span>
      <h2>ULTRA TO THE CORE — PLT ULTRA의 강점</h2>
      <p class="sub">모터부터 피더, 제어 펌웨어, 어플리케이터까지 코어를 새로 설계했습니다.</p>
      <div class="au-adv-cards">
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-motors.webp" alt="신형 모터 · 기어박스 · 케이블" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">01</span>
            <h3 class="au-adv-en">NEW, STATE-OF-THE-ART MOTORS, GEARBOXES, AND CABLING</h3>
            <p class="au-adv-ko">신형 모터 · 기어박스 · 케이블</p>
            <p class="au-adv-p">ULTRA 시리즈는 내부 부품을 완전히 새로 설계해 신뢰성과 효율을 끌어올렸습니다. 새 모터 어레이는 초저온 환경용 모터로 구성되어 장시간 분사 후에도 멈추지 않고 작동합니다. 여기에 Cold Jet 전용 제어 펌웨어와 모터 드라이버를 적용해 사용 경험을 개선하고 잠재적 오류를 최소화했습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-sureflow.webp" alt="SureFlow 피더 시스템" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">02</span>
            <h3 class="au-adv-en">SUREFLOW FEEDER SYSTEM</h3>
            <p class="au-adv-ko">SureFlow 피더 시스템</p>
            <p class="au-adv-p">특허받은 SureFlow 피더 시스템은 썸퍼 · 램로드 · 진동기와 단열 호퍼를 결합합니다. 호퍼를 최적으로 교반해 드라이아이스가 끊김 없이 시스템을 통과하도록 하여, 일정한 분사 흐름을 만듭니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-defrost.webp" alt="특허 출원 중인 디프로스트(제상) 사이클" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">03</span>
            <h3 class="au-adv-en">PATENT-PENDING DEFROST CYCLE</h3>
            <p class="au-adv-ko">특허 출원 중인 디프로스트(제상) 사이클</p>
            <p class="au-adv-p">PLT ULTRA에는 업계 최초, 특허 출원 중인 제상 사이클이 탑재되어 있습니다. 내부 부품이 얼거나 막혔을 때 자동 또는 수동으로 실행해 가동 중단 시간을 줄입니다. 어플리케이터나 HMI 화면에서 직관적으로 실행할 수 있으며, 최대 2분간 외부 공기를 기계 코어로 불어넣어 해동한 뒤 최소한의 중단으로 작업에 복귀시킵니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media is-cover"><img src="../../assets/img/adv-applicator.webp" alt="초내구성 어플리케이터" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">04</span>
            <h3 class="au-adv-en">ULTRA-DURABLE APPLICATORS</h3>
            <p class="au-adv-ko">초내구성 어플리케이터</p>
            <p class="au-adv-p">Precision · Performance 어플리케이터를 매우 견고하고 정비하기 쉽게 다시 설계했습니다. IP67 등급 부품과 방수 밀폐 커넥터를 적용해 수분 배출 성능을 높였습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-hmi-plt.webp" alt="Aero2 PLT ULTRA 7인치 LCD 컨트롤" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">05</span>
            <h3 class="au-adv-en">ULTRA-SMART HMI</h3>
            <p class="au-adv-ko">최대 9개 레시피를 저장하는 스마트 HMI</p>
            <p class="au-adv-p">작업자는 기계에 최대 9개의 레시피(분사 압력 · 공급량)를 저장해 특정 작업 · 소재 · 오염물에 맞춘 세척 조건을 바로 불러올 수 있습니다. HMI에는 비밀번호 잠금 기능이 있어, 관리자가 작업자의 설정 변경을 제한함으로써 드라이아이스 과다 사용이나 민감한 표면 손상을 예방할 수 있습니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-automation.webp" alt="자동화 · 로봇 통합 대응" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">06</span>
            <h3 class="au-adv-en">AUTOMATION & INTEGRATION CAPABLE</h3>
            <p class="au-adv-ko">자동화 · 로봇 통합 대응</p>
            <p class="au-adv-p">Aero2 ULTRA 시리즈는 자동화 설비나 생산 라인에 통합하는 데 필요한 요소를 갖추고 있습니다. 통합 키트(Integration Kit)를 별도로 구매해 적용합니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-service.webp" alt="QR 코드로 바로 해결하는 서비스 편의성" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">07</span>
            <h3 class="au-adv-en">ULTRA-INTUITIVE SERVICEABILITY</h3>
            <p class="au-adv-ko">QR 코드로 바로 해결하는 서비스 편의성</p>
            <p class="au-adv-p">ULTRA 시리즈의 모든 개선은 최고의 신뢰성과 간결한 사용 경험을 목표로 했습니다. 오류로 기계가 멈추면 작업자가 HMI 화면의 QR 코드를 스캔해 해당 오류의 해결 방법에 바로 접근합니다. 직접 해결하기 어려우면 서비스 티켓을 즉시 제출할 수 있으며, 장비 시리얼 번호 · 펌웨어 버전 · 오류 코드 · 가동 시간 같은 정보가 서비스 부서에 함께 전달됩니다.</p>
          </div>
        </article>
        <article class="au-adv-card">
          <div class="au-adv-media"><img src="../../assets/img/adv-connectivity.webp" alt="확장된 연결 옵션" loading="lazy" /></div>
          <div class="au-adv-copy">
            <span class="au-adv-num">08</span>
            <h3 class="au-adv-en">EXPANDED CONNECTIVITY OPTIONS</h3>
            <p class="au-adv-ko">확장된 연결 옵션</p>
            <p class="au-adv-p">무선 인터넷 사용이 제한된 현장을 위해 ULTRA 시리즈는 장비 데이터를 추출하는 방법을 넓혔습니다. 접근하기 쉬운 새 외부 패널에 microSD 카드 리더와 이더넷 포트를 두어, 분사 공정의 데이터를 확보하고 제어 · 분석할 수 있습니다.</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="au-tabs" id="details">
    <div class="au-tabbar" role="tablist" aria-label="제품 상세">
      <button type="button" role="tab" class="is-on" aria-selected="true" aria-controls="tabFeatures" id="tabBtnFeatures">Features</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="tabSpecs" id="tabBtnSpecs">Specifications</button>
    </div>
    <div class="au-wrap">
      <div class="au-tabpanel is-on" id="tabFeatures" role="tabpanel" aria-labelledby="tabBtnFeatures">
        <div class="au-feat-grid">
          <div>
            <span class="au-eyebrow">FEATURES</span>
            <h2 class="au-tab-h2">Aero<sub>2</sub> PLT ULTRA Features</h2>
            <p class="au-tab-sub">사진의 점 위에 마우스를 올리면 해당 기능의 위치와 설명을 확인할 수 있습니다.</p>
            <ul class="au-feat">
              <li data-feat="0"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>7인치 LCD 디스플레이 + 디지털 컨트롤</span></li>
              <li data-feat="1"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>직선형(straight-through) 에어 시스템 — 1인치 경로</span></li>
              <li data-feat="2"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>애플리케이션 레시피 저장(분사 압력 · 공급량)</span></li>
              <li data-feat="3"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>공기역학적 저부하 에어락 피더(Advanced Aerodynamic Low Load Airlock Feeder)</span></li>
              <li data-feat="4"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>특허받은 고효율 흐름 개시 레귤레이터(Flow Initiation Regulator)</span></li>
              <li data-feat="5"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>특허받은 다이렉트 드라이브 피딩 시스템</span></li>
              <li data-feat="6"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>디프로스트(제상) 사이클 — 특허 출원</span></li>
              <li data-feat="7"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>신형 모터 · 기어박스 · 케이블</span></li>
              <li data-feat="8"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>코팅 공구강급 알루미늄 합금 + 스테인리스 + 폴리머 프레임</span></li>
              <li data-feat="9"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>이동성과 조작성을 고려한 설계</span></li>
              <li data-feat="10"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>IoT — Cold Jet CONNECT&reg;</span></li>
              <li data-feat="11"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="none" stroke="#4fadb8" stroke-width="1.8"/><path d="m7.5 12.5 3 3 6-6.5" fill="none" stroke="#4fadb8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>로봇 통합 · 자동화 대응</span></li>
            </ul>
          </div>
          <div class="au-feat-pic au-hotspot" id="auHotspot">
            <img src="../../assets/img/aero2-plt-ultra-front.webp" alt="Aero2 PLT ULTRA" loading="lazy" />
            <button type="button" class="au-hs is-below" style="left:63.5%;top:12.5%" data-feat="0" aria-label="7인치 LCD · 디지털 컨트롤"><span class="au-hs-tip"><b>7인치 LCD · 디지털 컨트롤</b>분사 압력 · 공급량을 한 화면에서 확인하고 레시피를 저장합니다.</span></button>
            <button type="button" class="au-hs is-right is-below" style="left:83.5%;top:27%" data-feat="9" aria-label="인체공학 핸들"><span class="au-hs-tip"><b>인체공학 핸들</b>무게와 크기를 줄인 설계로 이동과 조작이 쉽습니다.</span></button>
            <button type="button" class="au-hs" style="left:34%;top:41%" data-feat="5" aria-label="단열 호퍼 · SureFlow 피더"><span class="au-hs-tip"><b>단열 호퍼 · SureFlow 피더</b>썸퍼 · 램로드 · 진동기가 3mm 펠렛을 끊김 없이 공급합니다.</span></button>
            <button type="button" class="au-hs" style="left:67%;top:43%" data-feat="1" aria-label="1인치 직선형 에어 시스템"><span class="au-hs-tip"><b>1인치 직선형 에어 시스템</b>압력 손실과 승화를 최소화해 250 psi까지 분사합니다.</span></button>
            <button type="button" class="au-hs" style="left:23%;top:54%" data-feat="8" aria-label="코팅 알루미늄 · 스테인리스 프레임"><span class="au-hs-tip"><b>코팅 알루미늄 · 스테인리스 프레임</b>가혹한 환경을 견디는 공구강급 합금 + 폴리머 프레임.</span></button>
            <button type="button" class="au-hs" style="left:47%;top:55%" data-feat="4" aria-label="펄스 없는 고압 분사"><span class="au-hs-tip"><b>펄스 없는 고압 분사</b>고효율 흐름 개시 레귤레이터로 일정한 분사 흐름을 만듭니다.</span></button>
            <button type="button" class="au-hs" style="left:67%;top:69%" data-feat="10" aria-label="연결 패널 · 포트"><span class="au-hs-tip"><b>연결 패널 · 포트</b>이더넷 · microSD 포트로 Cold Jet CONNECT®와 연결합니다.</span></button>
            <button type="button" class="au-hs" style="left:43%;top:84%" data-feat="9" aria-label="대형 바퀴 · 기동성"><span class="au-hs-tip"><b>대형 바퀴 · 기동성</b>현장 이동을 고려한 바퀴와 범퍼 설계.</span></button>
          </div>
        </div>
      </div>
      <div class="au-tabpanel" id="tabSpecs" role="tabpanel" aria-labelledby="tabBtnSpecs" hidden>
        <div class="au-feat-grid">
          <div>
            <span class="au-eyebrow">SPECIFICATIONS</span>
            <h2 class="au-tab-h2">Aero<sub>2</sub> PLT ULTRA Specifications</h2>
            <p class="au-tab-sub">Cold Jet 공식 스펙시트(2026-06) 기준입니다.</p>
            <ul class="au-speclist">
              <li><b>크기 (L×W×H)</b><span>98 × 48 × 114 cm (38.5 × 19 × 45 in)</span></li>
              <li><b>무게</b><span>110.2 kg (243 lb)</span></li>
              <li><b>호퍼 용량</b><span>27 kg (60 lb)</span></li>
              <li><b>디스플레이</b><span>7인치 LCD</span></li>
              <li><b>전원</b><span>110/230 VAC (50/60 Hz) · 4.5 A</span></li>
              <li><b>가변 공급량</b><span>0–2.7 kg/min (0–6 lb/min)</span></li>
              <li><b>드라이아이스 입자</b><span>투입 3mm → 분사 3mm (풀펠렛)</span></li>
              <li><b>분사 압력</b><span>2.4–17.2 bar (35–250 psi)</span></li>
              <li><b>공급 압력</b><span>2.8–17.2 bar (40–250 psi)</span></li>
              <li><b>노즐 공기 소비량</b><span>1.4–4.7 m³/min @ 5.5 bar (50–165 cfm @ 80 psi)</span></li>
              <li><b>에어 경로</b><span>1 in (25.4 mm) 직선형 튜빙</span></li>
              <li><b>SureFlow</b><span>썸퍼 · 램로드 · 전동 진동기 · 상시 호퍼 교반 · 단열 호퍼</span></li>
            </ul>
            <p class="au-note">압축공기 조건은 사용 노즐에 따라 달라지며, 컴프레서 용량 검토는 <a href="../compare-equip.html">장비 비교·추천받기</a>에서 도와드립니다.</p>
          </div>
          <div class="au-feat-pic"><img src="../../assets/img/aero2-plt-ultra-side.webp" alt="Aero2 PLT ULTRA 측면" loading="lazy" /></div>
        </div>
      </div>
    </div>
  </section>

  <section class="au-sec" id="accessories" style="padding-bottom:12px">
    <div class="au-wrap">
      <span class="au-eyebrow">ACCESSORIES</span>
      <h2 class="au-tab-h2">Aero<sub>2</sub> PLT ULTRA Accessories</h2>
      <p class="au-tab-sub">Performance Kit(3/4&quot; · 1&quot; 어플리케이터 + Performance 노즐)로 기본 구성하고, 표준 · 고유량 · 프래그먼팅 노즐로 현장에 맞게 확장합니다.</p>
      <h3 class="au-acc-h3">Nozzles <small>노즐</small></h3>
      <div class="au-accgrid is-3">
        <article><div class="pic"><img src="../../assets/img/acc-nozzles-all.webp" alt="All Nozzles" loading="lazy" /></div><h3>All Nozzles</h3><p>PLT ULTRA 호환 전체 노즐 · 프래그먼팅 노즐 포함</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-nozzles-standard.webp" alt="Standard Flow Nozzles" loading="lazy" /></div><h3>Standard Flow Nozzles</h3><p>100 cfm · 범용 표준</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-nozzles-high.webp" alt="High Flow Nozzles" loading="lazy" /></div><h3>High Flow Nozzles</h3><p>140–165 cfm · 최대 세척력</p></article>
      </div>
      <h3 class="au-acc-h3">Applicators <small>어플리케이터</small></h3>
      <div class="au-accgrid is-3">
        <article><div class="pic"><img src="../../assets/img/acc-applicators-all.webp" alt="All Applicators" loading="lazy" /></div><h3>All Applicators</h3><p>PLT ULTRA 호환 전체 어플리케이터</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-applicator-34.webp" alt="3/4 Applicators" loading="lazy" /></div><h3>3/4&quot; Applicators</h3><p>Performance Kit · 4-Function</p></article>
        <article><div class="pic"><img src="../../assets/img/acc-applicator-1.webp" alt="1 Applicators" loading="lazy" /></div><h3>1&quot; Applicators</h3><p>Performance Kit · 최대 유량</p></article>
      </div>
      <p class="au-note">전체 노즐 · 어플리케이터 라인업은 <a href="../nozzle.html">노즐 · 액세서리</a> 페이지에서 확인하실 수 있습니다.</p>
    </div>
  </section>

  <section class="au-sec au-lineup tint-hatch">
    <div class="au-wrap">
      <span class="au-eyebrow">ALL MODELS</span>
      <h2>Cold Jet 블라스터 전체 라인업</h2>
      <p class="sub">세척 대상과 현장 조건에 따라 다른 블라스터도 검토해 보세요. 용도별로 걸러 볼 수 있습니다.</p>
      <div class="au-filter" id="auFilter" role="tablist" aria-label="모델 필터">
        <span class="au-filter-pill" aria-hidden="true"></span>
        <button type="button" data-filter="all" class="is-on" aria-selected="true" role="tab"><b>ALL</b><small>전체 모델</small></button>
        <button type="button" data-filter="core" aria-selected="false" role="tab"><b>CORE</b><small>핵심 모델</small></button>
        <button type="button" data-filter="smart" aria-selected="false" role="tab"><b>SMART</b><small>정밀 제어 · 자동화</small></button>
        <button type="button" data-filter="pellet" aria-selected="false" role="tab"><b>PELLET</b><small>산업 설비 · 고착 오염</small></button>
        <button type="button" data-filter="micro" aria-selected="false" role="tab"><b>MICRO PARTICLE</b><small>정밀 · 민감 표면</small></button>
        <button type="button" data-filter="specialty" aria-selected="false" role="tab"><b>SPECIALTY</b><small>특수 작업</small></button>
      </div>
      <div class="au-models" id="auModels">
        <a class="au-model" href="aero2-ultra.html" data-cat="core smart pellet micro"><div class="pic"><img src="../../assets/img/blaster-aero2-pcs-ultra-white.webp" alt="Aero2 PCS ULTRA" loading="lazy" /></div><h3>Aero2&reg; PCS ULTRA</h3><p>입자 크기까지 제어하는 스마트 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model is-current" href="aero2-plt-ultra.html" data-cat="smart pellet" aria-current="page"><div class="pic"><img src="../../assets/img/blaster-aero2-plt-ultra-white.webp" alt="Aero2 PLT ULTRA" loading="lazy" /><span class="au-model-now">현재 페이지</span></div><h3>Aero2&reg; PLT ULTRA</h3><p>최대 250 psi 풀펠렛 스마트 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="i3-microclean-2.html" data-cat="core micro smart"><div class="pic"><img src="../../assets/img/blaster-i3-microclean-2-white.webp" alt="i MicroClean 2" loading="lazy" /></div><h3>i&sup3; MicroClean&reg; 2</h3><p>2세대 정밀 스마트 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="aero-series.html" data-cat="pellet"><div class="pic"><img src="../../assets/img/blaster-aero-40fp-white.webp" alt="Aero 40FP" loading="lazy" /></div><h3>Aero&reg; 40FP</h3><p>풀프레셔 전문가용 · 호퍼 40 lb</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="aero-series.html" data-cat="pellet"><div class="pic"><img src="../../assets/img/blaster-aero-80fp-white.webp" alt="Aero 80FP" loading="lazy" /></div><h3>Aero&reg; 80FP</h3><p>풀프레셔 전문가용 · 호퍼 80 lb</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="elite20-icerocket.html" data-cat="core pellet micro"><div class="pic"><img src="../../assets/img/blaster-elite-20-white.webp" alt="Elite 20" loading="lazy" /></div><h3>Elite 20</h3><p>실용형 펠렛 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="elite20-icerocket.html" data-cat="core pellet"><div class="pic"><img src="../../assets/img/blaster-icerocket-plt-white.webp" alt="IceRocket PLT" loading="lazy" /></div><h3>IceRocket PLT</h3><p>입문형 펠렛 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="i3-microclean.html" data-cat="micro"><div class="pic"><img src="../../assets/img/blaster-i3-microclean-white.webp" alt="i MicroClean" loading="lazy" /></div><h3>i&sup3; MicroClean&reg;</h3><p>탁상형 정밀 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="sdi-select-60.html" data-cat="micro pellet"><div class="pic"><img src="../../assets/img/blaster-sdi-select-60-white.webp" alt="SDI Select 60" loading="lazy" /></div><h3>SDI Select&trade; 60</h3><p>마이크로파티클 · 펠렛 겸용 범용 모델</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="c100.html" data-cat="specialty"><div class="pic"><img src="../../assets/img/blaster-c100-white.webp" alt="C100" loading="lazy" /></div><h3>C100</h3><p>완전 공압식 블라스터</p><span class="more">모델 상세 보기 →</span></a>
        <a class="au-model" href="e-co2-150.html" data-cat="specialty"><div class="pic"><img src="../../assets/img/blaster-e-co2-150-white.webp" alt="E-CO2 150" loading="lazy" /></div><h3>E-CO2&trade; 150</h3><p>연마재 + 드라이아이스 복합 분사</p><span class="more">모델 상세 보기 →</span></a>
      </div>

      <div class="cta-band" style="margin-top:24px;">
        <div>
          <h3>Aero2 PLT&reg; ULTRA 도입을 검토 중이신가요?</h3>
          <p>고압 · 고유량 운용에 필요한 컴프레서 사양과 노즐 구성까지 함께 안내해 드립니다.</p>
        </div>
        <a class="cta-btn" href="../../products/quote.html">견적문의 하기</a>
      </div>
    </div>
  </section>
"""
AERO2_PLT_ULTRA_SCRIPT = """  <script>
    (function(){
      var rail=document.getElementById('auThumbs'),img=document.getElementById('auStageImg'),cap=document.getElementById('auStageCap');
      if(!rail||!img)return;
      rail.addEventListener('click',function(e){
        var b=e.target.closest('button[data-src]');if(!b)return;
        rail.querySelectorAll('button').forEach(function(x){x.classList.remove('is-on')});b.classList.add('is-on');
        img.style.opacity=0;setTimeout(function(){img.src=b.dataset.src;img.alt=b.dataset.cap;cap.textContent=b.dataset.cap;img.style.opacity=1},150);
      });
    })();
  </script>
  <script>
    (function(){
      var scaleEl=document.getElementById('pcScale'),fill=document.getElementById('pcFill'),live=document.getElementById('pcLive');
      var dial=document.getElementById('pcDial'),num=document.getElementById('pcNum'),knob=document.getElementById('pcKnob'),face=document.getElementById('pcKnobFace'),arc=document.getElementById('pcArc'),ticks=document.getElementById('pcTicks');
      var hasDial=!!(scaleEl&&fill&&live);
      var MIN=0.3,MAX=3.0,STEP=0.1,SWEEP=270,ticking=false,touched=false,value=MAX;
      var snap=function(v){return Math.round((v-MIN)/STEP)*STEP+MIN};
      // 눈금 28개 (-135° ~ +135°)
      if(ticks){var h='';for(var i=0;i<28;i++){var a=(-135+i*(SWEEP/27))*Math.PI/180,big=(i%9===0),r1=big?108:113,r2=118;h+='<line x1="'+(150+r1*Math.sin(a)).toFixed(1)+'" y1="'+(150-r1*Math.cos(a)).toFixed(1)+'" x2="'+(150+r2*Math.sin(a)).toFixed(1)+'" y2="'+(150-r2*Math.cos(a)).toFixed(1)+'"'+(big?' stroke="#fff" stroke-width="2"':'')+'></line>'}ticks.innerHTML=h}
      function setValue(v){
        v=snap(Math.min(Math.max(v,MIN),MAX));value=v;
        var f=(v-MIN)/(MAX-MIN),deg=-135+f*SWEEP;
        if(fill)fill.style.width=(f*100)+'%';if(live)live.textContent=v.toFixed(1);if(num)num.textContent=v.toFixed(1);
        if(dial)dial.style.transform='translate(-50%,-50%) rotate('+deg.toFixed(1)+'deg)';
        if(face)face.style.transform='translate(-50%,-50%) rotate('+deg.toFixed(1)+'deg)';
        if(arc)arc.style.strokeDashoffset=(1-f).toFixed(4);
        if(knob){knob.setAttribute('aria-valuenow',v.toFixed(1));knob.setAttribute('aria-valuetext',v.toFixed(1)+'mm')}
      }
      // 스크롤 연동 — 사용자가 다이얼을 만지기 전까지만
      function onScrollUpdate(){
        ticking=false;if(touched||!hasDial)return;
        var r=scaleEl.getBoundingClientRect(),a=window.innerHeight*0.85,b=window.innerHeight*0.25;
        var p=Math.min(Math.max((a-r.top)/(a-b+r.height),0),1);
        setValue(MAX-p*(MAX-MIN));
      }
      function req(){if(!ticking){ticking=true;requestAnimationFrame(onScrollUpdate)}}
      if(hasDial){window.addEventListener('scroll',req,{passive:true});window.addEventListener('resize',req);onScrollUpdate()}
      // 다이얼 돌리기 — 포인터 각도 변화량 누적 (시계방향 = 커짐)
      if(knob){
        var turning=false,lastA=0,acc=0;
        var angleOf=function(e){var r=knob.getBoundingClientRect();return Math.atan2(e.clientY-(r.top+r.height/2),e.clientX-(r.left+r.width/2))*180/Math.PI};
        var markTouched=function(){touched=true;knob.classList.add('is-touched')};
        knob.addEventListener('pointerdown',function(e){markTouched();turning=true;knob.classList.add('is-turning');knob.setPointerCapture(e.pointerId);lastA=angleOf(e);acc=(value-MIN)/(MAX-MIN)*SWEEP;e.preventDefault()});
        knob.addEventListener('pointermove',function(e){
          if(!turning)return;var a=angleOf(e),d=a-lastA;if(d>180)d-=360;if(d<-180)d+=360;lastA=a;
          acc=Math.min(Math.max(acc+d,0),SWEEP);setValue(MIN+acc/SWEEP*(MAX-MIN));
        });
        var stop=function(e){if(!turning)return;turning=false;knob.classList.remove('is-turning');try{knob.releasePointerCapture(e.pointerId)}catch(x){}};
        knob.addEventListener('pointerup',stop);knob.addEventListener('pointercancel',stop);
        knob.addEventListener('wheel',function(e){markTouched();setValue(value+(e.deltaY<0?STEP:-STEP));e.preventDefault()},{passive:false});
        knob.addEventListener('keydown',function(e){var k=e.key;if(k==='ArrowRight'||k==='ArrowUp'){markTouched();setValue(value+STEP);e.preventDefault()}else if(k==='ArrowLeft'||k==='ArrowDown'){markTouched();setValue(value-STEP);e.preventDefault()}});
      }
      var gauge=document.getElementById('pwGauge');
      if(gauge){
        var gMin=2.4,gMax=17.2,gSweep=240,gVal=gMax,gTouched=false,gTick=false;
        var fillP=document.getElementById('pwFill'),needle=document.getElementById('pwNeedle'),psiEl=document.getElementById('pwPsi'),barEl=document.getElementById('pwBar'),rFill=document.getElementById('pwRangeFill'),ticksG=document.getElementById('pwTicks'),pcsG=document.getElementById('pwPcs');
        var cx=160,cy=170,R=120;
        var angOf=function(v){return -120+(v-gMin)/(gMax-gMin)*gSweep};
        var th='';for(var i=0;i<=43;i++){var a=(-120+i*(gSweep/43))*Math.PI/180,big=i%5===0,r1=big?R-30:R-24,r2=R-16;th+='<line x1="'+(cx+r1*Math.sin(a)).toFixed(1)+'" y1="'+(cy-r1*Math.cos(a)).toFixed(1)+'" x2="'+(cx+r2*Math.sin(a)).toFixed(1)+'" y2="'+(cy-r2*Math.cos(a)).toFixed(1)+'"'+(big?' stroke="#fff" stroke-width="2"':'')+'></line>'}ticksG.innerHTML=th;
        var pa=angOf(10)*Math.PI/180,pl=pcsG.querySelector('line'),pt=pcsG.querySelector('text');
        pl.setAttribute('x1',cx+(R-14)*Math.sin(pa));pl.setAttribute('y1',cy-(R-14)*Math.cos(pa));pl.setAttribute('x2',cx+(R+14)*Math.sin(pa));pl.setAttribute('y2',cy-(R+14)*Math.cos(pa));
        pt.setAttribute('x',cx+(R+26)*Math.sin(pa));pt.setAttribute('y',cy-(R+26)*Math.cos(pa)+4);
        function setG(v){
          v=Math.round(Math.min(Math.max(v,gMin),gMax)*10)/10;gVal=v;var f=(v-gMin)/(gMax-gMin);
          fillP.style.strokeDashoffset=(1-f).toFixed(4);needle.setAttribute('transform','rotate('+angOf(v).toFixed(1)+' '+cx+' '+cy+')');
          psiEl.textContent=v.toFixed(1);barEl.textContent=(v>=gMax?250:Math.round(v/0.0689476))+' psi';
          if(rFill)rFill.style.width=(8+f*92).toFixed(1)+'%';
          gauge.setAttribute('aria-valuenow',v.toFixed(1));gauge.setAttribute('aria-valuetext',v.toFixed(1)+' bar');
          var over=Math.max(0,(v-10)/(gMax-10));gauge.style.setProperty('--over',over.toFixed(3));
          var hot=document.getElementById('pwHot');if(hot){hot.style.strokeDashoffset=(1-over).toFixed(4);hot.style.opacity=over>0?1:0}
          var zone=document.getElementById('pwZone');var zi=over<=0?0:(v<13?1:v<15.5?2:3);if(zone)zone.textContent=['','POWER ZONE','HIGH POWER','ULTRA POWER'][zi];
          var zc=['#4fadb8','#4fadb8','#ff9f1c','#ff3b30'][zi];gauge.style.setProperty('--zone',zc);gauge.style.setProperty('--numc',zi>=2?zc:'#fff');gauge.classList.toggle('z3',zi===3);
          gauge.classList.toggle('is-over',v>10);gOver=over;
        }
        var gOver=0,baseAng=angOf(gVal);
        (function jitter(){var o=gOver;if(o>0){var j=(Math.random()-.5)*o*4;needle.setAttribute('transform','rotate('+(angOf(gVal)+j).toFixed(2)+' '+cx+' '+cy+')')}requestAnimationFrame(jitter)})();
        function gScroll(){gTick=false;if(gTouched)return;var r=gauge.getBoundingClientRect(),a=window.innerHeight*0.9,b=window.innerHeight*0.3;var p=Math.min(Math.max((a-r.top)/(a-b+r.height),0),1);setG(gMin+p*(gMax-gMin))}
        function gReq(){if(!gTick){gTick=true;requestAnimationFrame(gScroll)}}
        function gOrbit(){var sv=gauge.querySelector('svg');gauge.style.setProperty('--orbit',(sv.getBoundingClientRect().width/320*120)+'px')}gOrbit();window.addEventListener('resize',gOrbit);
        window.addEventListener('scroll',gReq,{passive:true});window.addEventListener('resize',gReq);gScroll();
        var gOn=false;var gAng=function(e){var sv=gauge.querySelector('svg'),r=sv.getBoundingClientRect(),sx=r.width/320,px=(e.clientX-r.left)/sx,py=(e.clientY-r.top)/sx;return Math.atan2(px-cx,-(py-cy))*180/Math.PI};
        var gApply=function(e){var a=Math.min(Math.max(gAng(e),-120),120);setG(gMin+(a+120)/gSweep*(gMax-gMin))};
        gauge.addEventListener('pointerdown',function(e){gTouched=true;gauge.classList.add('is-touched');gOn=true;gauge.classList.add('is-turning');gauge.setPointerCapture(e.pointerId);gApply(e);e.preventDefault()});
        gauge.addEventListener('pointermove',function(e){if(gOn)gApply(e)});
        var gStop=function(e){if(!gOn)return;gOn=false;gauge.classList.remove('is-turning');try{gauge.releasePointerCapture(e.pointerId)}catch(x){}};
        gauge.addEventListener('pointerup',gStop);gauge.addEventListener('pointercancel',gStop);
        gauge.addEventListener('wheel',function(e){gTouched=true;gauge.classList.add('is-touched');setG(gVal+(e.deltaY<0?0.2:-0.2));e.preventDefault()},{passive:false});
        gauge.addEventListener('keydown',function(e){var k=e.key;if(k==='ArrowRight'||k==='ArrowUp'){gTouched=true;setG(gVal+0.2);e.preventDefault()}else if(k==='ArrowLeft'||k==='ArrowDown'){gTouched=true;setG(gVal-0.2);e.preventDefault()}});
      }
      // 수치 카운트업
      var counters=document.querySelectorAll('.au-count');
      if(counters.length&&'IntersectionObserver' in window){
        var io=new IntersectionObserver(function(es){es.forEach(function(en){if(!en.isIntersecting)return;var el=en.target,to=parseFloat(el.dataset.to),dec=parseInt(el.dataset.dec||'0',10),t0=null;io.unobserve(el);
          function step(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1100,1);p=1-Math.pow(1-p,3);el.textContent=(to*p).toFixed(dec);if(p<1)requestAnimationFrame(step)}requestAnimationFrame(step)})},{threshold:.4});
        counters.forEach(function(c){c.textContent=(0).toFixed(parseInt(c.dataset.dec||'0',10));io.observe(c)});
      }
      var hs=document.querySelectorAll('#auHotspot .au-hs'),fl=document.querySelectorAll('#tabFeatures .au-feat li');
      function hl(btn){hs.forEach(function(b){b.classList.toggle('is-on',b===btn)});fl.forEach(function(li){li.classList.toggle('is-hl',!!btn&&li.dataset.feat===btn.dataset.feat)})}
      hs.forEach(function(b){b.addEventListener('mouseenter',function(){hl(b)});b.addEventListener('mouseleave',function(){hl(null)});b.addEventListener('focus',function(){hl(b)});b.addEventListener('blur',function(){hl(null)});b.addEventListener('click',function(e){e.preventDefault()})});
      var hsBox=document.getElementById('auHotspot');if(hsBox)hsBox.addEventListener('mouseleave',function(){hl(null)});
      var fBox=document.getElementById('auFilter'),fPill=fBox&&fBox.querySelector('.au-filter-pill'),fBtns=fBox?fBox.querySelectorAll('button'):[],cards=document.querySelectorAll('#auModels .au-model');
      function movePill(b){if(!fPill)return;fPill.style.left=b.offsetLeft+'px';fPill.style.top=b.offsetTop+'px';fPill.style.width=b.offsetWidth+'px';fPill.style.height=b.offsetHeight+'px'}
      fBtns.forEach(function(b){b.addEventListener('click',function(){
        fBtns.forEach(function(x){x.classList.remove('is-on');x.setAttribute('aria-selected','false')});b.classList.add('is-on');b.setAttribute('aria-selected','true');movePill(b);
        var k=b.dataset.filter;cards.forEach(function(c){var show=k==='all'||(' '+c.dataset.cat+' ').indexOf(' '+k+' ')>-1;c.classList.toggle('is-hidden',!show);if(show){c.style.animation='none';void c.offsetWidth;c.style.animation=''}});
      })});
      if(fBtns.length){movePill(fBox.querySelector('.is-on'));window.addEventListener('resize',function(){movePill(fBox.querySelector('.is-on'))})}
      var tabs=document.querySelectorAll('.au-tabbar [role=tab]');
      tabs.forEach(function(b){b.addEventListener('click',function(){
        tabs.forEach(function(x){x.classList.remove('is-on');x.setAttribute('aria-selected','false');var p=document.getElementById(x.getAttribute('aria-controls'));if(p){p.classList.remove('is-on');p.hidden=true}});
        b.classList.add('is-on');b.setAttribute('aria-selected','true');var p=document.getElementById(b.getAttribute('aria-controls'));if(p){p.classList.add('is-on');p.hidden=false}
      })});
      document.querySelectorAll('.au-pc-play').forEach(function(btn){
        btn.addEventListener('click',function(){
          var v=document.getElementById(btn.dataset.v),box=btn.parentNode;if(!v)return;
          if(v.paused){v.play();box.classList.add('is-playing');btn.querySelector('span').textContent='일시정지';btn.querySelector('i').textContent='❚❚'}
          else{v.pause();box.classList.remove('is-playing');btn.querySelector('span').textContent='영상 재생';btn.querySelector('i').textContent='▶'}
        });
      });
    })();
  </script>
"""
# PLT ULTRA는 BLASTER_MODELS에 넣지 않는다 — 넣으면 다른 모델 페이지의 "같은 카테고리의
# 다른 모델" 카드 목록이 바뀌어 핸드오프 HTML과 달라진다. 별도 목록으로만 생성.
BLASTER_EXTRA_PAGES = [
    {"slug": "aero2-plt-ultra", "custom_title": AERO2_PLT_ULTRA_TITLE, "custom_desc": AERO2_PLT_ULTRA_DESC,
     "custom_body": AERO2_PLT_ULTRA_BODY, "custom_script": AERO2_PLT_ULTRA_SCRIPT},
]



BLASTER_CATEGORIES = [
    ("smart", "① 스마트 블라스터", "IoT · Industry 4.0 — Cold Jet CONNECT&reg;로 원격 모니터링 · 진단이 가능한 라인입니다."),
    ("pellet", "② 펠렛 블라스터", "범용 산업현장을 위한 표준 라인입니다."),
    ("particle", "③ 마이크로파티클 블라스터", "정밀 세척을 위한 소형 · 정밀 라인입니다."),
    ("specialty", "④ 특수 목적 블라스터", "특수한 작업 조건을 위한 전용 라인입니다."),
]

BLASTER_MODELS = [
    {
        "slug": "aero2-ultra", "category": "smart", "name": "Aero2 PCS&reg; ULTRA",
        # (2026-10-14, §55) 상세 페이지는 커스텀 본문으로 교체 — 아래 features/specs 데이터는
        # 더 이상 이 페이지 출력에 쓰이지 않지만 다른 모델 페이지의 카드(name/tagline)용으로 유지.
        "custom_title": AERO2_PCS_ULTRA_TITLE, "custom_desc": AERO2_PCS_ULTRA_DESC,
        "custom_body": AERO2_PCS_ULTRA_BODY, "custom_script": AERO2_PCS_ULTRA_SCRIPT,
        "tagline": "0.3~3.0mm 28단계 입자 제어, 가장 다재다능한 스마트 드라이아이스 블라스터",
        "overview": [
            "Aero2 ULTRA 시리즈는 Cold Jet이 선보이는 최고 사양의 스마트 드라이아이스 블라스터 라인입니다. "
            "작업자를 배려한 직관적인 HMI 디스플레이와 인체공학적 설계로, 세척 과정을 완전히 제어할 수 있습니다.",
        ],
        "advantages": [
            ("Smart", "Cold Jet CONNECT&reg;를 통한 원격 모니터링 · 진단 (업계 최초)"),
            ("Easy to Use", "7인치 LCD 화면과 디지털 컨트롤로 손쉬운 조작"),
            ("Versatile", "특허받은 입자 제어 시스템(PCS)으로 3mm~0.3mm까지 입자 크기 정밀 조정"),
            ("Efficient", "직선형(straight-through) 에어 시스템으로 공급 효율 극대화"),
            ("Consistent", "특허받은 SureFlow 피더 시스템으로 일관된 드라이아이스 공급"),
        ],
        "features": [
            "Aero2 PCS ULTRA — 특허받은 입자 제어 시스템(PCS)으로 드라이아이스 입자 크기를 3mm~0.3mm까지 정밀 조정",
            "Aero2 PLT ULTRA — 펄스 없는 강력한 분사를 구현하는 혁신적 에어 시스템으로 강력한 오염물 제거",
            "7인치 LCD 터치스크린으로 현장에서 직접 설정 확인 · 조정",
            "Cold Jet CONNECT&reg;를 통한 원격 모니터링 · 진단",
            "Industry 4.0 스마트팩토리 환경에 대응하는 경량화 설계",
        ],
        "specs": [
            ("구성", "Aero2 PCS ULTRA / Aero2 PLT ULTRA 2개 모델"),
            ("제어 방식", "7인치 LCD 터치스크린"),
            ("원격 관리", "Cold Jet CONNECT&reg; 지원"),
            ("입자 조정 범위 (PCS ULTRA)", "3mm ~ 0.3mm"),
            ("상세 스펙", "무게 · 크기 · 압력 · 공기 소비량 등 수치 스펙은 정식 스펙시트로 안내해 드립니다"),
        ],
        "accessories": True,
    },
    {
        "slug": "i3-microclean-2", "category": "smart", "name": "i3 MicroClean&reg; 2",
        "tagline": "1세대보다 드라이아이스 사용량을 25% 이상 줄인 2세대 정밀 스마트 블라스터",
        "overview": [
            "\"Soft on Surfaces. Tough on Contaminants.\" i3 MicroClean 2는 향상된 파워와 효율, 직관적인 제어, "
            "IoT 연동 기능을 갖춘 차세대 정밀 세척 솔루션입니다. 1세대 대비 소모품(드라이아이스) 사용량을 25% "
            "이상 절감하면서도, 블록 · 펠렛을 모두 사용할 수 있는 유연성을 유지합니다.",
        ],
        "advantages": [
            ("Efficient", "1세대 i3 MicroClean 대비 소모품 사용량 25% 이상 절감"),
            ("IoT Capability", "Cold Jet CONNECT&reg;로 원격 모니터링 · 진단"),
            ("Intuitive Controls", "7인치 LCD 화면으로 파라미터 조정 · 레시피 저장"),
            ("Designed for Precision", "민감한 표면과 복잡한 형상도 안전하게 세척"),
            ("Low Noise Operation", "낮은 공급 압력으로도 효과적으로 작동해 소음 감소"),
        ],
        "features": [
            "1세대 i3 MicroClean 대비 소모품(드라이아이스) 사용량 25% 이상 절감",
            "Cold Jet CONNECT&reg; 연동으로 사용 데이터 원격 확인",
            "블록 · 펠렛 겸용 호퍼로 유연한 운영",
            "정전기 방지 접지 케이블 내장",
        ],
        "specs": [
            ("전체 시스템 크기 · 무게", "79 × 64 × 119 cm, 86 kg (190 lbs)"),
            ("블라스터 본체 크기 · 무게", "79 × 48 × 53 cm, 60.5 kg (133.4 lbs)"),
            ("호퍼 용량", "11 kg (25 lbs), 블록 · 펠렛 겸용"),
            ("사용 압력", "1.4 ~ 10 bar (20 ~ 145 psi)"),
            ("공기 소비량", "0.3 ~ 1.4 ㎥/min (80 psi 기준)"),
            ("공급 속도", "0 ~ 0.7 kg/min"),
        ],
        "accessories": True,
    },
    {
        "slug": "aero-series", "category": "pellet", "name": "Aero&reg; Series (40FP / 80FP)",
        "tagline": "풀프레셔(Full-Pressure) 전문가용 블라스터, 호퍼 용량별 40FP · 80FP 2종",
        "overview": [
            "\"Proven, time tested machines.\" Aero 시리즈는 오랜 기간 현장에서 검증된 펠렛 블라스터입니다. "
            "20 psi(1.4 bar)의 부드러운 세척부터 300 psi(20 bar)의 강력한 블라스팅까지, 전 압력 구간에서 "
            "안정적인 성능을 제공합니다.",
        ],
        "advantages": [
            ("Performance SureFlow System", "특허받은 시스템으로 호퍼를 가득 채운 채 30m 호스로도 막힘 없이 사용"),
            ("Patented Feeder Technology", "공기역학적 로딩 방식으로 패드 · 로터 마모를 줄여 장비 수명 연장"),
            ("Advanced Radial Feeding System", "펄스 없는 일관된 분사와 정밀한 이송속도 제어"),
            ("Full Range of Pressure", "20 psi(1.4 bar)부터 300 psi(20 bar)까지 전 압력 구간 대응"),
            ("Rugged and Mobile", "고강도 산업 현장에서의 지속적인 사용을 견디는 내구성"),
        ],
        "features": [
            "공기역학적 로딩 설계로 패드 · 로터 마모를 줄여 장비 수명 연장",
            "경량 컴팩트 모터로 무게 절감과 전력 소비 감소",
            "펄스 없는 일관된 펠렛 공급과 정밀 이송속도 제어가 가능한 로터",
            "전 압력 구간(Full range of blast pressure) 대응",
            "온보드 압력 조절기 탑재",
        ],
        "specs": [
            ("무게 (40FP)", "116.8 kg (257 lbs)"),
            ("크기 (40FP)", "91 × 51 × 102 cm"),
            ("호퍼 용량 (40FP)", "18.2 kg (40 lbs)"),
            ("사용 압력", "1.4 ~ 17.2 bar (20 ~ 250 psi)"),
            ("공기 소비량 (40FP)", "2.8 ~ 4.7 ㎥/min (80 psi 기준)"),
            ("공급 속도 (40FP)", "0 ~ 2 kg/min"),
            ("80FP", "40FP와 동일 계열의 대용량 호퍼 모델 (상세 스펙은 견적 문의 시 안내)"),
        ],
        "accessories": True,
    },
    {
        "slug": "elite20-icerocket", "category": "pellet", "name": "Elite 20 &amp; IceRocket PLT",
        "tagline": "전문가급 성능의 입문형 블라스터 2종",
        "overview": [
            "\"Versatile and reliable machines for many applications.\" Elite 20과 IceRocket PLT는 신뢰할 수 있는 "
            "성능을 합리적인 가격에 제공하는 전문가급 입문형 블라스터입니다. 가벼운 작업부터 고강도 작업까지 "
            "폭넓게 대응하는 운영 유연성을 갖췄습니다.",
        ],
        "advantages": [
            ("Durable", "스테인리스 스틸 프레임으로 내구성과 신뢰성 확보"),
            ("Insulated Lid and Hopper", "드라이아이스 승화를 최소화해 중단 없는 세척 보장"),
            ("Easy-adjusting Dosing System", "드라이아이스 투입량을 손쉽게 조절"),
            ("User Friendly Control Panel", "블라스팅 파라미터를 직관적으로 제어"),
        ],
        "features": [
            "스테인리스 스틸 프레임으로 내구성과 신뢰성 확보",
            "단열 뚜껑과 호퍼로 드라이아이스 승화를 최소화, 중단 없는 세척 보장",
            "손쉬운 용량 조절과 사용자 친화적 제어판",
            "IceRocket PLT — 최소한의 압축공기 요구조건으로도 안정적으로 작동",
            "Elite 20 — 다목적 · 중작업용 대형 블라스팅에 적합",
        ],
        "specs": [
            ("구성", "Elite 20 / IceRocket PLT 2개 모델"),
            ("프레임", "스테인리스 스틸"),
            ("호퍼", "단열 설계"),
            ("상세 스펙", "무게 · 크기 · 압력 · 공기 소비량 등 수치 스펙은 정식 스펙시트로 안내해 드립니다"),
        ],
        "accessories": True,
    },
    {
        "slug": "i3-microclean", "category": "particle", "name": "i3 MicroClean&reg;",
        "tagline": "특허받은 단일호스 패턴 공급 기술의 탁상형 정밀 블라스터",
        "overview": [
            "\"Gentle Cleaning in a Table-top Format.\" i3 MicroClean은 가볍고 정밀한 단일호스 저압 블라스터로, "
            "최소 12 CFM의 공기로도 작동하며 20~140 psi(1.4~9.7 bar)의 다양한 압력에서 블록 드라이아이스로 "
            "블라스팅할 수 있습니다.",
        ],
        "advantages": [
            ("Efficient", "1회 충전으로 최대 45분 연속 세척"),
            ("Flexibility", "조정 가능한 분사 압력으로 성능 최적화"),
            ("Designed for Precision Applications", "민감한 표면과 복잡한 형상도 안전하게 세척"),
            ("Low Noise Operation", "낮은 공급 압력으로 조용한 작동"),
        ],
        "features": [
            "1회 충전으로 최대 45분 연속 세척 가능",
            "특허받은 단일호스 공급 장치로 최대 분사 정밀도 제공",
            "5×5×10인치 또는 6×6×12인치 블록 드라이아이스 사용",
            "조정 가능한 분사 압력으로 성능 최적화",
            "내장 20마이크론 에어필터로 오염된 압축공기 영향 최소화",
            "인체공학적 조명 적용기, 통합 정전기 방지 본딩 케이블",
            "컴팩트 · 휴대 가능한 설계, 내구성 있는 이동 카트 포함",
        ],
        "specs": [
            ("무게", "59.1 kg (130 lbs)"),
            ("크기", "55.9 × 40.6 × 53.3 cm"),
            ("호퍼 용량", "9.1 kg (20 lbs)"),
            ("사용 압력", "1.4 ~ 9.7 bar (20 ~ 140 psi)"),
            ("공기 소비량", "0.3 ~ 1.4 ㎥/min (140 psi 기준)"),
            ("공급 속도", "0 ~ 0.5 kg/min"),
            ("사용 드라이아이스", "5\"×5\"×10\" 또는 6\"×6\"×12\" 블록"),
            ("부품 번호", "2A0169"),
        ],
        "accessories": True,
    },
    {
        "slug": "sdi-select-60", "category": "particle", "name": "SDI Select&trade; 60",
        "tagline": "바테크가 국내에도 공급해 온 대표 범용 모델",
        "overview": [
            "\"Utilize Any Type of Dry Ice.\" SDI Select 60은 단순하고 사용하기 쉬우며 다재다능한 드라이아이스 "
            "블라스터입니다. 특허받은 피더 기술로 표준 블록부터 3mm 펠렛, 너겟, 슬라이스, 심지어 남은 스크랩 "
            "아이스까지 셰이브 방식으로 사용할 수 있어, 드라이아이스 수급이 제한적인 현장에도 새로운 세척 "
            "기회를 열어줍니다. Aero 계열 노즐 · 액세서리와 호환되며 20~250 PSI 범위에서 부드럽게도, "
            "강력하게도 세척할 수 있습니다.",
        ],
        "advantages": [
            ("Shave with Any Type of Dry Ice", "표준 블록 · 3mm 펠렛 · 너겟 · 슬라이스 · 스크랩 아이스까지 모두 사용 가능"),
            ("Low Noise Levels", "최소 50 CFM부터 세척 가능해 압축공기 비용과 소음 절감"),
            ("Clean Aggressively", "최대 250 PSI까지 압력을 높여 강한 오염물도 제거"),
            ("Versatile", "민감한 표면부터 고강도 오염까지 폭넓게 대응"),
        ],
        "features": [
            "표준 블록부터 스크랩 아이스까지, 어떤 드라이아이스 미디어든 사용 가능(Shave 방식)",
            "3mm 펠렛 성능을 위한 바이패스 기능",
            "최소 50 CFM부터 세척 가능해 압축공기 비용 절감",
            "최대 250 PSI까지 압력 조절 가능",
            "Aero 노즐 및 액세서리와 호환",
        ],
        "specs": [
            ("무게", "155.9 kg (343 lbs)"),
            ("크기", "61 × 71 × 109 cm (24×28×43\")"),
            ("호퍼 용량", "27.2 kg (60 lbs)"),
            ("사용 압력", "1.4 ~ 17.2 bar (20 ~ 250 psi)"),
            ("공기 소비량", "1.4 ~ 6.1 ㎥/min · 50~215 CFM (80 psi 기준)"),
            ("공급 속도", "0 ~ 2.7 kg/min (0~6 lbs/min)"),
            ("부품 번호", "2A0253 / 2A0236"),
        ],
        "accessories": True,
    },
    {
        "slug": "c100", "category": "specialty", "name": "C100",
        "tagline": "전원 없이 압축공기만으로 작동하는 완전 공압식 블라스터",
        "overview": [
            "\"A Fully Pneumatic Machine.\" Aero C100 Pneumatic은 지금까지 나온 공압식 드라이아이스 블라스터 "
            "중 가장 강력하고 효율적인 모델입니다. 다른 공압식 장비 대비 2배 빠른 세척 성능과, 매번 균일하게 "
            "세척되는 펄스 없는 분사 스트림을 제공합니다.",
        ],
        "advantages": [
            ("Fully Pneumatic Machine", "전원 연결 없이 압축공기만으로 작동, 다른 공압식 대비 2배 빠른 세척"),
            ("Performance SureFlow System", "호퍼를 가득 채운 채 30m 호스로도 막힘 없이 사용"),
            ("Advanced Radial Feeding System", "펄스 없는 분사와 정밀한 이송속도 제어"),
            ("Patented Feeder Technology", "공기역학적 로딩으로 패드 · 로터 마모 감소"),
            ("Full Range of Pressure", "20 psi(1.4 bar)부터 250 psi(17.2 bar)까지 전 구간 대응"),
        ],
        "features": [
            "완전 공압식(Fully pneumatic) 기계로 전원 연결이 불필요",
            "다른 공압식 장비 대비 세척 속도 2배",
            "펄스 없는 스트림으로 매번 균일한 세척",
            "최대 30m(100ft) 호스 길이 지원",
            "1인치 Urebrade 블라스트 호스, 에어호스, 무광 어플리케이터, 정전기 방지 케이블, 노즐 행어, "
            "호스랩, 호스 캐리어 기본 포함",
        ],
        "specs": [
            ("호퍼 용량", "45.5 kg (100 lbs)"),
            ("무게", "117 kg (257 lbs)"),
            ("크기", "78.7 × 38.1 × 114.3 cm"),
            ("사용 압력", "1.4 ~ 17.2 bar (20 ~ 250 psi)"),
            ("공기 소비량", "1.4 ~ 5 ㎥/min (80 psi 기준)"),
            ("공급 속도", "0 ~ 3.2 kg/min (0~7 lbs/min)"),
            ("공급 압력 범위", "65 ~ 250 psi"),
            ("부품 번호", "2A0155"),
        ],
        "accessories": True,
    },
    {
        "slug": "e-co2-150", "category": "specialty", "name": "E-CO2&trade; 150",
        "tagline": "연마재 + 드라이아이스 복합 분사, 도장 · 코팅 · 부식 제거 전용",
        "overview": [
            "부식 · 도장 제거 등 기존 세척 방식은 다량의 호흡성 분진과 2차 폐기물을 남기고, 표면에 수분 · "
            "잔여물을 남기는 경우가 많습니다. E-CO2 150은 Cold Jet 드라이아이스 블라스터(PLT 60 · Aero 80 · "
            "C100)와 1.5입방피트 규모의 전용 가압 연마재 포트를 결합해 이 문제를 해결합니다. 트리거 한 번으로 "
            "연마재와 드라이아이스를 동시에 분사합니다.",
        ],
        "advantages": [
            ("Reduce Respirable Dust", "제3자 검증 기준 호흡성 · 유해 분진 최대 97% 감소"),
            ("Meet OSHA and Environmental Guidelines", "호흡성 분진 · 2차 폐기물 관련 규정을 손쉽게 충족"),
            ("Allows for Immediate Re-coating", "표면에 수분 · 잔여물이 남지 않아 별도 건조 공정 불필요"),
            ("Achieve Cleanliness Levels", "SP10 / SA2.5 / NA2 수준의 청정도 달성"),
            ("Environmentally Responsible", "재생 CO2로 만든 드라이아이스와 재생 연마재 사용"),
        ],
        "features": [
            "Cold Jet 고유의 연마재-드라이아이스 혼합물을 트리거 한 번으로 동시 분사",
            "제3자 검증 기준 호흡성 분진 최대 97% 감소",
            "표면에 수분 · 잔여물을 남기지 않아 건조 공정 불필요",
            "SP10 / SA2.5 / NA2 수준의 청정도 달성",
            "도장 제거, 코팅 제거, 부식 제거 등 산업 코팅 제거 작업에 특화",
        ],
        "specs": [
            ("블라스트 포트 용량", "68 kg (150 lbs)"),
            ("건조 중량", "61.2 kg (135 lbs)"),
            ("크기", "61 × 53.3 × 99 cm (24×21×39\")"),
            ("사용 압력", "50 ~ 150 psi"),
            ("공급 압력 범위", "100 ~ 150 psi"),
            ("노즐 공기 소비량", "2.0 ~ 6.1 ㎥/min · 70~215 CFM (80 psi 기준)"),
            ("페어링 가능 블라스터", "PLT 60 · Aero 80 · C100"),
        ],
        "accessories": True,
    },
]

# ---------------------------------------------------------------------------
# 펠렛타이저 데이터
# ---------------------------------------------------------------------------

PELLETIZER_MODELS = [
    {
        "slug": "pe-80", "name": "PE-80", "tagline": "저용량 · 입문형 펠렛타이저",
        "features": [
            "사용자 친화적 인터페이스와 간단한 조작으로 초보자도 쉽게 운영",
            "3 mm 블라스팅 펠렛 전용 생산",
            "다양한 전원 사양 지원(400V/50Hz, 480V/60Hz, 220V/50Hz, 200V/60Hz)",
        ],
        "specs": [
            ("생산능력", "최대 80 kg/h (176 lbs/hr)"),
            ("펠렛 크기", "3 mm 전용"),
            ("소비전력", "3 kWh (최대 6.5A)"),
            ("크기", "600 × 1000 × 1560 mm"),
            ("무게", "203 kg (447.5 lbs)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 80", "re-co2-80")]},
    },
    {
        "slug": "pr120h", "name": "PR120H", "tagline": "중소용량 고용량 시리즈",
        "features": [
            "7인치 터치스크린 패널PC로 원격 지원 가능",
            "방습 인클로저로 소음 75dB(A) 이하로 감소",
            "서브쿨링 기술로 CO2 낭비 최소화",
        ],
        "specs": [
            ("생산능력", "120 kg/h (265 lbs/hr)"),
            ("펠렛 크기", "3 / 10 / 16 mm (요청 시 다른 크기 가능)"),
            ("크기", "1150 × 650 × 1738 mm"),
            ("무게", "704 kg (1552 lbs, 유압유 포함)"),
            ("기동 시간", "5분 이내"),
            ("공기 품질", "ISO 8573-1, Class 3 이상"),
            ("부품 번호", "512641 (CE & UL 인증)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 160", "re-co2-160")]},
    },
    {
        "slug": "pr350h", "name": "PR350H", "tagline": "중용량 고성능 펠렛타이저",
        "features": [
            "폐쇄형 챔버 기술로 짧은 기동시간과 빠른 생산",
            "원버튼 자동운전",
            "자동 다이 교체로 4가지 펠렛 크기 즉시 전환",
        ],
        "specs": [
            ("생산능력", "350 kg/h (772 lbs/hr)"),
            ("펠렛 크기", "3 / 6 / 10 / 16 mm (자동 다이 교체)"),
            ("크기", "1500 × 1000 × 1800 mm"),
            ("무게", "1515 kg (유압유 포함)"),
            ("기동 시간", "3분 미만"),
            ("소음", "75 dB(A) 이하"),
            ("CO2 변환계수", "2.2 (업계 최저 수준)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 320 V2", "re-co2-320-v2")]},
    },
    {
        "slug": "pr750h", "name": "PR750H", "tagline": "대용량 생산 라인용",
        "features": [
            "폐쇄형 챔버 기술로 빠른 시작과 생산 보장",
            "15인치 터치스크린, 인터넷 연결 시 원격 지원",
            "방음 인클로저로 소음 75dB(A) 이하",
            "서브쿨링 기술, 자동 익스트루더 플레이트 교환으로 다운타임 및 CO2 손실 절감",
        ],
        "specs": [
            ("생산능력", "750 kg/h (1,653 lbs/hr)"),
            ("펠렛 크기", "3 / 6 / 10 / 16 mm (자동 다이 교체)"),
            ("크기", "1500 × 1500 × 1800 mm"),
            ("무게", "1822 kg (4017 lbs, 유압유 포함)"),
            ("모델 번호", "90636 (CE 380V·50Hz) / 90637 (UL 480V·60Hz)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 320 V2", "re-co2-320-v2"), ("RE-CO2 3500", "re-co2-3500")]},
    },
    {
        "slug": "pr1500h", "name": "PR1500H", "tagline": "PR H 시리즈 최상위, 초대형 생산시설용",
        "features": [
            "폐쇄형 챔버 기술, 15인치 터치스크린 원격 지원",
            "이전 세대 대비 연장된 서비스 간격",
            "방음 · 방습 인클로저로 소음 80dB(A) 이하",
            "서브쿨링 기술, 자동 익스트루더 플레이트 교환",
        ],
        "specs": [
            ("생산능력", "1,500 kg/h (3,306 lbs/hr)"),
            ("펠렛 크기", "3 / 6 / 10 / 16 mm"),
            ("크기", "2210 × 1820 × 2150 mm"),
            ("무게", "4000 kg (8818 lbs)"),
            ("CO2 공급 압력", "13 ~ 18 bar (188~261 psi)"),
            ("압축공기 공급", "8 ~ 10 bar (116~145 psi)"),
            ("전력", "3×480V AC / 60Hz (25 kW / 33.5 Hp)"),
            ("소음", "80 dB(A) 이하"),
            ("작동 온도 범위", "5°C ~ 43°C (41~109°F)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 3500", "re-co2-3500")]},
    },
    {
        "slug": "special-forms", "name": "DS 시리즈 · R 시리즈 (특수 형태)",
        "tagline": "슬라이스형 드라이아이스, 펠렛 → 슬라이스 변환 장비",
        # (2026-09-17, 17차 핸드오프) 이 모델 카드/제목 태그/CTA는 허브·형제
        # 페이지가 공유하는 name/tagline을 그대로 쓰고, 페이지 자신의
        # 브레드크럼·H1·히어로 설명만 page_breadcrumb/page_title/page_tagline로
        # 덮어쓴다(R Series 리포머 중심으로 재편집). features/specs는 페이지
        # 전용이라 직접 교체.
        "page_breadcrumb": "R 시리즈 리포머",
        "page_title": "R 시리즈 슬라이스 리포머",
        "page_tagline": "펠렛을 필요한 규격의 슬라이스와 블록으로 재성형하는 장비",
        "features": [
            "R500H · R1000H · R2000H — 생산된 펠렛을 슬라이스와 블록으로 재성형",
            "요구 규격과 처리량에 맞춰 리포머 모델을 선택",
            "리포머에 펠렛을 공급할 드라이아이스 제조기가 별도로 필요",
        ],
        "specs_headers": ("모델", "최대 처리능력"),
        "specs": [
            ("R500H", "600 kg/h"),
            ("R1000H", "1,000 kg/h"),
            ("R2000H", "2,500 kg/h"),
        ],
    },
]

# ---------------------------------------------------------------------------
# CO2 리커버리 데이터
# ---------------------------------------------------------------------------

RECOVERY_INTRO_HTML = """
<p>드라이아이스를 생산할 때 액체 CO2를 대기압으로 낮추는 과정에서 절반 가량은 드라이아이스(고체)로,
나머지 절반은 가스로 바뀝니다. 이 가스는 보통 그대로 대기 중에 배출되는데, Cold Jet의
<b>RE-CO2 리커버리 시스템</b>은 이 가스를 회수해 다시 드라이아이스 생산에 투입합니다.
그 결과 액체 CO2 사용량과 비용을 크게 줄일 수 있습니다.</p>
<div class="icon-row" style="grid-template-columns:repeat(4,1fr);">
  <div class="item"><div class="ic">💧</div><span>액체 CO2 최대 40% 절감</span></div>
  <div class="item"><div class="ic">📈</div><span>동일 LCO2로 최대 70% 증산</span></div>
  <div class="item"><div class="ic">🌍</div><span>대기 배출 CO2 저감</span></div>
  <div class="item"><div class="ic">⏱️</div><span>ROI 대부분 12개월 이내</span></div>
</div>
<p style="margin-top:22px; font-size:13px; color:var(--text-muted);">거의 모든 브랜드의 펠렛타이저와 호환되는
모듈식 설계로, 기존 생산 라인에도 비교적 쉽게 추가할 수 있습니다. (출처: Cold Jet 공식 웹사이트)</p>
"""

RECOVERY_HERO_HTML = """    <section class="subhero-parallax rec-hero-stage">
      <div class="subhero-breadcrumb wrap"><a href="../../index.html">홈</a> &gt; <a href="../index.html">제품 · 자동화 · 공급</a> &gt; CO₂ 리커버리</div>
      <div class="hero-fit">
        <video class="subhero-parallax-img rec-hero-video" autoplay muted loop playsinline preload="auto" data-buffer="60" data-pan-scale="1.06" data-blur-start="0.5">
          <source src="../../assets/video/recovery-hero.mp4" type="video/mp4" />
        </video>
        <div class="subhero-textbox">
          <span class="ind-hero-eyebrow">COLD JET × VATEK / CO₂ RECOVERY SYSTEM</span>
          <h1>버려지던 CO₂를<br><span class="bls-hero-accent">다시 생산 자원으로.</span></h1>
          <p class="bls-hero-main">드라이아이스 생산 과정에서 발생하는 리버트 가스(revert gas)를 회수해 다시 액화하고, 펠렛타이저 생산에 재사용합니다. 버려지는 CO<sub>2</sub>를 줄이고 LCO<sub>2</sub> 사용 효율을 높이는 회수·재액화 시스템입니다.</p>
        </div>
        <div class="pel-hero-mask" aria-hidden="true">
          <img src="../../assets/img/coldjet-logo.png" alt="" />
          <span>×</span>
          <img src="../../assets/img/vatek-logo-wordmark.png" alt="" />
        </div>
      </div>
    </section>"""

_RECOVERY_COMMON_FEATURES = [
    "거의 모든 브랜드 펠렛타이저와 호환되는 모듈형 설계",
    "액체 CO2 사용량 절감으로 운영비 감소",
    "동일 액체 CO2 투입량 대비 드라이아이스 증산 가능",
    "대기 중 CO2 배출 저감",
]

RECOVERY_MODELS = [
    {
        "slug": "re-co2-80", "name": "RE-CO2 80", "tagline": "소규모 운영을 위한 모듈형 CO2 리커버리",
        "overview": [
            "RE-CO2 80은 PE-80과 같은 소형 펠렛타이저와 페어링되는 입문형 CO2 리커버리 모델로, "
            "소규모 생산 라인에도 CO2 재사용 효과를 적용할 수 있습니다.",
        ],
        "features": _RECOVERY_COMMON_FEATURES,
        "specs": [
            ("처리 용량", "최대 80 kg/h"),
            ("적합 조합", "PE-80 펠렛타이저"),
            ("상세 스펙", "정식 스펙시트로 안내해 드립니다"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PE-80", "pe-80")]},
    },
    {
        "slug": "re-co2-160", "name": "RE-CO2 160", "tagline": "중소 규모 생산 라인을 위한 CO2 리커버리",
        "overview": [
            "RE-CO2 160은 PR120H와 같은 중소용량 펠렛타이저와 페어링되는 모델로, 중간 규모 운영에서도 "
            "안정적인 CO2 회수 효율을 제공합니다.",
        ],
        "features": _RECOVERY_COMMON_FEATURES,
        "specs": [
            ("처리 용량", "최대 160 kg/h"),
            ("적합 조합", "PR120H 펠렛타이저"),
            ("상세 스펙", "정식 스펙시트로 안내해 드립니다"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PR120H", "pr120h")]},
    },
    {
        "slug": "re-co2-320-v2", "name": "RE-CO2 320 V2",
        "tagline": "가장 지능형 · 확장 가능 · 지속가능한 동급 최대 규모 CO2 리커버리 시스템",
        "overview": [
            "RE-CO2 320 V2는 드라이아이스 생산시설에서 배출되는 CO2 가스를 포집해 액체로 전환한 뒤 다시 "
            "생산에 투입하는 컴팩트한 리커버리 유닛입니다. V2 모델은 Cold Jet 펠렛타이저 제어판과 직접 "
            "통신하며, 여러 대를 동시에 운용할 때도 지능형으로 가스 흐름을 최적화합니다.",
        ],
        "advantages": [
            ("Sustainability", "배출되던 CO2 가스를 생산 자원으로 전환"),
            ("Efficiency", "액체 CO2 낭비를 최소화"),
            ("Cost Reduction", "연간 액체 CO2 비용을 최대 40%까지 절감"),
            ("Output Expansion", "동일한 액체 CO2 투입량으로 생산량을 최대 70%까지 확대"),
            ("User-Friendly", "펠렛타이저 HMI로 플러그앤플레이 제어, 규모에 맞춘 모듈 구성"),
        ],
        "features": [
            "재설계된 버퍼탱크 프레임 · 커버로 최적화된 가스 흐름",
            "개선된 밸브 제어 연결부",
            "과열 컨트롤러가 탑재된 전기 캐비닛",
            "24V DC 코일 및 추가 온도 센서",
            "저온 지역 대응 접근 플러그",
            "고성능 냉각팬 및 클로 커플링 모터",
            "바이패스 밸브가 장착된 리시버",
            "업그레이드된 2단 오일 분리기 · 오일 레귤레이터",
        ],
        "specs": [
            ("액화 용량", "최대 320 kg/h (705.4 lbs/hr)"),
            ("크기 (가로×세로×높이)", "2,718 × 1,320 × 3,751 mm"),
            ("버퍼탱크 미포함 높이", "2,259 mm"),
            ("유닛 무게", "2,175 kg (버퍼탱크 325 kg 별도)"),
            ("전원", "440~480V AC 60Hz 또는 400V AC 50Hz"),
            ("소비전력 · 전류", "50 kWh, 85A"),
            ("냉매유 · 압축기유", "POE32 / PAO68 (식품등급)"),
            ("작동 온도 범위", "5℃ ~ 30℃"),
            ("소음", "최대 85 dB"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PR350H", "pr350h"), ("PR750H", "pr750h")]},
    },
    {
        "slug": "re-co2-3500", "name": "RE-CO2 3500", "tagline": "대형 생산시설을 위한 고용량 · 고효율 CO2 리커버리",
        "overview": [
            "RE-CO2 3500은 대형 생산시설을 위한 고용량 CO2 리커버리 유닛입니다. 배출된 CO2를 압축 · "
            "냉각해 재사용 가능한 액체 CO2로 전환하며, 배출량 저감과 외부 공급 의존도 감소, 액체 CO2 "
            "비용 최대 절반 절감 효과를 기대할 수 있습니다. 컨테이너형 모듈로 최소한의 설비 변경만으로 "
            "설치할 수 있습니다.",
        ],
        "advantages": [
            ("Ultra-Low Energy Use", "동급 시스템 대비 업계 최저 수준의 에너지 소비"),
            ("R744 Refrigerant", "합성 냉매 없이 자연 냉매(CO2, R744) 사용"),
            ("Flexible Operation", "최대 용량 대비 25~100% 범위에서 유동적으로 운전"),
            ("Fully Autonomous", "운영자 개입 없이 완전 자동으로 운전"),
            ("Containerized Setup", "표준 컨테이너형으로 간편하게 설치"),
        ],
        "features": [
            "회수 CO2 톤당 135 kWh 이하의 에너지 소비",
            "합성 냉매가 필요 없는 자연 냉매(R744, CO2) 방식",
            "운영자 개입이 필요 없는 완전 자동 운전",
            "펠렛타이저 1~6대 규모까지 자동으로 생산 규모에 대응",
            "컨테이너형 설계로 최소한의 공간에 간편 설치",
            "오일프리 압축기로 암모니아 시스템 대비 유지보수 부담 최소화",
        ],
        "specs": [
            ("크기", "12.5m × 8.5m × 4.3m (컨테이너형)"),
            ("무게", "35,000 kg"),
            ("표준 처리 용량", "3,500 kg/h (옵션 시 최대 5,000 kg/h)"),
            ("전원", "3×400V+N+PE, 50Hz, TN-S"),
            ("소비전력", "톤당 135 kWh 이하"),
            ("냉매", "R744(CO2) 자연 냉매, 폐쇄루프 방식"),
            ("계장용 공기", "7 barg, ISO 8573-1 Class 2 기준"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PR750H", "pr750h"), ("PR1500H", "pr1500h")]},
    },
]

ACCESSORIES_HTML = """
<div class="sub-grid">
  <div class="sub-card"><h3>Applicators (어플리케이터)</h3><p>작업자의 편의성과 안전성을 고려해 설계된 핸들형 분사기구입니다.</p></div>
  <div class="sub-card"><h3>Nozzles (노즐)</h3><p>세척 강도와 분사 패턴을 결정하는 업계 최첨단 노즐 라인입니다.</p></div>
  <div class="sub-card"><h3>Hoses (호스)</h3><p>유연하면서도 내구성 있는 에어 · 블라스트 전용 호스입니다.</p></div>
  <div class="sub-card"><h3>Additional Accessories (기타 액세서리)</h3><p>퀵 커넥트 피팅 등 작업 편의를 높이는 부속품입니다.</p></div>
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:14px;">전체 라인업은
<a href="../nozzle.html">노즐 · 액세서리</a> 페이지에서도 확인하실 수 있습니다.</p>
"""


def _features_html(features):
    return "<ul style=\"padding-left:20px; display:grid; gap:8px;\">" + "".join(
        f"<li>{f}</li>" for f in features
    ) + "</ul>"


def _specs_html(specs, headers=("항목", "사양")):
    rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in specs)
    return f'<table class="compare-table"><tr><th>{headers[0]}</th><th>{headers[1]}</th></tr>{rows}</table>'


def _overview_html(paragraphs):
    return "".join(f"<p>{p}</p>" for p in paragraphs)


def _advantages_html(advantages):
    cards = "".join(
        f'<div class="sub-card"><h3>{title}</h3><p>{desc}</p></div>' for title, desc in advantages
    )
    return f"""
      <h2 style="font-size:20px; margin-top:36px;">Cold Jet&reg;만의 강점</h2>
      <div class="sub-grid" style="margin-top:14px;">{cards}</div>
"""


def _cross_links_html(cross_links, depth_group_prefix=".."):
    if not cross_links:
        return ""
    items = cross_links["items"]
    group = cross_links["group"]
    label = cross_links["label"]
    links = " · ".join(
        f'<a href="{depth_group_prefix}/{group}/{slug}.html"><b>{name}</b></a>' if slug else f"<b>{name}</b>"
        for name, slug in items
    )
    return f"""
      <div class="placeholder-note" style="border-style:solid; background:var(--mint); border-color:var(--mint-line); color:var(--text-dark);">
        {label}: {links}
      </div>
"""


def _quicknav(has_accessories):
    items = [("#features", "Features"), ("#specs", "Specifications")]
    if has_accessories:
        items.append(("#accessories", "Accessories"))
    chips = "".join(f'<a class="chip" href="{href}">{label}</a>' for href, label in items)
    return f'<div class="chip-grid" style="margin:20px 0 8px;">{chips}</div>'


def build_group_index(root, code, group_slug, group_title, group_tagline, models,
                       categories, nav_html, footer_html, page_shell, asset, intro_html="",
                       hero_html=None, cover_class="", extra_head=""):
    depth = 2
    group_dir = os.path.join(root, code, group_slug)
    os.makedirs(group_dir, exist_ok=True)

    if categories:
        sections = ""
        for cat_key, cat_title, cat_desc in categories:
            cat_models = [m for m in models if m["category"] == cat_key]
            cards = "".join(f"""
        <div class="sub-card">
          <div class="img-ph" style="min-height:120px; margin-bottom:14px;">[제품 이미지]</div>
          <h3>{m['name']}</h3>
          <p>{m['tagline']}</p>
          <a class="more" href="{m['slug']}.html">모델 상세 보기 →</a>
        </div>""" for m in cat_models)
            sections += f"""
      <h2 style="font-size:20px; margin-top:36px; color:var(--blue-dark);">{cat_title}</h2>
      <p style="color:var(--text-muted); font-size:14px; margin-bottom:16px;">{cat_desc}</p>
      <div class="sub-grid">{cards}</div>
"""
    else:
        cards = "".join(f"""
        <div class="sub-card">
          <div class="img-ph" style="min-height:120px; margin-bottom:14px;">[제품 이미지]</div>
          <h3>{m['name']}</h3>
          <p>{m['tagline']}</p>
          <a class="more" href="{m['slug']}.html">모델 상세 보기 →</a>
        </div>""" for m in models)
        sections = f'<div class="sub-grid" style="margin-top:20px;">{cards}</div>'

    if hero_html is None:
        hero_html = f"""  <div class="wrap breadcrumb"><a href="{asset('index.html', depth)}">홈</a> &gt;
    <a href="{asset('products/index.html', depth)}">제품 · 자동화 · 공급</a> &gt; {group_title}</div>
  <section class="page-hero" style="padding-top:24px;">
    <div class="wrap">
      <span class="cat">제품</span>
      <h1>{group_title}</h1>
      <p>{group_tagline}</p>
    </div>
  </section>"""

    cover_attr = f' class="{cover_class}"' if cover_class else ""
    body = f"""
{hero_html}
  <section{cover_attr}>
    <div class="wrap">
      {intro_html}
      {sections}
      <div class="cta-band" style="margin-top:36px;">
        <div>
          <h3>어떤 모델이 맞을지 모르겠다면</h3>
          <p>현장 조건을 알려주시면 담당자가 적합한 모델을 추천해 드립니다.</p>
        </div>
        <a class="cta-btn" href="{asset('products/quote.html', depth)}">견적문의 하기</a>
      </div>
    </div>
  </section>
"""
    html = page_shell(group_title, group_tagline, depth, code, body, extra_head=extra_head)
    with open(os.path.join(group_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def build_model_page(root, code, group_slug, group_title, model, siblings,
                      nav_html, footer_html, page_shell, asset):
    depth = 2
    group_dir = os.path.join(root, code, group_slug)
    os.makedirs(group_dir, exist_ok=True)

    # (2026-10-14, §55) 핸드오프 HTML 본문을 통째로 쓰는 커스텀 상세 페이지
    if model.get("custom_body"):
        html = page_shell(model["custom_title"], model["custom_desc"], depth, code, model["custom_body"],
                          extra_script=model.get("custom_script", ""))
        with open(os.path.join(group_dir, f"{model['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        return

    overview_block = ""
    if model.get("overview"):
        overview_block = f"""
      {_overview_html(model['overview'])}
"""

    advantages_block = _advantages_html(model["advantages"]) if model.get("advantages") else ""

    accessories_block = ""
    if model.get("accessories"):
        accessories_block = f"""
      <h2 id="accessories" style="font-size:20px; margin-top:36px; scroll-margin-top:90px;">Accessories</h2>
      {ACCESSORIES_HTML}
"""

    cross_links_block = _cross_links_html(model.get("cross_links"))

    other_cards = "".join(f"""
        <div class="sub-card">
          <h3>{s['name']}</h3>
          <p>{s['tagline']}</p>
          <a class="more" href="{s['slug']}.html">모델 상세 보기 →</a>
        </div>""" for s in siblings if s["slug"] != model["slug"])

    maintenance_block = f"""
      <div class="placeholder-note" style="margin-top:20px;">
        정기 점검이 필요하신가요? 예방정비 플랜 안내와 정식 스펙시트 · 카탈로그 자료 요청은
        <a href="{asset('products/quote.html', depth)}">견적문의</a>를 통해 접수해 드립니다.
      </div>
"""

    body = f"""
  <div class="wrap breadcrumb"><a href="{asset('index.html', depth)}">홈</a> &gt;
    <a href="{asset('products/index.html', depth)}">제품 · 자동화 · 공급</a> &gt;
    <a href="index.html">{group_title}</a> &gt; {model.get('page_breadcrumb', model['name'])}</div>
  <section class="page-hero" style="padding-top:24px;">
    <div class="wrap">
      <span class="cat">제품</span>
      <h1>{model.get('page_title', model['name'])}</h1>
      <p>{model.get('page_tagline', model['tagline'])}</p>
      {_quicknav(model.get('accessories', False))}
    </div>
  </section>
  <section>
    <div class="wrap">
      <div style="display:grid; grid-template-columns:2fr 1fr 1fr; gap:12px; margin-bottom:28px;">
        <div class="img-ph" style="min-height:240px;">[제품 대표 이미지]</div>
        <div class="img-ph" style="min-height:240px;">[제품 상세 이미지 1]</div>
        <div class="img-ph" style="min-height:240px;">[제품 상세 이미지 2]</div>
      </div>

      {overview_block}
      {advantages_block}

      <h2 id="features" style="font-size:20px; margin-top:36px; scroll-margin-top:90px;">Features</h2>
      {_features_html(model['features'])}

      <h2 id="specs" style="font-size:20px; margin-top:36px; scroll-margin-top:90px;">Specifications</h2>
      {_specs_html(model['specs'], model.get('specs_headers', ("항목", "사양")))}
      {cross_links_block}
      {accessories_block}
      {maintenance_block}

      <h2 style="font-size:20px; margin-top:36px;">같은 카테고리의 다른 모델</h2>
      <div class="sub-grid">{other_cards}</div>

      <div class="cta-band" style="margin-top:12px;">
        <div>
          <h3>{model['name']} 도입을 검토 중이신가요?</h3>
          <p>현장 조건에 맞는 정확한 견적을 안내해 드립니다.</p>
        </div>
        <a class="cta-btn" href="{asset('products/quote.html', depth)}">견적문의 하기</a>
      </div>
    </div>
  </section>
"""
    html = page_shell(f"{model['name']} | {group_title}", model["tagline"], depth, code, body)
    with open(os.path.join(group_dir, f"{model['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)


# (2026-09-09, 15차 핸드오프 — 블라스터 페이지 신규 제작) products/blaster/index.html
# 을 build_group_index()의 자동 생성 템플릿 대신 완전히 새로 디자인한 14섹션
# 커스텀 페이지로 교체한다. Hero 영상 → Application → 4 Systems → Particle
# Control → Cold Jet Difference → Product Lineup(탭 필터) → Find the Right
# System(매트릭스) → Proven in the Field(국내 고객사 로고 20+) → Cold Jet+VATEK
# → Test Before You Buy → What You Need → Automation → Choosing → Final CTA.
# BLASTER_MODELS/BLASTER_CATEGORIES 데이터 구조는 이 커스텀 디자인에 아직
# 맞춰 재설계되지 않았으므로(범위 밖) 이 상수는 그대로 정적 HTML을 보관한다 —
# 개별 모델 상세 페이지(build_model_page)는 기존 데이터 기반 생성 그대로 유지.
BLASTER_PAGE_TITLE = "드라이아이스 세척기 · DRY ICE BLASTERS"
BLASTER_PAGE_DESC = "세척 대상이 다르면 필요한 블라스터도 달라집니다. Smart · Pellet · MicroParticle · Specialty — Cold Jet 드라이아이스 세척기의 차이와 선택 기준, 그리고 바테크의 테스트·지원을 안내합니다."
BLASTER_SCRIPT = """  <script>
  (function(){
    // 이미지: 로드 완료 시 부드럽게 나타남 (JS가 있을 때만 숨김 → 무-JS 환경 안전)
    document.documentElement.classList.add('js-media-fade');
    var imgs=document.querySelectorAll('.bls-sec img, .bls-pcs img, .bls-hero-stage img');
    var mark=function(img){ img.classList.add('is-loaded'); };
    imgs.forEach(function(img){
      if (img.complete && img.naturalWidth>0) { mark(img); return; }
      img.addEventListener('load',function(){ mark(img); },{once:true});
      img.addEventListener('error',function(){ mark(img); },{once:true});
    });
    // 비디오: 뷰포트 근처에서만 다운로드 시작, 재생 가능해지면 페이드 인
    var vids=document.querySelectorAll('video.bls-media-fade');
    var prime=function(v){
      if (v.dataset.primed) return; v.dataset.primed='1';
      if (v.preload==='none') v.preload='auto';
      v.load();
    };
    vids.forEach(function(v){
      var show=function(){ v.classList.add('is-loaded'); };
      if (v.readyState>=3) show();
      v.addEventListener('loadeddata',show,{once:true});
      v.addEventListener('canplay',show,{once:true});
    });
    if ('IntersectionObserver' in window) {
      var vo=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ prime(e.target); vo.unobserve(e.target); } }); },{rootMargin:'600px 0px'});
      vids.forEach(function(v){ vo.observe(v); });
    } else { vids.forEach(prime); }
  })();
  </script>
  <script>
  (function(){
    var v=document.getElementById('blsDetailVideo'),btn=document.getElementById('blsDetailPlayBtn');
    if (v && btn) {
      btn.addEventListener('click',function(){
        if (v.paused) { v.play(); } else { v.pause(); }
      });
      v.addEventListener('play',function(){
        btn.classList.add('is-playing');
        btn.querySelector('.bls-play-label').textContent='일시정지';
        btn.querySelector('.bls-play-icon').textContent='❙❙';
      });
      v.addEventListener('pause',function(){
        btn.classList.remove('is-playing');
        btn.querySelector('.bls-play-label').textContent='영상 재생';
        btn.querySelector('.bls-play-icon').textContent='▶';
      });
    }
    document.querySelectorAll('.bls-prod-bg-btn').forEach(function(btn){
      btn.addEventListener('click',function(e){
        e.preventDefault();
        var media=btn.closest('.bls-prod-media'), img=media.querySelector('img');
        var toBlack=!media.classList.contains('is-black-bg');
        media.classList.toggle('is-black-bg',toBlack);
        img.style.opacity=0;
        setTimeout(function(){
          img.src = toBlack ? img.getAttribute('data-bg-black') : img.getAttribute('data-bg-white');
          img.style.opacity=1;
        },180);
        btn.textContent = toBlack ? '흰색 배경' : '검정 배경';
      });
    });
    [['pcsVideo1','pcsPlayBtn1'],['pcsVideo2','pcsPlayBtn2']].forEach(function(pair){
      var vv=document.getElementById(pair[0]), bb=document.getElementById(pair[1]);
      if (!vv || !bb) return;
      var media=vv.closest('.bls-pcs-demo-media');
      bb.addEventListener('click',function(){ if (vv.paused) { vv.play(); } else { vv.pause(); } });
      vv.addEventListener('play',function(){ bb.classList.add('is-playing'); bb.querySelector('.bls-play-label').textContent='일시정지'; bb.querySelector('.bls-play-icon').textContent='❙❙'; if (media) media.classList.add('is-playing'); });
      vv.addEventListener('pause',function(){ bb.classList.remove('is-playing'); bb.querySelector('.bls-play-label').textContent='영상 재생'; bb.querySelector('.bls-play-icon').textContent='▶'; if (media) media.classList.remove('is-playing'); });
    });
  })();
  </script>
  <script>
  (function(){
    var tabs=document.querySelectorAll('.bls-tabs button'),cards=document.querySelectorAll('#blsProdGrid .bls-prod');
    tabs.forEach(function(b){b.addEventListener('click',function(){
      if (b.classList.contains('is-active')) return;
      tabs.forEach(function(t){t.classList.toggle('is-active',t===b);});
      var f=b.getAttribute('data-filter');
      var toShow=[],toHide=[];
      cards.forEach(function(c){
        var cats=(c.getAttribute('data-cat')||'').split(' ');
        var show=f==='all'||cats.indexOf(f)>-1;
        var wasHidden=c.classList.contains('is-hidden');
        if (show && wasHidden) toShow.push(c);
        else if (!show && !wasHidden) toHide.push(c);
      });
      toHide.forEach(function(c){ c.classList.add('is-filter-out'); });
      setTimeout(function(){
        toHide.forEach(function(c){ c.classList.add('is-hidden'); c.classList.remove('is-filter-out'); });
        toShow.forEach(function(c,i){
          c.classList.remove('is-hidden');
          c.classList.add('is-filter-in');
          void c.offsetWidth;
          setTimeout(function(){ c.classList.remove('is-filter-in'); }, 40 + i*60);
        });
      }, toHide.length ? 260 : 0);
    });});
  })();
  (function(){
    var scaleEl=document.getElementById('blsScale'),fill=document.getElementById('blsScaleFill'),live=document.getElementById('blsScaleLive');
    var dial=document.getElementById('pcsDial'),num=document.getElementById('pcsLiveNum'),knob=document.getElementById('pcKnob'),face=document.getElementById('pcKnobFace'),arc=document.getElementById('pcArc'),ticks=document.getElementById('pcTicks');
    if(!scaleEl||!fill||!live)return;
    var MIN=0.3,MAX=3.0,STEP=0.1,SWEEP=270,ticking=false,touched=false,value=MAX;
    var snap=function(v){return Math.round((v-MIN)/STEP)*STEP+MIN};
    if(ticks){var h='';for(var i=0;i<28;i++){var a=(-135+i*(SWEEP/27))*Math.PI/180,big=(i%9===0),r1=big?108:113,r2=118;h+='<line x1="'+(150+r1*Math.sin(a)).toFixed(1)+'" y1="'+(150-r1*Math.cos(a)).toFixed(1)+'" x2="'+(150+r2*Math.sin(a)).toFixed(1)+'" y2="'+(150-r2*Math.cos(a)).toFixed(1)+'"'+(big?' stroke="#fff" stroke-width="2"':'')+'></line>'}ticks.innerHTML=h}
    function setValue(v){
      v=snap(Math.min(Math.max(v,MIN),MAX));value=v;
      var f=(v-MIN)/(MAX-MIN),deg=-135+f*SWEEP;
      fill.style.width=(f*100)+'%';live.textContent=v.toFixed(1)+' mm';if(num)num.textContent=v.toFixed(1);
      if(dial)dial.style.transform='translate(-50%,-50%) rotate('+deg.toFixed(1)+'deg)';
      if(face)face.style.transform='translate(-50%,-50%) rotate('+deg.toFixed(1)+'deg)';
      if(arc)arc.style.strokeDashoffset=(1-f).toFixed(4);
      if(knob){knob.setAttribute('aria-valuenow',v.toFixed(1));knob.setAttribute('aria-valuetext',v.toFixed(1)+'mm')}
    }
    function onScrollUpdate(){
      ticking=false;if(touched)return;
      var r=scaleEl.getBoundingClientRect(),a=window.innerHeight*0.85,b=window.innerHeight*0.25;
      var p=Math.min(Math.max((a-r.top)/(a-b+r.height),0),1);
      setValue(MAX-p*(MAX-MIN));
    }
    function req(){if(!ticking){ticking=true;requestAnimationFrame(onScrollUpdate)}}
    window.addEventListener('scroll',req,{passive:true});window.addEventListener('resize',req);onScrollUpdate();
    if(knob){
      var turning=false,lastA=0,acc=0;
      var markTouched=function(){touched=true;knob.classList.add('is-touched')};
      var angleOf=function(e){var r=knob.getBoundingClientRect();return Math.atan2(e.clientY-(r.top+r.height/2),e.clientX-(r.left+r.width/2))*180/Math.PI};
      knob.addEventListener('pointerdown',function(e){markTouched();turning=true;knob.classList.add('is-turning');knob.setPointerCapture(e.pointerId);lastA=angleOf(e);acc=(value-MIN)/(MAX-MIN)*SWEEP;e.preventDefault()});
      knob.addEventListener('pointermove',function(e){
        if(!turning)return;var a=angleOf(e),d=a-lastA;if(d>180)d-=360;if(d<-180)d+=360;lastA=a;
        acc=Math.min(Math.max(acc+d,0),SWEEP);setValue(MIN+acc/SWEEP*(MAX-MIN));
      });
      var stop=function(e){if(!turning)return;turning=false;knob.classList.remove('is-turning');try{knob.releasePointerCapture(e.pointerId)}catch(x){}};
      knob.addEventListener('pointerup',stop);knob.addEventListener('pointercancel',stop);
      knob.addEventListener('wheel',function(e){markTouched();setValue(value+(e.deltaY<0?STEP:-STEP));e.preventDefault()},{passive:false});
      knob.addEventListener('keydown',function(e){var k=e.key;if(k==='ArrowRight'||k==='ArrowUp'){markTouched();setValue(value+STEP);e.preventDefault()}else if(k==='ArrowLeft'||k==='ArrowDown'){markTouched();setValue(value-STEP);e.preventDefault()}});
    }
  })();
    </script>

"""
BLASTER_HUB_BODY = """
  <!-- ============ 01 HERO ============ -->
  <section class="subhero-parallax bls-hero-stage">
    <div class="subhero-breadcrumb wrap"><a href="../../index.html">홈</a> &gt; <a href="../index.html">제품 · 자동화 · 공급</a> &gt; 드라이아이스 세척기</div>
    <div class="hero-fit">
      <video class="subhero-parallax-img bls-hero-video" autoplay muted loop playsinline preload="auto" poster="../../assets/img/blaster-hero-poster.webp" aria-label="Cold Jet Aero2 PCS ULTRA · PLT ULTRA 블라스터" data-buffer="0" data-pan-scale="1">
        <source src="../../assets/video/blaster-hero-banner.mp4" type="video/mp4" />
      </video>
      <div class="subhero-textbox bls-hero-box">
        <span class="ind-hero-eyebrow">COLD JET × VATEK&nbsp;&nbsp;/&nbsp;&nbsp;DRY ICE BLASTERS</span>
        <h1>정밀한 세척은<br>블라스터의 <span class="bls-hero-accent">기술에서 시작됩니다.</span></h1>
        <p class="bls-hero-main">입자 제어부터 안정적인 공급과 분사까지.<br>Cold Jet의 핵심 기술에<br>바테크의 국내 현장 지원을 더합니다.</p>
      </div>
      <div class="bls-hero-mask" aria-hidden="true"></div>
    </div>
  </section>

  <!-- ============ 02 SEE IT IN ACTION ============ -->
  <section class="bls-sec bls-cover" id="bls-start">
    <div class="wrap">
      <div class="bls-head is-row reveal">
        <div>
          <span class="bls-dot-eyebrow">BUILT WITH PRECISION</span>
          <h2 class="cmp-h2">가까이서 확인하는<br>Cold Jet의 설계와 완성도.</h2>
        </div>
        <p class="bls-sub is-side">Cold Jet 블라스터의 구조와 마감을<br>제품 영상으로 자세히 확인해보세요.</p>
      </div>
      <div class="bls-showcase-frame reveal">
      <div class="bls-showcase">
        <div class="bls-showcase-media">
          <video id="blsDetailVideo" class="bls-media-fade" muted loop playsinline preload="metadata" poster="../../assets/img/blaster-detail-poster.webp">
            <source src="../../assets/video/blaster-hero.mp4" type="video/mp4" />
          </video>
          <span class="bls-showcase-cap">COLD JET&nbsp;&nbsp;/&nbsp;&nbsp;PRODUCT DETAILS</span>
          <button type="button" class="bls-play-btn" id="blsDetailPlayBtn" aria-label="영상 재생">
            <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
          </button>
        </div>
        <div class="bls-showcase-body">
          <span class="bls-dot-eyebrow">A CLOSER LOOK</span>
          <h3>가까이 볼수록,<br>드러나는 디테일.</h3>
          <p>장비의 전체 구성부터 각 부분의 마감까지, 짧은 제품 영상으로 Cold Jet 블라스터를 자세히 확인해보세요.</p>
          <p>이어지는 섹션에서는 실제 세척 성능을 좌우하는 입자 제어 · 공급 · 분사 기술을 살펴볼 수 있습니다.</p>
          <a class="bls-textlink" href="#bls-systems">내부 기술 살펴보기 ↓</a>
        </div>
      </div>
      </div>
    </div>
  </section>

  <!-- ============ 03 PARTICLE CONTROL ============ -->
  <section class="cmp-dark bls-pcs" id="bls-pcs">
    <div class="wrap">
      <div class="bls-pcs-head reveal">
        <span class="cmp-eyebrow">PARTICLE CONTROL</span>
        <h2 class="cmp-h2" style="line-height:61.2px; font-size:48px">섬세한 세척부터 강한 세척까지,<br /></h2>
        <div class="cmp-dark-body">
          <div><h2 class="cmp-h2" style="line-height:61.2px; font-size:31px; margin-top:0px">입자 크기로 작업 조건을 맞춥니다.</h2></div>
        </div>
      </div>
      <div class="bls-scale-row">
      <div class="bls-pcs-left">
      <div class="bls-scale reveal" id="blsScale">
        <div class="bls-scale-ends"><span>PRECISION</span><span>PERFORMANCE</span></div>
        <div class="bls-scale-bar">
          <b>0.3 mm</b>
          <div class="bls-scale-line">
            <div class="bls-scale-fill" id="blsScaleFill"></div>
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <b id="blsScaleLive">3.0 mm</b>
        </div>
        <div class="bls-scale-ends is-sub"><span>Micro Particle</span><span>Full Pellet</span></div>
      </div>
      <div class="bls-pcs-demos reveal">
        <div class="bls-pcs-demo">
          <div class="bls-pcs-demo-media">
            <video id="pcsVideo1" class="bls-media-fade" muted loop playsinline preload="none">
              <source src="../../assets/video/pcs-demo-namecard.mp4" type="video/mp4" />
            </video>
            <div class="bls-pcs-demo-overlay">Micro Particle<br />0.3mm</div>
            <button type="button" class="bls-play-btn is-small" id="pcsPlayBtn1" aria-label="영상 재생">
              <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
            </button>
          </div>
        </div>
        <div class="bls-pcs-demo">
          <div class="bls-pcs-demo-media">
            <video id="pcsVideo2" class="bls-media-fade" muted loop playsinline preload="none">
              <source src="../../assets/video/pcs-demo-asphalt.mp4" type="video/mp4" />
            </video>
            <div class="bls-pcs-demo-overlay">Full Pellet<br />3.0mm</div>
            <button type="button" class="bls-play-btn is-small" id="pcsPlayBtn2" aria-label="영상 재생">
              <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
            </button>
          </div>
        </div>
      </div>
      <div class="cmp-dark-body bls-pcs-desc" style="margin-top:clamp(18px,2vw,28px); font-size:16.5px; line-height:1.85;">
          <p>Cold Jet의 특허 PCS®는 3 mm 드라이아이스 펠렛을 투입해 0.3~3.0 mm 범위에서 0.1 mm 단위, 총 28개의 입자 크기를 선택할 수 있습니다.</p>
          <p style="margin-bottom:0">민감한 표면에는 작은 입자와 낮은 압력을, 고착된 오염에는 큰 입자와 높은 압력을 적용해 작업에 맞는 세척 조건을 설정할 수 있습니다.</p>
      </div>
      </div>
      <div class="bls-pcs-panel reveal">
        <div class="bls-pcs-panel-frame">
          <img class="bls-pcs-panel-img" src="../../assets/img/pcs-panel-frame.webp" alt="Cold Jet PCS 컨트롤 디스플레이" />
          <span class="bls-pcs-panel-num" id="pcsLiveNum">3.0</span>
          <img class="bls-pcs-panel-dial" id="pcsDial" src="../../assets/img/pcs-dial-knob.webp" alt="PCS 조절 다이얼" />
        </div>
        <div class="au-pc-zoom">
          <svg class="au-pc-leader" viewBox="0 0 100 60" preserveAspectRatio="none" aria-hidden="true"><path d="M50,0 L50,60" stroke="rgba(255,255,255,.35)" stroke-width="1" stroke-dasharray="3 4" fill="none"></path></svg>
          <div class="au-pc-knob" id="pcKnob" role="slider" tabindex="0" aria-label="입자 크기 다이얼" aria-valuemin="0.3" aria-valuemax="3.0" aria-valuenow="3.0" aria-valuetext="3.0mm">
            <svg class="au-pc-ring" viewBox="0 0 300 300" aria-hidden="true">
              <defs><linearGradient id="pcArcGrad" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#4fadb8"></stop><stop offset="100%" stop-color="#9fe3ea"></stop></linearGradient></defs>
              <path d="M 62.9 237.1 A 125 125 0 1 1 237.1 237.1" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="8" stroke-linecap="round"></path>
              <path id="pcArc" d="M 62.9 237.1 A 125 125 0 1 1 237.1 237.1" fill="none" stroke="url(#pcArcGrad)" stroke-width="8" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="0"></path>
              <g id="pcTicks" stroke="rgba(255,255,255,.55)" stroke-width="1.5"></g>
            </svg>
            <div class="au-pc-knob-face" id="pcKnobFace"><img src="../../assets/img/pcs-dial-knob.webp" alt="" draggable="false" /><i class="au-pc-knob-mark"></i></div>
            <span class="au-pc-knob-min">0.3</span><span class="au-pc-knob-max">3.0</span>
            <span class="au-pc-knob-hint is-l">↺ 작게</span><span class="au-pc-knob-hint is-r">크게 ↻</span>
            <div class="au-pc-guide" aria-hidden="true">
              <div class="au-pc-orbit"><svg class="au-pc-hand" viewBox="0 0 24 24"><path d="M9 11.5V5.2a1.7 1.7 0 0 1 3.4 0V11m0-3.4a1.7 1.7 0 0 1 3.4 0v3.9m0-2.5a1.7 1.7 0 0 1 3.4 0v6.3c0 3.3-2.5 5.7-5.8 5.7h-1.2c-1.9 0-3.4-.7-4.5-2L4.3 15a1.6 1.6 0 0 1 2.4-2.1L9 15.3" fill="#fff" stroke="#1b2426" stroke-width="1.3" stroke-linejoin="round" stroke-linecap="round"/></svg></div>
              <span class="au-pc-guide-label">잡고 돌려보세요</span>
            </div>
          </div>
        </div>
        <span class="bls-pcs-panel-cap" style="color:#ffffff; opacity:1; font-size:15px; max-width:460px; margin-left:auto; margin-right:auto; line-height:1.6; word-break:keep-all">다이얼을 잡고 돌려보세요 — 시계방향으로 돌리면 입자가 커지고, 반시계방향으로 돌리면 작아집니다. (휠 · 방향키도 가능)</span>
      </div>
      </div>
      <p class="cmp-dark-final bls-dark-final">작업에 맞는 세척 조건을 찾는 것이<br><em>장비 선택의 출발점</em>입니다.</p>
    </div>
  </section>

  <!-- ============ 04 DRY ICE BLASTER SYSTEMS ============ -->
  <section class="bls-sec bls-sys-sec tint-hatch" id="bls-systems">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">DRY ICE BLASTER SYSTEMS</span>
        <h2 class="cmp-h2">작업 목적에 따라 선택하는<br>Cold Jet 블라스터</h2>
        <p class="bls-sub">Cold Jet 블라스터는 사용하는 드라이아이스 입자, 제어 방식, 필요한 세척 강도와 작업 조건에 따라 여러 제품군으로 나뉩되어 있습니다.</p>
      </div>
      <div class="bls-sys-grid">
        <article class="bls-sys reveal is-large-media" id="bls-sys-smart">
          <div class="bls-sys-media">
            <img class="is-main" src="../../assets/img/blaster-smart-lineup.webp" alt="Cold Jet Aero2 PCS ULTRA · PLT ULTRA · i3 MicroClean" loading="lazy" decoding="async" />
          </div>
          <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">01</span>
            <span class="bls-en">SMART BLASTER</span>
            <h3 style="color: #000000">스마트형 블라스터</h3>
            <p class="bls-sys-head">세척 조건을 정밀하게 설정하고,<br>같은 조건을 반복해서 사용해야 하는 작업에.</p>
            <p>Smart 계열은 주요 세척 조건을 디지털 방식으로 설정하고 작업에 맞게 세밀하게 조정할 수 있는 제품군입니다.</p>
            <p>특허받은 PCS® 기술이 적용된 모델은 3 mm 펠렛을 투입해 0.3~3.0 mm 범위에서 0.1 mm 단위, 총 28개의 입자 크기를 선택할 수 있습니다.</p>
            <p>이를 통해 민감한 표면의 정밀 세척부터 고착 오염 제거까지 작업에 맞게 조건을 세밀하게 설정할 수 있습니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="aero2-ultra.html">Aero2 PCS ULTRA</a><span class="bls-badge">PARTICLE CONTROL SYSTEM</span><a class="bls-model-chip" href="aero2-ultra.html">Aero2 PLT ULTRA</a></dd></div>
              <div><dt>PCS ULTRA</dt><dd>0.3 – 3.0 mm · 28 Particle Sizes</dd></div>
            </dl>
            <a class="bls-more" href="aero2-ultra.html">Smart Blaster 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-iot.webp" alt="IoT" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
        <article class="bls-sys reveal is-large-media" id="bls-sys-pellet" style="--reveal-delay:0.06s">
          <div class="bls-sys-media">
            <img class="is-main" src="../../assets/img/blaster-pellet-lineup.webp" alt="Cold Jet Aero Series · ELITE 20 · IceRocket PLT" loading="lazy" decoding="async" />
          </div>
            <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">02</span>
            <span class="bls-en">PELLET BLASTER</span>
            <h3 style="color: #000000">펠렛형 블라스터</h3>
            <p class="bls-sys-head">일반 산업 세척과<br>고착 오염 제거처럼 높은 세척력이 필요한 작업에.</p>
            <p>3 mm 드라이아이스 펠렛을 사용하는 산업용 블라스터 제품군입니다.</p>
            <p>생산설비와 금형의 세척, 오일 · 그리스 · 카본 및 고착된 공정 잔류물 제거 등 상대적으로 높은 세척력이 필요한 작업에 폭넓게 사용됩니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="aero-series.html">Aero Series</a><a class="bls-model-chip" href="elite20-icerocket.html">ELITE 20</a><a class="bls-model-chip" href="elite20-icerocket.html">IceRocket PLT</a></dd></div>
              <div><dt>사용 입자</dt><dd>3 mm PELLET</dd></div>
            </dl>
            <a class="bls-more" href="aero-series.html">Pellet Blaster 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-pellet.webp" alt="3mm Pellet" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
        <article class="bls-sys reveal is-large-media" id="bls-sys-micro">
          <div class="bls-sys-media">
            <img class="is-main" src="../../assets/img/blaster-micro-lineup.webp" alt="Cold Jet i3 MicroClean · i3 MicroClean 2 · SDI Select 60" loading="lazy" decoding="async" />
          </div>
          <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">03</span>
            <span class="bls-en">MICRO PARTICLE BLASTER</span>
            <h3 style="color: #000000">마이크로파티클 블라스터</h3>
            <p class="bls-sys-head">민감한 표면과 정밀 작업에<br>작은 입자로 세밀하게 대응합니다.</p>
            <p>MicroParticle 블라스터는 3 mm 펠렛보다 작은 입자를 사용해 표면에 가해지는 충격을 줄이면서 세밀하게 세척하는 제품군입니다.</p>
            <p>정밀 금형, 전자 · 정밀 부품, 부품 후처리, 민감한 표면과 복원 작업처럼 표면 상태를 세심하게 관리해야 하는 작업에 적합합니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="i3-microclean-2.html">i³ MicroClean 2</a><span class="bls-badge">SMART MICRO PARTICLE</span><a class="bls-model-chip" href="i3-microclean.html">i³ MicroClean</a><a class="bls-model-chip" href="sdi-select-60.html">SDI Select 60</a></dd></div>
              <div><dt>사용 입자</dt><dd>MICRO PARTICLE — 드라이아이스를 미세 입자로 가공해 분사</dd></div>
            </dl>
            <a class="bls-more" href="i3-microclean-2.html">MicroParticle Blaster 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-micro.webp" alt="Micro Particle" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
        <article class="bls-sys reveal is-large-media" id="bls-sys-specialty" style="--reveal-delay:0.06s">
          <div class="bls-sys-media is-contain">
            <img class="is-main" src="../../assets/img/blaster-specialty-lineup.webp" alt="Cold Jet C100 · E-CO2 150" loading="lazy" style="position: absolute; left: 21px; top: 21px; width: 662px; height: 461px" />
          </div>
          <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">04</span>
            <span class="bls-en">SPECIALTY BLASTER</span>
            <h3 style="color: #000000">특수형 블라스터</h3>
            <p class="bls-sys-head">일반 블라스터와 다른 조건이 필요한<br>특수 작업에.</p>
            <p>전원 사용이 제한되는 현장이나 연마재를 함께 사용하는 표면처리처럼 일반적인 드라이아이스 세척과 다른 조건에는 특수형 시스템을 검토할 수 있습니다.</p>
            <p>E-CO2 150은 호환 Cold Jet 블라스터(PLT 60 · Aero 80 · C100)에 가압식 연마재 포트를 결합해 드라이아이스와 연마재를 함께 분사하는 시스템입니다. 도막 · 코팅 · 부식 제거와 같은 표면처리 작업에 사용됩니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="c100.html">C100 — 완전 공압식</a><a class="bls-model-chip" href="e-co2-150.html">E-CO2 150 — 드라이아이스 + 연마재</a></dd></div>
            </dl>
            <a class="bls-more" href="c100.html">Specialty System 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-specialty.webp" alt="Specialty" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- ============ 05 PRODUCT LINEUP ============ -->
  <section class="bls-sec bls-lineup-sec tint-hatch" id="bls-lineup">
    <div class="wrap">
      <div class="bls-head is-row reveal">
        <div>
          <span class="cmp-eyebrow">PRODUCT LINEUP</span>
          <h2 class="cmp-h2">Cold Jet 블라스터 라인업</h2>
          <p class="bls-sub">작업 목적과 필요한 세척 조건에 따라 적합한 제품을 비교해보세요.</p>
        </div>
        <div class="bls-tabs" role="tablist" aria-label="제품군 필터">
          <button data-filter="core" type="button"><b>CORE</b><small>핵심 모델</small></button>
          <button class="is-active" data-filter="all" type="button"><b>ALL</b><small>전체 모델</small></button>
          <button data-filter="smart" type="button"><b>SMART</b><small>정밀 제어 · 자동화</small></button>
          <button data-filter="pellet" type="button"><b>PELLET</b><small>산업 설비 · 고착 오염</small></button>
          <button data-filter="micro" type="button"><b>MICRO PARTICLE</b><small>정밀 · 민감 표면</small></button>
          <button data-filter="specialty" type="button"><b>SPECIALTY</b><small>특수 작업</small></button>
        </div>
      </div>
      <div class="bls-prod-grid" id="blsProdGrid">
      <a class="bls-prod reveal" data-cat="core smart pellet micro" href="aero2-ultra.html" style="--reveal-delay:0s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero2-pcs-ultra-white.webp" data-bg-black="../../assets/img/blaster-aero2-pcs-ultra.webp" data-bg-white="../../assets/img/blaster-aero2-pcs-ultra-white.webp" alt="Aero2® PCS ULTRA" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SMART</span><span class="bls-prod-cat">PELLET</span><span class="bls-prod-cat">MICRO PARTICLE</span><span class="bls-badge">PARTICLE CONTROL SYSTEM</span></div>
          <h3>Aero2® PCS ULTRA</h3>
          <p class="bls-prod-pos">입자 크기까지 정밀하게 제어하는 스마트 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>정밀 금형 · 민감한 표면 · 고착 오염 · 생산설비 · 로봇 · 자동화 라인</dd></div>
            <div><dt>핵심 기술</dt><dd>PCS® 0.3–3.0 mm · 28단계 · 프로그램 레시피 · 7" HMI · Cold Jet CONNECT®</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="smart pellet" href="aero2-plt-ultra.html" style="--reveal-delay:0.06s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero2-plt-ultra-white.webp" data-bg-black="../../assets/img/blaster-aero2-plt-ultra.webp" data-bg-white="../../assets/img/blaster-aero2-plt-ultra-white.webp" alt="Aero2® PLT ULTRA" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SMART</span><span class="bls-prod-cat">PELLET</span></div>
          <h3>Aero2® PLT ULTRA</h3>
          <p class="bls-prod-pos">3 mm 펠렛 세척 조건을 디지털로 설정 · 저장하는 스마트 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>생산설비 · 금형 · 반복 세척 공정 · 자동화 연계</dd></div>
            <div><dt>핵심 기술</dt><dd>SureFlow 피더 시스템 · 프로그램 레시피 · HMI · Cold Jet CONNECT®</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="core micro smart" href="i3-microclean-2.html" style="--reveal-delay:0.12s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-i3-microclean-2-white.webp" data-bg-black="../../assets/img/blaster-i3-microclean-2.png" data-bg-white="../../assets/img/blaster-i3-microclean-2-white.webp" alt="i³ MicroClean® 2" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SMART</span><span class="bls-prod-cat">MICRO PARTICLE</span><span class="bls-badge">SMART MICRO PARTICLE</span></div>
          <h3>i³ MicroClean® 2</h3>
          <p class="bls-prod-pos">디지털 제어와 IoT를 지원하는 차세대 마이크로파티클 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>정밀 금형 · 전자부품 · 부품 마무리 · 민감한 표면</dd></div>
            <div><dt>핵심 기술</dt><dd>블록 · 펠렛 모두 사용 · 최소 0.3 m³/min · 1.4–10 bar · 7" LCD · 레시피 · CONNECT®</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="pellet" href="aero-series.html" style="--reveal-delay:0.18s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero-40fp-white.webp" data-bg-black="../../assets/img/blaster-aero-40fp.png" data-bg-white="../../assets/img/blaster-aero-40fp-white.webp" alt="Aero® 40FP" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span></div>
          <h3>Aero® 40FP</h3>
          <p class="bls-prod-pos">40 lb 호퍼를 갖춘 산업용 풀프레셔 펠렛 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>생산설비 유지보수 · 오일 · 그리스 · 고착 잔류물 · 이동이 잦은 현장</dd></div>
            <div><dt>핵심 기술</dt><dd>SureFlow 시스템 · 래디얼 피더 · 정밀 공급량 제어 · 내장 압력 조절기</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="pellet" href="aero-series.html" style="--reveal-delay:0.24s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero-80fp-white.webp" data-bg-black="../../assets/img/blaster-aero-80fp.webp" data-bg-white="../../assets/img/blaster-aero-80fp-white.webp" alt="Aero® 80FP" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span></div>
          <h3>Aero® 80FP</h3>
          <p class="bls-prod-pos">80 lb 호퍼를 갖춘 대용량 산업용 풀프레셔 펠렛 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>생산설비 유지보수 · 오일 · 그리스 · 고착 잔류물 · 주조 · 코어박스</dd></div>
            <div><dt>핵심 기술</dt><dd>SureFlow 시스템 · 래디얼 피더 · 정밀 공급량 제어 · 내장 압력 조절기</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="core pellet micro" href="elite20-icerocket.html" style="--reveal-delay:0s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-elite-20-white.webp" data-bg-black="../../assets/img/blaster-elite-20.webp" data-bg-white="../../assets/img/blaster-elite-20-white.webp" alt="ELITE 20" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span><span class="bls-prod-cat">MICRO PARTICLE</span></div>
          <h3>ELITE 20</h3>
          <p class="bls-prod-pos">일반 산업 세척에 적합한 실용형 펠렛 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>일반 산업 세척 · 설비 · 부품 · 첫 도입</dd></div>
            <div><dt>핵심 기술</dt><dd>3 mm 펠렛 · 단일호스 방식 · 컴팩트 구성</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="core pellet" href="elite20-icerocket.html" style="--reveal-delay:0.06s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-icerocket-plt-white.webp" data-bg-black="../../assets/img/blaster-icerocket-plt.webp" data-bg-white="../../assets/img/blaster-icerocket-plt-white.webp" alt="IceRocket PLT" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span></div>
          <h3>IceRocket PLT</h3>
          <p class="bls-prod-pos">현장 이동이 편리한 소형 펠렛 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>일반 산업 세척 · 현장 이동 작업 · 첫 도입</dd></div>
            <div><dt>핵심 기술</dt><dd>3 mm 펠렛 · 컴팩트 · 경량 · 단일호스 방식</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="micro" href="i3-microclean.html" style="--reveal-delay:0.12s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-i3-microclean-white.webp" data-bg-black="../../assets/img/blaster-i3-microclean.webp" data-bg-white="../../assets/img/blaster-i3-microclean-white.webp" alt="i³ MicroClean®" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">MICRO PARTICLE</span></div>
          <h3>i³ MicroClean®</h3>
          <p class="bls-prod-pos">드라이아이스를 미세 입자로 가공해 분사하는 컴팩트 정밀 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>정밀 금형 · 전자부품 · 섬세한 표면 · 소규모 작업 공간</dd></div>
            <div><dt>핵심 기술</dt><dd>특허 쉐이빙 마이크로파티클 · 최소 12 cfm · 1.4–9.7 bar · 저소음 · 단일호스</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="micro pellet" href="sdi-select-60.html" style="--reveal-delay:0.18s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-sdi-select-60-white.webp" data-bg-black="../../assets/img/blaster-sdi-select-60.png" data-bg-white="../../assets/img/blaster-sdi-select-60-white.webp" alt="SDI Select™ 60" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">MICRO PARTICLE</span><span class="bls-prod-cat">PELLET</span></div>
          <h3>SDI Select™ 60</h3>
          <p class="bls-prod-pos">드라이아이스를 미세 입자로 가공하거나 3 mm 펠렛으로 전환해 사용할 수 있는 범용 모델</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>현장 조건이 다양한 작업 · 정밀 ~ 일반 세척 · 세척 대행</dd></div>
            <div><dt>핵심 기술</dt><dd>3가지 블라스팅 모드 · 단일호스 방식 · 국내 공급 실적 다수</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="specialty" href="c100.html" style="--reveal-delay:0s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-c100-white.webp" data-bg-black="../../assets/img/blaster-c100.png" data-bg-white="../../assets/img/blaster-c100-white.webp" alt="Cold Jet C100" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SPECIALTY</span></div>
          <h3>Aero® C100</h3>
          <p class="bls-prod-pos">전원 없이 압축공기만으로 작동하는 완전 공압식 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>전원 사용이 제한되는 현장 · 옥외 작업 · 장거리 호스 작업</dd></div>
            <div><dt>핵심 기술</dt><dd>완전 공압식 · SureFlow 시스템 · 100 lb 호퍼 · 최대 100 ft 호스</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="specialty" href="e-co2-150.html" style="--reveal-delay:0.06s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-e-co2-150-white.webp" data-bg-black="../../assets/img/blaster-e-co2-150.webp" data-bg-white="../../assets/img/blaster-e-co2-150-white.webp" alt="E-CO2™ 150" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SPECIALTY</span></div>
          <h3>E-CO2™ 150</h3>
          <p class="bls-prod-pos">드라이아이스와 연마재를 함께 사용하는 도막 · 코팅 · 부식 제거용 시스템</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>도막 · 코팅 제거 · 부식 제거 · 표면 전처리</dd></div>
            <div><dt>핵심 기술</dt><dd>1.5 ft³ 가압식 연마재 포트 · PLT 60 · Aero 80 · C100과 결합 · 드라이아이스 단독 분사 전환</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      </div>
    </div>
  </section>

  <!-- ============ 06 THE COLD JET DIFFERENCE ============ -->
  <section class="bls-sec" id="bls-tech">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">THE COLD JET DIFFERENCE</span>
        <h2 class="cmp-h2">성능과 내구성은,<br>보이지 않는 곳에서 결정됩니다.</h2>
        <p class="bls-sub">드라이아이스 블라스터의 성능은 최대 압력이나 호퍼 용량 같은 숫자만으로 판단하기 어렵습니다. 드라이아이스를 얼마나 안정적으로 공급하는지, 압축공기의 흐름을 얼마나 효율적으로 전달하는지, 노즐에서 원하는 분사 형태를 만드는지에 따라 실제 세척 결과와 작업 효율이 달라집니다. Cold Jet은 드라이아이스 공급부터 분사까지 전체 흐름을 하나의 시스템으로 설계합니다.</p>
      </div>
      <div class="bls-tech-list">
        <article class="bls-tech reveal">
          <div class="bls-tech-media"><img src="../../assets/img/sureflow-feeder-system.png" alt="SureFlow 피더 시스템" loading="lazy" style="object-fit: contain; width: 420px; height: 412px" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">01</span>
            <span class="bls-en">SUREFLOW FEEDER SYSTEM</span>
            <h3>안정적인 드라이아이스 공급</h3>
            <p>특허받은 SureFlow 피더 시스템은 Thumper, Ramrod, 진동 장치와 단열 호퍼를 통합해 호퍼 내부의 드라이아이스를 지속적으로 교반합니다.</p>
            <p>이를 통해 드라이아이스가 피더로 안정적으로 공급되도록 하고, 일정한 분사 흐름을 유지하도록 설계되었습니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal" style="--reveal-delay:0.06s">
          <div class="bls-tech-media is-cad is-lg"><img src="../../assets/img/coldjet-feeder-cad.png" alt="Cold Jet 피더 시스템 구조" loading="lazy" decoding="async" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">02</span>
            <span class="bls-en">FEEDING SYSTEM</span>
            <h3>정밀한 공급 제어로 일정한 분사 흐름</h3>
            <p>피더는 드라이아이스 공급량과 분사 안정성에 직접 영향을 줍니다.</p>
            <p>Cold Jet의 래디얼 피더는 공기역학적 방식으로 드라이아이스를 공급해 패드와 로터의 마모를 줄이고, 공급량을 정밀하게 제어하도록 설계되었습니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal">
          <div class="bls-tech-media is-cad is-lg"><img src="../../assets/img/coldjet-nozzle-family.webp" alt="Cold Jet 노즐 라인업" loading="lazy" style="object-fit: contain; width: 230%; height: 155%" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">03</span>
            <span class="bls-en">NOZZLE TECHNOLOGY</span>
            <h3>작업에 맞는 분사폭과 세척력을 만드는 노즐</h3>
            <p>같은 블라스터라도 노즐의 형상과 크기에 따라 분사폭과 집중도, 공기 소비량과 작업성이 달라집니다.</p>
            <p>Cold Jet은 다양한 작업 조건에 맞춰 선택할 수 있도록 여러 형태의 특허 노즐을 제공합니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal" style="--reveal-delay:0.06s">
          <div class="bls-tech-media is-product is-lg"><img src="../../assets/img/coldjet-connect-dashboard.webp" alt="Cold Jet Connect 대시보드" loading="lazy" decoding="async" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">04</span>
            <span class="bls-en">COLD JET CONNECT®</span>
            <h3>원격 모니터링과 진단 지원</h3>
            <p>Cold Jet CONNECT®를 이용하면 지원 모델의 장비 상태를 PC나 모바일에서 원격으로 확인하고 진단할 수 있습니다.</p>
            <p>교육 영상, 장비 문서, 문제 해결 안내와 서비스 지원 기능도 함께 이용할 수 있습니다.<br /><br />Aero2 ULTRA 시리즈와 i³ MicroClean 2 등 IoT 지원 모델에 적용됩니다.</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- ============ 07 TRUSTED WORLDWIDE ============ -->
  <section class="bls-sec bls-ref-sec tint-hatch" id="bls-ref">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">TRUSTED WORLDWIDE</span>
        <h2 class="cmp-h2">Cold Jet 장비는<br>국내외 다양한 산업 현장에서 사용되고 있습니다.</h2>
      </div>
    </div>
    <div class="bls-ref-row">
      <div class="bls-ref-track">
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-hyundai.png" alt="Hyundai" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kia.png" alt="Kia" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kumho-tire.png" alt="Kumho Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-nexen-tire.png" alt="Nexen Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-airbus_logo.png" alt="Airbus" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-spacex_logo.png" alt="SpaceX" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-coca-cola_logo.png" alt="Coca-Cola" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-nestle_logo.png" alt="Nestle" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-p_and_g_procter_and_gamble_logo.png" alt="P&G" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-caterpillar-logo.png" alt="Caterpillar" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-michelin_logo.png" alt="Michelin" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-goodyear_logo.png" alt="Goodyear" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-hyundai.png" alt="Hyundai" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kia.png" alt="Kia" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kumho-tire.png" alt="Kumho Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-nexen-tire.png" alt="Nexen Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-airbus_logo.png" alt="Airbus" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-spacex_logo.png" alt="SpaceX" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-coca-cola_logo.png" alt="Coca-Cola" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-nestle_logo.png" alt="Nestle" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-p_and_g_procter_and_gamble_logo.png" alt="P&G" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-caterpillar-logo.png" alt="Caterpillar" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-michelin_logo.png" alt="Michelin" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-goodyear_logo.png" alt="Goodyear" loading="lazy" decoding="async" /></div>
      </div>
    </div>
    <div class="bls-ref-row is-reverse">
      <div class="bls-ref-track">
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-bmw.png" alt="BMW" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-toyota.png" alt="Toyota" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-honda.png" alt="Honda" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-ford.png" alt="Ford" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-tesla.png" alt="Tesla" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-power-generation-siemens_energy_logo.png" alt="Siemens Energy" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-mining-rio_tinto_logo.png" alt="Rio Tinto" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-ball_corporation_logo.png" alt="Ball Corporation" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-smurfit_kappa_logo.png" alt="Smurfit Kappa" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rail-sncf-logo.png" alt="SNCF" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-stryker_corporation_logo.png" alt="Stryker" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-becton-dickinson-logo.png" alt="Becton Dickinson" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-bmw.png" alt="BMW" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-toyota.png" alt="Toyota" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-honda.png" alt="Honda" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-ford.png" alt="Ford" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-tesla.png" alt="Tesla" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-power-generation-siemens_energy_logo.png" alt="Siemens Energy" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-mining-rio_tinto_logo.png" alt="Rio Tinto" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-ball_corporation_logo.png" alt="Ball Corporation" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-smurfit_kappa_logo.png" alt="Smurfit Kappa" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rail-sncf-logo.png" alt="SNCF" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-stryker_corporation_logo.png" alt="Stryker" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-becton-dickinson-logo.png" alt="Becton Dickinson" loading="lazy" decoding="async" /></div>
      </div>
    </div>
  </section>



  <!-- ============ 10 GLOBAL TECHNOLOGY · LOCAL SUPPORT ============ -->
  <section class="bls-sec bls-partner" id="bls-partner">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">GLOBAL TECHNOLOGY · LOCAL SUPPORT</span>
        <h2 class="cmp-h2">장비만큼 중요한 것은,<br>한국에서의 기술 지원입니다.</h2>
      </div>
      <div class="bls-partner-grid">
        <img class="bls-partner-logo reveal" src="../../assets/img/coldjet-logo.png" alt="Cold Jet" />
        <img class="bls-partner-logo reveal" src="../../assets/img/vatek-logo-wordmark.png" alt="VATEK" />

        <div class="bls-partner-name reveal">Cold Jet LLC<span class="bls-partner-tagline">드라이아이스 블라스팅 기술의 개척자이자 글로벌 리더</span></div>
        <div class="bls-partner-name reveal">VATEK Corporation<span class="bls-partner-tagline">Cold Jet 대한민국 공식 총판</span></div>

        <div class="bls-partner-media reveal"><img src="../../assets/img/coldjet-hq-photo-1.jpg" alt="Cold Jet 본사" loading="lazy" decoding="async" /></div>
        <div class="bls-partner-media reveal"><img src="../../assets/img/vatek-building.jpg" alt="바테크 사옥" loading="lazy" decoding="async" /></div>

        <div class="bls-partner-desc reveal"><p>Cold Jet은 현대식 드라이아이스 블라스팅 장비의 원천 특허를 보유한 기술 기업으로, 블라스터 · 드라이아이스 생산설비 · 노즐 · 자동화 솔루션을 개발하고 공급하고 있습니다.</p></div>
        <div class="bls-partner-desc reveal">
          <p>1988년 설립한 바테크는 Cold Jet의 대한민국 공식 총판으로, 제품 공급뿐 아니라 세척 테스트, 렌탈 · 데모, 장비 선정, 설치, 기술지원과 A/S까지 국내 고객의 도입과 운용을 지원합니다.</p>
          <p>바테크는 Cold Jet의 교육, 세미나 및 글로벌 컨퍼런스에 지속적으로 참여해 최신 기술과 적용 사례를 국내 고객 지원에 반영하고 있습니다.</p>
        </div>

        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/coldjet-hq-building.webp" alt="Cold Jet 글로벌 본사" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-2.jpg" alt="Cold Jet 생산 공장" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-3.jpg" alt="Cold Jet 라운지" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-4.jpg" alt="Cold Jet 사내 카페" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-5.webp" alt="Cold Jet 컨퍼런스" loading="lazy" decoding="async" />
        </div>
        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/vatek-coldjet-photo-1.jpg" alt="Cold Jet 본사 방문" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-2.jpg" alt="Cold Jet Asia Dealer Conference" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-3.jpg" alt="Cold Jet 글로벌 딜러 컨퍼런스" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-4.jpg" alt="Cold Jet 세미나 참석" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-5.jpg" alt="Cold Jet R&D 신제품 개발" loading="lazy" decoding="async" />
        </div>

        <div class="bls-partner-divider"></div>
        <div class="bls-partner-divider"></div>

        <ul class="bls-facts">
          <li><b>1986</b><small>현대식 드라이아이스 블라스팅 원천 특허</small></li>
          <li><b>250+</b><small>글로벌 특허</small></li>
          <li><b>3 · 3</b><small>R&amp;D 연구소 · 생산공장</small></li>
          <li><b>14</b><small>기술센터</small></li>
        </ul>
        <ul class="bls-facts is-vatek">
          <li><b>1988</b><small>설립 · 제조업 기반</small></li>
          <li><b>2014</b><small>기업부설연구소 설립 (하남)</small></li>
          <li><b>TEST</b><small>시편 · 내방 · 방문 테스트</small></li>
          <li><b>A/S</b><small>설치 · 교육 · 기술지원</small></li>
        </ul>
      </div>
      <p class="bls-quote reveal">“Cold Jet의 기술과<br>바테크의 국내 현장 경험을 함께 제공합니다.”</p>
    </div>
  </section>



  <!-- ============ 14 FINAL CTA ============ -->
  <section class="bls-sec bls-final last-freeze" id="bls-final">
    <div class="wrap">
      <div class="bls-final-grid">
        <div>
          <span class="cmp-eyebrow">FIND YOUR BLASTER</span>
          <h2 class="cmp-h2">어떤 장비가 맞는지,<br>실제 세척으로 확인해보세요.</h2>
        </div>
        <div>
          <div class="cmp-lead">
            <p>세척 결과는 같은 장비를 사용해도 오염물의 종류와 부착 상태, 소재와 작업 조건에 따라 달라질 수 있습니다.</p>
            <p>바테크는 실제 부품 · 금형 · 오염 샘플을 이용한 테스트를 통해 필요한 세척 조건을 확인하고, 그 결과에 맞는 Cold Jet 블라스터와 노즐을 제안합니다.</p>
          </div>
          <div class="cmp-cta-btns">
            <a class="cta-btn" href="../../rental/demo.html">세척 테스트 신청</a>
            <a class="cmp-btn-ghost" href="../compare-equip.html">장비 상담</a>
          </div>
          <a class="bls-textlink" href="../../rental/index.html">렌탈 · 데모 보기 →</a>
        </div>
      </div>
    </div>
  </section>"""

PELLETIZER_PAGE_TITLE = '드라이아이스 생산 시스템 | 펠렛타이저·슬라이스·자동화'
PELLETIZER_PAGE_DESC = '펠렛타이저부터 슬라이스 제조기, 리포머, 정량 투입·포장·CO2 회수까지 Cold Jet 드라이아이스 생산 시스템과 적용 분야를 살펴보세요.'
PELLETIZER_SCRIPT = """  <script>
  /* 마지막 섹션(.last-freeze)이 뷰포트보다 높을 때 — top을 음수로 밀어 마지막 한 화면만 틀고정되게 한다.
     (섹션 상단이 화면에 닿는 순간 고정되면 아래 내용을 볼 수 없으므로, 섹션 하단이 화면 하단에 닿을 때 고정.) */
  (function () {
    var el = document.getElementById('bls-partner');
    if (!el) return;
    function sync() {
      if (window.innerWidth <= 900) { el.style.top = ''; return; }
      el.style.top = Math.min(0, window.innerHeight - el.offsetHeight) + 'px';
    }
    sync();
    window.addEventListener('resize', sync);
    if ('ResizeObserver' in window) { new ResizeObserver(sync).observe(el); }
  })();
  </script>
  <script>
  (function () {
    var stage = document.getElementById('useStage');
    if (!stage) return;
    var items = Array.prototype.slice.call(stage.querySelectorAll('.plt-use-item'));
    var imgs = Array.prototype.slice.call(stage.querySelectorAll('.plt-use-frame img'));
    var counter = document.getElementById('useCounter'), tag = document.getElementById('useTag'), bar = document.getElementById('useProgress');
    var cur = 0, timer = null, stopped = false, DUR = 5000;
    function pad(n) { return String(n + 1).padStart(2, '0'); }
    function setActive(i) {
      cur = (i + items.length) % items.length;
      items.forEach(function (li, k) { li.classList.toggle('is-active', k === cur); });
      imgs.forEach(function (im, k) { im.classList.toggle('is-active', k === cur); });
      counter.innerHTML = pad(cur) + ' <i>/</i> ' + pad(items.length - 1);
      tag.textContent = items[cur].querySelector('small').textContent;
      restartBar();
    }
    function restartBar() {
      bar.style.animation = 'none';
      void bar.offsetWidth;
      bar.style.animation = stopped ? 'none' : 'pltUseProgress ' + DUR + 'ms linear forwards';
    }
    function play() { if (stopped) return; clearInterval(timer); timer = setInterval(function () { setActive(cur + 1); }, DUR); restartBar(); }
    function pause() { clearInterval(timer); bar.style.animationPlayState = 'paused'; }
    items.forEach(function (li, k) {
      li.querySelector('button').addEventListener('click', function () { stopped = true; clearInterval(timer); setActive(k); });
      li.addEventListener('mouseenter', function () { if (k !== cur) { setActive(k); if (!stopped) play(); } });
    });
    stage.addEventListener('mouseenter', pause);
    stage.addEventListener('mouseleave', function () { if (!stopped) { bar.style.animationPlayState = ''; play(); } });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) { entries.forEach(function (e) { e.isIntersecting ? play() : pause(); }); }, { threshold: .3 }).observe(stage);
    } else { play(); }
  })();
  </script>
  <script>
  (function () {
    var ytMedia = document.getElementById('ytTestMedia'), ytBtn = document.getElementById('ytTestPlayBtn');
    if (ytMedia && ytBtn) {
      ytBtn.addEventListener('click', function () {
        ytMedia.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/pkO1got3w3g?start=2232&autoplay=1&rel=0" title="Cold Jet Pelletizer" style="position:absolute;inset:0;width:100%;height:100%;border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
      });
    }
  })();
  </script>
  <script>
  (function () {
    var video = document.querySelector('.plt-reason-video');
    var grid = document.querySelector('.plt-reason-grid');
    if (!video || !grid) return;
    function sync() {
      if (window.innerWidth <= 1100) { grid.style.height = ''; return; }
      grid.style.height = '';
      var natural = grid.offsetHeight;
      grid.style.height = Math.max(video.offsetHeight, natural) + 'px';
    }
    sync();
    window.addEventListener('resize', sync);
    if ('ResizeObserver' in window) { new ResizeObserver(sync).observe(video); }
  })();
  </script>
  <script>
  (function () {
    var el = document.getElementById('compareFreeze');
    if (!el) return;
    function sync() {
      if (window.innerWidth <= 900) { el.style.top = ''; return; }
      el.style.top = Math.min(0, window.innerHeight - el.offsetHeight) + 'px';
    }
    sync();
    window.addEventListener('resize', sync);
    if ('ResizeObserver' in window) { new ResizeObserver(sync).observe(el); }
  })();
  </script>
  <script>
  (function () {
    var el = document.getElementById('techHlTitle');
    var el2 = document.getElementById('compareHlTitle');
    var targets = [el, el2].filter(Boolean);
    if (!targets.length) return;
    if (!('IntersectionObserver' in window)) { targets.forEach(function (t) { t.classList.add('is-hl'); }); return; }
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-hl');
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.4, rootMargin: '0px 0px -10% 0px' });
    targets.forEach(function (t) { obs.observe(t); });
  })();
  </script>
  <script>
  (function () {
    [['pltDefinitionVideo', 'pltDefinitionPlayBtn'], ['pltReasonVideo', 'pltReasonPlayBtn']].forEach(function (pair) {
    var v = document.getElementById(pair[0]), btn = document.getElementById(pair[1]);
    if (v && btn) {
      btn.addEventListener('click', function () { if (v.paused) { v.play(); } else { v.pause(); } });
      v.addEventListener('play', function () {
        btn.classList.add('is-playing');
        btn.querySelector('.bls-play-label').textContent = '일시정지';
        btn.querySelector('.bls-play-icon').textContent = '❙❙';
      });
      v.addEventListener('pause', function () {
        btn.classList.remove('is-playing');
        btn.querySelector('.bls-play-label').textContent = '영상 재생';
        btn.querySelector('.bls-play-icon').textContent = '▶';
      });
    }
    });
  })();
  </script>
  <script>
  (function () {
    var slider = document.getElementById('capacitySelector');
    var capacityNumber = document.getElementById('capacityNumber');
    var form = document.getElementById('productionFinder');
    var dimensionFields = document.getElementById('dimensionFields');
    var dimensionIntro = document.getElementById('dimensionIntro');
    var dimensionHelp = document.getElementById('dimensionHelp');
    var locationField = document.getElementById('locationField');
    var sliceSupplyField = document.getElementById('sliceSupplyField');
    var capacityLimit = document.getElementById('capacityLimit');
    var capacityTicks = document.getElementById('capacityTicks');
    var capacityStep = document.getElementById('capacityStep');
    var dimensionStep = document.getElementById('dimensionStep');
    var dailyDemand = document.getElementById('dailyDemand');
    var dailyHours = document.getElementById('dailyHours');
    var dailyResult = document.getElementById('dailyResult');
    var finderPrev = document.getElementById('finderPrev');
    var finderNextStep = document.getElementById('finderNextStep');
    var finderResult = document.getElementById('finderResult');
    var finderProducts = document.getElementById('finderProducts');
    var finderCurrentStep = document.getElementById('finderCurrentStep');
    var stepThreeLabel = document.getElementById('stepThreeLabel');
    var stepSummaries = [null, document.getElementById('stepSummary1'), document.getElementById('stepSummary2'), document.getElementById('stepSummary3'), document.getElementById('stepSummary4')];
    var progressButtons = Array.prototype.slice.call(document.querySelectorAll('[data-go-step]'));
    var finderSteps = Array.prototype.slice.call(form.querySelectorAll('[data-finder-step]'));
    var currentFinderStep = 1;
    var cards = Array.prototype.slice.call(document.querySelectorAll('.plt-product[data-capacity]'));
    if (!slider || !capacityNumber || !form || !dimensionFields) return;

    var output = {
      type: document.getElementById('finderType'),
      model: document.getElementById('finderModel'),
      reason: document.getElementById('finderReason'),
      config: document.getElementById('finderConfig'),
      next: document.getElementById('finderNext'),
      link: document.getElementById('finderLink'),
      note: document.getElementById('finderNote'),
      tip: document.getElementById('finderNoteTip')
    };
    var pelletModels = [
      { capacity:80, sizes:[3], name:'PE 80', image:'../../assets/img/pelletizer-pe80-official.jpg', link:'pe-80.html' },
      { capacity:120, sizes:[3,10,16], name:'PR120H', image:'../../assets/img/pelletizer-pr120h-official.jpg', link:'pr120h.html' },
      { capacity:350, sizes:[3,6,10,16], name:'PR350H', image:'../../assets/img/pelletizer-pr350h-official.jpg', link:'pr350h.html' },
      { capacity:750, sizes:[3,6,10,16], name:'PR750H', image:'../../assets/img/pelletizer-pr750h-official.jpg', link:'pr750h.html' },
      { capacity:1500, sizes:[3,6,10,16], name:'PR1500H', image:'../../assets/img/pelletizer-pr1500h-official.jpg', link:'pr1500h.html' }
    ];
    var pelletSizes = [1.7,3,6,10,16];
    var sliceFormats = [
      { value:'125 × 125 × 19 mm', models:'500,1000', label:'125 × 125 × 19 mm · R500H / R1000H' },
      { value:'125 × 125 × 25 mm', models:'500,1000,2000', label:'125 × 125 × 25 mm · R500H / R1000H / R2000H' },
      { value:'125 × 125 × 50 mm', models:'500,1000,2000', label:'125 × 125 × 50 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 19 mm', models:'500,1000', label:'127 × 254 × 19 mm · R500H / R1000H' },
      { value:'127 × 254 × 25 mm', models:'500,1000,2000', label:'127 × 254 × 25 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 50 mm', models:'500,1000,2000', label:'127 × 254 × 50 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 60 mm', models:'500,1000,2000', label:'127 × 254 × 60 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 64 mm', models:'500,1000,2000', label:'127 × 254 × 64 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 68 mm', models:'500,1000', label:'127 × 254 × 68 mm · R500H / R1000H' },
      { value:'127 × 254 × 76 mm', models:'2000', label:'127 × 254 × 76 mm · R2000H' },
      { value:'210 × 125 × 19 mm', models:'500,1000', label:'210 × 125 × 19 mm · R500H / R1000H' },
      { value:'210 × 125 × 25 mm', models:'500,1000', label:'210 × 125 × 25 mm · R500H / R1000H' },
      { value:'210 × 125 × 50 mm', models:'500,1000', label:'210 × 125 × 50 mm · R500H / R1000H' },
      { value:'210 × 125 × 60 mm', models:'500,1000', label:'210 × 125 × 60 mm · R500H / R1000H' },
      { value:'210 × 125 × 70 mm', models:'500,1000', label:'210 × 125 × 70 mm · R500H / R1000H' },
      { value:'150 × 150 × 19 mm', models:'500,1000', label:'150 × 150 × 19 mm · R500H / R1000H' },
      { value:'150 × 150 × 25 mm', models:'500,1000', label:'150 × 150 × 25 mm · R500H / R1000H' },
      { value:'150 × 150 × 50 mm', models:'500,1000', label:'150 × 150 × 50 mm · R500H / R1000H' },
      { value:'150 × 150 × 60 mm', models:'500,1000', label:'150 × 150 × 60 mm · R500H / R1000H' },
      { value:'150 × 150 × 70 mm', models:'500,1000', label:'150 × 150 × 70 mm · R500H / R1000H' },
      { value:'150 × 150 × 80 mm', models:'500,1000', label:'150 × 150 × 80 mm · R500H / R1000H' },
      { value:'150 × 150 × 90 mm', models:'500,1000', label:'150 × 150 × 90 mm · R500H / R1000H' },
      { value:'125 × 105 × 19 mm', models:'500,1000', label:'125 × 105 × 19 mm · R500H / R1000H' },
      { value:'125 × 105 × 25 mm', models:'500,1000', label:'125 × 105 × 25 mm · R500H / R1000H' },
      { value:'125 × 105 × 50 mm', models:'500,1000', label:'125 × 105 × 50 mm · R500H / R1000H' },
      { value:'138 × 60 × 19 mm', models:'500,1000', label:'138 × 60 × 19 mm · R500H / R1000H' },
      { value:'138 × 60 × 25 mm', models:'500,1000', label:'138 × 60 × 25 mm · R500H / R1000H' },
      { value:'138 × 60 × 50 mm', models:'500,1000', label:'138 × 60 × 50 mm · R500H / R1000H' },
      { value:'254 × 254 × 25 mm', models:'2000', label:'254 × 254 × 25 mm · R2000H' },
      { value:'254 × 254 × 50 mm', models:'2000', label:'254 × 254 × 50 mm · R2000H' },
      { value:'254 × 254 × 60 mm', models:'2000', label:'254 × 254 × 60 mm · R2000H' },
      { value:'254 × 254 × 64 mm', models:'2000', label:'254 × 254 × 64 mm · R2000H' },
      { value:'254 × 254 × 76 mm', models:'2000', label:'254 × 254 × 76 mm · R2000H' }
    ];
    var sliceFootprints = [
      { value:'125 × 125', inch:'5 × 5 in', className:'is-square' },
      { value:'127 × 254', inch:'5 × 10 in', className:'is-wide' },
      { value:'254 × 254', inch:'10 × 10 in', className:'is-large-square' },
      { value:'210 × 125', inch:'8 × 5 in', className:'is-landscape' },
      { value:'150 × 150', inch:'6 × 6 in', className:'is-square' },
      { value:'125 × 105', inch:'5 × 4 in', className:'is-compact' },
      { value:'138 × 60', inch:'5.4 × 2.4 in', className:'is-slim' }
    ];
    var reformers = [
      { code:'500', capacity:600, name:'R500H' },
      { code:'1000', capacity:1000, name:'R1000H' },
      { code:'2000', capacity:2500, name:'R2000H' }
    ];
    var shapeNames = { pellet:'펠렛·너겟', slice:'슬라이스·블록' };

    function currentShape() {
      return form.querySelector('input[name="iceShape"]:checked').value;
    }
    function currentSliceSupply() {
      return form.querySelector('input[name="sliceSupply"]:checked').value;
    }
    function updateFinderProgress() {
      var shape = currentShape();
      var nextLabels = shape === 'pellet' ? ['','제품 치수','설치 방식','생산량'] : ['','제품 치수','펠렛 공급','생산량'];
      stepThreeLabel.textContent = shape === 'pellet' ? '설치 방법 선택' : '펠렛 공급 방법 선택';
      finderSteps.forEach(function (step) {
        step.classList.toggle('is-active', Number(step.getAttribute('data-finder-step')) === currentFinderStep);
      });
      progressButtons.forEach(function (button) {
        var step = Number(button.getAttribute('data-go-step'));
        button.classList.toggle('is-active', step === currentFinderStep);
        button.classList.toggle('is-complete', step < currentFinderStep);
        button.setAttribute('aria-current', step === currentFinderStep ? 'step' : 'false');
      });
      finderPrev.disabled = currentFinderStep === 1;
      var progressNav = document.querySelector('.plt-finder-progress');
      if (progressNav) progressNav.style.setProperty('--fp', (currentFinderStep - 1) / 3);
      finderCurrentStep.textContent = currentFinderStep;
      if (currentFinderStep < 4) {
        finderNextStep.innerHTML = '다음 <i>→</i>';
      } else {
        finderNextStep.innerHTML = '추천 결과 보기 <i>→</i>';
      }
    }
    function setFinderStep(step) {
      currentFinderStep = Math.max(1, Math.min(4, step));
      if (currentFinderStep < 4) {
        finderResult.hidden = true;
        finderResult.classList.remove('is-visible');
      }
      updateFinderProgress();
    }
    function updateFinderSummaries() {
      var shape = currentShape();
      var shapeInput = form.querySelector('input[name="iceShape"]:checked');
      stepSummaries[1].textContent = shapeInput.nextElementSibling.querySelector('b').textContent;
      stepSummaries[2].textContent = dimensionSummary(shape);
      if (shape === 'pellet') {
        stepSummaries[3].textContent = form.querySelector('input[name="installation"]:checked').value === 'mobile' ? '장소 변경 고려' : '고정 설치';
      } else {
        stepSummaries[3].textContent = currentSliceSupply() === 'produce' ? '펠렛도 함께 생산' : '기존 펠렛 사용';
      }
      stepSummaries[4].textContent = Number(capacityNumber.value || 20).toLocaleString('ko-KR') + ' kg/h';
      updateFinderProgress();
    }
    function renderDimensions() {
      var shape = currentShape();
      locationField.hidden = shape !== 'pellet';
      sliceSupplyField.hidden = shape !== 'slice';
      if (shape === 'pellet') {
        dimensionFields.innerHTML = '<div class="plt-size-choice"><span>펠렛·너겟 직경</span><div>' + pelletSizes.map(function (size) {
          return '<label><input type="radio" name="diameter" value="' + size + '"' + (size === 3 ? ' checked' : '') + '><b>' + size + '</b><i>mm</i></label>';
        }).join('') + '</div></div>';
        dimensionIntro.textContent = '펠렛타이저가 압출·절단해 만드는 낱개 펠렛·너겟의 지름을 선택합니다. 이 규격과 필요한 생산량에 맞는 장비를 검토합니다.';
        dimensionHelp.textContent = '펠렛과 너겟은 길이를 지정하지 않으며, 직경 규격과 필요한 생산량으로 장비를 검토합니다.';
        dimensionStep.textContent = '02';
      } else {
        dimensionFields.innerHTML = '<div class="plt-slice-builder"><span class="plt-field-label">가로 × 세로</span><div class="plt-footprint-options">' + sliceFootprints.map(function (footprint, index) {
          return '<label><input type="radio" name="sliceFootprint" value="' + footprint.value + '"' + (index === 0 ? ' checked' : '') + '><span><i class="' + footprint.className + '" aria-hidden="true"></i><b>' + footprint.value + '</b><small>mm · ' + footprint.inch + '</small></span></label>';
        }).join('') + '</div><span class="plt-field-label plt-thickness-label">두께</span><div class="plt-thickness-options" id="thicknessOptions"></div></div>';
        renderSliceThickness();
        dimensionIntro.textContent = '이 규격은 완성된 슬라이스·블록의 크기입니다. 리포머(R Series)가 드라이아이스 펠렛을 압축해 선택한 가로×세로×두께로 성형합니다.';
        dimensionHelp.textContent = '첨부된 R Series 규격표를 기준으로 선택합니다. R Series는 펠렛을 슬라이스·블록으로 재성형하는 리포머입니다.';
        dimensionStep.textContent = '02';
      }
      Array.prototype.forEach.call(dimensionFields.querySelectorAll('input[name="diameter"]'), function (input) {
        input.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); updateVisual(); });
      });
      Array.prototype.forEach.call(dimensionFields.querySelectorAll('input[name="sliceFootprint"]'), function (input) {
        input.addEventListener('change', function () { renderSliceThickness(); updateCapacityLimit(); updateRecommendation(); updateVisual(); });
      });
      capacityStep.textContent = '04';
      updateFinderProgress();
      updateVisual();
    }
    function renderSliceThickness() {
      var container = dimensionFields.querySelector('#thicknessOptions');
      var selectedFootprint = dimensionFields.querySelector('input[name="sliceFootprint"]:checked');
      if (!container || !selectedFootprint) return;
      var formats = sliceFormats.filter(function (format) { return format.value.indexOf(selectedFootprint.value + ' × ') === 0; });
      container.innerHTML = formats.map(function (format, index) {
        var thickness = format.value.replace(selectedFootprint.value + ' × ', '').replace(' mm', '');
        var modelNames = format.models.split(',').map(function (code) { return 'R' + code + 'H'; }).join(' · ');
        return '<label><input type="radio" name="sliceThickness" value="' + format.value + '" data-models="' + format.models + '"' + (index === 0 ? ' checked' : '') + '><span><b>' + thickness + ' mm</b><small>' + modelNames + '</small></span></label>';
      }).join('');
      Array.prototype.forEach.call(container.querySelectorAll('input'), function (input) {
        input.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); updateVisual(); });
      });
      updateVisual();
    }
    function dimensionSummary(shape) {
      if (shape === 'pellet') return 'Ø ' + dimensionFields.querySelector('input[name="diameter"]:checked').value + ' mm';
      return dimensionFields.querySelector('input[name="sliceThickness"]:checked').value;
    }
    function nums(str) { return (String(str).match(/[\d.]+/g) || []).map(Number); }
    function isoFacePoints(pts) { return pts.map(function (p) { return p.x.toFixed(1) + ',' + p.y.toFixed(1); }).join(' '); }
    function isoBoxSvg(w, d, h) {
      var ux = 0.866, uy = 0.5, vx = -0.866, vy = 0.5;
      var scaleH = 188 / ((w + d) * ux);
      var scaleV = 168 / ((w + d) * uy + h);
      var scale = Math.min(scaleH, scaleV, 1.35);
      var W = w * scale, D = d * scale, H = Math.max(h * scale, 5);
      var cx = 110 - (W * ux - D * ux) / 2;
      var cy = 96 - (W * uy + D * uy + H) / 2;
      var top = { x: cx, y: cy };
      var right = { x: cx + W * ux, y: cy + W * uy };
      var left = { x: cx + D * vx, y: cy + D * vy };
      var front = { x: cx + W * ux + D * vx, y: cy + W * uy + D * vy };
      var rightB = { x: right.x, y: right.y + H };
      var leftB = { x: left.x, y: left.y + H };
      var frontB = { x: front.x, y: front.y + H };
      var fill = 'fill="#ffffff" stroke="none"';
      var edges = [[top, right], [top, left], [right, front], [left, front], [right, rightB], [left, leftB], [front, frontB], [rightB, frontB], [leftB, frontB]];
      var d1 = edges.map(function (e) { return 'M' + e[0].x.toFixed(1) + ',' + e[0].y.toFixed(1) + ' L' + e[1].x.toFixed(1) + ',' + e[1].y.toFixed(1); }).join(' ');
      return '<polygon points="' + isoFacePoints([right, front, frontB, rightB]) + '" ' + fill + '></polygon>' +
        '<polygon points="' + isoFacePoints([left, front, frontB, leftB]) + '" ' + fill + '></polygon>' +
        '<polygon points="' + isoFacePoints([top, right, front, left]) + '" ' + fill + '></polygon>' +
        '<path d="' + d1 + '" fill="none" stroke="#283739" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"></path>';
    }
    function isoCylinderSvg(diameter) {
      var rx = 4 + (diameter / 16) * 20;
      var ry = rx * 0.5;
      var height = rx * 3.4;
      var cx = 110, topY = 96 - (height + ry * 2) / 2 + ry;
      var fill = 'fill="#ffffff" stroke="none"';
      return '<rect x="' + (cx - rx) + '" y="' + topY + '" width="' + (rx * 2) + '" height="' + height + '" ' + fill + '></rect>' +
        '<ellipse cx="' + cx + '" cy="' + (topY + height) + '" rx="' + rx + '" ry="' + ry + '" ' + fill + '></ellipse>' +
        '<ellipse cx="' + cx + '" cy="' + topY + '" rx="' + rx + '" ry="' + ry + '" ' + fill + '></ellipse>' +
        '<path d="M ' + (cx - rx) + ' ' + topY + ' L ' + (cx - rx) + ' ' + (topY + height) + ' A ' + rx + ' ' + ry + ' 0 0 0 ' + (cx + rx) + ' ' + (topY + height) + ' L ' + (cx + rx) + ' ' + topY + '" fill="none" stroke="#283739" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"></path>' +
        '<ellipse cx="' + cx + '" cy="' + topY + '" rx="' + rx + '" ry="' + ry + '" fill="none" stroke="#283739" stroke-width="1.6"></ellipse>';
    }
    function updateVisual() {
      var svg = document.getElementById('finderVisualSvg');
      var caption = document.getElementById('finderVisualCaption');
      if (!svg || !caption) return;
      var shape = currentShape();
      if (shape === 'pellet') {
        var diameterInput = dimensionFields.querySelector('input[name="diameter"]:checked');
        if (!diameterInput) return;
        var d = Number(diameterInput.value);
        svg.innerHTML = isoCylinderSvg(d);
        caption.textContent = 'Ø ' + d + ' mm';
      } else {
        var footprintInput = dimensionFields.querySelector('input[name="sliceFootprint"]:checked');
        var thicknessInput = dimensionFields.querySelector('input[name="sliceThickness"]:checked');
        if (!footprintInput || !thicknessInput) return;
        var fp = nums(footprintInput.value);
        var th = nums(thicknessInput.value);
        var w = fp[0], dep = fp[1], h = th[2];
        svg.innerHTML = isoBoxSvg(w, dep, h);
        caption.textContent = w + ' × ' + dep + ' × ' + h + ' mm';
      }
    }
    function setResult(result) {
      var products = result.products || [{ name:result.name, image:result.image, role:result.productRole || '추천 장비', processImage:result.processImage }];
      finderProducts.innerHTML = products.map(function (product, index) {
        return '<article><div><img src="' + product.image + '" alt="' + product.name + '" class="' + (product.processImage ? 'is-process' : '') + '"></div><span>' + String(index + 1).padStart(2,'0') + ' / ' + product.role + '</span><strong>' + product.name + '</strong></article>';
      }).join('<span class="plt-result-op is-plus" aria-hidden="true"></span>');
      var eqOp = document.getElementById('finderResultEq');
      if (eqOp) eqOp.style.display = products.length > 1 ? '' : 'none';
      output.type.textContent = result.type;
      output.model.textContent = result.name;
      output.reason.textContent = result.reason;
      output.config.textContent = result.config;
      output.next.textContent = result.next;
      output.link.href = result.link;
      output.link.firstChild.nodeValue = result.linkText + ' ';
      output.note.textContent = result.note || '이 결과는 장비 검토를 위한 참고 자료입니다. 실제 장비 선정은 필요한 생산량과 제품 규격, LCO₂ 공급 조건, 후공정과 자동화 범위를 확인한 뒤 결정합니다.';
      output.tip.textContent = result.tip || '';
      output.tip.style.display = result.tip ? 'block' : 'none';
    }
    function capacityTip(list, need, matched) {
      if (!matched) return null;
      var sorted = list.slice().sort(function (a, b) { return a.capacity - b.capacity; });
      var idx = sorted.findIndex(function (item) { return item.capacity === matched.capacity; });
      var prev = idx > 0 ? sorted[idx - 1] : null;
      var prevCap = prev ? prev.capacity : 0;
      var range = matched.capacity - prevCap;
      if (prev && range > 0 && (need - prevCap) <= range * 0.4) {
        return { type:'down', text:'선택하신 ' + need.toLocaleString('ko-KR') + ' kg/h를 ' + prevCap.toLocaleString('ko-KR') + ' kg/h로 조금만 낮추면 ' + prev.name + ' 모델로도 충분해 투자비를 줄일 수 있습니다.' };
      }
      if (matched.capacity > need) {
        return { type:'up', text:'이번 조건에 추천된 ' + matched.name + '는 최대 ' + matched.capacity.toLocaleString('ko-KR') + ' kg/h까지 생산할 수 있는 모델입니다. 해당 생산량까지는 추가 모델 변경 없이 대응할 수 있습니다.' };
      }
      return null;
    }
    function updateCapacityLimit() {
      var shape = currentShape();
      var max = 1500;
      var description = '고정형 펠렛타이저 기준';
      if (shape === 'pellet') {
        var diameter = Number(dimensionFields.querySelector('input[name="diameter"]:checked').value);
        var mobile = form.querySelector('input[name="installation"]:checked').value === 'mobile';
        if (mobile) {
          max = 350;
          description = 'Production Hub · PR120H 또는 PR350H 기준';
        } else if (diameter === 1.7) {
          max = 1500;
          description = '1.7 mm · 표준 모델 별도 검토';
        }
      } else {
        var selected = dimensionFields.querySelector('input[name="sliceThickness"]:checked');
        var codes = selected.getAttribute('data-models').split(',');
        max = codes.indexOf('2000') !== -1 ? 2500 : (codes.indexOf('1000') !== -1 ? 1000 : 600);
        var supplyDescription = currentSliceSupply() === 'produce' ? ' · 펠렛타이저 함께 구성' : ' · 기존 펠렛 공급';
        description = (codes.indexOf('2000') !== -1 ? '선택 규격의 R2000H 포함 기준' : '선택 규격의 R500H·R1000H 기준') + supplyDescription;
      }
      slider.max = max;
      capacityNumber.max = max;
      var current = Number(capacityNumber.value) || 20;
      if (current > max) current = max;
      if (current < 20) current = 20;
      slider.value = current;
      capacityNumber.value = current;
      capacityLimit.innerHTML = '<b>현재 조건에서 선택 가능</b><span>최대 ' + max.toLocaleString('ko-KR') + ' kg/h · ' + description + '</span>';
      var tickValues = [20, .25, .5, .75, 1].map(function (value, index) {
        if (index === 0) return 20;
        if (index === 4) return max;
        return Math.round((20 + (max - 20) * value) / 10) * 10;
      });
      capacityTicks.innerHTML = tickValues.map(function (value, index) {
        return '<span>' + value.toLocaleString('ko-KR') + (index === 4 ? ' kg/h' : '') + '</span>';
      }).join('');
    }
    function updateRecommendation() {
      var allowedMax = Number(slider.max);
      var need = Math.max(20, Math.min(allowedMax, Number(capacityNumber.value) || 20));
      var shape = currentShape();
      var size = dimensionSummary(shape);
      var result;

      if (shape === 'pellet') {
        var diameter = Number(dimensionFields.querySelector('input[name="diameter"]:checked').value);
        var mobile = form.querySelector('input[name="installation"]:checked').value === 'mobile';
        var candidates = mobile ? pelletModels.filter(function (item) { return item.name === 'PR120H' || item.name === 'PR350H'; }) : pelletModels;
        var machine = candidates.find(function (item) { return item.capacity >= need && item.sizes.indexOf(diameter) !== -1; });
        if (mobile && machine) {
          result = { name:'Production Hub + ' + machine.name, image:'../../assets/img/pelletizer-hub-official.png', link:'../quote.html', linkText:'Production Hub 상담', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'설치 장소 변경을 고려해 ' + machine.name + '를 탑재한 독립형 Production Hub 구성을 추천합니다.', config:size + ' · ' + machine.name + ' 탑재', next:'이동·설치 인프라 확인' };
        } else if (mobile && !machine) {
          result = { name:'Production Hub 맞춤 검토', image:'../../assets/img/pelletizer-hub-official.png', link:'../quote.html', linkText:'Production Hub 상담', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'Production Hub는 PR120H 또는 PR350H 구성만 가능하므로 선택한 직경과 생산량에 대한 별도 검토가 필요합니다.', config:size + ' · Hub 적용성 검토', next:'생산량·설치 장소 확인' };
        } else if (!machine) {
          result = { name:'맞춤 펠렛 생산 시스템', image:'../../assets/img/pelletizer-pr1500h-official.jpg', link:'../quote.html', linkText:'시스템 구성 상담', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'선택한 직경과 생산량을 동시에 충족하는 단일 표준 모델이 없어 다이와 병렬 구성을 함께 검토해야 합니다.', config:size + ' · 다이 및 생산량 검토', next:'일일 운전 시간 확인' };
        } else {
          result = { name:machine.name, image:machine.image, link:machine.link, linkText:'추천 모델 상세 보기', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'입력한 조건과 생산량을 기준으로 우선 검토할 수 있는 펠렛타이저입니다.', config:size + ' · 전용 다이 검토', next:'LCO₂ 공급 조건 확인', tip:(capacityTip(candidates, need, machine) || {}).text };
        }
      } else {
        var formatOption = dimensionFields.querySelector('input[name="sliceThickness"]:checked');
        var supportedModels = formatOption.getAttribute('data-models').split(',');
        var reformer = reformers.find(function (item) { return item.capacity >= need && supportedModels.indexOf(item.code) !== -1; });
        var makePellets = currentSliceSupply() === 'produce';
        var pelletizer = pelletModels.find(function (item) { return item.capacity >= need; });
        if (reformer) {
          if (makePellets && pelletizer) {
            var pelletizerTip = capacityTip(pelletModels, need, pelletizer);
            var reformerCandidates = reformers.filter(function (item) { return supportedModels.indexOf(item.code) !== -1; });
            var reformerTip = capacityTip(reformerCandidates, need, reformer);
            var combinedTip = (pelletizerTip && pelletizerTip.type === 'down') ? pelletizerTip.text : (reformerTip && reformerTip.type === 'down') ? reformerTip.text : (pelletizerTip ? pelletizerTip.text : (reformerTip ? reformerTip.text : ''));
            result = { name:pelletizer.name + ' + ' + reformer.name, image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, products:[{name:pelletizer.name,image:pelletizer.image,role:'펠렛 생산'},{name:reformer.name,image:'../../assets/img/pelletizer-rseries-official.jpg',role:'슬라이스 재성형',processImage:true}], link:'../quote.html', linkText:'통합 생산 시스템 상담', type:shapeNames[shape] + ' 생산·리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'펠렛 생산부터 슬라이스·블록 재성형까지 이어지도록 ' + pelletizer.name + ' 펠렛타이저와 ' + reformer.name + ' 리포머를 함께 구성합니다.', config:size + ' · ' + pelletizer.name + ' → ' + reformer.name, next:'펠렛 이송·버퍼 구성 확인', note:'R Series 자체는 드라이아이스를 생산하지 않는 리포머입니다. 이 추천은 필요한 펠렛을 현장에서 생산하는 펠렛타이저를 함께 포함한 1차 구성입니다.', tip:combinedTip };
          } else if (makePellets && !pelletizer) {
            result = { name:'펠렛타이저 맞춤 구성 + ' + reformer.name, image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, products:[{name:'펠렛타이저 맞춤 구성',image:'../../assets/img/pelletizer-pr1500h-official.jpg',role:'펠렛 생산'},{name:reformer.name,image:'../../assets/img/pelletizer-rseries-official.jpg',role:'슬라이스 재성형',processImage:true}], link:'../quote.html', linkText:'통합 생산 시스템 상담', type:shapeNames[shape] + ' 생산·리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'리포머 처리량에 맞는 펠렛을 함께 생산하려면 복수 펠렛타이저 또는 생산라인 맞춤 구성이 필요합니다.', config:size + ' · 펠렛 생산 병렬 구성 → ' + reformer.name, next:'펠렛타이저 대수·버퍼 용량 확인', note:'R Series 자체는 드라이아이스를 생산하지 않습니다. 시간당 1,500 kg을 초과하는 펠렛 생산은 단일 표준 펠렛타이저 범위를 넘어 병렬 구성과 연속 운전 조건을 함께 검토해야 합니다.' };
          } else {
            result = { name:reformer.name, image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, link:'special-forms.html', linkText:'R Series 상세 보기', type:shapeNames[shape] + ' 리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'기존에 공급되는 펠렛을 선택한 규격으로 재성형하며 필요한 처리량을 충족하는 가장 가까운 R Series 리포머입니다.', config:size + ' · 기존 펠렛 공급 → ' + reformer.name, next:'원료 펠렛 공급량·이송 확인', note:'R Series는 펠렛을 슬라이스·블록으로 재성형하는 리포머입니다. 이 구성은 필요한 양의 펠렛이 기존 제조기 또는 외부 공급을 통해 확보된다는 조건입니다.', tip:(capacityTip(reformers.filter(function (item) { return supportedModels.indexOf(item.code) !== -1; }), need, reformer) || {}).text };
          }
        } else {
          result = { name:'R Series 맞춤 검토', image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, link:'../quote.html', linkText:'리포머 구성 상담', type:shapeNames[shape] + ' 리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'선택한 규격과 처리량을 동시에 충족하는 표준 R Series 구성이 없어 규격 또는 병렬 운전을 검토해야 합니다.', config:size + (makePellets ? ' · 펠렛타이저 함께 검토' : ' · 기존 펠렛 공급 조건'), next:'규격·처리량 재검토', note:'R Series는 리포머입니다. 펠렛도 함께 생산하는 경우에는 필요한 처리량에 맞는 드라이아이스 제조기 구성까지 함께 검토해야 합니다.' };
        }
      }

      cards.forEach(function (card) { card.classList.remove('is-recommended'); });
      if (shape === 'pellet') {
        var matchingCard = cards.find(function (card) { return card.querySelector('h3').textContent === result.name; });
        if (matchingCard) matchingCard.classList.add('is-recommended');
      }
      setResult(result);
      slider.setAttribute('aria-valuetext', '시간당 ' + need.toLocaleString('ko-KR') + '킬로그램, 추천 ' + result.name);
      updateFinderSummaries();
    }
    function updateFromDailyDemand() {
      var demand = Math.max(1, Number(dailyDemand.value) || 1);
      var hours = Math.max(1, Math.min(24, Number(dailyHours.value) || 1));
      var calculated = Math.ceil(demand / hours);
      var applied = Math.max(20, Math.min(Number(slider.max), calculated));
      dailyResult.innerHTML = '<small>필요 시간당 생산량</small><b>' + calculated.toLocaleString('ko-KR') + ' kg/h</b>' + (calculated > Number(slider.max) ? '<em>현재 조건의 최대 범위를 초과합니다.</em>' : '');
      slider.value = applied;
      capacityNumber.value = applied;
      updateRecommendation();
    }

    slider.addEventListener('input', function () {
      capacityNumber.value = slider.value;
      updateRecommendation();
    });
    capacityNumber.addEventListener('input', function () {
      var raw = Number(capacityNumber.value);
      if (!isNaN(raw) && capacityNumber.value !== '') {
        slider.value = Math.max(20, Math.min(Number(slider.max), raw));
      }
      updateRecommendation();
    });
    capacityNumber.addEventListener('blur', function () {
      var clamped = Math.max(20, Math.min(Number(slider.max), Number(capacityNumber.value) || 20));
      capacityNumber.value = clamped;
      slider.value = clamped;
      updateRecommendation();
    });
    Array.prototype.forEach.call(form.querySelectorAll('input[name="iceShape"]'), function (radio) {
      radio.addEventListener('change', function () { renderDimensions(); updateCapacityLimit(); updateRecommendation(); });
    });
    Array.prototype.forEach.call(form.querySelectorAll('input[name="installation"]'), function (radio) {
      radio.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); });
    });
    Array.prototype.forEach.call(form.querySelectorAll('input[name="sliceSupply"]'), function (radio) {
      radio.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); });
    });
    progressButtons.forEach(function (button) {
      button.addEventListener('click', function () { setFinderStep(Number(button.getAttribute('data-go-step'))); });
    });
    finderPrev.addEventListener('click', function () { setFinderStep(currentFinderStep - 1); });
    finderNextStep.addEventListener('click', function () {
      if (currentFinderStep < 4) {
        setFinderStep(currentFinderStep + 1);
      } else {
        finderResult.hidden = false;
        finderResult.classList.remove('is-visible');
        void finderResult.offsetWidth;
        finderResult.classList.add('is-visible');
        output.model.setAttribute('tabindex', '-1');
        output.model.focus({ preventScroll:true });
        finderResult.scrollIntoView({ behavior:'smooth', block:'start' });
      }
    });
    dailyDemand.addEventListener('input', updateFromDailyDemand);
    dailyHours.addEventListener('input', updateFromDailyDemand);
    renderDimensions();
    updateCapacityLimit();
    updateRecommendation();
    setFinderStep(1);
  })();
  </script>
"""
PELLETIZER_HUB_BODY = """
  <main class="plt-page">
    <section class="subhero-parallax pel-hero-stage">
      <div class="subhero-breadcrumb wrap"><a href="../../index.html">홈</a> &gt; <a href="../index.html">제품 · 자동화 · 공급</a> &gt; 드라이아이스 제조기</div>
      <div class="hero-fit">
        <video class="subhero-parallax-img pel-hero-video" autoplay muted loop playsinline preload="auto" poster="../../assets/img/pelletizer-hero-poster.webp" data-buffer="0" data-pan-scale="1">
          <source src="../../assets/video/pelletizer-hero.mp4" type="video/mp4" />
        </video>
        <div class="subhero-textbox">
          <span class="ind-hero-eyebrow">COLD JET × VATEK / DRY ICE PRODUCTION</span>
          <h1>필요한 드라이아이스를<br><span class="bls-hero-accent">필요한 만큼 생산합니다.</span></h1>
          <p class="bls-hero-main">액화 CO<sub>2</sub>로 펠렛과 너겟을 생산하고, 필요에 따라 슬라이스와 블록으로 재성형합니다. 정량 공급과 포장, CO<sub>2</sub> 회수 시스템까지 필요한 생산량과 사용 목적에 맞춰 구성할 수 있습니다.</p>
          
        </div>
        <div class="pel-hero-mask" aria-hidden="true">
          <img src="../../assets/img/coldjet-logo.png" alt="" />
          <span>×</span>
          <img src="../../assets/img/vatek-logo-wordmark.png" alt="" />
        </div>
      </div>
    </section>

    <section class="plt-definition pel-cover tint-hatch" id="what-is-pelletizer">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">WHAT IS A PELLETIZER?</span><h2 class="plt-title">펠렛타이저는<br>드라이아이스를 직접 생산하는 장비입니다.</h2></div>
          <p class="plt-lead">액화 CO<sub>2</sub>(LCO<sub>2</sub>)를 팽창시켜 드라이아이스 스노우를 만들고, 이를 압축·압출해 펠렛이나 너겟 형태로 생산합니다.</p>
        </div>
        <div class="bls-showcase-frame reveal">
        <div class="bls-showcase">
          <div class="bls-showcase-media">
            <video id="pltDefinitionVideo" class="bls-media-fade" muted loop playsinline preload="metadata" poster="../../assets/img/pelletizer-nozzle-snow.jpg">
              <source src="../../assets/video/pelletizer-definition.mp4" type="video/mp4" />
            </video>
            <span class="bls-showcase-cap">COLD JET&nbsp;&nbsp;/&nbsp;&nbsp;PELLETIZER</span>
            <button type="button" class="bls-play-btn" id="pltDefinitionPlayBtn" aria-label="영상 재생">
              <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
            </button>
          </div>
          <div class="bls-showcase-body">
            <span class="bls-dot-eyebrow">DRY ICE PRODUCTION MACHINES</span>
            <h3>드라이아이스의 품질을 결정하는<br>생산 기술</h3>
            <p>Cold Jet은 Sub-Cooling Technology와 정밀한 압축·압출 기술을 적용해 밀도가 높고 균일한 드라이아이스를 생산합니다. LCO<sub>2</sub> 사용 효율과 안정적인 연속 생산, 제품 규격 전환까지 실제 생산 과정에서 필요한 요소를 하나의 시스템에 담았습니다.</p>
          </div>
        </div>
        </div>
      </div>
    </section>

    <section class="plt-section plt-category-select" id="machine-categories">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">DRY ICE MACHINE CATEGORIES</span><h2 class="plt-title">생산 목적과 환경에 맞게<br>선택할 수 있는 Cold Jet 생산 시스템</h2></div>
          <p class="plt-lead">드라이아이스의 형태와 크기, 생산량 그리고 환경 조건에 따라 장비를 구성할 수 있습니다. 각 제품군을 선택해 상세 내용을 확인해보세요.</p>
        </div>
        <div class="plt-category-grid">
          <a class="plt-category-card" href="#model-finder">
            <div class="plt-category-media"><img src="../../assets/img/pelletizer-category-pellet-lineup.jpg" alt="Cold Jet 펠렛 제조기" loading="lazy" decoding="async" /></div>
            <div class="plt-category-body"><span class="plt-category-num">01</span><h3>펠렛 제조기</h3><p>PE 80 · PR120H · PR350H · PR750H · PR1500H — 소규모 자체 생산부터 대용량 생산까지, 액화 CO<sub>2</sub>로 펠렛과 너겟을 생산하는 Cold Jet의 펠렛타이저 라인업입니다.</p><span class="bls-more">시리즈 보기 <i>→</i></span></div>
          </a>
          <a class="plt-category-card" href="#model-finder">
            <div class="plt-category-media"><img src="../../assets/img/pelletizer-category-slice-ds1000.jpg" alt="Cold Jet 슬라이스 제조기" loading="lazy" decoding="async" /></div>
            <div class="plt-category-body"><span class="plt-category-num">02</span><h3>다이렉트 슬라이스 제조기</h3><p>DS500E · DS1000E — 펠렛을 별도로 생산하지 않고 액화 CO<sub>2</sub>에서 드라이아이스 슬라이스를 직접 생산하는 시스템입니다.</p><span class="bls-more">시리즈 보기 <i>→</i></span></div>
          </a>
          <a class="plt-category-card" href="#model-finder">
            <div class="plt-category-media"><img src="../../assets/img/pelletizer-category-special-unit.jpg" alt="Cold Jet 특수 제조기" loading="lazy" decoding="async" /></div>
            <div class="plt-category-body"><span class="plt-category-num">03</span><h3>특수 생산 시스템</h3><p>Production Hub · P3000 · Dosing &amp; Bagging System — 일반적인 고정형 펠렛 생산과 다른 조건에 대응하는 시스템입니다. 현장 이동형 Production Hub, Integrated Dosing System 등 사용 목적에 맞는 구성을 선택할 수 있습니다.</p><span class="bls-more">자세히 보기 <i>→</i></span></div>
          </a>
          <a class="plt-category-card" href="#model-finder">
            <div class="plt-category-media"><img src="../../assets/img/pelletizer-category-dosing-system.jpg" alt="Cold Jet 통합 정량 공급 시스템" loading="lazy" decoding="async" /></div>
            <div class="plt-category-body"><span class="plt-category-num">04</span><h3>통합 정량 공급 시스템</h3><p>드라이아이스 생산과 정량 공급을 하나의 시스템으로 구성합니다. 생산된 드라이아이스를 설정한 양만큼 용기나 생산 공정에 바로 공급할 수 있습니다.</p><span class="bls-more">자세히 보기 <i>→</i></span></div>
          </a>
          <a class="plt-category-card" href="special-forms.html">
            <div class="plt-category-media"><img src="../../assets/img/pelletizer-category-reformer.jpg" alt="Cold Jet R Series 리포머" loading="lazy" decoding="async" /></div>
            <div class="plt-category-body"><span class="plt-category-num">05</span><h3>리포머</h3><p>R500H · R1000H · R2000H — 드라이아이스 펠렛을 다시 압축해 슬라이스나 블록 형태로 만드는 장비입니다. R500H · R1000H · R2000H 등 필요한 생산량과 제품 규격에 맞춰 선택할 수 있습니다.</p><span class="bls-more">R Series 자세히 보기 <i>→</i></span></div>
          </a>
        </div>
      </div>
    </section>

    <section class="plt-section plt-applications" id="applications">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">WHERE DRY ICE WORKS</span><h2 class="plt-title">용도에 맞는<br>드라이아이스를 생산합니다.</h2></div>
          <p class="plt-lead">드라이아이스는 사용 목적에 따라 필요한 형태와 규격이 달라집니다. 블라스팅, 식품 냉각, 운송 등 사용처를 먼저 정하면 필요한 규격과 생산량, 후공정 구성을 보다 정확하게 검토할 수 있습니다.</p>
        </div>
        <div class="plt-use-stage" id="useStage">
          <ol class="plt-use-index">
            <li class="plt-use-item is-active" data-i="0"><button type="button"><span class="plt-use-no">01</span><span class="plt-use-main"><b>드라이아이스 세척<small>펠렛타이저</small></b><span class="plt-use-desc">블라스팅에 사용하는 3 mm 펠렛을 필요한 곳에서 직접 생산할 수 있습니다.</span></span></button></li>
            <li class="plt-use-item" data-i="1"><button type="button"><span class="plt-use-no">02</span><span class="plt-use-main"><b>식품 공정 냉각<small>펠렛 · 너겟 / 정량 투입</small></b><span class="plt-use-desc">혼합·분쇄·포장 등의 생산 공정에서 펠렛이나 너겟을 투입해 제품의 온도를 낮추거나 유지합니다.</span></span></button></li>
            <li class="plt-use-item" data-i="2"><button type="button"><span class="plt-use-no">03</span><span class="plt-use-main"><b>식품 배송 · 콜드체인<small>슬라이스 / 자동 포장</small></b><span class="plt-use-desc">육류, 수산물, 밀키트와 냉동식품 등 저온 유지가 필요한 제품의 운송에 사용합니다. 필요한 보냉 시간과 포장 조건에 맞춰 드라이아이스의 형태와 투입량을 결정합니다.</span></span></button></li>
            <li class="plt-use-item" data-i="3"><button type="button"><span class="plt-use-no">04</span><span class="plt-use-main"><b>항공 케이터링<small>R Series 리포머</small></b><span class="plt-use-desc">기내식 등 온도 관리가 필요한 식품의 보관과 운송에 사용할 드라이아이스 슬라이스를 생산합니다.</span></span></button></li>
            <li class="plt-use-item" data-i="4"><button type="button"><span class="plt-use-no">05</span><span class="plt-use-main"><b>바이오 · 생명과학<small>슬라이스 / 정량 투입</small></b><span class="plt-use-desc">검체와 의약품 등 저온 유지가 필요한 운송과 보관에 사용할 드라이아이스를 생산합니다.</span></span></button></li>
            <li class="plt-use-item" data-i="5"><button type="button"><span class="plt-use-no">06</span><span class="plt-use-main"><b>드라이아이스 생산 · 판매<small>고용량 라인 / 리포머</small></b><span class="plt-use-desc">판매 용도에 맞는 펠렛, 너겟, 슬라이스 등을 필요한 생산량에 맞춰 생산하고 포장할 수 있습니다.</span></span></button></li>
          </ol>
          <div class="plt-use-media">
            <div class="plt-use-frame">
              <img class="is-active" src="../../assets/img/pelletizer-use-cleaning.jpg" alt="Cold Jet 장비로 생산한 드라이아이스를 담는 모습" loading="lazy" decoding="async">
              <img src="../../assets/img/pelletizer-use-foodprocess.webp" alt="드라이아이스와 함께 포장되는 육류 제품" loading="lazy" decoding="async">
              <img src="../../assets/img/pelletizer-use-coldchain.jpg" alt="냉동 탑차를 이용한 콜드체인 운송" loading="lazy" decoding="async">
              <img src="../../assets/img/pelletizer-use-aviation.jpg" alt="항공 기내식 케이터링 카트" loading="lazy" decoding="async">
              <img src="../../assets/img/pelletizer-use-bio.webp" alt="실험실에서 검체를 다루는 연구원" loading="lazy" decoding="async">
              <img src="../../assets/img/pelletizer-use-production.jpg" alt="노즐에서 분사되는 드라이아이스 펠렛" loading="lazy" decoding="async">
              <span class="plt-use-progress" aria-hidden="true"><i id="useProgress"></i></span>
            </div>
            <div class="plt-use-caption"><span id="useCounter">01 <i>/</i> 06</span><span id="useTag">펠렛타이저</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="plt-section plt-reasons">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">WHY PRODUCE ON DEMAND?</span><h2 class="plt-title">드라이아이스를<br>직접 생산하는 이유</h2></div>
          <p class="plt-lead">드라이아이스는 생산된 순간부터 계속 승화합니다. 필요한 양을 필요한 시점에 직접 생산하면 보관 중 발생하는 손실을 줄이고, 외부 공급 일정에 맞출 필요 없이 생산과 사용 계획을 직접 관리할 수 있습니다.</p>
        </div>
        <div class="plt-reason-stage">
          <div class="plt-reason-video reveal">
            <div class="bls-showcase-media">
              <video id="pltReasonVideo" class="bls-media-fade" muted loop playsinline preload="metadata">
                <source src="../../assets/video/pelletizer-ondemand.mp4" type="video/mp4" />
              </video>
              <span class="bls-showcase-cap">COLD JET&nbsp;&nbsp;/&nbsp;&nbsp;ON-DEMAND PRODUCTION</span>
              <button type="button" class="bls-play-btn" id="pltReasonPlayBtn" aria-label="영상 재생">
                <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
              </button>
            </div>
          </div>
        <div class="plt-reason-grid">
          <article class="plt-reason"><h3>필요할 때 바로 생산</h3><p>필요한 시점에 필요한 양을 생산해 작업 일정이나 출하 계획에 맞춰 사용할 수 있습니다.</p></article>
          <article class="plt-reason"><h3>생산 직후 바로 사용</h3><p>생산한 드라이아이스를 바로 사용하면 보관 중 발생하는 승화 손실을 줄일 수 있습니다.</p></article>
          <article class="plt-reason"><h3>용도에 맞는 규격</h3><p>블라스팅, 냉각, 운송 등 사용 목적에 맞춰 펠렛과 너겟의 규격을 선택할 수 있습니다.</p></article>
          <article class="plt-reason"><h3>필요한 생산량에 맞게</h3><p>소규모 자체 사용부터 대용량 생산·판매까지 필요한 생산량에 맞는 장비를 선택할 수 있습니다.</p></article>
        </div>
        </div>
      </div>
    </section>

    <section class="plt-section plt-tech" id="pelletizer-difference">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">THE COLD JET DIFFERENCE</span><h2 class="plt-title hl-title" id="techHlTitle"><span class="plt-hl" style="--hd:0s;--hr:-0.6deg">드라이아이스 생산을 위한</span><br><span class="plt-hl" style="--hd:.32s;--hr:0.5deg">Cold Jet의 핵심 기술</span></h2></div>
          <p class="plt-lead">Cold Jet은 LCO<sub>2</sub> 사용 효율부터 드라이아이스의 밀도와 균일성, 생산 초기의 안정성과 제품 규격 전환까지 실제 생산 과정에서 필요한 기술을 발전시켜 왔습니다. 아래 네 가지 기술은 Cold Jet 펠렛타이저의 주요 특징입니다.</p>
        </div>
        <div class="bls-tech-list">
          <article class="bls-tech reveal">
            <div class="bls-tech-media"><img src="../../assets/img/pelletizer-tech-01.jpg" alt="드라이아이스 노즐 분사" loading="lazy" decoding="async" /></div>
            <div class="bls-tech-body">
              <span class="bls-num">01</span>
              <span class="bls-en">SUB-COOLING TECHNOLOGY</span>
              <h3>LCO<sub>2</sub> 사용 효율을 높이는<br>Sub-Cooling Technology</h3>
              <p>Sub-Cooling Technology는 펠렛타이저에 공급되는 액화 CO<sub>2</sub>를 사전에 냉각해 드라이아이스로 전환되는 비율을 높이는 기술입니다. 같은 양의 드라이아이스를 생산할 때 필요한 LCO<sub>2</sub> 사용량을 줄이는 데 도움이 됩니다.</p>
            </div>
          </article>
          <article class="bls-tech reveal" style="--reveal-delay:0.06s">
            <div class="bls-tech-media"><img src="../../assets/img/pelletizer-tech-03.jpg" alt="열교환기 CO2 냉각" loading="lazy" decoding="async" /></div>
            <div class="bls-tech-body">
              <span class="bls-num">02</span>
              <span class="bls-en">HIGH-DENSITY PELLET PRODUCTION</span>
              <h3>단단하고 균일한<br>드라이아이스 생산</h3>
              <p>Cold Jet은 드라이아이스 스노우를 정밀하게 압축한 뒤 다이 플레이트를 통해 압출합니다. 충분한 밀도로 성형된 드라이아이스는 취급과 운송 과정에서 쉽게 부서지지 않고, 균일한 형태를 유지하는 데 유리합니다.</p>
            </div>
          </article>
          <article class="bls-tech reveal">
            <div class="bls-tech-media"><img src="../../assets/img/pelletizer-tech-04.jpg" alt="압출 헤드 구조" loading="lazy" decoding="async" /></div>
            <div class="bls-tech-body">
              <span class="bls-num">03</span>
              <span class="bls-en">CLOSED-CHAMBER TECHNOLOGY</span>
              <h3>생산 초기부터<br>안정적인 품질</h3>
              <p>Closed-Chamber Technology는 생산을 시작하는 초기 단계부터 일정한 품질의 드라이아이스를 만들 수 있도록 설계된 기술입니다. 빠른 기동과 안정적인 생산 전환을 통해 대기 시간과 불필요한 CO<sub>2</sub> 손실을 줄입니다.</p>
            </div>
          </article>
          <article class="bls-tech reveal" style="--reveal-delay:0.06s">
            <div class="bls-tech-media"><img src="../../assets/img/pelletizer-tech-02.jpg" alt="유압 압축 구동부" loading="lazy" decoding="async" /></div>
            <div class="bls-tech-body">
              <span class="bls-num">04</span>
              <span class="bls-en">AUTOMATIC QUICK DIE CHANGE</span>
              <h3>생산 규격을<br>빠르게 전환합니다.</h3>
              <p>Automatic Quick Die Change가 적용된 모델은 여러 규격의 다이 플레이트를 장비에 장착해 두고, HMI에서 필요한 규격을 선택해 빠르게 전환할 수 있습니다. PR350H · PR750H 등 지원 모델에서는 3 mm, 6 mm, 10 mm, 16 mm 규격을 선택할 수 있어 제품 변경에 따른 작업 중단 시간을 줄일 수 있습니다.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="plt-section plt-lineup" id="pelletizer-lineup">
      <div class="wrap">
        <section class="plt-finder" id="model-finder" aria-labelledby="finderTitle">
          <div class="plt-finder-head">
            <div><span class="plt-eyebrow">FIND YOUR PRODUCTION SYSTEM</span><h2 id="finderTitle">조건을 선택하고<br>적합한 생산 시스템을 확인해보세요.</h2></div>
            <div class="plt-finder-intro"><p>필요한 드라이아이스 형태와 규격, 설치 방법과 시간당 생산량을 선택하면 검토 가능한 장비 구성을 확인할 수 있습니다.</p></div>
            <nav class="plt-finder-progress" aria-label="장비 선택 단계">
              <button type="button" class="is-active" data-go-step="1"><i>01</i><span>드라이아이스 형태 선택</span><small id="stepSummary1">펠렛 · 너겟</small></button>
              <button type="button" data-go-step="2"><i>02</i><span>희망 규격 선택</span><small id="stepSummary2">Ø 3 mm</small></button>
              <button type="button" data-go-step="3"><i>03</i><span id="stepThreeLabel">설치 방법 선택</span><small id="stepSummary3">고정 설치</small></button>
              <button type="button" data-go-step="4"><i>04</i><span>희망 생산량 선택</span><small id="stepSummary4">350 kg/h</small></button>
            </nav>
          </div>

          <div class="plt-finder-shell">
            <div class="plt-finder-row">
              <div class="plt-finder-main">
                <form class="plt-finder-form" id="productionFinder">
              <fieldset class="plt-shape-field is-active" data-finder-step="1">
                <legend><span>01</span> 원하는 드라이아이스 형태</legend>
                <div class="plt-shape-options">
                  <label><input type="radio" name="iceShape" value="pellet" checked><span><i class="shape-pellet" aria-hidden="true"></i><b>펠렛 · 너겟</b><small>블라스팅 · 공정 냉각 · 대용량 냉각</small></span></label>
                  <label><input type="radio" name="iceShape" value="slice"><span><i class="shape-slice" aria-hidden="true"></i><b>슬라이스 · 블록</b><small>운송 · 콜드체인 · 장시간 보냉</small></span></label>
                </div>
              </fieldset>

              <fieldset class="plt-dimension-field" data-finder-step="2">
                <legend><span id="dimensionStep">02</span> 원하는 제품 규격</legend>
                <p class="plt-field-intro" id="dimensionIntro">생산하려는 펠렛 또는 너겟의 지름을 선택하세요. 선택한 규격과 필요한 생산량을 기준으로 검토 가능한 장비를 안내합니다.</p>
                <div class="plt-dimension-fields" id="dimensionFields"></div>
                <p id="dimensionHelp">선택한 규격은 장비와 다이 구성을 검토하기 위한 기준입니다. 최종 사양은 필요한 생산량과 LCO<sub>2</sub> 공급 조건 등을 확인한 뒤 결정합니다.</p>
              </fieldset>

              <fieldset class="plt-location-field" id="locationField" data-finder-step="3">
                <legend><span id="locationStep">03</span> 설치 장소 변경 가능성</legend>
                <div class="plt-binary-options">
                  <label><input type="radio" name="installation" value="fixed" checked><span><b>고정 설치</b><small>한 장소에서 지속적으로 생산</small></span></label>
                  <label><input type="radio" name="installation" value="mobile"><span><b>이동 설치</b><small>Production Hub 검토</small></span></label>
                </div>
                <p><strong>Production Hub는 PR120H 또는 PR350H를 기반으로 구성됩니다.</strong></p>
              </fieldset>

              <fieldset class="plt-supply-field" id="sliceSupplyField" data-finder-step="3" hidden>
                <legend><span>03</span> 리포머용 펠렛 공급 방법</legend>
                <p class="plt-field-intro">R Series 리포머는 드라이아이스 펠렛을 압축해 슬라이스 또는 블록 형태로 만듭니다. 리포머에 사용할 펠렛을 직접 생산할지, 기존 펠렛이나 외부 공급을 이용할지 선택하세요.</p>
                <div class="plt-binary-options">
                  <label><input type="radio" name="sliceSupply" value="produce" checked><span><b>펠렛도 함께 생산</b><small>펠렛타이저 + R Series 구성</small><em>필요 설비: 드라이아이스 펠렛 제조기 + 리포머. 펠렛타이저가 펠렛을 생산하고, 리포머가 이를 압축해 원하는 슬라이스·블록 규격으로 성형합니다.</em></span></label>
                  <label><input type="radio" name="sliceSupply" value="existing"><span><b>기존 펠렛 사용</b><small>R Series 단독 구성</small><em>필요 설비: 리포머. 이미 확보한 드라이아이스 펠렛을 리포머에 투입해 원하는 슬라이스·블록 규격으로 압축·성형합니다.</em></span></label>
                </div>
              </fieldset>

              <fieldset class="plt-capacity-field" data-finder-step="4">
                <legend><span id="capacityStep">04</span> 필요한 시간당 생산량</legend>
                <div class="plt-capacity-limit" id="capacityLimit">현재 조건에서 선택 가능: 최대 1,500 kg/h</div>
                <div class="plt-selector">
                  <label for="capacitySelector" class="plt-selector-label">필요한 시간당 생산량</label>
                  <div class="plt-selector-track">
                    <input id="capacitySelector" type="range" min="20" max="1500" value="350" step="10" aria-describedby="capacityHelp" />
                    <div class="plt-capacity-ticks" id="capacityTicks" aria-hidden="true"></div>
                  </div>
                  <div class="plt-capacity-value"><input id="capacityNumber" type="number" min="1" max="1500" value="350" inputmode="numeric" aria-label="필요한 시간당 생산량 직접 입력"><span>kg/h</span></div>
                </div>
                <p id="capacityHelp">필요한 시간당 생산량을 입력하세요. 평균 사용량뿐 아니라 최대 사용량과 하루 실제 생산 시간을 함께 고려하면 적정 생산 능력을 검토하는 데 도움이 됩니다.</p>
                <details class="plt-demand-calc">
                  <summary>일일 사용량으로 시간당 생산량 계산</summary>
                  <div class="plt-demand-fields">
                    <label><span>하루 필요량</span><span class="plt-unit-input"><input id="dailyDemand" type="number" min="1" value="1000" inputmode="numeric"><i>kg/day</i></span></label>
                    <label><span>하루 생산 시간</span><span class="plt-unit-input"><input id="dailyHours" type="number" min="1" max="24" value="8" inputmode="numeric"><i>hours</i></span></label>
                    <output id="dailyResult"><small>필요 시간당 생산량</small><b>125 kg/h</b></output>
                  </div>
                </details>
              </fieldset>
                </form>
              </div>

              <aside class="plt-finder-visual" id="finderVisual" aria-hidden="true">
                <svg id="finderVisualSvg" viewBox="0 0 220 200" role="img" aria-label="선택한 치수의 3D 미리보기"></svg>
                <span class="plt-finder-visual-caption" id="finderVisualCaption"></span>
              </aside>
            </div>

            <div class="plt-finder-nav">
              <button type="button" class="plt-step-back" id="finderPrev" disabled>이전</button>
              <span><b id="finderCurrentStep">1</b> / 4</span>
              <button type="button" class="plt-step-next" id="finderNextStep">다음 <i>→</i></button>
            </div>

            <aside class="plt-finder-result" id="finderResult" aria-live="polite" hidden>
              <div class="plt-result-top"><span class="plt-result-label">선택한 조건에 맞는 장비</span><span class="plt-result-live">실시간 확인</span></div>
              <div class="plt-result-row">
              <div class="plt-result-products" id="finderProducts" aria-label="추천 제품 구성"></div>
              <span class="plt-result-op is-eq" id="finderResultEq" aria-hidden="true"></span>
              <div class="plt-result-summary"><small id="finderType">펠렛 생산 · 350 kg/h</small><h3 id="finderModel">PR350H</h3><p id="finderReason">입력한 조건과 생산량을 기준으로 우선 검토할 수 있는 펠렛타이저입니다.</p></div>
              </div>
              <div class="plt-result-actions" hidden><dl><div><dt>확인 사항</dt><dd id="finderConfig">펠렛 규격 확인</dd></div><div><dt>다음 단계</dt><dd id="finderNext">실제 사용량 확인</dd></div></dl></div>
              <div class="plt-result-note-box">
                <span class="plt-result-note-title">NOTE</span>
                <p id="finderNote">이 결과는 장비 검토를 위한 참고 자료입니다. 실제 장비 선정은 필요한 생산량과 제품 규격, LCO<sub>2</sub> 공급 조건, 후공정과 자동화 범위를 확인한 뒤 결정합니다.</p>
                <p id="finderNoteTip"></p>
                <div class="plt-result-note-footer"><a class="plt-btn is-small" id="finderLink" href="pr350h.html">추천 모델 상세 보기 <span>→</span></a></div>
              </div>
            </aside>
          </div>
        </section>
      </div>
    </section>

    <section class="plt-section plt-tech" id="difference">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">THE COLD JET DIFFERENCE</span><h2 class="plt-title hl-title" id="compareHlTitle"><span class="plt-hl" style="--hd:0s">생산량과 함께</span><br><span class="plt-hl" style="--hd:.32s">운전 안정성도 확인해야 합니다.</span></h2></div>
          <p class="plt-lead">펠렛타이저는 시간당 생산량만으로 장비를 판단하기 어렵습니다. 장시간 운전의 안정성, 제품 규격을 바꿀 때 필요한 시간, LCO<sub>2</sub> 사용 효율과 후공정 연결까지 실제 운영에 필요한 조건을 함께 확인해야 합니다. Cold Jet은 펠렛타이저뿐 아니라 정량 공급, 리포머, CO<sub>2</sub> 회수 등 생산 전후 공정을 연결할 수 있는 시스템을 제공합니다.</p>
        </div>
      </div>
    </section>

  </main>

      <div class="plt-compare-freeze" id="compareFreeze" style="padding: clamp(72px, 8vw, 128px) 0;">
        <div class="wrap">
          <div class="plt-head reveal">
            <div><span class="plt-eyebrow">COLD JET VS. GENERIC</span><h2 class="plt-title">펠렛타이저를 선택할 때<br>무엇을 비교해야 할까요?</h2></div>
            <p class="plt-lead">같은 생산량의 펠렛타이저라도 LCO<sub>2</sub> 사용 효율과 운전 방식, 제품 규격 전환, 원격 지원, 후공정 연결 방식에는 차이가 있습니다. 장비를 검토할 때 확인해야 할 주요 항목을 정리했습니다.</p>
          </div>
          <div class="plt-compare">
            <span class="plt-compare-line" aria-hidden="true"></span>
            <div class="plt-compare-head"><span>구매 시 비교할 항목</span><b>일반 제조기 검토 시</b><strong>Cold Jet 생산 시스템</strong></div>
            <div class="plt-compare-row"><span>제품 형태와 용량</span><p>생산 가능한 규격과 시간당 생산량 확인</p><p>80~1,500 kg/h 생산 라인과 R Series 리포머 구성</p></div>
            <div class="plt-compare-row"><span>LCO<sub>2</sub> 전환</span><p>LCO<sub>2</sub> 소비량과 전환 효율 확인</p><p>Sub-Cooling Technology 적용</p></div>
            <div class="plt-compare-row"><span>운전과 규격 전환</span><p>기동 방식과 제품 규격 변경 방법 확인</p><p>자동 운전 및 지원 모델의 Automatic Quick Die Change</p></div>
            <div class="plt-compare-row"><span>상태 확인과 지원</span><p>원격 모니터링과 서비스 방식 확인</p><p>지원 모델의 Cold Jet CONNECT® 원격 모니터링 및 진단</p></div>
            <div class="plt-compare-row"><span>후공정 연결</span><p>이송·계량·포장 설비 연계 방식 확인</p><p>정량 공급, 포장, 리포머 등 생산 공정 연계 가능</p></div>
            <div class="plt-compare-row"><span>CO<sub>2</sub> 회수</span><p>리버트 가스 처리 및 회수 방식 확인</p><p>RE-CO<sub>2</sub> 시스템을 연계해 리버트 가스 회수·재사용 가능</p></div>
          </div>
          <p class="plt-compare-note">※ 제조사와 모델에 따라 기능과 사양은 다를 수 있습니다. 실제 비교 시에는 필요한 생산량과 제품 규격, LCO<sub>2</sub> 공급 조건과 자동화 범위를 기준으로 확인해야 합니다.</p>
        </div>
      </div>

  <!-- ============ GLOBAL TECHNOLOGY · LOCAL SUPPORT ============ -->
  <section class="bls-sec bls-partner last-freeze" id="bls-partner" style="padding-bottom: clamp(200px, 26vh, 320px);">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">GLOBAL TECHNOLOGY · LOCAL SUPPORT</span>
        <h2 class="cmp-h2">장비만큼 중요한 것은,<br>한국에서의 기술 지원입니다.</h2>
      </div>
      <div class="bls-partner-grid">
        <img class="bls-partner-logo reveal" src="../../assets/img/coldjet-logo.png" alt="Cold Jet" />
        <img class="bls-partner-logo reveal" src="../../assets/img/vatek-logo-wordmark.png" alt="VATEK" />

        <div class="bls-partner-name reveal">Cold Jet LLC<span class="bls-partner-tagline">드라이아이스 블라스팅 기술의 개척자이자 글로벌 리더</span></div>
        <div class="bls-partner-name reveal">VATEK Corporation<span class="bls-partner-tagline">Cold Jet 대한민국 공식 총판</span></div>

        <div class="bls-partner-media reveal"><img src="../../assets/img/coldjet-hq-photo-1.jpg" alt="Cold Jet 본사" loading="lazy" decoding="async" /></div>
        <div class="bls-partner-media reveal"><img src="../../assets/img/vatek-building.jpg" alt="바테크 사옥" loading="lazy" decoding="async" /></div>

        <div class="bls-partner-desc reveal"><p>Cold Jet은 현대식 드라이아이스 블라스팅 기술을 비롯해 드라이아이스 생산설비, CO<sub>2</sub> 회수 시스템, 노즐과 자동화 솔루션을 개발·공급하고 있습니다.</p></div>
        <div class="bls-partner-desc reveal">
          <p>1988년 설립한 바테크는 Cold Jet의 대한민국 공식 총판으로, 장비 선정부터 설치·시운전, 교육과 A/S까지 국내 고객의 장비 도입과 운영을 지원합니다.</p>
          <p>바테크는 Cold Jet의 교육, 세미나 및 글로벌 컨퍼런스에 지속적으로 참여해 최신 기술과 적용 사례를 국내 고객 지원에 반영하고 있습니다.</p>
        </div>

        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/coldjet-hq-building.webp" alt="Cold Jet 글로벌 본사" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-2.jpg" alt="Cold Jet 생산 공장" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-3.jpg" alt="Cold Jet 라운지" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-4.jpg" alt="Cold Jet 사내 카페" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-5.webp" alt="Cold Jet 컨퍼런스" loading="lazy" decoding="async" />
        </div>
        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/vatek-coldjet-photo-1.jpg" alt="Cold Jet 본사 방문" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-2.jpg" alt="Cold Jet Asia Dealer Conference" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-3.jpg" alt="Cold Jet 글로벌 딜러 컨퍼런스" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-4.jpg" alt="Cold Jet 세미나 참석" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-5.jpg" alt="Cold Jet R&D 신제품 개발" loading="lazy" decoding="async" />
        </div>

        <div class="bls-partner-divider"></div>
        <div class="bls-partner-divider"></div>

        <ul class="bls-facts">
          <li><b>1986</b><small>현대식 드라이아이스 블라스팅 원천 특허</small></li>
          <li><b>250+</b><small>글로벌 특허</small></li>
          <li><b>3 · 3</b><small>R&amp;D 연구소 · 생산공장</small></li>
          <li><b>14</b><small>기술센터</small></li>
        </ul>
        <ul class="bls-facts is-vatek">
          <li><b>1988</b><small>설립 · 제조업 기반</small></li>
          <li><b>2014</b><small>기업부설연구소 설립 (하남)</small></li>
          <li><b>TEST</b><small>시편 · 내방 · 방문 테스트</small></li>
          <li><b>A/S</b><small>설치 · 교육 · 기술지원</small></li>
        </ul>
      </div>
      <p class="bls-quote reveal">“Cold Jet의 기술과<br>바테크의 국내 현장 경험을 함께 제공합니다.”</p>
    </div>
  </section>
"""


def build_blaster(root, nav_html, footer_html, page_shell, asset):
    depth = 2
    html = page_shell(BLASTER_PAGE_TITLE, BLASTER_PAGE_DESC, depth, "products", BLASTER_HUB_BODY,
                       extra_script=BLASTER_SCRIPT,
                       footer_hero_p="설비 특성, 오염 상태와 작업 환경을 고려해 현장에 맞는 솔루션을 제안합니다.")
    group_dir = os.path.join(root, "products", "blaster")
    os.makedirs(group_dir, exist_ok=True)
    with open(os.path.join(group_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    for m in BLASTER_MODELS + BLASTER_EXTRA_PAGES:
        build_model_page(root, "products", "blaster", "드라이아이스 세척기 (블라스터)", m, BLASTER_MODELS,
                          nav_html, footer_html, page_shell, asset)
    return 1 + len(BLASTER_MODELS) + len(BLASTER_EXTRA_PAGES)


def build_pelletizer(root, nav_html, footer_html, page_shell, asset):
    depth = 2
    extra_head = '\n<link rel="stylesheet" href="%spelletizer-page.css?v=20260914-10" />' % asset('assets/css/', depth)
    html = page_shell(PELLETIZER_PAGE_TITLE, PELLETIZER_PAGE_DESC, depth, "products", PELLETIZER_HUB_BODY,
                       extra_script=PELLETIZER_SCRIPT, extra_head=extra_head,
                       footer_hero_p="필요한 생산량과 드라이아이스 형태, LCO<sub>2</sub> 공급 조건과 후공정 구성을 확인해 현장에 맞는 생산 시스템을 제안합니다.")
    group_dir = os.path.join(root, "products", "pelletizer")
    os.makedirs(group_dir, exist_ok=True)
    with open(os.path.join(group_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    for m in PELLETIZER_MODELS:
        build_model_page(root, "products", "pelletizer", "드라이아이스 제조기 (펠렛타이저)", m, PELLETIZER_MODELS,
                          nav_html, footer_html, page_shell, asset)
    return 1 + len(PELLETIZER_MODELS)


RECOVERY_SCRIPT = """  <script>
  /* 마지막 섹션(.last-freeze)이 뷰포트보다 높을 때 — top을 음수로 밀어 마지막 한 화면만 틀고정되게 한다. */
  (function () {
    var el = document.getElementById('bls-partner');
    if (!el) return;
    function sync() {
      if (window.innerWidth <= 900) { el.style.top = ''; return; }
      el.style.top = Math.min(0, window.innerHeight - el.offsetHeight) + 'px';
    }
    sync();
    window.addEventListener('resize', sync);
    if ('ResizeObserver' in window) { new ResizeObserver(sync).observe(el); }
  })();
  </script>
  <script>
  (function () {
    var el = document.getElementById('recCompareHlTitle');
    if (!el) return;
    if (!('IntersectionObserver' in window)) { el.classList.add('is-hl'); return; }
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-hl');
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.6 });
    obs.observe(el);
  })();
  </script>
  <script>
  (function () {
    var form = document.getElementById('reco2Finder');
    if (!form) return;
    var IMG = '../../assets/img/';
    var PELLET = {
      pe80:   { cap:80 },
      pr120h: { cap:120 },
      pr350h: { cap:350 },
      pr750h: { cap:750 }
    };
    var RECO = {
      '80':   { name:'RE-CO2 80',     cap:80,   img:IMG + 'recovery-reco2-80-product.jpg',   href:'re-co2-80.html' },
      '160':  { name:'RE-CO2 160',    cap:160,  img:IMG + 'recovery-reco2-160-product.jpg',  href:'re-co2-160.html' },
      '320':  { name:'RE-CO2 320 V2', cap:320,  img:IMG + 'recovery-reco2-320-product.jpg',  href:'re-co2-320-v2.html' },
      '3500': { name:'RE-CO2 3500',   cap:3500, img:IMG + 'recovery-reco2-3500-render.jpg',  href:'re-co2-3500.html' }
    };
    var TOLERANCE = 30;
    var progress = document.querySelector('#reco2-finder .plt-finder-progress');
    var stepButtons = Array.prototype.slice.call(progress.querySelectorAll('[data-rec-step]'));
    var fields = Array.prototype.slice.call(form.querySelectorAll('[data-rec-field]'));
    var prev = document.getElementById('recPrev'), next = document.getElementById('recNextStep');
    var curEl = document.getElementById('recCurrentStep');
    var result = document.getElementById('recResult');
    var visualImg = document.getElementById('recVisualImg'), visualCap = document.getElementById('recVisualCaption');
    var growWrap = document.getElementById('recGrowthInputWrap'), growInput = document.getElementById('recGrowthAmount');
    var summaryList = document.getElementById('recSummaryList');
    var out = { type:document.getElementById('recType'), model:document.getElementById('recModel'), reason:document.getElementById('recReason'), tip:document.getElementById('recNoteTip'), link:document.getElementById('recLink'), products:document.getElementById('recProducts') };
    var step = 1;

    function val(name) { var el = form.querySelector('input[name="' + name + '"]:checked'); return el ? el.value : ''; }
    function label(name) { var el = form.querySelector('input[name="' + name + '"]:checked'); return el ? el.parentNode.querySelector('b').textContent : ''; }

    // 3500(대형·컨테이너형)이 아니면 80/160/320V2 조합으로 총 용량을 충족시키는 구성을 찾는다
    function combine(total) {
      if (total > 320 * 3 + TOLERANCE) return [{ key:'3500', count:1 }];
      var tiers = ['80', '160', '320'], remaining = total, combo = [];
      while (remaining > 0) {
        var picked = null;
        for (var i = 0; i < tiers.length; i++) {
          var t = RECO[tiers[i]];
          if (remaining <= t.cap + TOLERANCE) { picked = tiers[i]; break; }
        }
        if (picked) { combo.push(picked); remaining = 0; }
        else { combo.push('320'); remaining -= 320; }
      }
      var counts = {};
      combo.forEach(function (k) { counts[k] = (counts[k] || 0) + 1; });
      return Object.keys(counts).sort(function (a, b) { return RECO[a].cap - RECO[b].cap; }).map(function (k) { return { key:k, count:counts[k] }; });
    }

    function recommend() {
      var band = PELLET[val('recModel')], grow = val('recGrowth') === 'grow';
      var growAmt = grow ? Math.max(0, Number(growInput.value) || 0) : 0;
      var total = band.cap + growAmt;
      var combo = combine(total);
      var rows = [
        { label:'현재 생산량', value:label('recModel') },
        { label:'증설 계획', value:label('recGrowth') }
      ];
      if (grow) rows.push({ label:'희망 추가 생산량', value:growAmt.toLocaleString() + ' kg/h' });
      rows.push({ label:'총 필요 용량', value:total.toLocaleString() + ' kg/h' });
      summaryList.innerHTML = rows.map(function (r) { return '<div class="rec-summary-row"><span>' + r.label + '</span><b>' + r.value + '</b></div>'; }).join('');
      var reason;
      if (combo.length === 1 && combo[0].key === '3500') {
        reason = '총 ' + total.toLocaleString() + ' kg/h 규모의 대형 생산량에는 컨테이너형 3500이 회수 톤당 에너지 소비가 가장 낮습니다.';
      } else if (combo.length > 1) {
        reason = '총 ' + total.toLocaleString() + ' kg/h를 충족하려면 한 모델만으로는 부족합니다. ' + combo.map(function (c) { return RECO[c.key].name + (c.count > 1 ? ' × ' + c.count : ''); }).join(' + ') + ' 조합으로 용량을 채웁니다.';
      } else {
        reason = '시간당 ' + total.toLocaleString() + ' kg 생산량을 충족하는 가장 가까운 회수 용량의 모델입니다.';
      }
      var primary = combo.slice().sort(function (a, b) { return RECO[b.key].cap - RECO[a.key].cap; })[0];
      var modelLabel = combo.map(function (c) { return RECO[c.key].name + (c.count > 1 ? ' × ' + c.count : ''); }).join(' + ');
      out.type.textContent = '총 생산량 ' + total.toLocaleString() + ' kg/h';
      out.model.textContent = modelLabel;
      out.reason.innerHTML = reason;
      out.tip.textContent = combo.length > 1 ? 'RE-CO2는 모듈형 구조로, 여러 유닛을 한 라인에 함께 구성할 수 있습니다.' : '';
      out.link.href = RECO[primary.key].href;
      visualImg.src = RECO[primary.key].img; visualImg.alt = RECO[primary.key].name;
      visualCap.textContent = modelLabel;
      out.products.innerHTML = combo.map(function (c, i) {
        var r = RECO[c.key];
        return '<article><div><img src="' + r.img + '" alt="' + r.name + '"></div><span>' + String(i + 1).padStart(2, '0') + ' · CO₂ 리커버리</span><strong>' + r.name + (c.count > 1 ? ' × ' + c.count : '') + '</strong></article>';
      }).join('<span class="plt-result-op is-plus" aria-hidden="true"></span>');
    }

    function syncSummaries() {
      var grow = val('recGrowth') === 'grow';
      growWrap.hidden = !grow;
      document.getElementById('recSummary1').textContent = label('recModel');
      document.getElementById('recSummary2').textContent = grow ? ('증설 예정 · +' + (Number(growInput.value) || 0) + 'kg/h') : label('recGrowth');
      recommend();
    }

    function setStep(n) {
      step = Math.max(1, Math.min(3, n));
      fields.forEach(function (f) { f.classList.toggle('is-active', Number(f.getAttribute('data-rec-field')) === step); });
      stepButtons.forEach(function (b) {
        var s = Number(b.getAttribute('data-rec-step'));
        b.classList.toggle('is-active', s === step);
        b.classList.toggle('is-complete', s < step);
        b.setAttribute('aria-current', s === step ? 'step' : 'false');
      });
      prev.disabled = step === 1;
      progress.style.setProperty('--fp', (step - 1) / 2);
      curEl.textContent = step;
      next.style.display = step < 3 ? '' : 'none';
      next.innerHTML = step < 2 ? '다음 <i>→</i>' : '결과 보기 <i>→</i>';
      if (step === 3) {
        result.hidden = false;
        result.classList.remove('is-visible');
        void result.offsetWidth;
        result.classList.add('is-visible');
      } else {
        result.hidden = true;
        result.classList.remove('is-visible');
      }
    }

    form.addEventListener('change', syncSummaries);
    growInput.addEventListener('input', syncSummaries);
    stepButtons.forEach(function (b) { b.addEventListener('click', function () { setStep(Number(b.getAttribute('data-rec-step'))); }); });
    prev.addEventListener('click', function () { setStep(step - 1); });
    next.addEventListener('click', function () {
      setStep(step + 1);
      if (step === 3) {
        var top = result.getBoundingClientRect().top + window.pageYOffset - 96;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
    syncSummaries();
    setStep(1);
  })();
  </script>
  <script>
  (function () {
    [['recShowcaseVideo', 'recShowcasePlayBtn'], ['recProcessVideo', 'recProcessPlayBtn']].forEach(function (pair) {
    var v = document.getElementById(pair[0]), btn = document.getElementById(pair[1]);
    if (v && btn) {
      // 재생 전 첫 장면이 보이도록 메타데이터 로드 후 첫 프레임으로 이동
      v.addEventListener('loadedmetadata', function () { try { v.currentTime = 0.01; } catch (e) {} }, { once: true });
      btn.addEventListener('click', function () { if (v.paused) { v.play(); } else { v.pause(); } });
      v.addEventListener('play', function () {
        btn.classList.add('is-playing');
        btn.querySelector('.bls-play-label').textContent = '일시정지';
        btn.querySelector('.bls-play-icon').textContent = '❙❙';
      });
      v.addEventListener('pause', function () {
        btn.classList.remove('is-playing');
        btn.querySelector('.bls-play-label').textContent = '영상 재생';
        btn.querySelector('.bls-play-icon').textContent = '▶';
      });
    }
    });
    // 수치 카운트업: .rec-stats가 화면에 들어오면 0 → 목표값으로 한 번만 애니메이션
    var stats = document.querySelector('.rec-stats');
    if (stats) {
      var counters = stats.querySelectorAll('.rec-count');
      var run = function () {
        counters.forEach(function (el) {
          var target = parseInt(el.getAttribute('data-count'), 10) || 0, dur = 1400, t0 = null;
          var step = function (ts) {
            if (t0 === null) t0 = ts;
            var p = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * e);
            if (p < 1) requestAnimationFrame(step); else el.textContent = target;
          };
          requestAnimationFrame(step);
        });
      };
      if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
          if (entries.some(function (en) { return en.isIntersecting; })) { run(); io.disconnect(); }
        }, { threshold: 0.4 });
        io.observe(stats);
      } else { run(); }
    }
  })();
  </script>
  <script>
  (function () {
    var el = document.getElementById('rec-final');
    if (!el) return;
    function sync() {
      if (window.innerWidth <= 900) { el.style.top = ''; return; }
      el.style.top = Math.min(0, window.innerHeight - el.offsetHeight) + 'px';
    }
    sync();
    window.addEventListener('resize', sync);
    if ('ResizeObserver' in window) { new ResizeObserver(sync).observe(el); }
  })();
  </script>
"""


RECOVERY_BODY = """    <section class="subhero-parallax rec-hero-stage">
      <div class="subhero-breadcrumb wrap"><a href="../../index.html">홈</a> &gt; <a href="../index.html">제품 · 자동화 · 공급</a> &gt; CO₂ 리커버리</div>
      <div class="hero-fit">
        <video class="subhero-parallax-img rec-hero-video" autoplay muted loop playsinline preload="auto" poster="../../assets/img/recovery-hero-poster.webp" data-buffer="0" data-pan-scale="1">
          <source src="../../assets/video/recovery-hero.mp4" type="video/mp4" />
        </video>
        <div class="subhero-textbox">
          <span class="ind-hero-eyebrow">COLD JET × VATEK / CO₂ RECOVERY SYSTEM</span>
          <h1>버려지던 CO₂를<br><span class="bls-hero-accent">다시 생산 자원으로.</span></h1>
          <p class="bls-hero-main">드라이아이스 생산 과정에서 발생하는 리버트 가스(revert gas)를 회수해 다시 액화하고, 펠렛타이저 생산에 재사용합니다. 버려지는 CO<sub>2</sub>를 줄이고 LCO<sub>2</sub> 사용 효율을 높이는 회수·재액화 시스템입니다.</p>
        </div>
        <div class="pel-hero-mask" aria-hidden="true">
          <img src="../../assets/img/coldjet-logo.png" alt="" />
          <span>×</span>
          <img src="../../assets/img/vatek-logo-wordmark.png" alt="" />
        </div>
      </div>
    </section>
  <section class="plt-definition rec-cover tint-hatch" id="what-is-reco2">
    <div class="wrap">
      <div class="plt-head">
        <div><span class="plt-eyebrow">WHAT IS RE-CO2?</span><h2 class="plt-title">버려지던 절반의 CO<sub>2</sub>를,<br>다시 드라이아이스로.</h2></div>
        <p class="plt-lead">펠렛타이저에서 LCO<sub>2</sub>를 대기압으로 낮추면 약 절반은 드라이아이스 스노우가 되고, 나머지 절반은 가스가 되어 배출됩니다. RE-CO2 리커버리 시스템은 이 리버트 가스를 포집해 다시 액화하고, 펠렛타이저로 되돌려 보냅니다.</p>
      </div>
      <div class="bls-showcase-frame reveal">
        <div class="bls-showcase">
          <div class="bls-showcase-body">
            <span class="bls-dot-eyebrow">LCO2-TO-DRY ICE CONVERSION</span>
            <h3>LCO<sub>2</sub> 비용과<br>원료 손실을 줄입니다.</h3>
            <p>리버트 가스를 회수해 다시 생산에 사용하면 드라이아이스 생산에 필요한 LCO<sub>2</sub> 사용량과 비용을 최대 40%까지 줄일 수 있습니다. Cold Jet의 RE-CO<sub>2</sub> 시스템은 필요한 회수 용량과 현장 조건에 맞춰 구성할 수 있으며, Cold Jet 펠렛타이저는 물론 통합 블라스팅 시스템과 대부분의 타사 펠렛타이저에도 연결됩니다.</p>
            <div class="rec-stats">
              <div><strong><span class="rec-count" data-count="40">0</span><i>%</i></strong><span>드라이아이스 생산 비용 절감 (최대)</span></div>
              <div><strong><span class="rec-count" data-count="70">0</span><i>%</i></strong><span>같은 LCO<sub>2</sub>로 더 많은 생산량 (최대 70%)</span></div>
              <div><strong><span class="rec-count" data-count="12">0</span><i>개월</i></strong><span>예상 투자 회수 기간 (조건에 따라 상이)</span></div>
            </div>
          </div>
          <div class="rec-showcase-visual">
            <div class="bls-showcase-media">
              <video id="recShowcaseVideo" class="bls-media-fade" muted loop playsinline preload="auto">
                <source src="../../assets/video/recovery-cost-savings.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="rec-showcase-ctrl">
              <span class="bls-showcase-cap">COLD JET&nbsp;&nbsp;/&nbsp;&nbsp;RE-CO2 RECOVERY</span>
              <button type="button" class="bls-play-btn" id="recShowcasePlayBtn" aria-label="영상 재생">
                <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="plt-section cmp-dark rec-how" id="how-it-works">
    <div class="wrap">
      <div class="plt-head">
        <div><span class="plt-eyebrow">ENGINEERED FOR RELIABILITY</span><h2 class="plt-title">오래, 안정적으로 운전하는 설계.<br>그것이 Cold Jet 리커버리의 품질입니다.</h2></div>
        <p class="plt-lead">RE-CO2는 CO<sub>2</sub>를 회수하는 장비를 넘어, 생산 현장에서 흔들림 없이 운전하도록 설계된 시스템입니다.</p>
      </div>
      <div class="bls-showcase-frame reveal">
        <div class="bls-showcase">
          <div class="bls-showcase-media">
            <video id="recProcessVideo" class="bls-media-fade" muted loop playsinline preload="auto">
              <source src="../../assets/video/recovery-process.mp4" type="video/mp4" />
            </video>
            <span class="bls-showcase-cap">COLD JET&nbsp;&nbsp;/&nbsp;&nbsp;RE-CO2 RECOVERY</span>
            <button type="button" class="bls-play-btn" id="recProcessPlayBtn" aria-label="영상 재생">
              <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
            </button>
          </div>
          <div class="bls-showcase-body">
            <span class="bls-dot-eyebrow">RELIABILITY BY DESIGN</span>
            <h3>회수 장비가 아니라,<br>믿고 맡길 수 있는 운전 시스템입니다.</h3>
            <p>RE-CO2는 제어·냉각·배관·전기 계통까지 하나의 시스템으로 설계해, 생산 현장에서 흔들림 없는 성능을 유지합니다.</p>
            <p>폐회로 구조로 회수된 CO<sub>2</sub>의 품질을 일정하게 유지하고, 강화된 내구성과 원격 진단 기능으로 장기간 안정적인 운전을 지원합니다.</p>
          </div>
        </div>
      </div>
      <div class="plt-reason-grid rec-how-grid">
        <article class="plt-reason"><span class="num">01</span><h3>폐회로 방식의 안정적인 품질</h3><p>외부와 섞이지 않는 폐회로 안에서 재액화되어, 회수된 CO<sub>2</sub>의 품질이 항상 일정합니다.</p></article>
        <article class="plt-reason"><span class="num">02</span><h3>생산과 함께 움직이는 자동 제어</h3><p>펠렛타이저의 PLC·HMI와 연동되어 리커버리 시스템이 유기적으로 운전됩니다.</p></article>
        <article class="plt-reason"><span class="num">03</span><h3>장시간 운전을 견디는 내구 설계</h3><p>배관·구동·전기 계통까지 유지보수성과 내구성을 고려해 현장 운전에 맞게 설계했습니다.</p></article>
        <article class="plt-reason"><span class="num">04</span><h3>환경 대응과 원격 지원</h3><p>고온·실외 설치 조건까지 검증되었고, 원격 진단으로 빠르고 정확하게 대응합니다.</p></article>
      </div>
    </div>
  </section>

  <section class="plt-section" id="why-reco2">
    <div class="wrap">
      <div class="plt-head">
        <div><span class="plt-eyebrow">WHY RE-CO2</span><h2 class="plt-title">같은 LCO2로,<br>더 많은 드라이아이스를 생산합니다.</h2></div>
        <p class="plt-lead">버려지던 CO<sub>2</sub>를 다시 생산에 활용해 원료 손실을 줄이고 생산 효율을 높입니다. 모듈식 구성으로 필요한 규모에서 시작해 확장할 수 있으며, 기존 드라이아이스 생산 설비에도 유연하게 적용할 수 있습니다.</p>
      </div>
      <div class="bls-tech-list">
        <article class="bls-tech reveal">
          <div class="bls-tech-media"><img src="../../assets/img/recovery-hero-official.jpg" alt="Cold Jet RE-CO2 리커버리 유닛과 실내 설치 구성 렌더링" loading="lazy" decoding="async" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">01</span>
            <span class="bls-en">GREATER SUSTAINABILITY</span>
            <h3>CO<sub>2</sub>는 덜 버리고,<br>생산량은 더 높입니다.</h3>
            <p>드라이아이스 생산 중 대기로 배출되던 CO<sub>2</sub>를 회수해 다시 사용합니다. 실제 적용 현장에서는 동일한 양의 LCO<sub>2</sub>로 최대 70% 더 많은 드라이아이스를 생산한 사례도 보고되었습니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal" style="--reveal-delay:0.06s">
          <div class="bls-tech-media"><img src="../../assets/img/recovery-modular-array.jpg" alt="다수의 RE-CO2 모듈형 리커버리 유닛이 나란히 설치된 현장" loading="lazy" decoding="async" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">02</span>
            <span class="bls-en">GREATER VERSATILITY</span>
            <h3>필요한 규모에서 시작하고,<br>생산에 맞춰 확장합니다.</h3>
            <p>모듈식 설계로 생산 규모와 현장 조건에 맞는 리커버리 시스템을 구성할 수 있습니다. 필요한 용량으로 시작한 뒤 생산량이 증가하면 시스템을 단계적으로 확장할 수 있습니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal">
          <div class="bls-tech-media"><img src="../../assets/img/recovery-integration-render.jpg" alt="펠렛타이저 라인에 연결된 RE-CO2 리커버리 시스템 렌더링" loading="lazy" decoding="async" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">03</span>
            <span class="bls-en">GREATER INTEGRATION</span>
            <h3>기존 생산라인에도<br>유연하게 연결됩니다.</h3>
            <p>Cold Jet 펠렛타이저는 물론 다양한 브랜드의 드라이아이스 생산 설비와 연동할 수 있습니다. 설치 공간이 부족한 경우에는 LCO<sub>2</sub> 탱크 인근의 외부 공간에 설치하는 구성도 가능합니다.</p>
          </div>
        </article>
      </div>
      <blockquote class="bls-quote reveal">“CO<sub>2</sub> 비율이 2.4:1에서 1.35:1로 바로 개선됐습니다. 수익, 생산 능력, 회사 전체 성과가 크게 좋아졌습니다.”<cite>Richard Nimmons · Carbon Capture Scotland</cite></blockquote>
    </div>
  </section>

  <section class="plt-section plt-category-select tint-hatch" id="models">
    <div class="wrap">
      <div class="plt-head">
        <div><span class="plt-eyebrow">RE-CO2 LINEUP</span><h2 class="plt-title">펠렛타이저 생산량에 맞춰<br>선택하는 네 가지 용량.</h2></div>
        <p class="plt-lead">시간당 80 kg부터 3,500 kg까지, 함께 운용하는 펠렛타이저의 생산 능력에 맞는 회수 용량을 고릅니다. 모델을 선택하면 상세 사양을 볼 수 있습니다.</p>
      </div>
      <div class="rec-lineup">
        <a class="rec-lineup-item reveal" href="re-co2-80.html">
          <div class="rec-lineup-media"><img src="../../assets/img/recovery-reco2-80-product.jpg" alt="Cold Jet RE-CO2 80" loading="lazy" decoding="async" /></div>
          <div class="rec-lineup-body">
            <span class="plt-category-num">01</span>
            <h3>RE-CO2 80</h3>
            <div class="rec-lineup-spec"><strong>80<i>kg/h</i></strong><span>최대 회수량 · 176 lbs/h</span></div>
            <p>PE 80 펠렛타이저와 짝을 이루는 소규모 자체 생산용 모델입니다.</p>
            <span class="bls-more">모델 상세 보기 <i>→</i></span>
          </div>
        </a>
        <a class="rec-lineup-item reveal" href="re-co2-160.html" style="--reveal-delay:0.06s">
          <div class="rec-lineup-media"><img src="../../assets/img/recovery-reco2-160-product.jpg" alt="Cold Jet RE-CO2 160" loading="lazy" decoding="async" /></div>
          <div class="rec-lineup-body">
            <span class="plt-category-num">02</span>
            <h3>RE-CO2 160</h3>
            <div class="rec-lineup-spec"><strong>160<i>kg/h</i></strong><span>최대 회수량 · 352 lbs/h</span></div>
            <p>PR120H 펠렛타이저와 함께 구성하는 중소 규모 생산 라인용입니다.</p>
            <span class="bls-more">모델 상세 보기 <i>→</i></span>
          </div>
        </a>
        <a class="rec-lineup-item reveal" href="re-co2-320-v2.html" style="--reveal-delay:0.12s">
          <div class="rec-lineup-media"><img src="../../assets/img/recovery-reco2-320-product.jpg" alt="Cold Jet RE-CO2 320 V2" loading="lazy" decoding="async" /></div>
          <div class="rec-lineup-body">
            <span class="plt-category-num">03</span>
            <h3>RE-CO2 320 V2</h3>
            <div class="rec-lineup-spec"><strong>320<i>kg/h</i></strong><span>최대 회수량 · 705 lbs/h</span></div>
            <p>PR350H·PR750H와 짝을 이루는, 원격 지원과 모듈형 확장을 지원하는 중소·중형 생산용 CO<sub>2</sub> 회수 시스템입니다.</p>
            <span class="bls-more">모델 상세 보기 <i>→</i></span>
          </div>
        </a>
        <a class="rec-lineup-item is-wide reveal" href="re-co2-3500.html" style="--reveal-delay:0.18s">
          <div class="rec-lineup-media"><img src="../../assets/img/recovery-reco2-3500-render.jpg" alt="Cold Jet RE-CO2 3500 컨테이너형 설치" loading="lazy" decoding="async" /></div>
          <div class="rec-lineup-body">
            <span class="plt-category-num">04</span>
            <h3>RE-CO2 3500</h3>
            <div class="rec-lineup-spec"><strong>3,500<i>kg/h</i></strong><span>최대 회수량 · 7,716 lbs/h</span></div>
            <p>PR750H 3대 이상을 운용하는 대형 생산 시설을 위한 대용량 CO<sub>2</sub> 회수·재액화 컨테이너형 시스템입니다. CO<sub>2</sub>(R744)를 냉매로 사용해 회수 톤당 에너지 소비를 낮추도록 설계되었습니다.</p>
            <span class="bls-more">모델 상세 보기 <i>→</i></span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <section class="plt-section plt-lineup" id="pairing">
    <div class="wrap">
      <section class="plt-finder" id="reco2-finder" aria-labelledby="recFinderTitle">
        <div class="plt-finder-head">
          <div><span class="plt-eyebrow">WHICH ONE FITS?</span><h2 id="recFinderTitle">내 펠렛타이저에는 어떤 RE-CO2가 맞을까.</h2></div>
          <div class="plt-finder-intro"><p>현재 드라이아이스 생산량과 증설 계획을 선택하세요. 필요한 회수 용량에 맞는 RE-CO2 구성을 바로 확인할 수 있습니다.</p></div>
          <nav class="plt-finder-progress" aria-label="RE-CO2 선택 단계">
            <button type="button" class="is-active" data-rec-step="1"><i>01</i><span>현재 생산량 선택</span><small id="recSummary1">시간당 350kg 미만</small></button>
            <button type="button" data-rec-step="2"><i>02</i><span>증설 계획 선택</span><small id="recSummary2">현재 규모 유지</small></button>
            <button type="button" data-rec-step="3"><i>03</i><span>결과 보기</span></button>
          </nav>
        </div>

        <div class="plt-finder-shell">
          <div class="plt-finder-row">
            <div class="plt-finder-main">
              <form class="plt-finder-form" id="reco2Finder">
                <fieldset class="plt-shape-field is-active" data-rec-field="1">
                  <legend><span>01</span> 운용 중인 펠렛타이저</legend>
                  <div class="plt-shape-options rec-model-options">
                    <label><input type="radio" name="recModel" value="pe80"><span><i class="shape-pe80" aria-hidden="true"></i><b>시간당 80kg 미만</b><small>소규모 자체 생산</small></span></label>
                    <label><input type="radio" name="recModel" value="pr120h"><span><i class="shape-pr120h" aria-hidden="true"></i><b>시간당 120kg 미만</b><small>중소 규모 라인</small></span></label>
                    <label><input type="radio" name="recModel" value="pr350h" checked><span><i class="shape-pr350h" aria-hidden="true"></i><b>시간당 350kg 미만</b><small>중대형 생산</small></span></label>
                    <label><input type="radio" name="recModel" value="pr750h"><span><i class="shape-pr750h" aria-hidden="true"></i><b>시간당 750kg 미만</b><small>대형 생산 시설</small></span></label>
                  </div>
                </fieldset>

                <fieldset class="plt-location-field" data-rec-field="2">
                  <legend><span>02</span> 향후 증설 계획</legend>
                  <div class="plt-binary-options">
                    <label><input type="radio" name="recGrowth" value="keep" checked><span><b>현재 규모 유지</b><small>지금 생산량 기준으로 선정</small></span></label>
                    <label><input type="radio" name="recGrowth" value="grow"><span><b>증설 예정</b><small>희망 추가 생산량 직접 입력</small></span></label>
                  </div>
                  <div class="rec-growth-input" id="recGrowthInputWrap" hidden>
                    <label for="recGrowthAmount">희망 추가 생산량</label>
                    <div class="rec-growth-input-row"><input type="number" id="recGrowthAmount" min="0" step="10" placeholder="예: 80" /><span>kg/h</span></div>
                  </div>
                  <p>RE-CO2는 모듈형 구조로, 유닛을 추가 구성해 회수 용량을 늘릴 수 있습니다.</p>
                </fieldset>

                <fieldset class="plt-location-field rec-summary-field" data-rec-field="3">
                  <legend><span>03</span> 입력 정보 요약</legend>
                  <div class="rec-summary-list" id="recSummaryList"></div>
                </fieldset>
              </form>
            </div>

            <aside class="plt-finder-visual rec-finder-visual" id="recVisual" aria-hidden="true">
              <img id="recVisualImg" src="../../assets/img/recovery-reco2-320-product.jpg" alt="" />
              <span class="plt-finder-visual-caption" id="recVisualCaption">RE-CO2 320 V2</span>
            </aside>
          </div>

          <div class="plt-finder-nav">
            <button type="button" class="plt-step-back" id="recPrev" disabled>이전</button>
            <span><b id="recCurrentStep">1</b> / 3</span>
            <button type="button" class="plt-step-next" id="recNextStep">다음 <i>→</i></button>
          </div>

          <aside class="plt-finder-result" id="recResult" aria-live="polite" hidden>
            <div class="plt-result-top"><span class="plt-result-label">조건에 맞는 추천 구성</span><span class="plt-result-live">실시간 업데이트</span></div>
            <div class="plt-result-row">
              <div class="plt-result-products" id="recProducts" aria-label="추천 제품 구성"></div>
              <span class="plt-result-op is-eq" aria-hidden="true"></span>
              <div class="plt-result-summary"><small id="recType">총 생산량 350 kg/h</small><h3 id="recModel">RE-CO2 320 V2</h3><p id="recReason">입력한 생산량을 충족하는 가장 가까운 회수 용량의 구성입니다.</p></div>
            </div>
            <div class="plt-result-note-box">
              <span class="plt-result-note-title">NOTE</span>
              <p id="recNote">이 결과는 1차 장비 선정을 위한 안내입니다. 용량은 Cold Jet 공식 사양 기준이며, 통합 블라스팅 시스템과 타사 펠렛타이저 연결 여부, 실외 설치와 전기 요건은 현장 조건에 따라 별도로 검토합니다.</p>
              <p id="recNoteTip"></p>
              <div class="plt-result-note-footer"><a class="plt-btn is-small" id="recLink" href="re-co2-320-v2.html">추천 모델 상세 보기 <span>→</span></a></div>
            </div>
          </aside>
        </div>
      </section>
    </div>
  </section>

  <section class="plt-section plt-tech" id="difference">
    <div class="wrap">
      <div class="plt-head">
        <div><span class="plt-eyebrow">THE COLD JET DIFFERENCE</span><h2 class="plt-title hl-title" id="recCompareHlTitle"><span class="plt-hl" style="--hd:0s">같은 리커버리라도,</span><br><span class="plt-hl" style="--hd:.32s">생산 현장에서는 차이가 있습니다.</span></h2></div>
        <p class="plt-lead">일반적인 플랜트형 리커버리 시스템은 대형 중앙 설비 중심으로 구성되는 경우가 많습니다. Cold Jet RE-CO<sub>2</sub>는 드라이아이스 생산 공정과의 연동, 모듈형 확장, 설치 유연성과 유지보수·지원까지 고려해 설계한 리커버리 시스템입니다.</p>
      </div>
    </div>
  </section>

  <div class="plt-compare-freeze rec-compare" id="recCompare">
    <div class="wrap">
      <div class="plt-compare">
        <span class="plt-compare-line" aria-hidden="true"></span>
        <div class="plt-compare-head"><span>비교 시 볼 항목</span><b>일반 리커버리 시스템 검토 시</b><strong>Cold Jet 리커버리 시스템</strong></div>
        <div class="plt-compare-row"><span>설계 방식</span><p>필요 회수 용량과 설치 방식 확인</p><p>모듈형 설계, 필요한 규모에서 시작해 단계적으로 확장 가능</p></div>
        <div class="plt-compare-row"><span>생산라인 연동</span><p>펠렛타이저와의 연결 방식 확인</p><p>펠렛타이저 배출 CO<sub>2</sub>를 회수해 다시 생산라인으로 재공급</p></div>
        <div class="plt-compare-row"><span>설치 공간</span><p>탱크·배관·환기 및 설치 공간 확인</p><p>공간이 부족하면 LCO<sub>2</sub> 탱크 인근 실외 설치 가능</p></div>
        <div class="plt-compare-row"><span>확장성</span><p>향후 증설 방식과 추가 설비 확인</p><p>여러 용량과 모듈식 구성으로 현장 조건에 맞게 선택 가능</p></div>
        <div class="plt-compare-row"><span>유지보수·지원</span><p>서비스 체계와 주요 부품 공급 확인</p><p>V2 기준 원격 트러블슈팅 지원, 유지보수성과 대응성 개선</p></div>
        <div class="plt-compare-row"><span>CO<sub>2</sub> 활용 방식</span><p>회수된 CO<sub>2</sub>의 활용 방식은 시스템 구성에 따라 다름</p><p>회수한 CO<sub>2</sub>를 재액화해 다시 드라이아이스 생산에 사용</p></div>
      </div>
      <p class="plt-compare-note">※ 일반 리커버리 시스템의 사양과 구성은 제조사와 모델에 따라 다릅니다. 실제 비교 시에는 생산 규모, 설치 환경과 공급 조건을 기준으로 확인해야 합니다.</p>
    </div>
  </div>

  <section class="plt-section faq-section" id="faq">
    <div class="wrap">
    <div class="faq-head">
      <h2 style="font-size: 46px; margin: 36px 0 0; padding-top: 20px; color: #000000">자주 묻는 질문 <span class="faq-en" style="font-size: 30px">FAQ</span></h2>
      <p class="faq-intro">Cold Jet이 전 세계 고객에게 가장 많이 받는 CO<sub>2</sub> 리커버리 질문을 정리했습니다.</p>
    </div>
    <div class="faq-list">
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">CO<sub>2</sub> 리커버리 시스템은 무엇이고 어떻게 작동하나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>기존 드라이아이스 생산 설비에 추가하는 장치입니다. 일반 생산 과정에서 사용되지 않고 배출되던 CO<sub>2</sub> 가스를 포집·회수해, 더 많은 드라이아이스를 만드는 데 다시 사용합니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">LCO<sub>2</sub>를 얼마나 절약할 수 있나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>드라이아이스 생산 중 배출되던 LCO<sub>2</sub>를 회수해 최대 40%까지 절약할 수 있습니다. 같은 양의 LCO<sub>2</sub>로 생산량을 늘리는 쪽으로 활용할 수도 있습니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">기존 생산 설비에 연결할 수 있나요? 추가 장비가 필요한가요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>현재 사용 중인 드라이아이스 생산 장비와 매끄럽게 연결되도록 설계되어 있으며, 추가 장비나 개조는 최소한으로 필요합니다. 대부분의 펠렛타이저 브랜드와 호환됩니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">회수한 CO<sub>2</sub>는 LCO<sub>2</sub> 탱크로 돌아가나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>아니요. 재액화된 CO<sub>2</sub>는 밸브를 거쳐 펠렛타이저로 액체를 공급하는 배관에 합류합니다. 가스 공급사는 외부 물질이나 회수 CO<sub>2</sub>를 LCO<sub>2</sub> 탱크에 넣는 것을 엄격히 금지하고 있으며, RE-CO2는 이 규정을 지키면서 고품질 액체 CO<sub>2</sub>를 펠렛타이저에 지속적으로 공급합니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">드라이아이스 품질에 영향이 있나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>없습니다. 회수된 CO<sub>2</sub> 가스는 생산에 사용되는 LCO<sub>2</sub>와 같은 품질이며, 밀폐 순환 구조라 오염 가능성이 없습니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">투자 회수 기간은 어느 정도인가요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>예상 투자 회수 기간입니다. 실제 결과는 LCO<sub>2</sub> 가격, 생산량, 가동 시간과 회수 조건에 따라 달라집니다. 운영은 간단하고 유지보수도 최소한으로, 정기 점검만 권장됩니다.</p></div>
      </details>
    </div>
    </div>
  </section>

  <section class="bls-sec bls-final" id="rec-final">
    <div class="wrap">
      <div class="bls-final-grid">
        <div>
          <span class="cmp-eyebrow">START SAVING</span>
          <h2 class="cmp-h2">지금 배출하는 CO<sub>2</sub>가,<br>내일의 생산량입니다.</h2>
        </div>
        <div>
          <div class="cmp-lead">
            <p>펠렛타이저 모델과 시간당 생산량, 설치 공간만 알려주시면 적합한 RE-CO2 용량과 예상 절감 효과를 계산해 드립니다.</p>
            <p>바테크는 Cold Jet 대한민국 공식 대리점으로 현장 검토부터 설치, 시운전, 교육과 A/S까지 전 과정을 지원합니다.</p>
          </div>
          <div class="cmp-cta-btns">
            <a class="cta-btn" href="../../products/quote.html">절감 효과 상담 요청</a>
            <a class="cmp-btn-ghost" href="../pelletizer/index.html">펠렛타이저 보기</a>
          </div>
          <a class="bls-textlink" href="https://www.coldjet.com/wp-content/uploads/Cold-Jet-Dry-Ice-CO2-Recovery-Systems-20250814-DL.pdf" target="_blank" rel="noopener">Cold Jet RE-CO2 브로슈어 (PDF) →</a>
        </div>
      </div>
    </div>
  </section>


  <!-- ============ GLOBAL TECHNOLOGY · LOCAL SUPPORT ============ -->
  <section class="bls-sec bls-partner last-freeze" id="bls-partner" style="padding-bottom: clamp(200px, 26vh, 320px);">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">GLOBAL TECHNOLOGY · LOCAL SUPPORT</span>
        <h2 class="cmp-h2">장비만큼 중요한 것은,<br>한국에서의 기술 지원입니다.</h2>
      </div>
      <div class="bls-partner-grid">
        <img class="bls-partner-logo reveal" src="../../assets/img/coldjet-logo.png" alt="Cold Jet" />
        <img class="bls-partner-logo reveal" src="../../assets/img/vatek-logo-wordmark.png" alt="VATEK" />

        <div class="bls-partner-name reveal">Cold Jet LLC<span class="bls-partner-tagline">드라이아이스 블라스팅 기술의 개척자이자 글로벌 리더</span></div>
        <div class="bls-partner-name reveal">VATEK Corporation<span class="bls-partner-tagline">Cold Jet 대한민국 공식 총판</span></div>

        <div class="bls-partner-media reveal"><img src="../../assets/img/coldjet-hq-photo-1.jpg" alt="Cold Jet 본사" loading="lazy" decoding="async" /></div>
        <div class="bls-partner-media reveal"><img src="../../assets/img/vatek-building.jpg" alt="바테크 사옥" loading="lazy" decoding="async" /></div>

        <div class="bls-partner-desc reveal"><p>Cold Jet은 현대식 드라이아이스 블라스팅 장비의 원천 특허를 보유한 기술 기업으로, 블라스터 · 드라이아이스 생산설비 · 노즐 · 자동화 솔루션을 개발하고 공급하고 있습니다.</p></div>
        <div class="bls-partner-desc reveal">
          <p>1988년 설립한 바테크는 Cold Jet의 대한민국 공식 총판으로, 제품 공급뿐 아니라 세척 테스트, 렌탈 · 데모, 장비 선정, 설치, 기술지원과 A/S까지 국내 고객의 도입과 운용을 지원합니다.</p>
          <p>바테크는 Cold Jet의 교육, 세미나 및 글로벌 컨퍼런스에 지속적으로 참여해 최신 기술과 적용 사례를 국내 고객 지원에 반영하고 있습니다.</p>
        </div>

        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/coldjet-hq-building.webp" alt="Cold Jet 글로벌 본사" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-2.jpg" alt="Cold Jet 생산 공장" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-3.jpg" alt="Cold Jet 라운지" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-4.jpg" alt="Cold Jet 사내 카페" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-5.webp" alt="Cold Jet 컨퍼런스" loading="lazy" decoding="async" />
        </div>
        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/vatek-coldjet-photo-1.jpg" alt="Cold Jet 본사 방문" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-2.jpg" alt="Cold Jet Asia Dealer Conference" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-3.jpg" alt="Cold Jet 글로벌 딜러 컨퍼런스" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-4.jpg" alt="Cold Jet 세미나 참석" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-5.jpg" alt="Cold Jet R&D 신제품 개발" loading="lazy" decoding="async" />
        </div>

        <div class="bls-partner-divider"></div>
        <div class="bls-partner-divider"></div>

        <ul class="bls-facts">
          <li><b>1986</b><small>현대식 드라이아이스 블라스팅 원천 특허</small></li>
          <li><b>250+</b><small>글로벌 특허</small></li>
          <li><b>3 · 3</b><small>R&amp;D 연구소 · 생산공장</small></li>
          <li><b>14</b><small>기술센터</small></li>
        </ul>
        <ul class="bls-facts is-vatek">
          <li><b>1988</b><small>설립 · 제조업 기반</small></li>
          <li><b>2014</b><small>기업부설연구소 설립 (하남)</small></li>
          <li><b>TEST</b><small>시편 · 내방 · 방문 테스트</small></li>
          <li><b>A/S</b><small>설치 · 교육 · 기술지원</small></li>
        </ul>
      </div>
      <p class="bls-quote reveal">“Cold Jet의 기술과<br>바테크의 국내 현장 경험을 함께 제공합니다.”</p>
    </div>
  </section>"""


def build_recovery(root, nav_html, footer_html, page_shell, asset):
    depth = 2
    extra_head = (
        '\n<link rel="stylesheet" href="%spelletizer-page.css?v=20260914-10" />'
        '\n<link rel="stylesheet" href="%srecovery-page.css?v=20260916-11" />'
    ) % (asset('assets/css/', depth), asset('assets/css/', depth))
    html = page_shell(
        "CO2 리커버리",
        "드라이아이스 생산 중 배출되는 CO2 가스를 회수해 재사용하는 리커버리 시스템입니다. "
        "펠렛타이저 생산능력에 맞춰 4단계 모델을 제공합니다.",
        depth, "products", RECOVERY_BODY, extra_script=RECOVERY_SCRIPT, extra_head=extra_head,
    )
    group_dir = os.path.join(root, "products", "recovery")
    os.makedirs(group_dir, exist_ok=True)
    with open(os.path.join(group_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    for m in RECOVERY_MODELS:
        build_model_page(root, "products", "recovery", "CO2 리커버리", m, RECOVERY_MODELS,
                          nav_html, footer_html, page_shell, asset)
    return 1 + len(RECOVERY_MODELS)
