(function(){
  var root=document.getElementById('eqf'); if(!root) return;
  var P='../assets/img/';
  var M={
    pcs:{name:'Aero2® PCS ULTRA',cat:'BLASTER / SMART / MICRO PARTICLE + PELLET',img:P+'blaster-aero2-pcs-ultra-white.webp',link:'blaster/aero2-ultra.html',why:'0.3–3 mm 사이에서 입자 크기를 설정해 민감한 표면은 부드럽게, 고착 오염은 강하게 다룹니다. 조건을 레시피로 저장해 같은 결과를 반복합니다.'},
    plt:{name:'Aero2® PLT ULTRA',cat:'BLASTER / SMART / PELLET',img:P+'blaster-aero2-plt-ultra-white.webp',link:'blaster/aero2-plt-ultra.html',why:'표준 산업 현장의 기준 모델입니다. 3 mm 펠렛으로 금형, 설비, 이형제를 처리하고, 압력과 공급량을 디지털로 저장해 작업자에 따른 편차를 줄입니다.'},
    mc2:{name:'i³ MicroClean® 2',cat:'BLASTER / SMART / MICRO PARTICLE',img:P+'blaster-i3-microclean-2-white.webp',link:'blaster/i3-microclean-2.html',why:'단일 호스의 소형 마이크로파티클 블라스터입니다. 전자, 의료, 식품 설비의 얇은 오염과 미세 형상을 표면 손상 없이 세척하며, 이동과 설치가 간단합니다.'},
    mc1:{name:'i³ MicroClean®',cat:'BLASTER / MICRO PARTICLE / BENCHTOP',img:P+'blaster-i3-microclean-white.webp',link:'blaster/i3-microclean.html',why:'드라이아이스 블록을 깎아 분사하는 탁상형 모델로 벤치 작업과 소형 부품에 맞습니다.'},
    a40:{name:'Aero® 40FP',cat:'BLASTER / PELLET',img:P+'blaster-aero-40fp-white.webp',link:'blaster/aero-40fp.html',why:'풀프레셔 펠렛 블라스터의 소형 모델입니다. 단순하고 견고해 일반 세척을 안정적으로 처리합니다.'},
    a80:{name:'Aero® 80FP',cat:'BLASTER / PELLET / HIGH VOLUME',img:P+'blaster-aero-80fp-white.webp',link:'blaster/aero-80fp.html',why:'80 lb 대용량 호퍼로 재충전 없이 오래 작업합니다. 넓은 면적과 교대 작업, 중오염 설비에 맞는 풀프레셔 펠렛 블라스터입니다.'},
    e20:{name:'ELITE 20',cat:'BLASTER / PELLET / ENTRY',img:P+'blaster-elite-20-white.webp',link:'blaster/elite-20.html',why:'전문가급 성능을 갖춘 입문형입니다. 가볍고 좁은 공간과 이동이 잦은 현장, 첫 도입과 세척 서비스에 맞습니다.'},
    ir:{name:'IceRocket',cat:'BLASTER / PELLET / COMPACT',img:P+'blaster-icerocket-plt-white.webp',link:'blaster/icerocket-plt.html',why:'가장 작은 펠렛 블라스터로 소규모의 간헐적 작업에 맞습니다.'},
    sdi:{name:'SDI Select™ 60',cat:'BLASTER / MICRO PARTICLE + PELLET',img:P+'blaster-sdi-select-60-white.webp',link:'blaster/sdi-select-60.html',why:'더스팅, 일반, 고압 세 방식을 한 대로 전환하는 범용 모델입니다. 정밀과 일반을 오가는 현장에 대안이 됩니다.'},
    c100:{name:'Aero® C100',cat:'BLASTER / SPECIALTY / PNEUMATIC',img:P+'blaster-c100-white.webp',link:'blaster/c100.html',why:'전원 없이 압축공기만으로 작동하는 완전 공압식입니다. 전기 인입이 어렵거나 전기 사용을 피해야 하는 구역에서 유일한 선택입니다.'},
    eco:{name:'E-CO2™ 150',cat:'BLASTER / SPECIALTY / SURFACE PREP',img:P+'blaster-e-co2-150-white.webp',link:'blaster/e-co2-150.html',why:'드라이아이스에 연마재를 혼합해 분사합니다. 순수 드라이아이스로는 벗기기 어려운 도막, 코팅, 부식을 제거하는 표면처리 시스템입니다.'},
    pe80:{name:'PE 80',cat:'PELLETIZER / ENTRY',img:P+'pelletizer-pe80-official.jpg',link:'pelletizer/pe-80.html',why:'시간당 약 80 kg의 3 mm 펠렛을 만드는 소형 모델입니다. 블라스터 한두 대를 운용하는 현장이 배송 없이 신선한 펠렛을 직접 쓰기에 맞습니다.'},
    pr120:{name:'PR120H',cat:'PELLETIZER / R SERIES',img:P+'pelletizer-pr120h-official.jpg',link:'pelletizer/pr120h.html',why:'시간당 약 120 kg. 여러 대의 블라스터 상시 운용이나 소규모 공급을 시작하는 규모에 맞는 R 시리즈의 소형 모델입니다.'},
    pr350:{name:'PR350H',cat:'PELLETIZER / R SERIES',img:P+'pelletizer-pr350h-official.jpg',link:'pelletizer/pr350h.html',why:'시간당 약 350 kg. 지역 공급과 콜드체인 물량을 감당하는 가장 널리 쓰이는 중형 모델입니다.'},
    pr750:{name:'PR750H',cat:'PELLETIZER / R SERIES',img:P+'pelletizer-pr750h-official.jpg',link:'pelletizer/pr750h.html',why:'시간당 약 750 kg. 드라이아이스 판매 사업의 기준 모델로 리포머와 슬라이서를 연결해 너겟과 블록까지 생산합니다.'},
    pr1500:{name:'PR1500H',cat:'PELLETIZER / R SERIES / INDUSTRIAL',img:P+'pelletizer-pr1500h-official.jpg',link:'pelletizer/pr1500h.html',why:'시간당 약 1,500 kg. 복수 압출 헤드를 갖춘 산업 규모 모델로, 이 규모에서는 CO₂ 리커버리 결합이 원료비를 크게 줄입니다.'},
    forms:{name:'특수 형태 장비 (리포머, 슬라이서)',cat:'PELLETIZER / SPECIAL FORMS',img:P+'pelletizer-category-reformer.jpg',link:'pelletizer/reformer.html',why:'펠렛타이저 뒤에 연결해 너겟, 블록, 슬라이스를 만듭니다. 보냉용 판매까지 하려면 함께 구성합니다.'},
    re80:{name:'RE-CO₂ 80',cat:'CO₂ RECOVERY',img:P+'recovery-reco2-80-product.jpg',link:'recovery/re-co2-80.html',why:'PE 80 / PR120H급 소형 라인의 배출 CO₂를 회수하고 액화해 다시 생산에 씁니다. 원료비 절감을 시작하는 컴팩트 구성입니다.'},
    re160:{name:'RE-CO₂ 160',cat:'CO₂ RECOVERY',img:P+'recovery-reco2-160-product.jpg',link:'recovery/re-co2-160.html',why:'PR350H급 중형 라인에 맞는 모듈형 회수기입니다. 라인이 늘면 증설할 수 있습니다.'},
    re320:{name:'RE-CO₂ 320 V2',cat:'CO₂ RECOVERY',img:P+'recovery-reco2-320-product.jpg',link:'recovery/re-co2-320-v2.html',why:'PR750H급 대형 라인 또는 중형 2대에 맞는 2세대 모델입니다.'},
    re3500:{name:'RE-CO₂ 3500',cat:'CO₂ RECOVERY / PLANT',img:P+'recovery-reco2-3500-render.jpg',link:'recovery/re-co2-3500.html',why:'PR1500H와 복수 라인을 공장 단위로 회수하는 대용량 플랜트형입니다.'},
    combi:{name:'COMBI® PCS® 시리즈',cat:'AUTOMATION / FULLY AUTOMATED',img:P+'auto-combi-pcs-cell.webp',link:'automation.html#models',why:'펠렛타이저와 PCS 블라스터를 한 대에 결합해 LCO₂만 공급하면 스스로 드라이아이스를 만들며 분사합니다. 로봇 셀이나 컨베이어에 연결해 작업자 없이 연속 운전합니다.'},
    asp:{name:'ASP-T',cat:'AUTOMATION / TIRE MOLD',img:P+'auto-asp-t.webp',link:'automation.html#models',why:'KUKA 로봇과 PCS 60을 결합한 타이어 금형 전용 시스템입니다. 가황 프레스 앞에서 14"–22" 금형을 분해 없이 세척합니다.'},
    duct:{name:'DUCT ROBOT',cat:'AUTOMATION / IN-PIPE',img:P+'auto-duct-robot-track.webp',link:'automation.html#models',why:'Ø350–1,350 mm 배관 및 덕트 안을 주행하며 세척하고 카메라로 기록합니다. 사람이 들어갈 수 없는 내부를 해체 없이 처리합니다.'},
    custom:{name:'맞춤형 자동화 시스템',cat:'AUTOMATION / ENGINEERED BY VATEK',img:P+'auto-vatek-custom.webp',link:'quote.html',why:'표준 시스템으로 해결되지 않는 대상은 공정 설계부터 제작 관리, 설치, 시운전까지 바테크가 맞춤 구성합니다.',cta:'자동화 상담하기'},
    buy:{name:'드라이아이스 구매 및 공급',cat:'SUPPLY / PELLET / NUGGET / BLOCK',img:P+'supply-form-block.webp',link:'supply.html',why:'장비 없이 필요한 형태와 규격의 드라이아이스를 정기 또는 단건으로 공급받습니다. 용도에 맞는 펠렛, 너겟, 블록 선택 기준을 안내합니다.',cta:'공급 안내 보기'}
  };
  var L={goal:{clean:'세척',produce:'생산',recover:'CO₂ 회수',automate:'자동화',buy:'구매'},
    clean2:{precision:'정밀, 민감 표면',general:'일반 산업 세척',coating:'도막, 부식 제거'},
    clean3:{compact:'소형, 이동',standard:'표준 현장',heavy:'장시간, 대용량',nopower:'공압 전용'},
    produce2:{p80:'~80 kg/h',p120:'~120 kg/h',p350:'~350 kg/h',p750:'~750 kg/h',p1500:'1,000 kg/h+'},
    produce3:{pellet:'펠렛만',forms:'너겟, 블록 포함'},
    recover2:{r80:'80–120 kg/h 라인',r160:'PR350H급, 350 kg/h',r320:'PR750H급, 750 kg/h',r3500:'PR1500H급, 1,000 kg/h+'},
    automate2:{line:'생산라인 통합',tire:'타이어 금형',duct:'배관 및 덕트',custom:'맞춤 설계'}};
  var NEXT={clean:'실제 오염 샘플로 세척 테스트를 먼저 진행해 입자, 압력, 노즐을 확정합니다.',produce:'하루 사용량과 LCO₂ 공급 조건, 설치 공간을 확인해 모델과 부속 장비를 확정합니다.',recover:'펠렛타이저 실제 가동 시간과 가스 배출량으로 회수 용량을 산정합니다.',automate:'부품 샘플과 사이클 타임을 검토해 로봇, 부스, 유틸리티 구성을 제안합니다.',buy:'형태, 수량, 날짜를 알려주시면 수량 계산과 배송 방법을 안내합니다.'};
  var flow={clean:['clean2','clean3'],produce:['produce2','produce3'],recover:['recover2'],automate:['automate2'],buy:[]};
  var QL={goal:'목적',clean2:'세척 대상',clean3:'현장 조건',produce2:'시간당 생산량',produce3:'생산 형태',recover2:'펠렛타이저 규모',automate2:'자동화 대상'};
  var lastList=null;
  /* (2026-11-10) 추천 v3 — 최대 3가지: 1순위(best) + 함께 검토(also) / 함께 구성(addon).
     원칙 ① 기계 특성이 조건과 맞는 모델이 1순위 (예: 전원 불가 → 공압식 C100, 도막, 부식 → E-CO2, 대용량 → 80 lb 호퍼)
          ② 특성이 맞는 범위에서는 바테크 주력 4종(Aero2 PCS ULTRA / i³ MicroClean 2 / ELITE 20 / IceRocket)을 우선
          ③ 주력 4종은 렌탈 가능 모델 — 결과에 포함될 때만 '렌탈로 먼저 써보기' 버튼 표시
     각 항목: [모델 키, 역할, 이 조건에서의 이유] */
  var RENTAL={pcs:1,mc2:1,e20:1,ir:1};
  var SMALLER='생산량이 그보다 적다면', CUSTOM='표준 시스템으로 맞지 않는 대상이라면', SDI='더스팅, 일반, 고압을 전환해 쓰는 범용기를 원한다면';
  function recs(a){
    var g=a.goal;
    if(g==='buy') return [['buy','best','장비 없이 필요한 만큼만 공급받습니다.'],['pe80','also','사용량이 꾸준해 직접 생산이 유리하다면']];
    if(g==='automate') return {
      line:[['combi','best','생산라인 및 로봇 셀에 연결해 작업자 없이 연속 세척합니다.'],['custom','also',CUSTOM]],
      tire:[['asp','best','가황 프레스 앞에서 금형을 분해하지 않고 세척하는 전용 시스템입니다.'],['custom','also',CUSTOM]],
      duct:[['duct','best','사람이 들어갈 수 없는 배관 및 덕트 내부를 주행하며 세척합니다.'],['custom','also',CUSTOM]],
      custom:[['custom','best','대상과 공정에 맞춰 바테크가 설계부터 시운전까지 구성합니다.'],['combi','also','표준 구성으로 가능한 대상이라면']]}[a.automate2];
    if(g==='recover') return {
      r80:[['re80','best','시간당 80–120 kg급 소형 라인의 배출 가스량에 맞는 용량입니다.'],['re160','also','라인 증설 계획이 있다면']],
      r160:[['re160','best','시간당 350 kg급 중형 라인의 배출 가스량에 맞는 용량입니다.'],['re80','also','가동 시간이 짧거나 배출량이 적다면'],['re320','also','라인 증설 계획이 있다면']],
      r320:[['re320','best','시간당 750 kg급 대형 라인(또는 중형 2대)에 맞는 용량입니다.'],['re160','also','배출량이 그보다 적다면'],['re3500','also','복수 라인을 공장 단위로 회수하려면']],
      r3500:[['re3500','best','시간당 1,000 kg 이상의 라인이나 복수 라인을 공장 단위로 회수합니다.'],['re320','also','라인별로 나눠 회수하려면']]}[a.recover2];
    if(g==='produce'){
      var REC='CO₂ 회수로 원료비를 줄이려면';
      var base={
        p80:[['pe80','best','시간당 약 80 kg — 블라스터 한두 대가 쓰는 양에 맞습니다.'],['pr120','also','사용량이 늘어날 계획이라면']],
        p120:[['pr120','best','시간당 약 120 kg — 여러 대의 블라스터나 소규모 공급에 맞습니다.'],['pe80','also',SMALLER],['pr350','also','공급 물량이 늘어날 계획이라면']],
        p350:[['pr350','best','시간당 약 350 kg — 지역 공급과 콜드체인 물량에 맞습니다.'],['pr120','also',SMALLER],['pr750','also','판매 물량까지 늘릴 계획이라면']],
        p750:[['pr750','best','시간당 약 750 kg — 드라이아이스 판매 사업의 기준 규모입니다.'],['pr350','also',SMALLER],['re320','addon',REC]],
        p1500:[['pr1500','best','시간당 약 1,500 kg — 대규모 공급 허브 규모입니다.'],['pr750','also',SMALLER],['re3500','addon',REC]]}[a.produce2];
      if(a.produce3==='forms') return [base[0],['forms','addon','너겟, 블록, 슬라이스까지 만들려면'],base[base.length-1]];
      return base;
    }
    /* ---- 세척: 표면(clean2) × 현장(clean3) ---- */
    var s=a.clean2,c=a.clean3;
    if(c==='nopower'){ /* 전원 불가 → 공압식 C100이 유일. 전원을 쓸 수 있는 구역용 모델을 함께 안내 */
      if(s==='coating') return [['c100','best','전원 없이 압축공기만으로 작동하는 유일한 모델입니다.'],['eco','also','전원을 쓸 수 있는 구역의 도막, 부식 제거라면']];
      if(s==='precision') return [['c100','best','전원 없이 쓸 수 있는 유일한 모델입니다. 민감한 표면은 세척 테스트로 압력과 노즐 조건을 먼저 확인하세요.'],['mc2','also','전원을 쓸 수 있는 구역의 정밀 세척이라면']];
      return [['c100','best','전원 없이 압축공기만으로 작동하는 유일한 모델입니다.'],['e20','also','전원을 쓸 수 있는 구역의 일반 세척이라면']];
    }
    if(s==='coating'){ /* 도막, 코팅, 부식 → 연마재 혼합 E-CO2가 1순위 */
      var E=['eco','best','드라이아이스에 연마재를 섞어 도막, 코팅, 부식을 벗겨냅니다.'], THIN='드라이아이스만으로 처리할 수 있는 얇은 도막이나 잔류물이라면', STRONG='연마재 없이 강한 펠렛 세척으로 처리할 중오염이라면';
      if(c==='compact') return [E,['e20','also','얇은 도막이나 잔류물 수준이고 이동이 잦다면']];
      if(c==='heavy') return [E,['a80','also',STRONG],['pcs','also',THIN]];
      return [E,['pcs','also',THIN],['a80','also',STRONG]];
    }
    if(s==='precision'){ /* 정밀, 민감 → 미세 입자: 소형은 MicroClean 2, 그 외는 PCS ULTRA */
      if(c==='compact') return [['mc2','best','미세 입자로 민감한 표면을 다루고, 작아서 이동과 설치가 간단합니다.'],['pcs','also','입자 크기를 바꿔 일반 세척까지 한 대로 하려면'],['mc1','also','작업대 위에서 소형 부품만 다룬다면']];
      if(c==='heavy') return [['pcs','best','입자를 0.3 mm까지 줄여 민감한 표면을 다루고, 조건을 저장해 장시간 작업에도 같은 결과를 냅니다.'],['sdi','also',SDI]];
      return [['pcs','best','입자를 0.3 mm까지 줄여 민감한 표면을 다루고, 같은 장비로 일반 세척도 합니다.'],['mc2','also','미세 형상 위주의 정밀 세척이 대부분이라면'],['sdi','also',SDI]];
    }
    /* 일반 산업 세척 */
    if(c==='compact') return [['e20','best','가볍고 이동이 쉬우면서 일반 산업 세척을 전문가급 성능으로 처리합니다.'],['ir','also','더 작은 장비가 필요하거나 압축공기 여유가 적다면'],['a40','also','풀프레셔 펠렛 블라스터가 필요하다면']];
    if(c==='heavy') return [['a80','best','80 lb 대용량 호퍼로 재충전 횟수를 줄여 장시간 작업에 맞습니다.'],['pcs','also','세척 대상이 다양하고 조건을 저장해 반복하려면'],['plt','also','펠렛 세척 조건을 디지털로 관리하려면']];
    return [['pcs','best','3 mm 펠렛 세척부터 민감한 표면까지 한 대로 대응하고, 조건을 저장해 반복합니다.'],['e20','also','첫 도입이거나 도입 비용을 낮추고 싶다면'],['plt','also','3 mm 펠렛 세척만 한다면']];
  }
  /* 다음 단계 버튼 — 결과에 실제로 해당하는 것만 */
  var DEMO=['세척 테스트 신청','../rental/demo.html'], RENT=['렌탈로 먼저 써보기','../rental/vrental.html#fleet'];
  function actions(a,list){
    var g=a.goal, out=[];
    if(g==='clean'){
      out.push(DEMO, ['이 구성으로 견적 요청','quote.html']);
      if(list.some(function(r){return RENTAL[r[0]];})) out.push(RENT);
    } else if(g==='produce'){
      out.push(['생산 시스템 견적 및 상담','quote.html'], ['생산 시스템 자세히 찾기','pelletizer/index.html#model-finder']);
    } else if(g==='recover'){
      out.push(['회수 용량 산정 및 상담 요청','quote.html'], ['리커버리 모델 자세히 보기','recovery/index.html#models']);
    } else if(g==='automate'){
      out.push(['자동화 상담 요청','quote.html']);
      if(a.automate2==='line'||a.automate2==='custom') out.push(['샘플 세척 테스트 신청','../rental/demo.html']);
    } else if(g==='buy'){
      out.push(['드라이아이스 주문 및 견적 문의','quote.html'], ['전화 031-796-4300','tel:0317964300']);
    }
    return out;
  }
  function esc(v){return String(v==null?'':v).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  /* ® ™ 는 사이트 공통 윗첨자(sup.tm)로 */
  function tm(v){return esc(v).replace(/[®™]/g,function(c){return '<sup class="tm">'+c+'</sup>';});}
  /* (2026-11-10) v2 — '다음' 버튼 없이 항목을 누르면 바로 다음 질문으로 이동.
     (이전 버전은 결과 영역의 <p id="eqfNext">와 '다음' 버튼의 id가 겹쳐 버튼이 동작하지 않았음) */
  var ans={},path=['goal'],cur='goal',busy=false;
  var qs=root.querySelectorAll('.eqf-q'),res=document.getElementById('eqfResult');
  var back=document.getElementById('eqfBack'),reset=document.getElementById('eqfReset'),hint=document.getElementById('eqfHint');
  var stepEl=document.getElementById('eqfStep'),chips=document.getElementById('eqfChips'),line=document.getElementById('eqfLine');
  function computeNext(q){var f=flow[ans.goal]||[]; if(q==='goal') return f[0]||'result'; var i=f.indexOf(q); return f[i+1]||'result';}
  function total(){return ans.goal?1+(flow[ans.goal]||[]).length:0;}
  function show(id,dir){
    cur=id;
    root.classList.toggle('is-back',dir==='back');
    qs.forEach(function(q){q.classList.toggle('is-active',q.dataset.q===id);});
    res.classList.toggle('is-active',id==='result');
    root.classList.toggle('is-result',id==='result');
    var idx=path.indexOf(id),n=idx+1,t=total();
    if(id==='result'){ stepEl.innerHTML='<b>추천 결과</b>'; line.style.width='100%'; }
    else { stepEl.innerHTML='<b>질문 '+n+'</b>'+(t?' / '+t:''); line.style.width=(t?((n-1)/t*100):0)+'%'; }
    back.hidden=idx<=0; reset.hidden=idx<=0; if(hint) hint.hidden=id!=='result';
    /* 지금까지 고른 답 — 누르면 그 질문으로 돌아감 */
    chips.innerHTML=idx===0?'<span class="eqf-bar-hint">2~3개의 답변만으로, 적합한 장비와 서비스를 확인할 수 있습니다.</span>':'';
    path.slice(0,idx).forEach(function(k){ if(!L[k]||!L[k][ans[k]]) return;
      var c=document.createElement('button'); c.type='button'; c.className='eqf-chip'; c.textContent=L[k][ans[k]]; c.title='이 선택을 지우고 다시 고르기';
      c.addEventListener('click',function(){ show(k,'back'); }); chips.appendChild(c); });
    /* 현재 질문에서 이미 고른 항목 표시 */
    qs.forEach(function(q){ q.querySelectorAll('.eqf-opt').forEach(function(o){ o.classList.toggle('is-picked',ans[q.dataset.q]===o.dataset.v); }); });
  }
  function render(){
    var list=recs(ans),first=list[0],m=M[first[0]];
    lastList=list;
    document.getElementById('eqfName').innerHTML=tm(m.name); document.getElementById('eqfCat').textContent=m.cat; document.getElementById('eqfWhy').textContent=m.why;
    var note=document.getElementById('eqfNote'); note.hidden=!first[2]; note.textContent=first[2]||'';
    document.getElementById('eqfRent').hidden=!RENTAL[first[0]];
    var lk=document.getElementById('eqfLink'); lk.href=m.link; lk.innerHTML='<span>'+(m.cta?esc(m.cta):(tm(m.name)+' 상세 보기'))+'</span>';
    var md=document.getElementById('eqfMedia'),im=document.getElementById('eqfImg'); if(m.img){md.removeAttribute('data-empty');im.src=m.img;im.alt=m.name;}else{md.setAttribute('data-empty','');im.removeAttribute('src');}
    var more=document.getElementById('eqfMore'),rest=list.slice(1);
    more.innerHTML=rest.map(function(r){ var x=M[r[0]];
      return '<a class="eqf-more" href="'+esc(x.link)+'">'+
        (x.img?'<span class="eqf-more-media"><img src="'+esc(x.img)+'" alt="" loading="lazy"></span>':'')+
        '<span class="eqf-more-body"><span class="eqf-more-tags"><span class="eqf-more-tag'+(r[1]==='addon'?' is-addon':'')+'">'+(r[1]==='addon'?'함께 구성':'함께 검토')+'</span>'+(RENTAL[r[0]]?'<span class="eqf-rent">렌탈 가능</span>':'')+'</span>'+
        '<b>'+tm(x.name)+'</b><span class="eqf-more-note">'+esc(r[2])+'</span><span class="eqf-more-why">'+esc(x.why)+'</span>'+
        '<span class="eqf-more-go">자세히 보기 →</span></span></a>'; }).join('');
    document.getElementById('eqfGrid').classList.toggle('is-single',!rest.length);
    document.getElementById('eqfResultLead').textContent=rest.length?('선택하신 조건에 맞춰 먼저 검토할 장비 '+list.length+'가지입니다.'):'선택하신 조건에 맞는 장비입니다.';
    document.getElementById('eqfNextText').textContent=NEXT[ans.goal];
    var acts=actions(ans,list),ul=document.getElementById('eqfActions');
    ul.innerHTML=acts.map(function(x){return '<li><a href="'+esc(x[1])+'">'+esc(x[0])+'<span>→</span></a></li>';}).join('');
    ul.setAttribute('data-n',acts.length);
  }
  function keepInView(){
    var top=root.getBoundingClientRect().top;
    if(top<70||top>window.innerHeight*0.45){ window.scrollTo({top:window.pageYOffset+top-96,behavior:'smooth'}); }
  }
  root.addEventListener('click',function(e){
    var o=e.target.closest('.eqf-opt'); if(!o||busy) return; var wrap=o.closest('.eqf-q'); if(!wrap) return; var q=wrap.dataset.q;
    wrap.querySelectorAll('.eqf-opt').forEach(function(x){x.classList.toggle('is-picked',x===o);});
    var changed=ans[q]!==o.dataset.v;
    ans[q]=o.dataset.v;
    var idx=path.indexOf(q);
    if(changed){ path.slice(idx+1).forEach(function(k){ delete ans[k]; }); if(q==='goal'){ Object.keys(ans).forEach(function(k){ if(k!=='goal') delete ans[k]; }); } }
    var nx=computeNext(q); path=path.slice(0,idx+1); path.push(nx);
    busy=true;
    setTimeout(function(){ busy=false; if(nx==='result') render(); show(nx,'fwd'); keepInView(); },260);
  });
  back.addEventListener('click',function(){var idx=path.indexOf(cur); if(idx<=0) return; show(path[idx-1],'back');});
  reset.addEventListener('click',function(){ans={};path=['goal'];show('goal','back');keepInView();});
  /* (2026-11-19) 결과 카드 오른쪽 아래의 다시하기, 출력하기 — 다른 찾기 화면과 같은 자리, 같은 결과지(finder-print.js) */
  var again=document.getElementById('eqfAgain'),prt=document.getElementById('eqfPrint');
  if(again) again.addEventListener('click',function(){ans={};path=['goal'];show('goal','back');keepInView();});
  if(prt) prt.addEventListener('click',function(){
    if(!lastList) render();
    var first=lastList[0],m=M[first[0]];
    var conditions=path.filter(function(k){return k!=='result'&&L[k]&&L[k][ans[k]];}).map(function(k){return [QL[k]||k,L[k][ans[k]]];});
    var products=lastList.map(function(r,i){var x=M[r[0]]; return {name:x.name,image:x.img,role:i===0?'1순위 추천':(r[1]==='addon'?'함께 구성':'함께 검토')};});
    var payload={title:'장비 비교, 추천 결과',combine:false,conditions:conditions,products:products,name:m.name,type:m.cat,reason:m.why+(first[2]?' '+first[2]:''),note:NEXT[ans.goal]||'',tip:lastList.length>1?lastList.slice(1).map(function(r){return M[r[0]].name+': '+r[2];}).join(' / '):''};
    window.VatekFinderPrint.run(payload,{button:prt,printPage:'pelletizer/print.html'});
  });
  show('goal');
  var tabs=document.querySelectorAll('.eqf-tab'),tables=document.querySelectorAll('.eqf-table');
  tabs.forEach(function(t){t.addEventListener('click',function(){tabs.forEach(function(x){x.classList.toggle('is-active',x===t);});tables.forEach(function(x){x.classList.toggle('is-active',x.dataset.t===t.dataset.t);});});});
})();