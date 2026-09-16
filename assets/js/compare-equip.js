(function(){
  var root=document.getElementById('eqf'); if(!root) return;
  var P='../assets/img/';
  var M={
    pcs:{name:'Aero2® PCS ULTRA',cat:'BLASTER · SMART · MICRO PARTICLE + PELLET',img:P+'blaster-aero2-pcs-ultra-white.png',link:'blaster/aero2-ultra.html',why:'0.3–3 mm 사이에서 입자 크기를 설정해 민감한 표면은 부드럽게, 고착 오염은 강하게 다룹니다. 조건을 레시피로 저장해 같은 결과를 반복합니다.'},
    plt:{name:'Aero2® PLT ULTRA',cat:'BLASTER · SMART · PELLET',img:P+'blaster-aero2-plt-ultra-white.png',link:'blaster/aero2-ultra.html',why:'표준 산업 현장의 기준 모델입니다. 3 mm 펠렛으로 금형·설비·이형제를 처리하고, 압력·공급량을 디지털로 저장해 작업자에 따른 편차를 줄입니다.'},
    mc2:{name:'i³ MicroClean® 2',cat:'BLASTER · SMART · MICRO PARTICLE',img:P+'blaster-i3-microclean-2-white.png',link:'blaster/i3-microclean-2.html',why:'단일 호스의 소형 마이크로파티클 블라스터입니다. 전자·의료·식품 설비의 얇은 오염과 미세 형상을 표면 손상 없이 세척하며, 이동과 설치가 간단합니다.'},
    mc1:{name:'i³ MicroClean®',cat:'BLASTER · MICRO PARTICLE · BENCHTOP',img:P+'blaster-i3-microclean-white.png',link:'blaster/i3-microclean.html',why:'드라이아이스 블록을 깎아 분사하는 탁상형 모델로 벤치 작업과 소형 부품에 맞습니다.'},
    a40:{name:'Aero® 40FP',cat:'BLASTER · PELLET',img:P+'blaster-aero-40fp-white.png',link:'blaster/aero-series.html',why:'풀프레셔 펠렛 블라스터의 소형 모델입니다. 단순하고 견고해 일반 세척을 안정적으로 처리합니다.'},
    a80:{name:'Aero® 80FP',cat:'BLASTER · PELLET · HIGH VOLUME',img:P+'blaster-aero-80fp-white.png',link:'blaster/aero-series.html',why:'80 lb 대용량 호퍼로 재충전 없이 오래 작업합니다. 넓은 면적과 교대 작업, 중오염 설비에 맞는 풀프레셔 펠렛 블라스터입니다.'},
    e20:{name:'ELITE 20',cat:'BLASTER · PELLET · ENTRY',img:P+'blaster-elite-20-white.png',link:'blaster/elite20-icerocket.html',why:'전문가급 성능을 갖춘 입문형입니다. 가볍고 좁은 공간과 이동이 잦은 현장, 첫 도입과 세척 서비스에 맞습니다.'},
    ir:{name:'IceRocket',cat:'BLASTER · PELLET · COMPACT',img:P+'blaster-icerocket-plt-white.png',link:'blaster/elite20-icerocket.html',why:'가장 작은 펠렛 블라스터로 소규모·간헐적 작업에 맞습니다.'},
    sdi:{name:'SDI Select™ 60',cat:'BLASTER · MICRO PARTICLE + PELLET',img:P+'blaster-sdi-select-60-white.png',link:'blaster/sdi-select-60.html',why:'더스팅·일반·고압 세 방식을 한 대로 전환하는 범용 모델입니다. 정밀과 일반을 오가는 현장에 대안이 됩니다.'},
    c100:{name:'Aero® C100',cat:'BLASTER · SPECIALTY · PNEUMATIC',img:P+'blaster-c100-white.png',link:'blaster/c100.html',why:'전원 없이 압축공기만으로 작동하는 완전 공압식입니다. 전기 인입이 어렵거나 전기 사용을 피해야 하는 구역에서 유일한 선택입니다.'},
    eco:{name:'E-CO2™ 150',cat:'BLASTER · SPECIALTY · SURFACE PREP',img:P+'blaster-e-co2-150-white.png',link:'blaster/e-co2-150.html',why:'드라이아이스에 연마재를 혼합해 분사합니다. 순수 드라이아이스로는 벗기기 어려운 도막·코팅·부식을 제거하는 표면처리 시스템입니다.'},
    pe80:{name:'PE 80',cat:'PELLETIZER · ENTRY',img:P+'pelletizer-pe80-official.jpg',link:'pelletizer/pe-80.html',why:'시간당 약 80 kg의 3 mm 펠렛을 만드는 소형 모델입니다. 블라스터 한두 대를 운용하는 현장이 배송 없이 신선한 펠렛을 직접 쓰기에 맞습니다.'},
    pr120:{name:'PR120H',cat:'PELLETIZER · R SERIES',img:P+'pelletizer-pr120h-official.jpg',link:'pelletizer/pr120h.html',why:'시간당 약 120 kg. 여러 대의 블라스터 상시 운용이나 소규모 공급을 시작하는 규모에 맞는 R 시리즈의 소형 모델입니다.'},
    pr350:{name:'PR350H',cat:'PELLETIZER · R SERIES',img:P+'pelletizer-pr350h-official.jpg',link:'pelletizer/pr350h.html',why:'시간당 약 350 kg. 지역 공급과 콜드체인 물량을 감당하는 가장 널리 쓰이는 중형 모델입니다.'},
    pr750:{name:'PR750H',cat:'PELLETIZER · R SERIES',img:P+'pelletizer-pr750h-official.jpg',link:'pelletizer/pr750h.html',why:'시간당 약 750 kg. 드라이아이스 판매 사업의 기준 모델로 리포머·슬라이서를 연결해 너겟·블록까지 생산합니다.'},
    pr1500:{name:'PR1500H',cat:'PELLETIZER · R SERIES · INDUSTRIAL',img:P+'pelletizer-pr1500h-official.jpg',link:'pelletizer/pr1500h.html',why:'시간당 약 1,500 kg. 복수 압출 헤드를 갖춘 산업 규모 모델로, 이 규모에서는 CO₂ 리커버리 결합이 원료비를 크게 줄입니다.'},
    forms:{name:'특수 형태 장비 (리포머 · 슬라이서)',cat:'PELLETIZER · SPECIAL FORMS',img:P+'pelletizer-category-reformer.jpg',link:'pelletizer/special-forms.html',why:'펠렛타이저 뒤에 연결해 너겟·블록·슬라이스를 만듭니다. 보냉용 판매까지 하려면 함께 구성합니다.'},
    re80:{name:'RE-CO₂ 80',cat:'CO₂ RECOVERY',img:'',link:'recovery/re-co2-80.html',why:'PE 80·PR120H급 소형 라인의 배출 CO₂를 회수·액화해 다시 생산에 씁니다. 원료비 절감을 시작하는 컴팩트 구성입니다.'},
    re160:{name:'RE-CO₂ 160',cat:'CO₂ RECOVERY',img:'',link:'recovery/re-co2-160.html',why:'PR350H급 중형 라인에 맞는 모듈형 회수기입니다. 라인이 늘면 증설할 수 있습니다.'},
    re320:{name:'RE-CO₂ 320 V2',cat:'CO₂ RECOVERY',img:'',link:'recovery/re-co2-320-v2.html',why:'PR750H급 대형 라인 또는 중형 2대에 맞는 2세대 모델입니다.'},
    re3500:{name:'RE-CO₂ 3500',cat:'CO₂ RECOVERY · PLANT',img:'',link:'recovery/re-co2-3500.html',why:'PR1500H와 복수 라인을 공장 단위로 회수하는 대용량 플랜트형입니다.'},
    combi:{name:'COMBI® PCS® 시리즈',cat:'AUTOMATION · FULLY AUTOMATED',img:P+'auto-combi-pcs-cell.png',link:'automation.html#models',why:'펠렛타이저와 PCS 블라스터를 한 대에 결합해 LCO₂만 공급하면 스스로 드라이아이스를 만들며 분사합니다. 로봇 셀·컨베이어에 연결해 작업자 없이 연속 운전합니다.'},
    asp:{name:'ASP-T',cat:'AUTOMATION · TIRE MOLD',img:P+'auto-asp-t.webp',link:'automation.html#models',why:'KUKA 로봇과 PCS 60을 결합한 타이어 금형 전용 시스템입니다. 가황 프레스 앞에서 14"–22" 금형을 분해 없이 세척합니다.'},
    duct:{name:'DUCT ROBOT',cat:'AUTOMATION · IN-PIPE',img:P+'auto-duct-robot-track.webp',link:'automation.html#models',why:'Ø350–1,350 mm 배관·덕트 안을 주행하며 세척하고 카메라로 기록합니다. 사람이 들어갈 수 없는 내부를 해체 없이 처리합니다.'},
    custom:{name:'맞춤형 자동화 시스템',cat:'AUTOMATION · ENGINEERED BY VATEK',img:P+'auto-vatek-custom.webp',link:'quote.html',why:'표준 시스템으로 해결되지 않는 대상은 공정 설계부터 제작 관리, 설치·시운전까지 바테크가 맞춤 구성합니다.',cta:'자동화 상담하기'},
    buy:{name:'드라이아이스 구매 · 공급',cat:'SUPPLY · PELLET · NUGGET · BLOCK',img:P+'supply-form-block.png',link:'supply.html',why:'장비 없이 필요한 형태와 규격의 드라이아이스를 정기 또는 단건으로 공급받습니다. 용도에 맞는 펠렛·너겟·블록 선택 기준을 안내합니다.',cta:'공급 안내 보기'}
  };
  var L={goal:{clean:'세척',produce:'생산',recover:'CO₂ 회수',automate:'자동화',buy:'구매'},
    clean2:{precision:'정밀·민감 표면',general:'일반 산업 세척',coating:'도막·부식 제거'},
    clean3:{compact:'소형·이동',standard:'표준 현장',heavy:'장시간·대용량',nopower:'공압 전용'},
    produce2:{p80:'~80 kg/h',p120:'~120 kg/h',p350:'~350 kg/h',p750:'~750 kg/h',p1500:'1,000 kg/h+'},
    produce3:{pellet:'펠렛만',forms:'너겟·블록 포함'},
    recover2:{r80:'PE 80·PR120H급',r160:'PR350H급',r320:'PR750H급',r3500:'PR1500H·복수 라인'},
    automate2:{line:'생산라인 통합',tire:'타이어 금형',duct:'배관·덕트',custom:'맞춤 설계'}};
  var NEXT={clean:'실제 오염 샘플로 세척 테스트를 먼저 진행해 입자·압력·노즐을 확정합니다.',produce:'하루 사용량과 LCO₂ 공급 조건, 설치 공간을 확인해 모델과 부속 장비를 확정합니다.',recover:'펠렛타이저 실제 가동 시간과 가스 배출량으로 회수 용량을 산정합니다.',automate:'부품 샘플과 사이클 타임을 검토해 로봇·부스·유틸리티 구성을 제안합니다.',buy:'형태·수량·날짜를 알려주시면 수량 계산과 배송 방법을 안내합니다.'};
  var flow={clean:['clean2','clean3'],produce:['produce2','produce3'],recover:['recover2'],automate:['automate2'],buy:[]};
  function pick(a){
    var g=a.goal;
    if(g==='buy') return {m:M.buy};
    if(g==='automate') return {m:M[{line:'combi',tire:'asp',duct:'duct',custom:'custom'}[a.automate2]], alt: a.automate2==='line'?M.custom:(a.automate2==='custom'?M.combi:null)};
    if(g==='recover') return {m:M[{r80:'re80',r160:'re160',r320:'re320',r3500:'re3500'}[a.recover2]]};
    if(g==='produce'){var k={p80:'pe80',p120:'pr120',p350:'pr350',p750:'pr750',p1500:'pr1500'}[a.produce2]; return {m:M[k], alt:a.produce3==='forms'?M.forms:(k==='pr1500'||k==='pr750'?M[{pr1500:'re3500',pr750:'re320'}[k]]:null)};}
    var s=a.clean2,c=a.clean3;
    if(c==='nopower') return {m:M.c100, alt:s==='coating'?M.eco:null};
    if(s==='coating') return {m:M.eco, alt:M.a80};
    if(s==='precision') return c==='compact'?{m:M.mc2,alt:M.mc1}:{m:M.pcs,alt:M.sdi};
    if(c==='compact') return {m:M.e20,alt:M.ir};
    if(c==='heavy') return {m:M.a80,alt:M.plt};
    return {m:M.plt,alt:M.a40};
  }
  var ans={},hist=[],cur='goal';
  var qs=root.querySelectorAll('.eqf-q'),res=document.getElementById('eqfResult'),prog=root.querySelectorAll('.eqf-progress span');
  var back=document.getElementById('eqfBack'),reset=document.getElementById('eqfReset'),hint=document.getElementById('eqfHint');
  function show(id){
    cur=id; qs.forEach(function(q){q.classList.toggle('is-active',q.dataset.q===id);}); res.classList.toggle('is-active',id==='result');
    var step=id==='goal'?1:(id==='result'?4:(id.slice(-1)==='2'?2:3));
    prog.forEach(function(p,i){var n=i+1;p.classList.toggle('is-active',n===step);p.classList.toggle('is-done',n<step);
      var b=p.querySelector('b');var key=['goal',(ans.goal||'')+'2',(ans.goal||'')+'3'][i];
      b.textContent=(n<step&&ans[key]&&L[key])?L[key][ans[key]]:['하려는 일','대상 · 규모','현장 조건'][i];});
    back.hidden=hist.length===0; reset.hidden=hist.length===0; hint.textContent=id==='result'?'결과는 출발점입니다. 테스트와 상담으로 사양을 확정합니다.':'선택하면 다음 질문으로 넘어갑니다.';
  }
  function render(){
    var r=pick(ans),m=r.m; document.getElementById('eqfName').textContent=m.name; document.getElementById('eqfCat').textContent=m.cat; document.getElementById('eqfWhy').textContent=m.why;
    var lk=document.getElementById('eqfLink'); lk.href=m.link; lk.textContent=m.cta||(m.name+' 상세 보기');
    var md=document.getElementById('eqfMedia'),im=document.getElementById('eqfImg'); if(m.img){md.removeAttribute('data-empty');im.src=m.img;im.alt=m.name;}else{md.setAttribute('data-empty','');im.removeAttribute('src');}
    var alt=document.getElementById('eqfAlt'); if(r.alt){alt.hidden=false;document.getElementById('eqfAltName').textContent=r.alt.name;document.getElementById('eqfAltWhy').textContent=r.alt.why;document.getElementById('eqfAltLink').href=r.alt.link;}else alt.hidden=true;
    document.getElementById('eqfNext').textContent=NEXT[ans.goal];
    var sm=document.getElementById('eqfSummary'); sm.innerHTML=''; Object.keys(ans).forEach(function(k){if(L[k]&&L[k][ans[k]]){var s=document.createElement('span');s.textContent=L[k][ans[k]];sm.appendChild(s);}});
  }
  root.addEventListener('click',function(e){
    var o=e.target.closest('.eqf-opt'); if(!o) return; var q=o.closest('.eqf-q').dataset.q,v=o.dataset.v;
    o.parentNode.querySelectorAll('.eqf-opt').forEach(function(x){x.classList.toggle('is-picked',x===o);});
    ans[q]=v; if(q==='goal'){Object.keys(ans).forEach(function(k){if(k!=='goal')delete ans[k];});}
    hist.push(q); var f=flow[ans.goal],i=f.indexOf(q),nx=q==='goal'?(f[0]||'result'):(f[i+1]||'result');
    if(nx==='result') render(); setTimeout(function(){show(nx);},160);
  });
  back.addEventListener('click',function(){var p=hist.pop(); if(!p) return; delete ans[p]; if(p==='goal'){ans={};} show(p);});
  reset.addEventListener('click',function(){ans={};hist=[];root.querySelectorAll('.eqf-opt').forEach(function(x){x.classList.remove('is-picked');});show('goal');});
  var tabs=document.querySelectorAll('.eqf-tab'),tables=document.querySelectorAll('.eqf-table');
  tabs.forEach(function(t){t.addEventListener('click',function(){tabs.forEach(function(x){x.classList.toggle('is-active',x===t);});tables.forEach(function(x){x.classList.toggle('is-active',x.dataset.t===t.dataset.t);});});});
})();