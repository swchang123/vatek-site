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

# (2026-09-08, 8차 핸드오프) 산업 상세 페이지 "자동차 제조" — industries/automotive.html.
# 메가메뉴에는 나오지 않는 상세 페이지라 MENU가 아니라 아래 DETAIL_PAGES로 생성한다
# (헤더·메가메뉴·푸터는 cleaning/*와 같은 depth=1 셸, active_code는 "cleaning").
# 본문(히어로~함께 보면 좋은 페이지)은 핸드오프 HTML이 정본이라 통째로 보관.
AUTOMOTIVE_BODY = """
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/ind-card-automotive.png" aria-label="자동차 제조 현장 드라이아이스 세척">
      <source src="../assets/video/auto-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 자동차 제조</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">AUTOMOTIVE MANUFACTURING</span>
      <h1>자동차 제조</h1>
      <p class="cmp-hero-p auto-hero-lead">자동차 생산의 여러 공정에서 세척은 품질과 설비 관리의 중요한 과정입니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">AUTOMOTIVE PRODUCTION</span>
      <h2 class="cmp-h2">하나의 자동차가 만들어지는 동안,<br>세척해야 할 대상도 계속 달라집니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>자동차 생산라인에는 플라스틱과 고무 부품의 성형공정부터 차체 용접, 도장, 다이캐스팅, 부품 조립과 각종 후처리 공정까지 서로 다른 생산설비가 함께 운영됩니다.</p>
      <p>금형에는 이형제와 수지, 성형 과정에서 발생한 잔류물이 쌓이고, 용접 지그와 로봇 주변에는 용접 스패터와 슬래그가 축적됩니다. 도장라인에는 도료 비산 잔류물(오버스프레이)이, 다이캐스팅 공정에는 이형제와 윤활제, 카본 등이 남을 수 있습니다.</p>
      <p>이러한 오염은 단순히 설비가 더러워지는 문제에 그치지 않습니다. 오염이 축적되면 금형과 치공구의 상태, 센서와 설비의 작동, 제품의 품질, 정비 주기와 생산 중단시간에도 영향을 줄 수 있습니다.</p>
      <p class="auto-intro-close">따라서 자동차 제조에서의 세척은 생산과 별개의 청소 작업이 아니라, <b>공정을 안정적으로 유지하기 위한 설비 관리의 한 부분</b>으로 볼 필요가 있습니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/auto-production-line.jpg" alt="자동차 차체 조립라인의 산업용 로봇" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">자동차 제조에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PLASTIC & RUBBER MOLD CLEANING</span>
      <h3>사출 · 성형 금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-rubber-mold.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">금형의 정밀한 표면은 유지하면서<br>생산 잔류물을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>자동차의 내·외장재와 씰, 가스켓, 커넥터 등 다양한 부품은 플라스틱과 고무 성형공정을 통해 생산됩니다.</p><p>생산이 반복되면 금형 표면에는 이형제, 수지, 안료와 성형 과정에서 발생한 잔류물이 축적될 수 있습니다. 이러한 오염은 성형 품질과 금형 관리에 영향을 줄 수 있기 때문에 정기적인 세척이 필요합니다.</p><p>드라이아이스 세척은 비마모성 세정 방식의 특성을 이용해 금형의 표면과 형상을 최대한 유지하면서 축적된 오염물을 제거하는 데 활용됩니다. 설비와 금형의 조건에 따라 금형을 완전히 분해하거나 충분히 냉각한 뒤 세척해야 하는 시간을 줄일 수 있는 경우도 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>플라스틱 사출금형</li><li>고무 성형금형</li><li>우레탄 성형금형</li><li>정밀 성형금형</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">ROBOTIC WELD CELL CLEANING</span>
      <h3>용접라인 · 지그 · 로봇 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-welding-robot.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">용접 스패터는 제거하고,<br>지그와 센서의 상태는 유지합니다.</p>
      <div class="cmp-text auto-text"><p>자동차 차체 용접공정에서는 용접 스패터와 슬래그가 지그, 클램프, 로봇과 센서 주변에 지속적으로 쌓일 수 있습니다.</p><p>오염이 심해지면 지그의 위치 정밀도나 센서의 정상적인 작동에 영향을 줄 수 있고, 결과적으로 정비가 필요한 시점도 빨라질 수 있습니다.</p><p>드라이아이스 세척은 연마나 강한 기계적 제거가 부담되는 지그와 로봇, 센서 주변의 오염물을 제거하는 방법으로 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>용접 지그</li><li>클램프</li><li>용접 로봇</li><li>근접센서</li><li>용접 테이블</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">PAINT BOOTH & COATING LINE CLEANING</span>
      <h3>도장부스 · 코팅라인 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-paint-booth-fixture.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-paint-prep.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">도료가 축적되는 설비를<br>정기적으로 관리합니다.</p>
      <div class="cmp-text auto-text"><p>도장공정에서는 분사된 도료의 일부가 부스 내부와 지그, 행거, 캐리어, 컨베이어 등에 지속적으로 쌓입니다.</p><p>이렇게 축적된 도료와 코팅 잔류물은 설비의 움직임이나 접지 상태, 도장환경 관리에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 물을 사용하지 않는 건식 방식이며, 드라이아이스 자체가 작업 후 세정 잔재로 남지 않기 때문에 도장·코팅설비의 유지보수에 활용할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>도장부스</li><li>도장 지그</li><li>행거</li><li>캐리어</li><li>컨베이어</li><li>가이드레일</li><li>로봇</li><li>그레이팅</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">DIE CASTING & FOUNDRY</span>
      <h3>다이캐스팅 · 주조 공정</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-diecast-die.jpg" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-diecast-corebox.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">반복적으로 오염되는 금형과 치공구를<br>표면 상태를 고려해 세척합니다.</p>
      <div class="cmp-text auto-text"><p>자동차 제조에서는 알루미늄을 비롯한 다양한 금속 부품을 다이캐스팅과 주조공정으로 생산합니다.</p><p>반복 생산 과정에서 금형과 코어박스 등에는 이형제, 다이캐스팅용 윤활제, 수지, 카본, 내화성 코팅 잔류물 등이 축적될 수 있습니다.</p><p>드라이아이스 세척은 비마모성 세정 방식의 특성을 이용해 금형과 치공구의 주요 표면과 형상을 유지하면서 이러한 오염물을 제거하는 데 활용됩니다.</p></div>
      <a class="auto-rel-link" href="../industries/foundry.html"><span>관련 산업</span>주조 · 다이캐스팅 <i>→</i></a>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">SURFACE PREPARATION</span>
      <h3>표면 전처리</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-adhesive-component.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">도장과 접착 전에,<br>표면의 오염부터 제거합니다.</p>
      <div class="cmp-text auto-text"><p>자동차 부품의 도장이나 코팅, 접착과 실링 작업 전에는 표면에 남아 있는 오일, 이형제, 먼지와 공정 잔류물이 후속 공정에 영향을 주지 않도록 관리해야 합니다.</p><p>드라이아이스 세척은 물을 사용하지 않고 세정 매체가 표면에 남지 않는 특성을 이용해 도장이나 접착 전 표면을 준비하는 공정에 활용할 수 있습니다.</p><p>물세척과 달리 세척 후 수분 제거를 위한 별도 건조공정의 부담을 줄일 수 있다는 것도 장점 중 하나입니다.</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-06">
  <div class="auto-app-head reveal">
    <span class="auto-num">06</span>
    <div>
      <span class="auto-en">DEBURRING & DEFLASHING <em class="auto-fin">PARTS FINISHING</em></span>
      <h3>디버링 · 디플래싱</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/task-deburring-plastic.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">불필요한 버와 플래시는 제거하고,<br>부품의 형상은 유지합니다.</p>
      <div class="cmp-text auto-text"><p>플라스틱이나 고무 부품은 성형 또는 가공 후 가장자리나 작은 틈에 버(Burr) 또는 플래시(Flash)가 남을 수 있습니다.</p><p>드라이아이스 기술은 필요한 부분에 세척 강도를 조절해 버와 플래시를 제거하면서 부품의 주요 형상과 치수 변화를 최소화해야 하는 부품 마무리 공정에 활용됩니다.</p></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-07">
  <div class="auto-app-head reveal">
    <span class="auto-num">07</span>
    <div>
      <span class="auto-en">PRODUCTION EQUIPMENT & FACILITY MAINTENANCE</span>
      <h3>생산설비 · 시설 유지보수</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-facility-panel.jpg" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">자동차 공장에는 금형과 생산라인 외에도<br>관리해야 할 설비가 많습니다.</p>
      <div class="cmp-text auto-text"><p>자동차 공장은 금형과 용접·도장설비뿐 아니라 가공장비, 컨베이어, 모터, 제어반, 냉각설비와 물류장비 등 수많은 생산지원설비로 구성됩니다.</p><p>이러한 설비에는 오일과 그리스, 카본, 먼지와 각종 공정 잔류물이 지속적으로 쌓일 수 있습니다.</p><p>드라이아이스의 건식·비마모 특성은 물이나 연마재 사용이 부담스러운 다양한 설비의 유지보수 세척에 활용할 수 있습니다.</p></div>
      <p class="auto-note">전기·전자 장비의 경우 비전도성 세정 방식이라는 장점이 있지만, 실제 작업 가능 여부는 설비의 구조와 전원 상태, 현장의 안전조건을 반드시 함께 검토해야 합니다.</p>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">자동차 생산공정에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>이형제</b><small>RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/auto-rubber-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>수지 · 성형 잔류물</b><small>RESIN & PROCESS RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>용접 스패터</b><small>WELD SPATTER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/auto-weld-cell.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>슬래그</b><small>SLAG</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>도료 비산 잔류물</b><small>PAINT OVERSPRAY</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 · 그리스</b><small>OIL & GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/auto-pur-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제</b><small>ADHESIVE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/ind-card-foundry.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본</b><small>CARBON</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.48s"><img src="../assets/img/auto-pressing-tool.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>기타 공정 잔류물</b><small>OTHER PROCESS RESIDUE</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">자동차 제조에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>표면을 연마하지 않는 세척</b><p>금형과 치공구, 정밀 부품처럼 표면 상태와 치수를 유지해야 하는 대상에 적용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>물을 사용하지 않는 건식 세척</b><p>수분 관리가 중요한 도장공정과 전기·전자 설비, 각종 정밀장치의 세척에 활용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 표면에 충돌한 뒤 기체로 승화하기 때문에 사용한 드라이아이스 자체를 별도로 회수할 필요가 없습니다. 제거된 오염물은 별도로 회수하고 처리해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>분해와 정비시간을 줄일 수 있는 가능성</b><p>설비와 작업 조건에 따라 부품이나 금형을 완전히 분리하지 않고 현장에서 세척할 수 있는 경우가 있습니다. 이를 통해 세척을 위한 냉각, 분해, 재조립 등에 필요한 시간을 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>한 공장 안의 다양한 공정에 적용</b><p>금형, 용접라인, 도장설비, 다이캐스팅, 표면 전처리, 부품 마무리, 생산지원설비까지 — 자동차 공장 안의 서로 다른 세척 과제에 적용 가능성을 검토할 수 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 자동차 공장에서도,<br>공정마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>사출금형에 쌓이는 이형제와 용접 지그의 스패터, 도장라인의 도료 잔류물은 같은 자동차 공장에서 발생하지만 오염물의 성질과 세척 대상, 작업 조건은 서로 다릅니다.</p>
            <p>바테크는 오염물의 종류와 부착 정도, 세척 대상의 재질과 형상, 작업 환경과 원하는 결과를 확인한 뒤 실제 테스트를 통해 적용 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><b>사출금형</b><small>이형제 · 수지</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><b>용접 지그</b><small>스패터 · 슬래그</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><b>도장라인</b><small>도료 비산 잔류물</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">자동차 제조에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">자동차 생산 안에서도 세척 대상과 작업 목적에 따라 필요한 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/weld-fixture-robot.html"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>WELD LINE, FIXTURE & ROBOT CLEANING</small><b>용접라인 · 지그 · 로봇 세척</b><span>지그·클램프·로봇·센서 주변의 스패터와 슬래그</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/paint-booth-coating-line.html"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PAINT BOOTH & COATING LINE CLEANING</small><b>도장부스 · 코팅라인 세척</b><span>부스·행거·캐리어·컨베이어의 도료 비산 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/auto-adhesive-component.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/deburring-deflashing.html"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>DEBURRING & DEFLASHING</small><b>디버링 · 디플래싱</b><span>성형·가공 후 버와 플래시를 제거하는 부품 마무리</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.35s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/stackdo-automation.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">자동차 생산과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">자동차 제조에는 플라스틱 사출, 고무부품 성형, 다이캐스팅 등 서로 다른 제조기술이 함께 사용됩니다. 해당 공정을 산업 전체의 관점에서 더 자세히 보려면 관련 산업 페이지를 확인하세요.</p>
  </div>
  <ul class="auto-relind">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/rubber-tires.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-rubber-tire.png" alt="" loading="lazy" /></span><small>RUBBER & TIRES</small><b>고무 · 타이어</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/foundry.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-foundry.png" alt="" loading="lazy" /></span><small>FOUNDRY & DIE CASTING</small><b>주조 · 다이캐스팅</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN AUTOMOTIVE PLANTS</span>
      <h2 class="cmp-h2">글로벌 자동차 제조 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">세계 주요 자동차 제조사와 부품업체가 다양한 생산공정에서 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos" aria-label="Cold Jet 드라이아이스 세척을 사용하는 자동차 제조사">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:60%"><img src="../assets/img/logo-hyundai.webp" alt="Hyundai" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:66%"><img src="../assets/img/logo-kia.png" alt="Kia" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:44%"><img src="../assets/img/logo-honda.webp" alt="Honda" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:40%"><img src="../assets/img/logo-gm.webp" alt="General Motors" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:58%"><img src="../assets/img/logo-ford.webp" alt="Ford" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:46%"><img src="../assets/img/logo-citroen.webp" alt="Citroën" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:78%"><img src="../assets/img/logo-chrysler.webp" alt="Chrysler" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:42%"><img src="../assets/img/logo-bmw.webp" alt="BMW" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:42%"><img src="../assets/img/logo-volkswagen.webp" alt="Volkswagen" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:50%"><img src="../assets/img/logo-toyota.webp" alt="Toyota" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.40s; --w:44%"><img src="../assets/img/logo-tesla.webp" alt="Tesla" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.44s; --w:70%"><img src="../assets/img/logo-renault.webp" alt="Renault" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.48s; --w:48%"><img src="../assets/img/logo-nissan.webp" alt="Nissan" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 생산라인에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 자동차 공정이라도 오염물의 종류와 부착 정도, 설비의 재질과 형상, 작업 온도와 접근성에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 실제 테스트를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

# 07 블록(.auto-freeze) 틀고정 패럴랙스 — main.js 다음, </body> 앞에 삽입.
AUTOMOTIVE_SCRIPT = """  <script>
  (function(){
    // 07 생산설비·시설 유지보수 — 제목이 헤더 아래 도달하면 스크롤 속도의 15%로만 천천히 올라가고,
    // 뒤따르는 COMMON CONTAMINANTS 패널(불투명·z-index 2)이 그 위를 덮으며 올라온다. 푸터 리빌과 같은 방식으로
    // 덮이는 비율에 맞춰 블러(0~10px)를 준다.
    var fz=document.querySelector('.auto-freeze'),panel=document.querySelector('.auto-cont-panel');
    if(!fz||!panel||window.matchMedia('(max-width: 900px)').matches)return;
    var HEADER=76,RATE=0.85,BLUR_MAX=10,ty=0;
    function docTop(){return fz.getBoundingClientRect().top+window.pageYOffset-ty;}
    function upd(){
      var top=docTop(),h=fz.offsetHeight,p=window.pageYOffset+HEADER-top;
      if(p<=0){ty=0;fz.style.transform='';fz.style.filter='';return;}
      var max=h+240;ty=Math.min(p*RATE,max);
      // 블러는 덮고 올라오는 패널이 화면 절반을 넘긴 시점부터 시작 → 패널 상단이 헤더에 닿을 때 최대
      var vh=window.innerHeight,pt=panel.getBoundingClientRect().top;
      var covered=(vh-pt)/vh; var ratio=Math.max(0,Math.min(1,(covered-0.5)/0.45));
      fz.style.transform='translate3d(0,'+ty.toFixed(1)+'px,0)';
      fz.style.filter=ratio>0.02?'blur('+(ratio*BLUR_MAX).toFixed(2)+'px)':'';
    }
    var t=false;
    window.addEventListener('scroll',function(){if(t)return;t=true;requestAnimationFrame(function(){t=false;upd();});},{passive:true});
    window.addEventListener('resize',upd);
    upd();
  })();
  </script>
"""

# (2026-09-08, 9차 핸드오프) 산업 상세 15종 — 자동차 페이지와 같은 구조. 본문은 핸드오프 HTML이 정본.
PLASTICS_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/plastics-composites/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/ind-card-plastics.png" aria-label="플라스틱 · 복합소재 현장">
      <source src="../assets/video/plastics-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 플라스틱 · 복합소재</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">PLASTICS & COMPOSITES</span>
      <h1>플라스틱 · 복합소재</h1>
      <p class="cmp-hero-p auto-hero-lead">금형 표면에 쌓이는 이형제와 수지는 곧 제품 표면의 품질 문제로 이어집니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">PLASTICS & COMPOSITES PRODUCTION</span>
      <h2 class="cmp-h2">금형이 깨끗해야<br>부품도 깨끗하게 나옵니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>플라스틱 제조현장에는 사출·압출·블로우 성형기와 금형, 성형 후 부품을 마무리하는 후가공 공정, 도장이나 코팅을 위한 전처리 공정, 그리고 복합소재를 성형하는 툴링이 함께 운영됩니다.</p>
      <p>생산이 반복될수록 금형 표면에는 이형제와 수지에서 발생한 가스 잔류물(오프가스), 경화된 수지, 안료 잔류물이 쌓입니다. 복합재 툴링에는 이형제와 수지, 젤코트가 축적되고, 성형된 부품에는 버와 플래시가 남습니다.</p>
      <p>이러한 오염은 그대로 제품 표면에 전사되거나 치수 불량과 폐기율 증가로 이어질 수 있습니다. 반면 금형을 분해해 세척하려면 냉각과 분해, 재조립을 위한 생산 중단시간이 필요하고, 연마 방식의 세척은 금형 표면과 파팅라인에 마모를 남길 수 있습니다.</p>
      <p class="auto-intro-close">따라서 플라스틱 제조에서의 세척은 <b>금형의 표면 상태를 유지하면서 얼마나 자주, 얼마나 짧은 정지시간으로 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">플라스틱 · 복합소재 제조에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PLASTIC MOLD CLEANING</span>
      <h3>플라스틱 금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/plastics-composites-dry-ice-blasting-injection-mold.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-removing-offgas-from-mold.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">금형을 프레스에 장착한 상태, 작동 온도 그대로<br>이형제와 오프가스를 제거합니다.</p>
      <div class="cmp-text auto-text"><p>사출금형의 캐비티와 벤트, 좁은 틈에는 이형제, 수지 오프가스, 경화된 수지와 안료가 축적됩니다. 이 잔류물은 성형품의 표면 결함과 치수 불량, 폐기율 증가의 직접적인 원인이 됩니다.</p><p>드라이아이스 세척은 비마모성 세정 방식이기 때문에 금형의 치수와 세부 형상, 표면 광택을 유지하면서 축적된 오염물을 제거하는 데 활용됩니다. 금형 조건에 따라 프레스에서 분리하지 않고 작동 온도 상태로 세척할 수 있는 경우가 있으며, 이 경우 냉각·분해·재조립에 필요한 시간을 줄일 수 있습니다.</p><p>세척 시간이 줄면 금형을 더 자주 세척할 수 있고, 이는 성형품 품질을 일정하게 유지하는 데 도움이 됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>사출금형</li><li>압출·블로우 금형</li><li>PET 프리폼 금형(다캐비티)</li><li>핫러너 · 벤트</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">DEBURRING & DEFLASHING <em class="auto-fin">PARTS FINISHING</em></span>
      <h3>플라스틱 부품 디버링 · 디플래싱</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/plastics-composites-deburring-plastic-part.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-automated-deburr-deflash-e1752077764797.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">버와 플래시는 제거하고,<br>부품의 표면과 치수는 유지합니다.</p>
      <div class="cmp-text auto-text"><p>성형 또는 기계가공을 거친 플라스틱 부품에는 가장자리와 파팅라인을 따라 버(Burr)와 플래시(Flash)가 남습니다. 수작업 제거는 시간이 많이 들고 결과가 일정하지 않으며, 연마 방식은 표면을 손상시키거나 치수를 바꿀 수 있습니다.</p><p>드라이아이스는 세척 강도와 입자 크기를 조절해 불필요한 부분만 제거하는 방식으로 부품 마무리 공정에 활용됩니다. 세정 매체가 표면에 남지 않아 연마재 잔류나 교차오염 문제가 없고, 복잡한 형상이나 접근이 어려운 부위에도 적용할 수 있습니다.</p><p>반복 작업의 경우 로봇과 결합한 자동화 셀로 구성하는 사례도 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>사출 성형품</li><li>기계가공 플라스틱 부품</li><li>정밀 커넥터 · 하우징</li><li>자동화 디버링 셀</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">SURFACE PREPARATION</span>
      <h3>도장 · 코팅 전 표면 전처리</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/plastics-composites-automotive-surface-prep.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-coating-surface-preparation.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">물을 쓰지 않고 표면을 준비해<br>세척에서 도장으로 바로 넘어갑니다.</p>
      <div class="cmp-text auto-text"><p>플라스틱 부품에 남은 이형제, 오일, 먼지와 공정 잔류물은 도장과 코팅의 밀착력을 떨어뜨립니다. 물세척은 세척 후 건조공정이 필요하고, 화학 세정은 잔류물과 폐수 처리 문제를 남깁니다.</p><p>드라이아이스 세척은 물과 화학약품을 사용하지 않는 건식 방식으로, 세척 직후 별도 건조 없이 도장·코팅 공정으로 넘어갈 수 있습니다. 비마모성이므로 부품의 표면 질감과 형상을 유지한 채 오염물만 제거할 수 있어, 코팅 두께와 외관 품질을 일정하게 관리하는 데 도움이 됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>자동차 범퍼 · 외장 부품</li><li>도장 전 성형품</li><li>코팅 · 접착 전 표면</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">COMPOSITE TOOL CLEANING</span>
      <h3>복합재 툴링 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/plastics-composites-dry-ice-blasting-cleaning-composite-tooling.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-removing-gel-coat-buildup-from-composite-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">정밀한 복합재 툴의 셧오프와 공차를<br>마모 없이 관리합니다.</p>
      <div class="cmp-text auto-text"><p>복합소재 성형용 툴링에는 이형제, 수지, 젤코트, 오일 등이 층을 이루며 축적됩니다. 툴의 셧오프와 공차, 세부 형상은 성형품 품질을 좌우하기 때문에 연마 방식의 세척은 곧 툴 수명 단축으로 이어질 수 있습니다.</p><p>드라이아이스 세척은 툴 표면을 마모시키지 않고 축적된 수지와 이형제를 제거하는 데 활용됩니다. 툴을 라인에서 내리지 않고 작동 온도 상태로 세척할 수 있는 경우 냉각과 재가열, 분해·재조립에 드는 시간을 줄일 수 있으며, 세정 잔재가 남지 않아 추가 세척 단계가 필요하지 않습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>복합재 성형 툴</li><li>젤코트 · 수지 축적 금형</li><li>항공 · 풍력 · 선박용 대형 툴</li></ul></div>
      <a class="auto-rel-link" href="../industries/aerospace.html"><span>관련 산업</span>우주 · 항공 <i>→</i></a>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">플라스틱 · 복합소재 공정에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/plastics-composites-removing-mold-release-agent-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>이형제</b><small>MOLD RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/plastics-composites-removing-offgas-from-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>수지 오프가스</b><small>RESIN OFF-GAS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/plastics-composites-removing-residual-plastic-and-pigment-from-plastic-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>경화 수지 · 잔류 플라스틱</b><small>CURED RESIN & RESIDUAL PLASTIC</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/plastics-composites-dry-ice-blasting-injection-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>안료 잔류물</b><small>PIGMENT RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/plastics-composites-removing-gel-coat-buildup-from-composite-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>젤코트 축적물</b><small>GEL COAT BUILDUP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/plastics-composites-deburring-machined-part.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>버 · 플래시</b><small>BURRS & FLASH</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/plastics-composites-dry-ice-blasting-cleaning-automotive-parts-prior-to-painting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 · 먼지</b><small>OIL & DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/plastics-composites-dry-ice-blasting-removing-resin-from-composite-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>복합재 수지</b><small>COMPOSITE RESIN</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">플라스틱 · 복합소재 제조에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>금형 치수와 표면을 유지하는 비마모 세척</b><p>금형의 세부 형상과 파팅라인, 표면 광택을 유지하면서 축적된 오염물을 제거할 수 있습니다. 연마 방식에서 발생하는 금형 마모를 피할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>프레스 장착 상태 · 작동 온도 세척 가능성</b><p>금형 조건에 따라 분리하지 않고 뜨거운 상태로 세척할 수 있는 경우가 있어 냉각·분해·재조립 시간을 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 충돌 후 기체로 승화하므로 금형이나 부품에 연마재·수분·화학 잔류물이 남지 않습니다. 교차오염과 부품 폐기를 줄이는 데 도움이 됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>건조공정이 필요 없는 표면 전처리</b><p>물을 사용하지 않아 세척 후 바로 도장·코팅 공정으로 넘어갈 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>부품 마무리까지 하나의 방식으로</b><p>금형 세척뿐 아니라 디버링·디플래싱, 표면 전처리, 복합재 툴링까지 — 한 공장 안의 서로 다른 과제에 적용 가능성을 검토할 수 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 플라스틱 공장에서도,<br>금형과 부품마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>다캐비티 프리폼 금형의 오프가스, 복합재 툴의 젤코트, 성형품의 얇은 플래시는 모두 플라스틱 공장에서 발생하지만 오염물의 성질과 대상의 재질, 요구되는 세척 강도는 서로 다릅니다.</p>
            <p>바테크는 오염물의 종류와 부착 정도, 금형·부품의 재질과 형상, 작동 온도와 접근성을 확인한 뒤 실제 테스트를 통해 입자 크기와 압력 등 적용 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/plastics-composites-removing-offgas-from-mold.webp" alt="" loading="lazy" /><b>사출금형</b><small>이형제 · 오프가스</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/plastics-composites-dry-ice-blasting-removing-resin-from-composite-mold.webp" alt="" loading="lazy" /><b>복합재 툴</b><small>수지 · 젤코트</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/plastics-composites-deburring-plastic-part.webp" alt="" loading="lazy" /><b>성형 부품</b><small>버 · 플래시</small></li>
          </ul>
          <p class="auto-ae-key">금형을 얼마나 자주 세척할지 정하기 전에,<br><em>어떤 조건이면 세척할 수 있는지</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">플라스틱 · 복합소재에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">플라스틱 생산 안에서도 금형, 부품, 툴링에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/deburring-deflashing.html"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>DEBURRING & DEFLASHING</small><b>디버링 · 디플래싱</b><span>성형·가공 후 버와 플래시를 제거하는 부품 마무리</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">플라스틱 · 복합소재과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">플라스틱 성형은 자동차, 포장, 의료기기 등 여러 산업의 부품 생산공정으로 이어지고, 고무 성형과는 금형 관리의 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/medical.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></span><small>MEDICAL DEVICE MANUFACTURING</small><b>의료기기 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.30s"><a href="../industries/rubber-tires.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-rubber-tire.png" alt="" loading="lazy" /></span><small>RUBBER & TIRES</small><b>고무 · 타이어</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN PLASTICS MANUFACTURING</span>
      <h2 class="cmp-h2">글로벌 플라스틱 제조 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">포장·의료·자동차 부품 등 다양한 분야의 플라스틱 제조사가 금형 세척과 부품 마무리 공정에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 플라스틱 · 복합소재 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:70%"><img src="../assets/img/plastics-composites-silgan.jpg" alt="Silgan Plastics" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:78%"><img src="../assets/img/plastics-composites-phillips-medisize.webp" alt="Phillips-Medisize" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:66%"><img src="../assets/img/plastics-composites-berry-logo.webp" alt="Berry Global" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:64%"><img src="../assets/img/plastics-composites-aptar.webp" alt="Aptar" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:70%"><img src="../assets/img/plastics-composites-amcor_logo.webp" alt="Amcor" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:66%"><img src="../assets/img/plastics-composites-tessy_logo.webp" alt="Tessy Plastics" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:70%"><img src="../assets/img/plastics-composites-srg_global_logo.webp" alt="SRG Global" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:74%"><img src="../assets/img/plastics-composites-milacron_logo.webp" alt="Milacron" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 금형에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 플라스틱 금형이라도 수지의 종류, 이형제와 오프가스의 축적 정도, 금형의 재질과 표면 처리, 작동 온도와 프레스 내 접근성에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 금형이나 성형 부품, 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 금형의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

RUBBER_TIRES_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/rubber-tires/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-rubber-tire.png" alt="고무 · 타이어 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 고무 · 타이어</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">RUBBER & TIRES</span>
      <h1>고무 · 타이어</h1>
      <p class="cmp-hero-p auto-hero-lead">금형이 뜨거운 상태로 프레스에 장착되어 있어도, 세척을 위해 멈추는 시간은 짧아야 합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">RUBBER & TIRE PRODUCTION</span>
      <h2 class="cmp-h2">금형을 식히고, 분해하고, 다시 데우는 시간이<br>생산에서 빠져나갑니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>고무·타이어 제조현장에서는 사출 성형기와 압축 프레스, 타이어 가류기(큐어링 프레스)에 장착된 금형이 높은 온도에서 연속으로 운전됩니다. 자동차용 씰과 가스켓, 산업용 고무부품, 신발, 타이어까지 대상은 다르지만 금형 관리의 과제는 비슷합니다.</p>
      <p>가류 사이클이 반복되면 금형 표면과 미세 벤트, 스프링 벤트, 사이드월의 복잡한 패턴에 이형제 잔류물과 가류된 고무, 카본 침착물이 쌓입니다. 이 오염은 제품 표면의 결함(블레미시)으로 나타나고, 벤트가 막히면 성형 불량으로 이어집니다.</p>
      <p>기존 방식으로는 금형을 냉각하고 분해한 뒤 수작업이나 샌드블라스팅으로 세척하고, 드릴로 벤트를 하나씩 뚫고, 다시 조립해 재가열해야 했습니다. 이 과정은 긴 생산 중단시간을 만들고, 연마 방식은 금형 표면을 조금씩 마모시킵니다. 마모된 금형에는 더 많은 이형제가 필요하고, 그만큼 오염도 빨라지는 악순환이 생깁니다.</p>
      <p class="auto-intro-close">따라서 고무·타이어 제조에서의 세척은 <b>금형을 뜨거운 상태로, 프레스에 장착한 채, 표면 마모 없이 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/auto-rubber-mold.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">고무 · 타이어 제조에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">RUBBER INJECTION MOLD CLEANING</span>
      <h3>고무 사출금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rubber-tires-dry-ice-blasting-cleans-rubber-injection-mold.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-removing-mold-release-agent-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">프레스에 장착된 뜨거운 금형에서<br>이형제와 가류 고무를 제거합니다.</p>
      <div class="cmp-text auto-text"><p>고무 사출금형에는 사이클이 반복될수록 이형제 잔류물과 가류된 고무가 층을 이루며 쌓입니다. 이 축적물은 시간이 지날수록 제거가 어려워지고, 제품 표면 결함과 치수 불량의 원인이 됩니다.</p><p>드라이아이스 세척은 금형을 프레스에서 분리하거나 냉각하지 않고 작동 온도 상태에서 세척하는 방식으로 활용됩니다. 뜨거운 금형과 -78℃ 드라이아이스의 온도 차는 오염물 제거에 유리하게 작용하며, Cold Jet 자료에 따르면 이 온도 차로 인한 열충격이나 금형 재질의 변화는 발생하지 않습니다.</p><p>비마모성이므로 금형의 공차와 표면 마감을 유지할 수 있고, 세척 후 바로 다음 사이클을 시작할 수 있어 재가열 대기시간이 필요하지 않습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>고무 사출금형</li><li>자동차 씰 · 가스켓 금형</li><li>산업용 고무부품 금형</li><li>O-링 · 정밀 고무 금형</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">RUBBER COMPRESSION MOLD CLEANING</span>
      <h3>고무 압축금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rubber-tires-cleaning-rubber-compression-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">복잡한 형상과 텍스처 표면에서<br>가류 고무와 이형제를 제거합니다.</p>
      <div class="cmp-text auto-text"><p>압축 성형금형은 캐비티가 크고 형상이 복잡하며, 텍스처가 있는 표면에 가류 고무와 이형제가 깊이 고착됩니다. 수작업 세척은 수 시간이 걸리고, 좁은 틈과 텍스처 사이의 잔류물은 완전히 제거하기 어렵습니다.</p><p>드라이아이스 세척은 입자가 복잡한 형상과 텍스처 표면 안쪽까지 도달해 축적물을 제거하는 방식으로 활용됩니다. 금형 표면을 마모시키지 않으므로 텍스처와 세부 형상이 유지되고, 세정 매체가 남지 않아 다음 사이클에서 쇼트샷이나 오염 문제가 발생하지 않습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>압축 성형금형</li><li>트랜스퍼 금형</li><li>텍스처 · 패턴 금형</li><li>신발 · 대형 고무부품 금형</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">TIRE MOLD CLEANING</span>
      <h3>타이어 금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rubber-tires-cleaning-tire-mold-while-hot-and-online-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/rubber-tires-dry-ice-blasting-cleaning-tire-mold-without-disassembly-or-cooldown.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">가류기에 장착된 상태로 사이드월 패턴과<br>미세 벤트까지 세척합니다.</p>
      <div class="cmp-text auto-text"><p>타이어 금형은 사이드월의 복잡한 패턴과 문자, 수백 개의 미세 벤트와 스프링 벤트로 구성됩니다. 가류 사이클이 반복되면 이형제와 카본 침착물이 패턴과 벤트에 쌓이고, 막힌 벤트는 타이어 표면 결함의 주요 원인이 됩니다.</p><p>기존 방식은 금형을 냉각하고 가류기에서 분리해 세척한 뒤 드릴로 벤트를 하나씩 뚫고 재조립·재가열하는 긴 과정이었습니다. 드라이아이스 세척은 금형을 가류기에 장착한 채 작동 온도 상태로 세척하는 방식으로 활용되며, 압축공기가 드라이아이스 입자를 벤트 안쪽까지 운반해 막힘을 제거합니다.</p><p>비마모성이므로 패턴과 문자, 벤트 가장자리가 마모되지 않아 금형 수명 관리에 유리합니다. Cold Jet은 사이드월 세척을 기준으로 기존 수 시간 단위의 작업이 수십 분 단위로 줄어든 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>타이어 가류 금형(사이드월 · 트레드)</li><li>미세 벤트 · 스프링 벤트</li><li>세그먼트 금형</li><li>컨테이너 · 블래더 주변</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">고무 · 타이어 공정에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/plastics-composites-removing-mold-release-agent-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>이형제 잔류물</b><small>SPENT RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/rubber-tires-cleaning-rubber-compression-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>가류 고무 잔사</b><small>VULCANIZED RUBBER RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/rubber-tires-tire-mold-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 침착물</b><small>CARBON DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/rubber-tires-dry-ice-blasting-cleaning-tire-mold-without-disassembly-or-cooldown.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>벤트 막힘</b><small>BLOCKED VENTS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/rubber-tires-cleaning-tire-mold-while-hot-and-online-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>사이드월 패턴 오염</b><small>SIDEWALL PATTERN FOULING</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/rubber-tires-dry-ice-blasting-cleans-rubber-injection-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>금형 표면 축적물</b><small>MOLD SURFACE BUILDUP</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">고무 · 타이어 제조에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>뜨거운 상태 · 프레스 장착 상태 세척</b><p>금형을 냉각하거나 분리하지 않고 작동 온도에서 세척할 수 있는 경우 냉각·분해·재조립·재가열에 드는 시간을 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>금형 마모 없는 비마모 세척</b><p>샌드블라스팅이나 와이어브러시, 드릴에 의한 표면 마모가 없어 패턴·문자·벤트 가장자리와 공차를 유지할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>미세 벤트와 복잡한 형상 접근</b><p>압축공기가 드라이아이스 입자를 미세 벤트와 스프링 벤트, 텍스처 안쪽까지 운반해 수작업으로 닿기 어려운 부위를 세척할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>이형제 악순환의 차단</b><p>금형 표면이 마모되지 않으면 필요한 이형제 양이 늘지 않고, 그만큼 오염 축적 속도도 관리할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>세정 매체 · 폐기물이 남지 않는 방식</b><p>연마재나 용제 폐기물이 발생하지 않고 금형에 수분·잔류물이 남지 않아, 세척 직후 다음 사이클로 복귀할 수 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 고무 공장에서도,<br>금형마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>사출금형의 얇은 이형제 층, 압축금형의 두껍게 고착된 가류 고무, 타이어 금형의 미세 벤트 막힘은 같은 현장에서 발생하지만 필요한 입자 크기와 압력, 노즐 구성은 서로 다릅니다.</p>
            <p>바테크는 금형의 재질과 형상, 오염물의 종류와 두께, 작동 온도와 프레스 내 접근성을 확인한 뒤 실제 테스트를 통해 적용 조건을 검토합니다. 3mm 펠렛으로 두꺼운 고무 축적물을 제거하는 작업과 미세 입자로 벤트를 세척하는 작업은 같은 장비에서도 다른 설정이 필요합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/rubber-tires-dry-ice-blasting-cleans-rubber-injection-mold.webp" alt="" loading="lazy" /><b>사출금형</b><small>이형제 · 가류 고무</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/rubber-tires-cleaning-rubber-compression-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>압축금형</b><small>고착 고무 · 텍스처 오염</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/rubber-tires-tire-mold-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>타이어 금형</b><small>카본 · 벤트 막힘</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 금형에 맞는 입자와 압력</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">고무 · 타이어에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">고무·타이어 생산 안에서도 금형의 종류와 오염 상태에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/deburring-deflashing.html"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>DEBURRING & DEFLASHING</small><b>디버링 · 디플래싱</b><span>성형·가공 후 버와 플래시를 제거하는 부품 마무리</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">고무 · 타이어과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">고무 성형은 자동차 부품 생산과 직접 연결되고, 플라스틱 성형과는 금형 관리의 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN RUBBER & TIRE PLANTS</span>
      <h2 class="cmp-h2">글로벌 타이어 · 고무부품 제조 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">세계 주요 타이어 제조사와 자동차용 고무부품, 산업용 고무 제조사가 금형 세척에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 고무 · 타이어 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:74%"><img src="../assets/img/rubber-tires-bridgestone_logo.webp" alt="Bridgestone" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:72%"><img src="../assets/img/rubber-tires-michelin_logo.webp" alt="Michelin" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:74%"><img src="../assets/img/rubber-tires-goodyear_logo.webp" alt="Goodyear" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:74%"><img src="../assets/img/rubber-tires-hankook_logo.webp" alt="Hankook" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:66%"><img src="../assets/img/rubber-tires-pirelli-logo.webp" alt="Pirelli" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:74%"><img src="../assets/img/rubber-tires-yokohama-logo.webp" alt="Yokohama" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:72%"><img src="../assets/img/rubber-tires-coopertires-logo.webp" alt="Cooper Tires" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:74%"><img src="../assets/img/rubber-tires-trelleborg-logo.webp" alt="Trelleborg" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:74%"><img src="../assets/img/rubber-tires-freudenberg_logo.webp" alt="Freudenberg" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:72%"><img src="../assets/img/rubber-tires-parkerhannifin-logo.webp" alt="Parker Hannifin" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.40s; --w:70%"><img src="../assets/img/rubber-tires-toyodagosei_logo.webp" alt="Toyoda Gosei" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 가류기의 금형에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 고무 금형이라도 고무 배합과 이형제의 종류, 축적물의 두께, 금형의 재질과 표면 처리, 프레스 내 접근성과 작동 온도에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 금형이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 금형의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

FOUNDRY_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/foundry/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/auto-diecast-die.jpg" alt="주조 · 다이캐스팅 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 주조 · 다이캐스팅</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">FOUNDRY & DIE CASTING</span>
      <h1>주조 · 다이캐스팅</h1>
      <p class="cmp-hero-p auto-hero-lead">금형과 코어박스의 표면 상태는 주물의 표면 품질로 그대로 이어집니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">FOUNDRY & DIE CASTING</span>
      <h2 class="cmp-h2">금형을 세척할 때마다<br>조금씩 깎아내고 있지는 않은지.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>주조·다이캐스팅 현장에는 영구금형(중력·저압·틸트 주조), 코어를 만드는 코어박스(콜드박스·쉘 코어박스), 고압 다이캐스팅과 스퀴즈·세미솔리드 주조용 금형, 단조 다이와 각종 코팅·핸들링 설비가 함께 운영됩니다.</p>
      <p>반복 주조 과정에서 금형 표면에는 내화성 코팅(도형재), 그라파이트 윤활제, 탄화된 이형제가 쌓이고, 코어박스에는 경화된 수지 바인더와 모래 잔류물이 고착됩니다. 다이캐스팅 금형에는 다이 윤활제와 산화물이 축적됩니다.</p>
      <p>이 오염은 주물 표면 결함, 가스 기공, 치수 편차와 폐기율 증가의 원인이 됩니다. 그런데 기존의 샌드블라스팅과 와이어브러시 세척은 세척할 때마다 파팅라인을 둥글게 마모시키고 정밀한 벤트와 스크린을 손상시켜, 고가의 금형을 예정보다 빨리 교체하게 만듭니다. 습식 세척은 강 재질의 다이와 주철 금형에 플래시 러스트(급속 녹)를 남길 수 있습니다.</p>
      <p class="auto-intro-close">따라서 주조에서의 세척은 <b>금형과 코어박스의 정밀 형상을 마모시키지 않으면서, 라인에서 내리지 않고 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/auto-diecast-corebox.jpg" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">주조 · 다이캐스팅에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PERMANENT MOLD CLEANING</span>
      <h3>영구금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/foundry-removing-refractory-coating-from-permanent-mold.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-aluminum-permanent-mold.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">내화 코팅과 탄화 이형제는 제거하고,<br>파팅라인과 냉각채널은 그대로 유지합니다.</p>
      <div class="cmp-text auto-text"><p>중력·저압 주조용 영구금형에서는 미세한 표면 변화도 용탕의 흐름과 제품 이형에 영향을 줍니다. 그런데 샌드블라스팅과 와이어브러시는 세척할 때마다 파팅라인을 둥글게 마모시키고 표면 마감을 떨어뜨려, 결국 금형 수명을 단축시킵니다.</p><p>드라이아이스 세척은 금형 표면을 마모시키지 않으면서 내화성 코팅, 그라파이트 윤활제, 탄화된 이형제를 복잡한 파팅라인과 내부 냉각채널에서 제거하는 방식으로 활용됩니다. 금형을 장착한 채 작동 온도에서 세척할 수 있는 경우 냉각과 분리에 드는 시간을 줄일 수 있습니다.</p><p>Cold Jet은 한 자동차 부품 주조공장이 드라이아이스 세척으로 전환한 뒤 금형 수명이 늘어난 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>알루미늄 영구금형</li><li>중력 · 틸트 주조 금형</li><li>저압 주조(LPPM) 금형</li><li>브레이크 부품 금형</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">CORE BOX CLEANING</span>
      <h3>코어박스 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/foundry-core-box-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/foundry-cleaning-of-a-multi-cavity-core-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">경화된 수지와 바인더를 제거하고,<br>벤트와 스크린의 날카로운 가장자리를 지킵니다.</p>
      <div class="cmp-text auto-text"><p>코어박스 세척은 주조현장에서 병목이 되기 쉬운 작업입니다. 경화된 수지와 모래 바인더, 이형제가 복잡한 형상에 고착되어 수작업 스크래핑에 수 시간이 걸리거나 외부 업체에 맡겨야 했고, 그동안 예비 툴링을 확보해야 했습니다.</p><p>드라이아이스 세척은 복잡한 형상 안쪽까지 도달해 경화된 수지와 바인더를 제거하는 방식으로 활용됩니다. 특히 가스 기공의 주요 원인인 슬롯 벤트와 스크린의 막힘을 마모 없이 제거해 배기 성능을 회복시킬 수 있습니다. Cold Jet은 한 독일 주조공장이 6시간의 수작업 세척을 1시간 이내로 줄인 사례를 소개하고 있습니다.</p><p>비전도성 세정 방식이므로 코어실의 센서와 오븐 시스템, 핸들링 지그 등 주변 설비의 유지보수에도 적용 가능성을 검토할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>콜드박스 · 쉘 코어박스</li><li>다캐비티 · 갱 코어박스</li><li>슬롯 벤트 · 스크린</li><li>코어 오븐 · 핸들링 지그</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">DIE CAST TOOLING & GENERAL EQUIPMENT</span>
      <h3>다이캐스팅 금형 · 일반 설비 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/foundry-removing-die-lube-from-magnesium-die-cast-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-high-pressure-die-casting-mold.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">다이를 뜨거운 상태로 세척해<br>교체 사이의 정지시간을 줄입니다.</p>
      <div class="cmp-text auto-text"><p>다이캐스팅에서는 오염이 제품 품질을 떨어뜨리지만, 설비를 멈추면 생산량이 바로 줄어듭니다. 고압 다이캐스팅(HPDC), 스퀴즈 주조, 세미솔리드 주조용 금형에는 다이 윤활제와 산화물이 두껍게 쌓입니다.</p><p>드라이아이스 세척은 금형을 작동 온도 상태로 세척해 냉각과 분해에 드는 시간을 줄이는 방식으로 활용됩니다. 비마모성이므로 파팅라인이 둥글게 마모되지 않고, 세정 잔재와 수분이 남지 않아 강 재질 다이의 플래시 러스트를 피할 수 있습니다. Cold Jet은 다이 교체마다 2시간의 정지시간을 없앤 사례를 제시하고 있습니다.</p><p>같은 방식은 단조 다이와 코팅 설비, 유압장치, 모터, 제어반 등 주조공장의 일반 설비 유지보수에도 확장할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>고압 다이캐스팅 금형</li><li>스퀴즈 · 세미솔리드 주조 금형</li><li>단조 다이</li><li>코팅 설비 · 유압장치 · 제어반</li></ul></div>
      <a class="auto-rel-link" href="../industries/automotive.html"><span>관련 산업</span>자동차 제조 <i>→</i></a>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">주조 · 다이캐스팅 공정에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/foundry-removing-refractory-coating-from-permanent-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>내화성 코팅(도형재)</b><small>REFRACTORY COATING</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/foundry-cleaning-of-a-multi-cavity-core-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>모래 · 바인더 잔류물</b><small>SAND & BINDER RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/foundry-core-box-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>경화 수지</b><small>HARDENED RESIN</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-aluminum-permanent-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄화 이형제</b><small>CARBONIZED RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-mold-for-brake-components.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>그라파이트 윤활제</b><small>GRAPHITE LUBRICANT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/foundry-removing-die-lube-from-magnesium-die-cast-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>다이 윤활제</b><small>DIE LUBRICANT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-die-cast-tooling.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>산화물</b><small>OXIDES</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-high-pressure-die-casting-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 침착물</b><small>CARBON DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.48s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-core-box-online.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>벤트 · 스크린 막힘</b><small>CLOGGED VENTS & SCREENS</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">주조 · 다이캐스팅에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why is-6">
    <li class="reveal" style="--reveal-delay:0.00s"><b>파팅라인과 벤트를 마모시키지 않는 세척</b><p>샌드블라스팅과 와이어브러시가 누적시키는 마모가 없어 금형의 치수 정밀도와 벤트·스크린의 날카로운 가장자리를 유지할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>뜨거운 상태 · 장착 상태 세척 가능성</b><p>영구금형과 다이캐스팅 금형, 단조 다이를 라인에서 내리지 않고 작동 온도에서 세척할 수 있는 경우 냉각·분리·재정렬에 드는 시간을 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>수분이 남지 않아 플래시 러스트를 피하는 방식</b><p>물을 사용하지 않아 강 재질 다이와 주철 금형에 급속 녹이 생기는 문제를 피할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>연마재 잔류물 없음</b><p>세정 매체가 승화하므로 금형이나 코어박스에 모래·비드가 남아 주물 결함을 만들지 않고, 사용한 연마재를 회수·처리할 필요가 없습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>비전도성 세정 방식</b><p>코어실의 센서와 제어반, 오븐 시스템처럼 전기부품이 포함된 설비의 유지보수에 적용 가능성을 검토할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.45s"><b>작업자 안전</b><p>용제 노출과 실리카 분진 흡입, 장시간 와이어브러시 작업의 신체 부담을 줄일 수 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 주조공장에서도,<br>금형과 코어박스의 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>영구금형의 두꺼운 내화 코팅, 코어박스 벤트의 경화 수지, 다이캐스팅 금형의 윤활제 축적은 같은 주조공장에서 발생하지만 필요한 세척 강도와 입자 크기, 노즐 구성은 서로 다릅니다.</p>
            <p>바테크는 금형의 재질과 형상, 오염물의 종류와 두께, 작동 온도와 접근성을 확인한 뒤 실제 테스트를 통해 적용 조건을 검토합니다. 정밀 벤트를 세척하는 조건과 내화 코팅을 제거하는 조건은 같은 장비에서도 다른 설정이 필요합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/foundry-removing-refractory-coating-from-permanent-mold.webp" alt="" loading="lazy" /><b>영구금형</b><small>내화 코팅 · 탄화 이형제</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/foundry-core-box-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>코어박스</b><small>경화 수지 · 바인더</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-die-cast-tooling.webp" alt="" loading="lazy" /><b>다이캐스팅 금형</b><small>다이 윤활제 · 산화물</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 금형에 맞는 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">주조 · 다이캐스팅에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">주조 현장 안에서도 금형, 코어박스, 일반 설비에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/rust-corrosion-removal.html"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>RUST, CORROSION & OXIDATION REMOVAL</small><b>녹 · 부식 · 산화물 제거</b><span>표면 녹과 느슨한 산화물(비마모 범위 내)</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">주조 · 다이캐스팅과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">주조·다이캐스팅은 자동차 부품 생산의 핵심 공정이며, 정밀 주조는 항공 부품 제조와도 연결됩니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE & AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN FOUNDRIES</span>
      <h2 class="cmp-h2">글로벌 주조 · 다이캐스팅 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">자동차 부품 주조와 정밀 주조, 알루미늄·철 주조 분야의 주요 기업이 금형과 코어박스 세척에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 주조 · 다이캐스팅 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:74%"><img src="../assets/img/foundry-thyssenkrupp_ag_logo.webp" alt="thyssenkrupp" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:74%"><img src="../assets/img/foundry-precision_castparts_logo.webp" alt="Precision Castparts" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:66%"><img src="../assets/img/foundry-nemak_logo.webp" alt="Nemak" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:72%"><img src="../assets/img/foundry-konzelmann_logo.webp" alt="Konzelmann" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:72%"><img src="../assets/img/foundry-hitachi-metals-logo.webp" alt="Hitachi Metals" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:72%"><img src="../assets/img/foundry-waupaca-foundry-logo.webp" alt="Waupaca Foundry" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:64%"><img src="../assets/img/foundry-grede_logo.webp" alt="Grede" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:68%"><img src="../assets/img/foundry-bosch-logo.webp" alt="Bosch" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:62%"><img src="../assets/img/foundry-alcoa_logo.webp" alt="Alcoa" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:68%"><img src="../assets/img/foundry-yamaha-logo.webp" alt="Yamaha" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 금형과 코어박스에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 주조 금형이라도 내화 코팅의 종류와 두께, 바인더의 경화 상태, 금형의 재질과 작동 온도, 라인 내 접근성에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 금형이나 코어박스, 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 금형의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

SEMICONDUCTOR_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/semiconductor-manufacturing/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/ind-card-semiconductor.png" aria-label="반도체 · 전자 제조 현장">
      <source src="../assets/video/semiconductor-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 반도체 · 전자 제조</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">SEMICONDUCTOR & ELECTRONICS</span>
      <h1>반도체 · 전자 제조</h1>
      <p class="cmp-hero-p auto-hero-lead">정밀한 공정일수록, 미세한 오염도 수율과 품질에 영향을 줄 수 있습니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">SEMICONDUCTOR VALUE CHAIN</span>
      <h2 class="cmp-h2">원료 생산에서 기판 조립까지,<br>세척이 필요한 지점은 공정마다 다릅니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>반도체·전자 제조는 폴리실리콘 원료 생산, 웨이퍼 제조(팹), 반도체 패키징·조립, PCB 제조·조립으로 이어지는 긴 밸류체인입니다. 각 단계에는 CVD 반응기, 웨이퍼 챔버와 증착·연마 툴링, 진공펌프와 임플란터, 반도체 몰드, 솔더링 설비와 검사 지그 등 서로 다른 장비가 운영됩니다.</p>
      <p>CVD 반응기 내부에는 실리콘 축적물과 분진이, 챔버 부품과 지그에는 플라즈마 코팅 잔류물과 연마 컴파운드가 남습니다. 반도체 몰드에는 왁스와 가스 축적물이, 성형·레이저 절단 후 칩에는 플래시와 접착제가, PCB에는 솔더 플럭스와 솔더볼, 컨포멀 코팅이 남습니다.</p>
      <p>이 오염은 수율 저하와 후속 공정 오염, 부품 불량으로 직결됩니다. 그런데 기존 방식인 수작업 세척과 화학 용제, 고압수는 시간이 오래 걸리고 기판을 손상시킬 수 있으며, 잔류물과 폐기물을 남겨 오히려 교차오염의 원인이 되기도 합니다.</p>
      <p class="auto-intro-close">따라서 반도체·전자 제조에서의 세척은 <b>민감한 표면을 손상시키지 않고, 잔류물을 남기지 않으면서, 장비를 분해하지 않고 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/ind-card-semiconductor.png" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">반도체 · 전자 제조에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">CVD REACTOR DECONTAMINATION</span>
      <h3>폴리실리콘 CVD 반응기 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/semiconductor-automated-dry-ice-cleaning-for-decontamination-of-parts.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">반응기 내부의 실리콘 축적물을<br>화학약품 없이, 표면 손상 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>폴리실리콘 제조에서는 CVD 반응기 내부에 실리콘 축적물과 분진이 쌓이는 것을 관리해야 합니다. 기존의 고압수 세척과 화학 스크러빙은 시간이 오래 걸리고 작업자가 유해 화학물질에 노출되며, 처리 비용이 드는 2차 폐기물을 만듭니다.</p><p>드라이아이스 세척은 반응기 내부 표면을 손상시키지 않으면서 축적물을 제거하는 방식으로 활용됩니다. 화학 용제가 필요 없어 작업 안전이 개선되고, 세정 매체가 승화하므로 2차 폐기물이 발생하지 않습니다. Cold Jet은 이 방식이 후속 공정 오염을 막고 불순물과 폐기율을 줄이는 데 기여한다고 설명합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>CVD 반응기 내부</li><li>반응기 부품 · 전극 주변</li><li>원료 생산 설비</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">WAFER FABRICATION EQUIPMENT</span>
      <h3>웨이퍼 공정장비 · 툴링 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/semiconductor-removing-polishing-compound-from-chamber-components-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/semiconductor-removing-photoresist-and-polishing-agent-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">챔버 부품과 증착 툴링의 정밀 표면을<br>긁지 않고 오염물을 떼어냅니다.</p>
      <div class="cmp-text auto-text"><p>웨이퍼 챔버, 증착 툴링, 연마 설비는 정밀하고 복잡한 부품으로 구성되어 있어 세척은 효과적이되 표면에 어떤 손상도 남기지 않아야 합니다. 플라즈마 코팅 공정 후의 지그와 표면, 테프론 코팅 알루미늄 챔버에 남은 연마 컴파운드는 잔류물 없이 제거되어야 다음 공정의 결함을 막을 수 있습니다.</p><p>드라이아이스 세척은 비마모성으로 표면을 긁거나 치수를 바꾸지 않으면서 오염물을 떼어내는 방식으로 활용됩니다. 화학 잔류물이 남지 않아 교차오염 위험을 줄일 수 있고, 반복 작업은 자동화 셀로 구성하는 사례도 있습니다.</p><p>진공펌프와 임플란터처럼 공정 부산물이 축적되는 설비는 분해 없이 현장에서 건식으로 세척할 수 있는 경우가 있어, 정비시간을 줄이고 고가 장비의 손상 위험을 낮추는 데 도움이 됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>웨이퍼 챔버 · 챔버 부품</li><li>증착 · 연마 툴링</li><li>플라즈마 코팅 지그</li><li>진공펌프 · 임플란터</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">SEMICONDUCTOR MOLD & CHIP FINISHING</span>
      <h3>반도체 몰드 세척 · 칩 후처리</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/semiconductor-dry-ice-cleaning-removing-wax-and-gas-buildup-from-semiconductor-molds.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/semiconductor-automated-dry-ice-blasting-removing-debris-from-laser-cut-microchip-edges.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">몰드는 뜨거운 상태로 세척하고,<br>절단된 칩 가장자리의 이물은 손상 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>반도체 패키징에 사용되는 몰드와 다이에는 왁스와 가스 축적물이 쌓여 칩 캐리어와 성형 부품의 품질을 떨어뜨립니다. 기존 세척은 냉각 대기와 수작업 스크러빙이 필요해 시간이 오래 걸렸습니다.</p><p>드라이아이스 세척은 몰드와 다이를 뜨거운 상태에서 분리하지 않고 세척하는 방식으로 활용되어, 툴링 손상 없이 축적물을 제거하고 정지시간을 줄이는 데 도움이 됩니다.</p><p>성형과 레이저 절단 후 칩 표면에 남은 플라스틱 플래시와 접착제 같은 이물도 비마모 방식으로 제거할 수 있어, 민감한 칩 가장자리와 표면을 손상시키지 않고 다음 공정으로 넘길 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>반도체 몰드 · 다이</li><li>칩 캐리어 성형 툴</li><li>레이저 절단 후 칩 가장자리</li><li>하네스 · 커넥터(비전도성 적용)</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">PCB MANUFACTURING & ASSEMBLY</span>
      <h3>PCB 제조 · 조립 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/semiconductor-cleaning-of-no-clean-flux-residues-from-the-pcba-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/semiconductor-removal-of-dross-and-flux-deposits-from-the-wave-soldering-pallet-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">플럭스 잔류물과 컨포멀 코팅을<br>비전도성 방식으로 제거합니다.</p>
      <div class="cmp-text auto-text"><p>PCB 제조에서는 솔더링 후 플럭스 잔류물, 솔더볼, 냉납 리드가 기판에 남아 단락과 부품 고장의 원인이 됩니다. 웨이브 솔더링 팔레트에는 드로스와 플럭스가 축적되고, 포고핀과 ICT 검사 지그도 주기적인 세척이 필요합니다.</p><p>드라이아이스 세척은 비전도성이고 잔류물을 남기지 않는 방식으로 활용되어, 용제나 브러시 없이 기판과 부품의 상태를 유지하면서 이런 오염물을 제거하는 데 도움이 됩니다.</p><p>컨포멀 코팅 도포 전 먼지·플럭스·오일 제거와, 리워크·수리 시 코팅을 선택적으로 제거하는 작업에도 활용됩니다. 스프레이 코팅 지그의 코팅 제거, 하네스와 커넥터의 표면 녹 제거, 세라믹 지지 디스크와 진공 하우징 세척 같은 설비 유지보수에도 적용 가능성을 검토할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>PCBA · 플럭스 잔류물</li><li>웨이브 솔더링 팔레트</li><li>포고핀 · ICT 검사 지그</li><li>컨포멀 코팅 지그</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">반도체 · 전자 공정에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/semiconductor-automated-dry-ice-cleaning-for-decontamination-of-parts.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>실리콘 축적물 · 분진</b><small>SILICON BUILDUP & DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/semiconductor-removing-polishing-compound-from-chamber-components-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>연마 컴파운드</b><small>POLISHING COMPOUND</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/semiconductor-removing-photoresist-and-polishing-agent-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>포토레지스트</b><small>PHOTORESIST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/semiconductor-dry-ice-cleaning-removing-wax-and-gas-buildup-from-semiconductor-molds.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>왁스 · 가스 축적물</b><small>WAX & GAS BUILDUP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/semiconductor-automated-dry-ice-blasting-removing-debris-from-laser-cut-microchip-edges.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>플래시 · 절단 이물</b><small>FLASH & CUTTING DEBRIS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/semiconductor-cleaning-of-no-clean-flux-residues-from-the-pcba-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>솔더 플럭스 · 솔더볼</b><small>SOLDER FLUX & SOLDER BALLS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/semiconductor-removal-of-dross-and-flux-deposits-from-the-wave-soldering-pallet-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>드로스</b><small>DROSS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/semiconductor-cleaning-pcb-board-after-welding-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>컨포멀 코팅</b><small>CONFORMAL COATING</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.48s"><img src="../assets/img/semiconductor-cleaning-the-mold-or-die-after-the-molding-process-of-the-microchips.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>몰드 잔류물</b><small>MOLD RESIDUE</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">반도체 · 전자 제조에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>민감한 표면을 긁지 않는 비마모 세척</b><p>웨이퍼 툴링, 챔버 부품, 칩 가장자리처럼 미세한 치수와 표면 상태를 유지해야 하는 대상에 적용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>비전도성 · 수분 없는 건식 세척</b><p>PCB, 하네스, 커넥터, 검사 지그 등 전기부품을 단락이나 수분 손상 위험 없이 세척할 수 있습니다. 실제 적용은 전원 상태와 안전조건을 함께 검토해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체 잔류 없음</b><p>드라이아이스가 승화하므로 화학 잔류물이나 수분, 연마재가 남지 않아 교차오염과 후속 공정 결함을 줄이는 데 도움이 됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>분해하지 않고 현장에서 세척</b><p>진공펌프, 반응기, 몰드처럼 분해에 시간이 드는 설비를 장착 상태에서 세척할 수 있는 경우 정비시간을 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>자동화 · 인라인 통합</b><p>반복적이고 정밀한 세척 작업은 로봇과 결합한 자동화 셀로 기존 생산공정에 통합한 사례가 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 반도체 공장에서도,<br>공정마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>CVD 반응기의 실리콘 축적물, 챔버 부품의 연마 컴파운드, PCB의 플럭스 잔류물은 같은 밸류체인 안에 있지만 오염물의 성질과 대상의 민감도, 요구되는 청정도는 서로 다릅니다.</p>
            <p>바테크는 대상의 재질과 코팅, 오염물의 종류와 부착 정도, 클린룸 등급과 작업 조건을 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/semiconductor-automated-dry-ice-cleaning-for-decontamination-of-parts.webp" alt="" loading="lazy" /><b>CVD 반응기</b><small>실리콘 축적물</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/semiconductor-removing-polishing-compound-from-chamber-components-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>웨이퍼 툴링</b><small>연마 컴파운드 · 포토레지스트</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/semiconductor-cleaning-of-no-clean-flux-residues-from-the-pcba-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>PCB · 지그</b><small>플럭스 · 컨포멀 코팅</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 공정의 청정도 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">반도체 · 전자 제조에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">반도체·전자 제조 안에서도 대상과 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/deburring-deflashing.html"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>DEBURRING & DEFLASHING</small><b>디버링 · 디플래싱</b><span>성형·가공 후 버와 플래시를 제거하는 부품 마무리</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.35s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">반도체 · 전자 제조과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">반도체 패키징 몰드는 정밀 사출 금형 관리와 과제를 공유하고, 전자부품은 의료기기와 자동차 전장으로 이어집니다.</p>
  </div>
  <ul class="auto-relind">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/medical.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></span><small>MEDICAL DEVICE MANUFACTURING</small><b>의료기기 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN SEMICONDUCTOR & ELECTRONICS</span>
      <h2 class="cmp-h2">글로벌 반도체 · 전자 제조 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">장비 제조사와 팹, 패키징·EMS 기업이 수동 장비부터 완전 자동화 로봇 셀까지 다양한 형태로 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 반도체 · 전자 제조 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:76%"><img src="../assets/img/semiconductor-lam_research_logo.jpg" alt="Lam Research" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:56%"><img src="../assets/img/semiconductor-nxp.jpg" alt="NXP" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:74%"><img src="../assets/img/semiconductor-infineon-seeklogo.jpg" alt="Infineon" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:70%"><img src="../assets/img/semiconductor-ase-technology-holding-seeklogo.jpg" alt="ASE Technology" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:60%"><img src="../assets/img/semiconductor-jabil.jpg" alt="Jabil" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:66%"><img src="../assets/img/semiconductor-plexus.jpg" alt="Plexus" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:72%"><img src="../assets/img/semiconductor-amphenol.jpg" alt="Amphenol" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:70%"><img src="../assets/img/semiconductor-ferrotec-seeklogo.jpg" alt="Ferrotec" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:60%"><img src="../assets/img/semiconductor-crsc.jpg" alt="CRSC" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 공정 장비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 반도체 설비라도 부품의 재질과 코팅, 오염물의 종류와 부착 정도, 요구되는 청정도와 클린룸 조건에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 지그, 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 공정 장비의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

MEDICAL_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/medical-equipment/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/ind-card-medical.png" aria-label="의료기기 제조 현장">
      <source src="../assets/video/medical-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 의료기기 제조</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">MEDICAL DEVICE MANUFACTURING</span>
      <h1>의료기기 제조</h1>
      <p class="cmp-hero-p auto-hero-lead">주사기 눈금 하나까지 재현해야 하는 금형에서, 세척은 품질관리의 일부입니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">MEDICAL EQUIPMENT MANUFACTURING</span>
      <h2 class="cmp-h2">금형의 미세 캐비티와 부품의 가장자리,<br>둘 다 손상 없이 관리해야 합니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>의료기기 제조는 높은 공차와 일관된 품질, 환자 안전과 규제 준수를 동시에 요구합니다. 사출·압축·열성형·블로우 금형과 압출 다이, 고무·마이크로 금형에서 부품이 생산되고, 임플란트와 스텐트, 수술기구, 카테터 팁처럼 작고 복잡한 부품은 성형 후 마무리 공정을 거칩니다.</p>
      <p>정밀 금형의 미세 캐비티에는 TPE·수지 잔류물과 이형제가 쌓이고, 성형된 부품에는 파팅라인 플래시와 가공 버가 남습니다. 금형의 눈금·문자·상표 같은 세부 형상이 마모되면 모든 부품에 그대로 재현되고, 부품에 남은 버는 기능과 안전에 영향을 줍니다.</p>
      <p>기존 금형 세척은 느리고 노동집약적이며 금형을 손상시킬 수 있습니다. 기존 디버링 방식은 부품을 손상시킬 위험이 있고, 연마 매체가 부품의 작은 구멍과 형상에 끼어 남을 수 있어 의료부품에서는 특히 문제가 됩니다.</p>
      <p class="auto-intro-close">따라서 의료기기 제조에서의 세척은 <b>금형과 부품의 표면·형상을 그대로 유지하면서, 클린룸 조건 안에서 일관되게 반복할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/medical-medical-mold-tool-cleaning.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">의료기기 제조에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">MEDICAL MOLD CLEANING</span>
      <h3>의료용 정밀 금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/medical-medical-device-mfg-cleans-molds.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/medical-clean-tpe-from-tooling.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">클린룸 안에서, 금형을 프레스에 장착한 채<br>세부 형상을 유지하며 세척합니다.</p>
      <div class="cmp-text auto-text"><p>의료용 플라스틱·고무 금형은 미세 캐비티에 쌓이는 잔류물을 일관되게 제거해야 부품이 규정 공차 안에서 생산됩니다. 금형을 분리해 세척하면 냉각·분해·재조립에 시간이 들고, 연마 방식은 눈금과 문자 같은 세부 형상을 마모시킵니다.</p><p>드라이아이스 세척은 금형을 뜨거운 상태로 프레스에 장착한 채 세척하는 방식으로 활용되며, Cold Jet은 ISO 8(Class 100,000)과 ISO 7(Class 10,000) 클린룸에서 검증·사용된 사례를 제시하고 있습니다. 비마모성이므로 Class A~D 표면의 마감과 세부 형상이 유지되어 주사기 눈금 같은 디테일이 매 사이클 정확히 재현됩니다.</p><p>세척 시간이 줄면 더 자주 세척할 수 있어 불량률을 낮추는 데 도움이 되고, 용제 잔류물이 남지 않아 추가 세척 단계가 필요하지 않습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>사출 · 압축 · 열성형 금형</li><li>블로우 · 회전 · 딥 몰딩 금형</li><li>압출 다이</li><li>고무 금형 · 마이크로 금형</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">DEBURRING & DEFLASHING OF MEDICAL PARTS <em class="auto-fin">PARTS FINISHING</em></span>
      <h3>의료부품 디버링 · 디플래싱</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/medical-orthopedic-uhmw-implant-deburring.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/medical-deburr-3d-printed-alif-anterior-lumbar-interbody-fusion-part.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">임플란트와 수술기구의 버를 제거하면서<br>형상과 공차, 표면 마감은 유지합니다.</p>
      <div class="cmp-text auto-text"><p>임플란트, 스텐트, 수술기구, 마이크로 툴, 카테터 팁, 매니폴드, 캐뉼라처럼 작고 복잡한 의료부품은 성형 후 파팅라인 플래시와 가공 버를 제거해야 합니다. 이 작업은 품질과 환자 안전, 규제 준수에 직결되지만, 기존 방식은 느리고 부품 손상 위험이 있으며 연마 매체가 작은 구멍에 끼어 남을 수 있습니다.</p><p>드라이아이스 세척은 부품의 표면 마감과 형상, 공차를 유지하면서 특정 부위를 정밀하게 겨냥해 버와 플래시를 제거하는 방식으로 활용됩니다. 복잡한 형상과 내부 채널에도 접근할 수 있고, 드라이아이스가 승화하므로 매체가 부품에 끼어 남는 문제가 없습니다.</p><p>Cold Jet 자료에 따르면 PEEK, 아세탈, 나일론, LCP, PBT 같은 고성능 폴리머와 티타늄, 스테인리스, 니티놀, 3D 프린팅 부품까지 다양한 재질에 적용된 사례가 있으며, 반복 작업은 블라스트 캐비닛과 로봇을 결합한 자동화 셀로 구성하는 경우가 많습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>정형외과 임플란트 · 3D 프린팅 부품</li><li>스텐트 · 카테터 팁 · 캐뉼라</li><li>수술기구 · 마이크로 툴</li><li>PEEK · 티타늄 · 니티놀 부품</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">PRECISION COMPONENT CLEANING</span>
      <h3>정밀 부품 · 설비 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/medical-deflashing-peek-and-metal.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">잔류물 없는 세척으로<br>완제품의 청정도를 유지합니다.</p>
      <div class="cmp-text auto-text"><p>의료기기 부품에는 성형·가공 과정에서 남은 잔류물이 없어야 하고, 세척 과정 자체가 새로운 오염을 만들어서는 안 됩니다. 화학 세정은 잔류물이 남을 수 있고, 연마 방식은 표면을 바꿉니다.</p><p>드라이아이스 세척은 세정 매체가 승화해 화학 잔류물이나 다른 오염물을 남기지 않는 방식으로, 정밀 부품과 생산설비의 세척에 활용됩니다. 제거된 오염물은 HEPA 필터로 포집하는 구성이 일반적입니다.</p><p>클린룸에서 적용할 경우 마이크로 입자 드라이아이스와 청정·건조 압축공기(수분 분리, 오일 필터), 적절한 방진복 등 클린룸 조건에 맞는 구성을 함께 검토해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>Class I · II · III 의료기기 부품</li><li>내구성 · 일회용 · 이식형 부품</li><li>클린룸 내 생산설비</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">의료기기 제조에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/medical-medical-device-mfg-cleans-molds.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>금형 잔류물</b><small>MOLD RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/medical-clean-tpe-from-tooling.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>TPE · 수지 잔류물</b><small>TPE & RESIN RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/medical-medical-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>이형제</b><small>RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/medical-deflashing-peek-and-metal.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>파팅라인 플래시</b><small>PARTING LINE FLASH</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/medical-orthopedic-uhmw-implant-deburring.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>가공 버</b><small>MACHINING BURRS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/medical-deburr-3d-printed-alif-anterior-lumbar-interbody-fusion-part.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>적층제조 잔류물</b><small>ADDITIVE MANUFACTURING RESIDUE</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">의료기기 제조에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>세부 형상을 유지하는 비마모 세척</b><p>금형의 눈금·문자·상표와 부품의 형상·공차·표면 마감을 바꾸지 않으면서 잔류물과 버를 제거할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>클린룸 적용 사례</b><p>Cold Jet의 마이크로 입자 기술은 ISO 8 · ISO 7 클린룸에서 검증·사용된 사례가 있습니다. 실제 적용은 시설의 등급과 절차에 맞춰 검토해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>매체가 끼어 남지 않는 방식</b><p>드라이아이스가 승화하므로 부품의 작은 구멍과 형상에 연마 매체가 남거나 교차오염이 생기는 문제가 없습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>프레스 장착 상태 세척 가능성</b><p>금형을 뜨거운 상태로 분리하지 않고 세척할 수 있는 경우 냉각·분해·재조립 시간을 줄이고 세척 주기를 짧게 할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>반복 가능한 일관된 결과</b><p>세척 강도와 입자 크기를 고정해 같은 조건을 반복할 수 있어, 저볼륨·고부가 부품의 마무리 공정에도 적합합니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 의료기기 공장에서도,<br>금형과 부품마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>정밀 금형의 미세 캐비티에 남은 TPE, 티타늄 임플란트의 가공 버, PEEK 부품의 얇은 플래시는 같은 현장에서 발생하지만 재질과 요구 공차, 허용되는 세척 강도가 서로 다릅니다.</p>
            <p>바테크는 대상의 재질과 형상, 오염물 또는 버의 상태, 클린룸 등급과 검증 요건을 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/medical-clean-tpe-from-tooling.webp" alt="" loading="lazy" /><b>정밀 금형</b><small>TPE · 수지 · 이형제</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/medical-orthopedic-uhmw-implant-deburring.webp" alt="" loading="lazy" /><b>금속 임플란트</b><small>가공 버</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/medical-deflashing-peek-and-metal.webp" alt="" loading="lazy" /><b>폴리머 부품</b><small>파팅라인 플래시</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 부품에 맞는 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">의료기기 제조에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">의료기기 제조 안에서도 금형과 부품, 설비에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/deburring-deflashing.html"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>DEBURRING & DEFLASHING</small><b>디버링 · 디플래싱</b><span>성형·가공 후 버와 플래시를 제거하는 부품 마무리</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">의료기기 제조과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">의료용 금형은 플라스틱·고무 성형과 같은 과제를 공유하고, 정밀 부품 마무리는 반도체·전자 제조와 연결됩니다.</p>
  </div>
  <ul class="auto-relind">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/rubber-tires.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-rubber-tire.png" alt="" loading="lazy" /></span><small>RUBBER & TIRES</small><b>고무 · 타이어</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/semiconductor.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-semiconductor.png" alt="" loading="lazy" /></span><small>SEMICONDUCTOR & ELECTRONICS</small><b>반도체 · 전자 제조</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN MEDICAL MANUFACTURING</span>
      <h2 class="cmp-h2">글로벌 의료기기 제조 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">주요 의료기기 제조사와 의료용 정밀 성형 업체가 금형 세척과 부품 마무리 공정에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 의료기기 제조 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:70%"><img src="../assets/img/medical-stryker_corporation_logo.webp" alt="Stryker" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:68%"><img src="../assets/img/medical-abbottlaboratories.webp" alt="Abbott" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:66%"><img src="../assets/img/medical-baxter.webp" alt="Baxter" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:60%"><img src="../assets/img/medical-becton-dickinson-logo.webp" alt="Becton Dickinson" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:78%"><img src="../assets/img/plastics-composites-phillips-medisize.webp" alt="Phillips-Medisize" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 금형과 부품에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 의료부품이라도 재질과 형상, 버와 잔류물의 상태, 요구 공차와 클린룸 조건, 검증 요건에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 금형이나 부품, 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 금형과 부품의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

AEROSPACE_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/aerospace-aviation/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-aerospace.png" alt="우주 · 항공 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 우주 · 항공</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">AEROSPACE & AVIATION</span>
      <h1>우주 · 항공</h1>
      <p class="cmp-hero-p auto-hero-lead">복합재 툴 표면의 상태가 곧 부품 품질입니다 — 세척이 그 표면을 바꾸면 안 됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">AEROSPACE & AVIATION MANUFACTURING</span>
      <h2 class="cmp-h2">툴링을 지키면서 세척하는 것,<br>항공 제조에서는 그 자체가 품질 조건입니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>우주·항공 제조는 OEM과 복합재 부품 제조사, 1차 협력사에 걸쳐 프리프레그 적층 툴과 습식 적층 금형, 고광택 툴과 테프론 코팅 툴, RTM·열성형·압축 금형, 정밀 주조용 코어박스와 영구금형, 접착·실링 지그와 전기 캐비닛 등 다양한 생산설비를 운영합니다.</p>
      <p>복합재 툴에는 컴포짓 테이프와 수지, 이형제, 섬유강화 테프론 테이프가 쌓이고, 지그와 금형에는 에폭시와 구조용 접착제, 실런트가 고착됩니다. 강 툴링과 가공설비에는 가공유와 EDM 스패터, 탄화 카본이 남습니다.</p>
      <p>기존 방식인 수작업 스크래핑은 노동집약적이고 작업자에게 부담이 크며, 화학 용제는 VOC 노출과 폐기물 문제를, 연마 블라스팅과 와이어브러시는 고광택 표면과 테프론 코팅의 손상을 남깁니다. 항공 부품의 엄격한 품질 기준에서 툴링 표면의 손상은 곧 부품 결함으로 이어집니다.</p>
      <p class="auto-intro-close">따라서 우주·항공 제조에서의 세척은 <b>고가의 정밀 툴링을 손상시키지 않고, 잔류물 없이, 라인에서 내리지 않고 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">우주 · 항공 제조에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">COMPOSITE TOOL CLEANING</span>
      <h3>복합재 툴링 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/aerospace-dry-ice-blasting-removing-resin-and-release-agents-from-composite-tooling.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">고광택 툴과 테프론 코팅 툴에서<br>수지와 이형제를 코팅 손상 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>복합재 제조는 현대 항공 생산의 중심이며, 툴링의 청정도가 부품 품질을 좌우합니다. 프리프레그 적층 툴과 습식 적층 금형, 고광택 툴과 테프론 코팅 툴에는 컴포짓 테이프와 수지, 이형제, 섬유강화 테프론 테이프가 층을 이루며 쌓입니다.</p><p>드라이아이스 세척은 광택 표면과 민감한 코팅을 손상시키지 않으면서 이 축적물을 제거하는 방식으로 활용됩니다. Cold Jet은 한 제조사가 수작업 스크래핑 대비 세척 시간을 크게 줄이면서 툴링 수명을 늘린 사례를 제시하고 있습니다.</p><p>툴을 작동 온도에서 분리하지 않고 세척할 수 있는 경우 냉각과 재가열, 분해·재조립에 드는 시간을 줄일 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>프리프레그 적층 툴</li><li>습식 적층 금형</li><li>고광택 · 테프론 코팅 툴</li><li>오토클레이브 주변 설비</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">PLASTIC & RUBBER MOLD CLEANING</span>
      <h3>성형 금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/aerospace-cleaning-plastic-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">RTM · 열성형 · 압축 금형을<br>작동 온도에서 좁은 모서리까지 세척합니다.</p>
      <div class="cmp-text auto-text"><p>항공 부품용 사출·열성형·압축·RTM 금형과 압출 다이에는 오프가스 축적물과 수지가 쌓여, 수작업으로는 닿기 어려운 복잡한 형상과 좁은 모서리에 남습니다. 금형 청정도는 부품 품질과 폐기율, 생산 효율에 직접 영향을 줍니다.</p><p>드라이아이스 세척은 금형을 라인에서 내리지 않고 작동 온도에서 세척하는 방식으로 활용되며, Cold Jet은 한 제조사가 금형 세척 시간을 2시간에서 30분으로 줄이면서 접근이 어려운 부위에서 더 나은 결과를 얻은 사례를 소개하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>RTM 금형</li><li>열성형 · 압축 금형</li><li>사출금형 · 압출 다이</li></ul></div>
      <a class="auto-rel-link" href="../industries/plastics-composites.html"><span>관련 산업</span>플라스틱 · 복합소재 <i>→</i></a>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">ADHESIVE REMOVAL</span>
      <h3>접착제 · 실런트 제거</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/aerospace-adhesive-and-sealant-removal-from-aircraft-part-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">항공 제조에서 가장 노동집약적인 작업 중 하나를<br>기판 손상 없이 처리합니다.</p>
      <div class="cmp-text auto-text"><p>접착제 제거는 항공 제조에서 가장 노동집약적인 세척 과제 중 하나입니다. 생산 지그와 금형, 툴링에 고착된 에폭시와 구조용 접착제, 컴포짓 테이프, 수지, 실런트는 수작업 스크래핑으로는 시간이 오래 걸리고 용제로는 VOC 노출 문제가 생깁니다.</p><p>드라이아이스 세척은 기판을 손상시키지 않고 2차 폐기물 없이 접착제와 실런트를 제거하는 방식으로 활용됩니다. 제거된 실런트는 건조한 상태로 떨어져 쓸어 담아 처리할 수 있습니다. Cold Jet은 미 공군 기지 구조정비 부서에서 실런트 제거에 적용해 첫 사용에서 투자 회수 수준의 공수 절감을 확인한 사례를 인용하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>접착 · 실링 지그</li><li>구조용 접착제 · 에폭시</li><li>컴포짓 테이프 잔류물</li><li>항공기 부품 실런트</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">SURFACE PREPARATION</span>
      <h3>표면 전처리</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/aerospace-dry-ice-blasting-used-in-surface-preparation-of-aircraft-part.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">코팅과 용접 전 표면을 건식으로 준비해<br>건조 대기와 플래시 러스트 걱정을 줄입니다.</p>
      <div class="cmp-text auto-text"><p>코팅 밀착력과 용접 품질, 후속 공정의 안정성은 표면 준비 상태에 달려 있습니다. 강 툴링과 금속 가공설비에는 가공유와 EDM 스패터, 실런트, 탄화 카본이 남습니다.</p><p>드라이아이스 세척은 물을 사용하지 않아 세척 직후 건조 대기 없이 바로 코팅이나 용접 공정으로 넘어갈 수 있는 방식으로 활용됩니다. 수분이 남지 않으므로 강 표면의 플래시 러스트 문제도 피할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>강 툴링 · 금속 가공설비</li><li>코팅 · 용접 전 부품 표면</li><li>EDM 가공 후 표면</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">FOUNDRY TOOLING</span>
      <h3>정밀 주조 툴링 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/aerospace-removing-release-agent-from-die-casting-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">항공 부품 주조용 금형과 코어박스를<br>마모 없이 관리합니다.</p>
      <div class="cmp-text auto-text"><p>항공 부품 주조에서는 영구금형과 코어박스, 다이캐스팅 툴링이 깨끗해야 품질 기준을 만족하는 금속 부품을 생산할 수 있습니다. 금형에는 이형제와 수지, 축적물이 쌓이고, 연마 세척은 정밀 형상을 마모시킵니다.</p><p>드라이아이스 세척은 비마모 방식으로 이형제와 수지, 축적물을 제거해 툴링 수명을 늘리면서 부품 품질과 폐기율을 관리하는 데 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>영구 알루미늄 금형</li><li>코어박스</li><li>다이캐스팅 툴링</li></ul></div>
      <a class="auto-rel-link" href="../industries/foundry.html"><span>관련 산업</span>주조 · 다이캐스팅 <i>→</i></a>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-06">
  <div class="auto-app-head reveal">
    <span class="auto-num">06</span>
    <div>
      <span class="auto-en">DEBURRING & DEFLASHING <em class="auto-fin">PARTS FINISHING</em></span>
      <h3>디버링 · 디플래싱</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/aerospace-deburring-plastic-part-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">고성능 폴리머 부품과 지그의 버를<br>부품 손상 없이 빠르게 제거합니다.</p>
      <div class="cmp-text auto-text"><p>항공 제조에서는 플라스틱과 고성능 폴리머 지그·부품의 버 제거가 대표적인 마무리 공정입니다. 수작업은 느리고 결과가 일정하지 않으며, 재작업과 폐기가 발생합니다.</p><p>드라이아이스 세척은 부품을 손상시키지 않고 필요한 부위의 버를 빠르게 제거하는 비마모 방식으로 활용됩니다. Cold Jet은 한 제조사가 부품당 수 초 수준으로 버 제거를 완료해 재작업과 폐기를 줄인 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>고성능 폴리머 지그 · 부품</li><li>성형 플라스틱 부품</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">우주 · 항공 제조에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/aerospace-dry-ice-blasting-removing-resin-and-release-agents-from-composite-tooling.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>수지 · 컴포짓 테이프</b><small>RESIN & COMPOSITE TAPE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/aerospace-removing-release-agent-from-die-casting-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>이형제</b><small>RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/aerospace-adhesive-and-sealant-removal-from-aircraft-part-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제 · 에폭시</b><small>ADHESIVE & EPOXY</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/aerospace-dry-ice-blasting-used-in-surface-preparation-of-aircraft-part.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>실런트</b><small>SEALANT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/aerospace-cleaning-plastic-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오프가스 축적물</b><small>OFF-GAS BUILDUP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/task-surface-industrial.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>가공유 · EDM 스패터</b><small>MACHINING OIL & EDM SPATTER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄화 카본</b><small>BURNT-ON CARBON</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/aerospace-deburring-plastic-part-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>버 · 플래시</b><small>BURRS & FLASH</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">우주 · 항공 제조에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why is-6">
    <li class="reveal" style="--reveal-delay:0.00s"><b>고광택 · 코팅 툴 표면을 지키는 비마모 세척</b><p>연마 매체와 와이어브러시가 손상시키는 고광택 금형 표면과 테프론 코팅 툴, 복합재 툴을 마모 없이 세척할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>작동 온도 · 장착 상태 세척 가능성</b><p>금형과 툴링을 냉각하거나 분해하지 않고 세척할 수 있는 경우 정지시간을 줄이고 세척 주기를 짧게 할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>2차 폐기물 없음</b><p>회수할 블라스트 매체도, 처리할 폐수와 용제도 없습니다. 제거된 오염물만 진공 흡입이나 청소로 처리합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>전기 설비에 적용 가능한 비전도성</b><p>전기 캐비닛과 제어 시스템을 단락 위험 없이 세척할 수 있습니다. 실제 적용은 전원 상태와 안전조건을 함께 검토해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>작업자 보호</b><p>용제의 VOC 노출을 없애고, 장시간 수작업 스크래핑의 신체 부담과 반복 긴장 손상을 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.45s"><b>건조 대기 없는 표면 전처리</b><p>물을 쓰지 않아 코팅이나 용접 전 건조 시간이 필요 없고, 플래시 러스트 걱정이 없습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 항공 공장에서도,<br>툴링마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>테프론 코팅 복합재 툴의 얇은 수지 층, 지그에 고착된 구조용 접착제, 폴리머 부품의 버는 같은 현장에서 발생하지만 대상의 민감도와 오염물의 두께, 허용되는 세척 강도가 서로 다릅니다.</p>
            <p>바테크는 툴링의 재질과 코팅, 오염물의 종류와 부착 정도, 작동 온도와 접근성을 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/aerospace-dry-ice-blasting-removing-resin-and-release-agents-from-composite-tooling.webp" alt="" loading="lazy" /><b>복합재 툴</b><small>수지 · 이형제</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/aerospace-adhesive-and-sealant-removal-from-aircraft-part-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>생산 지그</b><small>접착제 · 실런트</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/aerospace-deburring-plastic-part-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><b>폴리머 부품</b><small>버 · 플래시</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 툴링에 맞는 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">우주 · 항공에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">항공 제조 안에서도 툴링과 지그, 부품에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/deburring-deflashing.html"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>DEBURRING & DEFLASHING</small><b>디버링 · 디플래싱</b><span>성형·가공 후 버와 플래시를 제거하는 부품 마무리</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.35s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">우주 · 항공과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">항공 복합재 툴링은 플라스틱·복합소재 성형과, 정밀 주조 툴링은 주조 산업과 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/foundry.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-foundry.png" alt="" loading="lazy" /></span><small>FOUNDRY & DIE CASTING</small><b>주조 · 다이캐스팅</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN AEROSPACE & AVIATION</span>
      <h2 class="cmp-h2">글로벌 우주 · 항공 제조 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">항공기 · 엔진 제조사와 방산 · 우주 기업이 복합재 툴링과 성형 금형, 지그 세척에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 우주 · 항공 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:82%"><img src="../assets/img/aerospace-boeing.webp" alt="Boeing" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:70%"><img src="../assets/img/aerospace-airbus_logo.webp" alt="Airbus" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:86%"><img src="../assets/img/aerospace-lockheed-martin.webp" alt="Lockheed Martin" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:86%"><img src="../assets/img/aerospace-northrop-grumman.webp" alt="Northrop Grumman" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:70%"><img src="../assets/img/aerospace-ge_aerospace_logo.webp" alt="GE Aerospace" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:60%"><img src="../assets/img/aerospace-pratt-whitney.webp" alt="Pratt & Whitney" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:48%"><img src="../assets/img/aerospace-rolls-royce.png" alt="Rolls-Royce" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:74%"><img src="../assets/img/aerospace-collins-aerospace.webp" alt="Collins Aerospace" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:72%"><img src="../assets/img/aerospace-honeywell.webp" alt="Honeywell" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:72%"><img src="../assets/img/aerospace-gulfstream_aerospace_logo.webp" alt="Gulfstream" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.40s; --w:70%"><img src="../assets/img/aerospace-blue_origin-logo.webp" alt="Blue Origin" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.44s; --w:74%"><img src="../assets/img/aerospace-spacex_logo.webp" alt="SpaceX" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 툴링에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 항공 툴링이라도 재질과 코팅, 오염물의 종류와 두께, 작동 온도와 접근성, 요구되는 표면 상태에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 툴이나 지그, 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 툴링의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

FOOD_BEVERAGE_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/food-beverage/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-food.png" alt="식품 · 음료 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 식품 · 음료</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">FOOD & BEVERAGE</span>
      <h1>식품 · 음료</h1>
      <p class="cmp-hero-p auto-hero-lead">생산설비의 청결은 제품 품질과 위생 관리에 직접 연결됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">FOOD & BEVERAGE PROCESSING</span>
      <h2 class="cmp-h2">물과 세제 없이,<br>설비를 분해하지 않고 세척할 수 있는가.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>음료·제과·제빵·커피 로스팅·유제품·냉동식품·육가공·스낵·견과 가공 등 식품 생산현장에는 믹서와 블렌더, 슬라이서, 로스터·오븐·발효기, 건조기·압출기·몰드, 컨베이어와 체인, 계량기, 포장기와 라벨러, 접착제 도포기, 팔레타이저, 전기부품과 모터가 운영됩니다.</p>
      <p>이 설비에는 탄화된 식품 잔류물, 단백질 축적물, 유지와 지방산, 설탕·시럽과 캐러멜화 당분, 전분, 조미료 잔류물, 굳은 반죽, 효모·곰팡이, 유제품 잔류물, 접착제와 라벨이 쌓입니다. 축적물은 설비 효율을 떨어뜨리고 제품 품질과 교차오염, 위생 기준 준수에 영향을 줍니다.</p>
      <p>기존 방식은 물과 세제로 세척하고 건조하기까지 시간이 오래 걸리며, 전기부품과 모터 주변은 물을 쓰기 어렵습니다. 설비를 냉각하고 분해해야 하는 경우가 많아 세척은 곧 생산 중단을 의미했습니다.</p>
      <p class="auto-intro-close">따라서 식품·음료 제조에서의 세척은 <b>물과 화학약품 없이, 설비를 분해하지 않고, 위생 기준을 만족하며 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/food-beverage-cleaning-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">식품 · 음료 제조에서<br>드라이아이스 세척이 활용되는 주요 설비</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">OVENS, ROASTERS & PROOFERS</span>
      <h3>오븐 · 로스터 · 발효기</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/food-beverage-dry-ice-blasting-granola-oven.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/food-beverage-burned-wafer-dough-resides-cleaned-from-stainless-steel-wafer-plates.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">탄화된 당분과 반죽 잔류물을<br>뜨거운 상태의 설비에서 제거합니다.</p>
      <div class="cmp-text auto-text"><p>오븐 벨트와 웨이퍼 플레이트, 로스터 내부에는 탄화된 식품 입자와 캐러멜화된 당분, 눌어붙은 반죽이 층을 이루며 쌓입니다. 냉각을 기다린 뒤 긁어내는 기존 방식은 시간이 오래 걸리고 스테인리스 표면을 손상시킬 수 있습니다.</p><p>드라이아이스 세척은 설비가 뜨거운 상태에서도 적용할 수 있어 냉각 대기 시간을 줄일 수 있으며, 오븐 벨트의 그래놀라·당분 축적물과 웨이퍼 플레이트의 탄화 반죽을 제거한 사례가 Cold Jet 자료에 제시되어 있습니다. 물을 쓰지 않으므로 건조 과정도 필요하지 않습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>오븐 벨트 · 오븐 내부</li><li>로스터</li><li>웨이퍼 플레이트 · 베이킹 몰드</li><li>발효기 · 건조기</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">MIXERS, FRYERS & COOKERS</span>
      <h3>믹서 · 프라이어 · 조리설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/food-beverage-dough-carbon-and-grease-removed-from-food-mixer.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/food-beverage-cleaning-oil-residue-from-fryers-and-cookers.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">반죽 · 탄화물 · 그리스와 기름 잔류물을<br>손이 닿기 어려운 구석까지 제거합니다.</p>
      <div class="cmp-text auto-text"><p>믹서와 블렌더에는 굳은 반죽과 탄화물, 그리스가 축과 날개 뒤편에 쌓이고, 프라이어와 쿠커에는 기름과 지방산이 고착됩니다. 이런 부위는 수작업으로 닿기 어렵고 세제 잔류 우려도 있습니다.</p><p>드라이아이스 세척은 세정 매체가 승화하므로 설비에 잔류물이 남지 않고, 구석과 틈새에 접근할 수 있어 전체적인 청결도를 높이는 데 도움이 됩니다. Cold Jet 자료에는 식품 믹서의 반죽·탄화물·그리스 제거와 프라이어·쿠커의 기름 잔류물 제거 사례가 소개되어 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>믹서 · 블렌더</li><li>프라이어 · 쿠커</li><li>슬라이서 · 분할기</li><li>압출기 · 성형 몰드</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">CONVEYORS & CHAINS</span>
      <h3>컨베이어 · 체인</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/food-beverage-cleaning-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">긴 컨베이어 라인을 분해하지 않고<br>운전 상태에서 세척할 수 있는 경우가 있습니다.</p>
      <div class="cmp-text auto-text"><p>컨베이어와 체인, 냉각 컨베이어에는 제품 잔류물과 그리스, 초콜릿·피넛버터 같은 점성 식품이 축적됩니다. 긴 라인을 세척하려면 많은 인원과 시간이 필요하고, 물 세척 후 건조도 문제가 됩니다.</p><p>드라이아이스 세척은 컨베이어를 분해하지 않고 현장에서 세척하는 방식으로 활용되며, 설비 조건에 따라 운전 중 세척이 가능한 경우도 있습니다. Cold Jet은 한 제빵 공장이 빵 냉각기와 긴 컨베이어 세척에 투입되던 인원과 시간을 크게 줄인 사례를 인용하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>컨베이어 · 체인</li><li>냉각 컨베이어</li><li>반경형 피더 · 계량기</li><li>밀 · 로드아웃 빈</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">PACKAGING EQUIPMENT</span>
      <h3>포장 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/food-beverage-cleaning-chocolate-and-peanut-butter-from-processing-equipment.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">접착제와 라벨, 제품 잔류물을<br>포장기 · 라벨러에서 제거합니다.</p>
      <div class="cmp-text auto-text"><p>포장기와 백어, 라벨러, 박스 포머, 접착제 도포기, 팔레타이저에는 핫멜트 접착제와 라벨 잔류물, 제품 잔류물, 종이분진이 쌓입니다. 접착제는 용제로도 잘 지워지지 않고, 노즐 주변은 열이나 스크래퍼로 손상되기 쉽습니다.</p><p>드라이아이스 세척은 접착제와 라벨을 열이나 날카로운 도구 없이 제거하는 방식으로 활용되며, 노즐과 센서 같은 정밀 부품을 마모시키지 않습니다. 포장 설비에 대한 자세한 내용은 포장 산업 페이지에서 다룹니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>포장기 · 백어</li><li>라벨러 · 접착제 도포기</li><li>박스 포머 · 팔레타이저</li></ul></div>
      <a class="auto-rel-link" href="../industries/packaging.html"><span>관련 산업</span>포장 <i>→</i></a>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">ELECTRICAL COMPONENTS & FACILITY</span>
      <h3>전기부품 · 모터 · 시설</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">물을 쓸 수 없는 전기부품과 모터,<br>바닥 · 벽 · 덕트까지 건식으로 세척합니다.</p>
      <div class="cmp-text auto-text"><p>식품 공장에는 전기부품과 모터, 센서, 제어반이 곳곳에 있어 물 세척이 어렵고, 냉동창고와 바닥·벽·천장·덕트·배관은 넓은 면적을 세척해야 합니다.</p><p>드라이아이스는 비전도성이고 수분을 남기지 않아 전기부품과 모터, 센서를 손상 없이 세척하는 데 활용할 수 있습니다. 실제 적용은 전원 상태와 안전조건을 함께 검토해야 합니다. 냉동창고는 저온 상태에서 물 세척이 어려운 대표적 대상입니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>전기부품 · 모터 · 센서</li><li>냉동창고</li><li>바닥 · 벽 · 천장 · 덕트 · 배관</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">식품 · 음료 설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/food-beverage-burned-wafer-dough-resides-cleaned-from-stainless-steel-wafer-plates.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄화 식품 잔류물</b><small>CARBONIZED FOOD RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/food-beverage-dry-ice-blasting-granola-oven.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>설탕 · 시럽 · 캐러멜화 당분</b><small>SUGAR & SYRUP DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/food-beverage-cleaning-oil-residue-from-fryers-and-cookers.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>유지 · 지방 · 그리스</b><small>GREASE, OILS & FATS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/food-beverage-dough-carbon-and-grease-removed-from-food-mixer.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>굳은 반죽 · 전분</b><small>DOUGH & STARCH BUILDUP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/food-beverage-cleaning-chocolate-and-peanut-butter-from-processing-equipment.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>초콜릿 · 점성 식품</b><small>CHOCOLATE & VISCOUS PRODUCT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/food-beverage-cleaning-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>단백질 · 유제품 잔류물</b><small>PROTEIN & DAIRY RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/ind-card-food.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>조미료 잔류물</b><small>SEASONING RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/food-beverage-removing-labels-and-adhesive-from-rolling-conveyor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제 · 라벨</b><small>ADHESIVES & LABELS</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">식품 · 음료 제조에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>물 · 세제 · 용제를 쓰지 않는 건식 세척</b><p>폐수와 세제 잔류물이 없고 건조 과정이 필요 없습니다. 격리 설치와 폐기물 처리 부담도 줄어듭니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>설비를 분해하지 않고 현장에서 세척</b><p>설비 조건에 따라 뜨거운 상태나 운전 중에도 세척할 수 있는 경우가 있어, 세척으로 인한 생산 중단시간을 줄이는 데 도움이 됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>식품 등급 세정 매체</b><p>드라이아이스는 무색·무미·무취·무독성이며, Cold Jet 자료에 따르면 식품 주변 사용이 FDA 승인된 식품 등급 매체입니다. 공급 시 식품 접촉 기준 인증을 확인해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>스테인리스 · 씰 · 개스킷을 마모시키지 않음</b><p>비마모성이므로 표면을 긁거나 씰과 개스킷을 닳게 하지 않고, 비전도성이어서 전기부품과 센서, 모터에도 적용을 검토할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>구석 · 틈새 접근</b><p>수작업으로 닿기 어려운 모서리와 틈새에 접근할 수 있어 전체 청결도를 높이는 데 도움이 됩니다. Cold Jet은 세균 수 감소와 바이오필름 제거 사례를 제시하고 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 식품 공장에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>오븐의 탄화 잔류물, 믹서의 반죽과 지방, 포장라인의 접착제와 제품 잔류물은 같은 공장에서 발생하지만 오염물의 성질과 부착 정도, 설비의 재질과 위생 요건이 서로 다릅니다.</p>
            <p>바테크는 설비의 재질과 구조, 오염물의 종류, 세척 가능 시간대와 위생 기준을 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다. 청정·건조 압축공기와 식품 등급 드라이아이스 공급도 함께 계획합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/food-beverage-dry-ice-blasting-granola-oven.webp" alt="" loading="lazy" /><b>오븐 · 로스터</b><small>탄화 잔류물 · 당분</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/food-beverage-dough-carbon-and-grease-removed-from-food-mixer.webp" alt="" loading="lazy" /><b>믹서</b><small>반죽 · 지방 · 그리스</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/food-beverage-cleaning-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>컨베이어 · 포장라인</b><small>제품 잔류물 · 접착제</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 설비의 위생 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">식품 · 음료에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">식품·음료 제조 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">식품 · 음료과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">식품 포장라인은 포장 산업과, 용기 성형 금형은 플라스틱 산업과 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN FOOD & BEVERAGE PLANTS</span>
      <h2 class="cmp-h2">글로벌 식품 · 음료 생산 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">스낵·음료·육가공·유통 기업이 생산설비 위생 관리에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 식품 · 음료 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:66%"><img src="../assets/img/food-beverage-fritolay.jpg" alt="Frito-Lay" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:56%"><img src="../assets/img/food-beverage-kraft.jpg" alt="Kraft" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:58%"><img src="../assets/img/food-beverage-keurig_dr_pepper.svg_.jpg" alt="Keurig Dr Pepper" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:92%"><img src="../assets/img/food-beverage-rastellis-logo-1.jpg" alt="Rastelli's" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:62%"><img src="../assets/img/food-beverage-hy-vee.jpg" alt="Hy-Vee" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:84%"><img src="../assets/img/food-beverage-butcherbox_logo-1.jpg" alt="ButcherBox" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 생산설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 식품 설비라도 재질과 구조, 오염물의 종류와 부착 정도, 세척 가능 시간대와 위생 기준에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 설비 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산설비의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

PACKAGING_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/packaging/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-packaging.png" alt="포장 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 포장</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">PACKAGING</span>
      <h1>포장</h1>
      <p class="cmp-hero-p auto-hero-lead">고속 포장라인에서 세척 시간은 곧 라인 가동률입니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">PACKAGING MANUFACTURING</span>
      <h2 class="cmp-h2">접착제와 잉크, 제품 잔류물이<br>라인 정지와 불량의 원인이 됩니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>포장 산업은 인쇄·컨버팅 설비와 라벨링·접착 설비, 컨베이어·씰바·박스 포머·그리퍼 같은 포장라인 설비, 그리고 사출·블로우·PET 프리폼·열성형 금형을 운영하는 플라스틱 성형 공정으로 구성됩니다.</p>
      <p>인쇄 스테이션에는 마른 잉크와 바니시가, 접착제 노즐과 라벨러에는 핫멜트 접착제가, 포장라인에는 제품 잔류물과 카톤 분진, 그리스가 쌓입니다. 금형에는 오프가스 잔류물과 수지가, 열성형 툴에는 셀룰로오스 섬유와 칼슘 침착물이 축적됩니다.</p>
      <p>이 축적물은 라인 잼과 씰 불량, 인쇄 결함과 쇼트샷의 원인이 됩니다. 기존 방식인 수작업 스크래핑과 용제는 노동집약적이고 VOC 노출 문제가 있으며, 접착제 노즐은 토치로 태우거나 교체하는 경우도 많았습니다. 설비를 냉각하고 분해해야 하는 만큼 세척은 곧 정지시간이었습니다.</p>
      <p class="auto-intro-close">따라서 포장 산업에서의 세척은 <b>정밀 부품을 손상시키지 않고, 분해 없이, 라인 정지시간을 최소화하며 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/packaging-packaging-line-being-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">포장 산업에서<br>드라이아이스 세척이 활용되는 주요 공정</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PRINTING & GRAVURE EQUIPMENT</span>
      <h3>인쇄 · 그라비어 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-flexographic-printing-press.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">수년간 쌓인 잉크와 바니시를<br>수작업으로는 닿지 않던 부위까지 제거합니다.</p>
      <div class="cmp-text auto-text"><p>포장 인쇄기와 그라비어 설비에는 마른 잉크와 바니시, 접착제 층이 쌓여 인쇄 품질을 떨어뜨립니다. 용제와 수작업으로는 깊이 쌓인 축적물에 닿기 어렵습니다.</p><p>드라이아이스 세척은 설비 표면을 손상시키지 않고 축적된 잉크와 바니시를 제거하는 방식으로 활용됩니다. Cold Jet은 수년간 쌓인 잉크를 수작업으로 처리하지 못했던 컨버팅 업체의 인쇄 스탠드 세척 사례와, 골판지 인쇄 업체가 프레스 세척 시간을 크게 줄인 사례를 제시하고 있습니다. 인쇄 설비 전반은 인쇄 산업 페이지에서 자세히 다룹니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>인쇄 프레스 · 인쇄 스탠드</li><li>그라비어 설비</li><li>잉크 트레이 · 스탠드</li></ul></div>
      <a class="auto-rel-link" href="../industries/printing.html"><span>관련 산업</span>인쇄 <i>→</i></a>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">LABELING & ADHESIVE EQUIPMENT</span>
      <h3>라벨링 · 접착 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/food-beverage-removing-labels-and-adhesive-from-rolling-conveyor-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">접착제 노즐 헤드를 토치나 스크래퍼 없이,<br>교체하지 않고 세척합니다.</p>
      <div class="cmp-text auto-text"><p>접착제 노즐 헤드와 라벨링 시스템에는 핫멜트 접착제가 고착되어 생산 문제를 일으킵니다. 기존에는 토치로 태우거나 긁어내 VOC 위험과 손상 위험이 있었고, 노즐을 통째로 교체하는 비용도 들었습니다.</p><p>드라이아이스 세척은 열이나 날카로운 도구 없이 접착제 잔류물을 빠르게 제거하는 방식으로 활용되며, 수작업으로 접근하기 어려운 부위에도 닿습니다. 컨베이어에 붙은 라벨과 접착제 제거에도 같은 방식이 적용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>접착제 노즐 헤드 · 도포기</li><li>라벨러</li><li>히트 실러 · 핫나이프</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">PACKAGING LINE EQUIPMENT</span>
      <h3>포장라인 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/packaging-packaging-line-being-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">컨베이어 · 씰바 · 기어 · 스타휠을<br>장착 상태에서 세척해 분해 시간을 줄입니다.</p>
      <div class="cmp-text auto-text"><p>컨베이어와 씰바, 박스 포머, 오리엔터, 그리퍼, 패커에는 접착제와 제품 잔류물, 카톤 분진, 그리스가 쌓여 성능에 영향을 줍니다. 기어와 스타휠처럼 복잡한 구동부는 분해와 재조립에 시간이 듭니다.</p><p>드라이아이스 세척은 이 부품들을 장착 상태에서 세척하는 방식으로 활용되어, 분해·재조립에 드는 시간을 줄이는 데 도움이 됩니다. Cold Jet은 수작업과 화학 세척으로 제거되지 않던 고착 접착제를 드라이아이스로 빠르게 제거한 포장 공장 사례를 소개하고 있습니다. 비전도성이므로 센서와 PLC 패널 주변에도 적용을 검토할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>컨베이어 · 롤러 · 체인 레일</li><li>씰바 · 히트 실러</li><li>박스 포머 · 패커 · 오리엔터</li><li>기어 · 스타휠 · 그리퍼</li><li>계량기 · 백어 · 팔레타이저</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">INJECTION & PET MOLD CLEANING</span>
      <h3>사출 · PET 금형 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/packaging-pet-injection-mold-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">캐비티 · 벤트 · 파팅라인의 오프가스 잔류물을<br>금형이 뜨거운 상태에서 제거합니다.</p>
      <div class="cmp-text auto-text"><p>용기용 사출금형과 PET 프리폼 금형에는 오프가스 잔류물과 수지가 캐비티와 벤트, 파팅라인, 미세 기공에 쌓여 부품 품질을 떨어뜨립니다. 금형을 분리해 세척하면 냉각과 재조립에 시간이 듭니다.</p><p>드라이아이스 세척은 금형을 뜨거운 상태로 프레스에 장착한 채 세척하는 방식으로 활용되며, 비마모성이므로 치수와 미러 마감을 유지합니다. Cold Jet은 한 의약품 용기 제조사가 분해 없이 금형 세척 시간을 크게 줄인 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>용기 사출금형</li><li>PET 프리폼 금형</li><li>캐비티 · 벤트 · 파팅라인</li></ul></div>
      <a class="auto-rel-link" href="../industries/plastics-composites.html"><span>관련 산업</span>플라스틱 · 복합소재 <i>→</i></a>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">BLOW MOLD & THERMOFORM TOOLING</span>
      <h3>블로우 금형 · 열성형 툴링</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/packaging-cleaning-a-plastic-bottle-blow-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/packaging-dry-ice-cleaning-of-a-plastic-thermoforming-mold.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">블로우 금형의 에어벤트와 열성형 툴의 섬유 · 칼슘 침착물을<br>전용 노즐로 처리합니다.</p>
      <div class="cmp-text auto-text"><p>블로우 금형과 PET 금형은 후면 테이퍼와 에어벤트에 오프가스 잔류물이 쌓여 기존 방식으로는 충분히 접근하기 어렵습니다. 식품 포장과 몰드 파이버 제품용 열성형 툴에는 셀룰로오스 섬유와 칼슘 침착물, 공정 잔류물이 축적됩니다.</p><p>Cold Jet은 이런 어려운 형상에 닿는 전용 노즐을 제공하며, 한 음료 보틀러가 블로우 금형 세척 시간을 크게 줄인 사례와 몰드 파이버 제조사가 수작업 스크래핑의 표면 손상 없이 금형당 세척 시간을 줄인 사례를 소개하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>블로우 금형 · 에어벤트</li><li>열성형 툴링</li><li>몰드 파이버 금형</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">포장 설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/food-beverage-removing-labels-and-adhesive-from-rolling-conveyor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>핫멜트 접착제</b><small>HOT-MELT ADHESIVE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-flexographic-printing-press.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>마른 잉크 · 바니시</b><small>DRIED INK & VARNISH</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/packaging-packaging-line-being-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>제품 잔류물</b><small>PRODUCT RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카톤 분진 · 종이분진</b><small>CARTON & PAPER DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>그리스</b><small>GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/packaging-pet-injection-mold-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오프가스 잔류물</b><small>OFF-GASSING RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/packaging-cleaning-a-plastic-bottle-blow-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>플라스틱 수지</b><small>PLASTIC RESIN</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/packaging-dry-ice-cleaning-of-a-plastic-thermoforming-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>셀룰로오스 섬유 · 칼슘 침착물</b><small>CELLULOSE FIBERS & CALCIUM DEPOSITS</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">포장 산업에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>분해 없는 현장 세척</b><p>씰바와 접착제 노즐, 컨베이어 조립체를 분해하지 않고 세척할 수 있는 경우 냉각·분해·재조립 시간을 줄이고 라인 가동률을 높이는 데 도움이 됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>정밀 부품을 손상시키지 않음</b><p>접착제 노즐, 그리퍼, PLC 패널, 미러 마감 금형을 마모 없이 세척할 수 있어 씰 품질과 제품 외관을 일정하게 유지하는 데 기여합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>비전도성 · 수분 없음</b><p>센서와 PLC 패널, 접착제 노즐 주변을 수분에 의한 단락 위험 없이 세척할 수 있습니다. 실제 적용은 전원 상태와 안전조건을 함께 검토해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>2차 폐기물 없음</b><p>용제에 젖은 걸레나 폐용제 같은 유해 폐기물 처리 비용이 발생하지 않습니다. 제거된 오염물만 청소하면 됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>식품 · 의약품 포장에 적합한 매체</b><p>드라이아이스는 식품 등급 매체이며 물과 화학약품을 쓰지 않습니다. Cold Jet은 세척 후 ATP 위생 검사를 통과한 사례를 제시하고 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 포장 공장에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>접착제 노즐의 핫멜트, 포장라인 기어의 카톤 분진과 그리스, PET 금형 벤트의 오프가스 잔류물은 같은 공장에서 발생하지만 대상의 정밀도와 오염물의 성질, 접근성이 서로 다릅니다.</p>
            <p>바테크는 설비의 재질과 구조, 오염물의 종류와 부착 정도, 세척 가능 시간대를 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건과 노즐 구성을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/food-beverage-removing-labels-and-adhesive-from-rolling-conveyor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>접착제 노즐 · 라벨러</b><small>핫멜트 접착제</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp" alt="" loading="lazy" /><b>포장라인 구동부</b><small>카톤 분진 · 그리스</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/packaging-cleaning-a-plastic-bottle-blow-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>PET · 블로우 금형</b><small>오프가스 잔류물</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 라인의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">포장에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">포장 산업 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">포장과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">포장라인은 식품·음료 공장과, 용기 금형은 플라스틱 성형과, 포장 인쇄는 인쇄 산업과 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/food-beverage.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-food.png" alt="" loading="lazy" /></span><small>FOOD & BEVERAGE</small><b>식품 · 음료</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/printing.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /></span><small>PRINTING</small><b>인쇄</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN PACKAGING PLANTS</span>
      <h2 class="cmp-h2">글로벌 포장 제조 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">용기 · 연포장 · 골판지 · 종이 포장 기업이 금형과 포장라인 세척에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 포장 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:66%"><img src="../assets/img/plastics-composites-amcor_logo.webp" alt="Amcor" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:66%"><img src="../assets/img/plastics-composites-berry-logo.webp" alt="Berry Global" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:60%"><img src="../assets/img/packaging-tetra-pak-logo.webp" alt="Tetra Pak" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:56%"><img src="../assets/img/packaging-ball_corporation_logo.webp" alt="Ball Corporation" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:66%"><img src="../assets/img/packaging-sonoco.webp" alt="Sonoco" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:66%"><img src="../assets/img/plastics-composites-silgan.jpg" alt="Silgan" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:74%"><img src="../assets/img/packaging-smurfit_westrock_logo.webp" alt="Smurfit Westrock" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:66%"><img src="../assets/img/packaging-smurfit_kappa_logo.webp" alt="Smurfit Kappa" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:74%"><img src="../assets/img/packaging-huhtamaki_logo.webp" alt="Huhtamaki" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:66%"><img src="../assets/img/packaging-pactiv_logo.webp" alt="Pactiv" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.40s; --w:66%"><img src="../assets/img/packaging-graham-logo.webp" alt="Graham Packaging" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.44s; --w:70%"><img src="../assets/img/packaging-plastipak-official-logo.webp" alt="Plastipak" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 포장라인에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 포장 설비라도 재질과 구조, 오염물의 종류와 부착 정도, 세척 가능 시간대와 위생 요건에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 금형, 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 포장라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

PRINTING_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/printing/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-printing.png" alt="인쇄 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 인쇄</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">PRINTING</span>
      <h1>인쇄</h1>
      <p class="cmp-hero-p auto-hero-lead">잉크 축적은 정렬 오류와 색 편차로 나타납니다 — 세척 주기가 인쇄 품질을 결정합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">COMMERCIAL & INDUSTRIAL PRINTING</span>
      <h2 class="cmp-h2">분해 없이 세척할 수 있어야<br>충분히 자주 세척할 수 있습니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>상업 인쇄와 연포장·라벨 인쇄 현장에는 플렉소·옵셋·그라비어·디지털·활판 인쇄기와 롤러·드럼, 잉크 트레이와 피더·딜리버리 유닛, 기어 조립체와 데크 가이드, 그리퍼와 사이드 프레임, 라미네이터·코팅 설비, 접착제 노즐과 센서·제어장치가 운영됩니다.</p>
      <p>이 설비에는 굳은 잉크와 바니시, 접착제, 그리스와 잉크 미스트, 종이분진이 쌓입니다. 사이드 프레임과 그리퍼, 롤러의 잉크 축적은 정렬 문제와 잉크 튐, 색 편차로 이어지고, 기어와 베어링 하우징의 오염은 기계적 마모와 레지스터 오류의 원인이 됩니다.</p>
      <p>퍼티 나이프와 픽, 와이어브러시, 용제를 쓰는 기존 세척은 느리고 노동집약적이며, 롤러 표면과 아닐록스 셀, 센서를 손상시킬 수 있습니다. Cold Jet에 따르면 인쇄기 전체를 세척하는 데 하루 이상 걸리는 경우도 있어, 현장은 세척을 미루고 축적물은 쌓여 품질 문제가 누적됩니다.</p>
      <p class="auto-intro-close">따라서 인쇄 산업에서의 세척은 <b>롤러와 센서를 손상시키지 않고, 분해 없이, 충분히 자주 할 수 있을 만큼 빠르게 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/printing-large-printing-press-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">인쇄 산업에서<br>드라이아이스 세척이 활용되는 주요 설비</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PRINTING PRESSES & ROLLERS</span>
      <h3>인쇄기 · 롤러</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-flexographic-printing-press.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/printing-large-printing-press-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">플렉소 · 그라비어 · 옵셋 · 활판 인쇄기의<br>굳은 잉크와 그리스를 롤러 표면 손상 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>인쇄기 부품과 롤러, 저널, 잉크 핸들링 시스템에는 굳은 잉크와 그리스, 잔류물이 쌓입니다. 인쇄 환경에 수분이나 용제를 들이지 않으면서 이를 제거해야 하고, 롤러 표면은 마모되어서는 안 됩니다.</p><p>드라이아이스 세척은 플렉소·그라비어·옵셋·활판 설비의 굳은 잉크와 그리스를 제거하는 핵심 적용 분야로, 비마모성이어서 롤러 표면을 보호하면서 고착 오염물을 제거하는 방식으로 활용됩니다. 설비를 조립 상태로, 생산 직후 아직 따뜻한 상태에서 세척할 수 있는 경우가 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>플렉소 · 옵셋 · 그라비어 인쇄기</li><li>디지털 · 활판 인쇄기</li><li>롤러 · 드럼 · 저널</li><li>그리퍼 · 사이드 프레임</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">INK TRAYS & FEED/DELIVERY UNITS</span>
      <h3>잉크 트레이 · 피더 · 딜리버리 유닛</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/printing-cleaning-ink-try-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">스크래퍼와 걸레가 놓치는 모서리까지<br>잉크 침착물을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>스테인리스 잉크 트레이와 딜리버리 유닛, 피더 시스템에는 두꺼운 잉크 침착물이 쌓여 수작업으로 제거하기에 시간이 오래 걸립니다. 스크래퍼와 걸레가 닿지 않는 모서리와 틈새에 남은 잉크는 잉크 전이와 인쇄 일관성에 영향을 줍니다.</p><p>드라이아이스 세척은 모서리와 틈새에 닿아 점진적 축적을 막는 방식으로 활용됩니다. Cold Jet은 한 상업 인쇄사가 수작업으로 한 시간 걸리던 잉크 트레이 세척을 크게 단축한 사례를 소개하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>잉크 트레이 · 리저버</li><li>피더 유닛 · 딜리버리 유닛</li><li>잉크 스탠드</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">GEAR ASSEMBLIES & DRIVE SYSTEMS</span>
      <h3>기어 조립체 · 구동 시스템</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/printing-dry-ice-blasting-removes-heavy-ink-and-grease-buildup-from-printing-press.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">구동 기어와 베어링 하우징의 잉크 미스트 · 그리스 · 종이분진을<br>분해 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>구동 기어와 데크 가이드, 베어링 하우징에는 잉크 미스트와 그리스, 종이분진이 쌓여 기계적 마모와 레지스터 오류로 이어집니다. 복잡한 기어 트레인과 저널은 분해하지 않으면 세척이 어렵습니다.</p><p>드라이아이스 세척은 기어 트레인과 저널 내부까지 닿아 분해 없이 오염물을 제거하는 방식으로 활용됩니다. 구동부를 깨끗하게 유지하면 마찰을 줄이고 정렬 불량과 조기 고장의 원인이 되는 유격을 예방하는 데 도움이 됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>구동 기어 · 기어 트레인</li><li>데크 가이드 · 데크 조립체</li><li>베어링 하우징 · 저널</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">FLEXIBLE PACKAGING & LABEL PRINTING</span>
      <h3>연포장 · 라벨 인쇄 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/printing-cleaning-burnished-ink-from-flexible-packaging-equipment-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/printing-dry-ice-blasting-removing-burnished-ink-and-adhesive-from-packaging-line.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">수성 · 유성 잉크와 접착제 잔류물을<br>외주 없이 사내에서 처리합니다.</p>
      <div class="cmp-text auto-text"><p>연포장과 라벨 인쇄는 여러 잉크와 접착제, 기재를 다루며 생산 일정이 빠듯해 롤러 세척을 외주에 맡기는 곳이 많습니다. 라벨 인쇄 설비에는 잉크와 접착제 캐리오버, 감긴 라벨과 이탈 라벨이 수년간 축적됩니다.</p><p>드라이아이스 세척은 수성·유성 잉크와 접착제 잔류물을 모두 제거하는 방식으로 활용되어 세척을 사내로 가져오는 데 도움이 됩니다. Cold Jet은 골판지 인쇄사와 봉투 제조사가 물·화학 세척 대비 세척 시간을 크게 줄인 사례, 라벨 인쇄사가 수년간 쌓인 잉크·접착제를 정밀 표면 손상 없이 제거한 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>연포장 인쇄 라인</li><li>라벨 프레스</li><li>인쇄 헤드 · 데크 조립체</li><li>접착제 노즐 · 도포기</li></ul></div>
      <a class="auto-rel-link" href="../industries/packaging.html"><span>관련 산업</span>포장 <i>→</i></a>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">LAMINATORS & COATING EQUIPMENT</span>
      <h3>라미네이터 · 코팅 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">좁은 공간에 강하게 붙은 접착제를<br>물 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>라미네이팅·코팅·메탈라이징 설비에는 접근이 어려운 부위에 접착제와 잔류물이 강하게 고착됩니다. 물을 쓰는 수작업은 좁은 공간에서 문제가 많고 시간이 오래 걸립니다.</p><p>드라이아이스 세척은 수작업으로 닿지 않는 부위에 접근해 고착 접착제를 제거하는 방식으로 활용됩니다. Cold Jet은 라미네이터 세척 시간을 절반 이하로 줄인 사례를 소개하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>라미네이터</li><li>코팅 · 메탈라이징 설비</li><li>고무 · 플라스틱 롤러</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">인쇄 설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/printing-cleaning-burnished-ink-from-flexible-packaging-equipment-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>굳은 잉크</b><small>BURNISHED INK</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/printing-cleaning-ink-try-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>잉크 침착물</b><small>INK DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-flexographic-printing-press.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>바니시</b><small>VARNISH</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/printing-dry-ice-blasting-removing-burnished-ink-and-adhesive-from-packaging-line.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제 · 라벨 잔류물</b><small>ADHESIVE & LABEL RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/printing-dry-ice-blasting-removes-heavy-ink-and-grease-buildup-from-printing-press.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>그리스 · 잉크 미스트</b><small>GREASE & INK MIST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/printing-large-printing-press-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>종이분진</b><small>PAPER DUST</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">인쇄 산업에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>조립 상태 · 온간 상태 세척</b><p>설비를 분해하지 않고, 생산 직후 따뜻한 상태에서 세척할 수 있는 경우가 있어 세척이 생산 중단이 아닌 일상 정비가 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>롤러 · 아닐록스 · 센서를 마모시키지 않음</b><p>스크래핑과 와이어브러시가 닳게 하는 롤러 표면과 아닐록스 셀, 민감한 센서와 전자 제어장치를 손상 없이 세척할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세척 주기를 짧게 할 수 있는 속도</b><p>Cold Jet은 수작업 대비 세척 시간을 크게 줄인 사례를 다수 제시합니다. 자주 세척하면 축적물이 품질에 영향을 주기 전에 관리할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>수분 · 용제 없는 건식 세척</b><p>인쇄 환경에 수분과 용제를 들이지 않고, 세척 직후 바로 생산에 복귀할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>2차 폐기물 없음</b><p>용제에 젖은 걸레나 흡착 패드 같은 유해 폐기물이 발생하지 않아 처리 비용과 매립 폐기물을 줄일 수 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 인쇄 공장에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>잉크 트레이의 두꺼운 잉크 침착물, 구동 기어의 그리스와 종이분진, 라미네이터의 고착 접착제는 같은 현장에서 발생하지만 대상의 민감도와 오염물의 두께, 접근성이 서로 다릅니다.</p>
            <p>바테크는 설비의 재질과 구조, 잉크·접착제의 종류와 부착 정도, 세척 가능 시간대를 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/printing-cleaning-ink-try-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>잉크 트레이</b><small>두꺼운 잉크 침착물</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/printing-dry-ice-blasting-removes-heavy-ink-and-grease-buildup-from-printing-press.webp" alt="" loading="lazy" /><b>구동 기어</b><small>그리스 · 종이분진</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/printing-dry-ice-blasting-removing-burnished-ink-and-adhesive-from-packaging-line.webp" alt="" loading="lazy" /><b>연포장 라인</b><small>굳은 잉크 · 접착제</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 인쇄기의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">인쇄에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">인쇄 산업 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">인쇄과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">연포장·라벨 인쇄는 포장 산업과, 식품 포장 인쇄는 식품·음료 산업과 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/food-beverage.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-food.png" alt="" loading="lazy" /></span><small>FOOD & BEVERAGE</small><b>식품 · 음료</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN PRINTING OPERATIONS</span>
      <h2 class="cmp-h2">글로벌 인쇄 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">상업 인쇄와 포장 인쇄 기업이 인쇄기와 롤러, 잉크 시스템 세척에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 인쇄 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:66%"><img src="../assets/img/packaging-smurfit_kappa_logo.webp" alt="Smurfit Kappa" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:76%"><img src="../assets/img/printing-transcontinental_logo.webp" alt="Transcontinental" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:66%"><img src="../assets/img/printing-coveris_logo.webp" alt="Coveris" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:70%"><img src="../assets/img/printing-graphic-packaging-logo.webp" alt="Graphic Packaging" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:56%"><img src="../assets/img/printing-quad_wordmark_logo.webp" alt="Quad" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:70%"><img src="../assets/img/printing-shutterfly_logo.webp" alt="Shutterfly" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 인쇄기에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 인쇄 설비라도 롤러와 부품의 재질, 잉크와 접착제의 종류, 축적 정도와 세척 가능 시간대에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 인쇄기의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

POWER_GENERATION_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/power-generation/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-power.png" alt="발전 · 전력 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 발전 · 전력</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">POWER GENERATION</span>
      <h1>발전 · 전력</h1>
      <p class="cmp-hero-p auto-hero-lead">설비의 오염은 점검과 유지보수뿐 아니라 운전 신뢰성과도 연결됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">POWER GENERATION & UTILITIES</span>
      <h2 class="cmp-h2">물과 연마재를 쓸 수 없는 설비를<br>정지 기간 안에 세척해야 합니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>가스·수력·원자력·석탄 화력 발전소와 변전소에는 터빈 블레이드와 연소실, HRSG 핀튜브와 보일러 튜브뱅크, 발전기 고정자·회전자 권선, 변압기 부싱과 애자, 개폐기·제어반·보호계전기 같은 설비가 운영됩니다.</p>
      <p>이 설비에는 탄소 침착물과 오일, 파울링, 표면 산화물, 암모늄염과 유황 침착물, 재와 슬래그·스케일, 염분과 석탄분진 같은 전도성 오염물이 쌓입니다. 핀 표면의 침착물은 열전달을 떨어뜨리고, 권선과 애자의 전도성 오염은 절연저항 저하와 누설전류, 플래시오버로 이어집니다.</p>
      <p>기존 방식인 화학 용제와 고압수, 연마 블라스팅은 수분에 의한 부식, 정밀 부품에의 그릿 잔류, 절연물 손상 위험이 있고 대량의 2차 폐기물을 만듭니다. 세척은 정해진 정지 기간 안에 끝나야 하며, 원자력 시설에서는 폐기물 처리 비용이 세척 비용을 넘기도 합니다.</p>
      <p class="auto-intro-close">따라서 발전 · 전력에서의 세척은 <b>전기설비를 손상시키지 않고, 수분과 2차 폐기물 없이, 정지 기간 안에 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/power-generation-cleaning-generator-stator-windings-in-steam-generation-plan-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">발전 · 전력에서<br>드라이아이스 세척이 활용되는 주요 설비</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">GAS TURBINES & HRSG</span>
      <h3>가스터빈 · 배열회수보일러(HRSG)</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/power-generation-dry-ice-blasting-removing-surface-rust-from-turbine-compressor-component.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">터빈의 탄소 침착물과 HRSG 핀튜브의 파울링을<br>분해 없이 제거해 열효율을 회복합니다.</p>
      <div class="cmp-text auto-text"><p>가스터빈의 블레이드·연소실·압축기 섹션에는 탄소 침착물과 오일, 입자상 물질이 쌓이고, HRSG 튜브 번들에는 암모늄염(황산수소암모늄)과 유황 침착물, 산화철, 파울링이 촘촘한 핀 사이에 축적됩니다.</p><p>드라이아이스 세척은 터빈을 완전 분해하지 않고 현장에서 세척하는 방식으로 활용되며, 튜브 번들 용접부를 손상시키지 않고 핀 사이까지 닿아 열전달 효율을 회복하는 데 도움이 됩니다. Cold Jet은 수작업으로 며칠 걸리던 8MW 터빈 세척을 수 시간에 마친 사례와, 세척 후 출력이 개선된 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>터빈 블레이드 · 연소실 · 압축기 섹션</li><li>HRSG 핀튜브 · 이코노마이저</li><li>튜브 번들 · 튜브 시트</li><li>시동 모터 · 알터네이터 · 보조설비</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">HYDROELECTRIC GENERATORS</span>
      <h3>수력 발전기 · 권선</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/power-generation-cleaning-hydroelectric-generator-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">고정자 · 회전자 권선의 전도성 오염을 제거해<br>절연저항을 회복합니다.</p>
      <div class="cmp-text auto-text"><p>수십 년 운전된 수력 발전기의 고정자·회전자 권선과 여자 시스템에는 탄소분진과 오일, 습기가 결합된 전도성 오염이 쌓여 절연저항과 성극지수(PI)를 떨어뜨립니다. 물 세척은 권선에 수분을 남기고, 연마재는 절연물을 손상시킵니다.</p><p>드라이아이스는 비전도성이고 수분을 남기지 않아 권선부터 주철 하우징까지 발전기 부품 세척에 활용됩니다. Cold Jet은 세척 후 절연저항과 성극지수가 크게 개선된 사례와, 폐기 대상으로 판단됐던 발전기를 세척 후 복귀시킨 사례를 소개하고 있습니다. 터빈 러너와 흡출관의 퇴적물·조류 제거에도 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>고정자 · 회전자 권선</li><li>발전기 하우징 · 여자 시스템</li><li>터빈 러너 · 흡출관</li><li>제어반 · 보호계전기</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">NUCLEAR FACILITIES</span>
      <h3>원자력 시설 · 제염</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/power-generation-dry-ice-blasting-is-used-in-nuclear-facilities-for-decontamination-and-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">세정 매체가 승화하므로<br>방사성 폐기물 부피를 늘리지 않습니다.</p>
      <div class="cmp-text auto-text"><p>원자력 시설에서는 세척에 쓴 물이나 연마재가 그대로 방사성 폐기물이 됩니다. 운전 중 시설의 열교환기·증기발생기·펌프·환기 설비 유지보수와 해체·제염 과정에서 폐기물 부피는 곧 처리 비용입니다.</p><p>드라이아이스는 충돌 후 승화해 제거된 오염물 외에 2차 폐기물을 남기지 않습니다. Cold Jet은 벽·바닥·핫셀·글러브박스·덕트의 표면 오염 제거, 해체 전 정리(POCO) 단계의 느슨한 오염과 스케일 제거, 재사용 전 펌프·밸브·공구·차폐재 세척에 적용된 사례를 제시하며, 연마 블라스팅 대비 폐기물 부피를 크게 줄였다고 설명합니다. 적용은 시설의 방사선 관리 규정에 따라 검토해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>증기발생기 · 열교환기</li><li>펌프 · 밸브 · 배관 · 계측기</li><li>핫셀 · 글러브박스 · 환기 덕트</li><li>바닥 · 벽 · 차폐재</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">BOILERS & STEAM TURBINES</span>
      <h3>보일러 · 증기터빈 · 대기오염 방지설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/power-generation-cleaning-metallic-fins-on-steam-turbine-rotor-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">재 · 슬래그 · 스케일을 제거하고<br>건조 시간 없이 바로 점검할 수 있습니다.</p>
      <div class="cmp-text auto-text"><p>석탄 화력과 증기 발전 설비의 보일러·과열기·이코노마이저 튜브뱅크에는 재와 그을음, 스케일이 쌓여 튜브 사이를 막고(브리징), 증기터빈 로터와 다이어프램, 응축기 튜브시트에도 침착물이 형성됩니다. SCR 촉매와 전기집진기에는 비산재가 쌓입니다.</p><p>드라이아이스 세척은 튜브 사이의 브리징을 깨고 표면을 점검·비파괴검사 가능한 상태로 만드는 방식으로 활용되며, 물을 쓰지 않아 건조 시간 없이 복귀할 수 있습니다. SCR 허니콤 촉매의 비산재 제거에도 막힘이나 화학적 손상 위험 없이 적용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>보일러 튜브 · 과열기 · 이코노마이저</li><li>증기터빈 블레이드 · 다이어프램 · 케이싱</li><li>응축기 · 열교환기 · 공기예열기</li><li>SCR 촉매 · 전기집진기</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">ELECTRICAL SUBSTATIONS</span>
      <h3>변전설비 · 고전압 기기</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/power-generation-dry-ice-blasting-being-used-to-clean-a-high-voltage-insulator-at-an-electrical-substation.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/power-generation-cleaning-generator-stator-windings-in-steam-generation-plan-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">애자와 부싱의 전도성 오염을 물 없이 제거해<br>누설전류와 플래시오버를 예방합니다.</p>
      <div class="cmp-text auto-text"><p>변전소의 세라믹·폴리머 애자, 변압기 부싱, 차단기, 부스바에는 염분과 석탄분진, 산업 오염물 같은 전도성 침착물이 쌓여 절연 거리를 줄이고 누설전류와 플래시오버, 화재의 원인이 됩니다. 제어반과 보호계전기, SCADA 랙의 분진은 접지 고장과 오동작을 일으킵니다.</p><p>드라이아이스 세척은 물과 연마재 없이 이 오염물을 제거하는 방식으로 활용되어, 짧은 정비 시간 안에 절연 성능을 회복하는 데 도움이 됩니다. 커패시터 뱅크와 전압조정기의 냉각핀 세척에도 적용됩니다. 실제 적용은 활선 여부와 안전 절차를 함께 검토해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>세라믹 · 폴리머 애자</li><li>변압기 부싱 · 라디에이터</li><li>차단기 · 개폐기 · 부스바</li><li>제어반 · 보호계전기 · SCADA</li><li>커패시터 뱅크 · 전압조정기</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">발전 · 전력 설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/power-generation-dry-ice-blasting-removing-surface-rust-from-turbine-compressor-component.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄소 침착물 · 오일</b><small>CARBON DEPOSITS & OILS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/power-generation-cleaning-generator-stator-windings-in-steam-generation-plan-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>전도성 분진 (탄소 · 석탄 · 염분)</b><small>CONDUCTIVE DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/power-generation-cleaning-metallic-fins-on-steam-turbine-rotor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>암모늄염 · 유황 침착물</b><small>AMMONIUM & SULFUR DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>재 · 그을음 · 슬래그</b><small>ASH, SOOT & SLAG</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>스케일 · 파울링</b><small>SCALE & FOULING</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>표면 산화물 · 산화철</b><small>SURFACE OXIDATION & IRON OXIDE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/power-generation-cleaning-hydroelectric-generator-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>퇴적물 · 조류</b><small>SEDIMENT & ALGAE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/power-generation-dry-ice-blasting-being-used-to-clean-a-high-voltage-insulator-at-an-electrical-substation.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>염분 · 대기 오염물</b><small>SALT SPRAY & POLLUTANTS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.48s"><img src="../assets/img/power-generation-dry-ice-blasting-is-used-in-nuclear-facilities-for-decontamination-and-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>방사성 표면 오염</b><small>RADIOACTIVE SURFACE CONTAMINATION</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">발전 · 전력에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why is-6">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비전도성</b><p>권선·변압기·개폐기·제어반 같은 전기설비에 단락이나 절연 손상 위험 없이 적용을 검토할 수 있습니다. 활선 여부와 안전 절차는 별도로 확인해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>수분 없는 건식 세척</b><p>권선의 전기적 트래킹과 수분에 의한 부식을 일으키지 않으며, 건조 시간 없이 바로 점검하거나 복귀할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>2차 폐기물 없음</b><p>폐수 회수와 폐연마재 처리가 필요 없습니다. 원자력 시설에서는 방사성 폐기물 부피를 늘리지 않는다는 점이 특히 중요합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>비마모성</b><p>정밀 가공된 터빈 블레이드 프로파일과 권선 절연물의 모재를 깎아내지 않고 오염물만 제거합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>분해 감소 · 정지 기간 단축</b><p>설치 상태에서 세척할 수 있는 경우 분해·재조립 시간을 줄일 수 있습니다. Cold Jet은 세척 시간을 크게 줄인 발전 사례를 다수 제시하고 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.45s"><b>열전달 효율 회복</b><p>핀튜브와 튜브뱅크 사이의 침착물과 브리징을 제거해 차압을 낮추고 열효율을 회복하는 데 도움이 됩니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 발전소 안에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>터빈 압축기의 탄소 침착물, 발전기 권선의 전도성 분진, 변전소 애자의 염분 오염은 같은 사업소에서 발생하지만 대상의 민감도와 오염물의 성질, 안전 조건이 크게 다릅니다.</p>
            <p>바테크는 설비의 재질과 절연 구조, 오염물의 종류, 정지 기간과 안전 절차를 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/power-generation-dry-ice-blasting-removing-surface-rust-from-turbine-compressor-component.webp" alt="" loading="lazy" /><b>터빈 압축기</b><small>탄소 침착물 · 표면 산화물</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/power-generation-cleaning-generator-stator-windings-in-steam-generation-plan-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>발전기 권선</b><small>전도성 분진 · 오일</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/power-generation-dry-ice-blasting-being-used-to-clean-a-high-voltage-insulator-at-an-electrical-substation.webp" alt="" loading="lazy" /><b>변전소 애자</b><small>염분 · 대기 오염물</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 설비의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">발전 · 전력에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">발전 · 전력 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/rust-corrosion-removal.html"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>RUST, CORROSION & OXIDATION REMOVAL</small><b>녹 · 부식 · 산화물 제거</b><span>표면 녹과 느슨한 산화물(비마모 범위 내)</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">발전 · 전력과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">열교환기·터빈·회전기기 세척은 석유 · 가스 플랜트와, 대형 전기설비 유지보수는 광업과 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/oil-gas.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-oilgas.png" alt="" loading="lazy" /></span><small>OIL & GAS</small><b>오일 · 가스</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/mining.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /></span><small>MINING</small><b>광업</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN POWER GENERATION</span>
      <h2 class="cmp-h2">글로벌 발전 · 전력 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">전력회사와 발전설비 제조사가 터빈·발전기·변전설비 유지보수에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 발전 · 전력 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:72%"><img src="../assets/img/power-generation-siemens_energy_logo.webp" alt="Siemens Energy" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:66%"><img src="../assets/img/power-generation-ge_vernova_logo.webp" alt="GE Vernova" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:50%"><img src="../assets/img/power-generation-pg-e_logo.webp" alt="PG&E" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:74%"><img src="../assets/img/power-generation-southern_california_edison_logo.webp" alt="Southern California Edison" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:74%"><img src="../assets/img/power-generation-logo_new_york_power_authority.webp" alt="New York Power Authority" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:70%"><img src="../assets/img/power-generation-andritz_hydro_logo.webp" alt="Andritz Hydro" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:70%"><img src="../assets/img/power-generation-baker_hughes_logo.webp" alt="Baker Hughes" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:56%"><img src="../assets/img/power-generation-eaton_corporation_logo.webp" alt="Eaton" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:56%"><img src="../assets/img/power-generation-enbw_logo.webp" alt="EnBW" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:66%"><img src="../assets/img/power-generation-first_solar_logo.webp" alt="First Solar" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 발전설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 발전설비라도 재질과 절연 구조, 오염물의 종류와 부착 정도, 정지 기간과 안전 절차에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 발전설비의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

OIL_GAS_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/oil-gas/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/oil-gas-oil__gas_hero_banner-poster.jpg" alt="오일 · 가스 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 오일 · 가스</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">OIL & GAS</span>
      <h1>오일 · 가스</h1>
      <p class="cmp-hero-p auto-hero-lead">오염물은 성능 저하에서 끝나지 않고, 부식과 설비 고장, 작업 안전으로 이어집니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">OIL & GAS · PETROCHEMICAL · REFINING</span>
      <h2 class="cmp-h2">셧다운을 기다리지 않고,<br>운전 중에도 세척할 수 있는가.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>유전과 파이프라인, 정유·석유화학 플랜트에는 열교환기와 핀팬 쿨러, 펌프와 압축기, 압력·저장 용기와 탱크, 배관과 밸브, 터빈·모터 같은 회전기기, 전기 제어반, 프랙 펌프 트럭과 운송 장비가 운영됩니다.</p>
      <p>이 설비에는 중질유와 비투멘, 파라핀, 카본, 산과 화학물질, 가용성 염과 염화물, 유황 침착물, 열화된 도장과 경미한 부식이 쌓입니다. 정기적으로 세척·정비하지 않으면 성능이 떨어지고 배관과 자산에 부식 손상이 진행되며, 작업 환경의 안전에도 영향을 줍니다.</p>
      <p>기존 방식인 샌드블라스팅과 고압수 세척은 표면에 이물과 미생물을 박아 넣거나 수분을 남겨 도장 불량과 부식의 원인이 될 수 있고, 물로 인해 작업장이 미끄럽고 진흙탕이 되기도 합니다. 대부분 셧다운이나 정기보수 기간에만 세척할 수 있어 세척 주기가 길어집니다.</p>
      <p class="auto-intro-close">따라서 석유 · 가스에서의 세척은 <b>수분과 연마재 없이, 설비를 운전 상태로 두고, 연중 어느 때나 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/oil-gas-bp-refinery-tank-cleaning.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">석유 · 가스에서<br>드라이아이스 세척이 활용되는 주요 작업</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">HEAVY OIL, CARBON & BITUMEN REMOVAL</span>
      <h3>중질유 · 카본 · 비투멘 제거</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/oil-gas-cleaning-heavy-carbon-buildup.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/oil-gas-dry-ice-blasting-removing-carbon-buildup.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">중질유 · 비투멘 · 파라핀 · 카본을<br>설비 구조를 보존하면서 제거합니다.</p>
      <div class="cmp-text auto-text"><p>열교환기와 펌프, 용기, 모터, 배관에는 중질유와 비투멘, 카본, 부식성 물질이 두껍게 쌓입니다. 운송 장비와 유전 설비도 마찬가지입니다. 연마 방식은 오염물과 함께 모재를 깎아내고, 용제는 유해 폐기물을 남깁니다.</p><p>드라이아이스 세척은 설비의 구조적 무결성을 보존하면서 이 침착물을 제거하는 방식으로 활용됩니다. Cold Jet은 운송 장비의 두꺼운 카본·비투멘 제거, 정유소 저장 탱크 세척, 유전 설비의 부식성 물질 제거 사례를 제시하고 있습니다. 유출물 정리와 가용성 염·염화물 제거에도 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>열교환기 · 펌프 · 용기</li><li>저장 · 생산 · 압력 탱크</li><li>배관 · 밸브 · 게이지</li><li>운송 장비 · 유전 설비</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">SURFACE PREPARATION FOR NDT & RECOATING</span>
      <h3>비파괴검사 · 재도장 전 표면 전처리</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/oil-gas-pipe-cleaning.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/oil-gas-surface-prep.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">라인을 세우지 않고 검사 · 재도장 전 표면을 준비해<br>부식을 더 자주 점검할 수 있습니다.</p>
      <div class="cmp-text auto-text"><p>파이프라인과 탱크, 용기의 비파괴검사(NDT)와 검사 전 세척, 재도장 전 전처리는 설비 유지관리(fabric maintenance) 팀의 핵심 업무입니다. 샌드블라스팅과 워터블라스팅은 미생물과 이물을 표면에 박아 넣어 도장 밀착에 영향을 줄 수 있습니다.</p><p>드라이아이스는 강 표면의 기공과 틈새에 침투해 오일과 열화 도장, 경미한 부식, 가용성 염과 염화물, 미생물을 제거하는 방식으로 활용되며, 수분이나 화학물질을 남기지 않아 세척 직후 재도장이 가능한 경우가 있습니다. 라인을 세우지 않고 작업할 수 있어 검사 주기를 짧게 하는 데 도움이 됩니다. Cold Jet은 용접 전 유황 침착물 제거 사례도 제시합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>파이프라인 · 배관 (경미한 부식)</li><li>탱크 · 용기 외면</li><li>용접 전 표면 (유황 침착물)</li><li>열화 도장 · 코팅</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">HEAT EXCHANGERS, FIN FANS & RADIATORS</span>
      <h3>열교환기 · 핀팬 · 라디에이터</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/oil-gas-hilcorp-removing-atmospheric-contamination-from-fin-fans.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/oil-gas-frac-pump-radiator.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">핀을 손상시키지 않고 열전달 표면을 세척해<br>운전 중에도 효율을 회복합니다.</p>
      <div class="cmp-text auto-text"><p>핀팬 열교환기와 HRSG 핀튜브, 프랙 펌프 트럭의 라디에이터 핀에는 수년간 분진과 대기 오염물, 오일이 쌓여 공기 흐름과 열전달을 막습니다. 얇은 핀은 고압수나 연마재에 쉽게 손상되고, 분해 세척은 시간이 많이 듭니다.</p><p>드라이아이스 세척은 핀과 모터, 베어링, 계측기를 손상시키지 않고 축적물을 제거하는 방식으로 활용되며, 시스템 조건에 따라 운전 중 세척이 가능한 경우가 있습니다. Cold Jet은 핀팬의 대기 오염물 제거, HRSG 핀튜브 세척, 프랙 펌프 라디에이터 세척 사례를 제시하고 있습니다. 물을 쓰지 않아 현장을 진흙탕으로 만들지 않는 점이 유전 작업에서 특히 평가받습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>핀팬 · 에어쿨러</li><li>HRSG 핀튜브 · 이코노마이저</li><li>프랙 펌프 트럭 라디에이터</li><li>보일러 · 응축기 · 증발기</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">ROTATING & ELECTRICAL EQUIPMENT</span>
      <h3>회전기기 · 전기설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/oil-gas-cleaning-turbine-in-oil-and-gas-.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">터빈 · 모터 · 발전기 권선과 제어반을<br>비전도성 매체로 세척합니다.</p>
      <div class="cmp-text auto-text"><p>정유소의 터빈과 압축기, 모터, 발전기 권선, 변압기, 개폐기, 전기 제어반은 물이나 전도성 매체로 세척할 수 없습니다. 가연성 환경에서 화재와 단락 위험도 고려해야 합니다.</p><p>드라이아이스는 비전도성이고 수분을 남기지 않아 회전기기와 전기설비 세척에 활용됩니다. Cold Jet은 정유소 터빈 세척 사례를 제시하며, 열교환기 핀부터 발전기 권선·회로까지 민감한 부품에 적용된다고 설명합니다. 실제 적용은 전원 상태, 방폭 구역 여부와 안전 절차를 함께 검토해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>터빈 · 압축기 (케이싱 · 스탠드)</li><li>모터 · 발전기 권선</li><li>변압기 · 개폐기 · 제어반</li><li>웰헤드 · 드릴링 장비</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">석유 · 가스 설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/oil-gas-cleaning-heavy-carbon-buildup.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>중질유 · 비투멘</b><small>HEAVY OIL & BITUMEN</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/oil-gas-dry-ice-blasting-removing-carbon-buildup.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 침착물</b><small>CARBON BUILDUP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/oil-gas-surface-prep.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>파라핀 · 타르</b><small>PARAFFIN & TAR</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/oil-gas-pipe-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>경미한 부식 · 산화물</b><small>LIGHT CORROSION</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/oil-gas-bp-refinery-tank-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>가용성 염 · 염화물</b><small>SOLUBLE SALTS & CHLORIDES</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/oil-gas-removing-sulfur-deposits-prior-to-welding.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>유황 침착물</b><small>SULFUR DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/oil-gas-hilcorp-removing-atmospheric-contamination-from-fin-fans.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>대기 오염물 · 분진</b><small>ATMOSPHERIC CONTAMINATION</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>열화 도장 · 코팅</b><small>FAILED COATINGS & PAINT</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">석유 · 가스에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성</b><p>부식성 에칭이나 산 손상, 마모를 일으키지 않아 열교환기 핀과 발전기 권선, 변압기, 배선 같은 민감한 부품에도 적용을 검토할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>수분 · 2차 폐기물 없음</b><p>물과 용제, 실리카 같은 매체를 쓰지 않고 매체가 승화하므로 회수·폐기할 것이 없습니다. 매체 잔류나 수분 손상 위험도 없습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>운전 중 · 현장 세척</b><p>설비 조건에 따라 운전 상태에서 세척할 수 있는 경우가 있어, 셧다운이나 정기보수 기간이 아니어도 연중 세척과 점검을 검토할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>비전도성 · 화재 위험 저감</b><p>전기설비 세척 시 단락과 화재 위험을 낮추고, 물이 없어 작업장이 미끄럽거나 진흙탕이 되지 않습니다. 분진 구름도 발생하지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>도장 밀착에 유리한 표면</b><p>미생물과 이물을 표면에 박아 넣지 않고 수분·화학 잔류물을 남기지 않아, 재도장·재코팅 전 전처리에 활용됩니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 플랜트 안에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>저장 탱크의 중질유·비투멘, 배관의 경미한 부식과 염분, 핀팬의 대기 오염물은 같은 사업장에서 발생하지만 오염물의 두께와 성질, 대상의 민감도, 작업 구역의 안전 등급이 서로 다릅니다.</p>
            <p>바테크는 설비의 재질과 구조, 오염물의 종류, 운전 상태와 안전 절차를 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다. 이동식 컴프레서 사용 시 애프터쿨러 등 공기 품질 확보 방안도 함께 계획합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/oil-gas-bp-refinery-tank-cleaning.webp" alt="" loading="lazy" /><b>저장 탱크 · 용기</b><small>중질유 · 비투멘</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/oil-gas-pipe-cleaning.webp" alt="" loading="lazy" /><b>배관 · 파이프라인</b><small>경미한 부식 · 염분</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/oil-gas-frac-pump-radiator.webp" alt="" loading="lazy" /><b>핀팬 · 라디에이터</b><small>대기 오염물 · 분진</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 플랜트의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">오일 · 가스에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">석유 · 가스 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/rust-corrosion-removal.html"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>RUST, CORROSION & OXIDATION REMOVAL</small><b>녹 · 부식 · 산화물 제거</b><span>표면 녹과 느슨한 산화물(비마모 범위 내)</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">오일 · 가스과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">열교환기·터빈·회전기기 유지보수는 발전 · 전력과, 중장비와 전기설비 세척은 광업과 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/power-generation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></span><small>POWER GENERATION</small><b>발전 · 전력</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/mining.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /></span><small>MINING</small><b>광업</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN OIL & GAS OPERATIONS</span>
      <h2 class="cmp-h2">글로벌 석유 · 가스 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">유전 서비스와 정유 기업이 설비 세척과 표면 전처리에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 오일 · 가스 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:70%"><img src="../assets/img/oil-gas-halliburton.webp" alt="Halliburton" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:72%"><img src="../assets/img/oil-gas-weatherford.webp" alt="Weatherford" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:66%"><img src="../assets/img/oil-gas-imperial_oil.svg_.webp" alt="Imperial Oil" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:66%"><img src="../assets/img/oil-gas-wellbore.webp" alt="NOV Wellbore" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:88%"><img src="../assets/img/oil-gas-sharp-oil-field-services-logo.webp" alt="Sharp Oil Field Services" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:62%"><img src="../assets/img/oil-gas-emory-dry-ice.webp" alt="Emory Dry Ice" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 플랜트 설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 플랜트 설비라도 재질과 구조, 오염물의 종류와 두께, 운전 상태와 작업 구역의 안전 절차에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 플랜트의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

MINING_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/mining/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-mining.png" alt="광업 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 광업</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">MINING</span>
      <h1>광업</h1>
      <p class="cmp-hero-p auto-hero-lead">분진과 그리스, 물이 부식을 부르는 환경 — 광산 설비 세척에는 다른 접근이 필요합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">MINING & MINERAL PROCESSING</span>
      <h2 class="cmp-h2">물을 쓰면 부식이 빨라지고,<br>연마재를 쓰면 설비가 닳습니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>광산과 선광·처리 현장에는 크러셔와 밀, 드레지, 스크린과 컨베이어, 링기어·압축기·펌프 같은 처리 설비, 덤프트럭과 로더 같은 운반 장비, 그리고 E-하우스·변압기·개폐기·고정자 권선·제어반 같은 전기설비가 운영됩니다.</p>
      <p>이 설비에는 두꺼운 그리스와 석탄분진, 오일, 비투멘, 카본 침착물, 광물 스케일, 광석 잔류물이 쌓입니다. 전기설비에 쌓인 전도성 분진은 과열과 아크, 조기 고장의 원인이 되고, 가연성 축적물은 화재 위험을 높입니다.</p>
      <p>기존 방식인 수작업 세척과 고압수, 화학 용제는 전기설비를 손상시키고 부식을 촉진하며 작업자 안전 문제를 만들고 설비를 오랫동안 세웁니다. 특히 소금·칼륨(포타시) 광산처럼 물이 산화를 가속하는 환경에서는 물 세척 자체가 어렵습니다.</p>
      <p class="auto-intro-close">따라서 광업에서의 세척은 <b>수분 없이, 전기설비를 손상시키지 않고, 설비를 오래 세우지 않으면서 두꺼운 오염을 제거할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/mining-dry-ice-blasting-removing-contaminants-in-salt-mine.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">광업에서<br>드라이아이스 세척이 활용되는 주요 설비</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">EXTRACTION & PROCESSING EQUIPMENT</span>
      <h3>채광 · 처리 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mining-cleaning-chains-and-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/mining-dry-ice-blasting-removing-contaminants-in-salt-mine.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">크러셔 · 컨베이어 · 링기어 · 펌프의 두꺼운 오염을<br>장착 상태에서 제거합니다.</p>
      <div class="cmp-text auto-text"><p>크러셔와 드레지, 밀, 스크린, 컨베이어와 체인에는 그리스와 광석 잔류물, 광물 스케일이 두껍게 쌓이고, 링기어·압축기·펌프·블리더·하이드라 슬라이드는 분해 세척에 많은 시간이 듭니다.</p><p>드라이아이스 세척은 이 설비를 분해하지 않고 장착 상태에서 세척하는 방식으로 활용되며, 비마모성이어서 베어링과 씰, 센서를 닳게 하지 않습니다. Cold Jet은 광산 서비스 업체가 설비 무결성을 유지하면서 처리 시간을 크게 개선한 사례와, 소금 광산에서의 오염물 제거 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>크러셔 · 밀 · 드레지</li><li>컨베이어 · 체인 · 스크린</li><li>링기어 · 압축기</li><li>펌프 · 블리더 · 하이드라 슬라이드</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">HAUL TRUCKS & TRANSPORT VEHICLES</span>
      <h3>덤프트럭 · 로더 · 운반 장비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">섀시 · 엔진 · 유압 시스템의 광석과 그리스를<br>하부까지 제거합니다.</p>
      <div class="cmp-text auto-text"><p>광산 덤프트럭과 로더, 운반 차량에는 광석과 그리스, 환경 잔해가 두껍게 쌓입니다. 하부 구조와 기계 조립체는 수작업으로 접근하기 어렵고, 축적물을 제거하지 않으면 정비 주기와 신뢰성에 영향을 줍니다.</p><p>드라이아이스 세척은 차량 섀시와 엔진, 유압 시스템의 축적물을 제거하는 방식으로 활용되며, 수작업으로 닿기 어려운 하부와 조립체에 접근할 수 있습니다. Cold Jet은 축적물 제거가 정비 간격과 신뢰성 개선, 그리고 도로 운송 시 안전 요건 충족에도 도움이 된다고 설명합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>덤프트럭 · 로더</li><li>섀시 · 하부 구조</li><li>엔진 · 유압 시스템</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">ELECTRICAL SYSTEMS & FACILITY INFRASTRUCTURE</span>
      <h3>전기설비 · 시설 인프라</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mining-cleaning-control-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">E-하우스 · 변압기 · 고정자 권선의 전도성 분진을<br>물과 화학약품 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>E-하우스와 전기실, 변압기, 개폐기, 고정자 권선, 애자, 제어반에는 석탄분진과 광물 분진 같은 전도성 분진이 쌓여 과열과 아크, 절연 손상, 조기 고장을 일으킵니다. 윤활유실과 정비 베이, 저장 탱크, 핀팬도 정기 세척이 필요합니다.</p><p>드라이아이스는 비전도성이고 수분을 남기지 않아 변압기와 개폐기, 고정자 권선, 민감한 제어 시스템의 전도성 분진 제거에 활용됩니다. Cold Jet은 이런 세척이 전기 고장과 계획되지 않은 정지를 줄이는 데 도움이 된다고 설명합니다. 실제 적용은 전원 상태와 안전 절차를 함께 검토해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>E-하우스 · 전기실 · 제어반</li><li>발전기 · 변압기 · 개폐기</li><li>고정자 권선 · 애자</li><li>윤활유실 · 정비 베이 · 저장 탱크 · 핀팬</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">광산 설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/mining-cleaning-chains-and-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>두꺼운 그리스 · 오일</b><small>HEAVY GREASE & OIL</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/mining-cleaning-control-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>석탄분진 · 전도성 분진</b><small>COAL & CONDUCTIVE DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>비투멘 · 카본 침착물</b><small>BITUMEN & CARBON DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/mining-dry-ice-blasting-removing-contaminants-in-salt-mine.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>광물 스케일 · 염분</b><small>MINERAL SCALE & SALT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>광석 잔류물 · 환경 잔해</b><small>ORE RESIDUE & DEBRIS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>산화물 · 부식</b><small>OXIDATION & CORROSION</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">광업에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비전도성</b><p>고전압 시스템과 전동기, 개폐기, 발전기, 제어실을 단락이나 절연 손상 위험 없이 세척하는 방식으로 활용됩니다. 활선 여부와 안전 절차는 별도로 확인해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>수분 없는 건식 세척</b><p>소금·포타시·광물 채광처럼 물이 산화를 가속하는 환경에서 수분을 남기지 않는 세척 방법 중 하나입니다. 폐수와 폐매체도 발생하지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>비마모성</b><p>베어링과 씰, 센서, 게이지, 정밀 계측기를 닳게 하지 않고 표면의 질감이나 공구를 마모시키지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>장착 상태 세척 · 정지시간 단축</b><p>설비를 분해하지 않고 세척할 수 있는 경우 세척 후 바로 복귀할 수 있습니다. Cold Jet은 수작업 대비 세척 시간을 절반 이상 줄인 사례를 인용합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>작업자 · 화재 안전</b><p>유해 용제 노출을 줄이고, 설비의 가연성 축적물을 제거해 화재 위험을 낮추는 데 도움이 됩니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 광산 안에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>컨베이어 체인의 두꺼운 그리스, 제어반의 전도성 분진, 소금 광산 설비의 염분과 스케일은 같은 현장에서 발생하지만 오염물의 두께와 성질, 대상의 민감도, 부식 환경이 서로 다릅니다.</p>
            <p>바테크는 설비의 재질과 구조, 오염물의 종류, 운전 상태와 안전 절차, 현장의 압축공기 확보 방안(디젤 컴프레서 등)을 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/mining-cleaning-chains-and-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>컨베이어 · 체인</b><small>두꺼운 그리스 · 광석 잔류물</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/mining-cleaning-control-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>제어반 · 전기설비</b><small>전도성 분진</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/mining-dry-ice-blasting-removing-contaminants-in-salt-mine.webp" alt="" loading="lazy" /><b>소금 광산 설비</b><small>염분 · 광물 스케일</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 현장의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">광업에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">광업 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/rust-corrosion-removal.html"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>RUST, CORROSION & OXIDATION REMOVAL</small><b>녹 · 부식 · 산화물 제거</b><span>표면 녹과 느슨한 산화물(비마모 범위 내)</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">광업과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">대형 전기설비와 회전기기 유지보수는 발전 · 전력과, 중장비와 플랜트 설비 세척은 석유 · 가스와 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/power-generation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></span><small>POWER GENERATION</small><b>발전 · 전력</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/oil-gas.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-oilgas.png" alt="" loading="lazy" /></span><small>OIL & GAS</small><b>오일 · 가스</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN MINING OPERATIONS</span>
      <h2 class="cmp-h2">글로벌 광산 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">글로벌 광산 기업이 채광·처리 설비와 전기설비 유지보수에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 광업 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:66%"><img src="../assets/img/mining-rio_tinto_logo.webp" alt="Rio Tinto" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:66%"><img src="../assets/img/mining-barrick-gold-logo.webp" alt="Barrick Gold" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:74%"><img src="../assets/img/mining-freeport_mcmoran_logo.webp" alt="Freeport-McMoRan" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:72%"><img src="../assets/img/mining-sibanye-stillwater-logo.webp" alt="Sibanye-Stillwater" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:70%"><img src="../assets/img/mining-peabody_energy_logo.webp" alt="Peabody Energy" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:62%"><img src="../assets/img/mining-new_gold_inc__logo.webp" alt="New Gold" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 광산 설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 광산 설비라도 재질과 구조, 오염물의 종류와 두께, 운전 상태와 부식 환경, 안전 절차에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 광산 설비의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

TEXTILES_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/textiles/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-textile.png" alt="섬유 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 섬유</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">TEXTILES</span>
      <h1>섬유</h1>
      <p class="cmp-hero-p auto-hero-lead">설비에 남은 섬유 잔사와 접착제는 그대로 다음 원단의 결점이 됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">TEXTILES & NONWOVENS</span>
      <h2 class="cmp-h2">섬세한 롤러를 긁지 않고,<br>운전 온도에서 잔사를 걷어내야 합니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>섬유·부직포·기술섬유 공장에는 카딩기와 금속 침포, 방적기, 직기의 리드·헤들, 텐터(스텐터) 프레임과 체인·클립, 염색 롤러, 건조·큐어링 오븐, 라텍스 분사 설비, 접착제 도포기, 라미네이팅 롤러, 와이어 랩 정밀 롤러 같은 설비가 운영됩니다.</p>
      <p>이 설비에는 섬유 날림(플라이)과 분진, 왁스와 그리스, 라텍스와 접착제, 염료, 경화된 수지와 폴리머, 탄화 잔류물이 쌓입니다. 카딩기와 직기에 남은 플라이와 왁스는 오염성 B급 원단과 규격외품의 주요 원인이 되고, 롤러의 라텍스 축적은 원단 품질에 직접 영향을 줍니다.</p>
      <p>기존 방식인 스크레이퍼와 용제(MEK 등), 연마재, 물 세척은 리드와 헤들 깊숙이 닿지 못하거나, 와이어 랩 롤러를 손상시켜 재권선 비용을 발생시키고, 오븐 세척 시 냉각과 물 세척으로 전자 센서·제어반을 위험에 노출시킵니다.</p>
      <p class="auto-intro-close">따라서 섬유에서의 세척은 <b>섬세한 표면을 마모시키지 않고, 물과 용제 없이, 운전 온도에서 분해 없이 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/textiles-removing-fiber-buildup-from-a-wire-wrapped-roller-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">섬유 생산에서<br>드라이아이스 세척이 활용되는 주요 설비</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">FIBER PREPARATION & WEAVING</span>
      <h3>섬유 준비 · 제직 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/textiles-dry-ice-cleaning-of-metallic-card-clothing.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">카딩기 · 방적기 · 직기의 플라이와 왁스를<br>깊숙한 곳까지 제거합니다.</p>
      <div class="cmp-text auto-text"><p>카딩기의 금속 침포, 방적기, 직기의 리드와 헤들, 보빈에는 섬유 플라이와 분진, 왁스, 그리스가 쌓입니다. 이 잔사는 오염 관련 규격외품과 B급 원단의 주요 원인이며, 고속 제직 라인에서 스크레이퍼와 용제로는 깊은 부위까지 닿지 않아 결점이 반복됩니다.</p><p>드라이아이스 세척은 물이나 번오프(연소 제거) 없이 축적된 플라이·분진·그리스를 제거하는 방식으로 활용됩니다. Cold Jet은 기계 부품의 정밀도를 유지하면서 세척 정지시간을 절반 수준으로 줄인 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>카딩기 · 금속 침포</li><li>방적기</li><li>직기 · 리드 · 헤들 · 보빈</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">CONVEYANCE & ROLLER MAINTENANCE</span>
      <h3>와이어 롤러 · 텐터 체인 · 컨베이어</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/textiles-removing-fiber-buildup-from-a-wire-wrapped-roller-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/textiles-removing-hardened-dye-and-fiber-fly-from-conveyor-slats-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">와이어 랩 롤러의 라텍스 · 접착제를<br>재권선 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>와이어 랩 롤러와 텐터 체인, 클립에는 라텍스와 접착제가 쌓이고, 컨베이어 슬랫에는 경화된 염료와 섬유 플라이가 굳습니다. 스크레이퍼 같은 연마 방식은 와이어 랩을 손상시켜 롤러당 재권선 비용을 발생시키기 때문에, 기술섬유 공장에서는 세척으로 인한 손상 비용이 크게 문제됩니다.</p><p>드라이아이스는 비마모성이어서 와이어 랩과 클립, 금속 침포 같은 정밀 부품을 표면 마모 없이 세척하는 방식으로 활용됩니다. Cold Jet은 롤러·컨베이어 세척을 30분 수준으로 마친 사례와, 연마 세척으로 발생하던 롤러 재권선 비용을 없앤 사례를 제시하며, 이런 조건이 예방 정비 프로그램을 가능하게 한다고 설명합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>와이어 랩 · 정밀 롤러</li><li>텐터 · 스텐터 체인 · 클립</li><li>컨베이어 · 트로프 · 슬랫</li><li>라미네이팅 롤러 · 슬리터 · 닥터 블레이드</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">FINISHING, COATING & STENTER OVENS</span>
      <h3>가공 · 코팅 · 스텐터 오븐</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/ind-card-textile.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">경화 수지 · 폴리머 · 염료를<br>운전 온도에서 분해 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>가공 부서의 스텐터 프레임과 건조·큐어링 오븐, 라텍스 분사 설비, 코팅 헤드에는 경화된 수지와 폴리머, 염료, 오버스프레이, 탄화 잔류물이 쌓입니다. 이 "고온 구역" 세척은 전통적으로 냉각과 물 세척을 위한 전체 정지가 필요했고, 물은 전자 센서와 제어반을 손상시킬 위험이 있었습니다.</p><p>드라이아이스 세척은 운전 온도에서 분해 없이 오버스프레이와 탄화 잔류물을 제거하는 방식으로 활용되어, 장기 정지 대신 계획된 휴식 시간에 정비하는 것을 검토할 수 있습니다. 작업 환경이 건조하게 유지되어 센서·제어반 세척에도 적용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>텐터 · 스텐터 프레임</li><li>건조 · 큐어링 오븐</li><li>염색 롤러 · 염료조</li><li>라텍스 분사 · 접착제 도포 설비</li><li>컨버팅 설비</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">섬유 생산설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/textiles-dry-ice-cleaning-of-metallic-card-clothing.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>섬유 플라이 · 분진</b><small>FIBER FLY & DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>왁스 · 그리스</b><small>WAX & GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/textiles-removing-fiber-buildup-from-a-wire-wrapped-roller-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>라텍스 · 접착제</b><small>LATEX & ADHESIVES</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/textiles-removing-hardened-dye-and-fiber-fly-from-conveyor-slats-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>경화된 염료</b><small>HARDENED DYES</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>경화 수지 · 폴리머</b><small>RESINS & POLYMERS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/ind-card-textile.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄화 잔류물 · 오버스프레이</b><small>CARBONIZED RESIDUE</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">섬유 생산에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성</b><p>와이어 랩 롤러와 텐터 클립, 금속 침포 같은 정밀 부품을 표면 마모 없이 세척합니다. 연마 세척으로 발생하던 재권선·수리 비용을 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>물 · 용제 없는 건식 세척</b><p>MEK 같은 유해 용제와 물을 쓰지 않아 작업자 노출을 줄이고, 전자 센서와 제어반이 있는 설비도 건조한 상태로 세척할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>운전 온도 · 장착 상태 세척</b><p>스텐터 오븐과 건조 설비를 냉각·분해 없이 운전 온도에서 세척할 수 있는 경우 정지시간을 크게 줄일 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>품질 결점 감소</b><p>플라이·왁스·접착제 잔사를 더 자주, 더 깊이 제거함으로써 오염 관련 결점과 B급 원단을 줄이는 데 도움이 됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>세척 시간 · 인력 절감</b><p>Cold Jet은 5시간 걸리던 설비 세척을 15분으로, 3명·4시간 롤러 세척을 1명·1시간으로 줄인 사례를 제시하고 있습니다. 실제 결과는 설비와 오염 상태에 따라 다릅니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 섬유 공장 안에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>카딩기 침포의 플라이, 와이어 롤러의 라텍스, 스텐터 오븐의 경화 수지는 같은 공장에서 발생하지만 표면의 민감도와 오염물의 성질, 세척 시점의 온도가 서로 다릅니다.</p>
            <p>바테크는 설비의 표면 상태와 오염물의 종류, 운전 온도와 정지 가능 시간을 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/textiles-dry-ice-cleaning-of-metallic-card-clothing.webp" alt="" loading="lazy" /><b>금속 침포 · 카딩기</b><small>섬유 플라이 · 왁스</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/textiles-removing-fiber-buildup-from-a-wire-wrapped-roller-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>와이어 랩 롤러</b><small>라텍스 · 접착제</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/textiles-removing-hardened-dye-and-fiber-fly-from-conveyor-slats-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><b>컨베이어 슬랫</b><small>경화 염료 · 플라이</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 설비의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">섬유에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">섬유 생산 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">섬유과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">롤러와 접착제 도포 설비 세척은 포장 · 인쇄와, 부직포 위생재 생산은 의료기기와 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/printing.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /></span><small>PRINTING</small><b>인쇄</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/medical.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></span><small>MEDICAL DEVICE MANUFACTURING</small><b>의료기기 제조</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN TEXTILE MANUFACTURING</span>
      <h2 class="cmp-h2">글로벌 섬유 생산 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">섬유·부직포·기술섬유 제조사가 롤러와 생산설비 유지보수에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 섬유 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:70%"><img src="../assets/img/textiles-milliken_and_company_logo.webp" alt="Milliken" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:66%"><img src="../assets/img/textiles-shaw_industries_logo.webp" alt="Shaw Industries" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:62%"><img src="../assets/img/textiles-wlgore_logo.webp" alt="W. L. Gore" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:72%"><img src="../assets/img/textiles-logo-kimberly-clark.webp" alt="Kimberly-Clark" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:62%"><img src="../assets/img/plastics-composites-berry-logo.webp" alt="Berry Global" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:66%"><img src="../assets/img/textiles-medline-logo.webp" alt="Medline" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:60%"><img src="../assets/img/textiles-lacoste-logo.webp" alt="Lacoste" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 섬유 설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 섬유 설비라도 롤러 표면의 종류, 오염물의 성질과 경화 정도, 운전 온도와 정지 가능 시간에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 섬유 설비의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

ENGINEERED_WOOD_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/engineered-wood/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-wood.png" alt="엔지니어드 우드 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 엔지니어드 우드</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">ENGINEERED WOOD</span>
      <h1>엔지니어드 우드</h1>
      <p class="cmp-hero-p auto-hero-lead">피치와 수지, 미세 목분의 축적은 품질 문제이기 전에 화재 위험입니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">ENGINEERED WOOD · MDF · OSB · PLYWOOD</span>
      <h2 class="cmp-h2">뜨거운 프레스를 식히지 않고,<br>물 없이 세척해야 합니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>MDF·HDF·파티클보드·OSB와 합판 공장에는 열간 프레스와 프레스 플레이트, 프리프레스 벨트, 리파이너 플레이트, 드라이어와 환기 블레이드, 접착제·수지 도포 시스템, 샌딩 벨트, 합판의 주철 알루미늄 킬른 팬, 생산 롤러·실린더, 필러·레이스, 베니어 드라이어 같은 설비가 운영됩니다.</p>
      <p>이 설비에는 접착 수지와 피치, 파인 타르, 목섬유와 미세 목분, 응축 수지와 왁스, 열처리 부산물, 오일이 쌓입니다. 이 축적물은 가연성 조건을 만들어 화재 위험이 되고, 킬른 팬의 불균형을 일으켜 베어링·샤프트·모터 수명을 줄이며, 보드 표면 결점과 라인 정지로 이어집니다.</p>
      <p>기존 방식인 물 스크레이핑과 화학약품, 와이어 브러시, 앵글 그라인더, 니들건, 파워 치즐은 작업자 4명 이상이 여러 시간 밀폐 공간에서 뜨거운 잔류물과 분진에 노출되어야 하고, 정밀 표면을 마모시키며, 물은 목재의 팽윤과 목분 슬러리·생물 성장 문제를 만듭니다.</p>
      <p class="auto-intro-close">따라서 엔지니어드 우드에서의 세척은 <b>물 없이, 운전 온도에서 분해하지 않고, 정밀 표면을 마모시키지 않으면서 가연성 축적물을 제거할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/engineered-wood-dry-ice-blasting-cleaning-press-plates.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">엔지니어드 우드 생산에서<br>드라이아이스 세척이 활용되는 주요 설비</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PRESS & PLATE CLEANING</span>
      <h3>프레스 · 프레스 플레이트</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/engineered-wood-dry-ice-blasting-cleaning-press-plates.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/engineered-wood-dry-ice-blasting-cleaning-strand-orientation-equipmente.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">접착 수지 · 피치 · 목섬유가 쌓인 프레스를<br>뜨거운 상태에서 장착된 채 세척합니다.</p>
      <div class="cmp-text auto-text"><p>MDF·HDF와 OSB 생산에서 가장 흔한 세척 대상은 금속 프레스와 프레스 플레이트입니다. 접착 수지와 피치, 목섬유, 열처리 부산물이 쌓이며, 전통적으로 작업자 4명이 여러 시간 수작업으로 긁어내야 했습니다. 앵글 그라인더는 프레스 정밀도를 손상시킵니다.</p><p>드라이아이스 세척은 생산 사이클 직후 프레스 플레이트를 뜨거운 상태에서 장착된 채 세척하는 방식으로 활용되어, 작업자가 위험 구역에 머무는 시간을 줄입니다. Cold Jet은 이 작업을 작업자 1명, 최대 1시간 수준으로 줄인 사례를 제시하며, OSB 프레스와 스트랜드 배향 설비도 같은 방식으로 축적물을 관리해 보드 품질에 도움이 된다고 설명합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>금속 프레스 · 프레스 플레이트 · 플래튼</li><li>프리프레스 벨트 · 리파이너 플레이트</li><li>OSB 프레스 · 스트랜드 배향 설비</li><li>열처리 설비 · 생산 라인 툴링</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">DRYER & VENTILATION SYSTEMS</span>
      <h3>드라이어 · 환기 시스템</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/engineered-wood-removing-adhesive-from-veneer-dryer-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">응축 수지 · 왁스 · 미세 목분을 제거해<br>화재 위험과 효율 저하를 줄입니다.</p>
      <div class="cmp-text auto-text"><p>드라이어 부품과 환기 블레이드, 베니어 드라이어, 습식 스크러버, 피치로 막힌 증기 코일에는 응축 수지와 왁스, 미세 목분이 쌓입니다. 이 축적물은 화재 위험을 만들고 설비 효율을 떨어뜨리며, 수작업으로는 닿기 어려운 곳에 있습니다.</p><p>드라이아이스 세척은 분해 없이 장착 상태에서 이 축적물을 제거하는 방식으로 활용되어, 장기 정지 없이 생산 일정을 유지하면서 수작업이 닿지 못하는 부위까지 접근할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>드라이어 부품 · 베니어 드라이어</li><li>환기 블레이드 · 환기 시스템</li><li>습식 스크러버 · 증기 코일</li><li>금속 와이어 · 에어 라인</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">GLUE APPLICATORS & PRODUCTION COMPONENTS</span>
      <h3>접착제 도포기 · 생산 부품</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/engineered-wood-adhesive-and-resin-buildup-removed-from-production-surfaces-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">접착 수지를 열충격으로 취성화시켜<br>벨트와 툴링을 손상시키지 않고 제거합니다.</p>
      <div class="cmp-text auto-text"><p>접착제 도포기와 수지 도포 시스템, 글루 스프레더 롤, 샌딩 벨트, 핑거 조인트 블레이드 홀더의 접착 수지 축적은 제품 품질에 직접 영향을 주고 생산 정지를 일으킵니다. 화학 용제는 폐기물을 만들고, 기계적 제거는 벨트와 툴링을 손상시킵니다.</p><p>드라이아이스의 극저온은 끈적한 수지를 취성화시켜 갈라지게 하고, 이를 들어내는 방식으로 제거합니다. Cold Jet은 주요 제조사가 설비·툴링·벨트를 손상시키지 않고 기존 방식보다 나은 세척 결과를 얻었다고 보고한 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>접착제 도포기 · 수지 도포 시스템</li><li>글루 스프레더 롤</li><li>샌딩 벨트</li><li>핑거 조인트 블레이드 홀더 · 컨베이어</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">KILN FANS, ROLLERS & VENEER EQUIPMENT</span>
      <h3>합판 킬른 팬 · 롤러 · 베니어 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/engineered-wood-kiln-fan-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/engineered-wood-cleaning-production-rollers-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">킬른 팬을 떼지 않고 세척해<br>재설치 불균형을 피합니다.</p>
      <div class="cmp-text auto-text"><p>합판 공장의 주철 알루미늄 킬른 팬에는 운전 중 피치와 파인 타르가 쌓여 위험한 조건을 만듭니다. 팬을 떼어 수작업 세척하면 재설치 시 불균형이 생겨 베어링·샤프트·모터 수명이 줄어듭니다. 생산 롤러와 실린더, 필러·레이스, 베니어 설비에도 두꺼운 피치와 목재 잔류물이 쌓입니다.</p><p>드라이아이스 세척은 팬을 장착된 채 세척해 블레이드의 공기역학적 형상을 회복하면서 공장 밸런스를 유지하는 방식으로 활용됩니다. Cold Jet은 주요 합판 제조사가 킬른 팬 세척을 수 시간에서 10분 이내로 줄인 사례를 제시하고 있으며, 롤러·실린더 세척은 고압수 대비 2차 폐기물 없이 접근성이 좋았다고 보고합니다. 물을 쓰지 않아 베니어의 뒤틀림 위험도 없습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>주철 알루미늄 킬른 팬</li><li>생산 롤러 · 실린더</li><li>필러 · 레이스 · 베니어 설비</li><li>열간 프레스 플래튼 · 티플 · 트레이</li><li>베어링 · 샤프트 · 모터</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">엔지니어드 우드 설비에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/engineered-wood-adhesive-and-resin-buildup-removed-from-production-surfaces-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착 수지 · 글루</b><small>ADHESIVE RESIN & GLUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/engineered-wood-kiln-fan-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>피치</b><small>PITCH</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/engineered-wood-cleaning-production-rollers-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>파인 타르</b><small>PINE TAR</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/engineered-wood-dry-ice-blasting-cleaning-press-plates.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>목섬유 · 목재 잔류물</b><small>WOOD FIBER & PULP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/engineered-wood-dry-ice-blasting-cleaning-strand-orientation-equipmente.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>미세 목분</b><small>FINE WOOD DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/engineered-wood-removing-adhesive-from-veneer-dryer-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>응축 수지 · 왁스</b><small>CONDENSED RESIN & WAX</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>열처리 부산물 · 오일</b><small>HEAT-TREATMENT DERIVATIVES & OIL</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">엔지니어드 우드 생산에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why is-6">
    <li class="reveal" style="--reveal-delay:0.00s"><b>화재 위험 저감</b><p>피치·파인 타르·미세 목분·수지 같은 가연성 축적물을 제거하고, 매체가 승화해 인화성 잔류물을 남기지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>열간 · 장착 상태 세척</b><p>프레스와 킬른, 롤러를 운전 온도에서 분해 없이 세척할 수 있는 경우 냉각·분해·재조립 시간을 줄이고 더 자주 세척할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>물 · 2차 폐기물 없음</b><p>목재의 팽윤·뒤틀림, 목분 슬러리와 생물 성장 문제가 없고 폐수·화학약품·그릿 처리도 필요 없습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>비마모성</b><p>프레스 플레이트의 정밀도, 베어링·샤프트·모터, 라미네이트 벨트, 공압 호스와 배선, 전자 부품을 마모시키지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>작업자 안전</b><p>밀폐 공간에서 뜨거운 잔류물과 분진 곁에서 긁어내는 시간을 줄이고, 화학 용제 노출과 그라인더·치즐 사용을 없앱니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.45s"><b>세척 시간 · 인력 절감</b><p>Cold Jet은 여러 시간 걸리던 작업을 수 분~1시간으로, 작업자 4명을 1명으로 줄인 사례를 제시하고 있습니다. 실제 결과는 설비와 오염 상태에 따라 다릅니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 보드 공장 안에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>프레스 플레이트의 접착 수지, 킬른 팬의 피치·파인 타르, 샌딩 벨트와 센서의 미세 목분은 같은 공장에서 발생하지만 오염물의 두께와 경화 정도, 대상의 민감도, 세척 시점의 온도가 서로 다릅니다.</p>
            <p>바테크는 설비의 재질과 정밀도, 오염물의 종류, 운전 온도와 정지 가능 시간을 확인한 뒤 실제 테스트를 통해 3mm 펠렛부터 0.3mm 마이크로 입자까지 적합한 조건을 검토합니다. 깊은 프레스 내부용 노즐 연장과 협소부용 각도 노즐도 함께 계획합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/engineered-wood-dry-ice-blasting-cleaning-press-plates.webp" alt="" loading="lazy" /><b>프레스 플레이트</b><small>접착 수지 · 목섬유</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/engineered-wood-kiln-fan-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>킬른 팬</b><small>피치 · 파인 타르</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/engineered-wood-removing-adhesive-from-veneer-dryer-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><b>베니어 드라이어</b><small>접착제 · 응축 수지</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 설비의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">엔지니어드 우드에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">엔지니어드 우드 생산 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/mold-tool-cleaning.html"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>MOLD & TOOL CLEANING</small><b>금형 · 툴링 세척</b><span>이형제·수지·고무 잔사가 쌓이는 사출·고무·복합재 금형</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">엔지니어드 우드과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">접착제 도포 설비와 롤러 세척은 포장과, 열간 프레스·플레이트 세척은 플라스틱 · 복합소재와 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN ENGINEERED WOOD PLANTS</span>
      <h2 class="cmp-h2">글로벌 목재 보드 · 합판 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">MDF·OSB·합판 제조사가 프레스와 킬른, 생산설비 유지보수에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 엔지니어드 우드 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:74%"><img src="../assets/img/engineered-wood-weyerhaeuser-logo.webp" alt="Weyerhaeuser" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:70%"><img src="../assets/img/engineered-wood-georgia-pacific_logo.webp" alt="Georgia-Pacific" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:70%"><img src="../assets/img/engineered-wood-boise_cascade_logo.webp" alt="Boise Cascade" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:50%"><img src="../assets/img/engineered-wood-lp-logo.webp" alt="LP" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:66%"><img src="../assets/img/engineered-wood-west-fraser-logo.webp" alt="West Fraser" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:70%"><img src="../assets/img/engineered-wood-kronospan-logo.webp" alt="Kronospan" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:64%"><img src="../assets/img/engineered-wood-logo-arauco.webp" alt="Arauco" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:66%"><img src="../assets/img/engineered-wood-huber-engineered-woods-logo.webp" alt="Huber Engineered Woods" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 보드 · 합판 설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 보드 설비라도 재질과 정밀도, 오염물의 종류와 경화 정도, 운전 온도와 정지 가능 시간에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 보드 · 합판 설비의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

RAIL_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/rail-transportation/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/ind-card-transit.png" alt="철도 · 대중교통 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 철도 · 대중교통</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">RAIL & PUBLIC TRANSPORTATION</span>
      <h1>철도 · 대중교통</h1>
      <p class="cmp-hero-p auto-hero-lead">차량 정비의 세척은 체류시간을 줄이는 일이자, 전기계통 고장을 예방하는 일입니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">PASSENGER RAIL · PUBLIC TRANSIT · FREIGHT RAIL</span>
      <h2 class="cmp-h2">물은 플래시 러스트를 만들고,<br>전기계통에는 쓸 수 없습니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>여객철도·도시철도 운영기관과 화물철도·기관차 정비시설에는 견인전동기와 전기 캐비닛, 개폐기, 발전기·교류발전기, 제3궤조 애자, 캠 컨트롤러 박스, 브레이크 컨트롤러·액추에이터, 팬터그래프, 대차와 윤축, 차축·베어링, 디젤 엔진 블록, 냉각팬·라디에이터, 그리고 역사와 선로·분기기, 도장부스 같은 정비 대상이 있습니다.</p>
      <p>이 설비에는 그리스와 브레이크 분진, 탄소 분진, 접착제, 산화 잔류물, 오일 미스트, 도료, 압착된 유기물, 아스팔트, 껌과 그래픽 데칼이 쌓입니다. 애자와 전기 인프라에 쌓인 전도성 브레이크 분진은 전기가 접지로 튀는 경로가 되어 화재나 정전을 일으키고, 견인전동기의 탄소 분진과 그리스는 접지 문제·과열·전력 누설의 원인이 됩니다.</p>
      <p>기존 방식인 수작업 스크레이핑과 화학 용제, 고압수는 민감한 전기 부품을 손상시키고, 금속 표면에 즉시 플래시 러스트를 만들며, 토치와 용제로 작업자 위험을 만들고, 차량을 오랫동안 운행에서 빼야 합니다.</p>
      <p class="auto-intro-close">따라서 철도 · 대중교통에서의 세척은 <b>전기계통을 손상시키지 않고, 수분과 플래시 러스트 없이, 정비 체류시간 안에 세척할 수 있는가</b>의 문제입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/rail-cleaning-undercarriage-of-passenger-rail-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY APPLICATIONS</span>
    <h2 class="cmp-h2">철도 · 대중교통에서<br>드라이아이스 세척이 활용되는 주요 설비</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PROPULSION & ELECTRICAL SYSTEMS</span>
      <h3>추진 · 전기계통</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rail-cleaning-undercarriage-of-passenger-rail-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">견인전동기 · 제어반 · 제3궤조 애자의<br>탄소 분진과 그리스를 수분 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>견인전동기와 전기 캐비닛, 개폐기, 발전기·교류발전기, 제3궤조 애자, 캠 컨트롤러 박스에는 탄소 분진과 그리스, 산화 잔류물이 쌓여 접지 문제와 과열, 전력 누설을 일으킵니다. 물 세척은 건조 시간이 필요하고 단락 위험이 있습니다.</p><p>드라이아이스는 비전도성이고 승화 후 잔류물을 남기지 않아 고전압·민감 전기설비 세척에 활용됩니다. Cold Jet은 한 대형 운영기관이 적용 범위가 늘어나며 장비를 1대에서 7대 이상으로 확대했고, 고가의 반도체 컨트롤러 박스 교체를 피하며 재조립당 10~15인일의 노동을 줄인 사례를 제시하고 있습니다. 실제 적용은 전원 상태와 안전 절차를 함께 검토해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>견인전동기</li><li>전기 캐비닛 · 개폐기</li><li>발전기 · 교류발전기</li><li>제3궤조 애자 · 캠 컨트롤러 박스</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">TRANSIT INFRASTRUCTURE & PASSENGER AREAS</span>
      <h3>역사 · 선로 인프라 · 객실</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rail-removing-residue-and-grime-from-interior-of-subway-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/rail-removing-paint-from-exterior-panel-of-subway-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">선로 · 분기기 · 애자의 전도성 분진과<br>역사 · 객실의 오염을 화학약품 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>선로에는 차륜 미끄러짐을 일으키는 압착 유기물이, 분기기에는 그리스와 이물이 쌓입니다. 궤도 애자와 전기 인프라의 전도성 금속 브레이크 분진은 방치하면 화재나 정전으로 이어집니다. 차량 외판과 역사 벽, 터널의 그을음과 브레이크 분진, 승강장 바닥의 껌, 데칼과 차량 그래픽의 접착제, HVAC 코일도 정기 세척 대상입니다.</p><p>드라이아이스 세척은 모재 손상 없이 이 오염물을 제거하는 방식으로 활용되며, 물과 화학약품이 없어 공공 인프라를 뒷정리 부담 없이 세척할 수 있습니다. Cold Jet은 지하철 객실 내부의 잔류물·때 제거와 외판 도료 제거 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>선로 · 분기기 · 궤도 애자</li><li>차량 외판 · 객실 내부</li><li>역사 벽 · 승강장 · 터널</li><li>HVAC 코일 · 환기 스택</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">ROLLING STOCK & MECHANICAL COMPONENTS</span>
      <h3>대차 · 윤축 · 기관차 기계부</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rail-cleaning-freight-car-axels-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/rail-cleaning-freight-car-undercarriage-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">두꺼운 산업 그리스를 제거하면서<br>씰과 베어링은 손상시키지 않습니다.</p>
      <div class="cmp-text auto-text"><p>대차와 윤축, 차축·베어링, 스프링·기어, 디젤 엔진 블록, 브레이크 컨트롤러·액추에이터, 팬터그래프에는 두꺼운 그리스와 탄소 침착물, 환경 이물이 쌓입니다. 수작업 스크레이핑은 핀치 포인트 근처에서 작업자를 위험에 노출시키고, 물 세척은 강재 프레임에 플래시 러스트를 만듭니다.</p><p>드라이아이스는 두꺼운 그리스를 제거할 만큼 강하면서 씰과 베어링을 손상시키지 않는 세척 방식으로 활용되며, 운전 온도에서 작업자 손을 핀치 포인트에서 떨어뜨린 채 작업할 수 있습니다. Cold Jet은 정비시설에서 부품당 수 초 내 탄소 제거를 달성한 사례와, 기관차 재도장 전 표면 전처리를 플래시 러스트 없이 수행해 도장 밀착이 개선된 사례를 제시하고 있습니다. 화물차의 아스팔트 제거에도 적용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>대차 · 윤축 · 차축 · 베어링</li><li>스프링 · 기어 · 기계 조립체</li><li>디젤 엔진 블록 · 냉각팬 · 라디에이터</li><li>브레이크 컨트롤러 · 액추에이터 · 팬터그래프</li><li>탱크차 내부 · 배관 · 밸브</li></ul></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">LOCOMOTIVE ELECTRICAL & PAINT BOOTH</span>
      <h3>기관차 전력계통 · 도장부스</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rail-removing-asphalt-from-freight-car-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">디젤-전기 발전기의 탄소와 오일 미스트,<br>도장부스의 오버스프레이를 수분 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>디젤-전기 발전기와 견인 교류발전기, 전기 제어 캐비닛, 차단기, 배전 시스템에는 탄소와 오일 미스트가 쌓여 단락과 고장을 일으킵니다. 차량 재정비 시설의 도장부스 벽·바닥·환기 시스템·분사 장비에는 도료와 프라이머, 오버스프레이가 쌓여 도장 품질을 떨어뜨립니다.</p><p>드라이아이스 세척은 운전 온도에서 분해 없이 전력계통의 탄소·오일 미스트를 제거하는 방식으로 활용되며, 도장부스에는 수분이나 연마재를 도입하지 않고 부스 분해 없이 축적 도료를 제거합니다. Cold Jet은 여러 기관차 제조사·정비시설이 전기계통 세척에 적용해 고장률 개선을 보고했고, 대형 차량 임대사가 도장부스 유지보수용으로 여러 대를 도입한 사례를 제시하고 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>디젤-전기 발전기 · 견인 교류발전기</li><li>전기 제어 캐비닛 · 배전 시스템</li><li>도장부스 벽 · 바닥 · 환기</li><li>분사 장비 · 기관차 외판</li></ul></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">철도 차량 · 인프라에서<br>반복적으로 발생하는 주요 오염물</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/rail-cleaning-freight-car-axels-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>두꺼운 그리스</b><small>HEAVY GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/rail-cleaning-undercarriage-of-passenger-rail-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>브레이크 분진 (전도성)</b><small>METALLIC BRAKE DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/rail-cleaning-freight-car-undercarriage-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄소 분진 · 침착물</b><small>CARBON DUST & DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 미스트 · 산화 잔류물</b><small>OIL MIST & OXIDATIVE RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/rail-removing-paint-from-exterior-panel-of-subway-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>도료 · 프라이머 · 오버스프레이</b><small>PAINT & OVERSPRAY</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/rail-removing-asphalt-from-freight-car-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>아스팔트 · 압착 유기물</b><small>ASPHALT & ORGANIC MATTER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제 · 데칼 · 껌</b><small>ADHESIVES, DECALS & GUM</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/rail-removing-residue-and-grime-from-interior-of-subway-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>그을음 · 때</b><small>SOOT & GRIME</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">철도 · 대중교통에서<br>드라이아이스 세척을 검토하는 이유</h2>
  <ol class="auto-why is-6">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비전도성</b><p>견인전동기와 전기 캐비닛, 제3궤조 애자, 변압기를 단락이나 절연 손상 위험 없이 세척하는 방식으로 활용됩니다. 활선 여부와 안전 절차는 별도로 확인해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>플래시 러스트 없음</b><p>물을 쓰지 않아 강재 프레임과 부품에 플래시 러스트가 생기지 않고, 재도장 전 표면을 수분 없이 준비할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>2차 폐기물 없음</b><p>오염된 그릿이나 폐수, 유해 용제를 회수·폐기할 필요가 없어 처리 비용이 발생하지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>장착 상태 · 운전 온도 세척</b><p>추진계통과 브레이크 조립체를 완전 분해 없이 세척할 수 있는 경우 바로 운행에 복귀할 수 있습니다. Cold Jet은 정비 체류시간을 절반 수준으로 줄인 사례를 인용합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>작업자 안전 · 인체공학</b><p>토치와 용제, 와이어 브러시 스크레이핑을 없애고, 노즐 도달 거리로 핀치 포인트와 중장비 주변의 불편한 자세를 줄입니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.45s"><b>비마모성</b><p>씰과 베어링, 절연물, 정밀 부품을 마모시키지 않고 두꺼운 그리스와 탄소를 제거합니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 정비기지 안에서도,<br>설비마다 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>견인전동기의 탄소 분진, 차축의 두꺼운 그리스, 객실 내부의 때와 외판의 도료는 같은 정비기지에서 발생하지만 대상의 민감도와 오염물의 성질, 안전 조건이 크게 다릅니다.</p>
            <p>바테크는 설비의 재질과 절연 구조, 오염물의 종류, 정비 체류시간과 안전 절차를 확인한 뒤 실제 테스트를 통해 마이크로 입자부터 3mm 펠렛까지 적합한 조건을 검토합니다. 현장 작업에는 디젤 컴프레서 등 압축공기 확보 방안도 함께 계획합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/rail-cleaning-freight-car-axels-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>차축 · 베어링</b><small>두꺼운 그리스</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/rail-removing-residue-and-grime-from-interior-of-subway-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>객실 내부</b><small>잔류물 · 때</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/rail-removing-paint-from-exterior-panel-of-subway-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>차량 외판</b><small>도료 · 데칼</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>우리 차량의 세척 조건</em>부터 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">철도 · 대중교통에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">철도 · 대중교통 안에서도 설비와 오염물에 따라 필요한 세척 방법은 달라집니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.35s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED INDUSTRIES</span>
      <h2 class="cmp-h2">철도 · 대중교통과 연결되는<br>관련 산업</h2>
    </div>
    <p class="cmp-lead-p">견인전동기·발전기 같은 대형 전기설비 세척은 발전 · 전력과, 중장비 그리스와 디젤 엔진 세척은 광업과 같은 과제를 공유합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/power-generation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></span><small>POWER GENERATION</small><b>발전 · 전력</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/mining.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /></span><small>MINING</small><b>광업</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN IN RAIL & TRANSIT OPERATIONS</span>
      <h2 class="cmp-h2">글로벌 철도 · 대중교통 현장에서<br>검증된 기술</h2>
    </div>
    <p class="cmp-lead-p">철도 운영기관과 차량 제조·임대사가 차량과 인프라 유지보수에 Cold Jet 드라이아이스 세척 기술을 활용하고 있습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 철도 · 대중교통 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:48%"><img src="../assets/img/rail-deutsche-bahn-logo.webp" alt="Deutsche Bahn" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:56%"><img src="../assets/img/rail-sncf-logo.webp" alt="SNCF" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:52%"><img src="../assets/img/rail-sncb_logo.webp" alt="SNCB" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:62%"><img src="../assets/img/rail-east_japan_railway_company_logo.webp" alt="JR East" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:56%"><img src="../assets/img/rail-bay-area-rapid-transit-logo.webp" alt="BART" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:60%"><img src="../assets/img/rail-metra_logo.webp" alt="Metra" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:56%"><img src="../assets/img/rail-csx_corporation_logo.webp" alt="CSX" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:66%"><img src="../assets/img/rail-wabtec_logo.webp" alt="Wabtec" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:60%"><img src="../assets/img/rail-gatx-rail-logo.webp" alt="GATX Rail" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:62%"><img src="../assets/img/rail-union-tank-car_logo.webp" alt="Union Tank Car" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 차량 · 정비설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>같은 철도 차량이라도 재질과 절연 구조, 오염물의 종류와 부착 정도, 정비 체류시간과 안전 절차에 따라 적합한 세척 조건은 달라질 수 있습니다.</p>
      <p>실제 부품이나 시편을 이용한 테스트를 통해 세척 가능 여부와 작업 조건을 확인해보세요. 바테크는 테스트 결과를 바탕으로 현장에 적합한 세척 조건과 장비 구성을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 차량 · 정비설비의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

# (2026-09-08, 10차 핸드오프) 작업별 상세 첫 페이지 "금형·툴링 세척"(applications/)과
# 산업별 17번 "전문 세척 서비스" 상세 — 자동차 마스터 구조 + 전용 블록(.mtc-*, .auto-feature).
MOLD_TOOL_CLEANING_BODY = """
  <!-- 기술 내용·이미지 출처(Cold Jet 공식):
     https://www.coldjet.com/dry-ice-blasting/applications/plastic-rubber-mold-cleaning/
     https://www.coldjet.com/dry-ice-blasting/applications/composite-tool-cleaning/
     https://www.coldjet.com/dry-ice-blasting/applications/core-box-cleaning/
     https://www.coldjet.com/dry-ice-blasting/industries/rubber-tires/  ·  /industries/foundry/  ·  /industries/plastics-composites/
     사례: https://www.coldjet.com/resources/performance-plastics/  ·  https://blog.coldjet.com/what-is-the-best-way-to-clean-a-rubber-mold-dry-ice-blasting (Vernay)
           https://www.coldjet.com/resources/progress-casting-group/  ·  https://www.coldjet.com/resources/mws-friedrichshafen-gmbh-cold-jet-gmbh/
     이미지는 모두 저장소 assets/img 에 로컬화된 Cold Jet 자료를 재사용. 단, 히어로 배너 1장은 원본 URL 참조 → 다운로드 후 data-local 경로로 교체:
       ../assets/img/mold-cleaning-hero-banner.jpg  →  assets/img/mold-cleaning-hero-banner.jpg
     로고 2장(Wikimedia Commons, data-local 참조): Kumho_Tire_logo_(2023).svg → logo-kumho-tire.png / NEXEN_TIRE_LOGO.jpg → logo-nexen-tire.jpg (흰 배경 JPG — 배경 투명 처리 후 사용) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/mold-cleaning-hero-banner.jpg" alt="금형을 드라이아이스로 세척하는 장면" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 금형 · 툴링 세척</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">MOLD &amp; TOOLING CLEANING</span>
      <h1>금형 · 툴링 세척</h1>
      <p class="cmp-hero-p auto-hero-lead">오염물은 제거하고,<br>금형의 표면과 정밀한 형상은 보호합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page mtc-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">MOLD MAINTENANCE</span>
      <h2 class="cmp-h2">금형 세척은 단순히 표면을<br>깨끗하게 만드는 작업이 아닙니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>사출금형과 고무·타이어 금형, 복합재 툴링, 다이캐스팅 금형과 코어박스에는 생산이 반복될수록 이형제, 수지, 오프가스, 접착제, 카본과 각종 공정 잔류물이 축적됩니다.</p>
      <p>특히 캐비티와 벤트, 파팅라인과 미세한 홈에 쌓인 오염은 제품의 외관과 성형 상태, 이형성, 벤팅과 금형 관리에 영향을 줄 수 있습니다. 벤트가 막히면 쇼트나 번(burn) 같은 성형 불량으로 이어지기도 합니다.</p>
      <p>그런데 금형 세척에서는 오염물을 제거하는 것만큼 중요한 것이 있습니다. 바로 금형의 표면과 형상을 유지하는 것입니다. 와이어 브러시, 연마 패드, 일부 연마재를 사용하는 방식은 오염물을 빠르게 제거할 수 있지만, 반복적인 마찰과 연마가 정밀한 표면과 모서리, 파팅라인에 영향을 줄 수 있습니다.</p>
      <p class="auto-intro-close">금형 세척에서는 "얼마나 강하게 닦는가"보다 <b>필요한 오염물은 제거하면서 금형은 어떻게 보호할 것인가</b>를 함께 고려해야 합니다.</p>
    </div>
  </div>
  <ul class="mtc-detail reveal" aria-label="금형에서 오염이 쌓이는 부위">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/plastics-composites-removing-residual-plastic-and-pigment-from-plastic-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span><small>CAVITY</small><b>캐비티</b></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/foundry-cleaning-of-a-multi-cavity-core-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span><small>VENT</small><b>벤트</b></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/medical-medical-mold-tool-cleaning.webp" alt="" loading="lazy" /><span><small>PARTING LINE</small><b>파팅라인 · 실링면</b></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/rubber-tires-tire-mold-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span><small>FINE PATTERN</small><b>미세 패턴 · 홈</b></span></li>
  </ul>
  <p class="mtc-quote reveal">잘 닦는 것만큼, <em>무엇을 지켜야 하는지</em>도 중요합니다.</p>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">MOLD &amp; TOOLING APPLICATIONS</span>
    <h2 class="cmp-h2">재질과 생산공정이 달라도,<br>금형 세척에서 고려해야 할 기본은 같습니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PLASTIC &amp; INJECTION MOLD</span>
      <h3>플라스틱 · 사출금형</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/plastics-composites-dry-ice-blasting-injection-mold.webp" alt="사출금형 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-removing-offgas-from-mold.webp" alt="금형의 오프가스 잔류물 제거" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">캐비티와 벤트에 축적되는<br>성형 잔류물을 세척합니다.</p>
      <div class="cmp-text auto-text"><p>플라스틱 사출공정에서는 수지에서 발생하는 오프가스, 이형제, 안료와 성형 잔류물이 금형의 캐비티와 벤트, 복잡한 형상에 반복적으로 축적될 수 있습니다. Cold Jet 자료에 따르면 이러한 오염은 벤트 막힘, 쇼트, 플레이트아웃, 번, 플래시 같은 성형 문제의 원인이 됩니다.</p><p>드라이아이스 세척은 금형 표면을 연마하는 방식이 아니기 때문에 정밀한 캐비티와 복잡한 형상을 고려해야 하는 사출금형 세척에 활용할 수 있습니다. 작은 오리피스와 마이크로 캐비티를 가진 정밀 금형, 텍스처 금형, PET 프리폼 금형 등에도 적용된 사례가 있습니다.</p><p>적용 조건에 따라 금형을 장비에서 완전히 분리하지 않고 성형 온도 상태에서 세척할 수 있는 경우도 있어, 세척을 위한 냉각·분해·재조립에 드는 정비시간을 줄이는 데 도움이 될 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>사출금형 (Injection Mold)</li><li>압축금형 (Compression Mold)</li><li>열성형 금형 (Thermoform)</li><li>블로우 금형</li><li>PET 프리폼 금형</li><li>LSR · LIM 금형</li><li>압출 다이 (Extrusion Die)</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">RUBBER &amp; TIRE MOLD</span>
      <h3>고무 · 타이어 금형</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/rubber-tires-tire-mold-cleaning-with-dry-ice-blasting.webp" alt="타이어 금형 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/rubber-tires-dry-ice-blasting-cleans-rubber-injection-mold.webp" alt="고무 사출금형 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">미세한 패턴과 벤트 구조를 고려하면서<br>축적된 성형 잔류물을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>고무 성형과 타이어 생산에서는 이형제, 가류된 고무 잔류물, 카본과 성형 부산물이 금형의 홈과 벤트에 축적될 수 있습니다. 오염이 쌓이면 금형에 제품이 붙거나 표면 얼룩, 불필요한 플래시가 생겨 라인을 세워 세척해야 하는 상황이 반복됩니다.</p><p>특히 타이어 금형처럼 미세한 트레드 패턴과 다수의 벤트가 있는 금형은 세척 과정에서도 금형의 형상과 표면 상태를 세심하게 고려해야 합니다. 샌드블라스팅이나 와이어 브러시는 반복될수록 이 표면을 마모시킬 수 있습니다.</p><p>드라이아이스 세척은 비마모성 방식으로, 조건에 따라 타이어 금형을 가류기에서 분리하지 않고 고온 상태에서 세척한 사례가 있습니다. Cold Jet 자료에 따르면 금형 온도와 드라이아이스의 온도 차로 인한 열충격이나 금속 조직 변화는 확인되지 않았습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>고무 사출금형</li><li>고무 압축금형</li><li>타이어 금형 (트레드 세그먼트 · 사이드월)</li><li>씰 · 가스켓 · 프로파일 금형</li><li>실리콘 금형</li></ul></div>
      <a class="auto-rel-link" href="../industries/rubber-tires.html"><span>관련 산업</span>고무 · 타이어 <i>→</i></a>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">COMPOSITE TOOL CLEANING</span>
      <h3>복합재 툴링</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/aerospace-dry-ice-blasting-removing-resin-and-release-agents-from-composite-tooling.webp" alt="복합재 툴링의 수지·이형제 제거" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-removing-gel-coat-buildup-from-composite-mold-with-dry-ice-blasting.webp" alt="복합재 금형의 젤코트 축적물 제거" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">툴링의 표면 마감은 유지하면서<br>이형제와 수지 잔류물을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>복합재 생산에는 스틸과 알루미늄, 에폭시와 우레탄, 테프론 코팅과 경질 아노다이징 표면, 젤코트 툴링까지 다양한 재질과 표면 마감을 가진 금형과 툴링이 사용됩니다.</p><p>프리프레그(Pre-preg), 웻 레이업, SMC·BMC 압축성형, RTM, 인발성형 등의 공정에서는 이형제(희생형·반영구·영구), 에폭시, 실리콘, 테프론 테이프와 태키 테이프, 페놀릭, 카본·그래파이트 섬유 잔류물이 툴링 표면에 남을 수 있습니다.</p><p>드라이아이스 세척은 툴 표면을 에칭하거나 프로파일을 바꾸지 않는 비마모성 방식으로, 셧오프와 파팅라인 같은 치수 기준면을 고려하면서 이러한 잔류물을 제거하는 데 활용됩니다. 승화하는 세정 매체이므로 항공 부품 제조에서 문제가 되는 이물(FOD)이 남지 않는다는 점도 Cold Jet 자료에서 강조됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>프리프레그 · 웻 레이업 툴링</li><li>SMC · BMC 압축금형</li><li>RTM 툴링</li><li>인발성형 다이</li><li>테프론 코팅 · 아노다이징 툴</li><li>에폭시 · 우레탄 툴</li></ul></div>
      <a class="auto-rel-link" href="../industries/aerospace.html"><span>관련 산업</span>우주 · 항공 <i>→</i></a>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">DIE CAST TOOLING &amp; CORE BOX</span>
      <h3>다이캐스팅 · 주조 툴링</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-die-cast-tooling.webp" alt="다이캐스팅 툴링 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/foundry-core-box-cleaning-with-dry-ice-blasting.webp" alt="코어박스 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">반복 생산으로 오염되는<br>금형과 코어박스를 관리합니다.</p>
      <div class="cmp-text auto-text"><p>다이캐스팅 금형과 영구금형, 코어박스에는 반복적인 생산 과정에서 이형제, 다이캐스팅용 윤활제, 콜드박스·쉘 코어 바인더 수지, 카본, 내화 코팅과 공정 잔류물이 축적될 수 있습니다.</p><p>코어박스와 주조용 금형은 복잡한 형상과 다수의 벤트, 정밀한 표면을 가지고 있기 때문에 세척 과정에서도 이러한 구조를 고려해야 합니다. Cold Jet 자료에 따르면 연마재 블라스팅은 코어박스의 벤트를 손상시킬 수 있어, 벤트를 막지 않고 열어 주는 세척 방식이 필요합니다.</p><p>드라이아이스 세척은 이러한 벤트와 미세 형상을 연마 없이 세척하는 데 활용되며, 조건에 따라 고압 다이캐스팅(HPDC) 금형과 코어박스를 라인에서 분리하지 않고 작업 온도 상태에서 세척한 사례가 있습니다. 코어박스처럼 형상이 복잡한 대상에는 미세입자(MicroParticle) 드라이아이스가 주로 사용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>다이캐스팅 금형 (HPDC · 반용융)</li><li>영구금형 · 저압주조 금형</li><li>코어박스 (콜드박스 · 쉘)</li><li>주조 지그 · 트림 다이</li></ul></div>
      <a class="auto-rel-link" href="../industries/foundry.html"><span>관련 산업</span>주조 · 다이캐스팅 <i>→</i></a>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">같은 금형이라도,<br>생산공정에 따라 쌓이는 오염물은 다릅니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/plastics-composites-removing-mold-release-agent-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>이형제</b><small>MOLD RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/plastics-composites-removing-residual-plastic-and-pigment-from-plastic-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>수지 · 폴리머 잔류물</b><small>RESIN &amp; POLYMER RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/plastics-composites-removing-offgas-from-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오프가스 잔류물</b><small>OFF-GAS RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/rubber-tires-cleaning-rubber-compression-mold-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>고무 · 가류 잔류물</b><small>RUBBER RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/aerospace-dry-ice-blasting-removing-resin-and-release-agents-from-composite-tooling.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>에폭시 · 접착 테이프</b><small>EPOXY &amp; TACKY TAPE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/medical-clean-tpe-from-tooling.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>실리콘 · 엘라스토머</b><small>SILICONE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/plastics-composites-dry-ice-blasting-cleaning-composite-tooling.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 · 그래파이트</b><small>CARBON &amp; GRAPHITE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/foundry-removing-die-lube-from-magnesium-die-cast-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>다이캐스팅 윤활제</b><small>DIE LUBRICANT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.48s"><img src="../assets/img/foundry-removing-refractory-coating-from-permanent-mold.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>내화 코팅 · 바인더</b><small>REFRACTORY COATING &amp; BINDER</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">금형을 세척하는 방법이<br>금형 자체에 부담이 되어서는 안 됩니다.</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성 세척</b><p>드라이아이스 입자는 금형 표면을 깎아내는 연마재가 아닙니다. 정밀한 금형 표면과 파팅라인, 벤트의 형상을 고려하면서 오염물을 제거하는 데 활용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>물을 사용하지 않는 건식 세척</b><p>물을 이용한 세척이 아니기 때문에 세척 후 금형과 주변 설비를 별도로 건조해야 하는 부담을 줄일 수 있습니다. 녹 발생 우려가 있는 스틸 금형에도 이 점이 중요합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스 입자는 세척 과정에서 승화하여 기체로 전환되므로 모래나 비드 같은 블라스팅 매체가 금형과 주변에 남지 않습니다. 단, 제거된 오염물 자체는 남기 때문에 필요에 따라 별도의 회수와 처리가 필요합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>분해와 냉각 시간을 줄일 가능성</b><p>적용 대상과 작업 조건에 따라 금형을 장비에서 완전히 분리하지 않거나 상온까지 냉각하지 않고 세척할 수 있는 경우가 있습니다. 이 경우 세척과 정비를 위한 생산 중단시간을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>복잡한 형상에 접근</b><p>노즐과 분사 조건을 조정하여 캐비티, 홈, 벤트, 좁은 공간과 복잡한 형상에 접근할 수 있습니다. 입자 크기를 조절하면 미세한 부위와 넓은 면에 각각 다른 강도로 대응할 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark mtc-preserve">
    <div class="wrap">
      <div class="mtc-preserve-grid">
        <div class="reveal">
          <span class="cmp-eyebrow">PRESERVE THE TOOLING</span>
          <h2 class="cmp-h2">한 번 깨끗하게 만드는 것보다,<br>반복해서 세척할 수 있는 방법이 중요합니다.</h2>
          <div class="cmp-dark-body">
            <p>금형은 한 번 사용하고 교체하는 소모품이 아니라, 같은 형상을 반복해서 생산하기 위한 정밀한 생산 도구입니다. 파팅라인과 실링면, 벤트와 캐비티, 표면 마감 상태는 제품의 성형과 품질에 직접 영향을 줍니다.</p>
            <p>따라서 금형 세척은 한 번의 제거 성능뿐 아니라, 반복적인 세척이 금형의 표면과 형상에 어떤 영향을 줄 것인지까지 함께 고려해야 합니다. 세척 주기가 잦아질수록 이 차이는 더 커집니다.</p>
          </div>
        </div>
        <div class="mtc-preserve-side reveal" style="--reveal-delay:0.16s">
          <ul class="mtc-preserve-pics">
            <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/medical-medical-device-mfg-cleans-molds.webp" alt="정밀 금형 캐비티" loading="lazy" /><small>정밀 캐비티 · 파팅라인</small></li>
            <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-core-box-online.webp" alt="코어박스 벤트" loading="lazy" /><small>코어박스 벤트</small></li>
          </ul>
          <p class="auto-ae-key">오염물을 제거하는 것과 금형을 보호하는 것은<br><em>같은 세척 과정 안에서 함께</em> 고려되어야 합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page ind-page auto-page mtc-page mtc-mid">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first mtc-ae">
  <div class="auto-ae">
    <div class="reveal">
      <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
      <h2 class="cmp-h2">같은 금형이라도,<br>세척 조건은 같지 않습니다.</h2>
      <div class="cmp-lead">
        <p>사출금형의 얇은 오프가스와 고무금형에 고착된 가류 잔류물, 복합재 툴링의 이형제, 다이캐스팅 금형의 윤활제는 같은 조건으로 세척할 수 없습니다.</p>
        <p>금형의 재질과 표면처리, 형상과 온도, 오염물의 종류와 부착 정도에 따라 적절한 분사 조건은 달라집니다. 바테크는 실제 금형과 오염 상태를 확인하고 세척 테스트를 통해 적합한 조건을 찾습니다.</p>
      </div>
      <ul class="mtc-vars" aria-label="테스트에서 조정하는 변수">
        <li>드라이아이스 입자 크기</li><li>분사 압력</li><li>드라이아이스 공급량</li><li>노즐</li><li>분사 거리</li><li>분사 각도</li>
      </ul>
      <p class="mtc-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
    </div>
    <div class="mtc-ae-side reveal" style="--reveal-delay:0.16s">
      <div class="mtc-ae-cols"><span>금형</span><span>대표 오염물</span><span>세척 조건에서 고려할 점</span></div>
      <ul class="mtc-ae-rows">
        <li class="reveal" style="--reveal-delay:0.30s"><img src="../assets/img/plastics-composites-dry-ice-blasting-injection-mold.webp" alt="" loading="lazy" /><div><b>사출금형</b><small>INJECTION MOLD</small></div><div class="mtc-ae-c"><span>오프가스</span><span>이형제</span></div><p>얇게 넓게 퍼진 잔류물. 미세입자·낮은 압력으로 광택면과 텍스처를 유지하며 벤트를 열어 주는 방향</p></li>
        <li class="reveal" style="--reveal-delay:0.42s"><img src="../assets/img/rubber-tires-tire-mold-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><div><b>고무 · 타이어 금형</b><small>RUBBER / TIRE MOLD</small></div><div class="mtc-ae-c"><span>가류 고무</span><span>카본</span></div><p>고착된 잔류물과 깊은 패턴. 고온 금형에서는 열 효과가 더해져 조건이 달라짐 — 압력·입자 크기를 단계적으로 확인</p></li>
        <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/aerospace-dry-ice-blasting-removing-resin-and-release-agents-from-composite-tooling.webp" alt="" loading="lazy" /><div><b>복합재 툴링</b><small>COMPOSITE TOOL</small></div><div class="mtc-ae-c"><span>에폭시</span><span>이형제</span></div><p>에폭시·우레탄·코팅 툴은 재질별 허용 범위가 다름. 반영구 이형제를 남길지 함께 제거할지에 따라 조건을 나눔</p></li>
        <li class="reveal" style="--reveal-delay:0.66s"><img src="../assets/img/foundry-dry-ice-blasting-cleaning-die-cast-tooling.webp" alt="" loading="lazy" /><div><b>다이캐스팅 금형 · 코어박스</b><small>DIE CAST / CORE BOX</small></div><div class="mtc-ae-c"><span>윤활제</span><span>바인더 · 코팅</span></div><p>두껍게 고착된 잔류물과 다수의 벤트. 벤트를 손상시키지 않는 각도와 미세입자 조합을 우선 검토</p></li>
      </ul>
    </div>
  </div>
</div>
</div>
</div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page mtc-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">INDUSTRIES</span>
      <h2 class="cmp-h2">금형과 툴링이 사용되는<br>다양한 생산현장에서 활용할 수 있습니다.</h2>
    </div>
    <p class="cmp-lead-p">금형 세척은 특정 산업의 작업이 아닙니다. 각 산업의 생산공정과 함께 보려면 산업 페이지를 확인하세요.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS &amp; COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/rubber-tires.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-rubber-tire.png" alt="" loading="lazy" /></span><small>RUBBER &amp; TIRES</small><b>고무 · 타이어</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/foundry.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-foundry.png" alt="" loading="lazy" /></span><small>FOUNDRY &amp; DIE CASTING</small><b>주조 · 다이캐스팅</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE &amp; AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.35s"><a href="../industries/medical.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></span><small>MEDICAL DEVICE MANUFACTURING</small><b>의료기기 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.42s"><a href="../industries/semiconductor.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-semiconductor.png" alt="" loading="lazy" /></span><small>SEMICONDUCTOR &amp; ELECTRONICS</small><b>반도체 · 전자 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.49s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PROVEN MOLD CLEANING APPLICATIONS</span>
      <h2 class="cmp-h2">다양한 금형과 툴링에서<br>확인된 적용 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 금형 세척 자료에 소개된 사용 기업입니다. 아래 사례는 각 현장의 조건에서 확인된 결과이며, 모든 금형에 같은 결과를 보장하는 것은 아닙니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 금형 세척을 사용하는 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:74%"><img src="../assets/img/medical-becton-dickinson-logo.webp" alt="Becton Dickinson" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:76%"><img src="../assets/img/plastics-composites-silgan.jpg" alt="Silgan Plastics" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:74%"><img src="../assets/img/plastics-composites-milacron_logo.webp" alt="Milacron" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:60%"><img src="../assets/img/aerospace-airbus_logo.webp" alt="Airbus" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:76%"><img src="../assets/img/aerospace-collins-aerospace.webp" alt="Collins Aerospace" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:42%"><img src="../assets/img/logo-bmw.webp" alt="BMW" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:74%"><img src="../assets/img/aerospace-spacex_logo.webp" alt="SpaceX" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:70%"><img src="../assets/img/rubber-tires-bridgestone_logo.webp" alt="Bridgestone" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:70%"><img src="../assets/img/rubber-tires-michelin_logo.webp" alt="Michelin" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:70%"><img src="../assets/img/rubber-tires-hankook_logo.webp" alt="Hankook" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.40s; --w:72%"><img src="../assets/img/logo-kumho-tire.png" alt="Kumho Tire" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.44s; --w:56%"><img src="../assets/img/logo-nexen-tire.png" alt="Nexen Tire" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.48s; --w:66%"><img src="../assets/img/foundry-nemak_logo.webp" alt="Nemak" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.52s; --w:72%"><img src="../assets/img/foundry-precision_castparts_logo.webp" alt="Precision Castparts" loading="lazy" /></li>
  </ul>
  <ul class="mtc-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>RUBBER MOLD</small><b>고무 성형금형</b><span>Vernay</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>밸브·씰류 고무 성형금형</dd></div>
        <div><dt>오염물</dt><dd>고무 오프가스 잔류물</dd></div>
        <div><dt>기존 방식</dt><dd>프레스에서 금형을 내려 냉각 후 세척. 회당 6~8시간 손실, 재가열 별도</dd></div>
        <div><dt>적용</dt><dd>프레스 안에서 드라이아이스 세척 (분해·냉각 없이)</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>세척시간 6시간 이상 → 30분~1시간 (금형 복잡도에 따라). 금형을 내리는 횟수가 줄어 파손 위험도 감소</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>INJECTION MOLD</small><b>정밀 사출금형</b><span>Performance Plastics</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>정밀 플라스틱 사출금형</dd></div>
        <div><dt>오염물</dt><dd>성형 잔류물 · 이형제</dd></div>
        <div><dt>기존 방식</dt><dd>반복 세척 시 파팅라인 손상과 금속 표면 변화 우려</dd></div>
        <div><dt>적용</dt><dd>매일, 매 교대마다 드라이아이스 세척을 정기 사용</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>파팅라인이 밀리거나 금속이 변하지 않았고, 연속 생산시간이 늘어났다고 보고 (사용자 인용)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.20s">
      <div class="mtc-case-head"><small>CORE BOX · PERMANENT MOLD</small><b>코어박스 · 영구금형</b><span>Progress Casting Group</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>정밀 다이캐스팅·사형주조용 금형과 코어박스</dd></div>
        <div><dt>오염물</dt><dd>바인더 수지 · 이형제 · 코팅 잔류물</dd></div>
        <div><dt>기존 방식</dt><dd>화학약품·브러시 수작업. 작업자 2~3명이 3~4시간, 벤트 손상 우려</dd></div>
        <div><dt>적용</dt><dd>미세입자 드라이아이스로 고온·온라인 상태에서 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>작업자 1명이 약 10분에 금형 1개 세척 (해당 현장 기준). 벤트를 보호하면서 연마 세척을 대체</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR MOLD</span>
    <h2 class="cmp-h2">우리 금형에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>금형의 재질과 표면 상태, 오염물의 종류와 부착 정도에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 금형 또는 샘플을 이용한 세척 테스트를 통해 드라이아이스 세척의 적용 가능성과 적절한 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">금형 세척 사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

CONTRACT_CLEANING_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/contract-cleaning/
     + https://www.coldjet.com/dry-ice-blasting/industries/restoration-remediation/
     + https://blog.coldjet.com/tag/contract-cleaning (사례: Industrial Cleaning Solutions / Advanced Indoor Air Quality Care / USCleanBlast)
     바테크 실제 현장 사진(assets/img/vatek-field-*.png): 동상 세척(히어로·브릿지) / 유물 기계 세척 · 문화재 증기기관차 세척(05) / 기름유출 사고 세척(스트립·MORE THAN CLEANING POWER)
     원본 URL 참조 이미지(배포 시 assets/img/ 로 로컬화):
       Cleaning-in-progress-Fire-v2-500x500.jpg → contract-fire-restoration.jpg
       DRYICEBLASTING_APPLICATIONS_REMEDIATION-5-1-1-500x500.jpg → contract-mold-remediation-attic.jpg
       로고 5종(robotworx, USCleanBlast, Bonazza, Adrian-Environmental, us-flood-team) → logo-*.png
     나머지 이미지는 기존 로컬 자산 재사용 -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/vatek-field-statue-cleaning-graded.png" alt="전문 세척 서비스 현장 — 동상 드라이아이스 세척" style="object-position: 50% 40%" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 전문 세척 서비스</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">CONTRACT CLEANING</span>
      <h1>전문 세척 서비스</h1>
      <p class="cmp-hero-p auto-hero-lead">현장이 달라지면, 세척해야 할 대상과 오염물도 달라집니다.</p>
      <p class="cmp-hero-p auto-hero-body">생산설비와 금형, 식품·포장설비, 인쇄기와 발전설비에서 복원 현장까지 — 세척 대상과 오염물, 작업환경과 요구되는 결과는 현장마다 달라집니다. 드라이아이스 세척은 물을 사용하지 않는 건식 세척이자 연마재를 사용하지 않는 비마모성 방식으로, 다양한 산업설비와 표면에 축적된 오염물을 현장에서 제거하는 데 활용할 수 있습니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">CONTRACT CLEANING SERVICES</span>
      <h2 class="cmp-h2">전문 세척업체가 만나는 현장은<br>하나가 아닙니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>전문 세척업체는 매번 서로 다른 작업 조건을 마주합니다. 어떤 현장에서는 생산설비에 쌓인 오일과 그리스를 제거해야 하고, 다른 현장에서는 인쇄기의 잉크와 접착제, 식품설비의 탄화 잔류물, 발전설비의 고착 오염물을 제거해야 합니다. 화재나 수해 이후의 복원 현장에서는 다시 그을음과 각종 오염물을 다루게 됩니다.</p>
      <p>따라서 전문 세척에서는 단순히 세척력이 강한 방법을 선택하기보다, 오염물의 종류와 부착 상태, 세척 대상의 재질과 형상, 작업공간과 접근성, 세척 후 필요한 처리 과정까지 함께 고려하는 것이 중요합니다.</p>
      <p class="auto-intro-close">전문 세척의 경쟁력은 더 강하게 세척하는 데 있는 것이 아니라, <b>서로 다른 현장에 맞는 방법을 찾는 데</b> 있습니다.</p>
    </div>
  </div>
  <ul class="auto-strip" aria-label="다양한 현장">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/food-beverage-cleaning-conveyors-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span>식품 컨베이어</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/printing-large-printing-press-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span>인쇄기</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/power-generation-cleaning-hydroelectric-generator-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span>수력 발전기</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/vatek-field-oil-spill-cleanup-graded.png" alt="" loading="lazy" style="object-position: 100% 100%" /><span>기름유출 사고 현장</span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY SERVICE AREAS</span>
    <h2 class="cmp-h2">하나의 세척 기술이<br>서로 다른 현장에서 활용됩니다.</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">INDUSTRIAL & FACILITY CLEANING</span>
      <h3>생산설비 · 시설 유지보수</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/industry-maintenance.jpg" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">설비의 구조와 작업 조건을 고려하면서<br>축적된 오염물을 현장에서 제거합니다.</p>
      <div class="cmp-text auto-text"><p>생산설비에는 운전과 생산이 반복되면서 오일, 그리스, 먼지와 각종 공정 잔류물이 축적됩니다. 컨베이어와 산업용 로봇, 모터와 기계설비, 공장 인프라처럼 업종을 가리지 않고 존재하는 설비가 전문 세척업체의 가장 흔한 작업 대상입니다.</p><p>드라이아이스 세척은 물을 사용하지 않고 별도의 연마재를 남기지 않는 방식이기 때문에 다양한 산업설비의 현장 세척에 활용할 수 있습니다. 적용 조건에 따라 설비의 완전한 분해나 세척 후 건조 작업을 줄일 수 있는 경우도 있습니다. 전기·제어설비는 전원 상태와 설비 구조, 안전 조건을 별도로 확인한 뒤 적용 여부를 판단합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>생산설비 · 기계설비</li><li>산업용 로봇 · 컨베이어</li><li>모터 · 공장 인프라</li><li>일부 전기 · 제어설비 (조건 확인 후)</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>오일 · 그리스 · 수지 · 접착제 · 분진 · 생산 잔류물</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">FOOD PROCESSING EQUIPMENT</span>
      <h3>식품 생산설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/food-beverage-dry-ice-blasting-granola-oven.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">생산설비에 축적되는<br>식품 잔류물과 탄화 오염물을 건식으로 세척합니다.</p>
      <div class="cmp-text auto-text"><p>Cold Jet 자료에 따르면 식품 현장의 전문 세척업체는 유지와 단백질 잔류물, 탄화 잔류물, 접착제와 라벨 잔류물을 위생 기준 안에서 제거해야 합니다. 물과 화학세정제를 쓰는 기존 방식은 설비 분해와 마스킹, 세척 후 건조가 뒤따르고, 수분을 피해야 하는 전기부품과 모서리·틈새는 세척이 어렵습니다.</p><p>드라이아이스 세척은 물과 세정제 없이 설비를 제자리에서 세척하는 방식으로 활용되어, 세척을 위한 생산 중단 시간을 줄이는 데 도움이 될 수 있습니다. 위생 관리는 세척 방식 하나로 완결되지 않으므로, 현장의 위생 절차와 함께 적용 여부를 검토합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>오븐 · 로스터 · 프루퍼</li><li>믹서 · 블렌더 · 슬라이서</li><li>컨베이어 · 체인</li><li>포장설비 · 라벨링 설비</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>탄화 식품 · 유지 · 단백질 잔류물 · 반죽 · 시럽 · 접착제 · 라벨 잔류물</p></div>
      <a class="auto-rel-link" href="../industries/food-beverage.html"><span>관련 산업</span>식품 · 음료 <i>→</i></a>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">PRINTING & PACKAGING EQUIPMENT</span>
      <h3>인쇄 · 포장설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/printing-cleaning-ink-try-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">정밀한 인쇄 · 포장 부품에 축적된<br>잉크와 접착제를 관리합니다.</p>
      <div class="cmp-text auto-text"><p>인쇄 현장은 굳은 잉크와 눌어붙은 종이분진, 그리스와 접착제가 세척 시간과 비용을 늘리는 대표적인 현장입니다. 롤러와 실린더, 그리퍼와 피더, UV 드라이어처럼 정밀하고 손상되기 쉬운 부품이 많아 세척 방법 선택에 주의가 필요합니다.</p><p>드라이아이스 세척은 비마모성 방식이어서 롤러 표면과 정밀 부품의 상태를 고려하면서 잉크·접착제를 제거하는 데 활용됩니다. 설비를 거의 분해하지 않고 세척할 수 있는 경우가 있어 세척 서비스의 소요 시간을 줄이는 데 도움이 될 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>롤러 · 실린더 · 인쇄판 주변</li><li>그리퍼 · 피더 · 가이드</li><li>UV 드라이어 · 급지 시스템</li><li>포장설비 · 라벨링 장비</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>잉크 · 바니시 · 접착제 · 종이분진 · 오일 · 그리스</p></div>
      <a class="auto-rel-link" href="../industries/printing.html"><span>관련 산업</span>인쇄 <i>→</i></a>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">POWER & HEAVY INDUSTRIAL EQUIPMENT</span>
      <h3>발전 · 에너지 · 중공업 설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/power-generation-cleaning-metallic-fins-on-steam-turbine-rotor-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/oil-gas-hilcorp-removing-atmospheric-contamination-from-fin-fans.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">대형 설비의 유지보수 과정에서<br>축적된 고착 오염물을 관리합니다.</p>
      <div class="cmp-text auto-text"><p>발전소와 석유·가스 플랜트에서는 터빈과 발전기, 열교환기와 펌프 같은 대형 설비의 정기 세척·정비를 외부 전문업체에 맡기는 경우가 많습니다. 오일과 그리스, 카본과 공정 잔류물이 두껍게 고착되어 있고, 분해와 냉각에 긴 시간이 걸리는 설비입니다.</p><p>드라이아이스 세척은 건식·비마모성 방식으로 설비를 제자리에서 세척하는 데 활용되어 정비 시간을 줄이는 데 도움이 될 수 있습니다. 전기설비의 경우 드라이아이스가 비전도성이라는 이유로 통전 상태 작업을 일반화하지 않습니다 — 전원 상태, 설비 구조, 작업환경과 안전 조건을 별도로 확인한 뒤 판단합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>터빈 · 발전기</li><li>열교환기 · 핀팬 · 라디에이터</li><li>펌프 · 회전기기</li><li>대형 기계설비</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>오일 · 그리스 · 카본 · 공정 잔류물 · 분진</p></div>
      <a class="auto-rel-link" href="../industries/power-generation.html"><span>관련 산업</span>발전 · 전력 <i>→</i></a>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">RESTORATION & SPECIALTY CLEANING</span>
      <h3>복원 · 특수 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/vatek-field-artifact-machinery-cleaning-graded.png" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/vatek-field-heritage-locomotive-cleaning-graded.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">산업설비를 넘어,<br>표면 보호가 중요한 복원 작업에도 활용됩니다.</p>
      <div class="cmp-text auto-text"><p>바테크는 국내에서 동상과 야외 전시 유물, 증기기관차 같은 대형 문화재의 표면 오염물을 드라이아이스로 세척한 현장 경험을 가지고 있습니다. Cold Jet은 전문 세척업체의 작업 영역으로 화재·연기 복원, 곰팡이 제거, 수해 복원, 역사적 건축물 복원, 클래식카 복원을 함께 소개합니다. 서로 다른 현장이지만, 복원 대상의 원래 표면을 보존하면서 오염물을 제거해야 한다는 조건은 같습니다.</p><p>드라이아이스 세척은 연마재와 수분을 더하지 않는 방식이어서 목재·석재·구조물처럼 표면 상태를 고려해야 하는 복원 작업에 활용됩니다. 각 분야의 세부 내용은 아래 별도 페이지에서 다룹니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>화재 · 수해 복원</li><li>곰팡이 제거</li><li>역사적 건축물 · 문화재 복원</li><li>자동차 복원 · 디테일링</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>그을음 · 연기 잔류물 · 탄화물 · 곰팡이 · 생물성 침착물 · 오래된 도막</p></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">전문 세척에서는<br>한 가지 오염물만 다루지 않습니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/printing-dry-ice-blasting-removes-heavy-ink-and-grease-buildup-from-printing-press.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 · 그리스</b><small>OIL & GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/oil-gas-cleaning-heavy-carbon-buildup.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 · 탄화 잔류물</b><small>CARBONIZED RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/printing-cleaning-burnished-ink-from-flexible-packaging-equipment-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>잉크 · 도료</b><small>INK & PAINT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/food-beverage-removing-labels-and-adhesive-from-rolling-conveyor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제 · 라벨</b><small>ADHESIVE & LABELS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>수지 · 폴리머</b><small>RESIN & POLYMER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/food-beverage-dough-carbon-and-grease-removed-from-food-mixer.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>식품 · 유지 잔류물</b><small>FOOD & FAT RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/rail-removing-asphalt-from-freight-car-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>아스팔트 · 타르</b><small>ASPHALT & TAR</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/contract-fire-restoration.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>그을음 · 연기 잔류물</b><small>SOOT & SMOKE RESIDUE</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">세척하는 시간뿐 아니라,<br>작업 전후에 필요한 과정까지 함께 봐야 합니다.</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>물을 사용하지 않는 건식 세척</b><p>물과 세정제, 용제를 쓰지 않는 방식이므로 세척 후 별도의 건조 과정이 필요한 작업을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>비마모성 세척 방식</b><p>모래나 금속 입자로 표면을 연마하는 방식이 아닙니다. 세척 대상의 표면 상태를 고려해야 하는 작업에 활용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스 입자는 충돌 후 승화하므로 모래·비드처럼 분사한 매체 자체는 현장에 남지 않습니다. 단, 제거된 오염물은 남을 수 있어 필요에 따라 회수와 처리가 필요합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>현장 세척 가능성</b><p>대상과 조건에 따라 설비를 완전히 분리하지 않고 세척할 수 있는 경우가 있어, 분해·재조립에 필요한 작업시간을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>다양한 세척 조건 설정</b><p>입자 크기, 분사 압력, 드라이아이스 공급량, 노즐, 분사 거리와 각도를 조정하여 서로 다른 오염물과 설비에 대응할 수 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="auto-feature is-nofig">
    <div class="wrap auto-feature-body reveal">
      <span class="cmp-eyebrow">MORE THAN CLEANING POWER</span>
      <h2 class="cmp-h2">전문 세척에서는<br>세척력만으로 작업 방법을 결정할 수 없습니다.</h2>
      <p class="cmp-lead-p">실제 현장에서는 오염물을 얼마나 빨리 제거하는지만으로 작업 방법을 선택하기 어렵습니다. 세척 대상의 표면 상태와 재질, 작업공간, 설비의 분해 여부, 주변 설비에 미치는 영향, 세척 후 처리, 작업시간을 함께 고려해야 합니다.</p>
      <p class="auto-feature-key">좋은 세척 방법은<br>오염물뿐 아니라 <em>작업 전체</em>를 함께 봅니다.</p>
    </div>
  </section>
  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 장비라도,<br>작업 대상에 따라 세척 조건은 달라집니다.</h2>
          <div class="cmp-dark-body">
            <p>인쇄기에 쌓인 잉크와 식품설비의 탄화 잔류물, 산업설비의 오일과 그리스는 같은 조건으로 세척할 수 없습니다. 오염물의 종류와 두께, 부착 정도, 세척 대상의 재질과 형상, 작업공간과 접근성에 따라 필요한 입자 크기, 분사 압력, 드라이아이스 공급량, 노즐과 작업 방법도 달라집니다.</p>
            <p>바테크는 실제 세척 대상과 오염물의 상태를 확인한 뒤 세척 테스트를 통해 적절한 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/food-beverage-cleaning-oil-residue-from-fryers-and-cookers.webp" alt="" loading="lazy" /><b>FOOD EQUIPMENT</b><small>탄화 잔류물 · 유지</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/printing-dry-ice-blasting-removing-burnished-ink-and-adhesive-from-packaging-line.webp" alt="" loading="lazy" /><b>PRINTING PRESS</b><small>잉크 · 접착제</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/oil-gas-dry-ice-blasting-removing-carbon-buildup.webp" alt="" loading="lazy" /><b>INDUSTRIAL EQUIPMENT</b><small>오일 · 그리스 · 고착 오염</small></li>
          </ul>
          <p class="auto-ae-key">전문 세척에서는 장비의 성능만큼<br><em>현장에 맞는 조건을 설정하는 경험</em>이 중요합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">전문 세척 서비스에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">전문 세척업체가 고객 현장에서 자주 만나는 작업 유형입니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.35s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">ACROSS INDUSTRIES</span>
      <h2 class="cmp-h2">전문 세척 서비스는<br>다양한 산업현장과 연결됩니다.</h2>
    </div>
    <p class="cmp-lead-p">전문 세척업체의 고객 현장은 특정 산업에 머물지 않습니다. 각 산업 페이지에서 설비별 세척 과제를 확인할 수 있습니다.</p>
  </div>
  <ul class="auto-relind is-grid">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/food-beverage.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-food.png" alt="" loading="lazy" /></span><small>FOOD & BEVERAGE</small><b>식품 · 음료</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/printing.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /></span><small>PRINTING</small><b>인쇄</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.30s"><a href="../industries/power-generation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></span><small>POWER GENERATION</small><b>발전 · 전력</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.40s"><a href="../industries/oil-gas.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-oilgas.png" alt="" loading="lazy" /></span><small>OIL & GAS</small><b>오일 · 가스</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.50s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.60s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.70s"><a href="../industries/rail.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-transit.png" alt="" loading="lazy" /></span><small>RAIL & PUBLIC TRANSPORTATION</small><b>철도 · 대중교통</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-bridge-sec">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">SPECIALIZED CLEANING & RESTORATION</span>
    <h2 class="cmp-h2">일반 산업세척을 넘어,<br>전문적인 복원 작업에도 활용됩니다.</h2>
  </div>
  <ul class="auto-bridge">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/industry.html#ind-special" data-target="../industries/restoration.html"><span class="auto-bridge-img"><img src="../assets/img/contract-fire-restoration.jpg" alt="" loading="lazy" /></span><small>FIRE & WATER RESTORATION</small><b>화재 · 수해 복원</b><p>그을음과 연기 잔류물, 수해 이후 오염된 표면과 구조물을 세척·복원하는 분야.</p><span class="auto-bridge-more">화재 · 수해 복원 자세히 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../cleaning/industry.html#ind-special" data-target="../industries/mold-remediation.html"><span class="auto-bridge-img"><img src="../assets/img/contract-mold-remediation-attic.jpg" alt="" loading="lazy" /></span><small>MOLD REMEDIATION</small><b>곰팡이 제거</b><p>목재와 구조물 등에 발생한 곰팡이 오염을 물리적으로 제거하는 작업.</p><span class="auto-bridge-more">곰팡이 제거 자세히 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../cleaning/industry.html#ind-special" data-target="../industries/historical-restoration.html"><span class="auto-bridge-img"><img src="../assets/img/vatek-field-statue-cleaning-graded.png" alt="" loading="lazy" /></span><small>HISTORICAL RESTORATION</small><b>역사적 건축물 · 문화재 복원</b><p>목재, 석재 및 오래된 건축 요소처럼 표면 상태를 고려해야 하는 복원 세척 분야.</p><span class="auto-bridge-more">역사적 건축물 · 문화재 복원 자세히 보기 →</span></a></li>
  </ul>
</div>
<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">CONTRACT CLEANING IN THE FIELD</span>
      <h2 class="cmp-h2">서로 다른 현장에서 확인된<br>전문 세척 적용 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 자료와 블로그에 소개된 전문 세척업체의 적용 사례입니다. 수치는 해당 현장의 조건에서 확인된 결과이며, 일반적인 효과로 확대 해석하지 않습니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 드라이아이스 세척을 사용하는 전문 세척 서비스 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:62%"><img src="../assets/img/logo-robotworx.png" alt="RobotWorx" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:44%"><img src="../assets/img/logo-uscleanblast.png" alt="USCleanBlast" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:44%"><img src="../assets/img/logo-bonazza.png" alt="Bonazza Dry Ice Blasting" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:22%"><img src="../assets/img/logo-adrian-environmental.png" alt="Adrian Environmental" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:30%"><img src="../assets/img/logo-us-flood-team.png" alt="U.S. Flood Team" loading="lazy" /></li>
  </ul>
  <ul class="mtc-cases auto-field-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>INDUSTRIAL CLEANING</small><b>산업설비 · 상업용 주방 전문 세척</b><span>Industrial Cleaning Solutions (미국 미주리)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>진공 탱크·배관, 라디에이터, 열교환기, 상업·산업용 주방설비</dd></div>
        <div><dt>오염물</dt><dd>공정 잔류물 · 유지 · 고착 오염물</dd></div>
        <div><dt>특징</dt><dd>스테인리스·아연도금·도장강판 등 재질이 다른 설비를 한 장비로 대응, 도장·코팅 전 표면 전처리도 수행</dd></div>
        <div><dt>적용</dt><dd>현장 상황에 맞춰 분사 조건을 바꾸며 드라이아이스 세척 서비스 제공</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>다양한 재질과 현장에 하나의 세척 방식으로 대응한 사례로 Cold Jet 블로그에 소개 (Contractor of the Month)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>FIRE RESTORATION</small><b>화재 복원 · 탄화 목재 제거</b><span>Advanced Indoor Air Quality Care</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>화재 피해 건물의 구조 목재</dd></div>
        <div><dt>오염물</dt><dd>탄화 목재 · 카본 · 연기 냄새의 원인 잔류물</dd></div>
        <div><dt>기존 방식</dt><dd>샌딩·소다 블라스팅 — 작업기간과 인력, 2차 폐기물 부담</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 블라스터 3대, 작업자 8명, 약 8일 작업</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>대체 방식 견적의 약 절반 기간에 완료. 냄새 원인 잔류물이 제거되어 코팅·탈취제 사용을 최소화했다고 보고 (해당 현장 기준)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.20s">
      <div class="mtc-case-head"><small>HISTORICAL RESTORATION</small><b>기념물 복원 세척</b><span>USCleanBlast.com</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>세부 장식이 있는 역사적 기념물</dd></div>
        <div><dt>오염물</dt><dd>오염 · 생물성 침착물</dd></div>
        <div><dt>기존 방식</dt><dd>설계자가 처음 요구한 소다 블라스팅 — 2차 폐기물 격리·수거 비용</dd></div>
        <div><dt>적용</dt><dd>비마모성 드라이아이스 세척으로 세부 형상을 보존하며 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>세정 매체 폐기물이 남지 않아 격리 설비 없이 작업, 소다 블라스팅 대비 비용을 크게 줄였다고 보고 (사용자 인용)</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">새로운 세척 작업을<br>검토하고 계신가요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>전문 세척 현장은 작업 대상과 오염물, 재질과 작업환경이 매번 다릅니다.</p>
      <p>바테크는 실제 세척 대상 또는 샘플을 이용한 테스트를 통해 드라이아이스 세척의 적용 가능성과 필요한 작업 조건을 확인합니다. 장비 도입뿐 아니라 렌탈과 현장 지원도 함께 검토할 수 있습니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 현장의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

# (2026-09-08, 11차 핸드오프 batch2) 산업 상세 5종 + 작업별 상세 3종 — 본문은 핸드오프 HTML이 정본
# (히어로 앞 출처 주석부터 "함께 보면 좋은 페이지"까지 통째).
FACILITY_MAINTENANCE_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/applications/facility-maintenance/ (+ Cold Jet Facility Maintenance 컷시트 #004312162024, resources/motor-techniques-inc, industries/contract-cleaning 고객 인용). 생산설비 실사진: 바테크 제공 Volpak 포장기 세척 현장 (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/facility-volpak-machine-cleaning.webp" aria-label="생산설비 · 시설 유지보수 현장">
      <source src="../assets/video/facility-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 생산설비 · 시설 유지보수</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">FACILITY MAINTENANCE</span>
      <h1>생산설비 · 시설 유지보수</h1>
      <p class="cmp-hero-p auto-hero-lead">설비는 멈춰 있을 때보다,<br>가동되는 동안 더 빠르게 오염됩니다.</p>
      <p class="cmp-hero-p auto-hero-body">컨베이어와 로봇, 모터와 제어반, 냉각설비와 배관, 물류장비까지 — 운전이 반복될수록 오일과 그리스, 분진, 도료·수지와 공정 잔류물이 쌓입니다. 드라이아이스 세척은 물과 연마재를 사용하지 않는 건식·비마모성 방식으로, 설비의 구조와 오염 상태를 고려하면서 현장 유지보수 세척에 활용할 수 있습니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">KEEP EQUIPMENT CLEAN</span>
      <h2 class="cmp-h2">설비의 오염은<br>외관만의 문제가 아닙니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>생산설비에 먼지와 오일, 그리스와 공정 잔류물이 계속 쌓이면 점검해야 할 부위를 가리고, 냉각과 통풍을 방해하거나, 움직이는 부품과 센서 주변의 관리 부담을 높일 수 있습니다.</p>
      <p>하지만 설비를 세척하기 위해 매번 장시간 생산을 중단하고, 분해하고, 세척 후 다시 건조·조립하는 것도 현장에는 큰 부담입니다. 그래서 세척은 자주 미뤄지고, 오염은 그동안 계속 쌓입니다.</p>
      <p>따라서 설비 유지보수에서는 단순히 "얼마나 깨끗하게 닦이는가"보다 "어떻게 세척하고, 얼마나 분해해야 하며, 언제 다시 설비를 사용할 수 있는가"까지 함께 고려하는 것이 중요합니다.</p>
      <p class="auto-intro-close">설비 세척은 청소가 아니라 <b>유지보수의 한 과정</b>입니다.</p>
    </div>
  </div>
  <figure class="auto-intro-fig reveal"><img src="../assets/img/facility-volpak-machine-cleaning.webp" alt="" loading="lazy" /></figure>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">FACILITY MAINTENANCE APPLICATIONS</span>
    <h2 class="cmp-h2">공장 안에서 세척해야 할 대상은<br>생각보다 훨씬 많습니다.</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">PRODUCTION EQUIPMENT & AUTOMATION</span>
      <h3>생산설비 · 자동화설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/facility-volpak-machine-cleaning.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/facility-maintenance-dry-ice-blasting-removing-overspray-from-robotic-arm.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">생산라인 곳곳에 쌓이는 오염물을<br>설비 구조에 맞춰 세척합니다.</p>
      <div class="cmp-text auto-text"><p>생산설비와 자동화설비에는 공정이 반복되면서 오일과 그리스, 도료 비산 잔류물, 수지, 접착제와 각종 생산 잔류물이 쌓입니다. 사진의 포장기처럼 제품 잔류물이 이송부와 성형부 사이에 눌어붙으면 손이 닿지 않는 부위부터 관리가 어려워집니다.</p><p>드라이아이스 세척은 설비를 연마하는 방식이 아니며, 노즐과 분사 조건을 조절해 복잡한 기계 구조와 좁은 부위의 세척에 활용할 수 있습니다. Cold Jet 자료에 따르면 로봇의 경우 센서·배선·정밀 구동부 주변의 용접 스패터와 도료 비산 잔류물을 제거하는 데 사용됩니다.</p><p>적용 조건에 따라 설비를 완전히 분해하지 않고 현장에서 세척할 수 있는 경우도 있어, 분해·재조립에 드는 정비시간을 줄이는 데 도움이 될 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>생산기계 · 성형부 · 이송부</li><li>산업용 로봇 · 관절부 · End-of-arm tooling</li><li>컨베이어 벨트 · 체인 · 롤러 · 가이드레일</li><li>구동부 · 센서 하우징 · 케이블 하니스</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>오일 · 그리스 · 도료 비산 잔류물 · 수지 · 접착제 · 용접 스패터 · 생산 잔류물</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">ELECTRICAL SYSTEMS & MOTORS</span>
      <h3>모터 · 전기 · 제어설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/facility-maintenance-cleaning-electric-motor-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/facility-maintenance-dry-ice-blasting-cleaning-motor-controller-panel.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">물을 사용하기 어려운<br>전기 · 제어설비의 세척을 검토할 수 있습니다.</p>
      <div class="cmp-text auto-text"><p>전동기와 제어반에는 먼지, 오일 미스트, 카본, 미세 분진과 주변 공정에서 발생한 오염물이 축적됩니다. 권선과 통풍구, 냉각팬에 쌓인 오염은 열을 가두고, 단자와 버스바 주변의 오염은 점검을 어렵게 합니다.</p><p>드라이아이스는 물을 사용하는 세척 방식이 아니며, 전기적으로 비전도성인 특성이 있습니다. Cold Jet 자료는 이 특성을 바탕으로 모터 권선·스테이터 슬롯, 전기 박스와 단자함, PLC·HMI 캐비닛과 MCC 세척에 드라이아이스를 사용한다고 소개합니다.</p><p>단, 비전도성이라는 이유로 "전원이 켜진 상태에서 모든 전기설비를 세척할 수 있다"고 일반화하지 않습니다. 실제 적용 여부는 전원 상태, 설비 구조, 제조사 기준, 절연 상태와 노후도, 현장 안전조건을 확인한 뒤 판단해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>전동기 · 권선 · 스테이터 · 발전기</li><li>전기 박스 · 단자함 · 정션박스 · 스위치기어</li><li>제어반 · MCC · PLC · HMI 캐비닛 · VFD</li><li>제어반 냉각팬 · 통풍구</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>먼지 · 오일 미스트 · 카본 · 미세 분진 · 공정 오염물</p></div>
      <p class="auto-note">전기·제어설비 세척은 전원 차단 여부와 안전 절차를 현장 기준에 따라 별도로 확인합니다.</p>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">COOLING & PROCESS SUPPORT SYSTEMS</span>
      <h3>냉각 · 열교환 · 유체설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/facility-maintenance-cleaning-cooling-fan-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/facility-maintenance-cleaning-pipe-in-food-facility-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">열을 식히고 유체를 이동시키는 설비도<br>오염이 쌓이면 관리가 필요합니다.</p>
      <div class="cmp-text auto-text"><p>냉각팬과 열교환기, 배관과 유체설비에는 먼지, 오일, 그리스, 공정 잔류물이 축적됩니다. 특히 열교환기와 냉각팬은 핀과 통풍구에 오염물이 쌓이면 공기의 흐름과 열교환 상태에 영향을 줄 수 있고, 배관 외부의 오염은 누유와 부식을 육안으로 확인하기 어렵게 만듭니다.</p><p>Cold Jet 자료에 따르면 드라이아이스 세척은 고압 세척과 달리 얇은 핀을 휘게 하지 않으면서 핀 사이의 오염물을 제거하는 데 사용되고, 배관·피팅 외부에서는 가스켓과 표면 상태를 고려하면서 오염물을 제거하는 데 활용됩니다. 세척 후 표면에 수분이 남지 않아 세척 자체가 부식을 부르는 상황을 줄이는 데도 도움이 될 수 있습니다.</p><p>"효율을 원래대로 복구한다"고 단정하지는 않습니다. 오염물을 제거해 원래의 통풍과 열교환 상태를 유지하는 데 도움이 될 수 있다는 것이 정확한 표현입니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>냉각팬 · 팬 블레이드 · 환기설비</li><li>열교환기 핀 · 핀팬 쿨러 · 증발기 · 응축기 코일</li><li>배관 · 플랜지 · 호스 · 피팅 · 행거</li><li>유압 부품 · 스팀 · 압축공기 라인</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>먼지 · 오일 · 그리스 · 공정 잔류물 · 외부 부식</p></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">FACILITY INFRASTRUCTURE & MATERIAL HANDLING</span>
      <h3>공장 인프라 · 물류장비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/facility-maintenance-dry-ice-blasting-cleaning-walls-and-ceilings-at-manufacturing-plant.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/facility-maintenance-cleaning-forklift-in-food-facility-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">생산기계뿐 아니라<br>공장 전체가 유지보수의 대상입니다.</p>
      <div class="cmp-text auto-text"><p>공장 천장과 벽, 철골 빔과 기둥, 캣워크와 배관 외부, 지게차와 운반장비에도 먼지, 오일, 그리스와 각종 오염물이 축적됩니다. 넓은 면적과 높은 위치, 복잡한 구조 때문에 수작업으로 관리하기 어려운 부위가 많고, 그래서 정기 점검이나 감사 때 지적되는 항목이기도 합니다.</p><p>드라이아이스 세척은 이러한 공장 인프라와 물류장비를 현장에서 관리하는 방법으로 활용할 수 있습니다. Cold Jet 자료는 천장·빔·기둥의 먼지와 느슨한 도막 조각 제거, 지게차의 체인·유압 피팅·리프트 실린더·엔진룸 세척을 예로 들고 있으며, 분사 매체가 남지 않아 상부 구조물 세척 후 별도의 매체 수거가 필요하지 않다는 점을 특징으로 소개합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>천장 · 벽 · 철골 빔 · 기둥 · 캣워크</li><li>배관 외부 · 컨듀잇 · 천장 팬</li><li>지게차 · 팔레트 잭 · 시저 리프트</li><li>물류 · 운반장비의 체인 · 유압부 · 휠 어셈블리</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>먼지 · 오일 · 그리스 · 느슨한 도막 · 생산 잔류물</p></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first auto-tgrid-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">ACROSS THE FACILITY</span>
      <h2 class="cmp-h2">생산설비부터 공장 인프라까지,<br>관리해야 할 대상은 계속 이어집니다.</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet Facility Maintenance 자료가 제시하는 대표 적용 대상입니다. 각 사진은 해당 설비를 실제로 세척하는 장면입니다.</p>
  </div>
  <ul class="auto-cont is-4 auto-tgrid" aria-label="대표 세척 대상">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/facility-volpak-machine-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>생산설비</b><small>PRODUCTION EQUIPMENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/facility-maintenance-dry-ice-blasting-removing-overspray-from-robotic-arm.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>산업용 로봇</b><small>INDUSTRIAL ROBOTICS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/facility-maintenance-cleaning-conveyor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>컨베이어</b><small>CONVEYORS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/facility-maintenance-cleaning-electric-motor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>모터 · 발전기</b><small>MOTORS & GENERATORS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/facility-maintenance-cleaning-electrical-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>전기 · 제어반</b><small>ELECTRICAL & CONTROL PANELS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/facility-maintenance-cleaning-cooling-fan-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>열교환기 · 냉각설비</b><small>COOLING & HEAT EXCHANGE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/facility-maintenance-cleaning-pipe-in-food-facility-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>배관 · 공장 인프라</b><small>PIPES & FACILITY INFRASTRUCTURE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/facility-maintenance-cleaning-forklift-in-food-facility-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>물류 · 운반장비</b><small>MATERIAL HANDLING</small></span></li>
  </ul>
</div>
<div class="cmp-section auto-cont-after-tgrid">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">설비가 다르면,<br>쌓이는 오염물도 다릅니다.</h2>
  <ul class="auto-cont is-4" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 · 그리스</b><small>OIL & GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/engineered-wood-kiln-fan-cleaning-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>먼지 · 산업분진</b><small>DUST & INDUSTRIAL DEBRIS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/oil-gas-cleaning-heavy-carbon-buildup.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 · 그을음</b><small>CARBON & SOOT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/facility-maintenance-dry-ice-blasting-removing-overspray-from-robotic-arm.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>도료 비산 잔류물</b><small>PAINT OVERSPRAY</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/engineered-wood-adhesive-and-resin-buildup-removed-from-production-surfaces-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>수지 · 폴리머</b><small>RESIN & POLYMER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제</b><small>ADHESIVE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>용접 스패터</b><small>WELD SPATTER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/textiles-removing-hardened-dye-and-fiber-fly-from-conveyor-slats-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>고착 공정 잔류물</b><small>PROCESS BUILDUP</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">세척하는 시간뿐 아니라,<br>설비가 멈춰 있는 시간까지 함께 봐야 합니다.</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>현장 세척 가능성</b><p>적용 대상과 작업 조건에 따라 설비를 완전히 분해하지 않고 세척할 수 있는 경우가 있습니다. 분해·재조립 작업을 줄이면 정비시간을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>물을 사용하지 않는 건식 세척</b><p>물과 세정제를 쓰지 않는 방식이므로 세척 후 별도의 건조가 필요한 작업을 줄이는 데 도움이 될 수 있습니다. 수분을 피해야 하는 설비 주변에서도 검토할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>비마모성 방식</b><p>연마재를 분사해 표면을 깎아내는 방식이 아닙니다. 기계부품과 정밀한 표면, 일부 전기·전자설비에 적용을 검토할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스 입자는 충돌 후 승화합니다. 따라서 모래나 비드 같은 분사 매체 자체는 설비 주변에 남지 않습니다. 단, 제거된 오염물 자체는 남을 수 있으므로 필요에 따라 별도의 회수와 처리가 필요합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>좁고 복잡한 구조 접근</b><p>적절한 노즐과 분사 조건을 이용해 롤러 사이, 로봇 관절, 모터 통풍부, 배관·피팅 주변, 복잡한 기계 구조에 접근할 수 있습니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="auto-feature is-nofig">
    <div class="wrap auto-feature-body reveal">
      <span class="cmp-eyebrow">MAINTENANCE BEYOND CLEANING</span>
      <h2 class="cmp-h2">깨끗한 설비는,<br>상태를 확인하기 쉬운 설비이기도 합니다.</h2>
      <p class="cmp-lead-p">오일과 먼지가 두껍게 쌓인 설비에서는 작은 누유, 균열, 배선 상태, 체결부, 표면 부식, 부품의 이상을 육안으로 확인하기 어렵습니다. 세척이 설비의 문제를 직접 수리하는 작업은 아닙니다. 하지만 오염물을 제거하면 설비의 상태를 확인하고 정비가 필요한 부분을 발견하기 쉬운 환경을 만드는 데 도움이 됩니다. Cold Jet은 이런 이유로 드라이아이스 세척을 TPM(전사적 설비보전) 활동을 지원하는 수단으로 소개합니다.</p>
      <div class="auto-feature-cols">
        <div class="reveal" style="--reveal-delay:0.20s"><small>세척 후 확인이 쉬워지는 것</small><ul><li>배관·피팅·플랜지의 누유 흔적</li><li>전동기·베어링 하우징의 발열 부위</li><li>제어반 단자·버스바의 변색과 오염</li><li>철골·배관 외부의 부식 진행 상태</li><li>체결부 풀림 · 균열 · 마모 흔적</li></ul></div>
        <div class="reveal" style="--reveal-delay:0.32s"><small>유지보수 관점에서의 의미</small><ul><li>점검 포인트가 드러나 예방정비 계획에 반영할 수 있습니다</li><li>냉각·통풍 부위의 오염을 줄여 원래 상태 유지에 도움이 됩니다</li><li>정기 점검·감사에서 지적되는 항목을 미리 관리할 수 있습니다</li><li>세척 주기를 짧게 가져갈 수 있는 경우 오염이 두껍게 고착되기 전에 관리할 수 있습니다</li></ul></div>
      </div>
      <p class="auto-feature-key">설비 세척은 단순한 청소가 아니라<br><em>예방정비와 상태점검을 지원하는</em> 유지보수 과정의 하나입니다.</p>
    </div>
  </section>
  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 공장 안에서도,<br>세척 조건은 모두 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>전동기의 먼지와 오일, 로봇의 도료와 공정 잔류물, 컨베이어의 그리스와 접착제, 열교환기의 분진은 같은 조건으로 세척할 수 없습니다. 설비의 재질과 구조, 오염물의 종류와 부착 정도, 주변 부품, 작업공간, 안전조건에 따라 필요한 세척 조건도 달라집니다.</p>
            <p>바테크는 실제 설비와 오염 상태를 확인하고 세척 테스트를 통해 드라이아이스 입자 크기, 분사 압력, 드라이아이스 공급량, 노즐, 분사 거리와 각도를 조정해 적절한 세척 조건을 확인합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases is-4">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/facility-maintenance-cleaning-electric-motor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>ELECTRIC MOTOR</b><small>먼지 · 오일 → 권선과 절연체 상태를 고려</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/facility-maintenance-dry-ice-blasting-removing-overspray-from-robotic-arm.webp" alt="" loading="lazy" /><b>INDUSTRIAL ROBOT</b><small>도료 · 공정 잔류물 → 관절부와 센서 · 배선 고려</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/facility-maintenance-cleaning-conveyor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>CONVEYOR</b><small>오일 · 접착제 → 넓은 면적과 구동부 고려</small></li>
            <li class="reveal" style="--reveal-delay:0.72s"><img src="../assets/img/oil-gas-hilcorp-removing-atmospheric-contamination-from-fin-fans.webp" alt="" loading="lazy" /><b>HEAT EXCHANGER</b><small>분진 · 고착 오염 → 얇은 핀과 구조 고려</small></li>
          </ul>
          <p class="auto-ae-key">설비 이름보다,<br><em>실제 오염 상태와 작업 조건</em>을 먼저 봅니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">생산설비 · 시설 유지보수에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">설비 유지보수 현장에서 자주 함께 검토되는 작업 유형입니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/adhesive-resin-removal.html"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ADHESIVE & RESIN REMOVAL</small><b>접착제 · 수지 제거</b><span>롤러·노즐·지그·금형에 쌓이는 접착제와 수지</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/weld-fixture-robot.html"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>WELD LINE, FIXTURE & ROBOT CLEANING</small><b>용접라인 · 지그 · 로봇 세척</b><span>지그·클램프·로봇·센서 주변의 스패터와 슬래그</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.28s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/paint-booth-coating-line.html"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PAINT BOOTH & COATING LINE CLEANING</small><b>도장부스 · 코팅라인 세척</b><span>부스·행거·캐리어·컨베이어의 도료 비산 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.35s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/rust-corrosion-removal.html"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>RUST, CORROSION & OXIDATION REMOVAL</small><b>녹 · 부식 · 산화물 제거</b><span>표면 녹과 느슨한 산화물(비마모 범위 내)</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">ACROSS INDUSTRIES</span>
      <h2 class="cmp-h2">시설 유지보수는<br>특정 산업에만 필요한 작업이 아닙니다.</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet은 아래 산업의 설비보전 조직에서 시설 유지보수 세척이 이루어지고 있다고 소개합니다. 각 산업 페이지에서 설비별 세척 과제를 확인할 수 있습니다.</p>
  </div>
  <ul class="auto-relind is-grid">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/semiconductor.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-semiconductor.png" alt="" loading="lazy" /></span><small>SEMICONDUCTOR & ELECTRONICS</small><b>반도체 · 전자 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/food-beverage.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-food.png" alt="" loading="lazy" /></span><small>FOOD & BEVERAGE</small><b>식품 · 음료</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.30s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS & COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.40s"><a href="../industries/rubber-tires.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-rubber-tire.png" alt="" loading="lazy" /></span><small>RUBBER & TIRES</small><b>고무 · 타이어</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.50s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.60s"><a href="../industries/printing.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /></span><small>PRINTING</small><b>인쇄</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.70s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE & AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.80s"><a href="../industries/power-generation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></span><small>POWER GENERATION</small><b>발전 · 전력</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.90s"><a href="../industries/oil-gas.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-oilgas.png" alt="" loading="lazy" /></span><small>OIL & GAS</small><b>오일 · 가스</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">FACILITY MAINTENANCE IN PRACTICE</span>
      <h2 class="cmp-h2">생산현장에서 확인된<br>설비 유지보수 세척 사례</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 Facility Maintenance 페이지에 소개된 고객사와 공식 사례 자료입니다. 수치는 해당 현장의 조건에서 확인된 결과이며, 일반적인 효과로 확대 해석하지 않습니다.</p>
  </div>
  <ul class="auto-logos is-flex is-blend" aria-label="Cold Jet 드라이아이스 세척을 사용하는 생산설비 · 시설 유지보수 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:40%"><img src="../assets/img/facility-maintenance-3m.jpg" alt="3M" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:36%"><img src="../assets/img/logo-bmw.webp" alt="BMW" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:66%"><img src="../assets/img/facility-maintenance-boeing.webp" alt="Boeing" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:72%"><img src="../assets/img/facility-maintenance-caterpillar-logo.jpg" alt="Caterpillar" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:66%"><img src="../assets/img/facility-maintenance-coca-cola_logo.webp" alt="Coca-Cola" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:58%"><img src="../assets/img/logo-ford.webp" alt="Ford" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:40%"><img src="../assets/img/logo-gm.webp" alt="General Motors" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:84%"><img src="../assets/img/facility-maintenance-logo-kimberly-clark.webp" alt="Kimberly-Clark" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.32s; --w:48%"><img src="../assets/img/facility-maintenance-p_and_g_procter_and_gamble_logo.webp" alt="P&G" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.36s; --w:58%"><img src="../assets/img/facility-maintenance-nestle_logo.webp" alt="Nestlé" loading="lazy" /></li>
  </ul>
  <ul class="mtc-cases auto-field-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>ELECTRIC MOTORS</small><b>전동기 세척과 에너지 관리</b><span>Conservation Solutions / Motor Techniques (미국, Cold Jet 공식 사례)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>산업용 전동기 (권선 · 모터 캡 내부)</dd></div>
        <div><dt>오염물</dt><dd>장기간 세척되지 않아 약 5cm 두께로 쌓인 표면 오염물</dd></div>
        <div><dt>기존 문제</dt><dd>정기 세척 없이 운전되어 오염이 고착, 수작업으로는 분해와 장시간 작업이 필요</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척으로 표면 오염물을 제거한 뒤 캡 내부 고착물은 수공구로 마무리</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>전동기 시스템 진단 업체가 대체 방식 대비 전력 사용과 작업 인시 양쪽에서 비용 절감을 확인했다고 보고. Cold Jet은 이 사례를 "에너지 비용 30~40% 절감"으로 소개하지만, 해당 현장의 오염 상태에서 얻은 결과입니다.</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>CONVEYOR CHAIN</small><b>약 90m 이송 체인 세척</b><span>제조업체 고객 인용 (Cold Jet 공식 페이지)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>부품을 공장 전체로 이송하는 약 300ft(90m) 드로우 체인</dd></div>
        <div><dt>오염물</dt><dd>이송 중 체인에 쌓이는 먼지 · 이물질</dd></div>
        <div><dt>기존 방식</dt><dd>작업자 3명이 약 4시간 수작업 세척</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척으로 체인을 제자리에서 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>같은 작업을 작업자 1명이 약 30분에 완료했다고 보고. 이후 같은 장비를 공장 내 다른 설비 세척에도 확대 적용 (해당 현장 기준)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.20s">
      <div class="mtc-case-head"><small>FIN FAN COOLERS</small><b>핀팬 쿨러 대기 오염물 제거</b><span>Hilcorp (Cold Jet Oil & Gas 공식 자료)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>열교환기 핀팬 쿨러</dd></div>
        <div><dt>오염물</dt><dd>대기 중 먼지 · 오염물이 핀 사이에 축적</dd></div>
        <div><dt>기존 문제</dt><dd>핀이 얇아 고압 세척 시 변형 위험, 오염으로 열교환 상태 저하</dd></div>
        <div><dt>적용</dt><dd>핀을 휘게 하지 않는 비마모 방식으로 핀 사이 오염물 제거</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>설비를 분해하지 않고 현장에서 세척한 사례로 Cold Jet 공식 자료에 소개 (수치 미제시)</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 공장의 설비도<br>세척할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>공장마다 설비의 종류와 구조, 오염물, 유지보수 조건은 다릅니다.</p>
      <p>바테크는 실제 설비 또는 오염 샘플을 확인하고 세척 테스트를 통해 드라이아이스 세척의 적용 가능성과 적절한 작업 조건을 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 공장의 설비 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

RESTORATION_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/restoration-remediation/ (+ applications/remediation, resources/rossis-italian-restaurant, resources/historic-downtown-loveland) (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/ind-card-fire-restoration.png" aria-label="화재 · 수해 복원 현장">
      <source src="../assets/video/restoration-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 화재 · 수해 복원</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">FIRE & WATER RESTORATION</span>
      <h1>화재 · 수해 복원</h1>
      <p class="cmp-hero-p auto-hero-lead">화재와 수해 이후의 복원은, 표면에 남아 있는 오염물을 제거하는 것에서 시작됩니다.</p>
      <p class="cmp-hero-p auto-hero-body">화재 이후에는 그을음과 탄화물, 연기 잔류물과 냄새의 원인이 되는 카본계 오염물이 목재와 구조물 표면에 남습니다. 수해 현장 역시 물이 빠진 뒤에도 구조재와 표면에 각종 오염물이 남을 수 있습니다. 드라이아이스 세척은 물을 추가로 사용하지 않는 건식 방식으로, 목재와 구조물, 금속과 다양한 표면에 남은 오염물을 제거하는 복원 작업에 활용됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">AFTER FIRE & WATER DAMAGE</span>
      <h2 class="cmp-h2">불이 꺼지고 물이 빠진 뒤에도,<br>구조물에는 오염이 남습니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>화재가 진압된 건물에는 그을음과 탄화 잔류물, 연기 잔류물이 목재 빔과 트러스, 천장과 벽체에 남습니다. 특히 목재의 결과 다공성 표면에 스며든 카본계 침착물은 냄새의 원인이 되며, 코팅이나 탈취제로 덮어도 시간이 지나면 다시 드러나는 경우가 많습니다.</p>
      <p>수해 현장에서는 물이 빠진 뒤에도 구조재 표면에 진흙과 침전물, 먼지와 각종 오염물이 남고, 수분이 오래 머문 부위에는 2차 오염이 발생할 수 있습니다. 배수와 건조, 제습과 구조재의 수분 관리는 별도의 복원 공정이며, 드라이아이스 세척의 역할은 그 이후 표면에 남아 있는 오염물을 물을 더하지 않고 제거하는 과정입니다.</p>
      <p class="auto-intro-close">복원 세척의 목표는 표면을 가리는 것이 아니라, <b>구조물에 남은 오염물을 제거하고 다음 복원 공정을 준비하는 것</b>입니다.</p>
    </div>
  </div>
  <ul class="auto-strip" aria-label="다양한 현장">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/restoration-dry-ice-blasting-removing-smoke-and-soot-from-fire-damaged-wood.webp" alt="" loading="lazy" /><span>화재 피해 목재의 그을음 제거</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/restoration-removing-soot-from-a-metal-ceiling-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span>금속 천장의 그을음 제거</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/restoration-removing-fire-damage-and-soot-from-hardwood-floors-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span>원목 바닥의 화재 잔류물 제거</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/mold-remediation-dry-ice-blasting-removing-mold-spores-resulting-from-water-damage.png" alt="" loading="lazy" /><span>수해 이후 구조재 세척</span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY RESTORATION AREAS</span>
    <h2 class="cmp-h2">화재와 수해 현장에서<br>드라이아이스 세척이 맡는 부분입니다.</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">FIRE & SMOKE DAMAGED WOOD</span>
      <h3>화재 · 연기 피해 목재</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/restoration-dry-ice-blasting-removing-smoke-and-soot-from-fire-damaged-wood.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/contract-fire-restoration.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">목재 결에 스며든 그을음과 탄화층을<br>물을 더하지 않고 제거합니다.</p>
      <div class="cmp-text auto-text"><p>목재 빔과 트러스, 서까래, 벽체와 바닥의 구조재는 화재 이후 그을음과 탄화층, 연기 잔류물로 덮입니다. 샌딩과 손 닦기는 시간이 오래 걸리고 넓은 면적에서는 인력 부담이 크며, 소다 블라스팅은 분사한 매체를 다시 수거해야 합니다.</p><p>드라이아이스 세척은 표면의 탄화층과 그을음을 건식으로 제거하는 데 활용됩니다. Cold Jet 자료에 따르면 탄화된 재료와 카본 잔류물이 제거되면서 냄새의 원인이 함께 줄어들어, 지붕 구조재를 교체하는 대신 세척으로 복원한 사례가 보고되어 있습니다. 다만 탄화 깊이와 구조재의 강도는 별도로 확인해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>목재 빔 · 트러스 · 서까래</li><li>벽체 내부 구조재</li><li>바닥 구조재 · 원목 바닥</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>그을음 · 탄화물 · 연기 잔류물 · 카본 침착물</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">CEILINGS & STRUCTURAL SURFACES</span>
      <h3>천장 · 벽 · 구조물</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/restoration-removing-soot-from-a-metal-ceiling-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">금속 천장과 콘크리트, 벽돌처럼<br>재질이 다른 표면의 그을음을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>한 현장 안에도 금속 천장과 목재, 콘크리트와 벽돌, 도장된 강재처럼 서로 다른 재질이 섞여 있습니다. 재질마다 그을음이 부착되는 방식과 견딜 수 있는 세척 강도가 다릅니다.</p><p>드라이아이스 세척은 입자 크기와 분사 압력, 노즐을 바꾸어 같은 장비로 여러 재질에 대응할 수 있습니다. 얇은 금속 천장 패널처럼 변형되기 쉬운 표면은 낮은 조건에서 먼저 확인한 뒤 작업합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>금속 천장 · 덕트</li><li>콘크리트 · 벽돌</li><li>도장된 강재 · 기타 구조물</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>그을음 · 연기 잔류물 · 카본 침착물</p></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">HARD-TO-REACH STRUCTURES</span>
      <h3>복잡한 구조와 틈새</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/contract-fire-restoration.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">트러스 접합부와 못 주변, 배선 사이처럼<br>손이 닿지 않는 부위에 접근합니다.</p>
      <div class="cmp-text auto-text"><p>복원 현장에서 시간이 가장 많이 드는 곳은 넓은 면이 아니라 트러스 접합부와 못 주변, 배선과 배관 사이, 모서리와 좁은 틈입니다. 샌더와 브러시가 들어가지 않아 손으로 닦아야 하는 부위입니다.</p><p>Cold Jet 복원 자료는 판재와 조이스트 사이, 못 주변, 배선과 배관 주위처럼 기존 방식이 닿지 않는 부위를 드라이아이스 분사로 세척할 수 있다는 점을 강조합니다. 노즐을 바꾸어 좁은 공간에 접근하며, 표면을 갈아내는 방식이 아니므로 목재 형상을 유지하면서 작업할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>트러스 접합부 · 조이스트 사이</li><li>못 · 철물 주변</li><li>배선 · 배관 주위 · 모서리</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>그을음 · 탄화물 · 먼지 · 침착물</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">POST-FLOOD SURFACE CLEANING</span>
      <h3>수해 이후 표면 세척</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mold-remediation-dry-ice-blasting-removing-mold-spores-resulting-from-water-damage.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">물이 빠진 뒤 구조재에 남은 오염물을<br>수분을 더하지 않고 제거합니다.</p>
      <div class="cmp-text auto-text"><p>수해 복구에서 배수와 건조, 제습은 드라이아이스 세척이 대신할 수 없는 별개의 공정입니다. 구조재의 수분이 충분히 관리된 뒤에도 표면에는 진흙과 침전물, 먼지, 그리고 수분이 오래 머문 부위에 생긴 2차 오염이 남습니다.</p><p>드라이아이스 세척은 이 단계에서 물이나 세정제를 다시 더하지 않고 표면 오염물을 제거하는 방법으로 활용됩니다. 이미 물에 노출된 구조재에 수분을 추가하지 않는다는 점이 화학 처리나 습식 세척과 다른 부분입니다. 수해 이후 발생한 곰팡이 오염은 별도의 곰팡이 제거 페이지에서 다룹니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>수해 이후 목재 구조재</li><li>지하 · 저층 벽체와 바닥 구조</li><li>물에 잠긴 설비 외부 표면</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>진흙 · 침전물 · 먼지 · 수해 후 2차 오염</p></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">SURFACE CLEANING BEFORE RESTORATION</span>
      <h3>복원 전 표면 정리</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/restoration-removing-fire-damage-and-soot-from-hardwood-floors-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">도장과 코팅, 보수 공정 전에<br>표면의 오염물을 정리합니다.</p>
      <div class="cmp-text auto-text"><p>복원은 세척으로 끝나지 않습니다. 이후 도장과 코팅, 보수와 마감 공정이 이어지며, 그 결과는 세척된 표면의 상태에 좌우됩니다. 그을음이나 오염물이 남은 표면 위에 코팅을 올리면 부착 불량과 냄새의 재발로 이어질 수 있습니다.</p><p>드라이아이스 세척은 세정 매체나 수분을 남기지 않기 때문에, 세척 직후 건조 대기 없이 다음 공정으로 넘어갈 수 있는 경우가 있습니다. 제거된 그을음과 오염물은 바닥에 떨어지므로 방진포와 HEPA 진공 등으로 회수해 처리합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>재도장 · 코팅 예정 표면</li><li>보수 · 보강 예정 구조재</li><li>원목 바닥 · 마감재</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>그을음 · 연기 잔류물 · 먼지 · 노후 마감</p></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON DAMAGE & CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">화재와 수해 현장에서<br>반복적으로 마주치는 오염물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/restoration-removing-soot-from-a-metal-ceiling-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>그을음</b><small>SOOT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/restoration-dry-ice-blasting-removing-smoke-and-soot-from-fire-damaged-wood.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄화물</b><small>CHAR</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/restoration-removing-fire-damage-and-soot-from-hardwood-floors-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>연기 잔류물</b><small>SMOKE RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/contract-fire-restoration.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 침착물</b><small>CARBON DEPOSIT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/mold-remediation-dry-ice-blasting-removing-mold-spores-resulting-from-water-damage.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>수해 후 오염물</b><small>POST-FLOOD CONTAMINATION</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/mold-remediation-basement-mold-remediation-with-dry-ice-cleaning.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>먼지 · 침전물</b><small>DIRT & DEPOSIT</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">복원 현장에서 드라이아이스 세척을<br>검토하는 이유입니다.</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>물을 더하지 않는 건식 세척</b><p>이미 화재와 물에 노출된 구조재에 수분을 다시 더하지 않습니다. 세척 후 건조 대기가 필요한 공정을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>비마모성 방식</b><p>모래나 소다처럼 표면을 갈아내는 방식이 아니어서, 목재의 형상과 표면 상태를 고려하면서 그을음과 탄화층을 제거하는 데 활용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>복잡한 구조 접근</b><p>트러스 접합부와 못 주변, 배선과 배관 사이처럼 샌더와 브러시가 닿지 않는 부위에 노즐을 바꾸어 접근할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>분사 매체 자체가 남지 않음</b><p>드라이아이스 세정 매체는 승화하여 남지 않으므로 소다 블라스팅처럼 매체를 다시 수거하는 작업이 없습니다. 단, 제거된 그을음과 오염물은 회수·처리해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>수작업과 후처리 감소 가능성</b><p>손 닦기와 샌딩, 탈취제·코팅 반복 시공을 줄일 수 있는 경우가 있어 작업기간과 인력 부담을 낮추는 데 도움이 될 수 있습니다. 결과는 오염 정도와 재질에 따라 달라집니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="auto-feature is-nofig">
    <div class="wrap auto-feature-body reveal">
      <span class="cmp-eyebrow">REMOVE THE SOURCE</span>
      <h2 class="cmp-h2">냄새를 덮는 것보다,<br>냄새의 원인이 되는 오염물을 제거하는 것이 먼저입니다.</h2>
      <p class="cmp-lead-p">화재 냄새는 목재 결과 다공성 표면에 스며든 탄화물과 카본 잔류물에서 나옵니다. 코팅과 탈취제는 이를 덮을 뿐 없애지 못합니다. Cold Jet 복원 자료는 탄화된 재료와 카본 침착물을 제거하는 것이 냄새 문제의 근본적인 접근이라고 설명합니다. 다만 오염 정도와 재질, 구조, 침투 깊이에 따라 추가 복원 공정이 필요할 수 있으므로 모든 현장에서 같은 결과를 일반화하지 않습니다.</p>
      <p class="auto-feature-key">세척은 표면을 가리는 작업이 아니라,<br><em>다음 복원 공정을 위한 준비</em>입니다.</p>
    </div>
  </section>
  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 화재 현장이라도,<br>손상 정도와 표면 재질은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>목재 트러스의 탄화층과 금속 천장의 연기 잔류물, 벽돌과 콘크리트의 그을음은 같은 조건으로 세척할 수 없습니다. 재질과 오염 정도, 탄화 깊이와 표면 상태에 따라 입자 크기와 분사 압력, 노즐과 분사 거리가 달라집니다.</p>
            <p>바테크는 실제 현장의 구조재와 오염 상태를 확인하고, 눈에 띄지 않는 부위에서 먼저 조건을 확인한 뒤 본 작업의 분사 조건을 정합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/restoration-dry-ice-blasting-removing-smoke-and-soot-from-fire-damaged-wood.webp" alt="" loading="lazy" /><b>WOOD TRUSS</b><small>그을음 · 탄화물</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/restoration-removing-soot-from-a-metal-ceiling-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><b>METAL CEILING</b><small>연기 잔류물 · 카본</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/historical-restoration-loveland-fire-outside.jpg" alt="" loading="lazy" /><b>BRICK & CONCRETE</b><small>그을음 · 표면 침착물</small></li>
          </ul>
          <p class="auto-ae-key">복원 현장에서는 장비의 출력보다<br><em>재질과 손상 정도에 맞춘 조건</em>이 결과를 좌우합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">화재 · 수해 복원에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">복원 현장에서 함께 검토되는 작업 유형입니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED RESTORATION SOLUTIONS</span>
      <h2 class="cmp-h2">화재 · 수해 복원과<br>함께 살펴볼 분야</h2>
    </div>
    <p class="cmp-lead-p">수해 이후의 곰팡이 오염은 별도 페이지에서, 산업설비 중심의 전문 세척은 전문 세척 서비스 페이지에서 다룹니다.</p>
  </div>
  <ul class="auto-relind">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/mold-remediation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-mold-removal.png" alt="" loading="lazy" /></span><small>MOLD REMEDIATION</small><b>곰팡이 제거</b><span>자세히 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/contract-cleaning.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-cleaning-service.png" alt="" loading="lazy" /></span><small>CONTRACT CLEANING</small><b>전문 세척 서비스</b><span>자세히 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.20s"><a href="../industries/historical-restoration.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-heritage.png" alt="" loading="lazy" /></span><small>HISTORICAL RESTORATION</small><b>역사적 건축물 · 문화재 복원</b><span>자세히 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RESTORATION IN THE FIELD</span>
      <h2 class="cmp-h2">화재 · 수해 복원 현장에서<br>확인된 적용 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 복원 자료와 사례에 소개된 복원업체의 적용 경험입니다. 수치는 해당 현장의 조건에서 확인된 결과이며, 일반적인 효과로 확대 해석하지 않습니다.</p>
  </div>
  <ul class="auto-logos is-flex is-blend" aria-label="Cold Jet 드라이아이스 세척을 사용하는 화재 · 수해 복원 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:56%"><img src="../assets/img/mold-remediation-911restoration-logo.jpg" alt="911 Restoration" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:60%"><img src="../assets/img/mold-remediation-pauldavis-propertyrestorationexperts-logo.jpg" alt="Paul Davis Restoration" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:58%"><img src="../assets/img/mold-remediation-service-master.jpg" alt="ServiceMaster" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:52%"><img src="../assets/img/mold-remediation-puroclean_logo.jpg" alt="PuroClean" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:56%"><img src="../assets/img/mold-remediation-servpro-logo.jpg" alt="SERVPRO" loading="lazy" /></li>
  </ul>
  <ul class="mtc-cases auto-field-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>FIRE RESTORATION</small><b>화재 피해 건물의 탄화 목재 세척</b><span>Advanced Indoor Air Quality Care</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>화재 피해 건물의 구조 목재</dd></div>
        <div><dt>오염물</dt><dd>탄화 목재 · 카본 · 냄새의 원인이 되는 잔류물</dd></div>
        <div><dt>기존 방식</dt><dd>샌딩·소다 블라스팅 — 작업기간과 인력, 매체 수거 부담</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척으로 탄화층과 카본 잔류물 제거</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>탄화 목재와 카본이 제거되어 코팅·탈취제 사용을 최소화했다고 보고 (사용자 인용, 해당 현장 기준)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>SMOKE DAMAGE</small><b>화재 피해 식당의 그을음 · 연기 잔류물 제거</b><span>Rossi's Italian Restaurant (Cold Jet 사례)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>화재 피해 식당 내부 구조물과 표면</dd></div>
        <div><dt>오염물</dt><dd>그을음 · 연기 잔류물 · 냄새</dd></div>
        <div><dt>과제</dt><dd>영업 재개를 위해 표면 세척과 냄새 원인 제거를 함께 해결</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척으로 그을음 제거와 표면 정리</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>그을음·연기 피해 제거와 함께 표면의 냄새 원인이 줄어든 사례로 Cold Jet 사례에 소개</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.20s">
      <div class="mtc-case-head"><small>HISTORIC DOWNTOWN</small><b>구도심 화재 피해 건물의 연기 오염 제거</b><span>Historic Downtown Loveland (Cold Jet 사례)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>화재 피해를 입은 구도심 건물의 구조물</dd></div>
        <div><dt>오염물</dt><dd>연기 · 그을음</dd></div>
        <div><dt>과제</dt><dd>오래된 건물 표면을 보존하면서 오염 제거, 긴 후처리 없이 진행</dd></div>
        <div><dt>적용</dt><dd>비마모성 드라이아이스 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>세정 매체 수거 등 긴 후처리 없이 연기 피해를 제거한 사례로 소개</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">복원 현장에<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>화재와 수해 현장은 구조재의 재질과 손상 정도, 오염물의 종류와 침투 깊이가 현장마다 다릅니다.</p>
      <p>바테크는 실제 현장 또는 샘플 부재를 확인하고 세척 테스트를 통해 드라이아이스 세척의 적용 가능성과 적절한 작업 조건을 확인합니다. 복원업체의 장비 도입뿐 아니라 렌탈과 현장 지원도 함께 검토할 수 있습니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">복원 현장의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

MOLD_REMEDIATION_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/industries/restoration-remediation/ (+ applications/remediation, resources/mold-remediation, resources/cedar-log-home-restoration-historical-restoration) (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/mold-remediation-dryiceblasting_applications_remediation-5.jpg" alt="곰팡이 제거 현장" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 곰팡이 제거</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">MOLD REMEDIATION</span>
      <h1>곰팡이 제거</h1>
      <p class="cmp-hero-p auto-hero-lead">물을 더하지 않고, 구조재 표면의 곰팡이 오염을 제거합니다.</p>
      <p class="cmp-hero-p auto-hero-body">곰팡이는 목재 구조재와 다락, 크롤스페이스, 벽체 내부처럼 접근하기 어려운 장소에서 발생하는 경우가 많습니다. 드라이아이스 세척은 물을 추가하지 않는 건식 방식으로, 목재와 구조물 표면에 부착된 곰팡이와 오염물을 물리적으로 제거하는 데 활용됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">MOLD REMEDIATION</span>
      <h2 class="cmp-h2">곰팡이 제거는<br>보이는 얼룩만 지우는 작업이 아닙니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>목재 표면과 조이스트, 트러스, 합판, 다락과 크롤스페이스의 복잡한 구조와 틈새에는 곰팡이 오염이 넓게 퍼져 있는 경우가 많습니다. 샌딩과 와이어브러시는 판재 사이와 못·배선 주변처럼 접근성이 낮은 부위의 작업이 어렵고, 좁고 더운 공간에서 많은 수작업이 필요합니다.</p>
      <p>표면에 남은 곰팡이를 충분히 제거하지 못하면 살생물제와 봉합제(encapsulant)를 덧바르는 후속 공정이 뒤따르고, 그만큼 작업기간과 비용이 늘어납니다. 드라이아이스 분사는 이러한 복잡한 부위까지 접근하는 물리적인 표면 세척 방법으로 활용되며, 물이나 화학약품을 구조재에 더하지 않는다는 점이 습식 처리와 다릅니다.</p>
      <p class="auto-intro-close">곰팡이 제거의 목표는 얼룩을 가리는 것이 아니라, <b>구조재 표면에 부착된 곰팡이를 물리적으로 걷어내는 것</b>입니다.</p>
    </div>
  </div>
  <ul class="auto-strip" aria-label="다양한 현장">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/contract-mold-remediation-attic.jpg" alt="" loading="lazy" /><span>다락 구조재</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mold-remediation-crawl-space-before.jpg" alt="" loading="lazy" /><span>크롤스페이스 (작업 전)</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/mold-remediation-removing-mold-from-wood-beams-with-dry-ice-blasting.png" alt="" loading="lazy" /><span>목재 빔</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/mold-remediation-basement-mold-remediation-with-dry-ice-cleaning.png" alt="" loading="lazy" /><span>지하 구조</span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY REMEDIATION AREAS</span>
    <h2 class="cmp-h2">곰팡이 제거 현장에서<br>드라이아이스 세척이 활용되는 부위입니다.</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">ATTIC & ROOF STRUCTURE</span>
      <h3>다락 · 지붕 구조</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/contract-mold-remediation-attic.jpg" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/mold-remediation-dry-ice-blasting-removing-mold-spores-resulting-from-water-damage.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">덥고 좁은 다락에서<br>서까래와 합판 사이의 곰팡이를 제거합니다.</p>
      <div class="cmp-text auto-text"><p>다락은 곰팡이 제거 현장에서 가장 흔하고 가장 힘든 곳입니다. 지붕 합판과 서까래, 트러스 사이 좁은 공간에서 샌딩과 약품 도포를 반복해야 하고, 여름에는 작업 환경이 매우 덥습니다.</p><p>Cold Jet 자료에 따르면 다락 곰팡이 제거에서 드라이아이스 세척은 서까래 사이와 못 주변까지 접근해 표면의 곰팡이를 제거하는 데 활용되며, 기존 방식에 비해 작업 인원과 기간을 크게 줄인 사례가 보고되어 있습니다. 작업 전에는 지붕 누수 등 수분 유입 원인이 해결되어 있어야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>서까래 · 트러스</li><li>지붕 합판 하부</li><li>다락 바닥 조이스트</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>곰팡이 · 곰팡이 얼룩 · 먼지 · 수분 흔적</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">CRAWL SPACE</span>
      <h3>크롤스페이스 · 바닥 하부</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mold-remediation-crawl-space-before.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">습기가 머무는 바닥 하부 공간의<br>조이스트와 합판을 세척합니다.</p>
      <div class="cmp-text auto-text"><p>건물 바닥 아래의 낮은 공간은 습기가 오래 머물고 환기가 어려워 곰팡이가 자라기 쉬운 곳입니다. 작업자가 누워서 작업해야 하는 높이라 샌딩과 브러싱이 매우 어렵습니다.</p><p>드라이아이스 세척은 노즐과 호스로 접근하기 때문에 좁은 공간에서 조이스트 측면과 합판 하부의 곰팡이를 제거하는 데 활용됩니다. Cold Jet 사례에는 다락과 크롤스페이스의 곰팡이를 화학약품 없이 제거한 현장이 소개되어 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>바닥 조이스트</li><li>바닥 합판 하부</li><li>기초 주변 목재</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>곰팡이 · 습기 얼룩 · 먼지 · 침전물</p></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">WOOD BEAMS & JOISTS</span>
      <h3>목재 빔 · 조이스트</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mold-remediation-removing-mold-from-wood-beams-with-dry-ice-blasting.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">구조재의 형상과 강도를 고려하면서<br>표면의 곰팡이를 걷어냅니다.</p>
      <div class="cmp-text auto-text"><p>빔과 조이스트는 건물의 하중을 받는 구조재입니다. 곰팡이를 제거하기 위해 표면을 과도하게 갈아내면 단면이 줄고, 반대로 표면만 처리하면 판재 사이와 접합부에 오염이 남습니다.</p><p>드라이아이스 세척은 연마재로 표면을 깎는 방식이 아니어서 목재의 형상을 유지하면서 표면에 부착된 곰팡이를 제거하는 데 활용됩니다. 목재의 상태와 강도, 오염 깊이에 따라 분사 조건을 조정하며, 부식이나 구조적 손상이 있는 부재는 별도의 구조 검토가 필요합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>목재 빔 · 거더</li><li>바닥 · 천장 조이스트</li><li>접합부 · 철물 주변</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>곰팡이 · 곰팡이 얼룩 · 먼지</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">WALL CAVITIES & COMPLEX AREAS</span>
      <h3>벽체 내부 · 지하 · 복잡한 구조</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mold-remediation-basement-mold-remediation-with-dry-ice-cleaning.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">배선과 배관, HVAC 부품 주변처럼<br>손이 닿지 않는 부위에 접근합니다.</p>
      <div class="cmp-text auto-text"><p>벽체를 개방한 뒤 드러나는 스터드와 배선, 배관, 덕트 주변은 브러시가 들어가지 않는 부위가 많습니다. 지하 공간은 습기와 함께 먼지·침전물이 쌓여 있어 곰팡이와 오염이 섞여 있습니다.</p><p>Cold Jet 자료는 판재와 조이스트 사이, 배선과 HVAC 부품 주변, 못 주변처럼 기존 방식이 닿지 않는 부위를 드라이아이스 분사로 세척할 수 있다는 점을 강조합니다. 전기 배선 주변 작업은 전원 상태와 안전 조건을 별도로 확인한 뒤 진행합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>벽체 스터드 · 내부 합판</li><li>배선 · 배관 · 덕트 주변</li><li>지하 벽체 · 바닥 구조</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>곰팡이 · 먼지 · 침전물 · 습기 얼룩</p></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">POST-WATER-DAMAGE MOLD</span>
      <h3>수해 이후 곰팡이 오염</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/mold-remediation-dry-ice-blasting-removing-mold-spores-resulting-from-water-damage.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">침수 이후 발생한 곰팡이를<br>수분을 다시 더하지 않고 제거합니다.</p>
      <div class="cmp-text auto-text"><p>침수나 누수 이후 건조가 늦어진 구조재에는 짧은 기간에 곰팡이가 넓게 발생합니다. 이미 물에 노출된 목재에 습식 세척이나 약품 도포로 수분을 다시 더하는 것은 복원업체가 피하려는 상황입니다.</p><p>드라이아이스 세척은 건조 이후 표면의 곰팡이를 물을 더하지 않고 제거하는 데 활용됩니다. Adrian Environmental은 드라이아이스 세척이 목재에 수분을 더하지 않는다는 점과, 이후 방균 코팅 시공을 위한 표면 준비에 도움이 된다는 점을 장점으로 언급했습니다. 배수와 건조, 제습은 세척 전에 별도로 완료되어야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>침수 이후 목재 구조재</li><li>누수 부위 주변 구조</li><li>지하 · 저층 벽체</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>곰팡이 · 수해 후 오염물 · 침전물</p></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">WHERE MOLD HIDES</span>
  <h2 class="cmp-h2 reveal">곰팡이는 눈에 보이는 곳보다<br>보이지 않는 곳에서 자랍니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/contract-mold-remediation-attic.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>다락 구조재</b><small>ATTIC FRAMING</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/mold-remediation-crawl-space-before.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>크롤스페이스</b><small>CRAWL SPACE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/mold-remediation-removing-mold-from-wood-beams-with-dry-ice-blasting.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>목재 빔 · 조이스트</b><small>BEAMS & JOISTS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/mold-remediation-basement-mold-remediation-with-dry-ice-cleaning.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>벽체 내부 · 지하</b><small>WALL CAVITIES & BASEMENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/mold-remediation-dry-ice-blasting-removing-mold-spores-resulting-from-water-damage.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>수해 이후 목재</b><small>WATER-DAMAGED WOOD</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/historical-restoration-100_1894.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>통나무 · 외부 목재</b><small>LOG & EXTERIOR WOOD</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">곰팡이 제거에서 드라이아이스 세척을<br>검토하는 이유입니다.</h2>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>물을 추가하지 않는 건식 공정</b><p>곰팡이의 원인인 수분을 구조재에 다시 더하지 않습니다. 습식 세척이나 약품 도포 후 건조를 기다리는 과정을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>목재 및 복잡한 구조 세척</b><p>연마재로 표면을 깎는 방식이 아니어서 구조재의 형상을 유지하면서 표면에 부착된 곰팡이를 제거하는 데 활용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>좁은 틈과 모서리 접근</b><p>판재와 조이스트 사이, 못·배선·HVAC 부품 주변처럼 샌더와 브러시가 닿지 않는 부위에 노즐로 접근할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>반복적인 샌딩 · 브러싱 감소 가능성</b><p>수작업 샌딩과 약품·봉합제 반복 시공을 줄일 수 있는 경우가 있어, 작업 인원과 기간을 낮추는 데 도움이 될 수 있습니다. 결과는 오염 범위와 목재 상태에 따라 다릅니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>세정 매체 자체가 남지 않음</b><p>드라이아이스는 승화하여 남지 않습니다. 단, 제거된 곰팡이와 오염물은 바닥에 떨어지므로 방진포와 HEPA 진공으로 회수하고, 작업 구역 격리와 공기 관리가 함께 필요합니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="auto-feature is-nofig">
    <div class="wrap auto-feature-body reveal">
      <span class="cmp-eyebrow">MOISTURE FIRST</span>
      <h2 class="cmp-h2">곰팡이의 원인이 되는<br>수분 문제를 먼저 해결해야 합니다.</h2>
      <p class="cmp-lead-p">드라이아이스 세척은 곰팡이가 발생한 표면을 세척하는 방법이지, 누수나 결로, 높은 습도 같은 건축물의 수분 문제 자체를 해결하는 기술은 아닙니다. 수분 원인이 그대로라면 세척 후에도 곰팡이는 다시 발생할 수 있습니다. 표면 세척은 아래 복원 절차의 한 단계로 계획해야 합니다.</p>
      <div class="auto-feature-cols">
        <div class="reveal" style="--reveal-delay:0.20s"><small>작업 전에 확인할 것</small><ul><li>누수 · 결로 · 습기 유입 원인 확인</li><li>수분원 차단과 충분한 건조</li><li>작업 구역 격리 · 음압 등 공기 관리 계획</li><li>목재 상태와 오염 범위 확인, 소구역 테스트</li></ul></div>
        <div class="reveal" style="--reveal-delay:0.32s"><small>작업 중 · 작업 후</small><ul><li>제거된 곰팡이 · 분진의 회수 (방진포 · HEPA 진공)</li><li>작업자 보호구와 환기</li><li>필요 시 방균 코팅 등 후속 공정</li><li>작업 후 확인 (PRV 등 현장 기준에 따른 검증)</li></ul></div>
      </div>
      <p class="auto-feature-key">좋은 곰팡이 제거는 세척 그 자체보다<br><em>수분 관리와 복원 절차 안에서</em> 이루어집니다.</p>
    </div>
  </section>
  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 목재라도,<br>표면 상태와 곰팡이 오염 정도는 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>다락의 새 합판과 오래된 통나무 구조재, 침수 이후 강도가 떨어진 목재는 같은 조건으로 세척할 수 없습니다. 목재의 상태와 강도, 표면 마감, 오염의 깊이와 범위에 따라 입자 크기와 분사 압력, 노즐과 분사 거리가 달라집니다.</p>
            <p>바테크는 실제 구조재와 오염 상태를 확인하고, 눈에 띄지 않는 부위에서 먼저 조건을 확인한 뒤 본 작업의 분사 조건을 정합니다. 곰팡이 포자 제거율에 관한 수치는 검증 조건이 명확한 사례에서만 참고합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/contract-mold-remediation-attic.jpg" alt="" loading="lazy" /><b>ATTIC PLYWOOD</b><small>다락 합판 · 서까래</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/historical-restoration-100_1894.jpg" alt="" loading="lazy" /><b>AGED TIMBER</b><small>오래된 구조재 · 통나무</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/mold-remediation-dry-ice-blasting-removing-mold-spores-resulting-from-water-damage.png" alt="" loading="lazy" /><b>WATER-DAMAGED WOOD</b><small>수해 이후 목재</small></li>
          </ul>
          <p class="auto-ae-key">곰팡이 제거에서는 세척 강도보다<br><em>목재 상태에 맞춘 조건과 절차</em>가 결과를 좌우합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">곰팡이 제거에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">곰팡이 제거 현장에서 함께 검토되는 작업 유형입니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/facility-maintenance.html"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>PRODUCTION & FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>컨베이어·모터·제어반·냉각설비 등 생산지원설비</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED RESTORATION SOLUTIONS</span>
      <h2 class="cmp-h2">곰팡이 제거와<br>함께 살펴볼 분야</h2>
    </div>
    <p class="cmp-lead-p">화재·수해 이후의 표면 복원은 별도 페이지에서, 산업설비 중심의 전문 세척은 전문 세척 서비스 페이지에서 다룹니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/restoration.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-fire-restoration.png" alt="" loading="lazy" /></span><small>FIRE & WATER RESTORATION</small><b>화재 · 수해 복원</b><span>자세히 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/contract-cleaning.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-cleaning-service.png" alt="" loading="lazy" /></span><small>CONTRACT CLEANING</small><b>전문 세척 서비스</b><span>자세히 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">MOLD REMEDIATION IN PRACTICE</span>
      <h2 class="cmp-h2">구조물 곰팡이 제거 현장의<br>적용 사례</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 복원 자료와 사례에 소개된 복원업체의 적용 경험입니다. 수치는 해당 현장의 조건에서 확인된 결과이며, 일반적인 효과로 확대 해석하지 않습니다.</p>
  </div>
  <ul class="auto-logos is-flex is-blend" aria-label="Cold Jet 드라이아이스 세척을 사용하는 곰팡이 제거 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:56%"><img src="../assets/img/mold-remediation-911restoration-logo.jpg" alt="911 Restoration" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:60%"><img src="../assets/img/mold-remediation-pauldavis-propertyrestorationexperts-logo.jpg" alt="Paul Davis Restoration" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:58%"><img src="../assets/img/mold-remediation-service-master.jpg" alt="ServiceMaster" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:52%"><img src="../assets/img/mold-remediation-puroclean_logo.jpg" alt="PuroClean" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:56%"><img src="../assets/img/mold-remediation-servpro-logo.jpg" alt="SERVPRO" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:22%"><img src="../assets/img/logo-adrian-environmental.png" alt="Adrian Environmental" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:44%"><img src="../assets/img/logo-bonazza.png" alt="Bonazza Dry Ice Blasting" loading="lazy" /></li>
  </ul>
  <ul class="mtc-cases auto-field-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>ATTIC & CRAWL SPACE</small><b>다락과 크롤스페이스의 곰팡이 제거</b><span>Cold Jet 사례 (Contract Cleaning)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>주택 다락과 크롤스페이스의 목재 구조재</dd></div>
        <div><dt>오염물</dt><dd>곰팡이 · 곰팡이 얼룩</dd></div>
        <div><dt>기존 방식</dt><dd>샌딩 · 살생물제와 봉합제 도포</dd></div>
        <div><dt>적용</dt><dd>화학약품을 사용하지 않는 드라이아이스 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>화학약품 없이 다락과 크롤스페이스의 곰팡이를 제거한 사례로 소개</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>LOG HOME RESTORATION</small><b>통나무 주택의 곰팡이 · 오염층 제거</b><span>Bonazza Dry Ice Blasting</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>시더 통나무 주택 외부 목재</dd></div>
        <div><dt>오염물</dt><dd>곰팡이 · 먼지 · 오래된 오염층</dd></div>
        <div><dt>기존 방식</dt><dd>샌드 · 콘 블라스팅 + 샌딩 — 매체 수거와 추가 작업일</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척으로 표면 오염층 제거</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>샌드·콘 블라스팅 대비 3~4일, 샌딩 2일분의 작업을 줄였다고 보고 (사용자 인용, 해당 현장 기준)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.20s">
      <div class="mtc-case-head"><small>NO ADDED MOISTURE</small><b>수분을 더하지 않는 곰팡이 제거</b><span>Adrian Environmental</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>곰팡이가 발생한 목재 구조 부재</dd></div>
        <div><dt>오염물</dt><dd>곰팡이</dd></div>
        <div><dt>과제</dt><dd>곰팡이 성장의 원인인 수분을 세척 과정에서 다시 더하지 않기</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척 후 방균 코팅 시공</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>목재에 수분을 더하지 않고, 이후 방균 코팅을 위한 표면 준비에도 도움이 되었다고 보고 (사용자 인용)</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">현재 구조물에<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>곰팡이 제거 현장은 목재의 상태와 오염 범위, 수분 원인과 작업 공간이 현장마다 다릅니다.</p>
      <p>바테크는 실제 현장 또는 샘플 부재를 확인하고 세척 테스트를 통해 드라이아이스 세척의 적용 가능성과 적절한 작업 조건을 확인합니다. 수분 관리와 격리, 후속 공정은 현장의 복원 절차와 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">구조물의 곰팡이 제거 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

HISTORICAL_RESTORATION_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/applications/historical-restoration/ (+ resources/uss-monitor, industries/restoration-remediation) / 바테크 국내 현장 실사진 (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/ind-card-heritage.png" aria-label="역사적 건축물 · 문화재 복원 현장">
      <source src="../assets/video/historical-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 역사적 건축물 · 문화재 복원</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">HISTORICAL RESTORATION</span>
      <h1>역사적 건축물 · 문화재 복원</h1>
      <p class="cmp-hero-p auto-hero-lead">제거해야 할 오염물과 남겨야 할 흔적을 구분하는 것이 복원의 시작입니다.</p>
      <p class="cmp-hero-p auto-hero-body">역사적 건축물과 기념물, 박물관 유물의 표면에는 오랜 시간 쌓인 오염물과 함께 보존해야 할 표면 상태와 파티나, 제작 흔적이 공존합니다. 드라이아이스 세척은 연마재와 물을 사용하지 않는 비마모성 건식 방식으로, 대상의 재질과 상태를 확인하고 낮은 조건에서 먼저 테스트한 뒤 석재·벽돌·목재·금속 표면의 오염물을 제거하는 복원 작업에 활용됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">PRESERVATION FIRST</span>
      <h2 class="cmp-h2">오래되었다는 이유만으로<br>모든 흔적을 제거해서는 안 됩니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>역사적 건축물과 전시물의 표면에는 매연과 산성비 흔적, 생물성 오염, 노후 도막 같은 제거 대상뿐 아니라, 오랜 시간 형성된 표면 상태와 마감, 파티나, 제작 당시의 도구 흔적처럼 보존해야 할 요소가 함께 있습니다. 일반 산업세척처럼 "깨끗하게 만드는 것"만을 목표로 하면 남겨야 할 것까지 잃을 수 있습니다.</p>
      <p>샌드블라스팅은 연한 석재와 벽돌 표면을 깎아내고, 고압 세척은 벽돌과 석재 줄눈에 수분을 밀어 넣으며, 약품 처리는 다공성 재질에 흡수됩니다. Cold Jet 자료는 드라이아이스 세척이 마찰로 표면을 갈아내는 방식이 아니라 열충격과 승화 팽창으로 오염물을 떼어내는 방식이라는 점을 설명합니다. 그럼에도 어떤 대상이든 무엇을 제거하고 무엇을 남길지는 세척 전에 먼저 판단해야 합니다.</p>
      <p class="auto-intro-close">바테크는 국내에서 동상과 야외 전시 유물, 증기기관차 같은 대형 문화재의 표면 오염물을 드라이아이스로 세척한 현장 경험을 가지고 있습니다. <b>복원 세척은 소유기관과 복원 전문가의 판단 아래 진행되어야 합니다.</b></p>
    </div>
  </div>
  <ul class="auto-strip" aria-label="다양한 현장">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/vatek-field-statue-cleaning-graded.png" alt="" loading="lazy" /><span>바테크 국내 현장 — 동상 세척</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/vatek-field-artifact-machinery-cleaning-graded.png" alt="" loading="lazy" /><span>바테크 국내 현장 — 야외 전시 기계 유물</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/vatek-field-heritage-locomotive-cleaning-graded.png" alt="" loading="lazy" /><span>바테크 국내 현장 — 증기기관차</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/historical-restoration-cleaning-stone-statue-at-st.webp" alt="" loading="lazy" /><span>석조 성상 세척 (Cold Jet)</span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">KEY RESTORATION AREAS</span>
    <h2 class="cmp-h2">재질과 규모가 달라도,<br>남겨야 할 표면을 먼저 확인한다는 원칙은 같습니다.</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">MONUMENTS & SCULPTURES</span>
      <h3>기념물 · 조형물</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/historical-restoration-restoring-monument-in-puerto-rico-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/historical-restoration-dry-ice-blasting-cleaning-public-fountain-in-germany.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">조각의 세부를 유지하면서<br>수십 년 쌓인 오염을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>야외 기념물에는 교통 매연과 산성비 흔적, 조류 배설물, 이끼와 조류 같은 생물성 오염이 대리석과 화강암, 청동 표면에 쌓입니다. 조각의 얇은 부분과 새김 글자는 연마 방식으로 세척하면 마모될 수 있는 부위입니다.</p><p>드라이아이스 세척은 분사 압력과 입자 크기를 낮춰 얇은 조각 부위를 지나고, 두꺼운 오염층에는 조건을 높이는 식으로 한 대상 안에서도 조건을 바꾸어 작업합니다. Cold Jet 자료에는 남북전쟁 기념물을 세정 매체 격리 설비 없이 세척해 기간과 비용을 크게 줄인 사례가 소개되어 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>공공 조각 · 동상</li><li>화강암 · 대리석 기념물</li><li>청동 명판 · 석조 기단</li><li>기념 포 · 야외 설치물</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>매연 · 산성비 흔적 · 생물성 오염 · 이끼 · 조류 배설물</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">HISTORIC BUILDINGS</span>
      <h3>역사적 건축물</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/historical-restoration-restoring-historic-brick-masonry-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/historical-restoration-restoring-staircase-in-historic-prison-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">벽돌과 석재 외벽, 장식 부재를<br>해체하지 않고 제자리에서 세척합니다.</p>
      <div class="cmp-text auto-text"><p>역사적 벽돌과 석회암, 사암 외벽은 샌드블라스팅에 쉽게 마모되고, 고압 세척의 수분은 줄눈으로 스며들어 동결·융해 손상을 일으킬 수 있습니다. 주석 천장 타일과 석고 장식, 목조 장식은 약품이나 강한 세척에 손상되기 쉬운 부재입니다.</p><p>드라이아이스 세척은 노후 도막과 생물성 오염, 매연 얼룩을 원래 마감과 파티나를 고려하면서 제거하는 데 활용되며, 장식 부재를 해체하지 않고 제자리에서 작업할 수 있습니다. Cold Jet 자료에는 4,500 ft² 이상의 역사적 주석 천장을 손 연마 대비 훨씬 짧은 시간에 세척한 사례가 있습니다. 납 성분 도막이 있는 경우 별도의 격리와 회수, 보호구 규정이 적용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>벽돌 · 석조 외벽 · 줄눈</li><li>주석 천장 · 석고 장식</li><li>계단 · 난간 · 주철 부재</li><li>목재 구조 · 장식 부재</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>매연 · 산성비 얼룩 · 노후 도막 · 생물성 오염 · 그을음</p></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">HISTORIC WOOD</span>
      <h3>목재 구조물</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/historical-restoration-100_1894.jpg" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">오래된 목재의 결과 형상을 유지하면서<br>표면의 오염층을 걷어냅니다.</p>
      <div class="cmp-text auto-text"><p>오래된 목조 건축과 통나무 구조, 목재 외벽과 빔에는 먼지와 생물성 오염, 곰팡이와 노후 마감이 겹겹이 쌓입니다. 샌딩은 목재의 결과 도구 흔적을 함께 지우고, 습식 세척은 목재에 수분을 더합니다.</p><p>드라이아이스 세척은 목재를 깎아내지 않고 표면 오염층을 제거하는 데 활용됩니다. Cold Jet 사례에는 시더 통나무 주택의 곰팡이와 오염층을 샌드·콘 블라스팅 대비 짧은 기간에 제거한 현장이 소개되어 있습니다. 목재의 강도와 노후 정도에 따라 낮은 조건부터 확인해야 하며, 부후가 진행된 부재는 구조적 검토가 우선입니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>목재 외벽 · 통나무 구조</li><li>빔 · 트러스 · 장식 목부재</li><li>오래된 목조 건축</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>먼지 · 생물성 오염 · 곰팡이 · 노후 마감</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">METAL & INDUSTRIAL HERITAGE</span>
      <h3>금속 · 산업 유산</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/vatek-field-heritage-locomotive-cleaning-graded.png" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/vatek-field-artifact-machinery-cleaning-graded.png" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">철도차량과 기계 유물처럼<br>크고 복잡한 금속 유산을 현장에서 세척합니다.</p>
      <div class="cmp-text auto-text"><p>증기기관차와 산업 기계, 철제 구조물 같은 산업 유산은 크기가 커서 옮길 수 없고, 리벳과 배관, 부품 사이 틈이 많아 손 세척에 시간이 오래 걸립니다. 표면에는 먼지와 그리스, 매연, 노후 도막과 표면 산화물이 섞여 있습니다.</p><p>바테크는 국내에서 야외 전시 증기기관차와 기계 유물의 표면 오염물을 드라이아이스로 세척한 현장 경험을 가지고 있습니다. 드라이아이스 세척은 느슨한 표면 산화물과 오염층을 제거하는 데 활용되지만, 깊게 진행된 부식은 별도의 보존 처리 대상이며 금속 표면에 프로파일을 만드는 연마 블라스팅과는 역할이 다릅니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>증기기관차 · 철도차량</li><li>산업 기계 · 설비 유물</li><li>철제 구조물 · 주철 부재</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>먼지 · 그리스 · 매연 · 노후 도막 · 표면 산화물</p></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">MUSEUM ARTIFACTS</span>
      <h3>박물관 · 전시 유물</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/historical-restoration-restoring-wrought-iron-from-uss-monitor-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/historical-restoration-cleaning-stone-statue-at-st.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">현미경 검사 기준으로 확인된<br>유물 표면 세척 사례가 있습니다.</p>
      <div class="cmp-text auto-text"><p>박물관 소장품은 한 번의 실패한 세척이 영구적인 손상으로 남기 때문에 가장 엄격한 기준이 적용됩니다. 부식성 오염물과 매장 침착물, 오래된 보존 처리 잔류물을 제거하되 원래 표면은 유지해야 합니다.</p><p>The Mariners' Museum의 USS Monitor 보존 프로젝트에서는 드라이아이스 세척 후 표면을 350배 확대 검사해 피팅이나 마모 흔적이 확인되지 않았다고 보고했으며, 손으로 2~3주 걸릴 구조 판재 세척이 약 1시간에 이루어졐다고 소개되어 있습니다. 이는 해당 재질과 조건에서의 결과이며, 다른 유물에도 같은 결과를 일반화하지 않고 대상별 사전 테스트를 거칩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>군사 · 해양 유물</li><li>산업 기계 전시물</li><li>석재 · 세라믹 · 금속 유물</li><li>고가구 · 조명 등 목재·금속 물품</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>부식성 오염물 · 매장 침착물 · 먼지 · 오래된 보존 처리 잔류물</p></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">역사적 표면에서<br>반복적으로 마주치는 오염물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/historical-restoration-dry-ice-blasting-removing-contaminants-from-brick-masonry.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>환경 오염 · 매연</b><small>ENVIRONMENTAL GRIME</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/historical-restoration-loveland-fire-outside.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>그을음</b><small>SOOT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/historical-restoration-dry-ice-blasting-cleaning-public-fountain-in-germany.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>생물성 오염</b><small>BIOLOGICAL GROWTH</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/historical-restoration-restoring-monument-in-puerto-rico-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>이끼 · 오염 침착물</b><small>MOSS & DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/historical-restoration-dry-ice-blasting-restoring-historic-lighthouse.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>노후 도막</b><small>AGED / FAILING COATINGS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/historical-restoration-restoring-wrought-iron-from-uss-monitor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>부식성 오염물</b><small>CORROSIVE CONTAMINANTS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/historical-restoration-cleaning-stone-statue-at-st.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오래된 표면 침착물</b><small>AGED SURFACE DEPOSITS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/vatek-field-artifact-machinery-cleaning-graded.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>그리스 · 산업 유산 오염</b><small>GREASE & INDUSTRIAL RESIDUE</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">복원 전문가가 드라이아이스 세척을<br>검토하는 이유입니다.</h2>
  <ol class="auto-why is-6">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성 세척 방식</b><p>모래·소다처럼 마찰로 표면을 깎는 방식이 아닙니다. 조각의 세부와 파티나, 원래 마감을 고려해야 하는 대상에 활용할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>물을 사용하지 않는 건식 세척</b><p>벽돌과 석재 줄눈에 수분을 밀어 넣지 않으므로 동결·융해 손상과 약품 흡수 문제를 피하는 데 도움이 됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>복잡한 조각과 세부 형상 접근</b><p>새김 글자와 부조, 몰딩과 줄눈처럼 손 도구가 닿기 어려운 부위에 노즐로 접근할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>세정 매체 자체가 남지 않음</b><p>드라이아이스는 승화하여 남지 않아 매체 격리·수거 설비가 줄어듭니다. 단, 제거된 오염물과 도막(특히 납 성분)은 규정에 따라 회수·처리해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>현장에서 직접 세척</b><p>고정된 조각과 건축 부재, 대형 유물을 해체하거나 옮기지 않고 제자리에서 작업할 수 있는 경우가 많습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.45s"><b>분사 조건 조절 가능</b><p>입자 크기와 압력, 노즐, 거리와 각도를 낮은 조건부터 단계적으로 조정하여 목표 표면 상태에 맞출 수 있습니다. 적용 여부는 복원 전문가와 소유기관의 판단을 따릅니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="auto-feature is-nofig">
    <div class="wrap auto-feature-body reveal">
      <span class="cmp-eyebrow">TEST BEFORE RESTORATION</span>
      <h2 class="cmp-h2">복원 대상은<br>세척 전에 먼저 확인해야 합니다.</h2>
      <p class="cmp-lead-p">같은 석재, 같은 목재, 같은 금속이라도 노후 정도와 표면 마감, 과거의 도장·보수 이력, 파티나, 균열과 부식 상태가 다릅니다. 역사적 건축물과 유물에는 본 작업 전에 눈에 띄지 않는 작은 구역에서 세척 조건을 확인하는 과정이 특히 중요합니다. Cold Jet도 비마모성 결과는 "올바른 분사 조건을 사용할 때"의 결과라고 명시합니다.</p>
      <div class="auto-feature-cols">
        <div class="reveal" style="--reveal-delay:0.20s"><small>먼저 확인할 것</small><ul><li>재질과 노후 정도, 표면 강도</li><li>표면 마감 · 파티나 · 제작 흔적</li><li>과거 도장 · 보수 이력 (납 성분 도막 여부)</li><li>균열 · 박리 · 부식 상태</li></ul></div>
        <div class="reveal" style="--reveal-delay:0.32s"><small>낮은 조건부터 조정</small><ul><li>분사 압력 — 가장 낮은 조건에서 시작</li><li>입자 크기 — 미세 입자에서 펠렛으로</li><li>노즐 종류 · 분사 거리 · 각도</li><li>목표 표면 상태에 도달하면 그 조건으로 고정</li></ul></div>
      </div>
      <p class="auto-feature-key">복원 세척의 기준은 "얼마나 깨끗한가"가 아니라<br><em>무엇을 남겼는가</em>입니다.</p>
    </div>
  </section>
  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 문화재라도,<br>재질과 상태에 따라 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>화강암 기념물의 생물성 오염과 벽돌 외벽의 매연, 철제 유물의 부식성 오염물은 같은 조건으로 세척할 수 없습니다. 재질의 강도와 다공성, 표면 마감, 오염층의 두께와 부착 정도에 따라 입자 크기와 압력, 노즐과 거리가 달라집니다.</p>
            <p>바테크는 소유기관과 복원 전문가의 판단 아래 실제 대상 또는 동일 재질 샘플에서 낮은 조건부터 테스트하고, 목표 표면 상태에 맞는 조건을 확인한 뒤 본 작업을 진행합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/historical-restoration-restoring-monument-in-puerto-rico-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>STONE MONUMENT</b><small>생물성 오염 · 매연</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/historical-restoration-restoring-historic-brick-masonry-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>BRICK MASONRY</b><small>매연 · 노후 도막</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/historical-restoration-restoring-wrought-iron-from-uss-monitor-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>WROUGHT IRON ARTIFACT</b><small>부식성 오염물 · 침착물</small></li>
          </ul>
          <p class="auto-ae-key">문화재 세척에서는 장비의 성능보다<br><em>어디서 멈출지를 아는 조건 설정</em>이 중요합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">역사적 건축물 · 문화재 복원에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">복원 세척 현장에서 함께 검토되는 작업 유형입니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/rust-corrosion-removal.html"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>RUST, CORROSION & OXIDATION REMOVAL</small><b>녹 · 부식 · 산화물 제거</b><span>표면 녹과 느슨한 산화물(비마모 범위 내)</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g3" data-target="../applications/surface-preparation.html"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>SURFACE PREPARATION</small><b>표면 전처리</b><span>도장·코팅·접착 전 오일·이형제·먼지 제거</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED RESTORATION SOLUTIONS</span>
      <h2 class="cmp-h2">역사적 건축물 · 문화재 복원과<br>함께 살펴볼 분야</h2>
    </div>
    <p class="cmp-lead-p">화재 피해를 입은 역사적 건물의 복원은 화재·수해 복원 페이지에서, 복원업체의 폭넓은 작업 영역은 전문 세척 서비스 페이지에서 다룹니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/contract-cleaning.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-cleaning-service.png" alt="" loading="lazy" /></span><small>CONTRACT CLEANING</small><b>전문 세척 서비스</b><span>자세히 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/restoration.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-fire-restoration.png" alt="" loading="lazy" /></span><small>FIRE & WATER RESTORATION</small><b>화재 · 수해 복원</b><span>자세히 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PRESERVATION IN PRACTICE</span>
      <h2 class="cmp-h2">보존과 복원 현장에서<br>확인된 세척 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 Historical Restoration 자료에 소개된 보존기관과 복원업체의 적용 경험입니다. 수치는 해당 대상과 조건에서 확인된 결과이며, 다른 유물에 일반화하지 않습니다.</p>
  </div>
  <ul class="auto-logos is-flex is-blend" aria-label="Cold Jet 드라이아이스 세척을 사용하는 역사적 건축물 · 문화재 복원 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:64%"><img src="../assets/img/historical-restoration-mariners-_museum_logo.webp" alt="The Mariners' Museum and Park" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:56%"><img src="../assets/img/historical-restoration-jpaulgetty-logo.webp" alt="J. Paul Getty" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:26%"><img src="../assets/img/historical-restoration-veit.png" alt="Veit & Company" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:44%"><img src="../assets/img/logo-uscleanblast.png" alt="USCleanBlast" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:50%"><img src="../assets/img/historical-restoration-bonazza-dry-ice-blasting.webp" alt="Bonazza Dry Ice Blasting" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:52%"><img src="../assets/img/historical-restoration-cryomode-dryiceblasting-logo.webp" alt="CryoMode Dry Ice Blasting" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:50%"><img src="../assets/img/historical-restoration-nitrofreeze_logo.webp" alt="NitroFreeze" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:40%"><img src="../assets/img/historical-restoration-yeti_logo_2020-02.jpg" alt="YETI" loading="lazy" /></li>
  </ul>
  <ul class="mtc-cases auto-field-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>MUSEUM CONSERVATION</small><b>USS Monitor 철제 유물의 보존 세척</b><span>The Mariners' Museum and Park (미국 버지니아)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>남북전쟁 시기 철갑선 USS Monitor의 단철 구조 판재</dd></div>
        <div><dt>오염물</dt><dd>부식성 오염물 · 매장 침착물</dd></div>
        <div><dt>기존 방식</dt><dd>손 세척 — 판재 1장에 2~3주</dd></div>
        <div><dt>적용</dt><dd>National Park Service 해양유산 보조금 사업으로 드라이아이스 세척 테스트 후 적용</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>350배 확대 검사에서 피팅·마모 흔적이 확인되지 않았고, 판재 세척이 약 1시간으로 줄었다고 보고 (해당 재질·조건 기준)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>MONUMENT</small><b>남북전쟁 기념물 복원 세척</b><span>USCleanBlast.com</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>세부 장식이 있는 역사적 기념물</dd></div>
        <div><dt>오염물</dt><dd>오염 · 생물성 침착물</dd></div>
        <div><dt>기존 방식</dt><dd>설계자가 처음 요구한 소다 블라스팅 — 매체 격리·수거 비용</dd></div>
        <div><dt>적용</dt><dd>비마모성 드라이아이스 세척으로 세부 형상을 보존하며 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>세정 매체 격리 설비 없이 약 1.5일에 완료, 소다 블라스팅 대비 비용을 크게 줄였다고 보고 (Cold Jet 자료)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.20s">
      <div class="mtc-case-head"><small>LIGHTHOUSE</small><b>Split Rock 등대 복원 준비 세척</b><span>Veit & Company</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>역사적 등대 구조물</dd></div>
        <div><dt>오염물</dt><dd>노후 도막 · 표면 오염</dd></div>
        <div><dt>과제</dt><dd>복원 본 공정 전 표면 준비 단계에서 표면 손상 없이 오염 제거</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>초기 준비 단계에서 역사적 복원 프로젝트에 검토할 가치가 있는 방식임을 확인했다고 프로젝트 매니저가 언급 (사용자 인용)</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">복원 대상의<br>표면 상태부터 확인해보세요.</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>역사적 건축물과 유물은 재질과 노후 정도, 표면 마감과 보수 이력이 대상마다 다르며, 무엇을 남길지는 소유기관과 복원 전문가가 먼저 판단해야 합니다.</p>
      <p>바테크는 실제 대상 또는 동일 재질 샘플에서 낮은 조건부터 세척 테스트를 진행하여 드라이아이스 세척의 적용 가능성과 적절한 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">복원 대상의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

AUTOMOTIVE_DETAILING_BODY = """
<!-- 이미지 출처: Cold Jet 공식 https://www.coldjet.com/dry-ice-blasting/applications/automotive-detailing/ (원본 URL 참조 — 배포 시 assets/img/ 로 로컬화) -->
  <section class="subhero-parallax auto-hero-stage">
    <video class="subhero-parallax-img auto-hero-video" autoplay muted loop playsinline preload="auto" poster="../assets/img/automotive-detailing-automotive-restoration-still-1.jpg" aria-label="자동차 복원 · 디테일링 현장">
      <source src="../assets/video/detailing-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/industry.html">산업별 솔루션</a> &gt; 자동차 복원 · 디테일링</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">AUTOMOTIVE RESTORATION & DETAILING</span>
      <h1>자동차 복원 · 디테일링</h1>
      <p class="cmp-hero-p auto-hero-lead">묵은 오염물은 제거하고, 차량이 가진 원래의 표면과 디테일은 최대한 유지합니다.</p>
      <p class="cmp-hero-p auto-hero-body">자동차 하부와 엔진룸에는 시간이 지나면서 오일과 그리스, 도로 오염물, 방청 왁스와 각종 침착물이 쌓입니다. 특히 클래식카와 희소 차량의 복원에서는 단순히 깨끗하게 만드는 것보다 원래의 도장과 코팅, 공장 표시와 부품의 상태를 가능한 한 유지하는 것이 중요합니다. 드라이아이스 세척은 물을 사용하지 않는 비마모성 방식으로 차량의 다양한 부품과 복원 작업에 활용되고 있습니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">PRESERVE ORIGINALITY</span>
      <h2 class="cmp-h2">자동차 복원에서는<br>깨끗함만큼 원래의 상태가 중요합니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>클래식카와 수집 차량에서는 공장 도장과 OEM 코팅, 검사 표시(inspection mark)와 페인트 도브(paint daub), 날짜 스탬프와 라벨, 부품 표면의 원래 마감이 차량의 이력과 가치를 증명합니다. 그 위에 쌓인 오일과 도로 오염물, 방청 왁스를 제거하기 위해 표면을 갈아내거나 강한 용제로 닦아내면, 증명해야 할 흔적까지 함께 사라질 수 있습니다.</p>
      <p>드라이아이스 세척은 연마재와 물을 사용하지 않는 방식이어서 오염층은 제거하고 그 아래의 도장과 마킹은 드러내는 작업에 활용됩니다. Cold Jet 자료에는 1970년대에 도포된 방청 코팅을 두 시간 이내에 제거해 그 아래 공장 시그니처를 노출한 사례가 소개되어 있습니다. 다만 도장 상태와 부착력에 따라 결과가 달라지므로, 보존 대상 부위는 낮은 조건에서 먼저 확인합니다.</p>
      <p class="auto-intro-close">복원의 기준은 "얼마나 새것처럼 보이는가"가 아니라, <b>필요한 오염물만 제거하고 남겨야 할 표면을 구분했는가</b>입니다.</p>
    </div>
  </div>
  <ul class="auto-strip" aria-label="다양한 현장">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/automotive-detailing-dry-ice-cleaning-detailing-the-undercarriage-of-ferrari.webp" alt="" loading="lazy" /><span>고급차 언더바디</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/automotive-detailing-removing-oil-and-grime-from-engine-bay-components-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span>엔진룸 부품</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/automotive-detailing-dry-ice-blasting-car-frame-of-classic-bmw.webp" alt="" loading="lazy" /><span>클래식카 프레임</span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/automotive-detailing-removing-coating-from-wheel-well-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span>휠하우스 코팅 제거</span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">DETAILING & RESTORATION AREAS</span>
    <h2 class="cmp-h2">차량의 부위마다<br>쌓이는 오염물과 지켜야 할 표면이 다릅니다.</h2>
  </div>
<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">UNDERCARRIAGE & CHASSIS</span>
      <h3>언더바디 · 섀시</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/automotive-detailing-dry-ice-cleaning-detailing-the-undercarriage-of-ferrari.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/automotive-detailing-cleaning-undercarriage-of-a-high-end-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">하부의 오일과 도로 오염물을<br>부품을 떼어내지 않고 제거합니다.</p>
      <div class="cmp-text auto-text"><p>차량 하부는 오일과 그리스, 도로 오염물, 타르와 방청 왁스가 가장 두껍게 쌓이는 곳이고, 배기계와 서스펜션, 배선과 배관이 얽혀 있어 손과 브러시가 닿지 않는 곳이 많습니다. 고압 세척은 수분을 남기고, 용제 세척은 시간이 오래 걸립니다.</p><p>드라이아이스 세척은 리프트 위에서 하부 전체를 분해하지 않고 세척하는 데 활용되며, 노즐을 바꾸어 프레임 안쪽과 부품 사이 틈에 접근합니다. Cold Jet 자료에 따르면 고급차 디테일링과 딜러의 출고 전 정비에서 언더바디 세척이 대표적인 작업으로 소개됩니다. 하부 작업에는 차량 리프트가 사실상 필수입니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>프레임 · 플로어 팬</li><li>배기계 · 히트 실드</li><li>서브프레임 · 크로스멤버</li><li>하부 배선 · 배관 주변</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>오일 · 그리스 · 도로 오염물 · 타르 · 방청 왁스</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">ENGINE, ENGINE BAY & DRIVETRAIN</span>
      <h3>엔진 · 엔진룸 · 구동계</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/automotive-detailing-removing-oil-and-grime-from-engine-bay-components-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">배선과 센서가 있는 엔진룸을<br>물을 쓰지 않고 세척합니다.</p>
      <div class="cmp-text auto-text"><p>엔진룸에는 오일 미스트와 먼지가 섞여 굳은 오염이 커버와 하네스, 브래킷 사이에 쌓입니다. 변속기와 구동계 외부도 마찬가지입니다. 물과 증기 세척은 커넥터와 센서에 수분이 들어갈 위험이 있어 마스킹과 건조에 시간이 듭니다.</p><p>드라이아이스 세척은 건식 방식이어서 엔진과 변속기를 차량에 장착한 상태로 외부를 세척하는 데 활용됩니다. Cold Jet은 수 시간이 걸리던 엔진룸 세척이 수십 분 단위로 줄어든 예를 소개합니다. 다만 전장 부품이 있다는 이유로 "무조건 안전하다"고 보지 않고, 부품 상태와 전원 상태, 커넥터 밀폐 정도와 노후도를 확인한 뒤 분사 조건을 정합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>밸브 커버 · 인테이크 · 브래킷</li><li>알터네이터 · 스타터 · 컴프레서</li><li>변속기 · 디퍼렌셜 외부</li><li>하네스 · 커넥터 주변 (조건 확인 후)</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>오일 · 그리스 · 먼지 · 굳은 오염층</p></div>
    </div>
  </div>
</article>

<article class="auto-app" id="auto-03">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div>
      <span class="auto-en">WHEEL WELLS, SUSPENSION & BRAKES</span>
      <h3>휠하우스 · 서스펜션 · 브레이크</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/automotive-detailing-cleaning-steering-and-suspension-components-with-dry-ice-blasting.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/automotive-detailing-detailing-a-wheel-hub-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">휠하우스와 서스펜션의<br>복잡한 형상에 쌓인 오염을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>휠하우스와 서스펜션 암, 브레이크 캘리퍼와 허브 주변은 도로에서 튀어오른 흙과 타르, 브레이크와 타이어 마모 분진이 그리스와 섞여 두껍게 굳는 부위입니다. 스프링과 링크, 부싱 사이는 브러시가 들어가지 않습니다.</p><p>드라이아이스 세척은 휠을 탈거한 상태에서 서스펜션과 브레이크 주변, 펜더 라이너까지 세척하는 데 활용됩니다. 고무 부싱과 실, 플라스틱 라이너처럼 재질이 다른 부품이 섞여 있으므로 부위에 따라 입자 크기와 압력을 조정합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>휠하우스 · 펜더 라이너</li><li>컨트롤 암 · 링크 · 스프링</li><li>브레이크 캘리퍼 · 허브</li><li>스티어링 부품</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>흙 · 타르 · 브레이크 분진 · 그리스 · 표면 산화물</p></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-04">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div>
      <span class="auto-en">CLASSIC CAR & FRAME RESTORATION</span>
      <h3>클래식카 · 프레임 복원</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/automotive-detailing-dry-ice-blasting-car-frame-of-classic-bmw.webp" alt="" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/automotive-detailing-cleaning-the-wheel-well-of-a-classic-car-with-dry-ice-blasting-topaz-gigapixel-2x-scale.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">수십 년 쌓인 오염을 제거하면서<br>공장 마감과 흔적은 남깁니다.</p>
      <div class="cmp-text auto-text"><p>클래식카 복원에서는 프레임과 플로어, 휠하우스의 묵은 오염과 노후 도막, 느슨한 표면 녹을 제거하면서도 공장 도장과 검사 표시, 시리얼 번호와 스탬프를 보존해야 합니다. 샌드블라스팅은 이 모든 것을 함께 지우고, 화학 박리는 도장 층을 구분하지 못합니다.</p><p>드라이아이스 세척은 오염층과 부착력이 약해진 도막, 느슨한 표면 녹을 제거하는 데 활용되며 그 아래 금속과 남아 있는 도장은 갈아내지 않습니다. Cold Jet 자료에는 반복적인 분해가 부담인 희소 차량에서 분해를 줄이고 복원한 사례가 소개됩니다. 깊게 진행된 부식은 별도의 방청·보수 대상이며, 금속 표면 프로파일이 필요한 재도장 준비는 연마 블라스팅의 영역입니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>프레임 · 플로어 팬</li><li>휠하우스 · 이너 펜더</li><li>플로어 언더코팅 부위</li><li>원래 도장 · 마킹이 남은 부위</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>묵은 오염층 · 노후 도막 · 느슨한 표면 녹 · 언더코팅</p></div>
    </div>
  </div>
</article>

<div class="auto-freeze">
<article class="auto-app is-wide" id="auto-05">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div>
      <span class="auto-en">COATING REMOVAL & SIGNATURE RECOVERY</span>
      <h3>방청 코팅 제거 · 공장 시그니처 노출</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/automotive-detailing-removing-coating-from-wheel-well-with-dry-ice-cleaning.webp" alt="" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">코스모린과 후도장 코팅을 걷어내면<br>공장 시그니처가 드러납니다.</p>
      <div class="cmp-text auto-text"><p>출고 당시 도포된 방청 왁스(코스모린)와 소유자가 후에 덧바른 언더코팅, 애프터마켓 도장은 시간이 지나면 굳어 그 아래의 검사 표시와 페인트 도브, 날짜 스탬프를 덮어버립니다. 이 흔적들은 차량의 진품성을 증명하는 근거가 됩니다.</p><p>Cold Jet 자료는 드라이아이스 세척이 방청제와 애프터마켓 코팅을 제거해 공장 시그니처를 노출하는 작업에 활용된다고 소개하며, 1970년대 방청 코팅을 두 시간 이내에 제거한 사례를 언급합니다. 코팅 아래의 원래 도장 부착 상태에 따라 결과가 달라지므로, 보존 대상 부위는 눈에 띄지 않는 곳에서 낮은 조건으로 먼저 확인합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>방청 왁스 · 코스모린 도포 부위</li><li>애프터마켓 언더코팅</li><li>검사 표시 · 스탬프가 예상되는 부위</li></ul></div>
      <div class="auto-targets auto-contam"><span>주요 오염물</span><p>방청 왁스 · 언더코팅 · 애프터마켓 도막 · 묵은 오염</p></div>
    </div>
  </div>
</article>
</div>

</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">차량 복원 · 디테일링에서<br>반복적으로 마주치는 오염물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/automotive-detailing-removing-oil-and-grime-from-engine-bay-components-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 · 그리스</b><small>OIL & GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/automotive-detailing-cleaning-the-undercarriage-of-a-high-end-vehicle-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>도로 오염물</b><small>ROAD GRIME</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/automotive-detailing-removing-coating-from-wheel-well-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>방청 왁스 · 코스모린</b><small>RUST PREVENTIVE WAX</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/automotive-detailing-dry-ice-blasting-car-frame-of-classic-bmw.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오래된 코팅 · 언더코팅</b><small>AGED COATING</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/automotive-detailing-cleaning-the-wheel-well-of-a-classic-car-with-dry-ice-blasting-topaz-gigapixel-2x-scale.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>먼지 · 흙</b><small>DIRT & DEBRIS</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.30s"><img src="../assets/img/automotive-detailing-cleaning-steering-and-suspension-components-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>표면 산화물</b><small>SURFACE OXIDATION</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.36s"><img src="../assets/img/automotive-detailing-dry-ice-cleaning-detailing-the-undercarriage-of-ferrari.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>하부 침착물</b><small>UNDERBODY BUILDUP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.42s"><img src="../assets/img/automotive-detailing-detailing-a-wheel-hub-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>휠 · 허브 침착물</b><small>WHEEL & HUB BUILDUP</small></span></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">복원 · 디테일링 전문가가 드라이아이스 세척을<br>검토하는 이유입니다.</h2>
  <ol class="auto-why is-6">
    <li class="reveal" style="--reveal-delay:0.00s"><b>물을 사용하지 않는 건식 세척</b><p>커넥터와 센서, 배선이 있는 엔진룸과 하부에 수분을 남기지 않습니다. 마스킹과 건조 대기를 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>비마모성 방식</b><p>원래 도장과 크롬, 알루미늄, 고무와 플라스틱 표면을 갈아내지 않으면서 오염층을 제거하는 데 활용할 수 있습니다. 시리얼 번호와 마킹을 보존해야 하는 작업에 검토됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>좁고 복잡한 부위 접근</b><p>프레임 안쪽과 서스펜션 사이, 하네스 뒤처럼 브러시가 닿지 않는 부위에 노즐로 접근할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>분해를 줄일 수 있는 경우가 있음</b><p>엔진과 변속기, 하부를 장착 상태로 세척할 수 있는 경우가 있어, 반복적인 분해·재조립이 부담인 희소 차량에서 특히 검토됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.36s"><b>입자 크기와 분사 조건 조절</b><p>하부의 두꺼운 오염에는 강한 조건을, 도장과 마킹이 있는 부위에는 미세 입자와 낮은 압력을 사용하는 식으로 한 차량 안에서도 조건을 바꿉니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.45s"><b>세정 매체 자체가 남지 않음</b><p>드라이아이스는 승화하여 남지 않으므로 세척 후 매체를 닦아낼 필요가 없습니다. 단, 떨어진 오염물과 코팅 조각은 바닥에서 회수해야 합니다.</p></li>
  </ol>
</div>

    </div>
  </section>

  <section class="auto-feature">
    <figure class="auto-feature-fig"><img src="../assets/img/automotive-detailing-automotive-restoration-still-1.jpg" alt="" loading="lazy" /><figcaption>클래식카 복원 현장 — 원래 마감을 남기며 오염층만 제거 (Cold Jet)</figcaption></figure>
    <div class="wrap auto-feature-body reveal">
      <span class="cmp-eyebrow">PRESERVE THE DETAILS</span>
      <h2 class="cmp-h2">복원에서는<br>없애야 할 흔적과 남겨야 할 흔적이 다릅니다.</h2>
      <p class="cmp-lead-p">같은 프레임 위에 오일과 방청 왁스, 그리고 공장 검사 표시가 함께 있습니다. 복원 세척은 이 둘을 구분하는 작업입니다. 오염층은 제거하되, 그 아래 원래 마감이 드러나면 멈춰야 합니다. 따라서 보존 대상이 예상되는 부위는 낮은 조건에서 시작해 표면 상태를 확인하며 진행합니다.</p>
      <div class="auto-feature-cols">
        <div class="reveal" style="--reveal-delay:0.20s"><small>제거할 것</small><ul><li>오일 · 그리스 · 도로 오염물</li><li>묵은 방청 왁스 · 코스모린</li><li>애프터마켓 언더코팅 · 후도장</li><li>느슨한 표면 녹 · 불필요한 침착물</li></ul></div>
        <div class="reveal" style="--reveal-delay:0.32s"><small>보존할 가능성이 있는 것</small><ul><li>공장 도장 · OEM 코팅</li><li>검사 표시 · 페인트 도브(paint daub)</li><li>날짜 스탬프 · 시리얼 번호 · 라벨</li><li>원래 마감(original finish) · 파티나</li></ul></div>
      </div>
      <p class="auto-feature-key">복원 세척은 오염물을 지우는 만큼<br><em>어디에서 멈출지</em>를 아는 작업입니다.</p>
    </div>
  </section>
  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 차량 안에서도,<br>부위마다 필요한 세척 조건은 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>하부의 두꺼운 오일과 도로 오염물, 엔진룸의 정밀 부품 사이 오염, 도장과 마킹을 보존해야 하는 부위는 같은 조건으로 세척할 수 없습니다. "강·중·약"의 단순한 등급이 아니라, 대상 표면의 재질과 상태, 오염물의 종류와 두께에 따라 입자 크기와 압력, 노즐과 거리를 맞춥니다.</p>
            <p>바테크는 실제 차량의 부위별 상태를 확인하고, 보존 대상 부위는 눈에 띄지 않는 곳에서 낮은 조건부터 테스트한 뒤 부위별 조건을 정합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/automotive-detailing-cleaning-undercarriage-of-a-high-end-car-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>UNDERBODY</b><small>오일 · 도로 오염물 → 상대적으로 강한 조건</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/automotive-detailing-removing-oil-and-grime-from-engine-bay-components-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><b>ENGINE BAY</b><small>오일 · 먼지 · 정밀부품 → 세밀한 조건 조절</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/automotive-detailing-dry-ice-blasting-car-frame-of-classic-bmw.webp" alt="" loading="lazy" /><b>PAINTED / DELICATE PART</b><small>도장 · 마킹 보존 → 미세 입자 · 낮은 압력 · 사전 테스트</small></li>
          </ul>
          <p class="auto-ae-key">차량 복원에서는 장비의 출력보다<br><em>부위별로 조건을 바꾸는 판단</em>이 결과를 좌우합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relapps-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED APPLICATIONS</span>
      <h2 class="cmp-h2">자동차 복원 · 디테일링에서 함께 살펴볼<br>작업별 솔루션</h2>
    </div>
    <p class="cmp-lead-p">차량 복원 · 디테일링에서 함께 검토되는 작업 유형입니다.</p>
  </div>
  <ul class="auto-relapps">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/oil-grease-residue-removal.html"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>OIL, GREASE & HEAVY RESIDUE REMOVAL</small><b>오일 · 그리스 · 고착 오염 제거</b><span>설비에 고착된 유분·카본·공정 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/rust-corrosion-removal.html"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="auto-relapp-body"><small>RUST, CORROSION & OXIDATION REMOVAL</small><b>녹 · 부식 · 산화물 제거</b><span>표면 녹과 느슨한 산화물(비마모 범위 내)</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../cleaning/task.html#tsk-g2" data-target="../applications/ink-paint-coating-removal.html"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>INK, PAINT & COATING REMOVAL</small><b>잉크 · 도료 · 코팅 제거</b><span>인쇄·도장·코팅 설비의 잉크와 도료 잔류물</span></span><i>→</i></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../cleaning/task.html#tsk-g1" data-target="../applications/electrical-electronic.html"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-relapp-body"><small>ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</small><b>전기 · 전자 장비 세척</b><span>수분을 피해야 하는 모터·제어반·센서·정밀장치</span></span><i>→</i></a></li>
  </ul>
</div>

<div class="cmp-section auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RELATED SOLUTIONS</span>
      <h2 class="cmp-h2">자동차 복원 · 디테일링과<br>함께 살펴볼 분야</h2>
    </div>
    <p class="cmp-lead-p">생산라인의 금형·용접·도장설비 세척은 자동차 제조 페이지에서, 복원·디테일링 전문업체의 폭넓은 작업 영역은 전문 세척 서비스 페이지에서 다룹니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/contract-cleaning.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-cleaning-service.png" alt="" loading="lazy" /></span><small>CONTRACT CLEANING</small><b>전문 세척 서비스</b><span>자세히 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.10s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>자세히 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">RESTORATION & DETAILING IN PRACTICE</span>
      <h2 class="cmp-h2">자동차 복원 · 디테일링 현장의<br>적용 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 Automotive Detailing & Restoration 자료에 소개된 복원·디테일링 전문업체의 경험입니다. 고객 발언은 의미만 요약했으며, 수치는 해당 사례의 조건에서 확인된 결과입니다.</p>
  </div>
  <ul class="mtc-cases auto-field-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>CLASSIC RESTORATION</small><b>1970년대 방청 코팅 제거와 공장 시그니처 노출</b><span>Cold Jet 사례 (복원 전문 샵)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>클래식카 하부 · 프레임</dd></div>
        <div><dt>오염물</dt><dd>1970년대에 도포된 방청 코팅 · 묵은 오염</dd></div>
        <div><dt>기존 방식</dt><dd>수작업 박리 — 수개월 소요 예상</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척으로 코팅층 제거</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>두 시간 이내에 방청 코팅을 제거하고 그 아래 공장 시그니처를 노출했다고 소개 (해당 차량 기준)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>UNDERCARRIAGE</small><b>부식된 하부의 단계적 세척</b><span>Enthusiast Auto Group (Eric Keller)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>수집 차량의 언더바디</dd></div>
        <div><dt>오염물</dt><dd>도로 오염물 · 부식 진행 부위의 오염층</dd></div>
        <div><dt>과제</dt><dd>강한 세정제와 문지르기 없이 부위별로 세척 강도를 조절</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척 — 조건을 높이거나 낮추며 부위별 대응</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>세척 강도를 부위에 따라 조절할 수 있어 세정제 사용 없이 더 깨끗한 결과를 얻었다고 평가 (사용자 발언 요약)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.20s">
      <div class="mtc-case-head"><small>YOUNGTIMER</small><b>영타이머 차량 복원 · 디테일링</b><span>YoungTimer, LLC (Scott Ales)</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>1980~90년대 수집 차량</dd></div>
        <div><dt>오염물</dt><dd>오일 · 먼지 · 도로 오염물</dd></div>
        <div><dt>과제</dt><dd>원래 부품과 마감을 유지하면서 세척</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>복원·디테일링 업계에 잘 맞는 방식이라고 평가 (사용자 발언 요약)</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">차량의 원래 디테일을 유지하면서<br>세척할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>차량 복원은 부위마다 오염물과 표면 상태, 보존해야 할 요소가 다릅니다.</p>
      <p>바테크는 실제 차량 또는 탈거 부품을 확인하고 세척 테스트를 통해 드라이아이스 세척의 적용 가능성과 부위별 작업 조건을 확인합니다. 복원·디테일링 샵의 장비 도입뿐 아니라 렌탈과 현장 지원도 함께 검토할 수 있습니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>

    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">차량의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

WELD_FIXTURE_ROBOT_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/weld-line-cleaning/
       고객사/사례: BMW, GM, Honda, Nissan, Tesla, Toyota, Volkswagen 등 Cold Jet 공식 고객 목록. RobotWorx(로봇 재제조), Maclellan Integrated Services 인용 사례.
       이미지는 프로젝트에 이미 로컬화된 자동차 산업 자료(auto-weld-cell.webp, auto-welding-robot.webp, task-weld-fixture.webp)를 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/auto-weld-cell.webp" alt="로봇 용접셀의 지그와 픽스처" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 용접라인 · 지그 · 로봇 세척</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">WELD LINE CLEANING</span>
      <h1>용접라인 · 지그 · 로봇 세척</h1>
      <p class="cmp-hero-p auto-hero-lead">용접 스패터와 슬래그는 제거하고,<br>지그와 로봇의 정렬 상태는 고려합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">WELD CELL MAINTENANCE</span>
      <h2 class="cmp-h2">용접 스패터는<br>보이는 것보다 넓게 쌓입니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>용접 공정이 반복될수록 픽스처와 지그, 클램프와 센서 주변, 로봇 관절부에는 스패터와 슬래그, 그을음이 축적됩니다. Cold Jet 자료에 따르면 이러한 오염은 부품 정렬 불량, 오검지, 스패터 브리징과 용접 결함의 원인이 될 수 있습니다.</p>
      <p>기존에는 치즐과 해머, 스크레이퍼, 화학용제를 이용한 수작업으로 픽스처 1개에 1~1.5시간, 대형 용접셀 전체에는 5~6시간이 걸리는 경우도 있었습니다. 이 과정에서 프록시미티 스위치나 센서, 케이블이 손상될 위험도 있습니다.</p>
      <p class="auto-intro-close">드라이아이스 세척은 <b>스패터와 슬래그는 제거하면서 지그의 정렬과 센서·배선의 상태를 고려하는</b> 방식으로 활용할 수 있습니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">WELD LINE APPLICATIONS</span>
    <h2 class="cmp-h2">지그의 정렬과<br>로봇의 정밀도를 함께 고려합니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">WELDING FIXTURES &amp; JIGS</span>
      <h3>용접 픽스처 · 지그</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-weld-fixture.webp" alt="용접 픽스처 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-weld-cell.webp" alt="용접셀 지그 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">픽스처와 지그에 쌓인 스패터를<br>정렬을 유지하며 제거합니다.</p>
      <div class="cmp-text auto-text"><p>용접 픽스처와 트러니언, 셔틀 지그, 다이아몬드 플레이트, 용접 테이블에는 스패터와 슬래그, 그을음이 반복적으로 쌓입니다. Cold Jet 자료에 따르면 이 오염은 부품 정렬과 프록시미티 스위치의 오검지에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 금속면을 연마하지 않는 방식으로, 픽스처의 치수 기준면과 클램프 형상을 고려하면서 스패터를 제거하는 데 활용할 수 있습니다. 조건에 따라 라인 안에서 분해 없이 세척한 사례가 있어, 세척 주기를 더 자주 가져가는 데 도움이 될 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>용접 픽스처 · 지그</li><li>트러니언 · 셔틀 지그</li><li>다이아몬드 플레이트 · 용접 테이블</li><li>프록시미티 스위치 · 센서 · 케이블</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">WELDING ROBOTS</span>
      <h3>용접 로봇</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-welding-robot.webp" alt="용접 로봇 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-weld-cell.webp" alt="로봇 용접셀 전경" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">분해하지 않고,<br>관절부와 엔드이펙터를 세척합니다.</p>
      <div class="cmp-text auto-text"><p>로봇 100대 이상을 운용하는 대형 용접셀에서는 수작업 세척에 셀 하나당 5~6시간이 걸리는 경우도 있다고 Cold Jet 자료는 설명합니다. 로봇팔과 관절, 엔드이펙터, 용접건, 와이어 피더, 토치 노즐, 서보모터에도 스패터가 축적됩니다.</p><p>드라이아이스 세척은 로봇을 분해하지 않고 이 부위들을 세척하는 데 활용할 수 있으며, 비전도성 특성으로 배선과 서보모터 주변 세척에도 검토됩니다. 다만 활선 상태 세척 가능 여부는 로봇 제조사 기준과 현장 안전조건을 별도로 확인해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>로봇팔 · 관절부</li><li>엔드이펙터 · 용접건</li><li>와이어 피더 · 토치 노즐</li><li>로봇 베이스 · 서보모터 · 케이블 하니스</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">용접 공정에서<br>반복적으로 쌓이는 오염물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>용접 스패터</b><small>WELD SPATTER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-weld-cell.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>슬래그</b><small>WELD SLAG</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/auto-welding-robot.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>그을음 잔류물</b><small>SMOKE RESIDUE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>그리스 · 공정 잔류물</b><small>GREASE &amp; PROCESS BUILDUP</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">스패터를 없애는 방법이<br>지그의 정렬을 흐트러뜨려서는 안 됩니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성 세척</b><p>연마재로 깎아내는 방식이 아니므로, 반복 세척에도 픽스처의 치수 기준면과 클램프 형상을 고려할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>센서·배선 주변 접근</b><p>드라이아이스는 비전도성 특성이 있어 프록시미티 스위치, 센서, 케이블 주변 세척에 활용됩니다. 단, 활선 상태 세척은 설비 기준과 안전조건을 별도로 확인해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 승화하므로 매체 자체는 남지 않습니다. 제거된 스패터와 슬래그는 쓸어내거나 흡입해 처리합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>분해 없이 현장 세척</b><p>적용 조건에 따라 로봇과 픽스처를 분해하지 않고 라인 안에서 세척할 수 있는 경우가 있어, 정기적인 예방정비 일정을 세우는 데 도움이 될 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">지그의 스패터와<br>로봇의 관절부는 조건이 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>픽스처 표면에 고착된 스패터와 로봇 관절부의 얇은 잔류물, 센서 주변의 미세 오염은 같은 조건으로 세척할 수 없습니다.</p>
            <p>바테크는 실제 픽스처와 로봇을 확인하고 세척 테스트를 통해 입자 크기, 분사 압력, 노즐, 분사 거리와 각도를 조정해 적합한 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><b>용접 픽스처</b><small>스패터 · 슬래그</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/auto-welding-robot.webp" alt="" loading="lazy" /><b>용접 로봇 관절부</b><small>스패터 · 그리스</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/auto-weld-cell.webp" alt="" loading="lazy" /><b>센서 · 케이블 주변</b><small>미세 오염</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">INDUSTRIES</span>
      <h2 class="cmp-h2">용접라인은<br>다양한 제조 현장에 존재합니다.</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 용접라인 세척 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE &amp; AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/medical.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></span><small>MEDICAL DEVICE MANUFACTURING</small><b>의료기기 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/foundry.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-foundry.png" alt="" loading="lazy" /></span><small>FOUNDRY &amp; DIE CASTING</small><b>주조 · 다이캐스팅</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">WELD LINE CLEANING IN PRACTICE</span>
      <h2 class="cmp-h2">용접라인 세척에서<br>확인된 적용 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 용접라인 세척 자료에 소개된 사용 기업입니다. 아래 사례는 각 현장의 조건에서 확인된 결과이며, 모든 용접셀에 같은 결과를 보장하는 것은 아닙니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 용접라인 세척을 사용하는 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:42%"><img src="../assets/img/logo-bmw.webp" alt="BMW" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:40%"><img src="../assets/img/logo-gm.webp" alt="General Motors" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:44%"><img src="../assets/img/logo-honda.webp" alt="Honda" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:58%"><img src="../assets/img/logo-nissan.webp" alt="Nissan" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:56%"><img src="../assets/img/logo-tesla.webp" alt="Tesla" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.20s; --w:64%"><img src="../assets/img/logo-toyota.webp" alt="Toyota" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.24s; --w:70%"><img src="../assets/img/logo-volkswagen.webp" alt="Volkswagen" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.28s; --w:74%"><img src="../assets/img/logo-robotworx.png" alt="RobotWorx" loading="lazy" /></li>
  </ul>
  <ul class="mtc-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>ROBOT REFURBISHING</small><b>산업용 로봇 재제조</b><span>RobotWorx</span></div>
      <dl>
        <div><dt>세척 대상</dt><dd>재제조용 산업용 로봇 전체</dd></div>
        <div><dt>기존 방식</dt><dd>화학용제를 이용한 수작업 세척 — 로봇 부품 손상 우려, 초기 세척에 시간 소요</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척으로 초기 세척 공정 대체</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>로봇 부품 손상 없이 세척했고, 화학용제 방식보다 빠르게 초기 세척을 마쳤다고 보고 (사용자 인용)</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>INTEGRATED SERVICES</small><b>산업 설비 유지보수</b><span>Maclellan Integrated Services</span></div>
      <dl>
        <div><dt>기존 방식</dt><dd>수작업 세척 중심의 정비 일정</dd></div>
        <div><dt>적용</dt><dd>드라이아이스 세척 도입</dd></div>
      </dl>
      <p class="mtc-case-result"><span>확인된 결과</span>동일 인력으로 2~3배 많은 작업을 처리할 수 있었다고 보고 (사용자 인용)</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR WELD LINE</span>
    <h2 class="cmp-h2">우리 용접라인의 스패터도<br>세척할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>픽스처의 형상과 오염 상태, 로봇의 구조와 안전조건에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 픽스처 또는 로봇을 확인하고 세척 테스트를 통해 적용 가능성과 적절한 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

PAINT_BOOTH_COATING_LINE_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/facility-maintenance/ (Industrial Robotics: overspray 제거)
       https://www.coldjet.com/dry-ice-blasting/industries/automotive-manufacturing/ (Paint Booth & Coating Line)
       이미지는 프로젝트에 이미 로컬화된 자동차 산업 자료(auto-paint-booth-fixture.webp, auto-paint-prep.webp) 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/auto-paint-booth-fixture.webp" alt="도장부스 설비의 오버스프레이 세척" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 도장부스 · 코팅라인 세척</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">PAINT BOOTH &amp; COATING LINE CLEANING</span>
      <h1>도장부스 · 코팅라인 세척</h1>
      <p class="cmp-hero-p auto-hero-lead">도료가 쌓이는 설비를 관리해야,<br>도장라인도 안정적으로 유지할 수 있습니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">OVERSPRAY BUILDUP</span>
      <h2 class="cmp-h2">이 페이지는 도장을 벗기는 작업이 아니라,<br>도장설비를 관리하는 작업을 다룹니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>도장부스의 벽면과 그레이팅, 스키드와 행거, 도장 로봇에는 도료 비산 잔류물(오버스프레이)이 반복적으로 쌓입니다. 두껍게 축적되면 부스 환기와 도막 품질, 로봇의 센서·관절 동작에 영향을 줄 수 있습니다.</p>
      <p>중요한 구분이 있습니다. 제품 표면의 도막을 벗겨내는 작업과, 도장 설비에 쌓인 오버스프레이를 제거하는 작업은 다릅니다. 이 페이지는 후자, 즉 <b>설비 유지보수로서의 도장라인 세척</b>을 다룹니다.</p>
      <p class="auto-intro-close">드라이아이스 세척은 금속면과 도장 로봇의 센서·배선을 고려하면서 <b>설비에 쌓인 오버스프레이를 제거하는 데</b> 활용할 수 있습니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">PAINT LINE APPLICATIONS</span>
    <h2 class="cmp-h2">부스 구조물과 도장 로봇,<br>쌓이는 방식이 다릅니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">BOOTH STRUCTURE &amp; FIXTURES</span>
      <h3>부스 그레이팅 · 스키드 · 행거</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-paint-booth-fixture.webp" alt="도장부스 그레이팅 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-paint-prep.webp" alt="도장 지그 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">두껍게 고착된 오버스프레이를<br>구조물 형상을 고려하며 제거합니다.</p>
      <div class="cmp-text auto-text"><p>도장부스 벽면과 그레이팅, 스키드, 캐리어, 행거, 가이드레일에는 도료 비산 잔류물이 겹겹이 쌓여 시간이 지날수록 두껍고 단단해집니다. 방치하면 그레이팅의 통풍 상태와 부스 환경에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 금속 구조물을 연마하지 않는 방식으로, 조건에 따라 설비를 완전히 분해하지 않고 세척할 수 있어 정기적인 관리 주기를 가져가는 데 도움이 될 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>도장부스 벽면 · 그레이팅</li><li>스키드 · 캐리어 · 행거</li><li>가이드레일 · 컨베이어 픽스처</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">PAINT ROBOTS</span>
      <h3>도장 로봇</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-paint-prep.webp" alt="도장 로봇 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-paint-booth-fixture.webp" alt="도장 로봇팔 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">센서와 배선을 고려하면서<br>로봇팔의 오버스프레이를 제거합니다.</p>
      <div class="cmp-text auto-text"><p>Cold Jet 자료에 따르면 도장·용접·물류 로봇의 관절과 배선, 엔드오브암 툴링 주변에 쌓이는 공정 잔류물은 위치 정확도와 센서 오작동에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 로봇을 분해하지 않고 이 부위를 세척하는 데 활용되며, 이를 통해 로봇이 정지 없이 빠르게 작업에 복귀하는 데 도움이 될 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>도장 로봇팔 · 관절부</li><li>엔드오브암 툴링</li><li>센서 하우징 · 케이블 하니스</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">도장라인에서<br>반복적으로 쌓이는 오염물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/auto-paint-booth-fixture.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>도료 비산 잔류물</b><small>PAINT OVERSPRAY</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-paint-prep.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>프라이머 · 실러 잔류물</b><small>PRIMER &amp; SEALER</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/plastics-composites-dry-ice-blasting-cleaning-automotive-parts-prior-to-painting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>접착제 잔류물</b><small>ADHESIVE RESIDUE</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">도장을 제거하는 것과<br>도장설비를 세척하는 것은 다른 작업입니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성 세척</b><p>제품의 정상 도막이 아닌 설비에 축적된 오버스프레이 제거를 목적으로 하며, 금속 구조물 표면을 깎아내지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>물을 사용하지 않는 건식 세척</b><p>수분이 남지 않아 도장부스 특유의 부식·녹 발생 우려를 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 승화하므로 매체 자체가 부스 내부에 남지 않습니다. 제거된 오버스프레이는 별도로 회수·처리합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>복잡한 구조물 접근</b><p>그레이팅 틈과 로봇 관절부처럼 복잡한 형상에도 노즐과 분사 조건을 조정해 접근할 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">그레이팅의 두꺼운 오버스프레이와<br>로봇의 얇은 잔류물은 조건이 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>부스 구조물에 겹겹이 고착된 오버스프레이와, 로봇 관절부에 얇게 남은 잔류물은 필요한 분사 강도와 입자 크기가 다릅니다.</p>
            <p>바테크는 실제 설비와 오염 상태를 확인하고 세척 테스트를 통해 적합한 세척 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/auto-paint-booth-fixture.webp" alt="" loading="lazy" /><b>부스 그레이팅</b><small>고착 오버스프레이</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/auto-paint-prep.webp" alt="" loading="lazy" /><b>도장 로봇 관절부</b><small>얇은 잔류물</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">INDUSTRIES</span>
      <h2 class="cmp-h2">도장·코팅 공정은<br>여러 산업에 걸쳐 있습니다.</h2>
    </div>
    <p class="cmp-lead-p">도장부스와 코팅라인은 자동차뿐 아니라 다양한 생산현장에 존재합니다.</p>
  </div>
  <ul class="auto-relind is-2">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE &amp; AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">PAINT LINE CLEANING IN PRACTICE</span>
      <h2 class="cmp-h2">도장라인 유지보수에서<br>확인된 적용 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 자동차·시설 유지보수 자료에서 확인되는 사용 기업입니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 도장라인 세척을 사용하는 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:42%"><img src="../assets/img/logo-bmw.webp" alt="BMW" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:58%"><img src="../assets/img/logo-ford.webp" alt="Ford" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:40%"><img src="../assets/img/logo-gm.webp" alt="General Motors" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.12s; --w:66%"><img src="../assets/img/logo-hyundai.webp" alt="Hyundai" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.16s; --w:64%"><img src="../assets/img/logo-kia.png" alt="Kia" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR PAINT LINE</span>
    <h2 class="cmp-h2">우리 도장라인의 오버스프레이도<br>관리할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>부스 구조물의 재질과 오염 축적 정도, 로봇의 구조에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 설비 또는 샘플을 확인하고 세척 테스트를 통해 적용 가능성과 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

ELECTRICAL_ELECTRONIC_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/facility-maintenance/ (Electrical Systems & Motors)
       https://www.coldjet.com/dry-ice-blasting/applications/electronic-device-refurbishing/ (정밀 전자부품 · PCB 관련 내용만 산업용 맥락으로 발췌)
       이미지는 로컬화된 자료(auto-facility-motor.jpg, method-electrical-terminal.png, semiconductor-cleaning-pcb-board...webp, power-generation-...electrical-substation.webp) 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/power-generation-dry-ice-blasting-being-used-to-clean-a-high-voltage-insulator-at-an-electrical-substation.webp" alt="전기설비 세척" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 전기 · 전자 장비 세척</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">ELECTRICAL &amp; ELECTRONIC EQUIPMENT CLEANING</span>
      <h1>전기 · 전자 장비 세척</h1>
      <p class="cmp-hero-p auto-hero-lead">건식·비전도성 세척으로,<br>전기설비와 정밀 전자부품을 함께 고려합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">DUST, OIL MIST &amp; CARBON TRACKING</span>
      <h2 class="cmp-h2">전기·전자 설비의 오염은<br>고장의 원인이 될 수 있습니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>모터 권선과 배전반, 제어반, PCB와 커넥터에는 먼지, 오일 미스트, 카본 트래킹, 플럭스·접착 잔류물이 쌓입니다. Cold Jet 자료에 따르면 이러한 오염은 절연 저하와 과열, 단락의 원인이 될 수 있습니다.</p>
      <p>물세척은 전기설비에 단락 위험을 남기고, 화학용제는 PCB나 정밀 부품에 잔류물을 남길 수 있습니다. 드라이아이스는 물을 사용하지 않고 비전도성 특성이 있어 이러한 제약을 줄이는 방향으로 검토됩니다.</p>
      <p class="auto-intro-close">단, 이 특성이 <b>모든 활선 설비를 안전하게 세척할 수 있다는 의미는 아닙니다.</b> 전원 상태와 제조사 기준, 절연 상태와 현장 안전조건을 확인한 뒤 적용을 검토합니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">ELECTRICAL &amp; ELECTRONIC APPLICATIONS</span>
    <h2 class="cmp-h2">대형 전기설비와<br>정밀 전자부품은 접근이 다릅니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div>
      <span class="auto-en">INDUSTRIAL ELECTRICAL SYSTEMS</span>
      <h3>산업용 전기 · 제어설비</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-facility-motor.jpg" alt="전동기 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/method-electrical-terminal.png" alt="전기 단자함 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">권선과 배전반의 먼지·오일을<br>절연 상태를 고려하며 제거합니다.</p>
      <div class="cmp-text auto-text"><p>전동기 권선과 냉각통로, 배전반과 스위치기어, 브레이커 패널, 접속함, MCC, PLC 캐비닛, HMI 인클로저, VFD에는 먼지와 오일 미스트, 카본 트래킹이 축적됩니다.</p><p>드라이아이스 세척은 절연체를 손상시키지 않으면서 이 오염을 제거하는 데 활용됩니다. 적용 조건에 따라 설비를 분해하지 않고 세척한 사례가 있으나, 활선 상태 세척 가능 여부는 전원 차단 절차와 제조사 기준, 절연 상태를 별도로 확인해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>전동기 권선 · 냉각팬</li><li>배전반 · 스위치기어 · 접속함</li><li>MCC · PLC 캐비닛 · HMI · VFD</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div>
      <span class="auto-en">PRECISION ELECTRONICS</span>
      <h3>정밀 전자부품</h3>
    </div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/semiconductor-cleaning-pcb-board-after-welding-with-dry-ice-cleaning.webp" alt="PCB 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/method-electrical-terminal.png" alt="커넥터 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">미세입자로 조절해<br>PCB와 커넥터를 세척합니다.</p>
      <div class="cmp-text auto-text"><p>PCB, 전자 어셈블리, 커넥터, 하우징에는 납땜 후 플럭스 잔류물, 라벨·접착제 잔류물, 조립 공정 부산물이 남을 수 있습니다.</p><p>드라이아이스는 물을 사용하지 않는 방식으로, 미세입자(MicroParticle)로 조절해 노출된 PCB와 정밀 커넥터의 잔류물을 제거하는 데 활용됩니다. 조건에 따라 로봇 자동화 라인에 통합해 사용한 사례도 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>PCB · 전자 어셈블리</li><li>커넥터 · 하우징</li><li>플럭스 · 라벨 · 접착 잔류물</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">전기·전자 설비에서<br>반복적으로 쌓이는 오염물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>먼지</b><small>DUST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 미스트</b><small>OIL MIST</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.16s"><img src="../assets/img/mining-cleaning-control-box-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>카본 트래킹</b><small>CARBON TRACKING</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.24s"><img src="../assets/img/semiconductor-cleaning-pcb-board-after-welding-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>플럭스 · 접착 잔류물</b><small>FLUX &amp; ADHESIVE RESIDUE</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">비전도성이라는 특성이,<br>모든 활선 세척을 뜻하지는 않습니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비전도성 · 건식 세척</b><p>물을 사용하지 않는 비전도성 방식으로, 절연체와 배선 주변 세척에 검토됩니다. 활선 상태 세척은 전원 차단 절차와 현장 안전기준을 별도로 확인해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>비마모성 세척</b><p>PCB의 미세 회로나 커넥터 단자를 마모시키지 않는 방식으로, 미세입자를 사용해 민감한 부품에 대응할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 승화하므로 회로 기판에 매체 자체가 남지 않습니다. 제거된 오염물은 별도로 회수·처리합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>분해 없이 현장 세척</b><p>적용 조건에 따라 설비를 완전히 분해하지 않고 세척할 수 있는 경우가 있어, 정비시간을 줄이는 데 도움이 될 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">대형 설비의 오염과<br>PCB의 오염은 다른 조건이 필요합니다.</h2>
          <div class="cmp-dark-body">
            <p>전동기 권선의 먼지·오일과, PCB의 플럭스 잔류물은 필요한 입자 크기와 분사 강도가 전혀 다릅니다.</p>
            <p>바테크는 실제 설비와 오염 상태, 전원 상태와 안전조건을 확인한 뒤 세척 테스트를 통해 적합한 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /><b>전동기 · 배전반</b><small>먼지 · 오일 · 카본 트래킹</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/semiconductor-cleaning-pcb-board-after-welding-with-dry-ice-cleaning.webp" alt="" loading="lazy" /><b>PCB · 커넥터</b><small>플럭스 · 접착 잔류물</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건과 안전조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">INDUSTRIES</span>
      <h2 class="cmp-h2">전기·전자 설비는<br>거의 모든 산업에 존재합니다.</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 전기·전자 장비 세척 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/semiconductor.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-semiconductor.png" alt="" loading="lazy" /></span><small>SEMICONDUCTOR &amp; ELECTRONICS</small><b>반도체 · 전자 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/power-generation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></span><small>POWER GENERATION</small><b>발전 · 전력</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/facility-maintenance.html"><span class="auto-relind-img"><img src="../assets/img/facility-volpak-machine-cleaning.webp" alt="" loading="lazy" /></span><small>FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div>
      <span class="cmp-eyebrow">ELECTRICAL CLEANING IN PRACTICE</span>
      <h2 class="cmp-h2">전기 · 전자 설비 세척에서<br>확인된 적용 경험</h2>
    </div>
    <p class="cmp-lead-p">Cold Jet 공식 시설 유지보수 자료에서 확인되는 사용 기업입니다.</p>
  </div>
  <ul class="auto-logos is-flex" aria-label="Cold Jet 전기설비 세척을 사용하는 기업">
    <li class="reveal-pop" style="--reveal-delay:0.00s; --w:42%"><img src="../assets/img/logo-bmw.webp" alt="BMW" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.04s; --w:58%"><img src="../assets/img/logo-ford.webp" alt="Ford" loading="lazy" /></li>
    <li class="reveal-pop" style="--reveal-delay:0.08s; --w:40%"><img src="../assets/img/logo-gm.webp" alt="General Motors" loading="lazy" /></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR EQUIPMENT</span>
    <h2 class="cmp-h2">우리 전기·전자 설비에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>설비의 종류와 전원 상태, 오염 상태와 현장 안전조건에 따라 적용 가능성과 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 설비를 확인하고 세척 테스트를 통해 적용 가능성과 적절한 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

# (2026-09-08 12차 핸드오프, batch3) 작업별 솔루션 잔여 6페이지 — 신규 다운로드 없이 기존 로컬 이미지만 재사용.
ADHESIVE_RESIN_REMOVAL_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/adhesive-removal/
       이미지: 기존 로컬 자료(task-adhesive-rollers.webp, printing-dry-ice-blasting-removing-burnished-ink-and-adhesive-from-packaging-line.webp,
       packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp) 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/task-adhesive-rollers.webp" alt="접착제가 축적된 롤러 세척" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 접착제 · 수지 제거</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">ADHESIVE &amp; RESIN REMOVAL</span>
      <h1>접착제 · 수지 제거</h1>
      <p class="cmp-hero-p auto-hero-lead">붙어야 할 곳에서는 중요한 접착제도,<br>설비에 쌓이면 생산을 방해하는 오염물이 됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">BUILDUP ON EQUIPMENT</span>
      <h2 class="cmp-h2">접착제 자체가 아니라,<br>설비에 축적된 접착제가 문제입니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>글루건 노즐, 라벨링 헤드, 컨베이어 롤러, 박스 성형기, 포장설비, 접합 지그와 성형 다이에는 핫멜트, PSA(감압점착제), 라벨 접착제, 에폭시, 우레탄, 실리콘 실런트, 경화된 수지가 반복적으로 쌓입니다.</p>
      <p>Cold Jet 자료에 따르면 이러한 잔류물은 노즐 막힘, 라벨 정렬 불량, 롤러 표면 오염으로 인한 제품 결함의 원인이 될 수 있습니다. 기존에는 화학용제나 스크레이퍼로 수작업 제거하는 경우가 많았습니다.</p>
      <p class="auto-intro-close">드라이아이스 세척은 <b>화학용제 사용을 줄이면서 롤러와 노즐의 정밀한 표면을 고려하는</b> 방식으로 활용할 수 있습니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">ADHESIVE REMOVAL APPLICATIONS</span>
    <h2 class="cmp-h2">포장·인쇄 설비와<br>생산·조립 설비는 접착 오염 양상이 다릅니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div><span class="auto-en">PACKAGING &amp; PRINTING EQUIPMENT</span><h3>포장 · 인쇄 설비</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-adhesive-rollers.webp" alt="접착제 롤러 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/printing-dry-ice-blasting-removing-burnished-ink-and-adhesive-from-packaging-line.webp" alt="포장라인 접착제 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">글루건과 롤러의 접착 잔류물을<br>정밀 표면을 고려하며 제거합니다.</p>
      <div class="cmp-text auto-text"><p>글루건 노즐, 라벨링 헤드, 컨베이어 롤러, 박스 성형기에는 핫멜트와 라벨 접착제가 굳어 붙습니다. 이 잔류물이 쌓이면 접착량이 불균일해지거나 라벨이 밀리는 등 제품 품질에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 롤러의 정밀한 표면과 형상을 연마하지 않는 방식으로, 조건에 따라 라인을 분해하지 않고 세척할 수 있어 정기적인 관리 주기를 가져가는 데 도움이 될 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>글루건 · 노즐</li><li>라벨링 헤드 · 박스 성형기</li><li>컨베이어 롤러 · 포장설비</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div><span class="auto-en">MANUFACTURING &amp; ASSEMBLY</span><h3>생산 · 조립 설비</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp" alt="기어·스타휠 접착 잔류물 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/task-adhesive-rollers.webp" alt="접합 지그 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">경화된 에폭시와 실런트를<br>지그 형상을 고려하며 제거합니다.</p>
      <div class="cmp-text auto-text"><p>접합 지그, 복합재 툴링, 성형 다이, 프레스 공구에는 에폭시, 우레탄, 실리콘 실런트, 경화된 수지가 부착됩니다. 경화 정도와 표면 결합 상태에 따라 제거 난이도가 달라집니다.</p><p>드라이아이스 세척은 화학용제나 과도한 기계적 제거 없이 이러한 잔류물을 제거하는 데 활용할 수 있습니다. 다만 수지의 종류와 경화 상태에 따라 결과가 달라질 수 있어 사전 테스트를 권장합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>접합 지그 · 복합재 툴링</li><li>성형 다이 · 프레스 공구</li><li>생산설비 부착부</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">접착제 · 수지 종류에 따라<br>부착 양상이 다릅니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>핫멜트 · PSA</b><small>HOT MELT &amp; PSA</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/printing-dry-ice-blasting-removing-burnished-ink-and-adhesive-from-packaging-line.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>라벨 접착제</b><small>LABEL ADHESIVE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>에폭시 · 우레탄</b><small>EPOXY &amp; POLYURETHANE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>실리콘 실런트</b><small>SILICONE SEALANT</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">화학용제를 줄이면서,<br>정밀한 표면은 고려합니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>화학용제 사용 감소</b><p>용제 기반 제거 방식과 비교해 화학약품 사용을 줄이는 방향으로 검토할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>좁은 노즐 · 롤러 접근</b><p>노즐과 분사 조건을 조절해 좁은 틈과 롤러 표면, 지그의 복잡한 형상에 접근할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>표면 형상 유지</b><p>비마모성 방식으로 롤러와 지그의 정밀한 형상과 표면 상태를 고려하면서 접착 잔류물을 제거합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>현장 세척 가능성</b><p>적용 조건에 따라 설비를 분해하지 않고 라인 안에서 세척할 수 있는 경우가 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">얇은 라벨 접착제와<br>경화된 에폭시는 조건이 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>접착제의 종류, 경화 상태, 두께, 표면과의 결합 정도에 따라 필요한 세척 조건은 달라집니다. 수지를 모두 제거할 수 있다고 일반화하지 않습니다.</p>
            <p>바테크는 실제 부품이나 시편을 확인하고 세척 테스트를 통해 입자 크기, 분사 압력, 노즐, 분사 거리와 각도를 조정해 적합한 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><b>라벨링 롤러</b><small>핫멜트 · PSA</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/packaging-dry-ice-blasting-cleaning-gears-and-star-wheels-on-packaging-line.webp" alt="" loading="lazy" /><b>포장라인 기어</b><small>라벨 접착제</small></li>
            <li class="reveal" style="--reveal-delay:0.63s"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><b>접합 지그</b><small>에폭시 · 실런트</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">INDUSTRIES</span><h2 class="cmp-h2">접착제 오염은<br>여러 산업의 생산라인에 존재합니다.</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 접착제 제거 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS &amp; COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE &amp; AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/semiconductor.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-semiconductor.png" alt="" loading="lazy" /></span><small>SEMICONDUCTOR &amp; ELECTRONICS</small><b>반도체 · 전자 제조</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">ADHESIVE REMOVAL IN PRACTICE</span><h2 class="cmp-h2">포장 · 생산현장에서<br>확인된 적용 경험</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 Adhesive Removal 자료에서 확인되는 적용 사례입니다. 아래 사례는 각 현장의 조건에서 확인된 결과이며, 모든 접착제·설비에 같은 결과를 보장하는 것은 아닙니다.</p>
  </div>
  <ul class="mtc-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>PACKAGING LINE</small><b>라벨링 롤러 접착제 제거</b><span>Cold Jet 공식 사례</span></div>
      <dl><div><dt>기존 방식</dt><dd>화학용제를 이용한 수작업 세척 — 라인 정지 시간 소요</dd></div><div><dt>적용</dt><dd>드라이아이스 세척으로 라인 내 세척</dd></div></dl>
      <p class="mtc-case-result"><span>확인된 결과</span>화학용제 사용을 줄이고 세척시간을 단축했다고 보고</p>
    </li>
    <li class="reveal" style="--reveal-delay:0.10s">
      <div class="mtc-case-head"><small>PRINTING &amp; PACKAGING</small><b>포장설비 접착 잔류물 관리</b><span>Cold Jet 공식 사례</span></div>
      <dl><div><dt>세척 대상</dt><dd>기어 · 스타휠 · 컨베이어</dd></div><div><dt>적용</dt><dd>정기 예방정비 일정에 드라이아이스 세척 도입</dd></div></dl>
      <p class="mtc-case-result"><span>확인된 결과</span>설비 분해 없이 정기 세척이 가능해졌다고 보고</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">현재 사용 중인 접착제도<br>제거할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>접착제의 종류와 경화 상태, 세척 대상의 재질과 형상에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 부품 또는 샘플을 확인하고 세척 테스트를 통해 적용 가능성과 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""


INK_PAINT_COATING_REMOVAL_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/printing/ (구 Ink & Coating Removal 성격 자료 포함)
       + Coatings & Corrosion 자료 중 Abrasive-assisted 구분 언급만 참고(순수 드라이아이스 범위 밖은 별도 명시).
       이미지: printing-*.webp, task-pretreatment.jpg 기존 로컬 자료 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/printing-dry-ice-blasting-removes-heavy-ink-and-grease-buildup-from-printing-press.webp" alt="인쇄기 잉크 잔류물 세척" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 잉크 · 도료 · 코팅 제거</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">INK, PAINT &amp; COATING REMOVAL</span>
      <h1>잉크 · 도료 · 코팅 제거</h1>
      <p class="cmp-hero-p auto-hero-lead">설비에 축적된 잉크와 도료,<br>코팅 잔류물을 관리합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">SETTING EXPECTATIONS</span>
      <h2 class="cmp-h2">드라이아이스 세척으로<br>다룰 수 있는 범위를 먼저 구분합니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>인쇄설비에 남는 잉크·바니시 잔류물과, 생산설비에 쌓이는 도료 비산 잔류물(오버스프레이)·코팅 부산물은 드라이아이스 세척의 대표적인 적용 영역입니다.</p>
      <p class="auto-intro-close">다만 <b>강하게 부착된 산업용 도막 전체를 박리하거나, 재도장을 위한 표면 프로파일을 만드는 작업</b>은 순수 드라이아이스 세척과 목적이 다릅니다. 이런 경우 Cold Jet는 드라이아이스와 연마재를 함께 사용하는 별도의 공정을 안내하며, 이 페이지는 그 범위를 다루지 않습니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">CLEANING APPLICATIONS</span>
    <h2 class="cmp-h2">인쇄설비와 생산설비,<br>쌓이는 잔류물의 성질이 다릅니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div><span class="auto-en">PRINTING EQUIPMENT</span><h3>인쇄설비의 잉크 · 바니시</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/printing-cleaning-ink-try-with-dry-ice-blasting.webp" alt="인쇄기 잉크 트레이 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/printing-large-printing-press-cleaned-with-dry-ice-blasting.webp" alt="대형 인쇄기 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">실린더와 잉크 트레이의<br>고착 잉크를 정밀하게 제거합니다.</p>
      <div class="cmp-text auto-text"><p>플렉소·그라비어·옵셋 인쇄기의 실린더, 롤러, 닥터블레이드, 잉크 트레이에는 잉크와 바니시가 굳어 붙습니다. Cold Jet 자료에 따르면 이 잔류물은 인쇄 품질과 색상 일관성에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 실린더의 정밀한 표면을 연마하지 않는 방식으로, 색상 교체 시 세척시간을 줄이는 데 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>인쇄 실린더 · 롤러</li><li>닥터블레이드 · 잉크 트레이</li><li>플렉시블 포장설비</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div><span class="auto-en">PRODUCTION EQUIPMENT</span><h3>생산설비의 오버스프레이</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-pretreatment.jpg" alt="도장 지그 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/printing-dry-ice-blasting-removes-heavy-ink-and-grease-buildup-from-printing-press.webp" alt="설비 코팅 잔류물 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">도료 비산 잔류물과<br>코팅 부산물을 관리합니다.</p>
      <div class="cmp-text auto-text"><p>도장 지그, 캐리어, 컨베이어, 코팅 어플리케이터에는 도료 비산 잔류물과 코팅 부산물이 겹겹이 쌓입니다. 방치하면 설비 움직임과 도장환경 관리에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 이 잔류물을 설비 표면을 고려하며 제거하는 데 활용할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>도장 지그 · 캐리어</li><li>컨베이어 · 로봇</li><li>코팅 어플리케이터</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">인쇄 · 도장 · 코팅 공정에서<br>반복적으로 쌓이는 잔류물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/printing-cleaning-ink-try-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>잉크</b><small>INK</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/printing-large-printing-press-cleaned-with-dry-ice-blasting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>바니시</b><small>VARNISH</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>도료 비산 잔류물</b><small>PAINT OVERSPRAY</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/printing-dry-ice-blasting-removes-heavy-ink-and-grease-buildup-from-printing-press.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>코팅 부산물</b><small>COATING BUILDUP</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">실린더와 롤러의 정밀도를<br>유지하면서 잔류물을 제거합니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성 세척</b><p>인쇄 실린더의 정밀한 표면과 패턴을 연마하지 않는 방식으로 잔류물을 제거합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>색상 교체 세척시간 단축 가능성</b><p>조건에 따라 분해 없이 세척할 수 있어 인쇄물 색상 전환 시 세척시간을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 승화하므로 매체 자체는 남지 않습니다. 제거된 잉크·도료는 별도로 회수·처리합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>물 없는 건식 세척</b><p>수분이 인쇄 품질에 영향을 줄 수 있는 설비에서 건식 세척 방식을 검토할 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">인쇄 실린더의 얇은 잉크와<br>설비의 두꺼운 코팅은 조건이 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>실린더에 얇게 남은 잉크와, 도장 지그에 겹겹이 고착된 오버스프레이는 필요한 입자 크기와 분사 강도가 다릅니다.</p>
            <p>바테크는 실제 설비와 잔류물 상태를 확인하고 세척 테스트를 통해 적합한 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/printing-cleaning-ink-try-with-dry-ice-blasting.webp" alt="" loading="lazy" /><b>인쇄 실린더</b><small>잉크 · 바니시</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><b>도장 지그</b><small>오버스프레이</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">INDUSTRIES</span><h2 class="cmp-h2">인쇄 · 도장 · 코팅 공정은<br>다양한 산업에 걸쳐 있습니다.</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-3">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/printing.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /></span><small>PRINTING</small><b>인쇄</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/packaging.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></span><small>PACKAGING</small><b>포장</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">INK &amp; COATING REMOVAL IN PRACTICE</span><h2 class="cmp-h2">인쇄 · 도장설비 세척에서<br>확인된 적용 경험</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 Printing 자료에서 확인되는 적용 사례입니다.</p>
  </div>
  <ul class="mtc-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>PRINTING PRESS</small><b>실린더 잉크 잔류물 세척</b><span>Cold Jet 공식 사례</span></div>
      <dl><div><dt>기존 방식</dt><dd>화학용제 · 수작업 스크래핑 — 실린더 표면 손상 우려</dd></div><div><dt>적용</dt><dd>드라이아이스 세척으로 색상 교체 시 세척</dd></div></dl>
      <p class="mtc-case-result"><span>확인된 결과</span>실린더 표면 상태를 유지하며 세척시간을 줄였다고 보고</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 인쇄·도장설비의 잔류물도<br>관리할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>잉크·도료·코팅의 종류와 부착 정도, 설비의 재질에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 설비 또는 샘플을 확인하고 세척 테스트를 통해 적용 가능성과 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""


OIL_GREASE_RESIDUE_REMOVAL_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): Facility Maintenance, Mining, Oil & Gas, Rail Transportation, Contract Cleaning 자료 조합.
       단독 대표 Application 페이지가 없어 여러 산업 자료의 공통 오일·그리스 세척 내용을 조합해 작성.
       이미지: task-oil-tar-pipe.webp, auto-facility-motor.jpg 등 기존 로컬 자료 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/task-oil-tar-pipe.webp" alt="배관에 축적된 오일·타르성 오염" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 오일 · 그리스 · 고착 오염 제거</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">OIL, GREASE &amp; HEAVY BUILDUP REMOVAL</span>
      <h1>오일 · 그리스 · 고착 오염 제거</h1>
      <p class="cmp-hero-p auto-hero-lead">두껍게 쌓인 오일과 그리스는,<br>설비의 상태까지 가릴 수 있습니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">HEAVY BUILDUP</span>
      <h2 class="cmp-h2">시간이 지날수록,<br>오염은 더 두껍고 단단해집니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>기어, 베어링 하우징, 기계 프레임, 유압설비, 컨베이어, 펌프, 중장비에는 오일과 그리스, 윤활유, 타르성 잔류물, 탄화된 그리스가 시간이 지날수록 겹겹이 쌓입니다.</p>
      <p class="auto-intro-close">드라이아이스 세척은 <b>화학용제나 스팀 세척 없이</b> 이러한 고착 오염물을 제거하는 데 활용할 수 있습니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">HEAVY BUILDUP APPLICATIONS</span>
    <h2 class="cmp-h2">기계설비와 중장비의<br>고착 오염을 관리합니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div><span class="auto-en">MACHINERY &amp; MOVING PARTS</span><h3>기계설비 · 구동부</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="배관 오일 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/auto-facility-motor.jpg" alt="기계 프레임 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">기어와 베어링의 그리스를<br>분해 없이 제거합니다.</p>
      <div class="cmp-text auto-text"><p>기어, 베어링 하우징, 기계 프레임, 유압부품에는 오일과 그리스가 반복적으로 축적됩니다. 오염이 두꺼워지면 누유 위치나 균열, 마모 상태를 육안으로 확인하기 어려워질 수 있습니다.</p><p>드라이아이스 세척은 조건에 따라 설비를 완전히 분해하지 않고 세척할 수 있어, 정비 전 상태 확인을 위한 세척에 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>기어 · 베어링 하우징</li><li>기계 프레임 · 유압부품</li><li>컨베이어 · 펌프 · 컴프레서</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div><span class="auto-en">HEAVY &amp; RAIL EQUIPMENT</span><h3>중장비 · 철도설비</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/auto-facility-motor.jpg" alt="중장비 엔진 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="타르성 오염 배관 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">엔진과 대형 설비의<br>고착 오염을 관리합니다.</p>
      <div class="cmp-text auto-text"><p>엔진, 중장비, 채광설비, 철도차량 대차와 언더캐리지에는 오일, 타르성 잔류물, 아스팔트, 탄화된 그리스가 두껍게 고착될 수 있습니다.</p><p>드라이아이스 세척은 물이나 연마재 사용이 부담스러운 대형 설비의 현장 유지보수 세척에 활용할 수 있습니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>엔진 · 중장비</li><li>채광설비 · 철도 대차</li><li>플랜트 배관 · 밸브</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">고착 오염은<br>종류에 따라 제거 난이도가 다릅니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 · 그리스</b><small>OIL &amp; GREASE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>유압유 · 윤활유</b><small>HYDRAULIC &amp; LUBRICANT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>타르성 잔류물 · 아스팔트</b><small>TAR-LIKE BUILDUP</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>탄화된 그리스</b><small>CARBONIZED GREASE</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">오염 제거는 정비의 끝이 아니라,<br>상태 점검의 시작일 수 있습니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>분해 없이 현장 세척</b><p>적용 조건에 따라 설비를 완전히 분해하지 않고 세척할 수 있는 경우가 있어 정비시간을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>물을 사용하지 않는 건식 세척</b><p>세척 후 별도의 건조 작업을 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 승화하므로 매체 자체는 남지 않습니다. 제거된 오일·그리스는 별도로 회수·처리합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>상태 확인이 쉬운 표면</b><p>오염을 제거하면 누유, 균열, 마모 상태를 육안으로 확인하기 쉬운 환경을 만드는 데 도움이 될 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">얇은 오일막과<br>두껍게 고착된 그리스는 조건이 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>기어의 얇은 오일막과 중장비의 두껍게 탄화된 그리스는 필요한 분사 강도와 시간이 전혀 다릅니다.</p>
            <p>바테크는 실제 설비와 오염 상태를 확인하고 세척 테스트를 통해 적합한 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><b>배관 · 밸브</b><small>타르성 잔류물</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/auto-facility-motor.jpg" alt="" loading="lazy" /><b>기계 프레임</b><small>오일 · 그리스</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">INDUSTRIES</span><h2 class="cmp-h2">오일 · 그리스 오염은<br>중장비가 있는 모든 현장에 존재합니다.</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/mining.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /></span><small>MINING</small><b>채광</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/oil-gas.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-oilgas.png" alt="" loading="lazy" /></span><small>OIL &amp; GAS</small><b>석유 · 가스</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/rail.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-rail.png" alt="" loading="lazy" /></span><small>RAIL &amp; PUBLIC TRANSPORTATION</small><b>철도 · 대중교통</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/facility-maintenance.html"><span class="auto-relind-img"><img src="../assets/img/facility-volpak-machine-cleaning.webp" alt="" loading="lazy" /></span><small>FACILITY MAINTENANCE</small><b>생산설비 · 시설 유지보수</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section auto-proven-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">HEAVY BUILDUP REMOVAL IN PRACTICE</span><h2 class="cmp-h2">중장비 · 설비 유지보수에서<br>확인된 적용 경험</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 Facility Maintenance · Mining 자료에서 확인되는 적용 사례입니다.</p>
  </div>
  <ul class="mtc-cases">
    <li class="reveal" style="--reveal-delay:0.00s">
      <div class="mtc-case-head"><small>FACILITY MAINTENANCE</small><b>기계설비 오일·그리스 세척</b><span>Cold Jet 공식 사례</span></div>
      <dl><div><dt>기존 방식</dt><dd>화학세척제 · 스팀 세척</dd></div><div><dt>적용</dt><dd>드라이아이스 세척으로 정비 전 세척</dd></div></dl>
      <p class="mtc-case-result"><span>확인된 결과</span>분해 없이 상태 점검이 쉬워졌다고 보고</p>
    </li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">두껍게 쌓인 오염물도<br>세척할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>오염물의 두께와 경화 상태, 설비의 재질과 형상에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 설비 또는 샘플을 확인하고 세척 테스트를 통해 적용 가능성과 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""


RUST_CORROSION_REMOVAL_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/rust-removal/
       한계 설명(Sa 2.5 / White Metal / Anchor Profile 구분)은 Cold Jet Surface Rust Removal 공식 자료 기준.
       이미지: task-surface-rust.webp, power-generation-...-surface-rust-...webp 기존 로컬 자료 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/power-generation-dry-ice-blasting-removing-surface-rust-from-turbine-compressor-component.webp" alt="터빈 부품 표면 녹 세척" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 녹 · 부식 · 산화물 제거</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">RUST, CORROSION &amp; OXIDATION REMOVAL</span>
      <h1>녹 · 부식 · 산화물 제거</h1>
      <p class="cmp-hero-p auto-hero-lead">드라이아이스 세척은<br>모든 녹을 깎아내는 방식이 아닙니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">SURFACE-LEVEL vs. DEEP CORROSION</span>
      <h2 class="cmp-h2">표면 녹 제거와<br>연마 블라스팅은 목적이 다릅니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>표면 녹, 플래시 러스트, 초기 단계의 느슨한 산화물은 드라이아이스 세척으로 검토 가능한 영역입니다. 원래 표면 상태를 고려하면서 이러한 오염을 제거하는 데 활용할 수 있습니다.</p>
      <p class="auto-intro-close">하지만 <b>깊게 진행된 피팅 부식, 두꺼운 스케일, Sa 2.5 이상의 백색 금속면, 재도장을 위한 표면 프로파일(Anchor Profile)이 필요한 작업</b>에는 순수 드라이아이스 세척이 적합한 방법이 아닐 수 있습니다. 이 경우 연마 블라스팅 등 다른 방식을 검토해야 합니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">RUST REMOVAL APPLICATIONS</span>
    <h2 class="cmp-h2">기계 표면과<br>구조물의 표면 녹을 관리합니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div><span class="auto-en">MACHINE &amp; TOOLING SURFACES</span><h3>기계 · 툴링 표면</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-surface-rust.webp" alt="기계 표면 녹 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/power-generation-dry-ice-blasting-removing-surface-rust-from-turbine-compressor-component.webp" alt="터빈 부품 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">정밀 표면의 형상을 유지하며<br>표면 녹을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>기계 프레임, 정밀 부품, 터빈·컴프레서 구성품, 금형 표면에 발생하는 표면 녹과 초기 산화물은 드라이아이스 세척으로 검토할 수 있습니다.</p><p>비마모성 방식이므로 정밀한 형상을 연마하지 않으면서 접근할 수 있지만, 부식 깊이와 정도에 따라 결과가 달라질 수 있어 사전 테스트를 권장합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>기계 프레임 · 정밀 부품</li><li>터빈 · 컴프레서 구성품</li><li>금형 · 치공구 표면</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div><span class="auto-en">STRUCTURAL &amp; RESTORATION SURFACES</span><h3>구조물 · 복원 대상 표면</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/power-generation-dry-ice-blasting-removing-surface-rust-from-turbine-compressor-component.webp" alt="철골 구조물 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/task-surface-rust.webp" alt="자동차 하부 표면 녹 세척" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">느슨하게 부착된 산화물을<br>원형 표면을 고려하며 제거합니다.</p>
      <div class="cmp-text auto-text"><p>철골 구조물, 철도 인프라, 자동차 복원 대상의 언더바디 표면에 생긴 느슨한 표면 녹은 검사와 유지보수를 돕는 목적으로 세척할 수 있습니다.</p><p>다만 깊게 진행된 부식이나 강한 표면처리가 필요한 경우는 다른 방법을 검토해야 합니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>철골 구조물 · 철도 인프라</li><li>자동차 복원 언더바디</li><li>플랜트 배관 외부</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">WHAT DRY ICE CAN AND CANNOT DO</span>
  <h2 class="cmp-h2 reveal">가능한 영역과<br>다른 방법이 필요한 영역을 구분합니다.</h2>
  <div class="adopt-2col reveal" style="--reveal-delay:0.1s">
    <div>
      <h4>검토 가능한 영역</h4>
      <p class="adopt-2col-b">표면 녹 · 플래시 러스트 · 초기 산화물 · 느슨하게 부착된 표면 오염</p>
      <ul><li>정밀 표면의 형상 유지가 필요한 경우</li><li>연마 흔적을 남기지 않아야 하는 경우</li><li>검사·유지보수를 위한 표면 확인 목적</li></ul>
    </div>
    <div>
      <h4>Dry Ice Only 범위 밖</h4>
      <p class="adopt-2col-b">깊게 진행된 피팅 부식 · 두꺼운 스케일 · Sa 2.5 이상 백색 금속면 · Anchor Profile 형성</p>
      <ul><li>재도장을 위한 표면 프로파일이 필요한 경우</li><li>연마 블라스팅 등 별도 방식 검토 필요</li></ul>
    </div>
  </div>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">표면 녹 제거와<br>표면 보호를 함께 고려합니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>비마모성 세척</b><p>연마재로 깎아내는 방식이 아니므로 원래 표면 상태를 고려하면서 표면 녹을 제거합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>표면 수준의 산화물 대응</b><p>표면 녹과 느슨한 산화물 제거에 활용하며, 깊은 부식에는 다른 방식이 필요할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>수분을 남기지 않는 방식</b><p>물을 사용하지 않아 세척 직후 재부식 우려를 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>연마재가 남지 않는 방식</b><p>드라이아이스는 승화하므로 모래·비드 같은 연마재가 표면에 남지 않습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">부식 깊이와 요구되는 표면 상태에 따라<br>적합한 방법이 달라집니다.</h2>
          <div class="cmp-dark-body">
            <p>표면 녹인지, 피팅 부식인지, 재도장을 위한 프로파일이 필요한지에 따라 드라이아이스 세척이 적합한지 여부부터 확인해야 합니다.</p>
            <p>바테크는 실제 표면과 부식 상태를 확인하고 필요 시 세척 테스트를 통해 적용 가능성을 검토합니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><b>정밀 부품</b><small>표면 녹</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/power-generation-dry-ice-blasting-removing-surface-rust-from-turbine-compressor-component.webp" alt="" loading="lazy" /><b>터빈 · 컴프레서</b><small>산화물</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>적용 가능 여부부터</em> 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">INDUSTRIES</span><h2 class="cmp-h2">표면 녹 관리는<br>다양한 산업 설비에서 필요합니다.</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/oil-gas.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-oilgas.png" alt="" loading="lazy" /></span><small>OIL &amp; GAS</small><b>석유 · 가스</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/power-generation.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></span><small>POWER GENERATION</small><b>발전 · 전력</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/mining.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /></span><small>MINING</small><b>채광</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/automotive-detailing.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-detailing.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE RESTORATION &amp; DETAILING</small><b>자동차 복원 · 디테일링</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">현재 부식 상태에<br>드라이아이스 세척이 적합할까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>부식의 깊이와 진행 정도, 요구되는 표면 상태에 따라 적용 가능 여부가 달라집니다.</p>
      <p>바테크는 실제 표면을 확인하고 필요 시 테스트를 통해 적용 가능성과 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""


SURFACE_PREPARATION_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/surface-preparation/
       이미지: task-surface-industrial.jpg, task-surface-food.jpg, plastics-composites-...-automotive-parts-prior-to-painting.webp 등 기존 로컬 자료 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/task-surface-industrial.jpg" alt="도장 전 부품 표면 전처리" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 표면 전처리</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">SURFACE PREPARATION</span>
      <h1>표면 전처리</h1>
      <p class="cmp-hero-p auto-hero-lead">좋은 도장과 접착은,<br>깨끗한 표면에서 시작됩니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">CLEANLINESS, NOT PROFILE</span>
      <h2 class="cmp-h2">깨끗하게 만드는 전처리와,<br>표면을 거칠게 만드는 전처리는 다릅니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>도장, 코팅, 접착, 실링, 용접 전에는 표면에 남아 있는 이형제, 오일, 먼지, 미세입자, 지문·피지, 생산 잔류물이 후속 공정에 영향을 주지 않도록 관리해야 합니다.</p>
      <p class="auto-intro-close">드라이아이스 Surface Preparation은 <b>오염물을 제거하는 청정도 확보(Cleanliness Preparation)</b> 성격이 강합니다. 일반적인 연마 블라스팅처럼 재도장을 위한 표면 프로파일(Anchor Profile)을 만드는 방식은 아닙니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">SURFACE PREPARATION APPLICATIONS</span>
    <h2 class="cmp-h2">후속 공정에 따라<br>제거해야 할 오염물이 다릅니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div><span class="auto-en">BEFORE PAINTING &amp; COATING</span><h3>도장 · 코팅 전</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-surface-industrial.jpg" alt="도장 전 부품 세척" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-dry-ice-blasting-cleaning-automotive-parts-prior-to-painting.webp" alt="자동차 부품 도장 전처리" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">이형제와 먼지를 제거해<br>표면을 도장에 적합한 상태로 준비합니다.</p>
      <div class="cmp-text auto-text"><p>자동차, 플라스틱, 항공 부품의 도장·코팅 전에는 이형제, 오일, 먼지와 생산 잔류물이 도막 부착에 영향을 줄 수 있습니다.</p><p>드라이아이스 세척은 물을 사용하지 않고 세정 매체가 표면에 남지 않는 방식으로, 도장 전 표면을 준비하는 데 활용됩니다. 물세척과 달리 세척 후 건조공정의 부담을 줄일 수 있는 것도 장점입니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>자동차 · 플라스틱 부품</li><li>항공 복합재 부품</li><li>가전 패널 · 고무 성형 부품</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div><span class="auto-en">BEFORE BONDING &amp; FINISHING</span><h3>접착 · 실링 · 검사 전</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/task-surface-food.jpg" alt="전자부품 표면 전처리" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/task-surface-industrial.jpg" alt="정밀부품 표면 전처리" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">접착·실링 전<br>표면 오염물을 제거합니다.</p>
      <div class="cmp-text auto-text"><p>전자 하우징, 의료기기 부품에서는 접착이나 실링 전에 오일과 먼지, 미세입자, 지문·피지를 제거해야 접착 신뢰성을 확보하는 데 도움이 될 수 있습니다.</p><p>자동차 부품 등 반복 생산 라인에서는 로봇 기반 자동화 표면 전처리 사례도 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>전자 하우징 · 의료기기 부품</li><li>정밀 조립부품</li><li>자동화 라인 부품(로봇 통합)</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">COMMON CONTAMINANTS</span>
  <h2 class="cmp-h2 reveal">후속 공정에 영향을 줄 수 있는<br>표면 오염물입니다.</h2>
  <ul class="auto-cont" aria-label="주요 오염물">
    <li class="reveal-scale" style="--reveal-delay:0.00s"><img src="../assets/img/task-surface-industrial.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>이형제</b><small>MOLD RELEASE AGENT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.06s"><img src="../assets/img/plastics-composites-dry-ice-blasting-cleaning-automotive-parts-prior-to-painting.webp" alt="" loading="lazy" /><span class="auto-cont-l"><b>오일 · 윤활유</b><small>OIL &amp; LUBRICANT</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.12s"><img src="../assets/img/task-surface-food.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>먼지 · 미세입자</b><small>DUST &amp; FINE PARTICULATE</small></span></li>
    <li class="reveal-scale" style="--reveal-delay:0.18s"><img src="../assets/img/task-surface-industrial.jpg" alt="" loading="lazy" /><span class="auto-cont-l"><b>지문 · 생산 잔류물</b><small>FINGERPRINT &amp; PROCESS RESIDUE</small></span></li>
  </ul>
</div>

<div class="cmp-section auto-why-sec">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">청정도를 높이는 전처리와<br>표면을 거칠게 만드는 전처리를 구분합니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>수분이 남지 않는 방식</b><p>물을 사용하지 않아 도장·접착 전 표면에 수분이 남을 우려를 줄이는 데 도움이 될 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>세정 매체가 남지 않는 방식</b><p>드라이아이스는 승화하므로 매체 자체가 표면에 남지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>오일 · 이형제 제거</b><p>후속 공정에 영향을 줄 수 있는 오일과 이형제를 표면 손상 없이 제거하는 데 활용됩니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>건조공정 부담 감소</b><p>물세척과 달리 세척 후 수분 제거를 위한 별도 건조공정의 부담을 줄일 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">후속 공정이 요구하는 청정도에 따라<br>세척 조건이 달라집니다.</h2>
          <div class="cmp-dark-body">
            <p>도장 전 요구되는 청정도와 접착 전 요구되는 청정도는 다를 수 있습니다. 부품의 재질과 형상, 오염물의 종류에 따라 조건을 조정합니다.</p>
            <p>바테크는 실제 부품과 후속 공정 요구조건을 확인하고 세척 테스트를 통해 적합한 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/plastics-composites-dry-ice-blasting-cleaning-automotive-parts-prior-to-painting.webp" alt="" loading="lazy" /><b>자동차 부품</b><small>도장 전 이형제 · 오일</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/task-surface-food.jpg" alt="" loading="lazy" /><b>전자 하우징</b><small>접착 전 먼지 · 지문</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>후속 공정 요구조건부터</em> 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">INDUSTRIES</span><h2 class="cmp-h2">표면 전처리는<br>정밀 제조 전반에 걸쳐 있습니다.</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS &amp; COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE &amp; AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/medical.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></span><small>MEDICAL EQUIPMENT MANUFACTURING</small><b>의료기기 제조</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">우리 부품의 도장 전처리에<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>부품의 재질과 형상, 후속 공정이 요구하는 청정도에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 부품 또는 샘플을 확인하고 세척 테스트를 통해 적용 가능성과 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""


DEBURRING_DEFLASHING_BODY = """
  
  <!-- 기술 내용·이미지 출처(Cold Jet 공식): https://www.coldjet.com/dry-ice-blasting/applications/deburring-deflashing/
       이미지: task-deburring-plastic.jpg, task-deburring-precision.jpg, aerospace-deburring-plastic-part-with-dry-ice-cleaning.webp,
       plastics-composites-deburring-*.webp, medical-orthopedic-uhmw-implant-deburring.webp 기존 로컬 자료 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/plastics-composites-deburring-plastic-part.webp" alt="플라스틱 부품 디버링" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; <a href="../cleaning/task.html">작업별 솔루션</a> &gt; 디버링 · 디플래싱</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">DEBURRING &amp; DEFLASHING</span>
      <h1>디버링 · 디플래싱</h1>
      <p class="cmp-hero-p auto-hero-lead">불필요한 버와 플래시는 제거하고,<br>부품의 형상과 치수는 고려합니다.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">PARTS FINISHING, NOT CLEANING</span>
      <h2 class="cmp-h2">이 페이지는 세척보다<br>부품 마무리(Parts Finishing)를 다룹니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>사출 성형, 가공, 3D 프린팅 부품에는 파팅라인, 게이트, 벤트 주변에 플래시가, 가공 후 모서리나 홀·나사산 주변에는 버가 남을 수 있습니다.</p>
      <p class="auto-intro-close">드라이아이스 기술은 필요한 부분에 세척 강도를 조절해 <b>버와 플래시를 제거하면서 부품의 주요 형상과 치수 변화를 최소화</b>하는 부품 마무리 공정에 활용됩니다.</p>
    </div>
  </div>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">
  <div class="auto-sec-head reveal">
    <span class="cmp-eyebrow">DEBURRING &amp; DEFLASHING APPLICATIONS</span>
    <h2 class="cmp-h2">디버링과 디플래싱은<br>발생 원인이 다른 별개의 작업입니다.</h2>
  </div>

<article class="auto-app is-wide" id="auto-01">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div><span class="auto-en">DEFLASHING — MOLDED PARTS</span><h3>성형 부품 디플래싱</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/plastics-composites-deburring-plastic-part.webp" alt="플라스틱 부품 플래시 제거" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/aerospace-deburring-plastic-part-with-dry-ice-cleaning.webp" alt="정밀 성형부품 디플래싱" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">파팅라인과 게이트 주변의<br>플래시를 정밀하게 제거합니다.</p>
      <div class="cmp-text auto-text"><p>사출성형·압축성형 플라스틱, 고무, 서모셋 부품은 파팅라인, 게이트, 벤트 주변에 플래시가 남습니다. ABS, PP, 나일론, 페놀릭 등 재질에 따라 필요한 세척 강도가 다릅니다.</p><p>드라이아이스 세척은 노즐과 분사 조건을 조절해 이 부위를 타겟팅하며, 연마재가 부품 내부에 잔류하지 않는 방식으로 활용됩니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>사출 · 압축성형 플라스틱 부품</li><li>고무 · 서모셋 부품</li><li>3D 프린팅 부품</li></ul></div>
    </div>
  </div>
</article>

<article class="auto-app is-flip" id="auto-02">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div><span class="auto-en">DEBURRING — MACHINED &amp; PRECISION PARTS</span><h3>가공 · 정밀부품 디버링</h3></div>
  </div>
  <div class="auto-app-grid">
    <div class="auto-app-media is-pair"><figure class="reveal-scale" style="--reveal-delay:0.08s"><img src="../assets/img/medical-orthopedic-uhmw-implant-deburring.webp" alt="정밀 임플란트 부품 디버링" loading="lazy" /></figure><figure class="reveal-scale" style="--reveal-delay:0.20s"><img src="../assets/img/plastics-composites-deburring-machined-part.webp" alt="가공부품 디버링" loading="lazy" /></figure></div>
    <div class="auto-app-copy reveal" style="--reveal-delay:0.16s">
      <p class="auto-app-h">홀과 나사산 주변의 버를<br>공차를 고려하며 제거합니다.</p>
      <div class="cmp-text auto-text"><p>가공 후 남는 금속·플라스틱 버는 홀, 나사산, 모서리 주변에 발생합니다. 의료기기 부품, 커넥터, 자동차·항공 정밀부품처럼 공차가 중요한 대상에서는 형상 변화를 최소화하는 방식이 필요합니다.</p><p>드라이아이스는 세척 강도를 조절해 타겟 부위만 처리할 수 있어, 좁은 공차의 정밀부품 마무리에 검토됩니다. 다만 금속 버 전체를 모두 제거할 수 있다고 일반화하지 않으며, 버의 재질·형상·크기·부착 상태에 따라 적용 가능성이 달라집니다.</p></div>
      <div class="auto-targets"><span>대표 대상</span><ul><li>의료기기 정밀부품</li><li>커넥터 · 전자부품</li><li>자동차 · 항공 정밀부품</li></ul></div>
    </div>
  </div>
</article>
</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">WHY DRY ICE CLEANING</span>
  <h2 class="cmp-h2 reveal">타겟팅된 처리로<br>공차와 형상을 함께 고려합니다.</h2>
  <ol class="auto-why is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><b>타겟팅된 처리(Targeted Processing)</b><p>노즐과 분사 조건을 조절해 버·플래시가 있는 부위만 선택적으로 처리할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.09s"><b>복잡한 형상 접근</b><p>홀, 나사산, 좁은 틈처럼 복잡한 형상에도 접근할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>연마재가 부품에 남지 않음</b><p>드라이아이스는 승화하므로 모래·비드 매체가 부품 내부나 틈에 잔류하지 않습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.27s"><b>공차 변화 최소화 · 자동화 가능성</b><p>부품의 주요 치수 변화를 최소화하는 방향으로 조건을 설정하며, 반복 생산 부품은 자동화 라인에 통합할 수 있습니다.</p></li>
  </ol>
</div>
</div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark auto-dark">
    <div class="wrap">
      <div class="auto-ae">
        <div class="reveal">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">성형 플래시와<br>가공 버는 발생 위치와 조건이 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>재질(플라스틱·고무·금속), 버·플래시의 크기와 부착 상태, 요구되는 공차에 따라 필요한 조건이 달라집니다. 금속 버를 모두 제거할 수 있다고 일반화하지 않습니다.</p>
            <p>바테크는 실제 부품을 확인하고 세척 테스트를 통해 입자 크기, 분사 압력, 노즐, 거리와 각도를 조정해 적합한 조건을 찾습니다.</p>
          </div>
        </div>
        <div class="auto-ae-side reveal" style="--reveal-delay:0.16s">
          <ul class="auto-ae-cases">
            <li class="reveal" style="--reveal-delay:0.45s"><img src="../assets/img/plastics-composites-deburring-plastic-part.webp" alt="" loading="lazy" /><b>사출성형 부품</b><small>파팅라인 플래시</small></li>
            <li class="reveal" style="--reveal-delay:0.54s"><img src="../assets/img/medical-orthopedic-uhmw-implant-deburring.webp" alt="" loading="lazy" /><b>정밀 임플란트 부품</b><small>가공 버</small></li>
          </ul>
          <p class="auto-ae-key">장비를 먼저 정하기보다,<br><em>먼저 적합한 세척 조건</em>을 확인합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">

<div class="cmp-section is-first auto-relind-sec">
  <div class="auto-sec-head auto-sec-head-lead reveal">
    <div><span class="cmp-eyebrow">INDUSTRIES</span><h2 class="cmp-h2">정밀부품 마무리는<br>여러 산업의 생산 후공정입니다.</h2></div>
    <p class="cmp-lead-p">Cold Jet 공식 자료에서 확인되는 적용 산업입니다.</p>
  </div>
  <ul class="auto-relind is-4">
    <li class="reveal" style="--reveal-delay:0.00s"><a href="../industries/plastics-composites.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span><small>PLASTICS &amp; COMPOSITES</small><b>플라스틱 · 복합소재</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.07s"><a href="../industries/medical.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></span><small>MEDICAL EQUIPMENT MANUFACTURING</small><b>의료기기 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.14s"><a href="../industries/automotive.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span><small>AUTOMOTIVE MANUFACTURING</small><b>자동차 제조</b><span>산업 페이지 보기 →</span></a></li>
    <li class="reveal" style="--reveal-delay:0.21s"><a href="../industries/aerospace.html"><span class="auto-relind-img"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></span><small>AEROSPACE &amp; AVIATION</small><b>우주 · 항공</b><span>산업 페이지 보기 →</span></a></li>
  </ul>
</div>

<div class="cmp-section cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">TEST YOUR APPLICATION</span>
    <h2 class="cmp-h2">현재 부품의 버와 플래시에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>부품의 재질과 형상, 버·플래시의 부착 상태와 요구 공차에 따라 적합한 세척 조건은 달라집니다.</p>
      <p>바테크는 실제 부품 또는 샘플을 확인하고 세척 테스트를 통해 적용 가능성과 작업 조건을 확인합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">적용 상담 →</a>
      <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""





# (2026-09-07 6차 → 2026-09-08 7차 핸드오프 "산업별 솔루션") compare.html과 같은
# 편집형 구조(패럴랙스 히어로 + .cmp-panel 인트로 + 01 주요 산업 16 카드 / 02 산업
# 공통 유지보수 Featured / 03 전문 세척·복원 리스트 + APPLICATION ENGINEERING
# 어두운 섹션 + CTA + 함께 보면 좋은 페이지). 22개 카드의 영문 분류·
# 키워드·설명문·slug는 핸드오프 HTML이 정본이라 데이터 배열로 풀지 않고
# 본문을 통째로 보관한다(출력 HTML byte 동일). 카드 링크는 상세 페이지
# (../industries/*.html)가 아직 없어 href="#" + data-target 로 둔다.
INDUSTRY_BODY = """
  <section class="subhero-parallax">
    <img class="subhero-parallax-img" src="../assets/img/stackdo-blaster.jpg" alt="산업 현장 드라이아이스 세척" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="index.html">드라이아이스 세척가이드</a> &gt; 산업별 솔루션</div>
    <div class="subhero-textbox">
      <span class="ind-hero-eyebrow">INDUSTRY SOLUTIONS</span>
      <h1>산업별 솔루션</h1>
      <p class="cmp-hero-p">산업마다 오염물과 기재, 설비 조건이 다릅니다.<br>각 산업의 주요 세척 대상과 적용 방법을 확인해보세요.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">INDUSTRIES</span>
  <h2 class="cmp-h2">산업마다 다른 세척 과제,<br>그에 맞는 솔루션이 필요합니다.</h2>
  <div class="cmp-lead">
    <p>드라이아이스 세척은 모든 산업에 하나의 방식으로 적용되지 않습니다.</p>
    <p>오염물의 특성과 세척 대상의 재질, 설비 구조와 작업 환경, 원하는 결과에 따라 적합한 세척 조건과 적용 방법은 달라집니다.</p>
    <p>각 산업을 선택하면 실제 생산 현장에서 무엇을 세척하는지, 어떤 오염물이 문제가 되는지, 드라이아이스 세척이 어떻게 활용되는지 확인할 수 있습니다.</p>
  </div>
  <ul class="cmp-criteria ind-criteria reveal" aria-label="산업마다 달라지는 네 가지">
    <li><span>01</span><b>오염물</b><small>이형제 · 카본 · 오일 · 접착제 · 생산 잔류물</small></li>
    <li><span>02</span><b>세척 대상</b><small>금형 · 생산설비 · 부품 · 전기전자 · 제품 표면</small></li>
    <li><span>03</span><b>작업 조건</b><small>온도 · 가동 여부 · 접근성 · 분해 여부</small></li>
    <li><span>04</span><b>요구 결과</b><small>청정도 · 표면 보호 · 다운타임 · 유지보수</small></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section ind-hub" id="ind-core">
  <span class="ind-ghost" aria-hidden="true">01</span>
  <div class="cmp-vs-head ind-head">
    <span class="cmp-num">01<span class="cmp-num-of">/ 03</span></span>
    <div>
      <span class="cmp-vs-title">CORE INDUSTRIES · 주요 산업 분야 16</span>
      <h2 class="cmp-h2">자동차부터 광업까지,<br>주요 산업의 적용 분야</h2>
      <div class="cmp-lead ind-lead">
        <p>드라이아이스 세척은 자동차와 반도체부터 식품, 발전, 플랜트, 운송산업까지 다양한 생산 및 산업 현장에 적용됩니다.</p>
        <p>각 산업마다 오염물, 세척 대상, 설비 구조와 공정 조건이 다릅니다. 해당 산업을 선택하면 주요 세척 대상과 적용 포인트를 상세 페이지에서 확인할 수 있습니다.</p>
      </div>
    </div>
  </div>
  <div class="ind-grid">
    <a class="ind-card reveal" href="../industries/automotive.html" aria-label="자동차 제조 솔루션 보기" style="--reveal-delay:0s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">01</span>
        <span class="ind-card-en">AUTOMOTIVE MANUFACTURING</span>
        <h3>자동차 제조</h3>
        <p class="ind-card-kw">금형 · 용접 셀 · 도장라인 · 다이캐스팅</p>
        <p class="ind-card-desc">사출·고무 금형부터 용접 로봇과 치구, 도장설비, 다이캐스팅 툴링까지 자동차 생산공정 전반의 세척과 유지보수에 적용됩니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/semiconductor.html" aria-label="반도체 · 전자 제조 솔루션 보기" style="--reveal-delay:0.06s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-semiconductor.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">02</span>
        <span class="ind-card-en">SEMICONDUCTOR & ELECTRONICS</span>
        <h3>반도체 · 전자 제조</h3>
        <p class="ind-card-kw">웨이퍼 공정 · CVD · 증착 툴링 · 진공펌프 · 이온주입기</p>
        <p class="ind-card-desc">웨이퍼 챔버와 공정 툴링의 미세 입자·오일·분진·연마제 잔류물 제거부터 반도체 몰딩 및 PCB 세정까지 정밀 세정에 활용됩니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/plastics-composites.html" aria-label="플라스틱 · 복합소재 솔루션 보기" style="--reveal-delay:0.12s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">03</span>
        <span class="ind-card-en">PLASTICS & COMPOSITES</span>
        <h3>플라스틱 · 복합소재</h3>
        <p class="ind-card-kw">사출금형 · 디플래싱 · 표면 전처리 · 복합재 툴링</p>
        <p class="ind-card-desc">이형제, 수지 오프가스와 경화 잔류물을 제거하고, 성형품의 디버링·디플래싱 및 도장·코팅 전 표면처리에도 적용됩니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/rubber-tires.html" aria-label="고무 · 타이어 솔루션 보기" style="--reveal-delay:0.18s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-rubber-tire.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">04</span>
        <span class="ind-card-en">RUBBER & TIRES</span>
        <h3>고무 · 타이어</h3>
        <p class="ind-card-kw">타이어 금형 · 가류기 · 고무 사출금형 · 압축금형 · 벤트</p>
        <p class="ind-card-desc">금형을 프레스에서 분리하지 않고 이형제와 카본, 가황고무 잔류물을 제거해 금형 상태와 제품 표면 품질을 유지합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/food-beverage.html" aria-label="식품 · 음료 솔루션 보기" style="--reveal-delay:0s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-food.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">05</span>
        <span class="ind-card-en">FOOD & BEVERAGE</span>
        <h3>식품 · 음료</h3>
        <p class="ind-card-kw">오븐 · 믹서 · 프라이어 · 컨베이어 · 포장설비</p>
        <p class="ind-card-desc">탄화 식품, 유지·지방, 설탕·시럽, 반죽과 생산 잔류물을 물과 화학세제 없이 제거하여 생산설비를 건식으로 세정합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/foundry.html" aria-label="주조 · 다이캐스팅 솔루션 보기" style="--reveal-delay:0.06s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-foundry.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">06</span>
        <span class="ind-card-en">FOUNDRY & DIE CASTING</span>
        <h3>주조 · 다이캐스팅</h3>
        <p class="ind-card-kw">영구금형 · 코어박스 · 다이캐스팅 금형 · 주조설비</p>
        <p class="ind-card-desc">수지·바인더·이형제·내화 코팅과 다이 윤활제 등을 제거하면서 정밀한 금형면과 벤트의 형상을 보호합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/aerospace.html" aria-label="우주 · 항공 솔루션 보기" style="--reveal-delay:0.12s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">07</span>
        <span class="ind-card-en">AEROSPACE & AVIATION</span>
        <h3>우주 · 항공</h3>
        <p class="ind-card-kw">복합재 툴링 · 금형 · 접착제 제거 · 표면 전처리</p>
        <p class="ind-card-desc">항공용 복합재 금형과 생산 툴링의 수지·이형제·접착제를 제거하고, 부품 표면 전처리와 디버링에도 활용됩니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/medical.html" aria-label="의료기기 제조 솔루션 보기" style="--reveal-delay:0.18s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-medical.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">08</span>
        <span class="ind-card-en">MEDICAL DEVICE MANUFACTURING</span>
        <h3>의료기기 제조</h3>
        <p class="ind-card-kw">정밀금형 · 임플란트 · 스텐트 · 카테터 · 의료부품</p>
        <p class="ind-card-desc">의료용 금형 세척과 함께 임플란트, 스텐트, 카테터 팁 등 정밀 의료부품의 디버링·디플래싱 및 클린룸 제조공정에 적용됩니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/power-generation.html" aria-label="발전 · 전력 솔루션 보기" style="--reveal-delay:0s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-power.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">09</span>
        <span class="ind-card-en">POWER GENERATION</span>
        <h3>발전 · 전력</h3>
        <p class="ind-card-kw">터빈 · 발전기 · HRSG · 변압기 · 전기설비 · 원자력 · 제염</p>
        <p class="ind-card-desc">터빈과 발전기, 보일러·열교환 설비부터 권선·변압기·스위치기어까지 발전설비의 정비와 예방보전에 활용되며, 원자력 시설의 방사성 오염 제염에도 2차 폐기물 없이 적용됩니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/oil-gas.html" aria-label="오일 · 가스 솔루션 보기" style="--reveal-delay:0.06s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-oilgas.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">10</span>
        <span class="ind-card-en">OIL & GAS</span>
        <h3>오일 · 가스</h3>
        <p class="ind-card-kw">배관 · 탱크 · 열교환기 · 펌프 · 플랜트 설비</p>
        <p class="ind-card-desc">원유·중유, 역청, 파라핀, 카본과 염류 등 플랜트 오염물을 제거하고 점검·보수·재도장 전 표면 세정에 활용됩니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/packaging.html" aria-label="포장 솔루션 보기" style="--reveal-delay:0.12s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-packaging.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">11</span>
        <span class="ind-card-en">PACKAGING</span>
        <h3>포장</h3>
        <p class="ind-card-kw">포장기 · 라벨러 · 접착제 노즐 · 컨베이어 · 실링설비</p>
        <p class="ind-card-desc">포장라인에 축적되는 접착제, 잉크, 바니시, 종이분진과 제품 잔류물을 제거해 라벨링·실링·이송설비를 관리합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/printing.html" aria-label="인쇄 솔루션 보기" style="--reveal-delay:0.18s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">12</span>
        <span class="ind-card-en">PRINTING</span>
        <h3>인쇄</h3>
        <p class="ind-card-kw">인쇄기 · 롤러 · 잉크 트레이 · 기어 · 피더</p>
        <p class="ind-card-desc">플렉소·그라비어·옵셋 등 인쇄설비의 경화 잉크, 그리스와 종이분진을 제거하면서 롤러와 정밀 구동부를 보호합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/textiles.html" aria-label="섬유 솔루션 보기" style="--reveal-delay:0s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-textile.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">13</span>
        <span class="ind-card-en">TEXTILES</span>
        <h3>섬유</h3>
        <p class="ind-card-kw">카딩기 · 방적기 · 직기 · 텐터 · 염색 롤러</p>
        <p class="ind-card-desc">섬유 비산물, 왁스·그리스, 라텍스, 접착제와 염료 잔류물을 제거하여 롤러와 직조·가공설비를 세정합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/engineered-wood.html" aria-label="엔지니어드 우드 솔루션 보기" style="--reveal-delay:0.06s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-wood.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">14</span>
        <span class="ind-card-en">ENGINEERED WOOD</span>
        <h3>엔지니어드 우드</h3>
        <p class="ind-card-kw">프레스 · 프레스 플레이트 · 건조기 · 접착제 도포설비</p>
        <p class="ind-card-desc">MDF·HDF·OSB 생산설비에 축적되는 접착수지, 피치, 목섬유와 미세분진을 제거하여 프레스와 생산라인을 유지관리합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/rail.html" aria-label="철도 · 대중교통 솔루션 보기" style="--reveal-delay:0.12s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-transit.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">15</span>
        <span class="ind-card-en">RAIL & PUBLIC TRANSPORTATION</span>
        <h3>철도 · 대중교통</h3>
        <p class="ind-card-kw">대차 · 차축 · 견인모터 · 제어반 · 전기설비</p>
        <p class="ind-card-desc">철도차량의 대차·휠셋과 기계부품부터 견인모터·제어반·절연설비까지 정비 세정에 적용해 차량 가동중단을 줄입니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
    <a class="ind-card reveal" href="../industries/mining.html" aria-label="광업 솔루션 보기" style="--reveal-delay:0.18s">
      <div class="ind-card-media"><img src="../assets/img/ind-card-mining.png" alt="" loading="lazy" /></div>
      <div class="ind-card-body">
        <span class="ind-card-num">16</span>
        <span class="ind-card-en">MINING</span>
        <h3>광업</h3>
        <p class="ind-card-kw">크러셔 · 컨베이어 · 중장비 · 펌프 · 전기설비</p>
        <p class="ind-card-desc">채굴·선광·운송설비에 축적되는 광물분진, 오일·그리스와 카본을 제거하고 중장비 및 전기설비의 정비를 지원합니다.</p>
        <span class="ind-card-more">솔루션 보기 <i>→</i></span>
      </div>
    </a>
  </div>
</div>

<div class="ind-feat" id="ind-maint">
  <span class="ind-ghost" aria-hidden="true">02</span>
  <div class="ind-feat-wrap">
    <div class="cmp-vs-head ind-head">
      <span class="cmp-num">02<span class="cmp-num-of">/ 03</span></span>
      <div>
        <span class="cmp-vs-title">CROSS-INDUSTRY MAINTENANCE · FACILITY MAINTENANCE</span>
        <h2 class="cmp-h2">산업을 넘어 공통으로 필요한<br>설비·시설 유지보수</h2>
        <div class="cmp-lead ind-lead">
          <p>생산설비와 공장 인프라의 유지보수는 특정 산업에만 해당하지 않습니다.</p>
          <p>컨베이어, 로봇, 모터, 열교환기, 제어반, 배관 및 각종 생산 지원설비처럼 거의 모든 제조현장에 공통으로 존재하는 설비도 드라이아이스 세척의 중요한 적용 대상입니다.</p>
        </div>
      </div>
    </div>
    <div class="ind-feat-inner">
      <div class="ind-feat-media reveal">
        <img src="../assets/img/ind-card-maintenance.png" alt="생산설비와 공장 인프라의 유지보수 세척" loading="lazy" />
        <span class="ind-feat-tag">CROSS-INDUSTRY · ALL PLANTS</span>
      </div>
      <div class="ind-feat-body reveal" style="--reveal-delay:0.12s">
        <span class="ind-feat-label">대표 대상 <em>08</em></span>
        <ul class="ind-feat-list">
          <li>생산설비</li>
          <li>산업용 로봇</li>
          <li>컨베이어</li>
          <li>모터 · 발전기</li>
          <li>전기 · 제어반</li>
          <li>열교환기 · 냉각설비</li>
          <li>배관 · 공장 인프라</li>
          <li>물류 · 운반장비</li>
        </ul>
        <a class="ind-feat-more" href="../industries/facility-maintenance.html" aria-label="생산설비 · 시설 유지보수 솔루션 보기">생산설비 · 시설 유지보수 솔루션 보기 <i>→</i></a>
      </div>
    </div>
  </div>
</div>

<div class="cmp-section ind-hub ind-svc" id="ind-svc">
  <span class="ind-ghost" aria-hidden="true">03</span>
  <div class="cmp-vs-head ind-head">
    <span class="cmp-num">03<span class="cmp-num-of">/ 03</span></span>
    <div>
      <span class="cmp-vs-title">SPECIALIZED SERVICES &amp; RESTORATION · 전문 세척 · 복원 분야 5</span>
      <h2 class="cmp-h2">생산공정 밖, 전문 세척과<br>복원 현장에서도 쓰입니다.</h2>
      <div class="cmp-lead ind-lead">
        <p>제조산업뿐 아니라 전문 산업세척, 재해복구, 오염 제거 및 복원 작업에도 드라이아이스 세척이 활용됩니다.</p>
        <p>생산공정이 아닌 현장 서비스와 복원 작업의 관점에서 적용 범위를 확인해보세요.</p>
      </div>
    </div>
  </div>
  <div class="ind-list">
    <a class="ind-row reveal" href="../industries/contract-cleaning.html" aria-label="전문 세척 서비스 솔루션 보기" style="--reveal-delay:0s">
      <span class="ind-row-num">17</span>
      <span class="ind-row-media"><img src="../assets/img/ind-card-cleaning-service.png" alt="" loading="lazy" /></span>
      <span class="ind-row-title"><span class="ind-row-en">CONTRACT CLEANING</span><b>전문 세척 서비스</b></span>
      <span class="ind-row-text"><span class="ind-row-kw">산업설비 · 현장 세척 · 복원 · 전문 클리닝 서비스</span><span class="ind-row-desc">고객 현장의 설비와 오염 조건에 맞춰 산업세척, 유지보수, 복원·오염제거 작업을 제공하는 전문 서비스 분야입니다.</span></span>
      <span class="ind-row-more">솔루션 보기 <i>→</i></span>
    </a>
    <a class="ind-row reveal" href="../industries/restoration.html" aria-label="화재 · 수해 복원 솔루션 보기" style="--reveal-delay:0.06s">
      <span class="ind-row-num">18</span>
      <span class="ind-row-media"><img src="../assets/img/ind-card-fire-restoration.png" alt="" loading="lazy" /></span>
      <span class="ind-row-title"><span class="ind-row-en">FIRE & WATER RESTORATION</span><b>화재 · 수해 복원</b></span>
      <span class="ind-row-text"><span class="ind-row-kw">그을음 · 탄화물 · 연기 오염 · 수해 손상 · 악취</span><span class="ind-row-desc">화재 후 숯·그을음과 냄새의 원인이 되는 잔류물을 제거하고, 수해·침수로 오염된 구조물의 복원 세정에도 활용됩니다.</span></span>
      <span class="ind-row-more">솔루션 보기 <i>→</i></span>
    </a>
    <a class="ind-row reveal" href="../industries/mold-remediation.html" aria-label="곰팡이 제거 솔루션 보기" style="--reveal-delay:0.12s">
      <span class="ind-row-num">19</span>
      <span class="ind-row-media"><img src="../assets/img/ind-card-mold-removal.png" alt="" loading="lazy" /></span>
      <span class="ind-row-title"><span class="ind-row-en">MOLD REMEDIATION</span><b>곰팡이 제거</b></span>
      <span class="ind-row-text"><span class="ind-row-kw">목재 구조물 · 다락 · 크롤스페이스 · 벽체 내부</span><span class="ind-row-desc">보와 장선, 못·배선 주변처럼 접근하기 어려운 곳의 곰팡이 오염을 물과 연마재 없이 제거하는 복원 공정에 활용됩니다.</span></span>
      <span class="ind-row-more">솔루션 보기 <i>→</i></span>
    </a>
    <a class="ind-row reveal" href="../industries/historical-restoration.html" aria-label="역사적 건축물 · 문화재 복원 솔루션 보기" style="--reveal-delay:0.18s">
      <span class="ind-row-num">20</span>
      <span class="ind-row-media"><img src="../assets/img/ind-card-heritage.png" alt="" loading="lazy" /></span>
      <span class="ind-row-title"><span class="ind-row-en">HISTORICAL RESTORATION</span><b>역사적 건축물 · 문화재 복원</b></span>
      <span class="ind-row-text"><span class="ind-row-kw">석재 · 벽돌 · 목재 · 금속 · 조형물 · 문화재</span><span class="ind-row-desc">오래된 건축물과 기념물, 박물관 유물의 오염·그을음·생물성 침착물을 제거하면서 원래 표면과 세부 형상을 보존합니다.</span></span>
      <span class="ind-row-more">솔루션 보기 <i>→</i></span>
    </a>
    <a class="ind-row reveal" href="../industries/automotive-detailing.html" aria-label="자동차 복원 · 디테일링 솔루션 보기" style="--reveal-delay:0.24s">
      <span class="ind-row-num">21</span>
      <span class="ind-row-media"><img src="../assets/img/ind-card-detailing.png" alt="" loading="lazy" /></span>
      <span class="ind-row-title"><span class="ind-row-en">AUTOMOTIVE RESTORATION & DETAILING</span><b>자동차 복원 · 디테일링</b></span>
      <span class="ind-row-text"><span class="ind-row-kw">하부 · 엔진룸 · 휠하우스 · 섀시 · 정밀부품</span><span class="ind-row-desc">오일, 그리스와 도로 오염물을 제거하면서 도장면·고무·전기부품 등 차량의 원래 마감과 디테일을 최대한 보존합니다.</span></span>
      <span class="ind-row-more">솔루션 보기 <i>→</i></span>
    </a>
  </div>
</div>

    </div>
  </section>

  <section class="cmp-dark ind-dark">
    <div class="wrap">
      <div class="ind-ae">
        <div class="ind-ae-copy">
          <span class="cmp-eyebrow">APPLICATION ENGINEERING</span>
          <h2 class="cmp-h2">같은 산업이라도,<br>세척해야 할 것은 모두 다릅니다.</h2>
          <div class="cmp-dark-body">
            <p>자동차 공장 안에서도 사출금형의 이형제, 용접 지그의 스패터, 도장라인의 오버스프레이는 오염물도, 세척 대상도, 필요한 세척 강도도 서로 다릅니다.</p>
            <p>따라서 드라이아이스 세척은 산업이나 장비 모델만 보고 결정할 수 없습니다. 바테크는 실제 오염물의 종류와 부착 정도, 세척 대상의 재질과 형상, 작업 환경과 원하는 결과를 확인한 뒤 실제 세척 테스트를 통해 적절한 세척 조건을 찾습니다.</p>
          </div>
          <div class="ind-ae-key reveal">
            <span class="ind-ae-key-en">APPLICATION FIRST. <em>MACHINE SECOND.</em></span>
            <p class="ind-ae-key-main">장비를 먼저 고르는 것이 아니라,<br>세척 조건을 먼저 찾습니다.</p>
          </div>
        </div>
        <div class="ind-ae-visual">
          <div class="ind-ae-cases reveal">
            <span class="ind-ae-label">ONE PLANT · THREE DIFFERENT JOBS</span>
            <ul class="ind-ae-case-list">
              <li>
                <span class="ind-ae-case-img"><img src="../assets/img/ind-card-plastics.png" alt="" loading="lazy" /></span>
                <b>사출금형</b><small>이형제 · 수지 잔류</small>
              </li>
              <li>
                <span class="ind-ae-case-img"><img src="../assets/img/ind-card-automotive.png" alt="" loading="lazy" /></span>
                <b>용접 지그</b><small>Weld Spatter</small>
              </li>
              <li>
                <span class="ind-ae-case-img"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /></span>
                <b>도장라인</b><small>Paint Overspray</small>
              </li>
            </ul>
            <p class="ind-ae-case-note">오염물이 다르면 <em>세척 조건도 달라집니다.</em></p>
          </div>
          <ol class="ind-ae-steps">
            <li class="ind-ae-step reveal">
              <span class="ind-ae-num">01</span>
              <span class="ind-ae-step-img"><img src="../assets/img/ind-card-rubber-tire.png" alt="오염된 금형 근접" loading="lazy" /></span>
              <div class="ind-ae-step-body">
                <span class="ind-ae-step-en">SITE ASSESSMENT</span>
                <h3>현장 조건 확인</h3>
                <p class="ind-ae-step-lead">무엇을, 어디서, 어떤 상태로 닦아야 하는지부터 봅니다.</p>
                <ul class="ind-ae-tags"><li>오염물</li><li>재질</li><li>형상</li><li>작업환경</li><li>목표 결과</li></ul>
              </div>
            </li>
            <li class="ind-ae-step reveal" style="--reveal-delay:0.06s">
              <span class="ind-ae-num">02</span>
              <span class="ind-ae-step-img"><img src="../assets/img/guide-hero-work.jpg" alt="실제 드라이아이스 세척 테스트" loading="lazy" /></span>
              <div class="ind-ae-step-body">
                <span class="ind-ae-step-en">CLEANING TEST</span>
                <h3>실제 세척 테스트</h3>
                <p class="ind-ae-step-lead">실제 오염물과 대상으로 직접 분사해 확인합니다.</p>
                <ul class="ind-ae-tags"><li>분사 압력</li><li>드라이아이스 입자 크기</li><li>공급량</li><li>노즐</li><li>분사 거리 · 각도</li></ul>
              </div>
            </li>
            <li class="ind-ae-step reveal" style="--reveal-delay:0.12s">
              <span class="ind-ae-num">03</span>
              <span class="ind-ae-step-img"><img src="../assets/img/compare-hero.jpg" alt="노즐과 분사 조건 디테일" loading="lazy" /></span>
              <div class="ind-ae-step-body">
                <span class="ind-ae-step-en">OPTIMIZATION</span>
                <h3>조건 최적화</h3>
                <p class="ind-ae-step-lead">닦이는 정도와 표면 영향, 작업성 사이의 균형을 맞춥니다.</p>
                <ul class="ind-ae-tags"><li>세척 속도</li><li>표면 영향</li><li>오염물 제거 정도</li><li>작업성</li><li>드라이아이스 사용량</li></ul>
              </div>
            </li>
            <li class="ind-ae-step reveal" style="--reveal-delay:0.18s">
              <span class="ind-ae-num">04</span>
              <span class="ind-ae-step-img"><img src="../assets/img/stackdo-automation.jpg" alt="Cold Jet 장비와 자동화 시스템" loading="lazy" /></span>
              <div class="ind-ae-step-body">
                <span class="ind-ae-step-en">PROPOSAL</span>
                <h3>장비 및 적용방법 제안</h3>
                <p class="ind-ae-step-lead">확인된 조건에 맞는 장비와 작업 방식을 제안합니다.</p>
                <ul class="ind-ae-tags"><li>적합한 장비</li><li>노즐 구성</li><li>세척 조건</li><li>작업 방식</li><li>자동화 가능성 검토</li></ul>
              </div>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page">
    <div class="wrap">
<div class="cmp-section is-first cmp-cta">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">FROM TEST TO APPLICATION</span>
    <h2 class="cmp-h2">우리 공정에도<br>적용할 수 있을까요?</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>세척 대상과 오염물, 현재 세척 방식을 알려주시면 실제 테스트를 통해 적용 가능성과 적정 조건을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 · 데모 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">기술 상담 →</a>
    </div>
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
  <a class="sub-card" href="compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
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
          <h3 style="font-size: 25px">우리 산업의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

TASK_BODY = """
  <section class="subhero-parallax">
    <img class="subhero-parallax-img" src="../assets/img/guide-hero-work.jpg" alt="산업설비에 적용되는 드라이아이스 세척" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="index.html">드라이아이스 세척가이드</a> &gt; 작업별 솔루션</div>
    <div class="subhero-textbox tsk-hero-box">
      <span class="ind-hero-eyebrow">APPLICATIONS</span>
      <h1>작업별 솔루션</h1>
      <p class="cmp-hero-p">같은 드라이아이스 세척이라도 무엇을 제거하고, 무엇을 보호해야 하는지에 따라<br>필요한 세척 조건과 적용 방법은 달라집니다.<br>금형 세척부터 생산설비 유지보수, 접착제·코팅 제거, 표면 전처리와 부품 마무리까지<br>작업 목적에 맞는 솔루션을 확인해보세요.</p>
    </div>
  </section>
  <section class="subhero-cover cmp-page ind-page tsk-page">
    <div class="wrap">

<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">FIND YOUR APPLICATION</span>
  <h2 class="cmp-h2">산업이 달라도,<br>현장에서 반복되는 세척 과제는 비슷합니다.</h2>
  <div class="cmp-lead">
    <p>자동차, 반도체, 플라스틱, 식품, 발전과 같은 산업은 서로 다르지만 생산현장에서 발생하는 세척 과제에는 공통점이 있습니다.</p>
    <p>금형에는 이형제와 수지가 쌓이고, 생산설비에는 오일과 공정 잔류물이 축적되며, 용접라인에는 스패터가, 도장라인에는 오버스프레이가 남습니다. 또한 접착제 제거, 표면 전처리, 디버링·디플래싱처럼 세척을 넘어 생산공정 자체를 지원하는 작업도 있습니다.</p>
    <p>작업별 솔루션에서는 "어느 산업인가"보다 무엇을 제거해야 하는지, 어떤 표면을 보호해야 하는지, 어떤 결과가 필요한지를 기준으로 적합한 적용 방법을 살펴봅니다.</p>
  </div>
  <ul class="cmp-criteria ind-criteria tsk-keys reveal" aria-label="작업을 보는 세 가지 기준">
    <li><span>01</span><b>REMOVE</b><small>무엇을 제거할 것인가</small></li>
    <li><span>02</span><b>PROTECT</b><small>무엇을 보호할 것인가</small></li>
    <li><span>03</span><b>RESULT</b><small>어떤 결과가 필요한가</small></li>
  </ul>
</div>
</div>
</div>

<div class="cmp-section ind-hub tsk-group" id="tsk-g1">
  <span class="ind-ghost" aria-hidden="true">01</span>
  <div class="cmp-vs-head ind-head">
    <span class="cmp-num">01<span class="cmp-num-of">/ 04</span></span>
    <div>
      <span class="cmp-vs-title">EQUIPMENT & TOOL CLEANING · 설비 · 툴링 세척</span>
      <h2 class="cmp-h2">생산설비와 금형, 치공구의<br>본래 표면과 기능을 지키면서 세척합니다.</h2>
      <div class="cmp-lead ind-lead"><p>생산설비와 금형, 치공구의 본래 표면과 기능을 유지하면서 생산 과정에서 축적된 오염물을 제거합니다.</p></div>
    </div>
  </div>
  <div class="tsk-grid">
      <a class="tsk-card reveal is-wide" href="../applications/mold-tool-cleaning.html" aria-label="금형 · 툴링 세척 자세히 보기" style="--reveal-delay:0s">
        <span class="tsk-media"><img src="../assets/img/task-mold-tool-cleaning.webp" alt="" loading="lazy" /><span class="tsk-num">01</span></span>
        <div class="tsk-body">
          <span class="tsk-en">MOLD & TOOL CLEANING</span>
          <h3>금형 · 툴링 세척</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 대상</dt><dd>사출금형 · 고무금형 · 타이어금형 · 복합재 툴 · 다이캐스팅 툴 · 성형금형</dd></div>
            <div class="tsk-row"><dt>대표 오염</dt><dd>이형제 · 수지 · 고무 잔사 · 카본 · 생산 잔류물</dd></div>
          </dl>
          <p class="tsk-desc">복잡한 형상과 정밀한 표면을 유지하면서 금형과 툴링에 축적된 공정 잔류물을 제거합니다. 플라스틱·고무 금형 세척과 복합재 툴 세척을 하나의 솔루션으로 다룹니다.</p>
          <div class="tsk-rel"><span>관련 산업</span><ul><li>자동차 제조</li><li>플라스틱 · 복합소재</li><li>고무 · 타이어</li><li>주조 · 다이캐스팅</li><li>우주 · 항공</li></ul></div>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal" href="../industries/facility-maintenance.html" aria-label="생산설비 · 시설 유지보수 자세히 보기" style="--reveal-delay:0.06s">
        <span class="tsk-media"><img src="../assets/img/ind-card-maintenance.png" alt="" loading="lazy" /><span class="tsk-num">02</span></span>
        <div class="tsk-body">
          <span class="tsk-en">PRODUCTION & FACILITY MAINTENANCE</span>
          <h3>생산설비 · 시설 유지보수</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 대상</dt><dd>컨베이어 · 체인 · 롤러 · 생산설비 · 팬 · 열교환기 · 배관 · 물류장비 · 공장 인프라</dd></div>
          </dl>
          <p class="tsk-desc">설비를 가능한 한 현장에서 유지한 상태로 축적된 오염물을 제거하여 정비시간과 생산 중단 부담을 줄이는 데 활용합니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal" href="../applications/weld-fixture-robot.html" aria-label="용접라인 · 지그 · 로봇 세척 자세히 보기" style="--reveal-delay:0.12s">
        <span class="tsk-media"><img src="../assets/img/task-weld-fixture.webp" alt="" loading="lazy" /><span class="tsk-num">03</span></span>
        <div class="tsk-body">
          <span class="tsk-en">WELD LINE, FIXTURE & ROBOT CLEANING</span>
          <h3>용접라인 · 지그 · 로봇 세척</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 대상</dt><dd>용접 지그 · 클램프 · 로봇 · 센서 · 치공구</dd></div>
            <div class="tsk-row"><dt>대표 오염</dt><dd>Weld Spatter · Slag · Grease · 생산 잔류물</dd></div>
          </dl>
          <p class="tsk-desc">용접라인과 자동화 설비에 축적되는 스패터와 공정 오염물을 제거해 지그와 센서, 로봇의 정상적인 작동을 유지합니다.</p>
          <div class="tsk-rel"><span>관련 산업</span><ul><li>자동차 제조</li><li>일반 제조</li><li>철도 · 대중교통</li><li>중공업</li></ul></div>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal" href="../applications/paint-booth-coating-line.html" aria-label="도장부스 · 코팅라인 세척 자세히 보기" style="--reveal-delay:0.18s">
        <span class="tsk-media"><img src="../assets/img/task-pretreatment.jpg" alt="" loading="lazy" /><span class="tsk-num">04</span></span>
        <div class="tsk-body">
          <span class="tsk-en">PAINT BOOTH & COATING LINE CLEANING</span>
          <h3>도장부스 · 코팅라인 세척</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 대상</dt><dd>도장부스 · Grating · Paint Hook · Carrier · Conveyor · Robot</dd></div>
            <div class="tsk-row"><dt>대표 오염</dt><dd>Paint Overspray · Coating Residue</dd></div>
          </dl>
          <p class="tsk-desc">도장공정 주변에 반복적으로 축적되는 오버스프레이와 코팅 잔류물을 제거하여 설비와 생산라인을 관리합니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal" href="../applications/electrical-electronic.html" aria-label="전기 · 전자 장비 세척 자세히 보기" style="--reveal-delay:0s">
        <span class="tsk-media"><img src="../assets/img/method-electrical-terminal.png" alt="" loading="lazy" /><span class="tsk-num">05</span></span>
        <div class="tsk-body">
          <span class="tsk-en">ELECTRICAL & ELECTRONIC EQUIPMENT CLEANING</span>
          <h3>전기 · 전자 장비 세척</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 대상</dt><dd>모터 · 발전기 · 제어반 · 센서 · 전기부품 · 전자부품 · 정밀장치</dd></div>
          </dl>
          <p class="tsk-desc">수분 사용을 피해야 하는 전기·전자 설비와 정밀 부품의 오염 제거에 건식 세척의 특성을 활용합니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
  </div>
</div>

<div class="cmp-section ind-hub tsk-group" id="tsk-g2">
  <span class="ind-ghost" aria-hidden="true">02</span>
  <div class="cmp-vs-head ind-head">
    <span class="cmp-num">02<span class="cmp-num-of">/ 04</span></span>
    <div>
      <span class="cmp-vs-title">CONTAMINANT REMOVAL · 오염물 제거</span>
      <h2 class="cmp-h2">오염물이 다르면<br>필요한 세척 강도와 입자 조건도 다릅니다.</h2>
      <div class="cmp-lead ind-lead"><p>오염물의 종류와 부착 특성에 따라 필요한 세척 강도와 입자 조건은 달라집니다.</p></div>
    </div>
  </div>
  <div class="tsk-grid">
      <a class="tsk-card reveal" href="../applications/adhesive-resin-removal.html" aria-label="접착제 · 수지 제거 자세히 보기" style="--reveal-delay:0s">
        <span class="tsk-media"><img src="../assets/img/task-adhesive-rollers.webp" alt="" loading="lazy" /><span class="tsk-num">06</span></span>
        <div class="tsk-body">
          <span class="tsk-en">ADHESIVE & RESIN REMOVAL</span>
          <h3>접착제 · 수지 제거</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 오염</dt><dd>Glue · Hot Melt · Urethane · Epoxy · Sealant · Label Adhesive · Resin</dd></div>
            <div class="tsk-row"><dt>대표 대상</dt><dd>롤러 · 노즐 · 지그 · 금형 · 생산설비</dd></div>
          </dl>
          <p class="tsk-desc">접착제와 수지가 축적되는 생산설비와 부품을 화학용제나 과도한 기계적 제거 없이 세척합니다.</p>
          <div class="tsk-rel"><span>관련 산업</span><ul><li>포장</li><li>인쇄</li><li>자동차 제조</li><li>우주 · 항공</li><li>반도체 · 전자 제조</li></ul></div>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal" href="../applications/ink-paint-coating-removal.html" aria-label="잉크 · 도료 · 코팅 제거 자세히 보기" style="--reveal-delay:0.06s">
        <span class="tsk-media"><img src="../assets/img/ind-card-printing.png" alt="" loading="lazy" /><span class="tsk-num">07</span></span>
        <div class="tsk-body">
          <span class="tsk-en">INK, PAINT & COATING REMOVAL</span>
          <h3>잉크 · 도료 · 코팅 제거</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 오염</dt><dd>Ink · Paint · Varnish · Overspray · Coating Residue</dd></div>
            <div class="tsk-row"><dt>대표 대상</dt><dd>인쇄설비 · 롤러 · 도장설비 · 지그 · 생산라인</dd></div>
          </dl>
          <p class="tsk-desc">인쇄와 도장, 코팅공정에서 발생하는 잉크와 도료 잔류물을 설비와 표면 상태를 고려해 제거합니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal" href="../applications/oil-grease-residue-removal.html" aria-label="오일 · 그리스 · 고착 오염 제거 자세히 보기" style="--reveal-delay:0.12s">
        <span class="tsk-media"><img src="../assets/img/task-oil-tar-pipe.webp" alt="" loading="lazy" /><span class="tsk-num">08</span></span>
        <div class="tsk-body">
          <span class="tsk-en">OIL, GREASE & HEAVY RESIDUE REMOVAL</span>
          <h3>오일 · 그리스 · 고착 오염 제거</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 오염</dt><dd>Oil · Grease · Bitumen · Asphalt · Carbon · Paraffin · Process Residue</dd></div>
            <div class="tsk-row"><dt>대표 대상</dt><dd>생산설비 · 기계부품 · 배관 · 중장비 · 플랜트 설비</dd></div>
          </dl>
          <p class="tsk-desc">설비에 축적된 유분과 고착된 생산 잔류물을 제거하여 유지보수와 점검을 용이하게 합니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal" href="../applications/rust-corrosion-removal.html" aria-label="녹 · 부식 · 산화물 제거 자세히 보기" style="--reveal-delay:0.18s">
        <span class="tsk-media"><img src="../assets/img/task-surface-rust.webp" alt="" loading="lazy" /><span class="tsk-num">09</span></span>
        <div class="tsk-body">
          <span class="tsk-en">RUST, CORROSION & OXIDATION REMOVAL</span>
          <h3>녹 · 부식 · 산화물 제거</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 오염</dt><dd>표면 녹 · 느슨한 산화물 · 부식 생성물</dd></div>
            <div class="tsk-row"><dt>적용 범위</dt><dd>비마모성 세척 — 깊게 피팅된 녹이나 백색 금속면을 위한 강한 표면처리에는 한계가 있습니다</dd></div>
          </dl>
          <p class="tsk-desc">표면 녹과 느슨하게 부착된 산화물 등을 제거하여 검사 및 유지보수를 돕습니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
  </div>
</div>

<div class="cmp-section ind-hub tsk-group" id="tsk-g3">
  <span class="ind-ghost" aria-hidden="true">03</span>
  <div class="cmp-vs-head ind-head">
    <span class="cmp-num">03<span class="cmp-num-of">/ 04</span></span>
    <div>
      <span class="cmp-vs-title">PROCESS & PART FINISHING · 공정 · 부품 마무리</span>
      <h2 class="cmp-h2">세척을 넘어,<br>다음 공정을 준비하고 부품을 마무리합니다.</h2>
      <div class="cmp-lead ind-lead"><p>드라이아이스 기술은 단순한 설비 세척을 넘어 다음 생산공정을 준비하거나 부품을 마무리하는 공정에도 활용됩니다.</p></div>
    </div>
  </div>
  <div class="tsk-grid">
      <a class="tsk-card reveal" href="../applications/surface-preparation.html" aria-label="표면 전처리 자세히 보기" style="--reveal-delay:0s">
        <span class="tsk-media"><img src="../assets/img/ind-card-aerospace.png" alt="" loading="lazy" /><span class="tsk-num">10</span></span>
        <div class="tsk-body">
          <span class="tsk-en">SURFACE PREPARATION</span>
          <h3>표면 전처리</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 공정</dt><dd>도장 전 · 코팅 전 · 접착 전 · 용접 전 · 검사 전</dd></div>
            <div class="tsk-row"><dt>대표 오염</dt><dd>Oil · Mold Release · Dust · Fingerprint · Process Residue</dd></div>
          </dl>
          <p class="tsk-desc">후속 공정에 영향을 줄 수 있는 오일, 이형제, 먼지와 생산 잔류물을 제거해 표면을 다음 공정에 적합한 상태로 준비합니다.</p>
          <div class="tsk-rel"><span>관련 산업</span><ul><li>자동차 제조</li><li>우주 · 항공</li><li>플라스틱 · 복합소재</li><li>의료기기 제조</li><li>일반 제조</li></ul></div>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="tsk-card reveal is-finishing" href="../applications/deburring-deflashing.html" aria-label="디버링 · 디플래싱 자세히 보기" style="--reveal-delay:0.06s">
        <span class="tsk-media"><img src="../assets/img/task-deburring-precision.jpg" alt="" loading="lazy" /><span class="tsk-num">11</span></span>
        <div class="tsk-body">
          <span class="tsk-en">DEBURRING & DEFLASHING</span>
          <h3>디버링 · 디플래싱</h3>
          <dl class="tsk-rows">
            <div class="tsk-row"><dt>대표 대상</dt><dd>플라스틱 · 고무 · 정밀부품 · 커넥터 · 의료부품 · 성형부품</dd></div>
            <div class="tsk-row"><dt>구분</dt><dd>Cleaning이 아닌 Parts Finishing — 제품의 치수와 주요 형상을 유지하는 마무리 공정</dd></div>
          </dl>
          <p class="tsk-desc">성형 또는 가공 후 발생한 Burr와 Flash를 제거하면서 제품의 치수와 주요 형상을 유지하는 부품 마무리 공정에 활용합니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
  </div>
</div>

<div class="cmp-section ind-hub tsk-group" id="tsk-g4">
  <span class="ind-ghost" aria-hidden="true">04</span>
  <div class="cmp-vs-head ind-head">
    <span class="cmp-num">04<span class="cmp-num-of">/ 04</span></span>
    <div>
      <span class="cmp-vs-title">RESTORATION & REMEDIATION · 복원 · 오염 제거</span>
      <h2 class="cmp-h2">생산공정 밖,<br>복원과 재해복구 현장에서도 쓰입니다.</h2>
      <div class="cmp-lead ind-lead"><p>생산공정 외에도 화재, 수해, 곰팡이 및 각종 복원 작업에서 드라이아이스 세척의 건식·비마모 특성을 활용할 수 있습니다.</p></div>
    </div>
  </div>
  <div class="tsk-grid">
      <a class="tsk-card reveal is-wide" href="../cleaning/industry.html#ind-svc" aria-label="복원 · 재해복구 자세히 보기" style="--reveal-delay:0s">
        <span class="tsk-media"><img src="../assets/img/ind-card-fire-restoration.png" alt="" loading="lazy" /><span class="tsk-num">12</span></span>
        <div class="tsk-body">
          <span class="tsk-en">RESTORATION & REMEDIATION</span>
          <h3>복원 · 재해복구</h3>
          <dl class="tsk-rows">
            <div class="tsk-row is-sub"><dt>세부 영역</dt><dd><ul class="tsk-sub"><li><b>곰팡이 제거</b><i>Mold Remediation</i></li><li><b>화재 · 그을음 복원</b><i>Fire &amp; Smoke Restoration</i></li><li><b>수해 복원</b><i>Water Damage Restoration</i></li><li><b>역사적 건축물 · 문화재 복원</b><i>Historical Restoration</i></li><li><b>자동차 복원 · 디테일링</b><i>Automotive Restoration &amp; Detailing</i></li><li><b>전자장비 복원</b><i>Electronic Device Refurbishing</i></li></ul></dd></div>
          </dl>
          <p class="tsk-desc">물과 연마재를 쓰기 어려운 구조물과 유물, 차량과 전자장비의 복원 작업에서 표면을 보존하며 오염을 제거합니다. 세부 영역은 콘텐츠가 갖춰지는 대로 개별 상세 페이지로 확장합니다.</p>
          <span class="tsk-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
  </div>
</div>


    </div>
  </section>

  <section class="cmp-dark ind-dark tsk-dark">
    <div class="wrap">
      <div class="tsk-test">
        <div class="tsk-test-copy">
          <span class="cmp-eyebrow">APPLICATION TEST</span>
          <h2 class="cmp-h2">같은 오염물이라도,<br>세척 조건은 달라질 수 있습니다.</h2>
          <div class="cmp-dark-body">
            <p>같은 접착제나 수지라도 부착된 표면의 재질, 오염물의 두께와 경화 상태, 작업 온도와 접근성에 따라 필요한 세척 조건은 달라집니다.</p>
            <p>바테크는 실제 부품이나 시편을 이용해 적용 가능성을 확인하고, 드라이아이스 입자 크기, 분사 압력, 공급량, 노즐, 분사 거리와 각도 등을 조정해 적합한 세척 조건을 검토합니다.</p>
          </div>
        </div>
        <div class="tsk-test-side reveal">
          <span class="ind-ae-label">TEST VARIABLES</span>
          <ul class="tsk-vars">
            <li>드라이아이스 입자 크기</li>
            <li>분사 압력</li>
            <li>공급량</li>
            <li>노즐</li>
            <li>분사 거리 · 각도</li>
          </ul>
          <p class="tsk-test-key">결과는 장비가 아니라,<br><em>적절한 적용 조건</em>에서 시작됩니다.</p>
          <div class="cmp-cta-btns">
            <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
            <a class="cmp-btn-ghost" href="../cases/library.html">적용사례 보기 →</a>
          </div>
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
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
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
          <h3 style="font-size: 25px">우리 작업의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">제거할 오염물과 보호할 표면을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
"""

# (2026-09-08, 11차 핸드오프) "도입 가이드" 전면 개편 — compare/industry와 같은 편집형 구조로 전환.
ADOPT_BODY = """
  
  <!-- 기술 내용 출처(Cold Jet 공식): The Definitive Guide to Dry Ice Blasting, Cold Jet FAQ, Dry Ice Blasting Startup Guide,
       Compressed Air Guide, Facility Maintenance 자료. 수치(공기량 예시 등)는 Cold Jet 매뉴얼의 대표값이며 실제 요구조건은
       장비·노즐·작업조건에 따라 달라진다는 점을 각 섹션에 명시. 이미지는 기존 로컬 자료(adopt-*.jpg) 재사용. -->
  <section class="subhero-parallax auto-hero-stage">
    <img class="subhero-parallax-img" src="../assets/img/adopt-basic-setup.jpg" alt="드라이아이스 블라스터 기본 구성 — 블라스터, 압축공기, 드라이아이스 공급" />
    <div class="subhero-breadcrumb wrap"><a href="../index.html">홈</a> &gt; <a href="../cleaning/index.html">드라이아이스 세척가이드</a> &gt; 도입 가이드</div>
    <div class="subhero-textbox auto-hero-box">
      <span class="ind-hero-eyebrow">IMPLEMENTATION GUIDE</span>
      <h1>드라이아이스 세척 도입 가이드</h1>
      <p class="cmp-hero-p auto-hero-lead">장비를 고르기 전에,<br>우리 현장에 맞는 세척 조건부터 확인하세요.</p>
    </div>
  </section>

  <section class="subhero-cover cmp-page ind-page auto-page">
    <div class="wrap">
<div class="cmp-panel">
<div class="wrap">
<div class="cmp-section is-first auto-intro">
  <div class="auto-intro-grid">
    <div class="reveal">
      <span class="cmp-eyebrow">START WITH THE APPLICATION</span>
      <h2 class="cmp-h2">첫 번째 질문은<br>"어떤 장비가 좋은가?"가 아닙니다.</h2>
    </div>
    <div class="cmp-lead auto-intro-lead reveal" style="--reveal-delay:0.14s">
      <p>드라이아이스 세척의 도입은 장비 한 대를 선택하는 것으로 끝나지 않습니다. 무엇을 세척하는지, 어떤 오염물을 제거해야 하는지, 어느 정도까지 세척해야 하는지부터 압축공기와 드라이아이스 공급, 작업공간과 안전조건, 장비와 노즐 구성까지 함께 검토해야 합니다.</p>
      <p class="auto-intro-close">바테크는 실제 세척 대상과 작업 조건을 확인하고 테스트를 통해 적용 가능성을 검토한 뒤, 현장에 맞는 장비와 운용 방법을 제안합니다.</p>
    </div>
  </div>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>무엇을 세척합니까?</b><p>금형, 생산설비, 모터, 제어반, 부품, 로봇, 컨베이어, 표면 등</p></li>
    <li class="reveal" style="--reveal-delay:0.06s"><b>무엇을 제거해야 합니까?</b><p>이형제, 수지, 접착제, 오일, 그리스, 카본, 잉크, 도료, 스패터, 표면 녹 등</p></li>
    <li class="reveal" style="--reveal-delay:0.12s"><b>지켜야 할 것은 무엇입니까?</b><p>정밀한 금형면, 도장면, 코팅, 치수, 마킹, 센서, 배선, 제품 외관</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>어느 정도까지 세척해야 합니까?</b><p>육안 청정, 후공정 전처리, 설비 유지보수, 품질 안정, 검사 전 세척</p></li>
    <li class="reveal" style="--reveal-delay:0.24s"><b>지금 가장 문제되는 것은?</b><p>세척시간, 많은 인력, 설비 분해, 화학약품, 생산 중단시간</p></li>
  </ol>
</div>
</div>
</div>

<div class="cmp-section auto-apps-sec" id="auto-apps">

<article class="auto-app is-wide">
  <div class="auto-app-head reveal">
    <span class="auto-num">01</span>
    <div><span class="auto-en">APPLICATION TEST</span><h3>실제 세척 테스트</h3></div>
  </div>
  <div class="cmp-lead reveal" style="--reveal-delay:0.1s; max-width:820px">
    <p>같은 오염물이라도 부착 정도와 두께, 세척 대상의 재질과 형상, 온도와 표면 상태에 따라 세척 결과는 달라질 수 있습니다. 따라서 장비를 선택하기 전에 가능하면 실제 생산부품이나 금형, 설비 또는 동일 조건의 샘플을 이용해 세척 테스트를 진행하는 것이 좋습니다.</p>
    <p class="auto-intro-close">테스트의 목적은 단순히 "닦이는지"를 확인하는 것이 아니라, 현장에서 반복해서 사용할 수 있는 조건을 찾는 것입니다.</p>
  </div>
  <div class="auto-targets reveal" style="--reveal-delay:0.16s">
    <span>테스트 확인 항목</span>
    <ul><li>오염물 제거 정도</li><li>세척 속도</li><li>표면 변화</li><li>세밀한 형상 접근성</li><li>드라이아이스 소비량</li><li>필요한 압축공기</li><li>적절한 노즐</li><li>작업 편의성</li><li>예상 작업시간</li><li>자동화 가능성</li></ul>
  </div>
  <div class="auto-targets reveal" style="--reveal-delay:0.22s">
    <span>테스트 전 준비사항</span>
    <ul><li>실제 세척 대상 또는 샘플</li><li>제거해야 할 오염물</li><li>현재 세척방법 · 세척시간 · 작업 인원</li><li>설비 분해 여부</li><li>반드시 보호해야 할 표면</li><li>원하는 세척 결과</li><li>세척 빈도(일/주/월)</li><li>예상 작업 면적</li><li>사용 가능한 압축공기 정보</li><li>현장 사진 또는 동영상</li></ul>
  </div>
  <a class="auto-rel-link reveal" href="../rental/demo.html" style="--reveal-delay:0.28s"><span>다음 단계</span>세척 테스트 신청 <i>→</i></a>
</article>

<article class="auto-app is-wide">
  <div class="auto-app-head reveal">
    <span class="auto-num">02</span>
    <div><span class="auto-en">COMPRESSED AIR</span><h3>압축공기 확인</h3></div>
  </div>
  <div class="cmp-lead reveal" style="--reveal-delay:0.1s; max-width:820px">
    <p>드라이아이스 블라스터는 압축공기로 드라이아이스 입자를 가속합니다. 실제 세척 성능에는 압력뿐 아니라 공기량, 수분, 온도, 배관 크기와 호스 길이도 영향을 줍니다.</p>
  </div>
  <p class="mtc-quote reveal" style="--reveal-delay:0.14s">bar만큼 중요한 것이 <em>공기량(CFM · m³/min)</em>입니다.</p>
  <div class="adopt-2col reveal" style="--reveal-delay:0.18s">
    <div>
      <h4>공장 압축공기 · PLANT AIR</h4>
      <p class="adopt-2col-b">기존 설비를 활용할 수 있어 별도 콤프레서 이동이 필요 없는 경우가 많습니다.</p>
      <ul><li>사용 가능한 압력·유량</li><li>동시에 사용 중인 다른 에어툴</li><li>배관 직경 · 커넥션 크기</li><li>압력강하 · 공기 품질</li></ul>
    </div>
    <div>
      <h4>이동식 콤프레서 · MOBILE COMPRESSOR</h4>
      <p class="adopt-2col-b">야외 작업, 공장 에어가 부족한 장소, 이동 작업에 적합합니다.</p>
      <ul><li>디젤 콤프레서는 토출 공기가 뜨겁고 수분이 많을 수 있음</li><li>애프터쿨러 필요 여부</li><li>수분 분리기 필요 여부</li></ul>
    </div>
  </div>
  <p class="adopt-note reveal" style="--reveal-delay:0.24s"><b>AIR QUALITY MATTERS —</b> 드라이아이스는 약 −78.5°C로 매우 낮은 온도입니다. 공급공기에 수분이 많으면 얼어 피드라인과 노즐, 장비 내부에 문제를 일으킬 수 있고, 지나치게 뜨거운 공기는 드라이아이스의 승화를 촉진할 수 있습니다. 건조하고(Dry) 적정 온도(Cool)이며 충분한 유량(Flow)인지 함께 확인해야 합니다.</p>
  <table class="spec-table reveal" style="--reveal-delay:0.30s">
    <tr><th>펠렛 타입 참고값</th><td>약 2.8 m³/min(100 CFM), 5.5 bar(80 PSI) 수준</td></tr>
    <tr><th>마이크로파티클 참고값</th><td>약 0.9 m³/min(30 CFM) 수준</td></tr>
  </table>
  <p style="font-size:13px; color:var(--text-muted); margin-top:-6px;">* Cold Jet 매뉴얼의 대표값이며, 실제 요구 조건은 장비 모델과 노즐, 작업 조건에 따라 달라질 수 있습니다.</p>
</article>

<article class="auto-app is-wide">
  <div class="auto-app-head reveal">
    <span class="auto-num">03</span>
    <div><span class="auto-en">DRY ICE SUPPLY</span><h3>드라이아이스 공급</h3></div>
  </div>
  <div class="cmp-lead reveal" style="--reveal-delay:0.1s; max-width:820px">
    <p>드라이아이스는 보관 중에도 계속 승화합니다. 따라서 사용량과 사용 빈도, 배송 일정, 보관 방법을 장비 선택과 함께 고려해야 합니다.</p>
  </div>
  <div class="auto-targets reveal" style="--reveal-delay:0.16s">
    <span>확인 요소</span>
    <ul><li>사용하는 드라이아이스 형태(펠렛 · 마이크로파티클)</li><li>예상 소비량 · 작업 빈도</li><li>공급 거리 · 배송 주기</li><li>보관 컨테이너 · 보관시간</li><li>작업당 필요 수량</li></ul>
  </div>
  <p class="adopt-note reveal" style="--reveal-delay:0.22s">실제 소비량은 장비, 분사조건, 노즐, 오염물, 작업속도에 따라 달라지므로 일반화된 수치보다 테스트를 통한 확인을 권장합니다.</p>
  <a class="auto-rel-link reveal" href="../products/supply.html" style="--reveal-delay:0.28s"><span>관련 페이지</span>드라이아이스 공급 안내 <i>→</i></a>
</article>

<article class="auto-app is-wide">
  <div class="auto-app-head reveal">
    <span class="auto-num">04</span>
    <div><span class="auto-en">SITE &amp; SAFETY</span><h3>작업환경과 안전</h3></div>
  </div>
  <div class="cmp-lead reveal" style="--reveal-delay:0.1s; max-width:820px"><p>작업 장소도 장비 선택의 중요한 조건입니다.</p></div>
  <ol class="auto-why">
    <li class="reveal" style="--reveal-delay:0.00s"><b>환기</b><p>드라이아이스는 승화하며 CO₂가 됩니다. 밀폐공간·지하·탱크·피트처럼 환기가 제한된 곳에서는 CO₂가 축적될 수 있어 환기와 CO₂ 모니터링을 검토해야 합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.06s"><b>보호장비(PPE)</b><p>보안경, 적절한 장갑, 청력 보호구 착용이 필요합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.12s"><b>소음</b><p>압축공기를 사용하는 공정이므로 작업자 청력 보호와 주변 환경을 함께 고려합니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.18s"><b>제거된 오염물</b><p>드라이아이스는 승화하지만 제거된 오염물은 남습니다. 오염물 종류에 따라 집진·격리·회수·처리가 필요할 수 있습니다.</p></li>
    <li class="reveal" style="--reveal-delay:0.24s"><b>전기설비</b><p>건식·비전도성이라는 특성만으로 모든 활선 설비를 안전하게 세척할 수 있다고 일반화하지 않습니다. 제조사 기준과 전원 상태, 절연·밀폐 상태, 현장 안전규정을 확인해야 합니다.</p></li>
  </ol>
</article>

<article class="auto-app is-wide">
  <div class="auto-app-head reveal">
    <span class="auto-num">05</span>
    <div><span class="auto-en">MACHINE SELECTION</span><h3>장비 · 노즐 선정</h3></div>
  </div>
  <div class="cmp-lead reveal" style="--reveal-delay:0.1s; max-width:820px"><p>세척 테스트가 끝나면, 그 조건을 안정적으로 구현할 장비를 선택합니다. 모델을 먼저 보기보다, 아래 요소를 먼저 확인합니다.</p></div>
  <div class="auto-targets reveal" style="--reveal-delay:0.16s">
    <span>선정 시 고려 요소</span>
    <ul><li>필요한 세척 강도(정밀 ↔ 중오염 제거)</li><li>입자 크기(마이크로파티클 · 3mm 펠렛 · PCS 조절)</li><li>필요 압력과 공기량</li><li>드라이아이스 공급량</li><li>작업 면적 · 작업시간</li><li>장비 이동성</li><li>현장 에어 공급 방식</li><li>정밀 제어 필요성</li><li>자동화 가능성 · 작업 빈도</li></ul>
  </div>
  <table class="spec-table reveal" style="--reveal-delay:0.22s">
    <tr><th>정밀 금형 · 전자부품</th><td>낮은 공급량, 미세 입자, 세밀한 제어</td></tr>
    <tr><th>생산설비 · 오일·그리스</th><td>적절한 분사력, 작업속도, 넓은 노즐 선택지</td></tr>
    <tr><th>주조 · 고착 오염</th><td>높은 제거력, 충분한 공기량, 높은 작업량</td></tr>
    <tr><th>표면 전처리 · 자동화</th><td>반복성, 정밀한 제어, 로봇 통합</td></tr>
  </table>
  <p style="font-size:13px; color:var(--text-muted); margin-top:-6px;">* 예시이며, 실제 장비 모델은 VATEK 제품 라인업과 Cold Jet 최신 사양을 확인해 상담을 통해 안내합니다.</p>
  <div class="cmp-text auto-text reveal" style="--reveal-delay:0.28s">
    <p><b>노즐이 왜 중요한가.</b> 같은 장비도 어떤 노즐을 쓰느냐에 따라 분사폭, 집중도, 접근성, 공기소비량이 달라집니다. 넓은 면에는 넓은 분사폭, 좁은 홈에는 집중 노즐, 깊은 구조에는 긴 노즐, 민감한 표면에는 낮은 임팩트 조건이 검토됩니다.</p>
    <p><b>자동화가 필요한가.</b> 동일 부품을 반복 세척하고 사이클타임과 오염물이 일정하며 작업자 접근이 어려운 위치라면 자동화를 검토할 수 있습니다. 다품종·낮은 작업빈도·불규칙한 설비에는 수동 장비가 더 적합할 수 있습니다.</p>
  </div>
  <a class="auto-rel-link reveal" href="../products/compare-equip.html" style="--reveal-delay:0.34s"><span>관련 페이지</span>장비 비교·추천받기 <i>→</i></a>
</article>

</div>
</div>
</div>

<div class="cmp-panel auto-cont-panel">
<div class="wrap">
<div class="cmp-section is-first">
  <span class="cmp-eyebrow">TOTAL CLEANING COST</span>
  <h2 class="cmp-h2 reveal">장비 가격만 비교하면,<br>실제 세척비용을 알기 어렵습니다.</h2>
  <div class="auto-targets reveal" style="--reveal-delay:0.1s">
    <span>비교해야 할 요소</span>
    <ul><li>세척시간 · 인력</li><li>생산 중단시간</li><li>분해 · 재조립</li><li>냉각 · 건조 시간</li><li>화학약품 · 폐수 처리</li><li>연마재 처리 비용</li><li>드라이아이스 · 압축공기</li><li>장비 유지보수</li><li>표면 손상 위험</li></ul>
  </div>
  <p class="mtc-quote reveal" style="--reveal-delay:0.16s">세척하는 시간뿐 아니라, <em>세척 때문에 멈추는 시간</em>까지 함께 비교해보세요.</p>
</div>

<div class="cmp-section">
  <span class="cmp-eyebrow">TEST BEFORE YOU INVEST</span>
  <h2 class="cmp-h2 reveal">구매를 결정하기 전에,<br>실제 현장에서 확인해보세요.</h2>
  <div class="process-flow reveal" style="--reveal-delay:0.1s">
    <div class="step"><div class="num">1</div><h4>TEST</h4><p>실제 오염물 세척 가능성 확인</p></div>
    <div class="step"><div class="num">2</div><h4>DEMO</h4><p>작업자가 장비와 작업성 확인</p></div>
    <div class="step"><div class="num">3</div><h4>RENTAL</h4><p>일정기간 생산현장에서 사용</p></div>
    <div class="step"><div class="num">4</div><h4>PURCHASE</h4><p>적합한 조건 확인 후 도입</p></div>
    <div class="step"><div class="num">5</div><h4>AUTOMATION</h4><p>반복공정은 자동화 검토</p></div>
  </div>
</div>

<div class="cmp-section">
  <span class="cmp-eyebrow">AFTER INSTALLATION</span>
  <h2 class="cmp-h2 reveal">장비를 공급하는 것으로,<br>도입이 끝나지는 않습니다.</h2>
  <div class="auto-targets reveal" style="--reveal-delay:0.1s">
    <span>도입 이후 지원</span>
    <ul><li>설치 · 시운전</li><li>운영자 교육</li><li>노즐 선택 지원</li><li>예방정비 · A/S</li><li>부품 공급</li><li>드라이아이스 공급</li></ul>
  </div>
  <p class="mtc-quote reveal" style="--reveal-delay:0.16s">도입 검토부터 현장 적용, <em>교육과 A/S까지</em> 바테크가 전 과정을 지원합니다.</p>
</div>

<div class="cmp-section">
  <span class="cmp-eyebrow">BEFORE YOU START</span>
  <h2 class="cmp-h2 reveal">전체 도입 흐름</h2>
  <div class="process-flow is-7 reveal" style="--reveal-delay:0.1s">
    <div class="step"><div class="num">1</div><h4>APPLICATION</h4><p>세척 과제 확인</p></div>
    <div class="step"><div class="num">2</div><h4>TEST</h4><p>실제 세척 테스트</p></div>
    <div class="step"><div class="num">3</div><h4>SITE</h4><p>현장조건 확인</p></div>
    <div class="step"><div class="num">4</div><h4>UTILITY</h4><p>압축공기 · 드라이아이스</p></div>
    <div class="step"><div class="num">5</div><h4>EQUIPMENT</h4><p>장비 · 노즐 선정</p></div>
    <div class="step"><div class="num">6</div><h4>VALIDATION</h4><p>Demo · Rental · 도입</p></div>
    <div class="step"><div class="num">7</div><h4>SUPPORT</h4><p>교육 · 운영 · A/S</p></div>
  </div>
</div>
</div>
</div>

    </div>
  </section>

  <section class="faq-section wrap">
    <div class="faq-head">
      <h2 style="font-size: 46px; margin: 36px 0 0; padding-top: 20px; color: #000000">자주 묻는 질문 <span class="faq-en" style="font-size: 30px">FAQ</span></h2>
      <p class="faq-intro">도입을 검토하실 때 가장 많이 받는 질문을 정리했습니다.</p>
    </div>
    <div class="faq-list">
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">우리 공장 압축공기를 사용할 수 있나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>가능 여부는 압력뿐 아니라 사용 가능한 유량과 공기 품질, 배관 조건을 함께 확인해야 합니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">이동식 콤프레서를 별도로 사야 하나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>기존 공장 압축공기가 필요한 압력과 유량을 공급할 수 있다면 별도의 이동식 콤프레서가 필요하지 않을 수 있습니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">드라이아이스는 얼마나 사용하나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>장비와 오염물, 압력, 공급량, 노즐, 세척속도에 따라 달라지므로 테스트를 통해 예상 사용량을 확인하는 것이 가장 정확합니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">어떤 장비가 가장 좋나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>하나의 장비가 모든 작업에 가장 좋은 것은 아닙니다. 세척 대상과 오염물, 필요한 작업속도와 현장조건에 따라 달라집니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">작업자가 별도 교육을 받아야 하나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>장비 운전, 세척 조건, PPE와 안전, 기본 유지보수에 대한 교육이 필요합니다. 바테크는 설치 시 운영자 교육을 함께 진행합니다.</p></div>
      </details>
      <details class="faq-item">
        <summary><span class="faq-q" style="font-size: 25px">밀폐된 공간에서도 사용할 수 있나요?</span><span class="faq-toggle" aria-hidden="true"></span></summary>
        <div class="faq-a"><p>CO₂ 축적 위험을 고려해야 하며, 환기와 CO₂ 모니터링 등 별도의 안전 검토가 필요합니다.</p></div>
      </details>
    </div>
  </section>

  <section class="subhero-cover cmp-page cmp-tail ind-page auto-page">
    <div class="wrap">
<div class="cmp-section is-first cmp-cta auto-cta reveal">
  <div class="cmp-cta-left">
    <span class="cmp-eyebrow">START WITH A TEST</span>
    <h2 class="cmp-h2">우리 현장에 맞는지,<br>먼저 실제 세척으로 확인해보세요.</h2>
  </div>
  <div class="cmp-cta-right">
    <div class="cmp-text">
      <p>드라이아이스 세척은 세척 대상과 오염물, 작업환경에 따라 결과가 달라집니다.</p>
      <p>바테크는 실제 부품과 금형, 설비 또는 샘플을 이용한 테스트를 통해 세척 가능성, 필요한 작업 조건, 적합한 장비와 노즐을 함께 검토합니다.</p>
    </div>
    <div class="cmp-cta-btns">
      <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청 →</a>
      <a class="cmp-btn-ghost" href="../products/quote.html">도입 상담 →</a>
      <a class="cmp-btn-ghost" href="../products/index.html">장비 보기 →</a>
    </div>
  </div>
</div>
    </div>
  </section>

<div class="last-freeze">
<div class="wrap">
<h2 style="font-size: 46px; padding-top: 30px">함께 보면 좋은 페이지</h2>
      <div class="sub-grid" id="subGrid">
  <a class="sub-card" href="../cleaning/guide.html">
    <div class="sub-card-media"><img src="../assets/img/guide-principle-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">원리 · 기초</span>
      <h3 style="font-size: 25px">드라이아이스 세척의 이해</h3>
      <p style="font-size: 20px">드라이아이스의 물리적 특성부터 세척 원리와 장점, 세척 장비의 기본 개념까지 살펴봅니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/compare.html">
    <div class="sub-card-media"><img src="../assets/img/compare-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">비교 · 차이점</span>
      <h3 style="font-size: 25px">타 세척방식과 비교</h3>
      <p style="font-size: 20px">연마재·화학용제·고압세척 등 기존 방식과 드라이아이스 세척의 차이를 비교합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/task.html">
    <div class="sub-card-media"><img src="../assets/img/task-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">작업별 적용</span>
      <h3 style="font-size: 25px">작업별 솔루션</h3>
      <p style="font-size: 20px">이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
  <a class="sub-card" href="../cleaning/industry.html">
    <div class="sub-card-media"><img src="../assets/img/industry-thumb.jpg" alt="" loading="lazy" /></div>
    <div class="sub-card-body">
      <span class="sub-card-tag">산업별 적용</span>
      <h3 style="font-size: 25px">산업별 솔루션</h3>
      <p style="font-size: 20px">자동차·반도체·식품·발전 등 산업별 주요 세척 대상과 적용 방법을 안내합니다.</p>
      <span class="sub-card-more">자세히 보기 →</span>
    </div>
  </a>
</div>
      <div class="cta-band">
        <div>
          <h3 style="font-size: 25px">우리 생산라인의 세척 조건을 함께 검토해보세요</h3>
          <p style="font-size: 20px">세척 대상과 오염물을 알려주시면 적용 가능성과 적정 조건을 안내합니다.</p>
        </div>
        <a class="cta-btn" href="../rental/demo.html">세척 테스트 신청</a>
      </div>
      </div>
    </div>
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
# (2026-09-09, 14차 핸드오프 — 통합 최종본) products/index.html("제품·자동화·공급"
# 허브) 전면 리디자인 본문. SOLUTION ARCHITECTURE / SYSTEM ARCHITECTURE MAP /
# OUR SOLUTIONS 6개 / WHAT DO YOU NEED / AUTOMATION SPOTLIGHT 3단계 /
# COLD JET TECHNOLOGY 4개 / VATEK SUPPORT 6단계 / PURCHASE SUPPORT 3 / FINAL CTA.
PRODUCTS_HUB_BODY = """
  <div class="wrap breadcrumb"><a href="../index.html">홈</a> &gt; 제품·자동화·공급</div>

  <!-- ============ HERO ============ -->
  <section class="prd-hero">
    <div class="wrap prd-hero-grid">
      <div>
        <span class="prd-hero-eyebrow">PRODUCTS · AUTOMATION · SUPPLY</span>
        <h1>세척기 한 대부터,<br>생산·회수·자동화까지.</h1>
        <p class="prd-hero-sub">VATEK은 Cold Jet 드라이아이스 블라스터, 펠렛타이저, CO<sub>2</sub> 리커버리, 자동화 시스템과 드라이아이스 공급을 현장 조건에 맞게 구성합니다.</p>
        <p class="prd-hero-note">장비를 하나씩 판매하는 것이 아니라, 고객의 사용량과 공정, 생산 조건에 맞는 전체 시스템을 검토합니다.</p>
        <div class="prd-hero-btns">
          <a class="cta-btn" href="#prd-solutions">제품·시스템 보기 →</a>
          <a class="cmp-btn-ghost" href="compare-equip.html">장비 추천받기 →</a>
        </div>
        <div class="prd-hero-trust"><img src="../assets/img/coldjet-logo.png" alt="Cold Jet" />Cold Jet 대한민국 공식 대리점 · 설치 · 교육 · A/S · 드라이아이스 공급</div>
      </div>
      <div class="prd-hero-media">
        <figure class="is-tall"><img src="../assets/img/blaster-operator-t.png" alt="Cold Jet 드라이아이스 블라스터로 세척하는 작업자" /><figcaption>DRY ICE BLASTER</figcaption></figure>
        <figure><img src="../assets/img/stackdo-pelletizer.jpg" alt="Cold Jet 펠렛타이저" /><figcaption>PELLETIZER</figcaption></figure>
        <figure><img src="../assets/img/stackdo-automation.jpg" alt="자동화 드라이아이스 세척 시스템" /><figcaption>AUTOMATION</figcaption></figure>
      </div>
    </div>
  </section>

  <!-- ============ SOLUTION ARCHITECTURE ============ -->
  <section class="prd-arch">
    <div class="wrap prd-arch-grid">
      <div>
        <span class="cmp-eyebrow">SOLUTION ARCHITECTURE</span>
        <h2>필요한 것은<br>장비 한 대가 아니라,<br>공정에 맞는 구성입니다.</h2>
      </div>
      <div class="prd-arch-body">
        <p>세척 대상과 오염물, 압축공기 조건, 드라이아이스 사용량, 생산량과 자동화 수준에 따라 필요한 시스템은 달라집니다.</p>
        <p>VATEK은 세척부터 드라이아이스 생산, CO<sub>2</sub> 회수와 자동화까지 전체 운용 조건을 함께 검토합니다.</p>
      </div>
    </div>
  </section>

  <!-- ============ SYSTEM ARCHITECTURE MAP ============ -->
  <section class="prd-map">
    <div class="wrap">
      <div class="prd-map-head">
        <span class="cmp-eyebrow">SYSTEM ARCHITECTURE</span>
        <h2>VATEK이 구성할 수 있는<br>시스템의 흐름입니다.</h2>
      </div>
      <div class="prd-map-grid">
        <div class="prd-map-card">
          <b>A · 구매하여 사용</b>
          <div class="prd-map-flow">
            <div class="prd-map-node"><img src="../assets/img/adopt-pelletizer.jpg" alt="" />드라이아이스 공급</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><img src="../assets/img/stackdo-blaster.jpg" alt="" />드라이아이스 블라스터</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><div class="ph"></div>세척 작업</div>
          </div>
        </div>
        <div class="prd-map-card">
          <b>B · 직접 생산</b>
          <div class="prd-map-flow">
            <div class="prd-map-node"><div class="ph"></div>액체 CO2</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><img src="../assets/img/stackdo-pelletizer.jpg" alt="" />펠렛타이저</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><div class="ph"></div>드라이아이스</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><img src="../assets/img/stackdo-blaster.jpg" alt="" />블라스터 · 세척</div>
          </div>
        </div>
        <div class="prd-map-card">
          <b>C · CO2 회수</b>
          <div class="prd-map-flow">
            <div class="prd-map-node"><img src="../assets/img/stackdo-pelletizer.jpg" alt="" />펠렛타이저</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><div class="ph"></div>배출 CO2</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><div class="ph"></div>CO2 리커버리</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><div class="ph"></div>액체 CO2</div>
            <div class="prd-map-loop">↺ 펠렛타이저로 재투입</div>
          </div>
        </div>
        <div class="prd-map-card">
          <b>D · 자동화</b>
          <div class="prd-map-flow">
            <div class="prd-map-node"><img src="../assets/img/stackdo-pelletizer.jpg" alt="" />드라이아이스 생산</div>
            <div class="prd-map-node"><div class="ph"></div>입자 제어</div>
            <div class="prd-map-node"><img src="../assets/img/stackdo-blaster.jpg" alt="" />블라스팅 시스템</div>
            <div class="prd-map-node"><img src="../assets/img/stackdo-automation.jpg" alt="" />로봇 · 생산라인</div>
            <div class="prd-map-arrow">↓</div>
            <div class="prd-map-node"><b style="font-weight:800">자동화 세척</b></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ OUR SOLUTIONS ============ -->
  <section class="prd-solutions" id="prd-solutions">
    <div class="wrap">
      <div class="prd-sol-head">
        <div>
          <span class="cmp-eyebrow">OUR SOLUTIONS</span>
          <h2>필요한 구성만 선택하세요.</h2>
        </div>
      </div>
      <div class="prd-sol-grid">
        <a class="prd-sol-card" href="blaster/index.html">
          <div class="prd-sol-media"><img src="../assets/img/stackdo-blaster.jpg" alt="드라이아이스 세척기" loading="lazy" /></div>
          <div class="prd-sol-body">
            <span class="prd-sol-num">01 / DRY ICE BLASTERS</span>
            <h3>드라이아이스 세척기</h3>
            <p>정밀 세정부터 강한 산업 오염 제거까지, 세척 대상과 필요한 세정력에 맞는 Cold Jet 블라스터를 선택합니다.</p>
            <span class="prd-sol-kw">Smart · Pellet · MicroParticle · Specialty</span>
            <span class="prd-sol-cta">블라스터 살펴보기 →</span>
          </div>
        </a>
        <a class="prd-sol-card" href="pelletizer/index.html">
          <div class="prd-sol-media"><img src="../assets/img/stackdo-pelletizer.jpg" alt="드라이아이스 제조기" loading="lazy" /></div>
          <div class="prd-sol-body">
            <span class="prd-sol-num">02 / DRY ICE PRODUCTION</span>
            <h3>드라이아이스 제조기</h3>
            <p>액체 CO2를 이용해 필요한 곳에서 신선한 드라이아이스를 직접 생산하는 펠렛타이저 시스템입니다.</p>
            <span class="prd-sol-kw">On-demand production · Pelletizers</span>
            <span class="prd-sol-cta">펠렛타이저 살펴보기 →</span>
          </div>
        </a>
        <a class="prd-sol-card" href="recovery/index.html">
          <div class="prd-sol-media img-ph" style="display:flex;align-items:center;justify-content:center;">[제품 이미지]</div>
          <div class="prd-sol-body">
            <span class="prd-sol-num">03 / CO2 RECOVERY</span>
            <h3>CO2 리커버리</h3>
            <p>드라이아이스 생산 과정에서 배출되는 CO2 가스를 회수·액화하여 다시 드라이아이스 생산에 활용할 수 있도록 구성하는 시스템입니다.</p>
            <span class="prd-sol-kw">Recover · Reuse · CO2 utilization</span>
            <span class="prd-sol-cta">CO2 리커버리 살펴보기 →</span>
          </div>
        </a>
        <a class="prd-sol-card is-featured" href="automation.html">
          <div class="prd-sol-media"><img src="../assets/img/stackdo-automation.jpg" alt="자동화 시스템" loading="lazy" /></div>
          <div class="prd-sol-body">
            <span class="prd-sol-num">04 / AUTOMATION</span>
            <h3>자동화 시스템</h3>
            <p>드라이아이스 블라스팅을 로봇과 생산라인에 통합하여 반복 세척, 표면 전처리 및 부품 마감 공정을 자동화합니다.</p>
            <span class="prd-sol-kw">Robot integration · COMBI PCS</span>
            <span class="prd-sol-cta">자동화 시스템 보기 →</span>
          </div>
        </a>
        <a class="prd-sol-card" href="nozzle.html">
          <div class="prd-sol-media"><img src="../assets/img/blaster-operator-t.png" alt="노즐·액세서리" loading="lazy" /></div>
          <div class="prd-sol-body">
            <span class="prd-sol-num">05 / NOZZLES &amp; ACCESSORIES</span>
            <h3>노즐·액세서리</h3>
            <p>같은 장비라도 노즐, 호스와 Applicator 구성에 따라 세정 범위와 작업성, 세정 효율이 달라집니다.</p>
            <span class="prd-sol-kw">Nozzles · Applicators · Hoses</span>
            <span class="prd-sol-cta">노즐·액세서리 보기 →</span>
          </div>
        </a>
        <a class="prd-sol-card" href="supply.html">
          <div class="prd-sol-media"><img src="../assets/img/adopt-pelletizer.jpg" alt="드라이아이스 구매·공급" loading="lazy" /></div>
          <div class="prd-sol-body">
            <span class="prd-sol-num">06 / DRY ICE SUPPLY</span>
            <h3>드라이아이스 구매·공급</h3>
            <p>장비 운용에 필요한 드라이아이스를 정기 공급부터 필요 시 단건 구매까지 지원합니다.</p>
            <span class="prd-sol-kw">Dry ice · Regular supply</span>
            <span class="prd-sol-cta">드라이아이스 공급 안내 →</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- ============ WHAT DO YOU NEED ============ -->
  <section class="prd-need">
    <div class="wrap">
      <span class="cmp-eyebrow">WHAT DO YOU NEED?</span>
      <h2>무엇이 필요하신가요?</h2>
      <div class="prd-need-list">
        <a class="prd-need-row" href="blaster/index.html"><span class="prd-need-q">세척 장비가 필요합니다</span><span class="prd-need-a">드라이아이스 블라스터 →</span></a>
        <a class="prd-need-row" href="pelletizer/index.html"><span class="prd-need-q">드라이아이스 사용량이 많아 직접 생산하고 싶습니다</span><span class="prd-need-a">펠렛타이저 →</span></a>
        <a class="prd-need-row" href="recovery/index.html"><span class="prd-need-q">드라이아이스 생산 시 CO2 사용 효율을 높이고 싶습니다</span><span class="prd-need-a">CO2 리커버리 →</span></a>
        <a class="prd-need-row" href="automation.html"><span class="prd-need-q">세척 공정을 로봇·생산라인에 넣고 싶습니다</span><span class="prd-need-a">자동화 시스템 →</span></a>
        <a class="prd-need-row" href="nozzle.html"><span class="prd-need-q">현재 장비의 세정 성능과 작업성을 개선하고 싶습니다</span><span class="prd-need-a">노즐·액세서리 →</span></a>
        <a class="prd-need-row" href="supply.html"><span class="prd-need-q">드라이아이스를 안정적으로 공급받고 싶습니다</span><span class="prd-need-a">드라이아이스 공급 →</span></a>
      </div>
    </div>
  </section>

  <!-- ============ AUTOMATION SPOTLIGHT ============ -->
  <section class="prd-auto">
    <div class="wrap">
      <div class="prd-auto-head">
        <span class="cmp-eyebrow">FROM MANUAL TO FULL AUTOMATION</span>
        <h2>작업자가 사용하는 한 대의 장비에서,<br>완전 자동화 생산라인까지.</h2>
      </div>
      <div class="prd-auto-grid">
        <div class="prd-auto-card">
          <span class="prd-auto-lv">LEVEL 01</span>
          <h3>MANUAL CLEANING</h3>
          <p>작업자가 이동형 블라스터를 직접 사용합니다.</p>
          <div class="prd-auto-tags"><span>Flexible</span><span>Mobile</span><span>Multi-purpose</span></div>
        </div>
        <div class="prd-auto-card">
          <span class="prd-auto-lv">LEVEL 02</span>
          <h3>ROBOT INTEGRATED</h3>
          <p>블라스터를 기존 로봇 셀 또는 생산설비와 연동합니다.</p>
          <div class="prd-auto-tags"><span>Repeatability</span><span>Process Control</span><span>Line Integration</span></div>
        </div>
        <div class="prd-auto-card">
          <span class="prd-auto-lv">LEVEL 03</span>
          <h3>FULLY INTEGRATED</h3>
          <p>드라이아이스 생산 + 입자 제어 + 블라스팅 + 로봇·생산라인까지 하나로 연결합니다.</p>
          <div class="prd-auto-tags"><span>Continuous</span><span>Automated</span><span>COMBI PCS</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ COLD JET TECHNOLOGY ============ -->
  <section class="prd-tech">
    <div class="wrap">
      <span class="cmp-eyebrow">COLD JET TECHNOLOGY</span>
      <h2>장비 성능은 디테일에서 달라집니다.</h2>
      <div class="prd-tech-grid">
        <div class="prd-tech-card"><h3>FEEDER TECHNOLOGY</h3><p>드라이아이스 입자의 품질과 안정적인 공급을 고려한 공급 기술입니다.</p></div>
        <div class="prd-tech-card"><h3>NOZZLE TECHNOLOGY</h3><p>작업 조건에 따라 분사 패턴과 세정 효율을 최적화하는 노즐 구성입니다.</p></div>
        <div class="prd-tech-card"><h3>PARTICLE CONTROL</h3><p>민감한 표면부터 강한 오염까지 작업 목적에 맞게 입자 크기를 제어합니다.</p></div>
        <div class="prd-tech-card"><h3>SYSTEM INTEGRATION</h3><p>블라스터부터 생산·회수·자동화 시스템까지 연결 가능한 시스템 구성입니다.</p></div>
      </div>
    </div>
  </section>

  <!-- ============ VATEK SUPPORT ============ -->
  <section class="prd-support">
    <div class="wrap">
      <div class="prd-support-head">
        <span class="cmp-eyebrow">VATEK SUPPORT</span>
        <h2>제품을 공급하는 데서 끝나지 않습니다.</h2>
        <p>실제 현장에서 장비가 제대로 작동하려면 제품 선택뿐 아니라 압축공기, 전원, CO2 공급, 설치 공간, 노즐 구성과 작업 조건을 함께 검토해야 합니다.</p>
      </div>
      <div class="prd-process">
        <div class="prd-process-step"><div class="num">1</div><h4>공정 검토</h4></div>
        <div class="prd-process-step"><div class="num">2</div><h4>세척 테스트·데모</h4></div>
        <div class="prd-process-step"><div class="num">3</div><h4>장비·시스템 선정</h4></div>
        <div class="prd-process-step"><div class="num">4</div><h4>설치·시운전</h4></div>
        <div class="prd-process-step"><div class="num">5</div><h4>운영 교육</h4></div>
        <div class="prd-process-step"><div class="num">6</div><h4>A/S · 기술지원</h4></div>
      </div>
      <p class="prd-support-final">도입 검토부터 현장 적용, 교육과 A/S까지 바테크가 전 과정을 지원합니다.</p>
    </div>
  </section>

  <!-- ============ PURCHASE SUPPORT ============ -->
  <section class="prd-purchase">
    <div class="wrap">
      <div class="prd-purchase-head">PURCHASE SUPPORT</div>
      <div class="prd-purchase-grid">
        <a class="prd-util-card" href="compare-equip.html"><h4>장비 비교·추천받기</h4><p>어떤 장비가 적합한지 현장 조건을 기준으로 비교해보세요.</p><span>비교해보기 →</span></a>
        <a class="prd-util-card" href="process.html"><h4>구매 프로세스 안내</h4><p>테스트와 검토부터 견적, 계약, 설치까지 도입 절차를 확인하세요.</p><span>절차 보기 →</span></a>
        <a class="prd-util-card" href="quote.html"><h4>견적 요청</h4><p>세척 대상과 현장 조건을 알려주시면 적합한 구성과 견적을 안내합니다.</p><span>견적 요청하기 →</span></a>
      </div>
    </div>
  </section>

  <!-- ============ FINAL CTA ============ -->
  <section class="prd-cta">
    <div class="wrap">
      <span class="cmp-eyebrow" style="color:rgba(255,255,255,0.75)">FIND THE RIGHT SYSTEM</span>
      <h2>어떤 장비가 필요한지<br>아직 결정하지 않으셔도 됩니다.</h2>
      <p>세척 대상과 오염물, 드라이아이스 사용량과 현장 조건을 알려주세요. 필요한 장비와 시스템 구성을 함께 검토해드립니다.</p>
      <div class="prd-cta-btns">
        <a class="cta-btn" href="compare-equip.html">장비 추천받기 →</a>
        <a class="cmp-btn-ghost" href="../rental/demo.html">세척 테스트·데모 신청 →</a>
      </div>
    </div>
  </section>
"""


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
             # (2026-09-07, 6차 핸드오프) compare와 같은 방식 — 페이지 자신의 메타
             # 설명만 page_desc로 덮어쓰고, 메가메뉴·허브 카드가 공유하는
             # desc/nav_desc는 그대로 둔다. 핸드오프 HTML 하단의 인라인 스크립트는
             # compare의 우측 레일 스크립트와 동일(이 페이지엔 레일이 없어 즉시
             # return) — 출력 일치를 위해 같은 상수를 그대로 전달.
             "page_desc": "주요 산업 16개, 산업 공통 설비·시설 유지보수, 전문 세척·복원 분야까지 — 산업별 주요 세척 대상과 드라이아이스 세척 적용 방법을 확인하세요.",
             "full_custom_body": True,
             "extra_script": COMPARE_RAIL_SCRIPT,
             "body": INDUSTRY_BODY},
            {"slug": "task", "title": "작업별 솔루션",
             "desc": "이물질 제거, 몰드 클리닝, 탈청, 도장 전처리 등 작업 유형별 적용 방법을 안내합니다.",
             "nav_desc": "금형 세척부터 표면처리까지, 작업 목적에 맞는 방법을 제안합니다.",
             "nav_img": "assets/img/task-thumb.jpg",
             "rich_content": True,
             # (2026-09-08, 7차 핸드오프) compare/industry와 같은 편집형 구조로 전면
             # 재설계 — full_custom_body 방식으로 전환. desc/nav_desc는 메가메뉴·허브
             # 카드 공유값이라 유지, 페이지 자신의 메타 설명만 page_desc로 덮어쓴다.
             "page_desc": "금형·툴링 세척, 설비 유지보수, 접착제·코팅 제거, 표면 전처리, 디버링·디플래싱, 복원까지 — 무엇을 제거하고 무엇을 보호해야 하는지 기준으로 정리한 드라이아이스 세척 작업별 솔루션.",
             "full_custom_body": True,
             "extra_script": COMPARE_RAIL_SCRIPT,
             "body": TASK_BODY},
            {"slug": "adopt", "title": "도입 가이드",
             "desc": "도입 전 검토사항부터 설치 준비, 운영 체크리스트까지 순서대로 안내합니다.",
             "nav_desc": "도입 검토부터 설치까지, 필요한 절차를 단계별로 안내합니다.",
             "nav_img": "assets/img/adopt-thumb.jpg",
             "rich_content": True,
             # (2026-09-08, 11차 핸드오프) 전면 개편 — full_custom_body 방식으로 전환.
             # desc/nav_desc는 메가메뉴·허브 카드 공유값이라 유지, 페이지 자신의
             # <title>/메타 설명만 page_title/page_desc로 덮어쓴다.
             "page_title": "도입 가이드 | 드라이아이스 세척가이드",
             "page_desc": "장비를 고르기 전에 세척 대상과 오염물, 압축공기와 드라이아이스 공급, 작업환경과 안전조건을 확인하는 드라이아이스 세척 도입 절차 가이드.",
             "full_custom_body": True,
             "extra_script": AUTOMOTIVE_SCRIPT,
             "body": ADOPT_BODY},
        ],
    },
    {
        "code": "products", "label": "제품·자동화·공급", "short": "제품",
        "tagline": "세척기부터 제조기, 자동화 시스템, 소모품 공급까지 한 번에 확인하세요.",
        "nav_eyebrow": "PRODUCTS",
        "nav_intro": "세척기부터 제조기, 자동화까지 필요한 장비를 만나보세요.",
        "full_custom_body": True,
        "page_title": "제품·자동화·공급",
        "page_desc": "Cold Jet 드라이아이스 블라스터, 펠렛타이저, CO2 리커버리, 자동화 시스템과 드라이아이스 공급까지 — 현장 조건에 맞는 시스템을 구성합니다.",
        "body": PRODUCTS_HUB_BODY,
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


# (2026-09-09, 14차 핸드오프 — 통합 최종본) products 메가메뉴 전면 재설계.
# EQUIPMENT & SYSTEMS 5개 + SUPPLY & BUYING GUIDE 4개 2그룹 구조와 하단
# 트러스트 스트립은 기존 megamenu_html()의 단일 flat 리스트 템플릿으로
# 표현할 수 없어 products 전용으로 별도 구성한다. products/index.html
# 자기 자신을 렌더링할 때만(at_root=True) 같은 products/ 디렉터리 내
# 형제 페이지로의 링크를 "blaster/index.html"처럼 상대경로로 줄이고,
# 그 외 모든 페이지에서는 기존과 동일하게 asset("products/...", depth)로
# 계산한다(핸드오프 원본 HTML과 재조립 대조로 두 경우 모두 확인됨).
PRODUCTS_MEGA_ITEMS = [
    ("blaster", True, "드라이아이스 세척기 (블라스터)",
     "정밀 세정부터 강한 산업 오염 제거까지, 세척 대상에 맞는 Cold Jet 블라스터를 선택합니다.",
     "assets/img/stackdo-blaster.jpg", "EQUIPMENT & SYSTEMS"),
    ("pelletizer", True, "드라이아이스 제조기 (펠렛타이저)",
     "액체 CO2를 이용해 필요한 곳에서 신선한 드라이아이스를 직접 생산하는 펠렛타이저 시스템입니다.",
     "assets/img/stackdo-pelletizer.jpg", None),
    ("recovery", True, "CO2 리커버리",
     "드라이아이스 생산 중 배출되는 CO2 가스를 회수·액화해 다시 생산에 활용하는 시스템입니다.",
     None, None),
    ("automation", False, "자동화 시스템",
     "드라이아이스 블라스팅을 로봇과 생산라인에 통합해 반복 세척과 표면 전처리를 자동화합니다.",
     "assets/img/stackdo-automation.jpg", None),
    ("nozzle", False, "노즐·액세서리",
     "노즐과 호스, Applicator 구성에 따라 세정 범위와 작업성, 세정 효율이 달라집니다.",
     "assets/img/blaster-operator-t.png", None),
    ("supply", False, "드라이아이스 구매·공급",
     "장비 운용에 필요한 드라이아이스를 정기 공급부터 필요 시 단건 구매까지 지원합니다.",
     "assets/img/adopt-pelletizer.jpg", "SUPPLY & BUYING GUIDE"),
    ("compare-equip", False, "장비 비교·추천받기",
     "어떤 장비가 적합한지 현장 조건을 기준으로 비교해보세요.", None, None),
    ("process", False, "구매 프로세스 안내",
     "테스트와 검토부터 견적, 계약, 설치까지 도입 절차를 확인하세요.", None, None),
    ("quote", False, "견적 요청",
     "세척 대상과 현장 조건을 알려주시면 적합한 구성과 견적을 안내합니다.", None, None),
]


def products_megamenu_html(depth, at_root=False):
    items_html = []
    for i, (slug, is_group, title, desc, nav_img, group_label) in enumerate(PRODUCTS_MEGA_ITEMS):
        if group_label:
            items_html.append(f'<li class="megamenu-index-group">{group_label.replace("&", "&amp;")}</li>')
        active = " is-active" if i == 0 else ""
        if at_root:
            href = slug + ("/index.html" if is_group else ".html")
        else:
            href = asset("products/" + slug + ("/index.html" if is_group else ".html"), depth)
        img_attr = f' data-img="{asset(nav_img, depth)}"' if nav_img else ""
        items_html.append(
            f'<li class="megamenu-index-item{active}" data-i="{i}"><a href="{href}" data-desc="{desc}"{img_attr}>{title}</a></li>'
        )
    first_slug, first_is_group, first_title, first_desc, first_img, _ = PRODUCTS_MEGA_ITEMS[0]
    first_href = (first_slug + "/index.html") if at_root else asset("products/" + first_slug + "/index.html", depth)
    preview_bg = asset(first_img, depth)
    joined = '\n          '.join(items_html)
    return f"""<div class="megamenu" data-menu="products">
    <div class="megamenu-inner">
      <div class="megamenu-intro">
        <span class="megamenu-eyebrow">PRODUCTS · AUTOMATION · SUPPLY</span>
        <h3>세척부터 생산·회수·자동화까지</h3>
        <p>현장과 생산 조건에 맞는 드라이아이스 시스템을 구성합니다.</p>
      </div>
      <div class="megamenu-index">
        <span class="megamenu-index-label">MENU INDEX</span>
        <ul class="megamenu-index-list">
          <span class="megamenu-index-highlight" aria-hidden="true"></span>
          {joined}
        </ul>
        <div class="megamenu-trust-strip">
          <span>Cold Jet 대한민국 공식 대리점</span><span>세척 테스트·데모</span><span>설치·시운전</span><span>교육·A/S</span>
        </div>
      </div>
      <div class="megamenu-preview">
        <div class="megamenu-preview-img is-active" data-i="0"><div class="megamenu-preview-img-bg is-shown" style="background-image:url('{preview_bg}')"></div></div>
      </div>
      <div class="megamenu-detail">
        <span class="megamenu-detail-title">{first_title}</span>
        <p class="megamenu-detail-desc">{first_desc}</p>
        <a class="megamenu-detail-link" href="{first_href}">자세히 보기 →</a>
      </div>
    </div>
  </div>"""


def nav_html(depth, active_code=None, is_products_hub=False):
    items = []
    for m in MENU:
        li_active = " active" if m["code"] == active_code else ""
        hub_href = asset(f"{m['code']}/index.html", depth)
        menu_block = products_megamenu_html(depth, is_products_hub) if m["code"] == "products" else megamenu_html(m, depth)
        items.append(
            f'<li class="{li_active.strip()}">'
            f'<a href="{hub_href}">{m["label"]}<span class="nav-chevron" aria-hidden="true"></span></a>'
            f'{menu_block}'
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


def page_shell(title, description, depth, active_code, body, is_home=False, extra_script="", is_products_hub=False):
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
{nav_html(depth, active_code, is_products_hub)}
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
    if m.get("full_custom_body"):
        # (2026-09-09, 14차 핸드오프 — 통합 최종본) products/index.html 전면
        # 리디자인 — 기존 sub_grid 카드 나열 허브 템플릿 대신 핸드오프 본문
        # 전체(히어로~FINAL CTA)를 있는 그대로 사용. is_products_hub=True로
        # nav_html()에 전달해 자기 자신에 대한 products 메가메뉴 링크만
        # products/ 디렉터리 상대경로로 줄인다(§ products_megamenu_html 참고).
        html = page_shell(
            m.get("page_title", m["label"]),
            m.get("page_desc", m["tagline"]),
            depth, m["code"], m["body"],
            extra_script=m.get("extra_script", ""),
            is_products_hub=True,
        )
        with open(os.path.join(ROOT, m["code"], "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        return
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


# (2026-09-08) 메뉴에 속하지 않는 상세 페이지 — 산업별 솔루션 카드에서 들어가는
# 산업 상세(industries/<slug>.html). 앞으로 작업별 상세(applications/)도 같은 방식으로 추가.
DETAIL_PAGES = [
    {"dir": "industries", "slug": "automotive", "active_code": "cleaning",
     "page_title": "자동차 제조 | 산업별 솔루션",
     "page_desc": "사출·성형 금형, 용접 지그와 로봇, 도장부스, 다이캐스팅, 표면 전처리, 디버링, 생산설비 유지보수까지 — 자동차 제조공정별 세척 과제와 드라이아이스 세척 적용 방법.",
     "body": AUTOMOTIVE_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "plastics-composites", "active_code": "cleaning",
     "page_title": "플라스틱 · 복합소재 | 산업별 솔루션",
     "page_desc": "플라스틱 · 복합소재 제조의 금형 세척, 디버링·디플래싱, 표면 전처리, 복합재 툴링 세척에 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": PLASTICS_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "rubber-tires", "active_code": "cleaning",
     "page_title": "고무 · 타이어 | 산업별 솔루션",
     "page_desc": "고무 사출·압축 금형과 타이어 금형을 가류기에 장착한 상태로 세척하는 드라이아이스 세척의 적용 방식을 설명합니다.",
     "body": RUBBER_TIRES_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "foundry", "active_code": "cleaning",
     "page_title": "주조 · 다이캐스팅 | 산업별 솔루션",
     "page_desc": "주조·다이캐스팅 현장의 영구금형, 코어박스, 다이캐스팅 금형과 일반 설비에 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": FOUNDRY_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "semiconductor", "active_code": "cleaning",
     "page_title": "반도체 · 전자 제조 | 산업별 솔루션",
     "page_desc": "폴리실리콘 CVD 반응기, 웨이퍼 공정장비, 반도체 몰드, PCB 조립까지 반도체·전자 제조 밸류체인에서 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": SEMICONDUCTOR_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "medical", "active_code": "cleaning",
     "page_title": "의료기기 제조 | 산업별 솔루션",
     "page_desc": "정밀 의료용 금형의 인프레스 세척과 임플란트·수술기구 등 고정밀 의료부품의 디버링·디플래싱에 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": MEDICAL_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "aerospace", "active_code": "cleaning",
     "page_title": "우주 · 항공 | 산업별 솔루션",
     "page_desc": "복합재 툴링, 성형 금형, 접착제 제거, 표면 전처리, 정밀 주조 툴링, 디버링까지 우주·항공 제조에서 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": AEROSPACE_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "food-beverage", "active_code": "cleaning",
     "page_title": "식품 · 음료 | 산업별 솔루션",
     "page_desc": "오븐·로스터, 믹서, 프라이어, 컨베이어, 포장설비, 전기부품까지 식품·음료 생산설비를 물 없이 현장에서 세척하는 방식을 설명합니다.",
     "body": FOOD_BEVERAGE_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "packaging", "active_code": "cleaning",
     "page_title": "포장 | 산업별 솔루션",
     "page_desc": "인쇄·컨버팅 설비, 라벨링·접착 설비, 포장라인, 사출·블로우·PET·열성형 금형까지 포장 산업에서 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": PACKAGING_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "printing", "active_code": "cleaning",
     "page_title": "인쇄 | 산업별 솔루션",
     "page_desc": "플렉소·옵셋·그라비어 인쇄기, 롤러, 잉크 트레이, 기어 조립체, 라미네이터와 라벨 인쇄 설비의 잉크·접착제·그리스 제거에 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": PRINTING_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "power-generation", "active_code": "cleaning",
     "page_title": "발전 · 전력 | 산업별 솔루션",
     "page_desc": "가스터빈·HRSG, 수력 발전기 권선, 원자력 제염, 보일러·증기터빈, 변전설비까지 발전 · 전력 설비에서 비전도성 건식 세척이 활용되는 방식을 설명합니다.",
     "body": POWER_GENERATION_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "oil-gas", "active_code": "cleaning",
     "page_title": "오일 · 가스 | 산업별 솔루션",
     "page_desc": "중질유·비투멘·카본 제거, 비파괴검사·재도장 전 표면 전처리, 열교환기·핀팬·HRSG·프랙펌프 라디에이터 세척까지 석유 · 가스 플랜트에서 드라이아이스 세척이 활용되는 방식을 설명합니다.",
     "body": OIL_GAS_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "mining", "active_code": "cleaning",
     "page_title": "광업 | 산업별 솔루션",
     "page_desc": "크러셔·컨베이어 등 채광·처리 설비, 덤프트럭·로더 운반 장비, E-하우스·변압기·제어반 전기설비까지 광업 현장에서 비전도성 건식 세척이 활용되는 방식을 설명합니다.",
     "body": MINING_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "textiles", "active_code": "cleaning",
     "page_title": "섬유 | 산업별 솔루션",
     "page_desc": "카딩·방적·제직 설비의 섬유 날림과 왁스, 와이어 롤러와 텐터 체인의 라텍스·접착제, 스텐터 오븐의 경화 수지까지 섬유 · 부직포 생산설비에서 건식 비마모 세척이 활용되는 방식을 설명합니다.",
     "body": TEXTILES_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "engineered-wood", "active_code": "cleaning",
     "page_title": "엔지니어드 우드 | 산업별 솔루션",
     "page_desc": "MDF·HDF·PB·OSB 프레스와 플레이트, 드라이어·환기 설비, 접착제 도포기, 합판 킬른 팬·롤러·베니어 설비까지 엔지니어드 우드 생산에서 열간 · 장착 상태 세척이 활용되는 방식을 설명합니다.",
     "body": ENGINEERED_WOOD_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "rail", "active_code": "cleaning",
     "page_title": "철도 · 대중교통 | 산업별 솔루션",
     "page_desc": "견인전동기·제어반·제3궤조 애자 등 추진·전기계통, 역사·선로 인프라, 대차·차축·디젤 엔진, 도장부스까지 철도 · 대중교통 정비에서 플래시 러스트 없는 비전도성 세척이 활용되는 방식을 설명합니다.",
     "body": RAIL_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "mold-tool-cleaning", "active_code": "cleaning",
     "page_title": "금형 · 툴링 세척 | 작업별 솔루션",
     "page_desc": "사출금형, 고무·타이어 금형, 복합재 툴링, 다이캐스팅 금형과 코어박스 — 이형제·수지·오프가스·카본 등 축적된 오염물을 금형의 표면과 형상을 고려하며 제거하는 드라이아이스 금형 세척.",
     "body": MOLD_TOOL_CLEANING_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "contract-cleaning", "active_code": "cleaning",
     "page_title": "전문 세척 서비스 | 산업별 솔루션",
     "page_desc": "생산설비, 식품·인쇄·포장설비, 발전·중공업 설비에서 복원 현장까지 — 서로 다른 고객 현장의 오염물에 대응하는 전문 세척업체를 위한 드라이아이스 세척 안내입니다.",
     "body": CONTRACT_CLEANING_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "facility-maintenance", "active_code": "cleaning",
     "page_title": "생산설비 · 시설 유지보수 | 산업별 솔루션",
     "page_desc": "컨베이어·로봇·모터·제어반·냉각설비·배관·물류장비까지 — 거의 모든 제조현장에 공통으로 존재하는 생산설비와 공장 인프라의 유지보수 세척에 드라이아이스 세척을 활용하는 방법을 설명합니다.",
     "body": FACILITY_MAINTENANCE_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "restoration", "active_code": "cleaning",
     "page_title": "화재 · 수해 복원 | 산업별 솔루션",
     "page_desc": "화재 이후 목재·구조물에 남은 그을음·탄화물·연기 잔류물과 수해 이후 표면 오염물을 물을 더하지 않고 제거하는 드라이아이스 복원 세척을 설명합니다.",
     "body": RESTORATION_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "mold-remediation", "active_code": "cleaning",
     "page_title": "곰팡이 제거 | 산업별 솔루션",
     "page_desc": "다락·크롤스페이스·목재 빔 등 구조재 표면의 곰팡이 오염을 물을 더하지 않고 물리적으로 제거하는 드라이아이스 세척과, 함께 고려해야 할 수분 관리·복원 절차를 설명합니다.",
     "body": MOLD_REMEDIATION_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "historical-restoration", "active_code": "cleaning",
     "page_title": "역사적 건축물 · 문화재 복원 | 산업별 솔루션",
     "page_desc": "기념물·역사적 건축물·목재 구조·산업 유산·박물관 유물의 표면 오염물을 원래 표면과 파티나를 고려하면서 제거하는 드라이아이스 복원 세척과, 사전 테스트의 중요성을 설명합니다.",
     "body": HISTORICAL_RESTORATION_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "industries", "slug": "automotive-detailing", "active_code": "cleaning",
     "page_title": "자동차 복원 · 디테일링 | 산업별 솔루션",
     "page_desc": "언더바디·엔진룸·휠하우스·클래식카 프레임의 오일·도로 오염물·방청 왁스를 제거하면서 공장 도장과 검사 표시 등 차량의 원래 디테일을 보존하는 드라이아이스 복원·디테일링을 설명합니다.",
     "body": AUTOMOTIVE_DETAILING_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "weld-fixture-robot", "active_code": "cleaning",
     "page_title": "용접라인 · 지그 · 로봇 세척 | 작업별 솔루션",
     "page_desc": "용접 픽스처, 지그, 용접 로봇에 반복적으로 쌓이는 스패터와 슬래그, 그을음을 정렬 상태와 센서·배선을 고려하며 제거하는 드라이아이스 용접라인 세척.",
     "body": WELD_FIXTURE_ROBOT_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "paint-booth-coating-line", "active_code": "cleaning",
     "page_title": "도장부스 · 코팅라인 세척 | 작업별 솔루션",
     "page_desc": "도장부스 그레이팅, 스키드, 행거와 도장 로봇에 쌓이는 오버스프레이·프라이머 잔류물을 설비 형상과 센서·배선을 고려하며 제거하는 드라이아이스 세척.",
     "body": PAINT_BOOTH_COATING_LINE_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "electrical-electronic", "active_code": "cleaning",
     "page_title": "전기 · 전자 장비 세척 | 작업별 솔루션",
     "page_desc": "전동기·배전반·제어반 같은 산업용 전기설비와 PCB·커넥터 같은 정밀 전자부품의 먼지·오일·카본 트래킹·플럭스 잔류물을 절연 상태와 안전조건을 고려하며 제거하는 드라이아이스 세척.",
     "body": ELECTRICAL_ELECTRONIC_BODY, "extra_script": AUTOMOTIVE_SCRIPT},

    {"dir": "applications", "slug": "adhesive-resin-removal", "active_code": "cleaning",
     "page_title": "접착제 · 수지 제거 | 작업별 솔루션",
     "page_desc": "글루건·라벨링헤드·롤러·접합지그에 쌓이는 핫멜트·PSA·에폭시·우레탄·실리콘 잔류물을 화학용제 사용을 줄이며 정밀 표면을 고려해 제거하는 드라이아이스 세척.",
     "body": ADHESIVE_RESIN_REMOVAL_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "ink-paint-coating-removal", "active_code": "cleaning",
     "page_title": "잉크 · 도료 · 코팅 제거 | 작업별 솔루션",
     "page_desc": "인쇄 실린더·롤러의 잉크·바니시, 도장 지그·컨베이어의 오버스프레이·코팅 부산물을 정밀 표면을 고려해 제거하는 드라이아이스 세척. 산업용 도막 전체 박리는 별도 공정.",
     "body": INK_PAINT_COATING_REMOVAL_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "oil-grease-residue-removal", "active_code": "cleaning",
     "page_title": "오일 · 그리스 · 고착 오염 제거 | 작업별 솔루션",
     "page_desc": "기어·베어링·기계프레임·중장비·철도설비에 두껍게 축적된 오일·그리스·타르성 잔류물을 분해 없이 현장에서 제거하는 드라이아이스 세척.",
     "body": OIL_GREASE_RESIDUE_REMOVAL_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "rust-corrosion-removal", "active_code": "cleaning",
     "page_title": "녹 · 부식 · 산화물 제거 | 작업별 솔루션",
     "page_desc": "표면 녹과 초기 산화물을 원래 표면 상태를 고려하며 제거하는 드라이아이스 세척. 깊은 피팅 부식이나 재도장용 표면 프로파일이 필요한 작업과의 범위 구분을 명확히 설명.",
     "body": RUST_CORROSION_REMOVAL_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "surface-preparation", "active_code": "cleaning",
     "page_title": "표면 전처리 | 작업별 솔루션",
     "page_desc": "도장·코팅·접착·실링 전 이형제·오일·먼지·지문 등 표면 오염물을 제거하는 드라이아이스 표면 전처리. 재도장용 표면 프로파일 형성과는 다른 청정도 확보 목적임을 명시.",
     "body": SURFACE_PREPARATION_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
    {"dir": "applications", "slug": "deburring-deflashing", "active_code": "cleaning",
     "page_title": "디버링 · 디플래싱 | 작업별 솔루션",
     "page_desc": "사출성형 부품의 파팅라인·게이트 플래시와 가공부품의 버를 형상·공차 변화를 최소화하며 제거하는 드라이아이스 부품 마무리(Parts Finishing) 공정.",
     "body": DEBURRING_DEFLASHING_BODY, "extra_script": AUTOMOTIVE_SCRIPT},
]


def build_detail_pages():
    n = 0
    for d in DETAIL_PAGES:
        os.makedirs(os.path.join(ROOT, d["dir"]), exist_ok=True)
        html = page_shell(d["page_title"], d["page_desc"], 1, d["active_code"], d["body"],
                          extra_script=d.get("extra_script", ""))
        with open(os.path.join(ROOT, d["dir"], f"{d['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        n += 1
    return n


def main():
    for m in MENU:
        os.makedirs(os.path.join(ROOT, m["code"]), exist_ok=True)
        build_hub_page(m)
        for s in m["subs"]:
            if s.get("is_group"):
                continue  # 제품 그룹(블라스터/펠렛타이저)은 products.py가 별도 생성
            build_sub_page(m, s)
    build_home()
    n_detail = build_detail_pages()

    import products
    n_blaster = products.build_blaster(ROOT, nav_html, footer_html, page_shell, asset)
    n_pelletizer = products.build_pelletizer(ROOT, nav_html, footer_html, page_shell, asset)
    n_recovery = products.build_recovery(ROOT, nav_html, footer_html, page_shell, asset)

    total = sum(len(m["subs"]) for m in MENU if True) - 3  # blaster/pelletizer/recovery는 is_group이라 별도 카운트
    total_pages = 1 + len(MENU) + total + n_blaster + n_pelletizer + n_recovery + n_detail
    print(f"생성 완료: 홈 1개 + 허브 {len(MENU)}개 + 서브페이지 {total}개 "
          f"+ 블라스터 {n_blaster}개 + 펠렛타이저 {n_pelletizer}개 + CO2 리커버리 {n_recovery}개 "
          f"+ 산업 상세 {n_detail}개 "
          f"= 총 {total_pages}개")


if __name__ == "__main__":
    main()
