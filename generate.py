# -*- coding: utf-8 -*-
"""
VATEK 홈페이지 리뉴얼 - 정적 사이트 뼈대 생성 스크립트
- 홈페이지(index.html)는 별도의 풍부한 콘텐츠로 직접 작성
- 6개 대메뉴 허브 + 31개 서브메뉴 페이지는 공통 템플릿으로 일괄 생성
"""
import os
import math
import random

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# 0. 실제 제품 콘텐츠 (Cold Jet 공식 웹사이트 coldjet.com 정보를 바탕으로 국문 재구성)
#    스펙 수치는 coldjet.com 공개 자료 기준이며, 정식 계약 전 최신 스펙시트로 재확인이 필요합니다.
# ---------------------------------------------------------------------------

GUIDE_BODY = """
<p>드라이아이스 세척은 고체 이산화탄소(CO<sub>2</sub>) 펠릿 또는 미세 입자를 압축공기로 가속하여 표면의
오염물과 잔류물을 제거하는 산업용 세정 방식입니다. 드라이아이스는 표면과 충돌한 직후 고체에서 기체로
바로 승화하므로, 세정 매체 자체가 2차 잔류물로 남지 않는다는 점이 가장 큰 특징입니다.</p>
<p>모래 · 소다처럼 표면을 깎아내는 연마재 세척과 달리, 드라이아이스 입자는 표면을 마모시키지 않으면서도
강력한 세정력을 낼 수 있어 정밀 부품과 민감한 표면에도 폭넓게 적용됩니다.</p>

<div class="video-embed">
  <iframe src="https://www.youtube.com/embed/jtnrk4n3kDA" title="드라이아이스 세척 소개 영상 (VATEK 유튜브 채널)"
    loading="lazy" referrerpolicy="strict-origin-when-cross-origin"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen></iframe>
</div>
<p class="photo-caption">영상으로 보는 드라이아이스 세척 (출처: VATEK 유튜브 채널)</p>

<h2 style="font-size:20px; margin-top:36px;">세척 원리 — Impact · Cold · Expansion</h2>
<p>드라이아이스 세척의 세정 메커니즘은 아래 세 가지 효과가 결합되어 나타납니다.</p>
<div class="principle-row">
  <div class="principle-card">
    <img src="../assets/img/ice-impact.jpg" alt="Impact 원리" loading="lazy" />
    <h4>① Impact (충격)</h4>
    <p>초음속에 가깝게 가속된 펠릿이 오염층에 운동에너지를 전달해 표면에서 떼어냅니다.</p>
  </div>
  <div class="principle-card">
    <img src="../assets/img/ice-cold.jpg" alt="Cold 원리" loading="lazy" />
    <h4>② Cold (냉각)</h4>
    <p>영하 78.5℃의 저온 충격이 오염물과 기재 사이의 결합력을 급속히 약화시킵니다.</p>
  </div>
  <div class="principle-card">
    <img src="../assets/img/ice-expansion.jpg" alt="Expansion 원리" loading="lazy" />
    <h4>③ Expansion (팽창)</h4>
    <p>펠릿이 순간적으로 승화 · 팽창하며 균열된 오염층을 표면에서 완전히 분리시킵니다.</p>
  </div>
</div>

<h2 style="font-size:20px; margin-top:36px;">핵심 특징</h2>
<div class="icon-row" style="grid-template-columns:repeat(3,1fr);">
  <div class="item"><div class="ic">🛡️</div><span>비마모성 · 표면 손상 위험 낮음</span></div>
  <div class="item"><div class="ic">♻️</div><span>2차 폐기물 없음 (세정 매체 승화)</span></div>
  <div class="item"><div class="ic">🧪</div><span>화학물질 · 폐수 부담 저감</span></div>
  <div class="item"><div class="ic">⚡</div><span>비전도성 · 통전 상태 세척 가능</span></div>
  <div class="item"><div class="ic">🍽️</div><span>식품 등급, 인체에 무해</span></div>
  <div class="item"><div class="ic">⏱️</div><span>분해 최소화로 비가동 시간 단축</span></div>
</div>

<div class="content-photo"><img src="../assets/img/guide-effect-work.jpg" alt="드라이아이스 세척 효과를 보여주는 작업 장면" loading="lazy" /></div>
<p class="photo-caption">세척 전후 차이를 직관적으로 보여주는 작업 현장 사진 (참고: Cold Jet 공식 기술자료 p.13)</p>

<h2 style="font-size:20px; margin-top:36px;">안전 수칙</h2>
<p>드라이아이스 블라스팅 자체는 위험한 작업이 아니지만, 다음 사항은 반드시 지켜야 합니다.</p>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>밀폐 공간 작업 시 충분한 환기를 확보해 CO<sub>2</sub> 농도 상승을 방지합니다.</li>
  <li>장갑 · 보안경 · 청력 보호구 등 개인보호장비(PPE)를 착용합니다.</li>
  <li>CO<sub>2</sub>가 정체될 수 있는 저지대 · 밀폐구역을 사전에 확인하고 표시합니다.</li>
  <li>연속 노출 시간 제한을 준수합니다.</li>
</ul>

<h2 style="font-size:20px; margin-top:36px;">자주 묻는 질문</h2>
<div class="faq-list">
  <details class="faq-item">
    <summary>전자 · 정밀 장비에도 사용할 수 있나요?</summary>
    <p class="faq-a">네. 비전도성 · 비마모성 특성 덕분에 통전 중인 전기 패널이나 정밀 금형에도 널리
    사용됩니다. 다만 장비 민감도에 따라 압력 · 노즐을 조정해야 하므로 사전 테스트를 권장합니다.</p>
  </details>
  <details class="faq-item">
    <summary>세척 후 남는 것이 있나요?</summary>
    <p class="faq-a">드라이아이스 입자는 세척 즉시 기체로 승화하기 때문에 남는 것은 원래 있던
    오염물질뿐입니다. 별도 건조나 폐수 처리가 필요 없습니다.</p>
  </details>
  <details class="faq-item">
    <summary>다른 세척 방식과는 어떻게 다른가요?</summary>
    <p class="faq-a">연마재 · 화학용제 · 고압수 세척 등과의 구체적인 차이는
    <a href="compare.html">타 세척방식과 비교</a> 페이지에서 항목별로 확인하실 수 있습니다.</p>
  </details>
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:18px;">(참고: Cold Jet 공식 기술자료
The Definitive Guide to Dry Ice Blasting 및 coldjet.com)</p>
"""

COMPARE_BODY = """
<div class="hero-photo"><img src="../assets/img/compare-hero.jpg" alt="드라이아이스 블라스팅 작업 장면" loading="lazy" /></div>
<p class="photo-caption">드라이아이스 블라스팅 작업 장면 (참고: Cold Jet 공식 기술자료 p.16)</p>

<p>산업 현장에서 세정 방식을 선정할 때는 제거 성능뿐 아니라 기재의 손상 가능성, 2차 폐기물, 건조 및
폐수 처리, 작업자 안전, 설비 비가동 시간 등을 종합적으로 검토해야 합니다.</p>
<p>드라이아이스 세척은 비마모성 · 건식 · 승화라는 특성 덕분에 이러한 운용 요소를 동시에 단순화할 수
있다는 장점이 있습니다. 특히 기재의 표면 상태를 유지하면서 후처리 공정을 줄여야 하는 환경에서
검토 가치가 높습니다.</p>

<h2 style="font-size:20px; margin-top:32px;">세척 방식 비교표</h2>
<div style="overflow-x:auto;">
<table class="compare-table">
  <tr><th>세척 방식</th><th>기재 영향</th><th>2차 잔류물 · 폐기물</th><th>수분 · 건조</th><th>운영상 특징</th></tr>
  <tr><td><b>드라이아이스 세척</b></td><td class="good">비마모성</td><td class="good">승화되어 잔류하지 않음</td><td class="good">건식</td><td class="good">기재 보호와 후처리 단순화에 유리</td></tr>
  <tr><td>연마 블라스팅</td><td>연마재 종류에 따라 마모 · 요철 발생 가능</td><td>연마재 · 분진 발생</td><td>건식</td><td>표면 변화와 매체 처리 필요</td></tr>
  <tr><td>샌드 블라스팅</td><td>강한 연마작용으로 마모 · 요철 발생 가능</td><td>폐사 · 분진 발생</td><td>건식</td><td>분진 관리와 폐사 처리 필요</td></tr>
  <tr><td>레이저 세정</td><td>조건 설정에 따라 표면 영향 가능</td><td>증기화된 오염물 환기 관리 필요</td><td>건식</td><td>초기 투자와 전문적 운전조건 관리 필요</td></tr>
  <tr><td>수작업 · 화학용제</td><td>반복적 물리 접촉으로 민감 표면 손상 가능</td><td>용제 · 제거 오염물 취급 · 처리 필요</td><td class="bad">습식 · 용제</td><td>작업시간 · 인력 부담, 복잡 형상 접근성 고려 필요</td></tr>
  <tr><td>소다 블라스팅</td><td>비교적 부드러운 연마작용으로 표면 영향 가능</td><td>미세 소다 분말 잔류</td><td>건식</td><td>잔류 분말의 추가 제거 및 관리 필요</td></tr>
  <tr><td>고압 세척</td><td>고압수에 의해 민감 표면 손상 가능성</td><td>오 · 폐수 발생</td><td class="bad">습식</td><td>건조 · 부식 방지, 전기 · 정밀부품 보호 필요</td></tr>
</table>
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:14px;">※ 실제 세정 결과와 적용 가능성은
기재의 재질, 오염물의 종류와 두께, 분사 압력, 입자 크기, 노즐 및 작업 환경에 따라 달라질 수 있으므로
사전 테스트를 통한 조건 확인이 필요합니다.</p>

<h2 style="font-size:20px; margin-top:36px;">방식별 특징 한눈에 보기</h2>
<div class="method-card-grid">
  <div class="method-card"><img src="../assets/img/method-abrasive.jpg" alt="연마 블라스팅" loading="lazy" /><div class="mc-body"><h4>연마 블라스팅</h4><p>유리 · 호두껍질 등 연마재를 사용하며, 매체 종류에 따라 표면 마모나 요철이 발생할 수 있습니다.</p></div></div>
  <div class="method-card"><img src="../assets/img/method-sand.jpg" alt="샌드 블라스팅" loading="lazy" /><div class="mc-body"><h4>샌드 블라스팅</h4><p>강한 연마력으로 두꺼운 오염물 제거에 쓰이지만, 분진과 폐사 처리 부담이 있습니다.</p></div></div>
  <div class="method-card"><img src="../assets/img/method-laser.jpg" alt="레이저 세정" loading="lazy" /><div class="mc-body"><h4>레이저 세정</h4><p>비접촉 방식이지만 초기 장비 투자비가 높고 전문적인 운전 조건 관리가 필요합니다.</p></div></div>
  <div class="method-card"><img src="../assets/img/method-chemical.jpg" alt="수작업 및 화학용제 세정" loading="lazy" /><div class="mc-body"><h4>수작업 · 화학용제</h4><p>복잡한 형상에도 접근할 수 있지만, 반복적인 물리적 접촉과 용제 취급 부담이 있습니다.</p></div></div>
  <div class="method-card"><img src="../assets/img/method-soda.jpg" alt="소다 블라스팅" loading="lazy" /><div class="mc-body"><h4>소다 블라스팅</h4><p>비교적 부드러운 연마 방식이지만, 잔류 분말을 추가로 제거 · 관리해야 합니다.</p></div></div>
  <div class="method-card"><img src="../assets/img/method-highpressure.jpg" alt="고압 세척" loading="lazy" /><div class="mc-body"><h4>고압 세척</h4><p>강력한 세정력을 내지만 폐수가 발생하고, 전기 · 정밀 부품은 별도 보호가 필요합니다.</p></div></div>
</div>

<div class="placeholder-note">
  <b>도입 전 이렇게 확인해보세요</b><br />
  · 실제 시편 또는 부품을 이용한 세정 테스트를 통해 적용성을 확인할 수 있습니다.<br />
  · 오염물, 기재, 작업 조건을 바탕으로 적합한 세정 방식을 함께 검토해 드립니다.
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:18px;">(참고: Cold Jet 공식 기술자료
The Definitive Guide to Dry Ice Blasting 및 coldjet.com)</p>
"""

INDUSTRY_BODY = """
<p>Cold Jet의 드라이아이스 세척은 자동차, 식품, 전자 · 반도체, 고무 · 타이어, 주조, 발전설비 등 전 세계
다양한 산업에서 활용되고 있습니다. 동일한 장비를 사용하더라도 오염물의 성상과 기재 특성에 따라 분사
압력, 드라이아이스 입자 크기, 공급량, 노즐 구성 등 운전 조건을 작업 목적에 맞추어 조정합니다.</p>

<h2 style="font-size:20px; margin-top:32px;">8대 핵심 산업 솔루션</h2>
<div class="sub-grid">
  <div class="sub-card"><h3>자동차 · 모빌리티</h3><p>금형 · 설비 표면 오염 제거, 도장 전처리 및 생산설비 유지보수에 활용됩니다.</p></div>
  <div class="sub-card"><h3>식품 · 포장</h3><p>생산설비 표면의 잔여물 제거 등 분해 없이 건식 세정이 필요한 공정에 적합합니다.</p></div>
  <div class="sub-card"><h3>전자 · 반도체</h3><p>민감한 표면과 전기 · 전자 부품을 세정하며, 화학 세정제 사용을 줄일 수 있습니다.</p></div>
  <div class="sub-card"><h3>고무 · 타이어 · 플라스틱</h3><p>금형 세정, 디플래싱 및 반복적인 유지보수 공정에 사용됩니다.</p></div>
  <div class="sub-card"><h3>주조 · 중공업</h3><p>대형 설비의 표면 오염 및 잔류물 제거, 정기 유지보수 작업에 적용됩니다.</p></div>
  <div class="sub-card"><h3>발전 · 에너지</h3><p>주요 설비의 세정 및 유지보수, 예방 보전 작업에 활용됩니다.</p></div>
  <div class="sub-card"><h3>복원 · 시설관리</h3><p>화재 복구, 곰팡이 제거, 건축물 · 시설 표면의 세정 및 복원에 사용됩니다.</p></div>
  <div class="sub-card"><h3>일반 제조</h3><p>기계 · 금형 · 완제품 표면 세정 및 일반 유지보수 작업에 널리 적용됩니다.</p></div>
</div>

<h2 style="font-size:20px; margin-top:36px;">20개 세부 적용 산업</h2>
<p style="color:var(--text-muted); font-size:14.5px;">Cold Jet 공식 기술자료가 소개하는 세부 적용 산업입니다.</p>
<div class="industry-icon-grid">
  <div class="icon-card"><img src="../assets/img/industry-aerospace.jpg" alt="우주항공" loading="lazy" /><span>우주항공</span></div>
  <div class="icon-card"><img src="../assets/img/industry-automotive.jpg" alt="자동차" loading="lazy" /><span>자동차</span></div>
  <div class="icon-card"><img src="../assets/img/industry-detailing.jpg" alt="세차 · 복원 · 디테일링" loading="lazy" /><span>세차 · 복원 · 디테일링</span></div>
  <div class="icon-card"><img src="../assets/img/industry-cleaning-service.jpg" alt="세정 서비스" loading="lazy" /><span>세정 서비스</span></div>
  <div class="icon-card"><img src="../assets/img/industry-wood.jpg" alt="가공 목재" loading="lazy" /><span>가공 목재</span></div>
  <div class="icon-card"><img src="../assets/img/industry-fire-restoration.jpg" alt="화재 복구" loading="lazy" /><span>화재 복구</span></div>
  <div class="icon-card"><img src="../assets/img/industry-food.jpg" alt="식품산업" loading="lazy" /><span>식품산업</span></div>
  <div class="icon-card"><img src="../assets/img/industry-foundry.jpg" alt="주조(Foundry)" loading="lazy" /><span>주조(Foundry)</span></div>
  <div class="icon-card"><img src="../assets/img/industry-maintenance.jpg" alt="일반 유지보수 · 시설관리" loading="lazy" /><span>일반 유지보수 · 시설관리</span></div>
  <div class="icon-card"><img src="../assets/img/industry-heritage.jpg" alt="문화재 · 건축물 복원" loading="lazy" /><span>문화재 · 건축물 복원</span></div>
  <div class="icon-card"><img src="../assets/img/industry-medical.jpg" alt="의료 장비 제조" loading="lazy" /><span>의료 장비 제조</span></div>
  <div class="icon-card"><img src="../assets/img/industry-mold-removal.jpg" alt="곰팡이 제거" loading="lazy" /><span>곰팡이 제거</span></div>
  <div class="icon-card"><img src="../assets/img/industry-oilgas.jpg" alt="석유 및 가스" loading="lazy" /><span>석유 및 가스</span></div>
  <div class="icon-card"><img src="../assets/img/industry-plastics.jpg" alt="플라스틱 및 복합소재" loading="lazy" /><span>플라스틱 및 복합소재</span></div>
  <div class="icon-card"><img src="../assets/img/industry-packaging.jpg" alt="포장 산업" loading="lazy" /><span>포장 산업</span></div>
  <div class="icon-card"><img src="../assets/img/industry-power.jpg" alt="발전소 설비 · 원자력 제염" loading="lazy" /><span>발전소 설비 · 원자력 제염</span></div>
  <div class="icon-card"><img src="../assets/img/industry-printing.jpg" alt="인쇄" loading="lazy" /><span>인쇄</span></div>
  <div class="icon-card"><img src="../assets/img/industry-rubber-tire.jpg" alt="고무 및 타이어" loading="lazy" /><span>고무 및 타이어</span></div>
  <div class="icon-card"><img src="../assets/img/industry-semiconductor.jpg" alt="반도체" loading="lazy" /><span>반도체</span></div>
  <div class="icon-card"><img src="../assets/img/industry-textile.jpg" alt="섬유 산업" loading="lazy" /><span>섬유 산업</span></div>
</div>

<h2 style="font-size:20px; margin-top:36px;">기술 신뢰도를 높이는 구성 원칙</h2>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>산업별로 오염물의 성상과 기재 특성이 다르므로, 동일한 장비를 사용하더라도 분사 압력 · 입자 크기 ·
  공급량 · 노즐 구성 등 운전 조건을 작업 목적에 맞추어 조정합니다.</li>
  <li>업종명만 나열하기보다 주요 세정 대상 · 적용 목적 · 공정상의 이점을 함께 확인할 수 있도록 안내해
  드립니다.</li>
  <li>현장 테스트, 작업 전후 비교 자료, 기술지원 절차를 통해 실제 적용 가능성을 확인하실 수 있습니다.</li>
</ul>
<div class="placeholder-note">
  <b>바테크가 제공하는 것</b> — 현장 테스트 지원 · 산업별 세정 조건 검토 · 장비 · 드라이아이스 · 운영
  지원의 연계를 통해 장비 판매를 넘어 공정 솔루션을 함께 검토해 드립니다.
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:18px;">(참고: Cold Jet 공식 기술자료
The Definitive Guide to Dry Ice Blasting 및 coldjet.com Industries 자료 기준)</p>
"""

TASK_BODY = """
<p>세척 대상이 아니라 <b>어떤 작업</b>을 하려는지로도 적합한 방식을 찾을 수 있습니다. 표면 세척, 표면
처리 · 전처리, 디버링 · 디플래싱, 설비 유지보수까지 — 작업 목적에 따라 장비 사양보다 먼저 어떤 오염물을
어떤 조건에서 제거할 수 있는지를 확인하는 것이 중요합니다.</p>

<div class="task-card-grid">
  <div class="task-card">
    <div class="tc-photo"><img src="../assets/img/task-surface-food.jpg" alt="표면 세척 - 식품설비" loading="lazy" /><img src="../assets/img/task-surface-industrial.jpg" alt="표면 세척 - 산업설비" loading="lazy" /></div>
    <div class="tc-body">
      <h3>표면 세척</h3>
      <ul>
        <li>기계, 금형, 완제품 표면의 오염물 및 잔류물을 제거합니다.</li>
        <li>압력 · 입자 크기 · 공급량 조정을 통해 세정 강도를 조절할 수 있습니다.</li>
      </ul>
      <a class="tc-link" href="industry.html">관련 산업: 일반 제조 · 식품 →</a>
    </div>
  </div>
  <div class="task-card">
    <div class="tc-photo single"><img src="../assets/img/task-pretreatment.jpg" alt="표면 처리 · 전처리" loading="lazy" /></div>
    <div class="tc-body">
      <h3>표면 처리 · 전처리</h3>
      <ul>
        <li>도장 · 코팅 전 이형제, 윤활유, 먼지 등 표면 오염물을 제거합니다.</li>
        <li>물을 사용하지 않아 별도의 건조 공정을 줄이고 후속 공정과 바로 연계할 수 있습니다.</li>
      </ul>
      <a class="tc-link" href="industry.html">관련 산업: 자동차 · 도장 공정 →</a>
    </div>
  </div>
  <div class="task-card">
    <div class="tc-photo"><img src="../assets/img/task-deburring-precision.jpg" alt="디버링 · 디플래싱 - 정밀부품" loading="lazy" /><img src="../assets/img/task-deburring-plastic.jpg" alt="디버링 · 디플래싱 - 플라스틱부품" loading="lazy" /></div>
    <div class="tc-body">
      <h3>디버링 · 디플래싱</h3>
      <ul>
        <li>부품의 버(burr)와 플래시(flash)를 선택적으로 제거합니다.</li>
        <li>부품의 치수 정밀도와 주요 형상을 유지하는 데 유리합니다.</li>
      </ul>
      <a class="tc-link" href="industry.html">관련 산업: 고무 · 타이어 · 플라스틱 →</a>
    </div>
  </div>
  <div class="task-card">
    <div class="tc-icon">🔧</div>
    <div class="tc-body">
      <h3>설비 유지보수 · 예방보전</h3>
      <ul>
        <li>설비 오염 제거와 정기 세정 · 유지보수 작업에 적용됩니다.</li>
        <li>분해와 반복 수작업을 줄여 유지보수 공정의 효율화에 기여합니다.</li>
      </ul>
      <a class="tc-link" href="industry.html">관련 산업: 발전 · 에너지 →</a>
    </div>
  </div>
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:8px;">(참고: Cold Jet 공식 기술자료
The Definitive Guide to Dry Ice Blasting 및 coldjet.com Applications 자료 기준)</p>
"""

ADOPT_BODY = """
<div class="hero-photo"><img src="../assets/img/adopt-basic-setup.jpg" alt="드라이아이스 블라스터 기본 구성도" loading="lazy" /></div>
<p class="photo-caption">드라이아이스 블라스터 기본 구성 — 블라스터, 압축공기, 드라이아이스 공급 (참고: Cold Jet 공식 기술자료 p.23)</p>

<p>도입 가이드는 기술에 대한 관심을 실제 검토 단계로 전환하는 역할을 합니다. 필요한 인프라와 운전
조건을 미리 확인하면 현장 여건에 맞춰 적용 가능성을 보다 합리적으로 판단할 수 있습니다.</p>

<h2 style="font-size:20px; margin-top:32px;">도입 가이드 핵심 항목</h2>
<table class="spec-table">
  <tr><th>필요한 기본 구성</th><td>드라이아이스 블라스터, 압축공기 공급원, 드라이아이스, 전원, 개인보호장비(PPE)</td></tr>
  <tr><th>장비 선택 기준</th><td>세정 능력, 사용 환경, 장시간 운전 안정성, 안전 장치, 기술지원 및 부품 공급 체계</td></tr>
  <tr><th>드라이아이스 공급</th><td>펠릿과 마이크로파티클의 특성, 공급 방식, 보관 조건, 작업별 사용량 검토</td></tr>
  <tr><th>압축공기 조건</th><td>장비 유형과 작업 조건에 따른 압력 · 유량 요구사항 및 현장 에어 인프라 확인</td></tr>
  <tr><th>안전 가이드</th><td>환기 조건 확인, 제한된 공간에서의 CO<sub>2</sub> 농도 관리, 장갑 · 보안경 · 청력 보호구 등 PPE 착용</td></tr>
</table>

<div class="photo-pair">
  <div class="content-photo"><img src="../assets/img/adopt-lineup.jpg" alt="Cold Jet 드라이아이스 장비 라인업" loading="lazy" /></div>
  <div class="content-photo"><img src="../assets/img/adopt-compressor.jpg" alt="이동식 콤프레서 예시" loading="lazy" /></div>
</div>
<p class="photo-caption">Cold Jet 드라이아이스 장비 라인업(왼쪽)과 이동식 콤프레서 예시(오른쪽) (참고: Cold Jet 공식 기술자료 p.23)</p>

<h2 style="font-size:20px; margin-top:36px;">도입 방식</h2>
<p>Cold Jet 장비를 도입하는 방법에는 여러 옵션이 있습니다. 바테크 상담을 통해 현장에 맞는 방식을
확인하실 수 있습니다.</p>
<table class="compare-table">
  <tr><th>도입 방식</th><th>설명</th></tr>
  <tr><td>신규 구매</td><td>최신 기술이 적용된 신품 장비를 구매합니다.</td></tr>
  <tr><td>평가 프로그램(PEP)</td><td>구매 전 일정 기간 렌탈로 사용해보고, 납입한 렌탈료를 구매 대금에
    반영할 수 있는 방식입니다.</td></tr>
  <tr><td>인증 중고 장비</td><td>정밀 점검 · 수리를 거친 중고 장비를 상대적으로 낮은 비용에 도입합니다.</td></tr>
  <tr><td>금융 · 리스</td><td>분할 납부를 통해 초기 투자 부담을 낮출 수 있습니다.</td></tr>
</table>
<p style="font-size:13px; color:var(--text-muted);">* 위 옵션은 Cold Jet 글로벌 기준이며, 국내 적용 가능 여부와
세부 조건은 바테크 상담을 통해 확인하실 수 있습니다.</p>

<h2 style="font-size:20px; margin-top:36px;">펠릿 vs 마이크로파티클</h2>
<div class="content-photo"><img src="../assets/img/adopt-pellet-vs-micro.jpg" alt="펠릿과 마이크로파티클 비교" loading="lazy" /></div>
<p class="photo-caption">약 3mm 펠릿(왼쪽)과 약 0.3mm 마이크로파티클(오른쪽) 비교 (참고: Cold Jet 공식 기술자료 p.27)</p>
<p>매뉴얼은 약 3&nbsp;mm 펠릿을 고착된 오염물이나 강한 세정력이 필요한 작업에, 약 0.3&nbsp;mm
마이크로파티클을 섬세하고 민감한 표면 세정에 적합한 형태로 설명합니다. 적절한 단열 용기에 보관할 경우
최대 약 1주일간 사용할 수 있으나, 기후와 용기 성능에 따라 하루 약 2~10%가 승화할 수 있으므로 사용
일정에 맞춘 공급 계획이 중요합니다.</p>
<div class="content-photo" style="max-width:380px;"><img src="../assets/img/adopt-pelletizer.jpg" alt="드라이아이스 펠레타이저" loading="lazy" /></div>
<p class="photo-caption">현장에서 직접 생산할 경우 사용하는 드라이아이스 펠레타이저 예시 (참고: Cold Jet 공식 기술자료 p.27)</p>

<h2 style="font-size:20px; margin-top:36px;">압축공기 조건</h2>
<table class="spec-table">
  <tr><th>펠릿 타입</th><td>약 2.8 m³/min(100 CFM), 5.5 bar(80 PSI) 수준</td></tr>
  <tr><th>마이크로파티클 시스템</th><td>약 0.9 m³/min(30 CFM) 수준</td></tr>
</table>
<p style="font-size:13px; color:var(--text-muted);">* 매뉴얼의 일반 기준이며, 실제 요구 조건은 노즐과
세정 대상에 따라 달라질 수 있으므로 현장 확인이 필요합니다.</p>

<h2 style="font-size:20px; margin-top:36px;">안전 가이드</h2>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>작업자는 장갑, 보안경, 청력 보호구 등 적절한 PPE를 착용해야 합니다.</li>
  <li>밀폐되거나 환기가 제한된 공간에서는 환기 시스템과 CO<sub>2</sub> 농도 모니터링을 갖추어야 합니다.</li>
</ul>

<h2 style="font-size:20px; margin-top:36px;">기술 FAQ</h2>
<div class="faq-list">
  <details class="faq-item">
    <summary>어떤 형태의 드라이아이스를 사용하나요?</summary>
    <p class="faq-a">매뉴얼은 약 3mm 펠릿을 고착된 오염물과 강한 세정이 필요한 경우에, 약 0.3mm
    마이크로파티클을 섬세하고 민감한 표면 세정에 적합한 형태로 설명합니다.</p>
  </details>
  <details class="faq-item">
    <summary>드라이아이스는 얼마나 보관할 수 있나요?</summary>
    <p class="faq-a">매뉴얼 기준으로 적절한 단열 용기에 보관할 경우 최대 약 1주일간 사용할 수 있으나,
    기후와 용기 성능에 따라 하루 약 2~10%가 승화할 수 있으므로 사용 일정에 맞춘 공급 계획이
    중요합니다.</p>
  </details>
  <details class="faq-item">
    <summary>압축공기 조건은 어떻게 되나요?</summary>
    <p class="faq-a">매뉴얼의 일반 기준은 펠릿 타입 약 2.8 m³/min(100 CFM), 5.5 bar(80 PSI),
    마이크로파티클 시스템 약 0.9 m³/min(30 CFM) 수준입니다. 실제 요구 조건은 노즐과 세정 대상에 따라
    달라질 수 있으므로 현장 확인이 필요합니다.</p>
  </details>
  <details class="faq-item">
    <summary>안전 운용을 위해 무엇을 확인해야 하나요?</summary>
    <p class="faq-a">작업자는 장갑, 보안경, 청력 보호구 등 적절한 PPE를 착용해야 하며, 밀폐되거나
    환기가 제한된 공간에서는 환기 시스템과 CO<sub>2</sub> 농도 모니터링을 갖추어야 합니다.</p>
  </details>
</div>

<h2 style="font-size:20px; margin-top:36px;">도입 검토 프로세스</h2>
<div class="process-flow">
  <div class="step"><div class="num">1</div><h4>상담</h4><p>오염물 · 기재 · 세정 목표 확인</p></div>
  <div class="step"><div class="num">2</div><h4>테스트</h4><p>시편 또는 현장 테스트</p></div>
  <div class="step"><div class="num">3</div><h4>제안</h4><p>장비 · 노즐 · 운전조건 제안</p></div>
  <div class="step"><div class="num">4</div><h4>도입</h4><p>설치 · 교육 · 운전조건 확인</p></div>
  <div class="step"><div class="num">5</div><h4>운영지원</h4><p>A/S · 소모품 · 드라이아이스 공급</p></div>
</div>

<h2 style="font-size:20px; margin-top:36px;">친환경 공정</h2>
<div class="content-photo"><img src="../assets/img/adopt-carbon-cycle.jpg" alt="탄소 포집·활용 및 친환경 공정 도식" loading="lazy" /></div>
<p class="photo-caption">공장에서 포집된 CO<sub>2</sub>가 드라이아이스로 전환되어 세정에 쓰이는 순환 과정
(참고: Cold Jet 공식 기술자료 p.29)</p>
<p>드라이아이스 세척에 쓰이는 CO<sub>2</sub>는 산업 공정에서 이미 발생한 것을 포집해 재사용한 것으로,
세정 후에는 다시 대기 중으로 승화합니다. 별도로 새롭게 생산해 배출하는 방식이 아니라는 점에서, 화학
세정제나 폐수 처리 부담을 줄이는 공정으로 소개되고 있습니다.</p>

<h2 style="font-size:20px; margin-top:36px;">도입 전 체크리스트</h2>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>세척 대상과 오염물질 종류 파악 (재질, 민감도)</li>
  <li>필요 압축공기 용량 확인 (모델별로 상이)</li>
  <li>작업 공간의 환기 조건 점검</li>
  <li>드라이아이스 공급 방식 결정 (직접 생산 vs 구매)</li>
  <li>데모 테스트로 실제 세척 결과 사전 확인</li>
</ul>
<p>설치 · 시운전 절차는 <a href="../support/install.html">설치/시운전</a> 페이지에서도 확인하실 수 있습니다.</p>
<p style="font-size:13px; color:var(--text-muted); margin-top:18px;">(참고: Cold Jet 공식 기술자료
The Definitive Guide to Dry Ice Blasting 및 coldjet.com)</p>
"""

AUTOMATION_BODY = """
<p>생산 라인에 드라이아이스 세척을 통합하고 싶다면, Cold Jet의 통합 자동화 솔루션을 적용할 수 있습니다.</p>

<h2 style="font-size:20px; margin-top:32px;">COMBI&reg; PCS&reg; — 완전 자동화 솔루션</h2>
<p>업계 최고 수준의 드라이아이스 펠렛타이저와 입자 제어 시스템(PCS)을 하나로 결합한 완전 자동화 장비입니다.
드라이아이스 생산부터 블라스팅까지 중단 없이 연속 운영할 수 있습니다.</p>

<h2 style="font-size:20px; margin-top:32px;">PCS&reg; ULTRA — 반자동화 솔루션</h2>
<p>기존 자동화 생산 설비에 드라이아이스 블라스터를 통합하는 방식으로, 산업용 로봇 시스템과 연동해
라인의 일부 공정으로 편입할 수 있습니다.</p>

<h2 style="font-size:20px; margin-top:32px;">적용 산업</h2>
<div class="chip-grid">
  <span class="chip">항공우주</span><span class="chip">자동차 제조</span>
  <span class="chip">식품 · 음료</span><span class="chip">반도체 · PCB</span>
</div>
<p style="margin-top:18px;">공정별 맞춤 설계와 함께, Cold Jet CONNECT&reg;를 통한 원격 모니터링 · 진단이
제공됩니다. (출처: Cold Jet 공식 웹사이트)</p>
"""

NOZZLE_BODY = """
<p>세척 대상과 작업 조건에 맞춰 다양한 노즐과 액세서리를 조합해 사용할 수 있습니다.</p>
<table class="compare-table">
  <tr><th>구성품</th><th>설명</th></tr>
  <tr><td>노즐(Nozzles)</td><td>세척 강도와 분사 패턴을 결정하는 핵심 부품으로, 용도별 다양한 라인업이 제공됩니다.</td></tr>
  <tr><td>분사기(Applicators)</td><td>작업자의 편의성과 안전성, 조작 단순성을 고려해 설계된 핸들형 분사기구입니다.</td></tr>
  <tr><td>블라스트 호스</td><td>유연하면서도 내구성 있는 에어 · 블라스트 전용 호스입니다.</td></tr>
  <tr><td>예비 부품</td><td>장비 가동률 유지를 위한 각종 교체 부품을 보유하고 있습니다.</td></tr>
</table>
<p style="margin-top:18px;">세척 대상(정밀 전자부품 ~ 대형 산업설비)에 따라 적합한 노즐과 액세서리 구성이
달라지므로, 바테크 상담을 통해 최적 구성을 추천받으실 수 있습니다. (출처: Cold Jet 공식 웹사이트)</p>
"""

_SUPPLY_USES = [
    ("항공사 케이터링", "기내식 보관 · 운송 시 신선도 유지에 사용됩니다."),
    ("콜드체인 관리", "의약품 · 백신 등 온도 민감 물품의 운송 중 온도를 유지합니다."),
    ("식품 배송", "신선식품 배송 시 냉각재로 사용됩니다."),
    ("식품가공 냉각", "식품 처리 시설의 냉각 공정에 직접 활용됩니다."),
    ("생명과학 시료 보관", "의료 · 진단 검체를 저온 상태로 보관 · 운송합니다."),
    ("블라스팅용 원료", "드라이아이스 블라스팅 장비에 투입되는 세척용 미디어입니다."),
    ("재판매용 생산", "타 업체에 판매하기 위한 드라이아이스 생산입니다."),
    ("바이오가스", "바이오가스 업그레이드 과정의 CO2 포집 · 처리에 활용됩니다."),
    ("원격지 생산", "드라이아이스 공급이 어려운 원격 지역에서 현지 생산합니다."),
]
SUPPLY_BODY = """
<p>바테크는 장비뿐 아니라 드라이아이스(소모품) 자체도 정기적으로 공급합니다. 드라이아이스는 세척용
미디어 외에도 다양한 산업에서 활용됩니다.</p>
<div class="sub-grid">
""" + "".join(
    f'<div class="sub-card"><h3>{name}</h3><p>{desc}</p></div>' for name, desc in _SUPPLY_USES
) + """
</div>
<p style="margin-top:18px;">세척용 펠릿 정기 공급부터 냉장 · 냉동이 필요한 물류 · 의약품 운송용
드라이아이스까지, 필요한 형태와 주기에 맞춰 공급해 드립니다. (출처: Cold Jet 공식 웹사이트 참고)</p>
"""

COMPARE_EQUIP_BODY = """
<p>어떤 장비가 적합한지 아래 기준으로 먼저 가늠해보시고, 정확한 추천은 견적문의를 통해 받아보세요.</p>
<table class="compare-table">
  <tr><th>모델</th><th>구분</th><th>이런 현장에 적합</th></tr>
  <tr><td><a href="blaster/aero2-ultra.html">Aero2&reg; ULTRA</a> / <a href="blaster/i3-microclean-2.html">i3 MicroClean&reg; 2</a></td><td>스마트(IoT)</td><td>원격 모니터링 · 데이터 관리가 필요한 스마트팩토리</td></tr>
  <tr><td><a href="blaster/i3-microclean.html">i&sup3; MicroClean&reg;</a></td><td>정밀 · 소형</td><td>전자부품, 정밀금형 등 섬세한 표면</td></tr>
  <tr><td><a href="blaster/sdi-select-60.html">SDI Select&trade; 60</a></td><td>범용</td><td>다양한 산업의 일반적인 온 · 오프 세척</td></tr>
  <tr><td><a href="blaster/aero-series.html">Aero&reg; Series</a></td><td>풀프레셔</td><td>강한 오염물 제거가 필요한 현장</td></tr>
  <tr><td><a href="blaster/elite20-icerocket.html">Elite 20 / IceRocket PLT</a></td><td>입문형</td><td>압축공기 여건이 제한적인 현장, 첫 도입</td></tr>
  <tr><td><a href="blaster/c100.html">C100</a></td><td>완전 공압식</td><td>전원 연결이 어려운 현장</td></tr>
  <tr><td><a href="blaster/e-co2-150.html">E-CO2&trade; 150</a></td><td>연마재 복합</td><td>도장 · 코팅 · 부식 제거 작업</td></tr>
  <tr><td><a href="pelletizer/pe-80.html">PE-80</a></td><td>소용량 생산</td><td>자체 세척용 소량 드라이아이스가 필요한 현장</td></tr>
  <tr><td><a href="pelletizer/pr350h.html">PR350H 이상</a></td><td>대용량 생산</td><td>판매용 또는 대규모 세척 라인 공급</td></tr>
  <tr><td><a href="recovery/index.html">RE-CO2 시리즈</a></td><td>CO2 회수</td><td>드라이아이스 자체 생산량이 많은 현장</td></tr>
</table>
<p style="margin-top:18px;">현장 사진이나 도면, 세척 대상 정보를 <a href="quote.html">견적 요청</a> 시 함께 보내주시면
더 정확하게 추천해 드립니다.</p>
"""

PROCESS_BODY = """
<p>바테크의 장비 구매는 아래 순서로 진행됩니다. 고가 장비인 만큼 대부분의 고객사가 테스트 단계를 거쳐
내부 의사결정을 진행합니다.</p>
<ol style="padding-left:20px; display:grid; gap:14px;">
  <li><b>1. 문의 · 상담</b> — 세척 대상, 오염물질, 현장 조건을 바탕으로 적합한 장비를 안내받습니다.</li>
  <li><b>2. 데모 · 렌탈 테스트</b> — 실제 시료로 세척 테스트를 진행해 효과를 직접 확인합니다.</li>
  <li><b>3. 견적 및 사내 품의</b> — 테스트 결과를 바탕으로 견적을 받아 사내 구매 승인 절차를 진행합니다.</li>
  <li><b>4. 계약 및 도입</b> — 계약 후 설치 · 시운전을 거쳐 현장에 장비를 도입합니다.</li>
  <li><b>5. 사후 지원</b> — 교육, A/S, 소모품 공급 등 도입 이후에도 지속적으로 지원합니다.</li>
</ol>
<p style="margin-top:18px;">신규 구매 외에도 Cold Jet은 평가 프로그램(PEP), 인증 중고 장비, 금융 · 리스 등
다양한 도입 방식을 제공합니다. 국내 적용 조건은 상담 시 안내해 드립니다.</p>
"""

_CASES = [
    ("BÄMM Bakery", "식품 · 음료", "베이커리 생산설비를 물 없이 빠르게 세척"),
    ("자동차 부품 제조업체", "자동차", "드라이아이스 블라스팅을 자동화 라인에 통합해 디버링 공정을 자동화"),
    ("몰타 지역 외주 세척업체", "외주 세척 서비스", "건물 외벽 그래피티(낙서)를 몇 분 만에 제거"),
    ("클래식카 복원업체", "자동차 복원", "원형 손상 없이 표면을 세척해 복원 차량의 진정성을 유지"),
    ("KS Aluminum-Technologie GmbH", "금속 가공", "Werner Fiedler — 사용이 쉽고 신뢰할 수 있는 도입 사례로 평가"),
    ("Progress Casting", "주조(Foundry)", "Daryl Hesch — 예상 투자회수기간 6개월을 실제로는 1개월로 단축"),
    ("Silgan Plastics", "플라스틱", "Joe Pond — 세척 시간 절감과 화학물질 사용 감소를 동시에 달성"),
    ("The Mariners' Museum", "문화재 보존", "Will Hoffman — 문화재 표면 손상 없이 세척 가능함을 검증"),
]
LIBRARY_BODY = """
<p>국내 적용사례는 프로젝트별로 별도 자료로 정리해 안내해 드리며, 아래는 Cold Jet 본사가 공개한
글로벌 적용사례입니다. 바테크는 Cold Jet 대한민국 공식 대리점으로서 동일한 장비와 기술을 국내 현장에
공급합니다.</p>
<div class="sub-grid">
""" + "".join(
    f'<div class="sub-card"><h3>{name}</h3><p><b>{tag}</b><br />{desc}</p></div>' for name, tag, desc in _CASES
) + """
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:18px;">(출처: Cold Jet 공식 웹사이트 Case Studies / 고객 인터뷰)</p>
"""

TESTIMONIALS_BODY = """
<p>아래는 Cold Jet 글로벌 고객들이 남긴 이야기입니다. 정확한 원문 인용이 아닌 요지를 정리한 내용이며,
원문은 Cold Jet 공식 웹사이트에서 확인하실 수 있습니다.</p>
<div class="sub-grid">
  <div class="sub-card"><h3>Werner Fiedler</h3><p>KS Aluminum-Technologie GmbH<br />
    도입이 쉽고 신뢰할 수 있는 세척 방식이라고 평가했습니다.</p></div>
  <div class="sub-card"><h3>Tony Tai</h3><p>글로벌 초콜릿 제조사<br />
    사용자 친화적인 장비로 현장 효율성이 높아졌다고 전했습니다.</p></div>
  <div class="sub-card"><h3>Tom Mendel</h3><p>Performance Plastics<br />
    매일, 모든 교대조에서 장비를 사용하고 있다고 밝혔습니다.</p></div>
  <div class="sub-card"><h3>Daryl Hesch</h3><p>Progress Casting<br />
    예상했던 6개월 투자회수기간이 실제로는 1개월로 단축됐다고 전했습니다.</p></div>
  <div class="sub-card"><h3>Will Hoffman</h3><p>The Mariners' Museum<br />
    문화재 표면에 손상을 주지 않고 세척할 수 있음을 확인했다고 밝혔습니다.</p></div>
  <div class="sub-card"><h3>Joe Pond</h3><p>Silgan Plastics<br />
    세척 시간이 줄고 화학물질 사용량도 함께 감소했다고 전했습니다.</p></div>
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:18px;">(출처: Cold Jet 공식 웹사이트 고객 인터뷰 요약, 국문 재구성)</p>
"""

VRENTAL_BODY = """
<p>V RENTAL은 바테크가 운영하는 드라이아이스 장비 렌탈 프로그램입니다. 장비를 구매하기 전 실제 현장에서
성능을 검증하고 싶거나, 특정 프로젝트 · 성수기에만 한시적으로 장비가 필요한 경우에 활용할 수 있습니다.</p>
<h2 style="font-size:20px; margin-top:32px;">이런 경우에 적합합니다</h2>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>연간 사용 빈도가 낮아 구매보다 렌탈이 경제적인 경우</li>
  <li>특정 프로젝트나 성수기에만 일시적으로 장비가 필요한 경우</li>
  <li>구매 전 현장 적합성을 충분히 검증하고 싶은 경우</li>
  <li>보유 장비의 고장 · 정비 기간 동안 대체 장비가 필요한 경우</li>
</ul>
<p>렌탈 기간, 요금, 재고 현황은 장비 모델과 시점에 따라 달라지므로 <a href="../products/quote.html">견적문의</a>를
통해 안내받으실 수 있습니다.</p>
"""

RECOMMEND_BODY = """
<p>아래 기준으로 구매와 렌탈 중 무엇이 더 적합한지 가늠해보세요.</p>
<table class="compare-table">
  <tr><th>상황</th><th>추천</th></tr>
  <tr><td>연간 가동일이 많고 장기적으로 반복 사용</td><td class="good">구매</td></tr>
  <tr><td>특정 프로젝트 · 성수기에만 일시적으로 필요</td><td class="good">렌탈</td></tr>
  <tr><td>구매 전 현장 적합성 검증이 필요</td><td class="good">렌탈 후 구매 전환 (PEP 방식)</td></tr>
  <tr><td>보유 장비 고장 시 임시 대체가 필요</td><td class="good">단기 렌탈</td></tr>
</table>
<p style="margin-top:18px;">정확히 판단하기 어렵다면 <a href="demo.html">데모 테스트</a>부터 시작해보시는 것을 추천합니다.</p>
"""

DEMO_BODY = """
<p>실제 현장 시료로 세척 테스트를 진행해 도입 전에 효과를 직접 확인할 수 있습니다.</p>
<h2 style="font-size:20px; margin-top:32px;">진행 순서</h2>
<ol style="padding-left:20px; display:grid; gap:10px;">
  <li><b>1. 신청</b> — 세척 대상, 오염물질 종류, 현장 사진을 보내주세요.</li>
  <li><b>2. 사전 검토</b> — 담당자가 적합한 장비와 노즐 구성을 사전에 준비합니다.</li>
  <li><b>3. 테스트 진행</b> — 바테크 시연장 방문 또는 현장 방문을 통해 실제 세척 테스트를 진행합니다.</li>
  <li><b>4. 결과 공유</b> — 테스트 전후 비교와 함께 상세 결과를 안내해 드립니다.</li>
</ol>
<p>테스트에는 현장 조건에 따라 별도 비용이 발생할 수 있으며, 세부 조건은 상담 시 안내해 드립니다.</p>
"""

D_FAQ_BODY = """
<p><b>Q. 데모 테스트는 무료인가요?</b><br />
A. 기본적인 상담과 현장 조건 검토는 무료입니다. 실제 테스트 진행 여부와 비용은 장비 · 현장 조건에 따라
다르므로 상담 시 안내해 드립니다.</p>
<p><b>Q. 렌탈 기간은 얼마나 되나요?</b><br />
A. 단기(일 단위)부터 장기(월 단위)까지 현장 상황에 맞춰 조정할 수 있습니다.</p>
<p><b>Q. 렌탈료를 구매 비용에 반영할 수 있나요?</b><br />
A. 평가 프로그램(PEP) 방식으로 진행하는 경우, 납입한 렌탈료 일부를 이후 구매 대금에 반영할 수 있습니다.
세부 조건은 상담을 통해 확인해 주세요.</p>
"""

VISIT_BODY = """
<p>담당자가 직접 현장을 방문해 세척 대상과 작업 환경을 확인하고, 필요 시 휴대용 장비로 즉석 시연을
진행합니다.</p>
<h2 style="font-size:20px; margin-top:32px;">방문 상담에서 확인하는 것들</h2>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>세척 대상의 재질과 민감도</li>
  <li>현장의 압축공기 · 전원 조건</li>
  <li>환기 및 작업 공간 조건</li>
  <li>필요한 세척 주기와 물량</li>
</ul>
<p>방문 상담 신청은 <a href="../products/quote.html">견적문의</a> 페이지에서 함께 접수하실 수 있습니다.</p>
"""

INSTALL_BODY = """
<p>장비 도입이 결정되면 아래 순서로 설치와 시운전을 진행합니다.</p>
<ol style="padding-left:20px; display:grid; gap:10px;">
  <li><b>1. 현장 사전 점검</b> — 압축공기 용량, 전원, 배치 공간을 확인합니다.</li>
  <li><b>2. 설치</b> — 장비를 반입하고 배관 · 전원을 연결합니다.</li>
  <li><b>3. 시운전</b> — 실제 조건에서 정상 작동 여부를 점검합니다.</li>
  <li><b>4. 운용 교육</b> — 현장 작업자에게 조작법과 안전수칙을 교육합니다.</li>
</ol>
<p>정밀 장비의 경우 사전 현장 조건 확인이 특히 중요하며, 필요한 압축공기 · 전원 사양은 모델별
스펙시트를 기준으로 안내해 드립니다. 모델별 사양은 <a href="../products/blaster/index.html">제품 페이지</a>에서도
확인하실 수 있습니다.</p>
"""

EDUCATION_BODY = """
<p>장비를 안전하고 오래 사용하실 수 있도록 교육과 A/S를 함께 제공합니다.</p>
<h2 style="font-size:20px; margin-top:32px;">운용 교육</h2>
<p>장비 조작법, 노즐 교체, 일상 점검 항목, 안전수칙을 현장 작업자 대상으로 교육합니다.</p>
<h2 style="font-size:20px; margin-top:32px;">A/S 접수</h2>
<p>장비 이상 발생 시 <a href="../products/quote.html">견적문의</a> 페이지 또는 대표 연락처로 접수하시면
담당자가 원인을 확인한 뒤 방문 또는 원격으로 대응합니다.</p>
"""

TECHSUPPORT_BODY = """
<p>세척 결과가 기대에 못 미치거나 특수한 오염물질 대응이 필요한 경우, 기술지원팀이 노즐 · 압력 ·
이송속도 등 세척 조건을 함께 점검해 드립니다.</p>
<h2 style="font-size:20px; margin-top:32px;">지원 범위</h2>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>세척 조건(압력, 노즐, 이송속도) 최적화 상담</li>
  <li>신규 적용 부위에 대한 사전 테스트</li>
  <li>정기 점검 및 소모품(노즐 등) 교체 안내</li>
  <li>장비 이상 진단 및 수리 연계</li>
</ul>
"""

CATALOG_BODY = """
<p>모델별 상세 사양은 <a href="../products/blaster/index.html">드라이아이스 세척기</a>,
<a href="../products/pelletizer/index.html">드라이아이스 제조기</a>, <a href="../products/recovery/index.html">CO2 리커버리</a>
페이지에서 표로 확인하실 수 있습니다. 인쇄용 카탈로그 PDF가 필요하시면
<a href="../products/quote.html">견적문의</a> 시 함께 요청해 주세요.</p>
"""

KNOWLEDGE_BODY = """
<p>드라이아이스 세척의 원리, 산업별 활용, 타 세척방식과의 비교는 아래 페이지에 정리되어 있습니다.</p>
<div class="chip-grid">
  <span class="chip">세척 원리</span><span class="chip">안전 수칙</span>
  <span class="chip">산업별 활용</span><span class="chip">작업별 활용</span>
  <span class="chip">타 세척방식 비교</span><span class="chip">적용사례</span>
</div>
<div class="sub-grid" style="margin-top:20px;">
  <div class="sub-card"><h3>드라이아이스 세척 가이드</h3><p>원리 · 장점 · 안전 · FAQ</p>
    <a class="more" href="../cleaning/guide.html">보러가기 →</a></div>
  <div class="sub-card"><h3>타 세척방식과 비교</h3><p>연마재 · 화학용제 · 고압세척과 비교</p>
    <a class="more" href="../cleaning/compare.html">보러가기 →</a></div>
  <div class="sub-card"><h3>산업별 솔루션</h3><p>18개 산업별 적용 방식</p>
    <a class="more" href="../cleaning/industry.html">보러가기 →</a></div>
  <div class="sub-card"><h3>적용사례 라이브러리</h3><p>Cold Jet 글로벌 적용사례</p>
    <a class="more" href="../cases/library.html">보러가기 →</a></div>
</div>
"""

NEWS_BODY = """
<p>이 페이지에는 바테크의 보도자료, 전시회 참가 소식, 공지사항이 게시됩니다.
새로운 소식이 있을 때 이곳에서 가장 먼저 확인하실 수 있습니다.</p>
"""

ABOUT_BODY = """
<p>주식회사 바테크는 Cold Jet(미국) 대한민국 공식 대리점으로, 드라이아이스 블라스터 · 펠렛타이저 ·
CO2 리커버리 등 관련 장비와 드라이아이스(소모품) 공급을 함께 담당합니다. 기업 고객을 대상으로 한 B2B
공급을 중심으로 하며, 데모 · 렌탈 테스트로 현장 적합성을 검증한 뒤 구매를 진행하는 절차를 지원합니다.</p>
<table class="compare-table">
  <tr><th>항목</th><th>내용</th></tr>
  <tr><td>회사명</td><td>주식회사 바테크 (VATEK Corporation)</td></tr>
  <tr><td>사업분야</td><td>드라이아이스 블라스터 · 펠렛타이저 · CO2 리커버리 공급, 드라이아이스 제조 · 판매</td></tr>
  <tr><td>파트너십</td><td>Cold Jet(미국) 대한민국 공식 대리점</td></tr>
  <tr><td>주요 고객</td><td>기업 구매담당자, 현장 유지보수 책임자 (B2B)</td></tr>
  <tr><td>설립연도</td><td>[입력 필요]</td></tr>
  <tr><td>대표자</td><td>[입력 필요]</td></tr>
  <tr><td>주요 연혁</td><td>[입력 필요]</td></tr>
</table>
"""

PARTNER_BODY = """
<p>바테크는 Cold Jet(미국)의 대한민국 공식 대리점입니다. Cold Jet은 1988년 미국 오하이오주
러벨랜드(Loveland, Ohio)에서 창립된, 드라이아이스 블라스팅 기술을 세계 최초로 상용화한 기업입니다.</p>
<table class="compare-table">
  <tr><th>항목</th><th>내용</th></tr>
  <tr><td>창립</td><td>1988년, 미국 오하이오주 러벨랜드</td></tr>
  <tr><td>원천 특허</td><td>현대적 드라이아이스 블라스팅 장비 원천특허 US 4,617,064 (1986년)</td></tr>
  <tr><td>보유 특허</td><td>250개 이상의 국제 특허</td></tr>
  <tr><td>주요 연혁</td><td>1993년 미국 FAA(연방항공청) 승인 · 2016년 IceTech 인수 ·
    2020년 코로나19 백신 운송용 드라이아이스 생산장비 공급</td></tr>
  <tr><td>글로벌 서비스망</td><td>미국 · 캐나다 · 멕시코 · 벨기에(유럽 본부) · 덴마크 · 독일 · 폴란드 ·
    스페인 · 중국(3개 도시) · 일본 등 11개국 서비스 센터</td></tr>
</table>
<p style="margin-top:18px;">바테크는 이 검증된 기술과 정품 장비를 국내 현장에 가장 가까운 곳에서
공급 · 지원합니다. (출처: Cold Jet 공식 웹사이트 회사소개)</p>
"""

CAPABILITY_BODY = """
<p>바테크는 장비 판매 이후에도 국내에서 직접 대응할 수 있는 체계를 갖추고 있습니다.</p>
<div class="sub-grid">
  <div class="sub-card"><h3>설치 · 시운전</h3><p>현장 조건 점검부터 설치, 시운전까지 지원합니다.</p>
    <a class="more" href="../support/install.html">자세히 보기 →</a></div>
  <div class="sub-card"><h3>운용 교육 · A/S</h3><p>현장 작업자 교육과 A/S 접수 · 대응을 제공합니다.</p>
    <a class="more" href="../support/education.html">자세히 보기 →</a></div>
  <div class="sub-card"><h3>기술지원</h3><p>세척 조건 최적화, 신규 적용 부위 사전 테스트를 지원합니다.</p>
    <a class="more" href="../support/techsupport.html">자세히 보기 →</a></div>
  <div class="sub-card"><h3>소모품 공급</h3><p>드라이아이스, 노즐 등 소모품을 정기적으로 공급합니다.</p>
    <a class="more" href="../products/supply.html">자세히 보기 →</a></div>
</div>
"""

FACILITY_BODY = """
<table class="compare-table">
  <tr><th>항목</th><th>내용</th></tr>
  <tr><td>공식 파트너십</td><td>Cold Jet(미국) 대한민국 공식 대리점</td></tr>
  <tr><td>보유 시설</td><td>[입력 필요]</td></tr>
  <tr><td>보유 인증</td><td>[입력 필요]</td></tr>
  <tr><td>협력 파트너사</td><td>[입력 필요]</td></tr>
</table>
"""

QUOTE_BODY = """
<p>필요한 장비, 세척 대상, 현장 조건(압축공기 · 전원 · 공간)을 알려주시면 담당자가 적합한 모델과
견적을 안내해 드립니다. 판단이 어려우시면 <a href="compare-equip.html">장비 비교·추천받기</a> 또는
<a href="../rental/demo.html">데모 테스트</a>부터 시작하셔도 됩니다.</p>
<h2 style="font-size:20px; margin-top:32px;">문의 시 아래 정보를 함께 보내주시면 더 정확합니다</h2>
<ul style="padding-left:20px; display:grid; gap:8px;">
  <li>세척 대상과 오염물질 종류 (사진이 있으면 더 좋습니다)</li>
  <li>현장의 압축공기 · 전원 조건</li>
  <li>희망하는 도입 시기와 예산 범위</li>
</ul>
<p>담당자 확인 후 1~2영업일 내 연락드립니다.</p>
"""

LOCATION_BODY = """
<table class="compare-table">
  <tr><th>항목</th><th>내용</th></tr>
  <tr><td>주소</td><td>[입력 필요]</td></tr>
  <tr><td>대표전화</td><td>[입력 필요]</td></tr>
  <tr><td>이메일</td><td>[입력 필요]</td></tr>
  <tr><td>사업자등록번호</td><td>[입력 필요]</td></tr>
  <tr><td>오시는 길</td><td>[입력 필요]</td></tr>
</table>
"""

# ---------------------------------------------------------------------------
# 1. 정보구조(IA) 데이터
# ---------------------------------------------------------------------------
MENU = [
    {
        # (2026-09-03, 메가메뉴) 클로드 디자인 핸드오프 요청으로 "세척이란" →
        # "세척가이드"로 개명 — 이 label은 nav_html()/footer_html()/허브
        # 페이지 타이틀·브레드크럼/menu_picker_html() 등 사이트 전역에서
        # 공유되므로 한 곳만 바꾸면 전체에 일괄 반영된다.
        "code": "cleaning", "label": "드라이아이스 세척가이드", "short": "세척이란",
        "tagline": "드라이아이스 블라스팅의 원리와 장점, 우리 현장에 맞는 솔루션을 알아보세요.",
        "nav_eyebrow": "DRY ICE CLEANING",
        "nav_intro": "기술의 원리부터 산업별 적용까지 한눈에 살펴보세요.",
        "subs": [
            {"slug": "guide", "title": "드라이아이스 세척 가이드",
             "desc": "드라이아이스 세척의 원리, 장점, 안전 수칙과 자주 묻는 질문을 한 곳에 정리했습니다.",
             "nav_desc": "원리부터 적용 방법까지, 드라이아이스 세척을 쉽고 명확하게 알아보세요.",
             "nav_img": "assets/img/guide-principle-thumb.jpg",
             "rich_content": True,
             "hero_parallax": True,
             "hero_img": "../assets/img/guide-hero-work.jpg",
             "body": GUIDE_BODY},
            {"slug": "compare", "title": "타 세척방식과 비교",
             "desc": "연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.",
             "nav_desc": "기존 세척 방식과 비교해 드라이아이스 세척만의 차이를 확인하세요.",
             "nav_img": "assets/img/compare-thumb.jpg",
             "rich_content": True,
             "body": COMPARE_BODY},
            {"slug": "industry", "title": "산업별 솔루션",
             "desc": "자동차, 식품, 반도체·PCB, 금형, 인쇄, 발전, 조선 등 산업별로 어떤 문제를 해결하는지 설명합니다.",
             "nav_desc": "자동차·식품·전자 등 산업별 맞춤 세척 솔루션을 안내합니다.",
             "nav_img": "assets/img/industry-thumb.jpg",
             "rich_content": True,
             "body": INDUSTRY_BODY},
            {"slug": "task", "title": "작업별 솔루션",
             "desc": "이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.",
             "nav_desc": "금형 세척부터 표면처리까지, 작업 목적에 맞는 방법을 제안합니다.",
             "nav_img": "assets/img/task-thumb.jpg",
             "rich_content": True,
             "body": TASK_BODY},
            {"slug": "adopt", "title": "도입 가이드",
             "desc": "도입 전 검토사항부터 설치 준비, 운영 체크리스트까지 순서대로 안내합니다.",
             "nav_desc": "도입 검토부터 설치까지, 필요한 절차를 단계별로 안내합니다.",
             "nav_img": "assets/img/adopt-thumb.jpg",
             "rich_content": True,
             "body": ADOPT_BODY},
        ],
    },
    {
        "code": "products", "label": "제품·자동화·공급", "short": "제품",
        "tagline": "세척기부터 제조기, 자동화 시스템, 소모품 공급까지 한 번에 확인하세요.",
        "nav_eyebrow": "PRODUCTS",
        "nav_intro": "세척기부터 제조기, 자동화까지 필요한 장비를 만나보세요.",
        "subs": [
            {"slug": "blaster", "title": "드라이아이스 세척기 (블라스터)",
             "desc": "스마트 · 펠릿 · 마이크로파티클 · 특수 목적, 4개 카테고리 8개 모델 라인업을 소개합니다.",
             "nav_desc": "현장 규모와 작업에 맞는 블라스터 라인업을 소개합니다.",
             "is_group": True},
            {"slug": "pelletizer", "title": "드라이아이스 제조기 (펠렛타이저)",
             "desc": "액체 CO2로 드라이아이스 펠릿을 직접 생산하는 제조 장비를 소개합니다.",
             "nav_desc": "드라이아이스를 직접 생산하는 펠렛타이저를 소개합니다.",
             "is_group": True},
            {"slug": "recovery", "title": "CO2 리커버리",
             "desc": "드라이아이스 생산 중 배출되는 CO2 가스를 회수해 재사용하는 리커버리 시스템을 소개합니다.",
             "nav_desc": "배출 CO2를 회수해 재사용하는 리커버리 장비입니다.",
             "is_group": True},
            {"slug": "automation", "title": "자동화 시스템",
             "desc": "생산 라인에 통합 가능한 자동화 드라이아이스 세척 시스템을 소개합니다.",
             "nav_desc": "생산 라인에 통합되는 자동화 세척 시스템을 안내합니다.",
             "body": AUTOMATION_BODY},
            {"slug": "nozzle", "title": "노즐·액세서리",
             "desc": "작업 목적에 맞는 노즐과 각종 액세서리 구성품을 안내합니다.",
             "nav_desc": "작업 효율을 높이는 다양한 노즐과 액세서리입니다.",
             "body": NOZZLE_BODY},
            {"slug": "supply", "title": "드라이아이스 구매 (소모품 공급 안내)",
             "desc": "장비가 아닌 소모품으로서의 드라이아이스 정기 공급 및 구매 방법을 안내합니다.",
             "nav_desc": "정기 공급부터 단건 구매까지 안내합니다.",
             "body": SUPPLY_BODY},
            {"slug": "compare-equip", "title": "장비 비교·추천받기",
             "desc": "보유 현장 조건을 입력하면 적합한 장비 모델을 비교·추천해 드립니다.",
             "nav_desc": "현장에 맞는 장비를 비교하고 추천받으세요.",
             "body": COMPARE_EQUIP_BODY},
            {"slug": "process", "title": "구매 프로세스 안내",
             "desc": "테스트 → 사내 품의 → 계약으로 이어지는 실제 구매 절차를 단계별로 설명합니다.",
             "nav_desc": "상담부터 설치까지 구매 절차를 안내합니다.",
             "body": PROCESS_BODY},
            {"slug": "quote", "title": "견적 요청",
             "desc": "필요한 장비와 현장 조건을 알려주시면 담당자가 맞춤 견적을 안내해 드립니다.",
             "nav_desc": "필요한 장비의 맞춤 견적을 요청하세요.",
             "body": QUOTE_BODY},
        ],
    },
    {
        "code": "cases", "label": "적용사례", "short": "적용사례",
        "tagline": "다양한 산업 현장에서 검증된 실제 도입 사례를 확인하세요.",
        "nav_eyebrow": "CASE STUDIES",
        "nav_intro": "다양한 산업 현장의 실제 도입 사례를 확인하세요.",
        "subs": [
            {"slug": "library", "title": "적용사례 라이브러리",
             "desc": "산업별·작업별·Before & After 필터로 원하는 적용사례를 빠르게 찾아보세요.",
             "nav_desc": "산업별, 장비별 실제 적용 사례를 모아봤습니다.",
             "body": LIBRARY_BODY},
            {"slug": "testimonials", "title": "고객 후기·추천사",
             "desc": "실제 도입 담당자들이 남긴 사용 후기와 추천의 말을 모았습니다.",
             "nav_desc": "바테크와 함께한 고객들의 이야기를 들어보세요.",
             "body": TESTIMONIALS_BODY},
        ],
    },
    {
        "code": "rental", "label": "렌탈·데모", "short": "렌탈·데모",
        "tagline": "구매 전, 먼저 테스트해보세요. 렌탈과 데모로 적합성을 확인할 수 있습니다.",
        "nav_eyebrow": "RENTAL & DEMO",
        "nav_intro": "구매 전, 실제 현장에서 먼저 성능을 확인해보세요.",
        "subs": [
            {"slug": "vrental", "title": "V RENTAL 안내",
             "desc": "단기·장기로 장비를 빌려 쓸 수 있는 V RENTAL 프로그램을 소개합니다.",
             "nav_desc": "필요한 기간만큼 합리적으로 이용하는 렌탈 서비스입니다.",
             "body": VRENTAL_BODY},
            {"slug": "recommend", "title": "렌탈 추천 상황",
             "desc": "구매보다 렌탈이 더 적합한 현장 상황과 사례를 안내합니다.",
             "nav_desc": "이런 경우라면 렌탈을 추천합니다.",
             "body": RECOMMEND_BODY},
            {"slug": "demo", "title": "데모 테스트 신청",
             "desc": "실제 현장 시료로 세척 테스트를 진행하는 데모 신청 절차를 안내합니다.",
             "nav_desc": "도입 전, 현장에서 직접 성능을 확인해보세요.",
             "body": DEMO_BODY},
            {"slug": "faq", "title": "절차/조건/FAQ",
             "desc": "렌탈·데모 이용 절차와 조건, 자주 묻는 질문을 정리했습니다.",
             "nav_desc": "렌탈 신청 절차와 자주 묻는 질문을 안내합니다.",
             "body": D_FAQ_BODY},
            {"slug": "visit", "title": "방문 시연·상담 신청",
             "desc": "담당자가 직접 현장을 방문해 시연과 상담을 진행하는 일정을 신청할 수 있습니다.",
             "nav_desc": "전문 상담원이 직접 방문해 시연해드립니다.",
             "body": VISIT_BODY},
        ],
    },
    {
        "code": "support", "label": "지원·자료", "short": "지원·자료",
        "tagline": "설치부터 A/S, 기술자료까지 도입 이후 필요한 모든 것을 지원합니다.",
        "nav_eyebrow": "SUPPORT",
        "nav_intro": "설치부터 A/S까지, 도입 이후에도 끝까지 책임집니다.",
        "subs": [
            {"slug": "install", "title": "설치/시운전",
             "desc": "장비 설치와 초기 시운전 과정에서 안내드리는 절차를 소개합니다.",
             "nav_desc": "전문 인력이 설치부터 시운전까지 진행합니다.",
             "body": INSTALL_BODY},
            {"slug": "education", "title": "교육/A·S",
             "desc": "운용 인력 교육 프로그램과 A/S 접수·대응 절차를 안내합니다.",
             "nav_desc": "장비 운용 교육과 사후 관리를 지원합니다.",
             "body": EDUCATION_BODY},
            {"slug": "techsupport", "title": "기술지원 서비스",
             "desc": "현장 문제 해결을 위한 기술지원 서비스 범위와 대응 방식을 소개합니다.",
             "nav_desc": "현장에서 발생하는 문제를 신속하게 해결합니다.",
             "body": TECHSUPPORT_BODY},
            {"slug": "catalog", "title": "카탈로그 다운로드",
             "desc": "제품 카탈로그와 사양서를 PDF로 내려받을 수 있습니다.",
             "nav_desc": "제품별 상세 카탈로그를 내려받으세요.",
             "body": CATALOG_BODY},
            {"slug": "knowledge", "title": "Knowledge Center",
             "desc": "드라이아이스 세척 관련 백서와 업계 트렌드 콘텐츠를 제공합니다.",
             "nav_desc": "드라이아이스 세척 관련 지식 자료를 모았습니다.",
             "body": KNOWLEDGE_BODY},
            {"slug": "news", "title": "공지사항·뉴스",
             "desc": "보도자료, 전시회 참가 소식 등 회사의 최신 소식을 전합니다.",
             "nav_desc": "바테크의 최신 소식을 확인하세요.",
             "body": NEWS_BODY},
        ],
    },
    {
        "code": "company", "label": "회사소개", "short": "VATEK",
        "tagline": "Cold Jet 대한민국 공식 대리점, 바테크를 소개합니다.",
        "nav_eyebrow": "COMPANY",
        "nav_intro": "세계 최초이자 글로벌 리더 Cold Jet의 대한민국 공식 총판입니다.",
        "subs": [
            {"slug": "about", "title": "회사소개",
             "desc": "바테크의 사업 영역과 연혁, 비전을 소개합니다.",
             "nav_desc": "바테크의 비전과 연혁을 소개합니다.",
             "body": ABOUT_BODY},
            {"slug": "partner", "title": "Cold Jet 대한민국 공식 대리점",
             "desc": "세계 1위 드라이아이스 블라스팅 기업 Cold Jet과의 공식 파트너십을 소개합니다.",
             "nav_desc": "Cold Jet과의 파트너십을 소개합니다.",
             "body": PARTNER_BODY},
            {"slug": "capability", "title": "기술·서비스 역량",
             "desc": "설치, 기술지원, A/S로 이어지는 국내 대응 역량을 소개합니다.",
             "nav_desc": "축적된 기술력과 서비스 역량을 소개합니다.",
             "body": CAPABILITY_BODY},
            {"slug": "facility", "title": "시설/인증/파트너",
             "desc": "보유 시설과 인증 현황, 협력 파트너사를 소개합니다.",
             "nav_desc": "생산 시설과 보유 인증, 파트너사를 소개합니다.",
             "body": FACILITY_BODY},
            {"slug": "location", "title": "위치/연락처",
             "desc": "찾아오시는 길과 대표 연락처를 안내합니다.",
             "nav_desc": "오시는 길과 연락처를 안내합니다.",
             "body": LOCATION_BODY},
        ],
    },
]

CODE_ORDER = [m["code"] for m in MENU]

def find_menu(code):
    return next(m for m in MENU if m["code"] == code)


# ---------------------------------------------------------------------------
# 2. 공통 partial: head / nav / footer
# ---------------------------------------------------------------------------

def asset(path, depth):
    prefix = "../" * depth
    return prefix + path


def megamenu_html(m, depth):
    # (2026-09-03) 클로드 디자인 핸드오프(handoff_megamenu) 적용 — 기존
    # 카드형 .dropdown(호버 시 서브메뉴만 작게 뜨는 방식)을 화면 전체
    # 가로폭을 쓰는 4단 풀와이드 메가메뉴로 교체. 정적으로 넘겨받은
    # megamenu-nav.html.txt는 루트 기준 상대경로(예: "cleaning/index.html")로
    # 고정돼 있어 그대로 쓰면 depth가 있는 하위 페이지(예:
    # products/blaster/index.html)에서 링크가 깨지므로, 기존 nav_html()과
    # 동일하게 MENU 데이터 + asset(path, depth)로 매 페이지마다 올바른
    # 상대경로를 계산해 동적으로 생성한다. 서브메뉴 항목의 슬라이딩
    # 하이라이트/미리보기 이미지 교체/우측 설명 갱신은 assets/js/main.js
    # 하단에 그대로 이식한 megamenu JS가 담당(여긴 초기 HTML만 구성).
    index_items = []
    for i, s in enumerate(m["subs"]):
        active = " is-active" if i == 0 else ""
        href = asset(m["code"] + "/" + s["slug"] + ("/index.html" if s.get("is_group") else ".html"), depth)
        img_attr = f' data-img="{asset(s["nav_img"], depth)}"' if s.get("nav_img") else ""
        index_items.append(
            f'<li class="megamenu-index-item{active}" data-i="{i}">'
            f'<a href="{href}" data-desc="{s["nav_desc"]}"{img_attr}>{s["title"]}</a>'
            f'</li>'
        )
    first = m["subs"][0]
    first_href = asset(m["code"] + "/" + first["slug"] + ("/index.html" if first.get("is_group") else ".html"), depth)
    if first.get("nav_img"):
        preview = (
            f'<div class="megamenu-preview-img is-active" data-i="0">'
            f'<div class="megamenu-preview-img-bg is-shown" style="background-image:url(\'{asset(first["nav_img"], depth)}\')"></div>'
            f'</div>'
        )
    else:
        preview = f'<div class="megamenu-preview-img img-ph is-active" data-i="0">{first["title"]}</div>'
    return f"""<div class="megamenu">
    <div class="megamenu-inner">
      <div class="megamenu-intro">
        <span class="megamenu-eyebrow">{m["nav_eyebrow"]}</span>
        <h3>{m["label"]}</h3>
        <p>{m["nav_intro"]}</p>
      </div>
      <div class="megamenu-index">
        <span class="megamenu-index-label">MENU INDEX</span>
        <ul class="megamenu-index-list">
          <span class="megamenu-index-highlight" aria-hidden="true"></span>
          {''.join(index_items)}
        </ul>
      </div>
      <div class="megamenu-preview">
        {preview}
      </div>
      <div class="megamenu-detail">
        <span class="megamenu-detail-title">{first["title"]}</span>
        <p class="megamenu-detail-desc">{first["nav_desc"]}</p>
        <a class="megamenu-detail-link" href="{first_href}">자세히 보기 →</a>
      </div>
    </div>
  </div>"""


def nav_html(depth, active_code=None):
    items = []
    for m in MENU:
        li_active = " active" if m["code"] == active_code else ""
        hub_href = asset(f"{m['code']}/index.html", depth)
        items.append(
            f'<li class="{li_active.strip()}">'
            f'<a href="{hub_href}">{m["label"]}<span class="nav-chevron" aria-hidden="true"></span></a>'
            f'{megamenu_html(m, depth)}'
            f'</li>'
        )
    quote_href = asset("products/quote.html", depth)
    return f"""
  <header class="site-header">
    <div class="header-bar">
      <a class="logo" href="{asset('index.html', depth)}"><img class="logo-img" src="{asset('assets/img/vatek-logo.png', depth)}" alt="VATEK" /></a>
      <nav class="main-nav">
        <ul>{''.join(items)}</ul>
      </nav>
      <div class="header-right">
        <a class="cta-btn" href="{quote_href}">문의</a>
        <button class="nav-toggle" aria-label="메뉴 열기">☰</button>
        <img class="coldjet-badge" src="{asset('assets/img/coldjet-logo.png', depth)}" alt="Cold Jet" />
      </div>
    </div>
  </header>
"""


def footer_html(depth):
    # footer는 4칸 그리드(브랜드 1 + 카테고리 3)이므로 6개 대메뉴 중 대표 3개만
    # 노출하고 나머지는 위 홈 하단 "메뉴 선택" 카드 섹션(menu_picker_html)에서
    # 전부 다룬다.
    # (2026-09-02, 후속9) 사용자 요청 — 홈의 새 "메뉴 선택" 카드 섹션처럼 푸터도
    # 등장할 때 효과가 있으면 좋겠다는 요청. footer_html()은 57개 페이지 전체가
    # 공유하는 공통 partial이라, 여기 붙인 리빌 클래스는 홈뿐 아니라 사이트
    # 전체 페이지의 푸터에 똑같이 적용된다(어차피 스크롤 리빌 관찰자
    # assets/js/main.js가 클래스 유무만으로 전 페이지에서 동일하게 동작하므로
    # 별도 분기 불필요). 브랜드 영역 → 3개 카테고리 컬럼(인덱스 순 0.08초씩
    # 지연) 순서로 나타나도록 지연을 늦춘다. 맨 아래 저작권 바(.footer-bottom)는
    # 리빌 효과를 주지 않고 항상 그대로 보이게 둠 — 이 바는 페이지의 진짜
    # 마지막 요소라 "화면 하단 8% 안쪽은 아직 등장 전으로 치는" 관찰자
    # rootMargin(-8%) 규칙상, 문서 끝까지 스크롤해도 이 짧은 바(수십 px)는
    # 그 8% 구간을 넘어 올라올 수 없어 is-visible이 영원히 붙지 않고
    # opacity:0로 사라져 보이는 문제가 실제로 발생함(다른 리빌 요소는 아래에
    # 더 콘텐츠가 있어 스크롤로 8% 구간 위로 밀어올릴 수 있지만, 문서의 맨
    # 마지막 요소는 구조적으로 불가능). 그래서 이 요소만 리빌 대상에서 제외.
    cols = []
    for i, m in enumerate(MENU[:3]):
        links = "".join(
            f'<li><a href="{asset(m["code"] + "/" + s["slug"] + ("/index.html" if s.get("is_group") else ".html"), depth)}">{s["title"]}</a></li>'
            for s in m["subs"][:4]
        )
        delay = 0.06 + i * 0.08
        cols.append(f'<div class="footer-col reveal-pop" style="--reveal-delay:{delay:.2f}s"><h4>{m["label"]}</h4><ul>{links}</ul></div>')
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-top">
        <div class="footer-brand reveal">
          <a class="logo" href="{asset('index.html', depth)}">VATEK<span class="dot"></span></a>
          <p>주식회사 바테크 | 드라이아이스 블라스터·펠렛타이저·리커버리 및 관련 소모품 공급</p>
          <p>[사업자등록번호 입력] · [주소 입력]</p>
          <span class="partner-badge">🧊 Cold Jet 대한민국 공식 대리점</span>
        </div>
        {''.join(cols)}
      </div>
      <div class="footer-bottom">
        <span>© VATEK Corporation. All rights reserved. (본 페이지는 리뉴얼 시안이며 실제 배포용이 아닙니다)</span>
        <span>[대표전화 입력] · [이메일 입력]</span>
      </div>
    </div>
  </footer>
  <script src="{asset('assets/js/main.js', depth)}"></script>
"""


# (후속70) 사용자 요청: "임팩트 인트로(에너지 파티클+로고+플래시)는 최초 접속
# 때만 나오고, 그 다음부터 로고·홈 버튼을 눌러 홈에 다시 올 때는 그 인트로 없이
# 영상·헤더·본문 텍스트가 순서 없이 한 번에 나와야 한다" — 정적 사이트라 서버가
# "몇 번째 방문인지" 알 수 없으므로, 브라우저 localStorage에 방문 여부를 남겨
# 판별한다. CSS 애니메이션이 그리기 직전에 바로 시작되므로(레이스 없이) 이
# 판별 스크립트는 반드시 <head> 최상단, 스타일시트보다도 먼저 동기(sync,
# defer/async 없음)로 실행되어야 함 — 늦게 실행되면 인트로가 잠깐 보였다가
# 사라지는 깜빡임이 생김. 처음 방문(localStorage에 기록 없음)이면 플래그만
# 남기고 그대로 두어 인트로가 정상 재생되고, 이미 기록이 있으면 <html>에
# no-hero-intro 클래스를 붙여 style.css의 관련 애니메이션을 전부 끈다(아래
# .no-hero-intro 규칙 참고 — prefers-reduced-motion과 동일한 "즉시 전부 표시"
# 방식 재사용).
INTRO_GATE_SCRIPT = """<script>
(function () {
  try {
    if (localStorage.getItem('vatekIntroSeen')) {
      document.documentElement.classList.add('no-hero-intro');
    } else {
      localStorage.setItem('vatekIntroSeen', '1');
    }
  } catch (e) {}
})();
</script>
"""


def page_shell(title, description, depth, active_code, body, is_home=False):
    body_class = ' class="home"' if is_home else ""
    intro_gate = INTRO_GATE_SCRIPT if is_home else ""
    return f"""<!doctype html>
<html lang="ko">
<head>
{intro_gate}<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} | VATEK</title>
<meta name="description" content="{description}" />
<link rel="stylesheet" href="{asset('assets/css/style.css', depth)}" />
</head>
<body{body_class}>
{nav_html(depth, active_code)}
{body}
{footer_html(depth)}
</body>
</html>
"""


# ---------------------------------------------------------------------------
# 3. 허브 페이지 (대메뉴 index) 생성
# ---------------------------------------------------------------------------

def build_hub_page(m):
    depth = 1
    cards = ""
    for s in m["subs"]:
        href = f"{s['slug']}/index.html" if s.get("is_group") else f"{s['slug']}.html"
        cards += f"""
        <div class="sub-card">
          <h3>{s['title']}</h3>
          <p>{s['desc']}</p>
          <a class="more" href="{href}">자세히 보기 →</a>
        </div>"""
    body = f"""
  <div class="wrap breadcrumb"><a href="../index.html">홈</a> &gt; {m['label']}</div>
  <section class="page-hero" style="padding-top:24px;">
    <div class="wrap">
      <span class="cat">{m['short']}</span>
      <h1>{m['label']}</h1>
      <p>{m['tagline']}</p>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="sub-grid">{cards}</div>
      <div class="cta-band">
        <div>
          <h3>더 궁금한 점이 있으신가요?</h3>
          <p>현장 조건을 알려주시면 담당자가 1:1로 안내해 드립니다.</p>
        </div>
        <a class="cta-btn" href="../products/quote.html">견적문의 하기</a>
      </div>
    </div>
  </section>
"""
    html = page_shell(m["label"], m["tagline"], depth, m["code"], body)
    with open(os.path.join(ROOT, m["code"], "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------------------
# 4. 서브메뉴 상세 페이지 생성
# ---------------------------------------------------------------------------

def build_sub_page(m, s):
    depth = 1
    siblings = [x for x in m["subs"] if x["slug"] != s["slug"]][:4]
    sib_cards = "".join(
        f'<div class="sub-card"><h3>{x["title"]}</h3><p>{x["desc"]}</p>'
        f'<a class="more" href="{x["slug"]}/index.html">자세히 보기 →</a></div>'
        if x.get("is_group") else
        f'<div class="sub-card"><h3>{x["title"]}</h3><p>{x["desc"]}</p>'
        f'<a class="more" href="{x["slug"]}.html">자세히 보기 →</a></div>'
        for x in siblings
    )
    has_real_content = bool(s.get("body"))
    if has_real_content:
        if s.get("rich_content"):
            # 실제 사진·도식이 본문 안에 이미 포함된 페이지(세척가이드 5종)는
            # 일반 플레이스홀더 박스를 다시 얹지 않는다.
            main_block = s['body']
        else:
            main_block = f"""
      <div class="img-ph" style="min-height:220px; margin-bottom:28px;">[제품 사진/영상 영역]</div>
      {s['body']}
"""
    else:
        main_block = f"""
      <div class="img-ph" style="min-height:280px; margin-bottom:28px;">[이미지/영상 영역]</div>
      <h2 style="font-size:20px;">{s['title']}</h2>
      <p>{s['desc']}</p>
"""
    breadcrumb_html = f'<div class="wrap breadcrumb"><a href="../index.html">홈</a> &gt; <a href="index.html">{m["label"]}</a> &gt; {s["title"]}</div>'
    cover_tail = f"""
      <h2 style="font-size:20px; margin-top:32px;">같은 카테고리의 다른 페이지</h2>
      <div class="sub-grid">{sib_cards}</div>
      <div class="cta-band">
        <div>
          <h3>바테크에 직접 문의해보세요</h3>
          <p>현장 상황에 맞는 가장 정확한 답변을 담당자가 안내해 드립니다.</p>
        </div>
        <a class="cta-btn" href="../products/quote.html">견적문의 하기</a>
      </div>
"""
    if s.get("hero_parallax"):
        # (2026-09-04 v2, 프로토타입) 1차 시안(핀+커버)에서 사용자 피드백을
        # 반영해 패럴랙스 방식으로 교체: 대표 이미지가 메뉴바 바로 아래
        # 전체화면으로 표시되고, 브레드크럼도 이미지 위로 올라옴, 반투명
        # 텍스트 박스는 이미지 정중앙에 배치(설명문 줄바꿈 없이 한 줄).
        # 스크롤하면 이미지와 본문이 "같이" 올라가되 이미지가 더 느리게
        # 움직이고(패럴랙스), 스크롤할수록 이미지에 블러가 점점 강해져
        # 방문자 시선이 자연스럽게 본문으로 옮겨가도록 함. position:sticky가
        # 아닌 순수 스크롤 흐름 + JS 기반 transform/filter(assets/js/main.js
        # 하단 subhero 패럴랙스 블록)로 구현 — 우선 "드라이아이스 세척 가이드"
        # 1개 페이지에서만 틀을 잡아보고, 반응이 좋으면 다른 서브페이지에도
        # hero_parallax 플래그만 추가해 확장할 예정.
        body = f"""
  <section class="subhero-parallax">
    <img class="subhero-parallax-img" src="{s['hero_img']}" alt="{s['title']}" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="index.html">{m['label']}</a> &gt; {s['title']}</div>
    <div class="subhero-textbox">
      <h1>{s['title']}</h1>
      <p>{s['desc']}</p>
    </div>
  </section>
  <section class="subhero-cover">
    <div class="wrap">
      {main_block}
      {cover_tail}
    </div>
  </section>
"""
    else:
        body = f"""
  {breadcrumb_html}
  <section class="page-hero" style="padding-top:24px;">
    <div class="wrap">
      <span class="cat">{m['short']}</span>
      <h1>{s['title']}</h1>
      <p>{s['desc']}</p>
    </div>
  </section>
  <section>
    <div class="wrap">
      {main_block}
      {cover_tail}
    </div>
  </section>
"""
    html = page_shell(s["title"], s["desc"], depth, m["code"], body)
    with open(os.path.join(ROOT, m["code"], f"{s['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)


def energy_dots_html(count=64, seed=42):
    """진입 임팩트용 흩어진 점 파티클 — 화면 곳곳에 넓게 분포된 점들이 로고를 향해
    안쪽으로 빨려들어오며 수렴하는 에너지 필드를 연출. 빌드 시점에 좌표를 고정
    시드로 미리 계산해두므로 재생성해도 항상 동일한 결과가 나온다."""
    rnd = random.Random(seed)
    spans = []
    for i in range(count):
        angle = rnd.uniform(0, 2 * math.pi)
        distance = rnd.uniform(90, 560)
        dx = round(math.cos(angle) * distance, 1)
        dy = round(math.sin(angle) * distance, 1)
        size = round(rnd.uniform(1.8, 4.5), 1)
        delay = round(rnd.uniform(0, 1.4), 2)
        duration = round(rnd.uniform(.6, 1.1), 2)
        opacity = round(rnd.uniform(.5, 1), 2)
        style = (
            f"--dx:{dx}px; --dy:{dy}px; --sz:{size}px; "
            f"--op:{opacity}; animation-delay:{delay}s; animation-duration:{duration}s;"
        )
        spans.append(f'<span class="energy-dot" style="{style}"></span>')
    return "".join(spans)


# (후속69) 사용자 요청("클로드 디자인"이 작성한 상세 스펙)에 따라 기존 "우리의
# 능력"(.ability-section, 100vh 풀-락 pin + 스탯/하이라이트 텍스트 구성)을
# "우리의 가치"(.section-value)로 전면 재설계 — 제목만 `position:sticky;
# top:0`으로 붙여두고 그 아래 4개 콘텐츠 블록(.value-block)이 일반 문서
# 흐름으로 스크롤되며, 화면에 가장 많이 걸친 블록에 IntersectionObserver로
# 포커스를 주는 훨씬 단순한 구조로 바뀜(아래 build_home()의 .section-value,
# assets/css/style.css의 .value-* 규칙, assets/js/main.js의 valueBlocks
# 관련 블록 참고). 옛 ABILITY_HIGHLIGHTS(1986/20개+/14개/3개 정적 텍스트)는
# 더 이상 쓰이지 않아 제거하고, 대신 새 섹션의 "미디어 보도 및 수상" 블록에
# 쓰이는 실제 매체/시상 브랜드명 목록만 남김.
# 주의(다음 세션 참고): 이 재설계 스펙은 세션 컨텍스트 압축(compaction) 이후
# 요약본 기준으로 구현됨 — 클래스명·동작(포커스 전환, 카운트업, 반응형 등)은
# 정확히 반영했으나, "역사로 보는 신뢰"의 1996/2005/2021년 연혁 문구, "믿을 수
# 있는 규모"의 통계 라벨 일부는 원본 문구를 보유하지 못해 대괄호 placeholder
# (기존 .img-ph 관례와 동일)로 남아있음 — 사용자가 실제 문구를 주면 바로 교체.
# (2026-08-28 갱신) 사용자가 assets/img/에 15개 이미지 파일을 전부 넣어줘서
# 기술 라인업 사진·인증마크 2종·매체/시상 로고 12종은 실제 <img>로 교체 완료.
VALUE_MEDIA_LOGOS = [
    ("National Geographic", "logo-natgeo.png"),
    ("History Channel", "logo-history.png"),
    ("DIY Network", "logo-diy.png"),
    ("Goering Center", "logo-goering.png"),
    ("Inc. 5000", "logo-inc5000.png"),
    ("Ernst & Young", "logo-ey.png"),
    ("Mazzy Awards", "logo-mazzy.png"),
    ("Tristate Success Awards", "logo-tristate.png"),
    ("Fast 55", "logo-fast55.png"),
    ("International Business Awards", "logo-iba.png"),
    ("eAwards", "logo-eawards.png"),
    ("Plastics Technology", "logo-plastics.png"),
]

# (후속57) 사용자 요청: irisventure.com처럼 2줄이 서로 반대 방향으로 흐르는
# 고객 레퍼런스 로고 마퀴. "기업들 레퍼런스 이미지는 나중에 줄게. 일단 그래도
# 넣어서 모양만 보자"에 따라 실제 로고 대신 플레이스홀더 텍스트 칩으로 모양만
# 먼저 구성함(가운데 구슬 장식은 요청대로 제외). 실제 로고 수령 시 이 목록을
# <img> 태그로 교체하면 됨.
REF_MARQUEE_ROW1 = [f"고객사 {c}" for c in "ABCDEFGH"]
REF_MARQUEE_ROW2 = [f"고객사 {c}" for c in "IJKLMNOP"]


def _ref_marquee_track_html(names):
    chips = "".join(f'<span class="ref-chip">{name}</span>' for name in names)
    # translateX(-50%) 루프가 이음매 없이 이어지도록 동일한 칩 세트를 2번 반복
    return f'<div class="ref-marquee-track">{chips}{chips}</div>'


def ref_marquee_html():
    """(후속58) 사용자 요청: "우리들의 능력에서 틀고정 한 후 납품고객 리스트까지 다
    내려온 후 틀고정 풀리게 해줘" — 즉 이 마퀴가 "우리의 능력" 전체화면 핀
    바깥(핀이 풀린 뒤에 오는 별도 섹션)이 아니라, 핀이 걸려 있는 화면 안에서
    스탯/하이라이트 바로 아래에 함께 보이다가, 그 화면을 다 보여준 뒤에야 핀이
    풀리도록 해야 함. 그래서 더 이상 독립 <section>이 아니라 .ability-item
    내부에 삽입되는 조각으로 반환 — 큰 섹션 제목 없이 작은 라벨만 붙여 공간을
    아낀다."""
    return f"""
    <div class="ability-refs">
      <span class="ability-refs-label">Our Clients · 납품고객</span>
      <div class="ref-marquee" aria-hidden="true">
        <div class="ref-marquee-row ref-marquee-row-left">{_ref_marquee_track_html(REF_MARQUEE_ROW1)}</div>
        <div class="ref-marquee-row ref-marquee-row-right">{_ref_marquee_track_html(REF_MARQUEE_ROW2)}</div>
      </div>
    </div>
"""


# "우리가 하는 일" — pxpush.com (https://pxpush.com/) 의 "It's a whole new level..."
# 하단에서 본 스크롤 스택 카드 효과를 참고해 순수 CSS position:sticky로 구현.
# 항목마다 상단 sticky 위치를 한 행(--stackdo-head-h)씩 밀어서(--i 변수) 배치하면,
# 스크롤할수록 각 카드의 "번호+제목" 줄만 화면 위에 차곡차곡 쌓여 남고 본문은
# 다음 카드가 덮으며 사라짐 — 자바스크립트 없이 브라우저 기본 sticky 동작만으로
# 재현되므로 별도 스크롤 이벤트 처리나 외부 라이브러리가 필요 없음.
# (사용자 피드백 반영: "WHAT WE DO" 제목 자체도 `.stackdo-pin-title`로 이 sticky
# 스택의 맨 앞(z-index 최하단) 항목이 되도록 `.stackdo-list` 안으로 옮김 — 스크롤
# 시 제목이 먼저 화면 상단에 고정되고, 그 아래로 01~04가 차례로 쌓인 뒤, 4번(기술지원)
# 까지 다 쌓이고 나면 제목+4개 항목이 전부 같은 `.stackdo-list` 컨테이너를 sticky
# containing block으로 공유하므로 컨테이너 끝에서 다같이 스크롤에서 풀려나 함께
# 위로 사라짐 — 4번만 유독 먼저 1~3을 덮고 멈춰버리던 것과 달리 전체가 한 덩어리로
# 자연스럽게 마무리됨. 또한 `.stackdo-list`를 `.wrap`(최대폭 1160px) 밖으로 꺼내
# 섹션 전체 폭(100%)을 그대로 채우도록 구조를 바꿈.
#
# 버그 발견 및 수정 (2단계):
# 1) 마지막 항목(04 기술지원)이 sticky로 "고정되는 시점"과 "풀려나는 시점"이
#    수학적으로 정확히 같아서 — 고정되자마자 곧바로 풀려나 버려, 다른 항목들과
#    달리 전혀 멈춰있지 않고 1~3을 덮은 직후 바로 이어서 위로 사라지는 것처럼
#    보였음(사용자가 "기술지원만 다르게 동작한다"고 지적한 원인). 원인은
#    `.stackdo-list`의 전체 높이가 항목들의 실제 콘텐츠 높이 합과 정확히 같아서
#    컨테이너가 끝나는 지점과 마지막 항목이 sticky로 고정되는 지점이 겹쳐버렸기
#    때문 — 뒤에 여유 스크롤 공간이 전혀 없었던 게 근본 원인.
# 2) 1번을 단순히 `.stackdo-tail`(끝부분 여유 공간)만으로 고치면, 항목마다 sticky
#    top이 --stackdo-head-h씩 밀려있는 구조상 "풀려나는 시점"이 뒤 항목일수록
#    앞 항목보다 정확히 --stackdo-head-h씩 더 일찍 와버려 — 04, 03, 02, 01 순서로
#    차례차례 풀려나면서, 먼저 풀려났지만 z-index는 더 높은 항목이 스크롤되어
#    사라지는 도중 아직 고정된 앞 항목의 제목 줄을 잠깐 덮어버리는 현상이 남음
#    ("1,2,3,4가 함께 위로 올라가게" 요청과 어긋남). 최종 해결: 각 항목에
#    margin-bottom을 (마지막 인덱스 - i) * head-h 만큼 미리 부여(CSS
#    `.stackdo-item`)해 모든 항목의 release 시점 계산식이 정확히 같아지도록
#    맞춤 — 그 결과 제목+1~4가 전부 정확히 같은 스크롤 지점에서 동시에 풀려나
#    함께 위로 사라짐. `.stackdo-tail`은 이제 dwell 시간 보정용이 아니라, 전체가
#    풀려난 뒤 다음 섹션으로 넘어가기 전의 순수한 디자인 여백 역할만 담당.)
# 2026-08-27 (후속46) 제목만 우선 사용자 요청대로 교체(01 드라이아이스 블라스터 /
# 02 드라이아이스 제조 · 리커버리 / 03 자동화 시스템 / 04 렌탈 · 데모 서비스).
# 설명 문구·연결 링크(href)는 아직 예전 제목(제품·자동화 공급/생산·공급/렌탈·데모/
# 기술지원) 기준 그대로 남아 있어 03·04번은 새 제목과 내용이 서로 맞지 않는
# 상태 — 사용자 요청으로 일단 보류(추후 안내 예정).
# (후속47) 사용자가 보내준 실제 제품 사진은 처음엔 01(블라스터)에 넣었으나,
# 사용자가 "이건 제조기·펠렛타이저 사진"이라고 해서 02번(드라이아이스 제조 ·
# 리커버리)로 옮겼었음.
# (후속49) 사용자가 "지금도 블라스터 이미지가 제조/리커버리에 있어"라고 재차
# 정정 — 이 사진은 실제로는 블라스터 사진이 맞았음(원래 처음 요청대로 01번용).
# 02번에서 다시 01번으로 되돌리고 파일명도 stackdo-blaster.jpg로 변경, 02번은
# 다시 빗금 placeholder로. (제조·리커버리용 실제 사진은 아직 없음 — 추후 받으면
# 반영 예정.)
# (후속48) 사용자가 보내준 로봇팔 블라스팅 사진(assets/img/stackdo-automation.jpg)은
# "자동화 사진"이라고 알려줘서 03번(자동화 시스템)에 삽입.
# (후속50) 02번 제목을 "드라이아이스 제조 · 리커버리" → "드라이아이스 제조기 / 리커버리"로
# 변경하고, 사용자가 보내준 펠렛타이저/리커버리 장비 사진(assets/img/stackdo-pelletizer.jpg)을
# 02번에 삽입.
# (후속52) 사용자가 보내준 포터블 블라스터 카트 사진(assets/img/stackdo-rental.jpg)을
# 04번(렌탈 · 데모 서비스)에 삽입 — 이제 01~04 전 항목이 실사진 보유.
STACKDO_ITEMS = [
    (
        "01",
        "드라이아이스 블라스터",
        "블라스터부터 자동화 세척 시스템까지, 현장에 맞는 장비를 공급합니다.",
        "products/index.html",
        "[제품·자동화 공급 이미지 예정]",
        "stackdo-blaster.jpg",
    ),
    (
        "02",
        "제조기 · 리커버리",
        "액체 CO2로 드라이아이스를 직접 만드는 펠렛타이저와, 배출 CO2를 회수해 재사용하는 리커버리 장비를 공급합니다.",
        "products/pelletizer/index.html",
        "[드라이아이스 제조기·리커버리 이미지 예정]",
        "stackdo-pelletizer.jpg",
    ),
    (
        "03",
        "자동화 시스템",
        "구매 전, 실제 현장에서 먼저 성능을 확인해보세요.",
        "rental/index.html",
        "[렌탈·데모 이미지 예정]",
        "stackdo-automation.jpg",
    ),
    # (후속65) 신규 추가: "드라이아이스 생산 · 공급" — 장비가 아닌 소모품으로서
    # 드라이아이스 자체를 정기적으로 생산·공급받는 서비스. desc는 원래 02번
    # 자리에 있던 문구를 그대로 옮김(애초에 이 문구가 뜻하는 내용이 "생산·공급"
    # 이었음 — 02번은 이제 장비(제조기·리커버리) 자체를 소개하는 문구로 교체).
    # href도 이 문구와 정확히 맞는 기존 서브페이지(products/supply.html —
    # "드라이아이스 구매(소모품 공급 안내)")로 연결.
    # (후속68) 사용자가 보내준 드라이아이스 실사진(assets/img/stackdo-supply.jpg)을
    # 적용 — 플레이스홀더 상태 해소.
    (
        "04",
        "드라이아이스 생산 · 공급",
        "펠렛타이저로 직접 생산하거나, 소모품으로 정기 공급받을 수 있습니다.",
        "products/supply.html",
        "[드라이아이스 생산·공급 이미지 예정]",
        "stackdo-supply.jpg",
    ),
    (
        "05",
        "렌탈 · 데모 서비스",
        "설치부터 A/S까지, 도입 이후에도 끝까지 책임집니다.",
        "support/techsupport.html",
        "[기술지원 이미지 예정]",
        "stackdo-rental.jpg",
    ),
]


# (재설계 — "우리가 하는 일" 세로 적층(sticky-stack) 방식을 가로 적층형으로
# 전면 교체: 클로드 디자인에서 받은 스펙 파일 참고. 제목만 sticky로 고정된 채
# 01~05가 화면을 채우는 큰 패널로 하나씩 등장하고, 지나간 항목의 제목은
# FLIP 애니메이션으로 위쪽 탭 줄에 축소되어 박히며, 5개를 모두 지나면 같은
# 5열 그리드의 사진 갤러리가 나타난다. 아래 세 함수가 각각 탭 줄/갤러리/
# 패널 HTML을 STACKDO_ITEMS로부터 생성 — 옛 stackdo_items_html()(세로
# 적층용, .stackdo-item/.stackdo-head/.stackdo-body)을 대체.
def stackdo_tabs_html():
    tabs = []
    for i, (num, title, desc, href, ph_text, img) in enumerate(STACKDO_ITEMS):
        tabs.append(
            f'<a class="stackdo-tab" data-i="{i}" href="{asset(href, 0)}"><span class="stackdo-tab-label">{title}</span></a>'
        )
    return "".join(tabs)


def stackdo_gallery_html():
    items = []
    for i, (num, title, desc, href, ph_text, img) in enumerate(STACKDO_ITEMS):
        img_src = asset("assets/img/" + img, 0)
        items.append(
            f"""
          <a class="stackdo-gallery-item" data-i="{i}" href="{asset(href, 0)}">
            <span class="stackdo-gallery-imgwrap">
              <img class="stackdo-gallery-img-base" src="{img_src}" alt="{title}" loading="lazy" />
              <img class="stackdo-gallery-img-color" src="{img_src}" alt="" aria-hidden="true" loading="lazy" />
            </span>
            <span class="stackdo-gallery-cap">
              <span class="stackdo-gallery-title">{title}</span>
              <span class="stackdo-gallery-divider" aria-hidden="true"></span>
              <span class="stackdo-gallery-desc">{desc}</span>
              <span class="stackdo-gallery-more">자세히 보기 →</span>
            </span>
          </a>"""
        )
    return "".join(items)


def stackdo_panels_html():
    panels = []
    for i, (num, title, desc, href, ph_text, img) in enumerate(STACKDO_ITEMS):
        img_src = asset("assets/img/" + img, 0)
        panels.append(
            f"""
        <div class="stackdo-panel" data-i="{i}">
          <div class="stackdo-panel-body">
            <div class="stackdo-panel-text">
              <div class="stackdo-panel-head"><span class="num">{num}</span><h3>{title}</h3></div>
              <div class="stackdo-panel-desc">
                <p>{desc}</p>
                <a class="more" href="{asset(href, 0)}">자세히 보기 →</a>
              </div>
            </div>
            <img class="stackdo-panel-img" src="{img_src}" alt="{title}" loading="lazy" />
          </div>
        </div>"""
        )
    return "".join(panels)


# (2026-09-02, 후속9) 홈 하단 "메뉴 선택" 카드 6개를 생성한다. 상단 nav_html()의
# 드롭다운과 정확히 같은 6개 대메뉴(MENU)를 그대로 재사용해 정보구조를 두 번
# 정의하지 않으며, 각 카드 안에는 대메뉴 링크(제목)와 함께 하위 서브메뉴 중
# 최대 3개를 칩 형태 바로가기로 노출해 "상단 메뉴보다 더 쉽고 빠르게" 원하는
# 페이지를 바로 찾아갈 수 있게 한다(서브메뉴가 3개보다 많으면 "+N개" 칩이
# 허브 페이지로 안내). 카드 자체(.menu-picker-title-link)와 칩들이 모두
# <a>라 마크업상 앵커 중첩을 피하기 위해, 카드 전체를 감싸는 진짜 링크는
# 제목에만 걸고 CSS의 ::after 스트레치드 링크로 카드 전체 클릭 영역을 넓힌
# 뒤(assets/css/style.css .menu-picker-title-link::after), 칩들은 z-index를
# 그 위로 올려 각자 독립적으로 클릭되게 한다(표준적인 "카드 안에 보조
# 링크가 있는 카드" 패턴). 등장 애니메이션은 새 JS 없이 기존 공용 리빌
# 시스템(.reveal-pop + --reveal-delay)을 그대로 타 카드 인덱스 순서로
# 0.07초씩 늦게 나타나 좌상단→우하단으로 순서대로 튀어 오르는 느낌을 준다.
def menu_picker_html():
    cards = []
    for i, m in enumerate(MENU):
        hub_href = asset(f"{m['code']}/index.html", 0)
        delay = i * 0.07
        shown_subs = m["subs"][:3]
        chips = "".join(
            f'<a class="menu-picker-chip" href="{asset(m["code"] + "/" + s["slug"] + ("/index.html" if s.get("is_group") else ".html"), 0)}">{s["title"]}</a>'
            for s in shown_subs
        )
        more_count = len(m["subs"]) - len(shown_subs)
        if more_count > 0:
            chips += f'<a class="menu-picker-chip menu-picker-chip-more" href="{hub_href}">+{more_count}개</a>'
        cards.append(f"""
        <div class="menu-picker-card reveal-pop" style="--reveal-delay:{delay:.2f}s">
          <h3><a class="menu-picker-title-link" href="{hub_href}">{m['label']}</a></h3>
          <p>{m['tagline']}</p>
          <div class="menu-picker-chips">{chips}</div>
          <span class="menu-picker-arrow" aria-hidden="true">→</span>
        </div>""")
    return "".join(cards)


def build_home():
    depth = 0

    body = f"""
  <section class="hero">
    <div class="hero-video-wrap">
      <video class="hero-video" autoplay muted loop playsinline poster="assets/video/main-hero-poster.jpg">
        <source src="assets/video/main-hero.webm" type="video/webm">
        <source src="assets/video/main-hero.mp4" type="video/mp4">
      </video>
    </div>
    <div class="hero-overlay"></div>
    <div class="hero-intro" aria-hidden="true">
      {energy_dots_html()}
      <img class="power-core" src="assets/img/vatek-logo.png" alt="VATEK" />
      <div class="snap-flash"></div>
    </div>
    <div class="wrap">
      <h1>세계가 선택한 세척 기술,<br />생산의 <span class="accent">차이</span>를 만듭니다.</h1>
      <p class="lead">바테크는 세계 최초이자 글로벌 리더 Cold Jet의 대한민국 공식 총판입니다.
      압도적인 기술력과 현장 경험으로 더 정확하고 효율적인 산업 세척 솔루션을 제공합니다.</p>
      <div class="actions">
        <a class="cta-btn" href="products/quote.html">견적문의</a>
        <a class="cta-btn outline" href="rental/demo.html">데모 테스트 신청</a>
      </div>
    </div>
    <button type="button" class="hero-scroll autoscroll-hint" aria-label="다음 화면으로 스크롤">
      <span>Scroll down</span>
      <span class="hero-scroll-chevrons">
        <span class="chevron"></span>
        <span class="chevron"></span>
      </span>
    </button>
  </section>

  <section class="stackdo-section">
    <div class="stackdo-scroll" id="stackdoScroll">
      <div class="stackdo-frame">
        <div class="stackdo-header">
          <h2>우리가 하는 일</h2>
        </div>
        <div class="stackdo-tabs" id="stackdoTabs">
          {stackdo_tabs_html()}
        </div>
        <div class="stackdo-stage">
          <div class="stackdo-gallery" id="stackdoGallery">
            {stackdo_gallery_html()}
          </div>
          {stackdo_panels_html()}
        </div>
        <button type="button" class="stackdo-scroll-hint autoscroll-hint" aria-label="다음 화면으로 스크롤">
          <span>Scroll down</span>
          <span class="stackdo-scroll-hint-chevrons">
            <span class="chevron"></span>
            <span class="chevron"></span>
          </span>
        </button>
      </div>
    </div>
  </section>

  <section class="section-value">
    <div class="value-list">
      <div class="value-pin-title"><h2>우리의 가치</h2></div>
      <button type="button" class="value-scroll-hint autoscroll-hint" aria-label="다음 화면으로 스크롤">
        <span>Scroll down</span>
        <span class="value-scroll-hint-chevrons">
          <span class="chevron"></span>
          <span class="chevron"></span>
        </span>
      </button>
      <div class="value-content">
        <div class="value-block" data-tone="#f3f9fa">
          <span class="value-label">업계 최초</span>
          <div class="value-timeline">
            <div class="value-timeline-item">
              <b class="count-up" data-target="1986" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>최초의 산업용 블라스터 개발</span>
            </div>
            <div class="value-timeline-item">
              <b class="count-up" data-target="1996" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>최초로 NASA 기술 적용</span>
            </div>
            <div class="value-timeline-item">
              <b class="count-up" data-target="2005" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>최초의 블록형 블라스터 개발</span>
            </div>
            <div class="value-timeline-item">
              <b class="count-up" data-target="2021" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>최초의 스마트형 원격 시스템</span>
            </div>
          </div>
        </div>
        <div class="value-block" data-tone="#eaf6f7">
          <span class="value-label">업계 최대</span>
          <div class="value-stats">
            <div class="value-stat">
              <b class="count-up" data-target="3" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>글로벌 생산공장</span>
            </div>
            <div class="value-stat">
              <b class="count-up" data-target="120" data-suffix="+" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>최다 글로벌 특허 보유</span>
            </div>
            <div class="value-stat">
              <b class="count-up" data-target="14" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>글로벌 자회사</span>
            </div>
            <div class="value-stat">
              <b class="count-up" data-target="3" data-count-on-focus>0</b>
              <span class="rule"></span>
              <span>R&amp;D 연구소</span>
            </div>
          </div>
        </div>
        <div class="value-block" data-tone="#f3f9fa">
          <span class="value-label">검증된 기술력</span>
          <div class="value-feature">
            <div class="value-feature-text">
              <span class="value-feature-eyebrow">블라스터만 전 세계</span>
              <b class="value-feature-num"><span class="count-up" data-target="24000" data-comma data-count-on-focus>0</span><span class="unit">대 이상</span></b>
              <h3 class="value-feature-headline">압도적인 세계 판매량 1위</h3>
              <p class="value-feature-desc">24,000대가 넘는 글로벌 설치 실적과 다양한 산업 현장에서 축적된 경험을 통해, Cold Jet의 기술력과 신뢰성은 이미 검증되었습니다.</p>
            </div>
            <div class="value-feature-divider"></div>
            <div class="value-feature-img"><img src="{asset("assets/img/ability-tech-lineup-new.jpg", 0)}" alt="Cold Jet 기술 라인업" loading="lazy" /></div>
          </div>
        </div>
      </div>
    </div>
    <div class="value-content value-content-tail">
      <div class="value-block" data-tone="#e3f1f2">
        <span class="value-label">미디어 보도 및 수상</span>
        <div class="value-logos">
          {"".join(f'<img class="value-logo" src="{asset("assets/img/" + file, 0)}" alt="{name}" loading="lazy" />' for name, file in VALUE_MEDIA_LOGOS)}
        </div>
      </div>
    </div>
    <div class="belief-list">
      <div class="belief-pin-title"><h2>우리의 신념</h2></div>
      <div class="belief-video-scroll">
        <div class="belief-video-wrap">
          <video class="belief-video" autoplay muted loop playsinline poster="{asset("assets/video/belief-co2-poster.jpg", 0)}">
            <source src="{asset("assets/video/belief-co2.webm", 0)}" type="video/webm">
            <source src="{asset("assets/video/belief-co2.mp4", 0)}" type="video/mp4">
          </video>
          <div class="belief-video-box belief-video-box-lead">
            <h3 class="belief-video-heading">우리의 신념</h3>
            <p class="belief-video-sub"><span class="hl-blue">CO<sub>2</sub></span>에 새로운<br><span class="hl-green">가치</span>를 더합니다.</p>
            <img class="belief-video-logo" src="{asset("assets/img/co2-ribbon-logo.png", 0)}" alt="CO2" width="480" height="241" loading="lazy">
          </div>
          <button type="button" class="belief-scroll-hint autoscroll-hint" aria-label="다음 화면으로 스크롤">
            <span>Scroll down</span>
            <span class="belief-scroll-hint-chevrons">
              <span class="chevron"></span>
              <span class="chevron"></span>
            </span>
          </button>
          <p class="belief-video-desc-text">우리는 CO<sub>2</sub> 기술의 혁신으로,<br>지속가능한 산업 생태계를 만들고,<br>더 나은 환경과 사회적 가치를 함께 실현합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-coldjet">
    <div class="coldjet-list">
      <div class="coldjet-pin-title"><h2>우리는 <span class="hl-coldjet">'콜드젯 팀'</span>입니다.</h2></div>
      <div class="coldjet-video-scroll">
        <div class="coldjet-video-wrap">
          <video class="coldjet-video" autoplay muted loop playsinline poster="{asset("assets/video/coldjet-video-poster.jpg", 0)}">
            <source src="{asset("assets/video/coldjet-video.webm", 0)}" type="video/webm">
            <source src="{asset("assets/video/coldjet-video.mp4", 0)}" type="video/mp4">
          </video>
          <div class="coldjet-video-box coldjet-video-box-lead">
            <h3 class="coldjet-video-heading">WE ARE ONE TEAM</h3>
            <p class="coldjet-video-sub">콜드젯은 장비의 연구·개발·생산과 기술 교육을 담당하고 있으며,<br>바테크는 대한민국 공식 총판으로서 제품 판매부터 기술 지원 및 관련 서비스를 제공합니다.</p>
          </div>
          <button type="button" class="coldjet-scroll-hint autoscroll-hint" aria-label="다음 화면으로 스크롤">
            <span>Scroll down</span>
            <span class="coldjet-scroll-hint-chevrons">
              <span class="chevron"></span>
              <span class="chevron"></span>
            </span>
          </button>
          <div class="coldjet-video-desc-text coldjet-brand-row">
            <span class="coldjet-brand-chip"><img class="coldjet-brand-logo coldjet-brand-logo-vatek" src="{asset("assets/img/vatek-logo-mark.png", 0)}" alt="VATEK"></span>
            <span class="coldjet-brand-x">×</span>
            <span class="coldjet-brand-chip"><img class="coldjet-brand-logo coldjet-brand-logo-coldjet" src="{asset("assets/img/coldjet-logo.png", 0)}" alt="Cold Jet"></span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-menu-picker">
    <div class="wrap">
      <div class="section-head menu-picker-head">
        <h2 class="reveal">무엇을 도와드릴까요?</h2>
      </div>
      <div class="menu-picker-grid">
        {menu_picker_html()}
      </div>
    </div>
  </section>
"""
    html = page_shell(
        "바테크 | Cold Jet 대한민국 공식 대리점, 드라이아이스 세척 전문기업",
        "바테크는 Cold Jet 대한민국 공식 대리점으로 드라이아이스 세척기, 제조기, 자동화 시스템과 소모품을 공급합니다.",
        depth, None, body, is_home=True,
    )
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    for m in MENU:
        os.makedirs(os.path.join(ROOT, m["code"]), exist_ok=True)
        build_hub_page(m)
        for s in m["subs"]:
            if s.get("is_group"):
                continue  # 제품 그룹(블라스터/펠렛타이저)은 products.py가 별도 생성
            build_sub_page(m, s)
    build_home()

    import products
    n_blaster = products.build_blaster(ROOT, nav_html, footer_html, page_shell, asset)
    n_pelletizer = products.build_pelletizer(ROOT, nav_html, footer_html, page_shell, asset)
    n_recovery = products.build_recovery(ROOT, nav_html, footer_html, page_shell, asset)

    total = sum(len(m["subs"]) for m in MENU if True) - 3  # blaster/pelletizer/recovery는 is_group이라 별도 카운트
    total_pages = 1 + len(MENU) + total + n_blaster + n_pelletizer + n_recovery
    print(f"생성 완료: 홈 1개 + 허브 {len(MENU)}개 + 서브페이지 {total}개 "
          f"+ 블라스터 {n_blaster}개 + 펠렛타이저 {n_pelletizer}개 + CO2 리커버리 {n_recovery}개 "
          f"= 총 {total_pages}개")


if __name__ == "__main__":
    main()
