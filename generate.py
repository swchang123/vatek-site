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
<div class="co2-story" style="margin-bottom: 50px">
  <div class="wrap">
  <h2 style="font-size: 45px; color: #000000; position: static; margin-bottom: 40px; margin-top: 0px; padding-top: 10px">드라이아이스란 무엇인가?</h2>

  <div>
    <div>드라이아이스는 이산화탄소(CO₂)를 고체 상태로 만든 것입니다.<br>산업시설이나 바이오가스 시설 등에서 포집된 CO₂를 정제·액화한 뒤, 다시 고체로 전환하여 생산합니다.</div>
    <div style="padding-top: 20px">이 과정은 탄소 포집 및 활용(CCU, Carbon Capture and Utilization)의 한 형태로, 포집된 CO₂를 그대로 배출하지 않고 다시 자원으로 활용함으로써, 냉각과 산업용 세정 등 다양한 용도로 사용할 수 있습니다.</div>
    <div style="padding-top: 20px">포집된 CO₂는 정제와 압축 과정을 거쳐 액체 상태로 저장·운송되며, 이후 펠레타이저(Pelletizer)를 통해 드라이아이스로 생산됩니다. 이렇게 만들어진 드라이아이스는 산업 현장에서 냉각뿐 아니라 물이나 화학 세정제를 사용하지 않는 건식 세정 매체로도 활용됩니다.</div>
    <div><br></div>
  </div>
  <div><b style="color: #000000">'포집된 CO₂를 다시 활용 가능한 자원으로 전환하는 것'</b>, 이것이 드라이아이스가 만들어지는 과정입니다.</div>

  <div class="co2-second-life-card">
    <h3 class="co2-story-sub" style="font-size: 25px; margin-top: 0;">CO<sub>2</sub>에 두 번째 생명을</h3>
    <div class="co2-second-life-img">
      <img src="../assets/img/co2-second-life-infographic.png" alt="Giving CO2 a Second Life — 공장 배출부터 드라이아이스까지의 CO2 순환 경로 인포그래픽" loading="lazy" />
    </div>
    <p>한 번 배출된 CO<sub>2</sub>를 그대로 버리는 대신, 다시 산업에 활용할 수 있는 자원으로 전환합니다.</p>

    <blockquote class="cite-quote">
      <p>드라이아이스는 재활용된 CO<sub>2</sub>를 사용하기 때문에 탄소발자국 산정 시 CO<sub>2</sub>가 사용
      단계에서 다시 계산되지 않습니다. CO<sub>2</sub>는 생산자 단계에서 이미 산정됩니다.</p>
      <cite>— California Air Resources Board (캘리포니아 대기자원위원회)</cite>
    </blockquote>
    <div class="co2-scoop-photo">
      <img src="../assets/img/dry-ice-scoop-wide.png" alt="드라이아이스 펠렛 위의 투명 스쿱" loading="lazy" />
    </div>
  </div>

  <h3 class="co2-story-sub" style="font-size: 25px; color: #000000; padding-top: 60px">더 깨끗한 산업을 위한 CO<sub>2</sub>의 순환</h3>
  <p>드라이아이스는 새로운 CO<sub>2</sub>를 만들어 사용하는 것이 아니라, 이미 포집된 CO<sub>2</sub>를 다시
  활용하는 순환형 자원입니다.</p>
  <p style="color: #46595B">세정 과정에서는 물이나 화학 세정제를 사용하지 않으며, 드라이아이스 자체는 사용 후 다시 기체로
  승화합니다. 이러한 특성은 물 사용과 2차 폐기물 발생을 줄이는 산업 세정 방식으로 이어집니다.</p>

  <img src="../assets/img/co2-ribbon-logo.png" alt="co2-ribbon-logo" width="480" height="241" style="max-width: 100%; height: 120px; display: block; object-fit: cover; width: 256px; aspect-ratio: 480 / 241; position: static; margin-left: auto; margin-right: auto; margin-top: 50px" />
  <p class="co2-story-tagline" style="color: #000000; margin-top: 50px; margin-bottom: 50px; line-height: 2; padding-top: 10px">회수된 CO<sub>2</sub>를 다시 가치 있는 자원으로.<br />
  드라이아이스는 탄소를 순환시키는 또 하나의 방법입니다.</p>
  </div>
</div>

<div style="color: #000000">
  <div><b style="font-size: 45px; padding-top: 30px">왜 드라이아이스인가?</b></div>
  <div>
    <div style="padding-top: 20px; padding-bottom: 20px; line-height: 2; color: #46595B">드라이아이스는 고체 상태의 이산화탄소(CO₂)이므로, 일반 얼음과 달리 녹아 물이 되지 않고, 승화를 통해 고체에서 기체로 바로 변합니다.<br>온도는 약 -78.5°C로 매우 낮아, 냉각뿐 아니라 산업용 세정 매체로도 널리 활용됩니다.</div>
    <div style="text-align: center; padding: 20px 0"><b style="font-size: 25px">이러한 독특한 성질들 덕분에<br>드라이아이스는 여러 가지 용도에 활용될 수 있습니다.</b></div>
    <div class="use-trio">
      <div class="use-item">
        <img src="../assets/img/use-cleaning.png" alt="드라이아이스 세척 작업" loading="lazy" />
        <h4>세척 (Cleaning)</h4>
        <p style="width: 340px; height: 133px">화학물질이나 연마제를 사용하지 않고, 드라이아이스 펠렛을 이용하여 표면을 세척하는 방법입니다.</p>
      </div>
      <div class="use-item">
        <img src="../assets/img/use-cooling.png" alt="식품 냉각·보존" loading="lazy" />
        <h4>냉각/보존 (Cooling)</h4>
        <p>드라이아이스는 일반 얼음보다 훨씬 낮은 온도를 가지며, 물기를 남기지 않기 때문에 냉동식품, 의약품 등 온도에 민감한 물품을 운송할 때 냉매로 활용됩니다.</p>
      </div>
      <div class="use-item">
        <img src="../assets/img/use-science.png" alt="연구실 저온 시료 처리" loading="lazy" />
        <h4>과학적 용도 (Science)</h4>
        <p>드라이아이스는 시료를 냉동하거나, 정확하게 제어된 저온 환경을 조성하기 위해 연구실에서 사용됩니다.</p>
      </div>
    </div>
    <b style="display: block; font-size: 26px; margin-top: 40px">드라이아이스 세척이 다른 이유</b>
    <div style="padding-top: 20px; padding-bottom: 20px; line-height: 2; color: #46595B">
      <div>드라이아이스는 비마모성 세정 매체로, 세척 대상의 표면이나 장비를 손상시키지 않습니다.또한 표면에 충돌하는 순간 기체로 승화하기 때문에 2차 폐기물이 남지 않습니다. 비독성이며 화학 세정제 사용을 줄일 수 있어 작업자 안전과 환경 측면에서도 유리합니다. 물을 사용하지 않는 건식 세정 방식이므로, 세척 후 별도의 건조 공정이 필요하지 않는 것도 큰 장점입니다.</div>
    </div>
    <div class="eco-icons">
      <div class="eco-icon"><img src="../assets/img/eco-reduce-emissions.png" alt="배출 저감" loading="lazy" /><span>배출 저감</span></div>
      <div class="eco-icon"><img src="../assets/img/eco-water-free.png" alt="물 사용 없음" loading="lazy" /><span>물 사용 없음</span></div>
      <div class="eco-icon"><img src="../assets/img/eco-recycled.png" alt="재활용 자원" loading="lazy" /><span>재활용 자원</span></div>
      <div class="eco-icon"><img src="../assets/img/eco-chemical-free.png" alt="화학약품 없음" loading="lazy" /><span>화학약품 없음</span></div>
      <div class="eco-icon"><img src="../assets/img/eco-waste-free.png" alt="폐기물 없음" loading="lazy" /><span>폐기물 없음</span></div>
      <div class="eco-icon"><img src="../assets/img/eco-non-abrasive.png" alt="비마모성·비손상" loading="lazy" /><span>비마모성·비손상</span></div>
      <div class="eco-icon"><img src="../assets/img/eco-non-toxic.png" alt="무독성" loading="lazy" /><span>무독성</span></div>
      <div class="eco-icon"><img src="../assets/img/eco-non-flammable.png" alt="비전도성·비인화성" loading="lazy" /><span>비전도성·비인화성</span></div>
    </div>
    <div class="clean-compare">
      <div class="clean-compare-col">
        <h4 class="clean-compare-title" style="color: #000000; font-size: 20px; padding-top: 50px">기존 세척 방식</h4>
        <div class="clean-compare-fig">
          <ul class="clean-compare-legend">
            <li class="lg-water" style="font-style: normal">물</li>
            <li class="lg-chem" style="font-style: normal">화학약품</li>
            <li class="lg-dirt" style="font-style: normal">오염물</li>
          </ul>
          <img src="../assets/img/compare-traditional.png" alt="기존 세척 — 물과 화학약품이 필요하고 생산을 멈춰야 함" loading="lazy" />
        </div>
        <p class="clean-compare-note" style="font-style: normal; padding-bottom: 60px">생산 중단 → 냉각 → 분리 → 이송 → 세척 → 이송 → 재설치 → 재가열 → 생산 재개</p>
      </div>
      <div class="clean-compare-col">
        <h4 class="clean-compare-title is-dryice" style="color: #000000; font-size: 20px; padding-top: 50px">드라이아이스 세척</h4>
        <div class="clean-compare-fig">
          <ul class="clean-compare-legend">
            <li class="lg-dirt" style="font-style: normal">오염물</li>
          </ul>
          <img src="../assets/img/compare-dryice.png" alt="드라이아이스 세척 — 오염물만 제거, 생산 중 온라인 세척" loading="lazy" />
        </div>
        <p class="clean-compare-note" style="font-style: normal">생산 중 온라인 세척</p>
      </div>
    </div>
  </div>
</div>

<div class="co2-story principle-story">
  <div class="wrap">
    <h2 style="font-size: 45px; color: #000000; position: static; margin-bottom: 40px; margin-top: 0px; padding-top: 10px">드라이아이스의 세척원리</h2>
    <div class="principle-intro">
      <div class="principle-intro-text" style="line-height: 2; color: #46595B">
        <div>드라이아이스 세척은 압축공기로 세정 매체를 가속해 표면을 세척한다는 점에서 샌드, 비드, 소다 블라스팅과 유사합니다.</div>
        <div style="padding-top: 20px">차이점은 드라이아이스 세척이 고체 CO₂ 펠렛 또는 마이크로파티클을 사용한다는 점입니다. 이 입자들은 초음속으로 분사되어 오염물에 충돌한 뒤 즉시 승화하면서, 표면의 오염물과 이물질을 들어 올려 제거합니다.</div>
      </div>
      <div class="video-embed principle-intro-video">
        <video autoplay muted loop playsinline preload="none" poster="../assets/img/principle-kinetic-t.png">
          <source src="../assets/video/principle-nozzle.mp4" type="video/mp4" />
        </video>
      </div>
    </div>
    <div class="principle-grid">
      <div class="principle-col">
        <img class="principle-icon" src="../assets/img/icon-kinetic-t.png" alt="" />
        <h5>운동 에너지</h5>
        <img class="principle-img" src="../assets/img/principle-kinetic-t.png" alt="운동 에너지 — 펠렛 충격" loading="lazy" />
        <span class="principle-letter">I</span>
        <p><b>충격(Impact)</b>으로 운동 에너지 효과가 발생합니다. 부드러운 드라이아이스가 특수 설계된 노즐을 통해 압축공기로 초음속까지 가속됩니다. 운동 에너지는 선택한 입자 크기와 분사 압력으로 제어되며, 드라이아이스가 오염물에 충돌해 미세 균열을 만듭니다.</p>
      </div>
      <div class="principle-col">
        <img class="principle-icon" src="../assets/img/icon-thermal-t.png" alt="" />
        <h5>열역학적 충격</h5>
        <img class="principle-img" src="../assets/img/principle-thermal-t.png" alt="열역학적 충격 — 저온 취성화" loading="lazy" />
        <span class="principle-letter">C</span>
        <p>드라이아이스 펠렛의 <b>저온(Cold)</b>이 열 효과를 만듭니다. 드라이아이스의 온도(-78.5°C)는 오염물을 취성화(부서지기 쉽게)시켜 모재와 오염물 사이의 결합을 끊는 데 도움을 줍니다. 열 효과의 기여도는 체류 시간·이동 속도와 드라이아이스 공급량 설정에 따라 달라집니다. 이 세정 효과로 이미 미세 균열이 생긴 오염물이 수축하며 모재와의 결합력을 잃게 됩니다.</p>
      </div>
      <div class="principle-col">
        <img class="principle-icon" src="../assets/img/icon-explosion-t.png" alt="" />
        <h5>CO₂ 팽창</h5>
        <img class="principle-img" src="../assets/img/principle-expansion-t.png" alt="CO2 팽창 — 800배 부피 팽창" loading="lazy" />
        <span class="principle-letter">E</span>
        <p>드라이아이스 펠렛의 <b>팽창(Expansion)</b>입니다. 펠렛은 충돌 즉시 승화하며 부피가 800배로 팽창해, 오염물을 안쪽에서부터 밀어내어 제거(블라스팅)합니다.</p>
      </div>
      <div class="principle-col">
        <img class="principle-icon" src="../assets/img/icon-sublimation-t.png" alt="" />
        <h5>승화</h5>
        <img class="principle-img" src="../assets/img/principle-sublimation-t.png" alt="승화 — 잔류물 없는 깨끗한 표면" loading="lazy" />
        <span class="principle-letter">&nbsp;</span>
        <p>드라이아이스는 비마모성이며 기체로 변해 사라지기 때문에, 깨끗한 표면만 남아 금형의 수명을 연장시킵니다.</p>
      </div>
    </div>
  </div>
</div>

<div class="co2-story blaster-story">
  <div class="wrap">
    <h2 style="font-size: 45px; color: #000000; position: static; margin-bottom: 40px; margin-top: 0px; padding-top: 10px">드라이아이스 세척기?</h2>
    <div class="blaster-intro">
    <div class="blaster-intro-text" style="line-height: 2; color: #46595B">
      <div>
        <div>드라이아이스 세척기는 드라이아이스 펠렛 또는 마이크로파티클을 압축공기로 가속해 노즐로 고속 분사하는 산업용 세정 장비입니다. 분사 압력과 드라이아이스 공급량을 조절해 세정 대상과 오염 상태에 맞게 사용할 수 있습니다.<br>기술적으로는 드라이아이스 블라스터(Dry Ice Blaster)라고 부릅니다. 샌드 블라스터나 비드 블라스터처럼 세정 매체를 압축공기로 가속해 분사하는 방식이기 때문입니다. 다만 모래나 비드 대신 고체 이산화탄소(CO₂)인 드라이아이스를 사용합니다. 드라이아이스는 표면에 충돌한 뒤 곧바로 승화해 기체로 변하므로 세정 매체가 남지 않습니다.<br>국내에서는 주로 세척 목적으로 사용되기 때문에 ‘드라이아이스 세척기’라는 이름으로 더 익숙하게 불립니다.</div>
        <div><br></div>
      </div>
    </div>
    <div class="blaster-intro-img">
      <img src="../assets/img/blaster-operator-t.png" alt="Cold Jet 드라이아이스 블라스터로 세척 작업 중인 작업자" loading="lazy" />
    </div>
    </div>
  </div>
</div>

<h2 style="font-size: 26px; margin-top: 36px; color: #000000">드라이아이스 블라스팅의 시작, Cold Jet</h2>
<figure class="history-collage">
  <img src="../assets/img/coldjet-history-collage-teal.png" alt="1986년 미국 특허 도면, 초기 항공기 세척 작업 사진, 초기 Cold Jet 장비 라인업" loading="lazy" />
  <figcaption>1986년 미국 특허(No. 4,617,064) 도면 · 초기 항공기 세척 작업 · 초기 장비 라인업</figcaption>
</figure>
<p style="line-height: 2">콜드젯(Cold Jet)은, 1986년 최초의 드라이아이스 블라스터를 개발했으며, 1989년에는 산업용 드라이아이스 블라스터 관련 최초 특허를 확보하며 본격적인 기술 상용화의 기반을 마련했습니다.<br>이후 Cold Jet는 단순한 분사 장비를 넘어 드라이아이스 입자 제어, 노즐 설계, 정밀 세정, 자동화 및 공정 통합 기술을 지속적으로 개발하며 드라이아이스 블라스팅의 적용 범위를 확대해 왔습니다.</p>

<h2 style="font-size: 26px; margin-top: 36px; padding-top: 40px; color: #000000">산업 현장에서 검증된 드라이아이스 블라스터</h2>
<div class="proven-block">
  <div class="proven-text" style="line-height: 2">
    <p>드라이아이스 블라스터는 금형, 생산설비, 주조·자동차·전자·반도체 등 다양한 산업 현장에서 사용되며, 먼지와 오염, 장시간 운전 등 비교적 가혹한 조건에 노출되는 경우가 많습니다. 따라서 단순한 세정력뿐 아니라 장비의 내구성, 장시간 운전 시 성능 안정성, 유지보수성과 부품 공급 체계까지 중요한 선택 기준이 됩니다.</p>
    <p>Cold Jet는 이러한 산업 환경을 고려해 견고한 프레임 구조, 고품질 스테인리스 부품, 정밀하게 설계된 공압 시스템을 적용하고 있으며, 장시간 연속 운전에서도 안정적인 세정 성능을 유지하도록 설계되어 있습니다. 이러한 성능과 내구성은 전 세계 다양한 산업 현장에서 축적된 적용 경험을 통해 검증되어 왔습니다.</p>
  </div>
  <figure class="proven-lineup">
    <img src="../assets/img/lineup-trimmed-t.png" alt="Cold Jet 드라이아이스 블라스터 전 제품 라인업" loading="lazy" style="padding-top: 15px" />
  </figure>
</div>

<section class="faq-section">
  <div class="faq-head">
    <h2 style="font-size: 46px; margin: 36px 0 0; padding-top: 20px; color: #000000">자주 묻는 질문 <span class="faq-en" style="font-size: 30px">FAQ</span></h2>
    <p class="faq-intro">드라이아이스 세척을 처음 검토하실 때 가장 많이 받는 질문을 정리했습니다.</p>
  </div>
  <div class="faq-list">
    <details class="faq-item">
      <summary><span class="faq-q" style="font-size: 25px">드라이아이스를 보관해 두고 사용할 수 있나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
      <div class="faq-a"><p>보관은 가능하지만, 드라이아이스는 시간이 지나면서 고체에서 기체로 승화하여 양이 줄어들고 품질도 떨어집니다. 따라서 장기간 보관하기보다는 필요한 시점에 공급받아 가급적 빠르게 사용하는 것이 좋습니다.</p><p>바테크에서는 드라이아이스 보관을 위한 스티로폼 박스와 드라이아이스 전용 보냉용기도 판매하고 있습니다. 일반적으로 스티로폼 박스에 보관할 경우 하루 약 5~10%, 단열 성능이 높은 드라이아이스 전용 보냉용기의 경우 약 2~5% 정도의 승화 손실이 발생할 수 있습니다. 다만 실제 손실률은 외부 온도, 드라이아이스의 양과 크기, 용기의 단열 성능, 개폐 횟수 등에 따라 달라집니다.</p><p>드라이아이스는 승화하면서 CO₂ 가스가 발생하므로 완전히 밀폐된 용기에 보관해서는 안 됩니다.</p></div>
    </details>
    <details class="faq-item">
      <summary><span class="faq-q" style="font-size: 25px">드라이아이스는 어떤 크기를 사용하나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
      <div class="faq-a"><p>드라이아이스 세척에는 일반적으로 직경 3mm의 드라이아이스 펠렛을 사용합니다.</p><p>Cold Jet의 마이크로파티클(MicroParticle) 시스템은 3mm 펠렛을 미세하게 절단하여 0.3mm부터 3.0mm까지 0.1mm 간격으로 입자 크기를 조절할 수 있습니다. 세척 대상의 재질과 오염 정도에 따라 입자 크기를 세밀하게 설정할 수 있어 정밀 부품부터 강한 세척력이 필요한 산업용 설비까지 폭넓게 적용할 수 있습니다.</p></div>
    </details>
    <details class="faq-item">
      <summary><span class="faq-q" style="font-size: 25px">세척기를 사용하려면 무엇이 필요한가요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
      <div class="faq-a"><p>기본적으로 드라이아이스 세척기, 드라이아이스, 압축공기, 전원이 필요합니다.</p><p>필요한 압력과 공기량은 사용하는 장비와 노즐, 세척 대상에 따라 달라집니다. 또한 작업 중 드라이아이스가 CO₂ 가스로 승화하므로 충분한 환기가 필요하며, 작업 환경에 맞는 보호장비와 안전수칙을 준수해야 합니다.</p></div>
    </details>
    <details class="faq-item">
      <summary><span class="faq-q" style="font-size: 25px">드라이아이스 세척으로 모든 오염물을 제거할 수 있나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
      <div class="faq-a"><p>모든 오염물을 제거할 수 있는 것은 아닙니다. 드라이아이스 세척은 기름, 그리스, 이형제, 접착제, 수지, 잉크, 먼지 및 각종 생산 잔여물 등 다양한 오염물 제거에 효과적이지만, 오염물의 종류와 부착 정도, 세척 대상의 재질에 따라 세척 결과가 달라질 수 있습니다.</p><p>특히 소재 내부까지 깊게 진행된 녹이나 표면 자체를 깎아내야 하는 경우에는 연마재를 사용하는 다른 세척 방식이 더 적합할 수 있습니다. 적용 가능 여부가 확실하지 않다면 실제 샘플 테스트를 통해 세척 가능 여부와 적합한 조건을 확인하는 것이 가장 정확합니다.</p></div>
    </details>
  </div>
</section>
"""

COMPARE_BODY = """
  <section class="subhero-parallax">
    <img class="subhero-parallax-img" src="../assets/img/compare-hero.jpg" alt="산업 현장 드라이아이스 세척 작업" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="index.html">드라이아이스 세척가이드</a> &gt; 타 세척방식과의 비교</div>
    <div class="subhero-textbox">
      <h1>타 세척방식과의 비교</h1>
      <p class="cmp-hero-p">세척 성능만으로 적합한 세척 방식을 판단할 수는 없습니다.<br>표면 영향, 2차 폐기물, 수분, 작업시간과 설비 정지 등<br>산업현장에서 함께 고려해야 할 요소를 기준으로 주요 세척 방식을 비교해보세요.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">CHOOSING A CLEANING METHOD</span>
  <h2 class="cmp-h2">좋은 세척 방식은<br>‘잘 닦이는가’만으로 결정되지 않습니다.</h2>
  <div class="cmp-lead">
    <p>산업현장에서 세척은 단순히 오염물을 제거하는 작업으로 끝나지 않습니다.</p>
    <p>목표한 청정도를 확보하는 것은 기본이고, 그 과정에서 금형·생산설비·부품 및 제품 표면에 영향을 주지 않는지, 새로운 폐기물이나 폐수가 발생하는지, 세척을 위해 어느 정도의 생산 중단이 필요한지, 그리고 작업자의 안전과 주변 공정에 어떤 영향을 미치는지까지 함께 검토해야 합니다.</p>
    <p>예를 들어 연마재를 사용하는 세척은 강한 제거력이 필요한 작업에 효과적이지만 사용한 매체의 회수와 처리가 필요할 수 있고, 물을 사용하는 세척은 폐수와 건조 공정까지 고려해야 합니다. 수작업이나 화학세척 역시 적용이 간편한 반면 작업시간과 인력, 설비 분해·재조립이 전체 유지보수 시간에 영향을 줄 수 있습니다.</p>
    <p>드라이아이스 세척의 가장 큰 차이는 고체 CO₂를 세정 매체로 사용하고, 분사된 드라이아이스가 표면 충돌 후 기체로 승화한다는 점입니다. 따라서 물이나 연마재와 같은 세정 매체가 작업 후 표면에 남지 않는 건식 세척이 가능합니다.</p>
  </div>
  <ul class="cmp-criteria reveal" aria-label="세척 방식 검토 기준">
    <li><span>01</span><b>세정 성능</b></li>
    <li><span>02</span><b>모재 영향</b></li>
    <li><span>03</span><b>2차 폐기물</b></li>
    <li><span>04</span><b>수분 및 건조</b></li>
    <li><span>05</span><b>설비 정지시간</b></li>
    <li><span>06</span><b>작업환경</b></li>
  </ul>
  <p class="cmp-pull reveal">세척 대상은 오염물이지만,<br>보호해야 할 대상은 설비와 제품입니다.</p>
</div>
</div>
</div>

<div class="cmp-section">
  <span class="cmp-eyebrow">AT A GLANCE</span>
  <h2 class="cmp-h2">주요 산업 세척 방식,<br>한눈에 비교해보세요.</h2>
  <div class="cmp-table-wrap reveal">
    <table class="cmp-table">
      <thead>
        <tr><th>세척 방식</th><th>세정 원리</th><th>표면 영향</th><th>세정 매체 잔류</th><th>2차 처리</th><th>수분</th><th>주요 특징</th></tr>
      </thead>
      <tbody>
        <tr class="is-dryice"><td>드라이아이스 세척<small>DRY ICE</small></td><td>고체 CO₂ 입자의 충격·냉각·승화</td><td>비마모성 / 세척 조건 조정 가능</td><td>없음</td><td>제거된 오염물 처리</td><td>없음</td><td>건식 / 비마모 / 세정 매체 잔류 없음</td></tr>
        <tr><td>연마·샌드 블라스팅<small>ABRASIVE</small></td><td>연마 입자의 물리적 충격</td><td>표면 프로파일 또는 표면 변화 가능</td><td>있음</td><td>오염물과 사용 연마재 처리</td><td>없음</td><td>높은 제거력 / 표면처리 가능</td></tr>
        <tr><td>레이저 세정<small>LASER</small></td><td>레이저 에너지</td><td>재질과 공정조건에 따라 달라짐</td><td>없음</td><td>제거물 및 발생 흄 관리</td><td>없음</td><td>정밀한 비접촉 세정</td></tr>
        <tr><td>수작업·화학세척<small>MANUAL / CHEMICAL</small></td><td>물리적 제거 또는 화학적 용해</td><td>도구와 약품에 따라 달라짐</td><td>약품·와이퍼 등 발생 가능</td><td>폐용제 및 소모품 처리</td><td>방식에 따라 다름</td><td>간편하고 범용적 / 인력 의존</td></tr>
        <tr><td>고압수 세척<small>PRESSURE WASHING</small></td><td>고압수의 충격</td><td>압력과 재질에 따라 달라짐</td><td>물이 남음</td><td>폐수 처리</td><td>있음</td><td>넓은 면적의 일반 세척에 효과적</td></tr>
        <tr><td>소다 블라스팅<small>SODA</small></td><td>압축공기로 고형 세정 매체 분사</td><td>–</td><td>작업 후 남음</td><td>소다와 제거 오염물 회수 및 처리</td><td>–</td><td>드라이아이스는 분사 후 승화하지만, 소다는 고형 매체가 작업 후 남음</td></tr>
      </tbody>
    </table>
  </div>
  <p class="cmp-table-note">– 표기는 참고 자료에서 별도로 다루지 않은 항목입니다. 실제 결과는 재질, 오염물, 장비 설정과 작업 환경에 따라 달라질 수 있습니다.</p>
</div>

<div class="cmp-section cmp-rule">
  <span class="cmp-eyebrow">A SIMPLE RULE</span>
  <h2 class="cmp-h2">잘 닦인다는 이유만으로<br>더 거친 도구를 선택하지는 않습니다.</h2>
  <figure class="cmp-rule-photo reveal">
    <img src="../assets/img/rule-pan.png" alt="코팅 프라이팬을 철수세미로 닦는 장면" loading="lazy" />
    <figcaption>일상의 판단 — 코팅 프라이팬에 철수세미를 쓰지 않는 이유는 누구나 알고 있습니다.</figcaption>
  </figure>
  <div class="cmp-rule-grid">
    <div class="cmp-rule-text">
      <div class="cmp-text">
        <p>코팅 프라이팬을 깨끗하게 닦겠다고 철수세미를 사용하지는 않습니다.</p>
        <p>오염은 쉽게 제거될 수 있지만, 반복적인 마찰은 표면과 코팅을 손상시키고 결국 제품의 수명을 단축시킬 수 있기 때문입니다.</p>
        <p>우리는 일상에서도 이미 알고 있습니다. 세척은 단순히 ‘얼마나 잘 닦이는가’만의 문제가 아니라는 것을.</p>
        <p class="cmp-rule-bridge">산업현장도 다르지 않습니다.</p>
        <p>생산설비와 금형은 반복적으로 세척되고, 부품과 제품의 표면 역시 세척 과정에서 본래의 상태를 유지해야 합니다.</p>
        <p>따라서 한 번의 세척 성능뿐 아니라, 세척 과정에서 표면 상태와 치수, 기능과 외관 품질이 얼마나 유지되는지, 그리고 반복적인 세척이 장기적으로 설비와 생산품에 어떤 영향을 주는지까지 함께 고려해야 합니다.</p>
        <p>연마재를 사용하는 세척 방식은 강한 제거력과 표면처리가 필요한 작업에 적합할 수 있습니다. 반면 금형, 설비, 정밀 부품과 제품 표면처럼 원래 상태를 유지하면서 오염물만 제거해야 하는 경우에는 다른 접근이 필요합니다.</p>
      </div>
    </div>
    <figure class="cmp-rule-fig reveal" aria-label="거친 도구의 반복 사용이 표면에 미치는 영향">
      <span class="cmp-rule-fig-label">REPEATED ABRASION</span>
      <ol class="cmp-chain">
        <li><img class="cmp-chain-img" src="../assets/img/rule-step-1.png" alt="" loading="lazy" /><b>철수세미</b><span>거친 도구로 세척</span></li>
        <li><img class="cmp-chain-img" src="../assets/img/rule-step-2.png" alt="" loading="lazy" /><b>표면 스크래치</b><span>코팅·표면에 미세 손상</span></li>
        <li><img class="cmp-chain-img" src="../assets/img/rule-step-3.png" alt="" loading="lazy" /><b>반복 오염</b><span>손상된 표면에 오염이 더 쉽게 고착</span></li>
        <li><img class="cmp-chain-img" src="../assets/img/rule-step-4.png" alt="" loading="lazy" /><b>표면 열화 / 수명 단축</b><span>치수·표면 상태 변화, 설비 수명과 제품 품질에 영향</span></li>
      </ol>
      <figcaption>세척 성능이 아닌, 세척이 반복될 때 표면에 남는 영향의 흐름</figcaption>
    </figure>
  </div>
  <div class="cmp-key reveal">
    <p class="cmp-key-main">좋은 세척은 더 강하게 닦는 것이 아니라,<br>필요한 오염물은 <em>제거</em>하고<br>지켜야 할 표면은 <em>지키는</em> 것입니다.</p>
    <div class="cmp-key-sub">
      <span class="cmp-key-en">CLEANING PERFORMANCE <b>≠</b> AGGRESSIVENESS</span>
      <p>세정 성능과 표면에 가해지는 공격성은<br>같은 의미가 아닙니다.<br>잘 닦이는 것보다 더 중요한 것은,<br>세척 후에도 원래의 상태를 유지하는 것입니다.</p>
    </div>
  </div>
</div>

<div class="cmp-section cmp-vs" id="vs-01" data-n="01">
  <div class="cmp-vs-head reveal">
    <span class="cmp-num">01<span class="cmp-num-of">/ 06</span></span>
    <div>
      <span class="cmp-vs-title">드라이아이스 세척 vs 연마 블라스팅</span>
      <h2 class="cmp-vs-sub">표면까지 제거할 것인가,<br>오염물만 제거할 것인가</h2>
    </div>
  </div>
  <div class="cmp-vs-body is-img-left">
    <figure class="cmp-fig reveal">
      <img src="../assets/img/method-abrasive.jpg" alt="연마 블라스팅 작업" loading="lazy" />
      <figcaption>연마 블라스팅 — 고형 매체를 압축공기로 가속해 오염물을 물리적으로 제거</figcaption>
    </figure>
    <div class="cmp-text">
      <p>연마 블라스팅은 분쇄 유리, 플라스틱 비드, 기타 고형 매체를 압축공기로 가속하여 오염물을 물리적으로 제거하는 방식입니다.</p>
      <p>강한 오염 제거와 표면처리에 효과적이지만, 사용되는 매체와 분사 조건에 따라 표면 침식, 패임 또는 표면 프로파일 변화가 발생할 수 있습니다. 따라서 정밀 금형, 생산설비, 치공구와 정밀 부품처럼 치수와 표면 상태를 유지해야 하는 대상에서는 연마재가 미치는 영향을 충분히 검토해야 합니다.</p>
      <p>작업 후에는 사용된 연마재와 제거된 오염물이 함께 남기 때문에 회수와 처리가 필요합니다.</p>
      <p>드라이아이스는 모스 경도 약 1.5~2 수준의 비교적 부드러운 매체이며, 적절한 분사 조건에서는 모재를 연마하거나 의도적인 표면 프로파일을 형성하지 않고 오염물을 제거하는 데 적합합니다.</p>
      <p>또한 드라이아이스는 충돌 후 기체로 승화하기 때문에 사용한 세정 매체를 별도로 회수할 필요가 없습니다.</p>
    </div>
  </div>
  <p class="cmp-pull reveal">표면을 가공하는 세척과,<br>표면은 유지하면서 오염물만 제거하는 세척은 목적이 다릅니다.<br><small>— 금형뿐 아니라 설비와 부품, 제품 표면에도 같은 기준이 적용됩니다.</small></p>
</div>

<div class="cmp-section cmp-vs" id="vs-02" data-n="02">
  <div class="cmp-vs-head reveal">
    <span class="cmp-num">02<span class="cmp-num-of">/ 06</span></span>
    <div>
      <span class="cmp-vs-title">드라이아이스 세척 vs 샌드 블라스팅</span>
      <h2 class="cmp-vs-sub">강한 제거력이 필요한가,<br>모재 보존이 중요한가</h2>
    </div>
  </div>
  <figure class="cmp-fig cmp-band reveal">
    <img src="../assets/img/method-sand.jpg" alt="샌드 블라스팅 작업" loading="lazy" />
    <figcaption>샌드 블라스팅 — 녹·코팅 제거와 표면 거칠기 형성에 효과적인 대표적 연마 방식. 가공면·치수 관리가 필요한 부품에서는 영향을 먼저 검토</figcaption>
  </figure>
  <div class="cmp-cols">
    <div class="cmp-text">
      <p>샌드 블라스팅은 연마 입자를 고속으로 충돌시켜 오염물이나 표면층을 제거하는 대표적인 방식입니다.</p>
      <p>표면의 녹이나 코팅을 적극적으로 제거하거나 새로운 표면 거칠기를 형성해야 하는 경우에는 매우 효과적인 방법이 될 수 있습니다.</p>
      <p>반면 정밀 금형이나 치수 변화에 민감한 부품에서는 강한 연마 작용으로 인해 표면 패임이나 치수 변화, 표면 거칠기 변화가 발생할 가능성을 고려해야 합니다.</p>
    </div>
    <div class="cmp-text">
      <p>또한 작업 중에는 분진과 사용된 연마재가 발생하므로 작업장 격리, 집진, 개인보호구 및 작업 후 폐사 회수와 처리 등이 필요할 수 있습니다.</p>
      <p>드라이아이스 세척은 표면 자체를 연마하는 방식이 아닙니다. 오염물에 운동에너지와 급격한 온도 변화가 작용하고, 입자가 승화하면서 오염물의 박리를 돕습니다. 가공면, 설비 표면, 치수 관리가 필요한 부품에서도 같은 원리로 적용됩니다.</p>
    </div>
  </div>
  <div class="cmp-conclusion reveal">표면 프로파일을 만드는 것이 목적이라면 <em>샌드 블라스팅</em>이 적합할 수 있으며, 원래 표면 상태를 최대한 유지하면서 오염물을 제거하는 것이 목적이라면 <em>드라이아이스 세척</em>을 검토할 수 있습니다.</div>
</div>

<div class="cmp-section cmp-vs" id="vs-03" data-n="03">
  <div class="cmp-vs-head reveal">
    <span class="cmp-num">03<span class="cmp-num-of">/ 06</span></span>
    <div>
      <span class="cmp-vs-title">드라이아이스 세척 vs 레이저 세정</span>
      <h2 class="cmp-vs-sub">같은 건식 세정이라도<br>적용 방식은 전혀 다릅니다.</h2>
    </div>
  </div>
  <div class="cmp-cols">
    <div class="cmp-text">
      <p>레이저 세정은 레이저 에너지를 이용해 표면의 오염층이나 코팅층을 제거하는 비접촉식 건식 세정 기술입니다.</p>
      <p>세정 매체나 물을 사용하지 않고 특정 영역을 정밀하게 제어할 수 있다는 장점이 있지만, 적용 대상의 재질과 표면 상태, 반사율, 오염물 특성에 따라 레이저 출력·파장·펄스 등 적절한 공정조건을 설정해야 합니다.</p>
      <p>작업 영역과 필요한 처리속도에 따라 장비 투자비와 생산성도 함께 검토할 필요가 있습니다.</p>
    </div>
    <div class="cmp-text">
      <p>드라이아이스 세척은 압축공기, 분사압력, 드라이아이스 입자 크기와 공급량, 노즐 등을 조절해 세척 강도를 폭넓게 설정할 수 있습니다.</p>
      <p>노즐이 접근할 수 있는 복잡한 형상이나 비교적 넓은 설비에도 적용할 수 있다는 점에서 레이저와 다른 특징을 갖습니다.</p>
    </div>
  </div>
  <div class="cmp-duo reveal">
    <div class="cmp-duo-col">
      <img src="../assets/img/method-laser.jpg" alt="레이저 세정 — 정밀 부품 표면" loading="lazy" />
      <div class="cmp-duo-text">
        <span>LASER CLEANING</span>
        <h4>정밀한 비접촉 세정</h4>
        <p>재질과 공정조건에 맞는 정밀 설정</p>
      </div>
    </div>
    <div class="cmp-duo-col">
      <img src="../assets/img/industry-semiconductor.jpg" alt="정밀 부품·전자 부품의 드라이아이스 세척" loading="lazy" />
      <div class="cmp-duo-text">
        <span>DRY ICE CLEANING</span>
        <h4>비마모 건식 세정</h4>
        <p>정밀 부품부터 복잡한 설비 형상까지 대응</p>
      </div>
    </div>
  </div>
</div>

<div class="cmp-section cmp-vs" id="vs-04" data-n="04">
  <div class="cmp-vs-head reveal">
    <span class="cmp-num">04<span class="cmp-num-of">/ 06</span></span>
    <div>
      <span class="cmp-vs-title">드라이아이스 세척 vs 수작업·화학세척</span>
      <h2 class="cmp-vs-sub">실제 세척시간보다 더 긴 것은<br>‘세척을 위한 준비시간’일 수 있습니다.</h2>
    </div>
  </div>
  <div class="cmp-vs-body">
    <div class="cmp-text">
      <p>브러시, 스크레이퍼, 천과 화학용제를 이용한 수작업은 산업현장에서 가장 익숙하고 접근하기 쉬운 세척 방식입니다.</p>
      <p>작은 부품이나 국부 오염에는 효율적일 수 있지만, 생산설비나 복잡한 기계 구조에서는 접근하기 어려운 부분을 위해 설비를 분해하고, 반복적으로 긁고 닦은 뒤 다시 조립해야 하는 시간까지 전체 유지보수 시간에 포함됩니다. 작업자의 숙련도에 따라 결과 편차도 발생할 수 있습니다.</p>
      <p>화학용제를 사용할 경우에는 작업자 노출, 환기, 보관 및 폐용제 처리도 함께 고려해야 합니다.</p>
      <p>특히 일부 설비에서는 세척을 위해 다음과 같은 과정이 필요합니다.</p>
    </div>
    <figure class="cmp-fig reveal">
      <img src="../assets/img/industry-maintenance.jpg" alt="생산설비 정비·수작업 세척" loading="lazy" />
      <figcaption>생산설비와 치공구의 수작업 세척 — 분해와 접근, 재조립까지가 전체 유지보수 시간에 포함된다</figcaption>
    </figure>
  </div>
  <div class="cmp-flow reveal">
    <div class="cmp-flow-row">
      <span class="cmp-flow-label">일반적인 분해 세척</span>
      <ol class="cmp-flow-steps">
        <li>생산 중단</li><li>냉각</li><li>분해</li><li>세척</li><li>건조 또는 잔류물 제거</li><li>재조립</li><li>생산 재개</li>
      </ol>
    </div>
    <div class="cmp-flow-row is-dryice">
      <span class="cmp-flow-label">드라이아이스 세척</span>
      <ol class="cmp-flow-steps">
        <li>정지 또는 공정 준비</li><li>현장 세척</li><li>오염물 회수</li><li>재가동</li>
      </ol>
    </div>
    <p class="cmp-flow-note">무분해 또는 가동 중 세척 가능 여부는 설비 구조, 오염물, 온도 및 현장의 안전조건에 따라 달라집니다.</p>
  </div>
</div>

<div class="cmp-section cmp-vs" id="vs-05" data-n="05">
  <div class="cmp-vs-head reveal">
    <span class="cmp-num">05<span class="cmp-num-of">/ 06</span></span>
    <div>
      <span class="cmp-vs-title">드라이아이스 세척 vs 고압수 세척</span>
      <h2 class="cmp-vs-sub">세척 후 남는 ‘물’까지<br>생각해야 합니다.</h2>
    </div>
  </div>
  <div class="cmp-vs-body is-img-left">
    <figure class="cmp-fig reveal">
      <img src="../assets/img/method-electrical-terminal.png" alt="전기 단자대·배선 — 수분 유입에 민감한 설비 내부" loading="lazy" />
      <figcaption>제어반·단자대·센서·모터 등 설비 내부의 전기·전자 부품 — 물을 쓰는 세척에서는 수분 유입 보호가 먼저 필요하다</figcaption>
    </figure>
    <div class="cmp-text">
      <p>고압수 세척은 넓은 면적의 오염물을 빠르게 제거할 수 있어 산업현장에서 널리 사용되는 방법입니다.</p>
      <p>그러나 물을 사용하는 특성상 전기·전자 장치나 정밀기계에서는 수분 유입을 방지하기 위한 별도의 보호가 필요할 수 있으며, 작업 후에는 폐수 회수와 처리, 건조, 부식 가능성 등을 고려해야 합니다.</p>
      <p>드라이아이스 세척은 물을 사용하지 않는 건식 공정입니다.</p>
      <p>분사된 드라이아이스는 표면에 충돌한 후 기체로 승화하기 때문에 세척수가 남지 않으며 일반적으로 별도의 건조공정이 필요하지 않습니다.</p>
      <p>따라서 전기·전자 부품, 센서와 모터, 생산설비 내부처럼 수분을 최소화해야 하는 대상, 세척 후 빠른 공정 복귀가 필요한 작업, 폐수 관리가 부담되는 현장에서 검토할 가치가 있습니다.</p>
    </div>
  </div>
  <p class="cmp-pull reveal">물을 사용하는 순간,<br>세척은 ‘오염물 제거’만의 문제가 아니게 됩니다.</p>
</div>

<div class="cmp-section cmp-vs is-short" id="vs-06" data-n="06">
  <div class="cmp-vs-head reveal">
    <span class="cmp-num">06<span class="cmp-num-of">/ 06</span></span>
    <div>
      <span class="cmp-vs-title">드라이아이스 세척 vs 소다 블라스팅</span>
      <h2 class="cmp-vs-sub">비슷한 분사 방식,<br>다른 세정 매체</h2>
    </div>
  </div>
  <div class="cmp-vs-body is-compact">
    <div class="cmp-text">
      <p>소다 블라스팅과 드라이아이스 세척은 압축공기를 이용해 세정 매체를 표면에 분사한다는 점에서 유사합니다.</p>
      <p>그러나 가장 큰 차이는 <b>분사한 매체가 세척 후 어떻게 되는가</b>입니다.</p>
      <p>소다를 포함한 일반적인 고형 미디어 블라스팅에서는 분사된 매체와 제거된 오염물을 작업 후 회수하고 처리해야 합니다. 부품의 틈새나 설비 주변에 남은 매체는 후처리 부담으로 이어집니다.</p>
      <p>반면 드라이아이스는 충돌 후 기체로 승화하므로 드라이아이스 자체는 세정 잔재로 남지 않습니다.</p>
    </div>
    <figure class="cmp-fig is-small reveal">
      <img src="../assets/img/method-soda.jpg" alt="소다 블라스팅" loading="lazy" />
    </figure>
  </div>
</div>

    </div>
  </section>

  <nav class="cmp-rail" aria-label="비교 섹션 바로가기">
    <a href="#vs-01"><i></i>01</a><a href="#vs-02"><i></i>02</a><a href="#vs-03"><i></i>03</a><a href="#vs-04"><i></i>04</a><a href="#vs-05"><i></i>05</a><a href="#vs-06"><i></i>06</a>
  </nav>
  <section class="cmp-dark">
    <div class="wrap">
      <div class="cmp-dark-top">
      <span class="cmp-dark-q" aria-hidden="true">?</span>
      <span class="cmp-eyebrow">THE RIGHT METHOD</span>
      <h2 class="cmp-h2">그렇다면,<br>드라이아이스 세척이 항상 정답일까요?</h2>
      <p class="cmp-dark-sub">모든 세척 방식에는 적합한 목적이 있습니다.</p>
      <div class="cmp-dark-body">
        <p>드라이아이스 세척은 금형, 생산설비, 치공구, 정밀 부품 및 제품 표면 등 본래의 표면 상태를 유지하면서 오염물을 제거해야 하는 다양한 산업 현장에서 강점을 가질 수 있습니다. 하지만 모든 오염물과 모든 목적에 적합한 것은 아닙니다.</p>
        <p>표면 프로파일 형성, 강한 녹 제거, 의도적인 표면 가공 등이 필요한 경우 — 예를 들어 도장 전 표면 프로파일을 만들거나 깊게 피팅된 부식을 제거해야 하는 경우에는 연마재를 사용하는 방식이 더 적합할 수 있습니다.</p>
        <p>또한 모재에 강하게 결합된 일부 도료나 코팅은 드라이아이스만으로 제거속도가 충분하지 않거나 제거가 어려울 수 있습니다.</p>
        <p>드라이아이스 세척에는 압축공기와 드라이아이스 공급이 필요하며, 특히 밀폐되거나 환기가 충분하지 않은 장소에서는 승화된 CO₂의 축적을 방지하기 위해 적절한 환기와 CO₂ 농도 관리가 필요합니다.</p>
      </div>
      </div>
      <p class="cmp-dark-final reveal">중요한 것은 어떤 세척 방식이 <em>가장 강한가</em>가 아니라,<br>내 설비와 오염물에 어떤 방식이 <em>가장 적합한가</em>입니다.</p>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail">
    <div class="wrap">

<div class="cmp-section is-first">
  <span class="cmp-eyebrow">TOTAL CLEANING COST</span>
  <h2 class="cmp-h2">세척 비용은<br>장비 가격만으로 결정되지 않습니다.</h2>
  <p class="cmp-sub">세척 공정 전체의 비용을 함께 보세요.</p>
  <div class="cmp-lead">
    <p>장비 가격과 소모품 비용은 세척 방식 선택의 중요한 요소입니다. 하지만 산업현장에서는 그것만으로 실제 세척비용을 판단하기 어렵습니다.</p>
    <p>세척을 위해 설비가 멈추는 시간, 투입되는 작업자 수, 설비의 분해와 재조립, 세척 후 건조, 사용한 매체와 폐수의 처리, 그리고 반복적인 세척이 표면과 설비 수명, 생산품 품질에 미치는 영향까지 포함해야 실제 비용에 가까워집니다.</p>
  </div>
  <div class="cmp-cost-panel">
  <span class="cmp-cost-label">FORMULA</span>
  <div class="cmp-cost reveal">
    <span class="cmp-cost-total">TOTAL CLEANING COST</span>
    <span class="cmp-cost-eq">=</span>
    <span class="cmp-cost-item">Cleaning Time</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Labor</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Downtime</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Disassembly</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Drying</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Waste Treatment</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Surface Damage</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Equipment Life</span><span class="cmp-cost-plus">+</span>
    <span class="cmp-cost-item">Product Quality</span>
  </div>
  </div>
  <p class="cmp-pull reveal">세척하는 시간뿐 아니라,<br>세척이 설비와 제품에 남기는 영향까지 비교해보세요.</p>
</div>

<div class="cmp-section cmp-cta">
  <div class="cmp-cta-left">
    <h2 class="cmp-h2">우리 현장에는<br>어떤 세척 방식이 적합할까요?</h2>
    <p class="cmp-sub">세척 대상이 같아도 조건에 따라 결과는 달라질 수 있습니다.</p>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>오염물의 종류와 두께, 모재의 재질과 표면상태, 작업 온도, 설비의 형상과 접근성에 따라 적합한 세척 방식과 조건은 달라집니다.</p>
      <p>드라이아이스 세척 역시 압력만 높인다고 더 좋은 결과가 나오는 것은 아닙니다. 드라이아이스 입자 크기, 공급량, 압축공기 조건, 노즐 형태와 분사거리 등을 세척 대상에 맞게 설정하는 것이 중요합니다.</p>
      <p>따라서 도입 전에는 실제 부품이나 시편을 이용해 세척 가능 여부와 처리시간을 확인하고 기존 방식과 비교해보는 것이 가장 확실합니다.</p>
      <p>바테크는 실제 세척 테스트를 통해 적용 가능성을 확인하고, 현장 조건에 맞는 장비와 세척 조건을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기</a>
    </div>
    <p class="cmp-cta-fine">도입하기 전에, 실제 세척 결과부터 확인해보세요.</p>
  </div>
</div>

    </div>
  </section>
<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차, 식품, 반도체·PCB, 금형, 인쇄, 발전, 조선 등 산업별로 어떤 문제를 해결하는지 설명합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="adopt.html">
    <div class="sub-card-media"><img src="../assets/img/adopt-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">도입 절차</span>
      <h3 style="font-size: 25px">도입 가이드</h3>
      <p style="font-size: 20px">도입 전 검토사항부터 설치 준비, 운영 체크리스트까지 순서대로 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">실제 부품으로 세척 테스트를 받아보세요</h3>
          <p style="font-size: 20px">세척 가능 여부와 처리시간을 확인하고, 기존 방식과 직접 비교할 수 있습니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

COMPARE_RAIL_SCRIPT = """  <script>
  (function(){
    var secs=[].slice.call(document.querySelectorAll('.cmp-vs[id]')),rail=document.querySelector('.cmp-rail');
    if(!secs.length||!rail)return;
    var links={};rail.querySelectorAll('a').forEach(function(a){links[a.getAttribute('href').slice(1)]=a;});
    var pending=false;
    function update(){
      pending=false;
      var line=window.innerHeight*0.35,active=null;
      secs.forEach(function(s){var r=s.getBoundingClientRect();if(r.top<=line&&r.bottom>line)active=s.id;});
      rail.classList.toggle('is-on',!!active);
      Object.keys(links).forEach(function(k){links[k].classList.toggle('is-active',k===active);});
    }
    function onScroll(){if(!pending){pending=true;requestAnimationFrame(update);}}
    window.addEventListener('scroll',onScroll,{passive:true});
    window.addEventListener('resize',onScroll);
    update();
    rail.addEventListener('click',function(e){
      var a=e.target.closest('a[href^="#"]');if(!a)return;
      var t=document.getElementById(a.getAttribute('href').slice(1));if(!t)return;
      e.preventDefault();
      window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-96,behavior:'smooth'});
    });
  })();
  </script>
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
  <tr><th>드라이아이스 공급</th><td>펠렛과 마이크로파티클의 특성, 공급 방식, 보관 조건, 작업별 사용량 검토</td></tr>
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

<h2 style="font-size:20px; margin-top:36px;">펠렛 vs 마이크로파티클</h2>
<div class="content-photo"><img src="../assets/img/adopt-pellet-vs-micro.jpg" alt="펠렛과 마이크로파티클 비교" loading="lazy" /></div>
<p class="photo-caption">약 3mm 펠렛(왼쪽)과 약 0.3mm 마이크로파티클(오른쪽) 비교 (참고: Cold Jet 공식 기술자료 p.27)</p>
<p>매뉴얼은 약 3&nbsp;mm 펠렛을 고착된 오염물이나 강한 세정력이 필요한 작업에, 약 0.3&nbsp;mm
마이크로파티클을 섬세하고 민감한 표면 세정에 적합한 형태로 설명합니다. 적절한 단열 용기에 보관할 경우
최대 약 1주일간 사용할 수 있으나, 기후와 용기 성능에 따라 하루 약 2~10%가 승화할 수 있으므로 사용
일정에 맞춘 공급 계획이 중요합니다.</p>
<div class="content-photo" style="max-width:380px;"><img src="../assets/img/adopt-pelletizer.jpg" alt="드라이아이스 펠레타이저" loading="lazy" /></div>
<p class="photo-caption">현장에서 직접 생산할 경우 사용하는 드라이아이스 펠레타이저 예시 (참고: Cold Jet 공식 기술자료 p.27)</p>

<h2 style="font-size:20px; margin-top:36px;">압축공기 조건</h2>
<table class="spec-table">
  <tr><th>펠렛 타입</th><td>약 2.8 m³/min(100 CFM), 5.5 bar(80 PSI) 수준</td></tr>
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
    <p class="faq-a">매뉴얼은 약 3mm 펠렛을 고착된 오염물과 강한 세정이 필요한 경우에, 약 0.3mm
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
    <p class="faq-a">매뉴얼의 일반 기준은 펠렛 타입 약 2.8 m³/min(100 CFM), 5.5 bar(80 PSI),
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
        "nav_intro": "세척 원리부터 산업별 적용과 도입까지 한눈에 살펴보세요.",
        "subs": [
            {"slug": "guide", "title": "드라이아이스 세척의 이해",
             "desc": "드라이아이스 세척의 원리, 장점, 자주 묻는 질문을 한 곳에 정리했습니다.",
             "nav_desc": "드라이아이스의 물리적 특성부터 세척 원리와 주요 장점, 기존 세척 방식과의 차이, 드라이아이스 세척 장비의 기본 개념까지 체계적으로 살펴보세요.",
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
             # (2026-09-07) 페이지 자체의 <title>/메타 설명/H1은 새 편집형 디자인에
             # 맞춰 "타 세척방식과의 비교"로 바뀌지만, 이 title/desc/nav_desc
             # 필드는 메가메뉴·허브 카드·타 페이지의 "함께 보면 좋은 페이지"
             # 카드 등 사이트 전역에서 공유되며 핸드오프 검증 결과 그 쪽은
             # 변경되지 않았으므로 그대로 둔다. page_title/page_desc로 이 페이지
             # 자신의 head 태그만 별도로 덮어쓴다.
             "page_title": "타 세척방식과의 비교",
             "page_desc": "오염물은 제거하되 금형·생산설비·부품 및 제품 표면은 지키는 세척 — 표면 영향, 2차 폐기물, 수분, 설비 정지시간을 기준으로 드라이아이스 세척과 연마·샌드·레이저·화학·고압수·소다 블라스팅을 비교합니다.",
             "full_custom_body": True,
             "extra_script": COMPARE_RAIL_SCRIPT,
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
  <div class="header-peek">
    <button class="peek-toggle" aria-label="메뉴 열기">☰</button>
  </div>
"""


def footer_html(depth):
    # (2026-09-05, 후속: 4차 디자인 개선 핸드오프) 푸터 전면 재설계 — 1)선언/CTA
    # 행, 2)5칼럼(브랜드+세척가이드+제품·자동화·공급+사례·지원+문의하기),
    # 3)하단 바(저작권+약관/개인정보 링크+맨위로) 3단 구성. 화면 높이에 맞춰
    # 딱 한 화면(100vh)만 차지하도록 style.css 쪽에서 vh 기반 clamp()로
    # 크기를 조절하므로 여기서는 마크업 구조만 고정 — 카테고리 컬럼도 더는
    # MENU 순회로 자동 생성하지 않고(5칼럼 레이아웃에 맞춰 항목 구성이
    # MENU 대표 3개 노출 규칙과 달라짐) 디자인 그대로 하드코딩한다.
    return f"""
  <div class="footer-reveal-wrap">
    <div class="footer-spacer" aria-hidden="true"></div>

  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-hero">
          <div class="footer-watermark" aria-hidden="true">
            <span class="footer-wm-text">VATEK</span>
            <span class="footer-wm-ko">바테크</span>
          </div>
        <div class="footer-hero-main">
          <span class="footer-eyebrow">VATEK · COLD JET KOREA</span>
          <h2>도입 검토부터 현장 적용, <br>교육과 A/S까지<br><em>바테크</em>가 전 과정을 지원합니다.</h2>
          <p>설비 특성, 오염 상태, 작업 환경을 고려해 현장에 맞는 최적의 솔루션을 제안합니다.</p>
          <div class="footer-cta">
            <a class="footer-btn is-primary" href="{asset('products/index.html', depth)}">제품 살펴보기 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
            <a class="footer-btn" href="{asset('rental/index.html', depth)}">렌탈 · 데모 <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
          </div>
        </div>
      </div>
      <div class="footer-top">
        <div class="footer-brand">
          <a class="logo footer-logo" href="{asset('index.html', depth)}"><img src="{asset('assets/img/vatek-logo-wordmark.png', depth)}" alt="VATEK" /></a>
          <p>드라이아이스 블라스터·펠렛타이저·리커버리 및 관련 소모품을 공급하는 Cold Jet 대한민국 공식 대리점</p>
          <span class="partner-badge"><img src="{asset('assets/img/coldjet-logo.png', depth)}" alt="Cold Jet" /><b>대한민국 <br>공식 대리점</b></span>
          <span class="footer-microcap">OFFICIAL DISTRIBUTOR IN KOREA</span>
        </div>
        <div class="footer-col"><h4>세척 가이드</h4><ul><li><a href="{asset('cleaning/guide.html', depth)}">드라이아이스 세척의 이해</a></li><li><a href="{asset('cleaning/compare.html', depth)}">타 세척방식과 비교</a></li><li><a href="{asset('cleaning/industry.html', depth)}">산업별 솔루션</a></li><li><a href="{asset('cleaning/task.html', depth)}">작업별 솔루션</a></li><li><a href="{asset('cleaning/adopt.html', depth)}">도입 가이드</a></li></ul></div>
        <div class="footer-col"><h4>제품·자동화·공급</h4><ul><li><a href="{asset('products/blaster/index.html', depth)}">드라이아이스 세척기</a></li><li><a href="{asset('products/pelletizer/index.html', depth)}">드라이아이스 제조기</a></li><li><a href="{asset('products/recovery/index.html', depth)}">CO<sub>2</sub> 리커버리</a></li><li><a href="{asset('products/automation.html', depth)}">자동화 시스템</a></li><li><a href="{asset('products/supply.html', depth)}">드라이아이스 구매</a></li></ul></div>
        <div class="footer-col"><h4>사례·지원</h4><ul><li><a href="{asset('cases/library.html', depth)}">적용사례 라이브러리</a></li><li><a href="{asset('cases/testimonials.html', depth)}">고객 후기·추천사</a></li><li><a href="{asset('rental/index.html', depth)}">렌탈·데모</a></li><li><a href="{asset('support/catalog.html', depth)}">카탈로그 다운로드</a></li><li><a href="{asset('support/techsupport.html', depth)}">기술지원 서비스</a></li></ul></div>
        <div class="footer-contact">
          <h4>문의하기</h4>
          <a class="footer-tel" href="tel:0317964300"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6.2 6.2l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg><span>031-796-4300</span></a>
          <a class="footer-line" href="mailto:sales@vatek.co.kr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg><span>sales@vatek.co.kr</span></a>
          <p class="footer-line"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg><span>평일 09:00 – 18:00 <i>|</i> 주말·공휴일 휴무</span></p>
          <p class="footer-line"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.3 7-12a7 7 0 1 0-14 0c0 5.7 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg><span>경기도 하남시 산곡동로14번길 20</span></p>
          <span class="footer-microcap footer-microcap-line">CLEANER INDUSTRY<br>GREENER TOMORROW</span>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 주식회사 바테크. All rights reserved.</span>
        <nav class="footer-legal"><a href="{asset('company/about.html', depth)}">회사소개</a><a href="{asset('company/location.html', depth)}">위치·연락처</a><a href="#">이용약관</a><a href="#">개인정보처리방침</a></nav>
        <a class="footer-totop" href="#" aria-label="맨 위로"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M6 11l6-6 6 6"/></svg> TOP</a>
      </div>
    </div>
  </footer>
  </div>
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


def page_shell(title, description, depth, active_code, body, is_home=False, extra_script=""):
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
{footer_html(depth)}{extra_script}
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
    if s.get("full_custom_body"):
        # (2026-09-07, 5차 디자인 개선 핸드오프) "타 세척방식과의 비교" 페이지 —
        # 히어로 패럴랙스 + 신뢰 섹션(.cmp-dark) + 우측 고정 레일(01~06) +
        # 별도 CTA/비용 패널까지 구조가 기존 hero_parallax 템플릿(단일
        # subhero-cover + 공용 last-freeze 꼬리말)과 크게 달라 공용 로직을
        # 재사용하지 않고, 핸드오프로 받은 본문 전체(히어로~함께 보면 좋은
        # 페이지까지)를 있는 그대로 사용한다. 우측 레일 활성화 스크립트는
        # footer_html() 뒤(메인 main.js 스크립트 태그 다음)에 와야 하므로
        # page_shell()의 extra_script 인자로 별도 전달.
        body = s["body"]
    elif s.get("hero_parallax"):
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
      {main_block.rstrip()}
    </div>
  </section>
<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차, 식품, 반도체·PCB, 금형, 인쇄, 발전, 조선 등 산업별로 어떤 문제를 해결하는지 설명합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="adopt.html">
    <div class="sub-card-media"><img src="../assets/img/adopt-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">도입 절차</span>
      <h3 style="font-size: 25px">도입 가이드</h3>
      <p style="font-size: 20px">도입 전 검토사항부터 설치 준비, 운영 체크리스트까지 순서대로 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">바테크에 직접 문의해보세요</h3>
          <p style="font-size: 20px">현장 상황에 맞는 가장 정확한 답변을 담당자가 안내해 드립니다.</p>
        </div>
        <a class="cta-btn" href="../products/quote.html">견적문의 하기</a>
      </div>
      </div>
    </div>
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
    page_title = s.get("page_title", s["title"])
    page_desc = s.get("page_desc", s["desc"])
    html = page_shell(page_title, page_desc, depth, m["code"], body, extra_script=s.get("extra_script", ""))
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
