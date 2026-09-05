document.addEventListener("DOMContentLoaded", function () {
  // (참고) "함께 보면 좋은 페이지" 카드는 이제 순수 CSS 호버(이미지 확대 +
  // 카드 리프트 + 링크 슬라이드업)로만 동작 — 별도 JS 불필요.
  // 푸터 리빌 블러: 푸터(.site-footer)가 화면 아래에서 올라와 고정 화면
  // (.last-freeze)을 덮는 비율(0~1)에 맞춰 --freeze-blur를 0~10px로 갱신.
  // 히어로 이미지의 스크롤 블러(SUBHERO_BLUR_MAX)와 같은 감도.
  var freezeEl = document.querySelector(".last-freeze");
  var revealFooter = document.querySelector(".site-footer");
  if (freezeEl && revealFooter) {
    var FREEZE_BLUR_MAX = 10;
    var freezeTick = false;
    var updateFreezeBlur = function () {
      freezeTick = false;
      var vh = window.innerHeight || 1;
      var top = revealFooter.getBoundingClientRect().top;
      var covered = Math.min(1, Math.max(0, (vh - top) / vh));
      // (2026-09-05) 푸터 상단 경계가 화면 중간(covered 0.5)에 올 때까지는
      // 블러 없이 두고, 그 지점부터 완전히 덮이는 순간(1)까지 0→최대로 증가.
      var blurT = Math.min(1, Math.max(0, (covered - 0.5) / 0.5));
      freezeEl.style.setProperty("--freeze-blur", (blurT * FREEZE_BLUR_MAX).toFixed(2) + "px");
    };
    window.addEventListener("scroll", function () {
      if (!freezeTick) { freezeTick = true; requestAnimationFrame(updateFreezeBlur); }
    }, { passive: true });
    window.addEventListener("resize", updateFreezeBlur);
    updateFreezeBlur();
  }
  // FAQ 아코디언 슬라이드: 기본 <details> 토글을 가로채 .faq-a 높이를 애니메이션.
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var summary = item.querySelector("summary");
    var panel = item.querySelector(".faq-a");
    if (!summary || !panel) return;
    var animating = false;
    if (item.hasAttribute("open")) { item.classList.add("is-open"); panel.style.height = "auto"; }
    summary.addEventListener("click", function (e) {
      e.preventDefault();
      if (animating) return;
      animating = true;
      if (item.hasAttribute("open")) {
        panel.style.height = panel.scrollHeight + "px";
        item.classList.remove("is-open");
        requestAnimationFrame(function () { panel.style.height = "0px"; });
        panel.addEventListener("transitionend", function done(ev) {
          if (ev.propertyName !== "height") return;
          panel.removeEventListener("transitionend", done);
          item.removeAttribute("open"); animating = false;
        });
      } else {
        item.setAttribute("open", "");
        item.classList.add("is-open");
        panel.style.height = "0px";
        requestAnimationFrame(function () { panel.style.height = panel.scrollHeight + "px"; });
        panel.addEventListener("transitionend", function done(ev) {
          if (ev.propertyName !== "height") return;
          panel.removeEventListener("transitionend", done);
          panel.style.height = "auto"; animating = false;
        });
      }
    });
  });

  // preload="none" 자동재생 영상: 뷰포트에 들어올 때만 로드·재생, 벗어나면 정지
  // (모바일 데이터·초기 로딩 부담 최소화).
  var lazyVideos = document.querySelectorAll('video[preload="none"][autoplay]');
  if (lazyVideos.length && "IntersectionObserver" in window) {
    var vidObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) {
          if (v.preload === "none") { v.preload = "auto"; v.load(); }
          v.play().catch(function () {});
        } else {
          v.pause();
        }
      });
    }, { rootMargin: "200px 0px" });
    lazyVideos.forEach(function (v) { vidObs.observe(v); });
  }

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
  }
  // 모바일에서 대메뉴 탭 시 서브메뉴 펼치기
  document.querySelectorAll(".main-nav > ul > li > a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      var li = a.parentElement;
      if (li.querySelector(".megamenu") && window.innerWidth <= 960) {
        e.preventDefault();
        li.classList.toggle("open");
      }
    });
  });

  var prefersReducedMotion =
    window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // (후속56) 전체 페이지 스크롤을 부드럽게 — 참고 사이트(biofarma.com.ar)처럼
  // 마우스 휠/트랙패드로 스크롤할 때 즉시 뚝뚝 끊기지 않고 관성이 붙은 듯
  // 부드럽게 미끄러지도록 함. Lenis 같은 라이브러리를 CDN으로 불러올 수 없는
  // 환경(네트워크 제약)이라, 아래 "OUR HISTORY" 구간에서 이미 쓰던 것과 같은
  // 방식(휠 입력을 가로채 목표 스크롤 위치를 만들고, 매 프레임 현재 위치를
  // 목표값 쪽으로 일정 비율씩만 좁혀가는 lerp 감쇠)을 페이지 전체 스크롤에
  // 직접 적용해 자체 구현함.
  // - 데스크톱(마우스 휠·트랙패드, pointer:fine)에서만 동작 — 터치 기기는
  //   OS 자체의 관성 스크롤이 이미 부드러워서 손대지 않음(더블 스무딩 방지).
  // - prefers-reduced-motion이면 아예 켜지 않음(기존 다른 연출들과 동일 원칙).
  // - 모바일 메뉴(.main-nav)처럼 자체 스크롤이 있는 요소 위에서 휠을 돌릴 땐
  //   페이지 스크롤을 가로채지 않고 그 요소가 정상적으로 스크롤되게 비켜줌.
  // - 트랙패드로 좌우 스와이프(브라우저 뒤로/앞으로 가기 제스처)할 때는
  //   막지 않도록, 세로 이동이 가로 이동보다 뚜렷할 때만 관여함.
  // - 키보드(Page Up/Down, 방향키, Home/End)나 스크롤바 드래그, 앵커 링크
  //   이동처럼 휠이 아닌 다른 방식으로 스크롤이 바뀌면 목표값을 그 위치로
  //   즉시 재동기화해 다음 휠 입력이 엉뚱한 지점부터 이어지지 않게 함.
  var supportsFinePointer =
    window.matchMedia && window.matchMedia("(pointer: fine)").matches;
  if (supportsFinePointer && !prefersReducedMotion) {
    var smoothCurrent = window.scrollY;
    var smoothTarget = window.scrollY;
    var SMOOTH_EASE = 0.09;
    var smoothRaf = null;
    // (2026-09-02, 후속N) 체크포인트 점프의 감속률 — 기본은 SMOOTH_EASE와
    // 같지만, 아래 hsAnimateTo()가 매 점프 시작 시 "이동 거리"를 보고 이
    // 값을 필요할 때만 낮춘다(smoothScrollLoop는 이 값을 매 프레임 읽음).
    var currentEase = SMOOTH_EASE;

    // CSS의 scroll-behavior:smooth(html 요소, 앵커 이동용)가 켜져 있으면
    // 아래에서 매 프레임 호출하는 window.scrollTo()마다 브라우저가 자체
    // 스무스 애니메이션을 새로 걸어버려 우리 lerp 계산과 이중으로 부딪히며
    // 스크롤이 중간에 멈춰버리는 문제가 있었음 — 이 부드러운 휠 스크롤을
    // 켤 때는 인라인 스타일로 scroll-behavior를 auto로 덮어써 브라우저의
    // 자체 스무딩을 끄고, 우리 rAF 루프가 매 프레임 즉시 위치를 지정하도록 함.
    document.documentElement.style.scrollBehavior = "auto";

    var getMaxScroll = function () {
      return Math.max(
        0,
        document.documentElement.scrollHeight - window.innerHeight
      );
    };

    // (2026-09-02, 후속16/18) 사용자 요청 — 인덱스 페이지 한정, 맨 위(히어로)
    // 부터 "필요한 메뉴를 선택해보세요"(메뉴 선택 섹션)가 보이는 지점까지는
    // 위 자유 누적 스크롤 대신 "휠 한 번(제스처) = 다음/이전 체크포인트로
    // 정확히 이동"하도록 함. 체크포인트 순서:
    //   [0] 맨 위
    //   [1] "우리가 하는 일" 제목 상단 틀고정
    //   [2]~[6] 5개 탭(드라이아이스 블라스터/제조기·리커버리/자동화 시스템/
    //           드라이아이스 생산·공급/렌탈·데모 서비스)이 하나씩 위 탭
    //           자리로 날아가 붙는 순간들 — [6]에서 5개 탭이 전부 붙지만
    //           아직 갤러리(이미지 5장)는 나오지 않는다(후속18 버그수정,
    //           위 stackdoZones 주석 참고)
    //   [7] 갤러리(이미지 5장) 등장
    //   [8] "우리의 가치" 제목 상단 틀고정(첫 카드 "업계 최초"가 이 지점에서
    //       이미 포커스 라인 안에 들어와 함께 보임 — 실측 확인, 별도
    //       체크포인트 아님)
    //   [9]~[11] 나머지 가치 카드 3개(업계 최대/검증된 기술력/미디어 보도 및
    //            수상)가 하나씩 포커스(확대)되는 순간들 — 위
    //            applyValueFocus()의 "포커스 라인"(화면 세로 중앙) 공식을
    //            그대로 재사용해 각 카드 중심이 그 라인에 오는 위치를 계산
    //   [12] "우리의 신념" 제목 상단 틀고정
    //   [13] "우리의 신념" 텍스트 박스(제목/부제/로고) 등장
    //   [14] "우리는.. 실현합니다" 문장 등장
    //   [15] "우리는 '콜드젯 팀'입니다" 제목 상단 틀고정
    //   [16] VATEK×Cold Jet 로고 등장
    //   [17] "필요한 메뉴를 선택해보세요"(메뉴 선택 섹션) 도착 — 자동
    //        스크롤은 여기까지, 그 아래(푸터 등)는 이 기능의 대상이 아니므로
    //        마지막 체크포인트를 벗어나는 즉시 아래 원래의 자유 누적
    //        스크롤로 자연스럽게 넘어간다.
    // "처음엔 빠르게, 갈수록 느려지다 딱 멈추는" 감속 요청은 새 애니메이션을
    // 따로 만들지 않고 위 smoothScrollLoop의 lerp(SMOOTH_EASE) 감쇠를 그대로
    // 재사용 — smoothTarget을 체크포인트 값으로 지정하기만 하면 기존과 동일한
    // 감속으로 도착한다. 체크포인트 위치는 레이아웃(뷰포트 높이 등)에 따라
    // 달라질 수 있어 캐시하지 않고, 실제로 필요한 그 순간(휠 제스처 시작 시)
    // 마다 새로 계산해 항상 최신 상태를 보장한다. 각 구간의 실제 시각적
    // 상태(틀고정/포커스/등장 등)는 이 체크포인트 계산과 무관하게 이미 매
    // 프레임 scrollY를 기준으로 동작하는 기존 로직(updateStackdo/
    // applyValueFocus 등)이 그대로 담당 — 여기서는 그 로직들이 쓰는 것과
    // 동일한 공식으로 "그 상태가 시작되는 스크롤 위치"만 미리 계산해 그
    // 지점으로 점프시킬 뿐이다.
    // 실측 위치 그대로 목표로 삼으면, 지금 당장은 아직 화면에 들어오지 않은
    // (이미지 lazy-load 전이거나 그 사이 다른 요소의 실측이 살짝 달라질 수
    // 있는) 아래쪽 지점일수록 도착했을 때 레이아웃이 미세하게 달라져 있어
    // "정확히 그 스크롤 위치"가 요구하는 임계값(예: rect.top<=0)을 겨우
    // 못 넘는 경우가 실측 결과 확인됨(예: 콜드젯 제목 — 계산 시점엔
    // 11261.375였는데 도착해보니 rect.top이 0.375로 0을 살짝 못 넘겨
    // is-pinned가 안 켜짐). 사람 눈에는 안 보이는 수 px를 더 보태 항상
    // 임계값을 확실히 넘도록 함.
    var HS_EPS = 2;
    // (2026-09-02, 후속18) 뒤로(위로) 스크롤할 때 체크포인트가 어긋나는 문제
    // 발견 — "우리의 가치"/"우리의 신념"/"콜드젯 팀" 제목처럼 자기 자신이
    // position:sticky인 요소는, 한 번 상단에 틀고정된 뒤에는 아무리 더
    // 스크롤해도 getBoundingClientRect().top이 0 부근에 계속 머무른다(브라우저의
    // sticky 동작 자체가 그럼). 그래서 이미 그 지점을 지나친 뒤에(즉 아래쪽
    // 체크포인트에서 위쪽 체크포인트로 되돌아가려 할 때) 이 요소의 위치를
    // 다시 재는 순간 "진짜 원래 위치"가 아니라 "지금 화면에 고정된
    // scrollY 근처 값"이 나와버려, 위로 갈수록 목표 지점이 자꾸 지금
    // 위치 바로 근처로 다시 계산되는 문제가 있었음(실측으로 확인). 아직
    // 고정되지 않아(rect.top이 뚜렷하게 양수) 값이 신뢰할 수 있을 때마다
    // 그 값을 캐시해두고, 이미 고정되어 못 미더울 때는 그 캐시값을 대신
    // 쓰는 방식으로 해결 — 페이지에 처음 들어와 위에서부터 훑어 내려오는
    // 동안 자연히 한 번은 신뢰할 수 있는 값이 캐시되므로 별도 준비 없이도
    // 항상 정확한 값을 쓸 수 있다.
    var hsStableTop = {};
    var stableDocTopOf = function (el, key) {
      var rect = el.getBoundingClientRect();
      if (rect.top > 1) {
        hsStableTop[key] = rect.top + window.scrollY;
      }
      return hsStableTop[key] !== undefined
        ? hsStableTop[key]
        : rect.top + window.scrollY;
    };
    window.addEventListener("resize", function () {
      hsStableTop = {};
    });
    // (2026-09-02, 후속N) 사용자 요청 — "우리가 하는 일/우리의 가치/우리의
    // 신념" 제목이 화면 하단에서 크게 나타났다가 줄어들며 상단에 박히는
    // 연출(applyTitleShrinkZoom)이 방문자가 제목을 미처 인지하기도 전에
    // 너무 빨리 끝나버림 — 이 연출은 순전히 스크롤 위치로 구동되므로(시간
    // 기반 애니메이션이 아님), 그 스크롤을 만드는 체크포인트 점프 자체를
    // 아래 hsAnimateTo()에서 더 천천히 흐르게 해야 실제로 더 오래 보인다.
    // computeHeroStepCheckpoints()가 실행될 때마다, "그 체크포인트에 도착하는
    // 순간 = 제목이 막 다 줄어들어 박히는 순간"인 인덱스들을 여기에 채워둔다.
    var hsTitleDockIndices = [];
    var computeHeroStepCheckpoints = function () {
      var vh = window.innerHeight || document.documentElement.clientHeight;
      var docTopOf = function (el) {
        return el.getBoundingClientRect().top + window.scrollY;
      };

      var stackdoScrollEl = document.querySelector(".stackdo-scroll");
      var valuePinTitleEl = document.querySelector(".value-pin-title");
      var panelCount = document.querySelectorAll(".stackdo-panel").length;
      if (!stackdoScrollEl || !valuePinTitleEl || !panelCount) return null;

      var stackdoTop = docTopOf(stackdoScrollEl);
      var stackdoTotal =
        stackdoScrollEl.getBoundingClientRect().height - vh;
      // main.js의 updateStackdo() stackdoZones와 반드시 같은 값이어야 함
      // (후속18 — panelCount+1이 아니라 +2, 위 stackdoZones 주석 참고).
      var zones = panelCount + 2;
      var stackdoZoneW = stackdoTotal / zones;
      var points = [0, stackdoTop + HS_EPS];
      hsTitleDockIndices = [1]; // "우리가 하는 일" 제목 박힘 = 이 시점의 인덱스
      // (2026-09-02, 후속19) 사용자 피드백 — 탭(드라이아이스 블라스터 등)이
      // "스크롤이 멎고 난 뒤 시차를 두고" 위로 날아가 붙는 것처럼 보임. 실은
      // 탭 전환은 updateStackdo()가 각 구간의 시작 경계에서 idx가 바뀌는
      // 순간 CSS 전환(.stackdo-panel-head, transform .5s)을 트리거하는데,
      // 지금까지는 체크포인트를 그 "구간이 막 시작되는 지점"에 그대로 뒀기
      // 때문에 이 스크롤 애니메이션이 목적지에 거의 다 도착해서야 비로소
      // 전환이 시작돼, 도착 후에도 한참 더 움직이는 것처럼 보였음. 체크포인트
      // 목적지를 그 구간의 "시작"이 아니라 "안쪽 깊숙한 지점"(HS_LEAD)으로
      // 당겨두면, 실제 경계를 넘는 순간(=이번 스크롤 애니메이션의 초반부)
      // 곧바로 전환이 시작되고, 애니메이션이 목적지까지 감속하며 계속
      // 진행되는 동안 그 0.5s짜리 전환도 함께 재생돼 "스크롤과 동시에"
      // 움직이는 것처럼 보임(다음 구간 경계를 넘지 않도록 1 미만으로 유지해
      // 상태 자체는 그대로 유지). 아래 신념/콜드젯 체크포인트에도 동일하게 적용.
      var HS_LEAD = 0.7;
      for (var i = 1; i <= zones - 1; i++) {
        points.push(stackdoTop + stackdoZoneW * (i + HS_LEAD) + HS_EPS);
      }
      // 우리의 가치 제목
      points.push(stableDocTopOf(valuePinTitleEl, "value") + HS_EPS);
      hsTitleDockIndices.push(points.length - 1);

      // 가치 카드 4개(업계 최초/업계 최대/검증된 기술력/미디어 보도 및 수상)
      // 중 첫 번째(업계 최초)는 제목이 틀고정되는 바로 그 지점에서 이미
      // 포커스 라인 안에 들어와 함께 보이므로(실측 확인) 별도 체크포인트가
      // 아니라 바로 위 "우리의 가치 제목" 체크포인트에 자연히 포함됨 —
      // 나머지 3개(업계 최대/검증된 기술력/미디어 보도 및 수상)만 각각의
      // 체크포인트로 추가. applyValueFocus()의 focusY(=vh*0.5) 공식과
      // 동일하게, 각 카드의 세로 중심이 그 라인에 오는 스크롤 위치를 계산.
      var valueBlocks = document.querySelectorAll(".value-block");
      var focusY = vh * 0.5;
      for (var vb = 1; vb < valueBlocks.length; vb++) {
        var blockRect = valueBlocks[vb].getBoundingClientRect();
        var blockDocTop = blockRect.top + window.scrollY;
        points.push(blockDocTop + blockRect.height / 2 - focusY + HS_EPS);
      }

      // 우리의 신념 — 제목 틀고정 → applyValueFocus()의 beliefBoxTotalPx(3
      // 구간, 구간당 0.65vh)와 동일한 공식으로 텍스트 박스/문장 등장 지점 계산.
      var beliefPinTitleEl = document.querySelector(".belief-pin-title");
      var beliefVideoScrollEl = document.querySelector(".belief-video-scroll");
      if (beliefPinTitleEl) {
        points.push(stableDocTopOf(beliefPinTitleEl, "belief") + HS_EPS);
        hsTitleDockIndices.push(points.length - 1);
      }
      if (beliefVideoScrollEl) {
        var beliefTop = docTopOf(beliefVideoScrollEl);
        var beliefZoneW = 0.65 * vh;
        // 위 stackdoZoneW 루프와 같은 이유(HS_LEAD) — 박스(.75s)/문장(.8s)
        // 전환이 스크롤과 함께 진행되도록 각 구간 안쪽으로 당김.
        points.push(beliefTop + beliefZoneW * (1 + HS_LEAD) + HS_EPS); // 텍스트 박스(제목/부제/로고) 등장
        points.push(beliefTop + beliefZoneW * (2 + HS_LEAD) + HS_EPS); // "우리는.. 실현합니다" 등장
      }

      // 우리는 콜드젯 팀입니다 — 제목이 틀고정되는 순간 영상(.coldjet-video-wrap,
      // opacity/transform .7s)과 박스(.coldjet-video-box, is-risen)도 함께
      // 틀고정/등장하는데, 이 역시 위와 같은 이유로 "제목 체크포인트"를 그
      // 트리거 지점 그대로 두면 영상이 멎은 뒤 뒤늦게 자리를 잡는 것처럼
      // 보임 — coldjetVideoScrollEl 기준 0구간(제목 고정~로고 등장 전) 안쪽
      // 깊숙한 지점으로 당겨, 영상의 0.7s 전환이 이 체크포인트로 이동하는
      // 스크롤 애니메이션과 함께 재생되도록 함(로고 체크포인트도 동일).
      var coldjetPinTitleEl = document.querySelector(".coldjet-pin-title");
      var coldjetVideoScrollEl = document.querySelector(".coldjet-video-scroll");
      if (coldjetVideoScrollEl) {
        var coldjetTop = docTopOf(coldjetVideoScrollEl);
        var coldjetZoneW = 0.65 * vh;
        // (2026-09-05) 제목 도킹 체크포인트를 정확히 "제목이 상단에 닿는 지점"
        // 으로 — 기존처럼 구간 안쪽(HS_LEAD)으로 당겨두면 감속(lerp)의 느린
        // 꼬리 구간이 제목 축소 연출이 아니라 그 뒤 여백에 쓰여, 다른 세
        // 제목(~3초)보다 훨씬 빨리(~0.7초) 박혔음. 영상은 is-pinned 전환(.7s)
        // 으로 도착 직후 자연스럽게 나타난다.
        points.push(
          coldjetPinTitleEl
            ? stableDocTopOf(coldjetPinTitleEl, "coldjet") + HS_EPS
            : coldjetTop + HS_EPS
        ); // 제목 틀고정 + 영상 등장
        // (2026-09-02, 후속N+1) "우리는 콜드젯 팀입니다" 제목도 다른 3개
        // 제목(우리가 하는 일/우리의 가치/우리의 신념)과 똑같이 여기서
        // applyTitleShrinkZoom()이 완료되므로, 동일하게 title-dock 인덱스로
        // 등록해야 hsAnimateTo()가 같은 속도로 늦춰준다.
        hsTitleDockIndices.push(points.length - 1);
        points.push(coldjetTop + coldjetZoneW * (1 + HS_LEAD) + HS_EPS); // VATEK×Cold Jet 로고 등장
      } else if (coldjetPinTitleEl) {
        // (대비책) coldjetVideoScrollEl을 못 찾을 때만 예전 방식으로 대체
        points.push(stableDocTopOf(coldjetPinTitleEl, "coldjet") + HS_EPS);
        hsTitleDockIndices.push(points.length - 1);
      }

      // 필요한 메뉴를 선택해보세요 — 자동 스크롤의 마지막 지점
      var menuPickerEl = document.querySelector(".section-menu-picker");
      if (menuPickerEl) points.push(docTopOf(menuPickerEl) + HS_EPS);

      return points;
    };
    var nearestHeroStepIndex = function (points, y) {
      var bestI = 0;
      var bestDist = Infinity;
      for (var i = 0; i < points.length; i++) {
        var d = Math.abs(points[i] - y);
        if (d < bestDist) {
          bestDist = d;
          bestI = i;
        }
      }
      return bestI;
    };
    // (2026-09-02, 후속17/18) 사용자 요청 반영:
    // 1) 체크포인트로 이동(감속)하는 도중에 또 스크롤(드르르륵)하면, 그 애니메이션을
    //    무시하지 않고 "다음" 체크포인트로 이어서 이동(연속 동작 허용). 이를 위해
    //    지금 향하고 있는(또는 막 도착한) 체크포인트 인덱스를 추적해두고, 다음
    //    제스처가 오면 실제 스크롤 위치가 아니라 이 추적값을 기준으로 다음 칸을
    //    계산한다 — 애니메이션이 끝나기 전이라 실제 위치가 아직 목표에 못 미친
    //    상태여도 정확히 한 칸씩 더 이어갈 수 있도록.
    // 2) 델타값이 작은 "느린" 휠 입력(트랙패드/휠을 아주 천천히 미는 등)에는 이
    //    체크포인트 이동 방식을 아예 적용하지 않고 아래 기존의 자유 누적 스크롤로
    //    흘려보낸다.
    // 3) (후속18) 실제 마우스 휠을 한 번 "드르르륵" 돌리면 브라우저는 그 한 번의
    //    물리적 동작을 짧은 시간 안에 여러 개의 개별 wheel 이벤트로 잘게 쪼개어
    //    보낸다 — 이걸 그대로 "이벤트 하나 = 체크포인트 한 칸"으로 처리하면 한 번
    //    돌렸을 뿐인데 여러 칸이 순식간에 넘어가 버림. 그래서 "빠른" 이벤트들을
    //    시간 간격으로 묶어(제스처) 한 번의 물리적 동작 안에서는 맨 처음 이벤트만
    //    한 칸 이동을 트리거하고, 같은 동작이 이어지는 동안 오는 나머지 이벤트는
    //    (기본 스크롤만 막고) 무시한다. 이후 충분한 공백(HS_GESTURE_GAP_MS 이상)
    //    없이 오던 이벤트가 끊기고 — 즉 실제로 휠을 멈췄다가 — 다시 오면 그건 새
    //    동작으로 보고 한 칸 더 이동한다. 이렇게 하면 "드르르륵" 한 번 = 한 동작,
    //    "드르륵드르륵" 두 번(사이에 손을 뗀 공백이 있으면) = 두 동작이 된다.
    var hsTargetIndex = null;
    var HS_FAST_THRESHOLD = 32;
    var HS_GESTURE_GAP_MS = 180;
    var hsLastFastEventTime = -Infinity;

    // (2026-09-02, 후속N) "스크롤이 움직이는 동안에는 SCROLL DOWN 힌트가 안
    // 보이게" — 이 rAF 루프가 실제로 목표값을 향해 움직이고 있는 프레임에서만
    // <html>에 is-scrolling을 붙이고, 다 도착해 멈추는 즉시 뗀다. 각 힌트
    // 요소는 style.css의 html.is-scrolling .autoscroll-hint 규칙으로 이
    // 클래스가 붙어 있는 동안만 자기 자신의 opacity/애니메이션 상태와 무관하게
    // 강제로 숨겨진다.
    var hsScrolling = false;
    var setHsScrolling = function (v) {
      if (hsScrolling === v) return;
      hsScrolling = v;
      document.documentElement.classList.toggle("is-scrolling", v);
    };

    var smoothScrollLoop = function () {
      var diff = smoothTarget - smoothCurrent;
      if (Math.abs(diff) < 0.5) {
        smoothCurrent = smoothTarget;
      } else {
        smoothCurrent += diff * currentEase;
      }
      window.scrollTo(0, smoothCurrent);
      if (smoothCurrent !== smoothTarget) {
        setHsScrolling(true);
        smoothRaf = window.requestAnimationFrame(smoothScrollLoop);
      } else {
        smoothRaf = null;
        setHsScrolling(false);
      }
    };

    // (2026-09-02, 후속N) 사용자 요청 — "우리는..실현합니다"에서 "우리는
    // 콜드젯팀입니다"로 넘어갈 때만 유독 너무 순식간에(빠르게) 전환됨.
    // 원인: 두 체크포인트 사이 실제 이동 거리가 다른 구간들(대부분
    // 550~1200px)보다 훨씬 커서(신념→콜드젯 섹션 전환용 여유 1.0vh가 이
    // 한 번의 점프에 통째로 포함됨, 약 1800px 이상) — lerp 감쇠율
    // (SMOOTH_EASE)은 거리와 무관하게 항상 같은 "비율"만큼 남은 거리를
    // 좁혀가므로, 거리가 클수록 화면이 움직이는 절대 속도(px/프레임)도 그만큼
    // 커져 "휙" 하고 순간이동하는 것처럼 보인다.
    // 해결: 체크포인트로 점프를 시작하는 이 순간(=아직 smoothCurrent가 실제
    // 현재 위치일 때) 이동해야 할 거리를 미리 재서, 그 거리가 크면
    // currentEase를 낮춰(느리게) 첫 프레임의 이동 속도가 HS_JUMP_MAX_STEP(px)를
    // 넘지 않도록 한다 — 짧은 구간(대부분의 체크포인트, ~1300px 이하)은 원래
    // 감쇠율(SMOOTH_EASE) 그대로라 기존에 이미 다듬어둔 체감 속도·전환
    // 타이밍(HS_LEAD 등)이 전혀 바뀌지 않고, 유독 먼 이 구간만 더 느리고
    // 부드럽게 흐르도록 자동으로 낮아진다.
    var HS_JUMP_MAX_STEP = 90;
    // (2026-09-02, 후속N) 사용자 요청 — "우리가 하는 일/우리의 가치/우리의
    // 신념" 제목이 확대→축소되며 상단에 박히는 연출이 너무 빨리 끝나 미처
    // 인지하기 전에 지나가버림. 위 HS_JUMP_MAX_STEP과 같은 원리지만, 이
    // 연출은 순전히 이 점프의 스크롤 진행에 얹혀 재생되므로 일반적인
    // "거리가 큰 구간만 완화" 기준보다 더 낮은 상한을 둬 도착 인덱스가 위
    // hsTitleDockIndices에 있을 때만 한 번 더 느리게 만든다.
    var HS_TITLE_DOCK_MAX_STEP = 45;
    // (2026-09-05) 사용자 요청 — "우리의 신념" 제목 도킹이 "우리는 콜드젯
    // 팀입니다"보다 눈에 띄게 느림. 원인: 두 점프 모두 첫 프레임 이동량을
    // HS_TITLE_DOCK_MAX_STEP으로 제한하는데, 신념 구간은 이동 거리가 콜드젯
    // 구간의 약 2배(.belief-list의 큰 margin-top 포함)라 같은 px/프레임으로
    // 두 배의 시간이 걸림. 거리 대신 "기준 거리"(콜드젯 구간과 비슷한 1200px)
    // 로 감쇠율을 정해, 제목 도킹은 거리와 무관하게 늘 같은 체감 속도가 되게 함.
    var HS_TITLE_DOCK_REF_DIST = 1200;
    var hsAnimateTo = function (targetY, targetIndex) {
      var dist = Math.abs(targetY - window.scrollY);
      var isTitleDock =
        targetIndex != null && hsTitleDockIndices.indexOf(targetIndex) !== -1;
      var maxStep = isTitleDock ? HS_TITLE_DOCK_MAX_STEP : HS_JUMP_MAX_STEP;
      var easeDist = isTitleDock ? Math.min(dist, HS_TITLE_DOCK_REF_DIST) : dist;
      currentEase = easeDist > 0 ? Math.min(SMOOTH_EASE, maxStep / easeDist) : SMOOTH_EASE;
      smoothCurrent = window.scrollY;
      smoothTarget = targetY;
      if (smoothRaf === null) {
        smoothRaf = window.requestAnimationFrame(smoothScrollLoop);
      }
    };

    window.addEventListener(
      "wheel",
      function (e) {
        // 자체 스크롤 영역(예: 모바일 메뉴) 위에서는 관여하지 않음
        if (e.target && e.target.closest && e.target.closest(".main-nav")) {
          return;
        }
        // (후속58) "우리의 능력" 전체화면 핀 안(.ability-item)은 스탯+하이라이트+
        // 고객사 마퀴가 늘어나면서 짧은 창 높이 등 예외 상황에 화면보다 콘텐츠가
        // 커질 수 있어 overflow-y:auto 안전장치를 뒀는데, 그 상태에서도 이 전역
        // 휠 핸들러가 항상 이벤트를 가로채 "페이지 스크롤"로만 처리해버리면
        // 넘친 내용을 마우스 휠로 볼 방법이 없어짐. 실제로 내부에 넘치는
        // 콘텐츠가 있을 때만(= 흔치 않은 예외 상황) 비켜주고, 평소(내용이 화면에
        // 다 들어가는 일반적인 경우)에는 그대로 부드러운 페이지 스크롤을 적용함.
        var abilityItem = e.target && e.target.closest && e.target.closest(".ability-item");
        if (abilityItem && abilityItem.scrollHeight > abilityItem.clientHeight + 1) {
          return;
        }
        // 가로 스와이프가 더 뚜렷하면(브라우저 뒤/앞으로 가기 제스처 등) 비켜줌
        if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) {
          return;
        }
        // (2026-09-02, 후속16/17) 위 hsTargetIndex 주석 참고 — 인덱스 페이지의
        // 히어로~"우리가 하는 일"~"우리의 가치" 제목 직전 구간에서는, "빠른"
        // 휠 제스처 한 번에 다음/이전 체크포인트로 이동(진행 중이어도 이어서
        // 다음 칸으로 계속 이동 가능). "느린" 스크롤은 아래 자유 누적 스크롤로
        // 흘려보낸다.
        var deltaY = e.deltaY;
        if (e.deltaMode === 1) {
          deltaY *= 16; // line → px 근사치
        } else if (e.deltaMode === 2) {
          deltaY *= window.innerHeight; // page → px
        }
        if (document.body.classList.contains("home")) {
          var hsPoints = computeHeroStepCheckpoints();
          var hsInZone =
            hsPoints &&
            (hsTargetIndex !== null ||
              window.scrollY <= hsPoints[hsPoints.length - 1] + 2);
          if (hsInZone && Math.abs(deltaY) >= HS_FAST_THRESHOLD) {
            var hsNow = performance.now();
            var hsIsNewGesture =
              hsNow - hsLastFastEventTime >= HS_GESTURE_GAP_MS;
            hsLastFastEventTime = hsNow;
            if (!hsIsNewGesture) {
              // 방금 시작된 같은 물리적 동작(드르르륵)의 후속 이벤트 —
              // 첫 이벤트에서 이미 한 칸 이동을 시작했으므로 추가로는
              // 반응하지 않되, 기본 스크롤은 계속 막아 어긋나지 않게 함.
              e.preventDefault();
              return;
            }
            var hsDir = deltaY > 0 ? 1 : deltaY < 0 ? -1 : 0;
            if (hsDir !== 0) {
              var hsBaseIndex =
                hsTargetIndex !== null
                  ? hsTargetIndex
                  : nearestHeroStepIndex(hsPoints, window.scrollY);
              var hsNext = hsBaseIndex + hsDir;
              if (hsNext >= 0 && hsNext < hsPoints.length) {
                e.preventDefault();
                hsAnimateTo(hsPoints[hsNext], hsNext);
                hsTargetIndex = hsNext;
                return;
              }
              // 맨 위에서 더 위로(hsNext<0) 또는 마지막 체크포인트에서 더
              // 아래로(hsNext>=length) — 이 기능의 대상 밖이므로 아래 기존
              // 자유 누적 스크롤로 자연스럽게 넘어간다.
              hsTargetIndex = null;
            }
          } else {
            // 느린 스크롤이거나 체크포인트 구간 밖 — 추적 상태를 비우고 아래
            // 자유 스크롤로 넘어간다(다음 빠른 스크롤에서는 실제 위치 기준으로
            // 다시 가장 가까운 체크포인트를 계산).
            hsTargetIndex = null;
          }
        }
        e.preventDefault();
        // (2026-09-02, 후속N) 체크포인트 점프가 아닌 일반 자유 스크롤은 항상
        // 기본 감쇠율 그대로 — 위 hsAnimateTo()가 직전 점프에서 낮춰뒀을 수
        // 있는 currentEase를 여기서 되돌려, 자유 스크롤 특유의 체감 속도가
        // 점프 이후에도 계속 유지되도록 한다.
        currentEase = SMOOTH_EASE;
        if (smoothRaf === null) {
          // 휠 입력이 새로 시작될 때, 그사이 다른 방식(키보드 등)으로
          // 위치가 바뀌었을 수 있으니 실제 현재 위치로 맞춰서 시작
          smoothCurrent = window.scrollY;
          smoothTarget = window.scrollY;
        }
        smoothTarget += deltaY;
        smoothTarget = Math.max(0, Math.min(smoothTarget, getMaxScroll()));
        if (smoothRaf === null) {
          smoothRaf = window.requestAnimationFrame(smoothScrollLoop);
        }
      },
      { passive: false }
    );

    // 키보드/스크롤바 드래그/앵커 링크 등 휠이 아닌 방식으로 스크롤이 바뀐
    // 경우, 우리 애니메이션이 돌고 있지 않을 때만 목표값을 그 위치로 재동기화
    // (2026-09-02, 후속N) 버그 수정 — 브라우저 스크롤바를 직접 드래그해
    // 위치를 옮기면(휠 이벤트가 전혀 발생하지 않으므로) hsTargetIndex가
    // 예전 위치의 값으로 그대로 남아있었음. 예를 들어 "우리의 신념" 근처까지
    // 스크롤한 뒤 스크롤바를 맨 위로 드래그해도 hsTargetIndex는 여전히 그때의
    // 인덱스를 가리키고 있어, 맨 위에서 마우스 휠을 "한 번"만 굴려도(다음
    // 체크포인트 계산의 기준을 실제 위치가 아니라 이 낡은 인덱스로 삼아버려)
    // 그 낡은 인덱스+1 지점(페이지 훨씬 아래쪽)로 곧장 점프해버리는 게
    // 원인이었음. 이 리스너가 실행되는 시점(=우리 애니메이션이 돌고 있지
    // 않을 때, 즉 스크롤바 드래그·키보드·앵커 이동처럼 우리가 모르는 경로로
    // 위치가 바뀐 경우)마다 추적 상태를 함께 비워, 다음 빠른 휠 입력은 항상
    // "실제 현재 위치에서 가장 가까운 체크포인트"부터 다시 계산하게 한다.
    window.addEventListener(
      "scroll",
      function () {
        if (smoothRaf === null) {
          smoothCurrent = window.scrollY;
          smoothTarget = window.scrollY;
          hsTargetIndex = null;
          currentEase = SMOOTH_EASE;
        }
      },
      { passive: true }
    );

    // (2026-09-02, 후속N) "SCROLL DOWN을 클릭하면 다음 화면으로 자동
    // 스크롤" — 위 wheel 핸들러의 체크포인트 이동 로직과 동일한 방식(현재
    // 추적 중인 hsTargetIndex가 있으면 그다음, 없으면 현재 위치에서 가장
    // 가까운 체크포인트의 그다음)으로 다음 칸을 계산해 이동한다. 인덱스
    // 페이지가 아니거나 체크포인트를 계산할 수 없으면(예: 하위 페이지) 아무
    // 것도 하지 않는다.
    var hsJumpToNext = function () {
      if (!document.body.classList.contains("home")) return;
      var hsPoints = computeHeroStepCheckpoints();
      if (!hsPoints || !hsPoints.length) return;
      var hsBase =
        hsTargetIndex !== null
          ? hsTargetIndex
          : nearestHeroStepIndex(hsPoints, window.scrollY);
      var hsNext = hsBase + 1;
      if (hsNext < 0 || hsNext >= hsPoints.length) return;
      hsAnimateTo(hsPoints[hsNext], hsNext);
      hsTargetIndex = hsNext;
    };
    document.querySelectorAll(".autoscroll-hint").forEach(function (hintEl) {
      hintEl.addEventListener("click", function (e) {
        e.preventDefault();
        hsJumpToNext();
      });
    });
  }

  // 헤더: 아래로 스크롤하는 동안에는 페이지와 함께 위로 올라가며 사라지고,
  // 스크롤을 멈춰도 계속 숨겨진 채로 있다가, 위로 스크롤할 때만 다시 나타남
  var header = document.querySelector(".site-header");
  if (header) {
    // 홈페이지 진입 슬라이드다운 애니메이션은 fill:both라 끝난 뒤에도 계속
    // transform 값을 붙잡고 있어, 그대로 두면 스크롤에 따른 표시/숨김 전환을
    // 막아버림 — 애니메이션이 끝나면 제거해 스크롤 기반 전환에 넘겨줌
    header.addEventListener("animationend", function () {
      header.style.animation = "none";
    });

    if (!prefersReducedMotion) {
      var lastScrollY = window.scrollY;
      var onHeaderScroll = function () {
        var currentY = window.scrollY;
        // (2026-09-05, 수정) 이전에 html.is-scrolling(체크포인트 자동 스크롤 +
        // 일반 휠 입력의 이징 스크롤 모두가 공유하는 플래그)이 켜져 있는 동안
        // 무조건 헤더를 숨기도록 했더니, 이 플래그가 일반적인 위로 스크롤
        // 동작 중에도 한동안(관성이 잦아들 때까지) 켜져 있어 "위로 스크롤하면
        // 바로 메뉴바가 나타나야" 하는 원래 동작이 막혀버렸음. 실제로 고쳐야
        //했던 건 "우리의 신념" 제목이 도킹되는 순간 생기던 1~4px 수준의 미세한
        // 되돌림(sticky 전환 시 레이아웃 보정)뿐이었으므로, is-scrolling 체크는
        // 완전히 제거하고 아래 델타 임계값(4px)만으로 그 미세한 되돌림을
        // 무시한다 — 진짜 위로 스크롤(4px 초과)은 항상 즉시 헤더를 보여준다.
        var delta = currentY - lastScrollY;
        if (currentY <= 8) {
          header.classList.remove("nav-hidden");
        } else if (delta < -4) {
          // 위로 스크롤할 때만 다시 나타남
          header.classList.remove("nav-hidden");
        } else if (delta > 0) {
          // 아래로 스크롤하는 동안 숨김 — 멈춰도 그대로 숨겨진 채 유지
          header.classList.add("nav-hidden");
        }
        lastScrollY = currentY;
      };
      window.addEventListener("scroll", onHeaderScroll, { passive: true });
    }
  }

  // 홈 히어로: 영상이 페이지 스크롤 속도의 20%로만 움직이는 패럴랙스 효과
  // (나머지 콘텐츠는 평소처럼 100% 속도로 스크롤됨)
  var heroVideoWrap = document.querySelector(".hero-video-wrap");
  if (heroVideoWrap && !prefersReducedMotion) {
    var parallaxTicking = false;
    var applyHeroParallax = function () {
      // 영상은 스크롤량의 20%만 이동해야 하므로, 페이지와 함께 움직이는 나머지 80%를
      // 반대 방향으로 되돌려(보정해) 순수 이동량이 20%만 남도록 함
      var offset = window.scrollY * 0.8;
      heroVideoWrap.style.transform = "translateY(" + offset + "px)";
      parallaxTicking = false;
    };
    window.addEventListener(
      "scroll",
      function () {
        if (!parallaxTicking) {
          window.requestAnimationFrame(applyHeroParallax);
          parallaxTicking = true;
        }
      },
      { passive: true }
    );
    applyHeroParallax();
  }

  // 카운트업 공통 헬퍼(runCountUp/countUpResetText): 요소를 0에서 data-target까지
  // ease-out으로 애니메이션. (후속70) "우리의 가치" 전면 개편으로 이 섹션의
  // count-up 숫자(연혁 1986/1996/2005/2021 + 통계 3/120+/14/3)가 전부
  // data-count-on-focus로 통일되어, 아래 일반 스크롤-진입 관찰자(countUpEls)의
  // 대상에서는 빠지고 그 아래 valueBlocks 포커스 시스템이 전담한다. 다만
  // runCountUp/countUpResetText 자체는 두 시스템이 공유해야 하므로 먼저
  // 정의해둔다(예전에는 countUpEls.length가 0이 아닐 때만 정의되어 있었는데,
  // "우리의 가치" 숫자가 전부 data-count-on-focus로 빠지면서 이 파일에 다른
  // 일반 count-up이 없으면 countUpEls.length === 0이 되어 정의가 스킵되는
  // 버그가 있었음 — 항상 정의되도록 밖으로 뺌).
  var countUpRunId = new WeakMap();
  var countUpResetText = new WeakMap();
  var runCountUp = function (el) {
    var target = parseInt(el.getAttribute("data-target"), 10) || 0;
    var prefix = el.getAttribute("data-prefix") || "";
    // (후속59) 숫자 뒤에 "개"/"개+" 같은 단위가 붙는 경우를 위해 data-suffix 지원.
    var suffix = el.getAttribute("data-suffix") || "";
    // (2026-08-31 갱신) data-comma: 24,000처럼 천 단위 구분 쉼표가 필요한 큰
    // 숫자용 옵션 포맷.
    var useComma = el.hasAttribute("data-comma");
    var fmt = function (n) { return useComma ? n.toLocaleString("en-US") : String(n); };
    if (prefersReducedMotion) {
      el.textContent = prefix + fmt(target) + suffix;
      return;
    }
    var myRunId = (countUpRunId.get(el) || 0) + 1;
    countUpRunId.set(el, myRunId);
    var duration = 1400;
    var start = null;
    var tick = function (ts) {
      if (countUpRunId.get(el) !== myRunId) return; // 더 새로운 실행이 시작됨 — 중단
      if (start === null) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      var value = Math.round(target * eased);
      el.textContent = prefix + fmt(value) + suffix;
      if (progress < 1) window.requestAnimationFrame(tick);
    };
    window.requestAnimationFrame(tick);
  };
  // 리셋 시 표시할 "0" 텍스트(prefix/suffix 포함)를 모든 count-up 요소에 대해 미리 기억
  document.querySelectorAll(".count-up").forEach(function (el) {
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    countUpResetText.set(el, prefix + "0" + suffix);
  });

  // 홈 "우리의 능력" 등 일반 스크롤-진입 카운트업: 화면에 들어올 때마다 다시
  // 카운트, 벗어나면 리셋. (후속69/70) "우리의 가치" 숫자는 전부
  // data-count-on-focus로 이 selector에서 제외되어 있음 — 현재는 다른 절에
  // 일반 count-up이 없다면 이 블록은 사실상 비어 있을 수 있으나, 추후 다른
  // 섹션에 추가될 경우를 대비해 로직은 유지.
  var countUpEls = document.querySelectorAll(".count-up:not([data-count-on-focus])");
  if (countUpEls.length && "IntersectionObserver" in window) {
    var countUpObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var el = entry.target;
          if (entry.isIntersecting) {
            runCountUp(el);
          } else {
            // 화면 밖으로 나가면 다음 재진입 때 처음부터 다시 카운트되도록 리셋하고
            // 진행 중이던 tick 루프는 runId 불일치로 자연히 멈추게 함.
            countUpRunId.set(el, (countUpRunId.get(el) || 0) + 1);
            if (!prefersReducedMotion) {
              el.textContent = countUpResetText.get(el) || "0";
            }
          }
        });
      },
      { threshold: 0.5 }
    );
    countUpEls.forEach(function (el) {
      countUpObserver.observe(el);
    });
  }

  // (후속70) "우리의 가치" 포커스 타이밍 개선: 기존에는 IntersectionObserver의
  // intersectionRatio(화면에 "얼마나 많이" 보이는지)가 가장 큰 블록을 포커스했는데,
  // 이 방식은 블록이 화면 중앙 부근까지 거의 다 들어와야 확대되어 사용자가
  // 계속 스크롤을 내리면서 확대된 내용을 볼 수 있는 시간이 짧다는 피드백을 받음.
  // 대신 뷰포트 상의 고정된 "포커스 라인"(상단에서 FOCUS_LINE_RATIO 지점)에 가장
  // 가까운 블록을 포커스하는 스크롤+rAF 기반 방식으로 교체. 두 블록 사이의 전환은
  // 두 블록 중심의 "라인까지 거리"가 같아지는 지점(정확히는 두 중심의 중점)에서
  // 일어나므로, 라인을 화면 아래쪽으로 내릴수록(비율↑) 다음 블록이 아직 화면
  // 하단에서 덜 들어온, 더 이른 시점에 전환이 일어나 확대 상태로 더 오래 볼 수
  // 있게 된다. 단, 라인을 너무 내리면 전환 시점에 블록 아래쪽이 아직 화면 밖이라
  // "덜 보인 채로 확대"되는 부자연스러움이 생긴다. Playwright로 0.4~0.65 구간을
  // 각 블록의 "포커스되는 순간의 노출 비율"과 "포커스 유지 스크롤 거리"로 실측한
  // 결과, 0.5 지점이 4개 블록 모두 대부분 온전히 보이는 상태에서 확대가 시작되면서도
  // (가장 긴 "검증된 기술력" 블록만 하단 25% 정도가 아직 화면 밖) 기존보다 확대
  // 유지 구간이 뚜렷이 길어지는 최적 지점으로 확인됨.
  // (2026-09-02, 후속8) "우리는 콜드젯 팀입니다" 제목에서 처음 선보인
  // "화면 아래에서 아주 크게 나타났다가, 틀고정 위치에 가까워질수록
  // 원래 크기로 줄어들며 안착하는" 확대→축소 연출이 좋다는 피드백을 받아
  // 다른 sticky 제목(우리가 하는 일/우리의 가치/우리의 신념)에도 똑같이
  // 적용 — 여러 곳에서 재사용할 수 있도록 공용 함수로 뽑음(아래
  // if(valueBlocks.length) 블록 안이 아니라 이 조건과 무관한 최상위 스코프에
  // 둬서, 이 페이지에 .value-block이 없어도 항상 정의되도록 함). pinEl
  // 자신의 rect.top이 한 화면 높이(viewportH)만큼 남은 시점부터 정확히
  // 0(틀고정)에 닿는 순간까지의 구간에서 h2에 큰 배율→1배로 줄어드는
  // transform:scale을 인라인으로 준다.
  // 화면 폭이 좁아 원래(1배) 텍스트조차 이미 폭에 거의 꽉 차 있는 경우
  // (모바일 등) 그대로 목표 배율(3.6)을 곱하면 화면 밖으로 넘쳐 가로
  // 스크롤이 생기는 문제가 콜드젯 제목에서 실제로 있었음(Playwright로
  // scrollLeft가 움직이는 것까지 확인) — h2의 실측 너비(offsetWidth,
  // transform의 영향을 받지 않음) 기준으로 현재 화면 폭 안에 안전하게
  // 들어가는 최대 배율을 매 프레임 다시 계산해, 원래 목표 배율과 비교해
  // 더 작은(더 안전한) 쪽을 사용한다.
  // clearOnSettle=false로 넘기면 틀고정된 뒤(progress>=1) 이 함수는
  // transform을 아예 건드리지 않는다 — "우리의 신념" 제목처럼 틀고정 이후
  // 또 다른 코드(콜드젯 섹션으로 넘어가는 전환용 translateY, belief
  // 전환 블록)가 같은 요소의 transform을 자체 관리하는 경우, 이 함수가 그
  // 값을 지워버리지 않도록 반드시 그 블록보다 "뒤에서" 호출해야 한다.
  // (2026-09-02, 후속13) 사용자 요청 — 이 확대→축소 연출이 시작되는 순간
  // (큰 글씨로 처음 나타날 때)에는 글씨가 아예 안 보이는 상태(투명)였다가,
  // 축소되어 정위치에 와서 박히는 동안 서서히 불투명해지도록(자연스럽게
  // "나타나면서 안착") 추가. 이미 있던 scale과 정확히 같은 progress(0→1)를
  // 그대로 opacity(0→1)에도 써서 "제일 클 때 완전 투명 → 제 크기로 줄어들어
  // 틀고정되는 순간 완전 불투명"이 항상 같은 속도로 함께 일어난다.
  var applyTitleShrinkZoom = function (pinEl, h2El, viewportH, clearOnSettle) {
    if (!pinEl || !h2El || !viewportH) return;
    var top = pinEl.getBoundingClientRect().top;
    var progress = Math.min(1, Math.max(0, 1 - top / viewportH));
    if (progress >= 1) {
      if (clearOnSettle !== false) {
        h2El.style.transform = "";
        h2El.style.opacity = "";
      }
      return;
    }
    var naturalW = h2El.offsetWidth;
    var winW = window.innerWidth || document.documentElement.clientWidth;
    var safeMaxScale = naturalW > 0 ? Math.max(1, (winW - 32) / naturalW) : 1;
    var scaleMax = Math.min(3.6, safeMaxScale);
    var scale = scaleMax - (scaleMax - 1) * progress;
    h2El.style.transform = "scale(" + scale.toFixed(3) + ")";
    h2El.style.opacity = progress.toFixed(3);
  };

  var valueBlocks = document.querySelectorAll(".value-block");
  if (valueBlocks.length) {
    // (후속74) 1~3번 카드를 담은 sticky 제목 컨테이너(.value-list)와
    // 4번(미디어 보도 및 수상) 카드를 담은 별도 컨테이너(.value-content-tail)로
    // 마크업이 분리되어 있으므로, .value-content가 이제 두 개 존재한다.
    // 배경색은 항상 "포커스된 블록이 실제로 속한" 컨테이너에 적용해야 하므로,
    // 더 이상 첫 번째 .value-content 하나만 고정 참조하지 않고 매번
    // block.closest(".value-content")로 찾는다.
    var VALUE_FOCUS_LINE_RATIO = 0.5;
    // (후속73) 라인까지 최대 허용 거리 비율 — 아래 applyValueFocus() 참고.
    // Playwright로 0.35~0.8 구간을 실측한 결과 0.5(=vh의 절반)일 때, 첫 번째
    // 블록이 "다른 블록들이 포커스를 넘겨받는 순간의 노출 비율(75~100%)"과
    // 비슷하게 화면에 거의 다 들어온 뒤에야 확대되도록 맞춰짐(이보다 크게
    // 잡으면 절반도 안 보인 채로 확대돼 여전히 "이미 확대돼 있던 것처럼"
    // 보이는 문제가 남고, 이보다 작게 잡아도 큰 차이가 없음).
    var VALUE_FOCUS_MAX_DIST_RATIO = 0.5;
    var valueFocusedBlock = null;
    var valueTicking = false;
    // (후속75) "우리의 신념" 제목(.belief-pin-title)이 화면 하단에서 올라와
    // 정확히 상단(top:0)에 틀고정되는 순간까지의 진행률을 --postdo-light로
    // 매 프레임 갱신 — 아래 applyValueFocus() 참고. 이 요소 자신의 위치로
    // 계산하므로 "제목이 화면에 나타나기 시작하는 순간"과 "완전히
    // 틀고정되는 순간"이 항상 정확히 일치한다(요청 #2, #3 통합).
    var beliefPinTitleEl = document.querySelector(".belief-pin-title");
    var beliefPinTitleH2 = beliefPinTitleEl
      ? beliefPinTitleEl.querySelector("h2")
      : null;
    // (후속80) "우리가 하는 일"의 제목줄(.stackdo-header)이 실제로 화면
    // 최상단에 틀고정되는 순간 흰 배경+하단 구분선으로 바뀌는 것과 완전히
    // 같은 방식을, sticky로 구현된 이 두 제목(.value-pin-title/
    // .belief-pin-title)에도 적용하기 위한 요소 참조 — 아래 applyValueFocus()가
    // 매 프레임 각자의 rect.top<=0 여부로 is-pinned 클래스를 토글한다
    // (.stackdo-header가 main.js의 updateStackdo()에서 stackdoScroll의
    // rect.top<=0으로 is-pinned를 토글하는 것과 동일한 방식 — 다만 이
    // 둘은 프레임 전체가 아니라 제목 자신이 sticky이므로 자기 자신의
    // rect.top을 본다).
    var valuePinTitleEl = document.querySelector(".value-pin-title");
    var valuePinTitleH2 = valuePinTitleEl
      ? valuePinTitleEl.querySelector("h2")
      : null;
    // (후속82) "우리의 신념" 제목 바로 아래 CO2 영상 — 제목이 틀고정되는
    // 순간 영상도 함께 틀고정(position:sticky)되고, 그 안의 텍스트 박스는
    // 이후 스크롤에 따라 숨김→중앙 정지→위로 퇴장의 3단계로 움직인다.
    // 아래 applyValueFocus()에서 매 프레임 계산.
    var beliefVideoScroll = document.querySelector(".belief-video-scroll");
    var beliefVideoWrap = beliefVideoScroll
      ? beliefVideoScroll.querySelector(".belief-video-wrap")
      : null;
    // (후속85) 흰색 lead 박스(제목/부제)가 중앙 정지 후 퇴장(exited)하는 것과
    // "동시에" 본문 문장(더 이상 박스가 아닌 순수 텍스트, .belief-video-desc-text)이
    // 같은 자리로 올라와 정지(risen)하도록 아래 applyValueFocus()에서 같은
    // 구간(idx>=2)에 맞춰 두 클래스를 함께 토글한다.
    var beliefVideoBoxLead = beliefVideoWrap
      ? beliefVideoWrap.querySelector(".belief-video-box-lead")
      : null;
    var beliefVideoDescText = beliefVideoWrap
      ? beliefVideoWrap.querySelector(".belief-video-desc-text")
      : null;
    // (2026-09-02) "우리는 콜드젯입니다" — .belief-list 바로 다음 섹션. 구조와
    // JS 처리 모두 위 belief* 요소들과 완전히 동일한 패턴을 재사용한다(제목
    // sticky pin 여부 → 영상 sticky top/height 갱신 → 3구간 박스/문장 등장).
    var coldjetPinTitleEl = document.querySelector(".coldjet-pin-title");
    var coldjetPinTitleH2 = coldjetPinTitleEl
      ? coldjetPinTitleEl.querySelector("h2")
      : null;
    var coldjetVideoScroll = document.querySelector(".coldjet-video-scroll");
    var coldjetVideoWrap = coldjetVideoScroll
      ? coldjetVideoScroll.querySelector(".coldjet-video-wrap")
      : null;
    var coldjetVideoBoxLead = coldjetVideoWrap
      ? coldjetVideoWrap.querySelector(".coldjet-video-box-lead")
      : null;
    var coldjetVideoDescText = coldjetVideoWrap
      ? coldjetVideoWrap.querySelector(".coldjet-video-desc-text")
      : null;
    // (2026-09-02, 후속5→후속N) 히어로와 동일한 Scroll down 힌트(.coldjet-scroll-hint/
    // .belief-scroll-hint, 각각 .coldjet-video-wrap/.belief-video-wrap 안에
    // 절대 위치). 한때는 박스가 뜬 첫 구간에서만 보이고 다음 구간(로고/CO2
    // 문장)으로 넘어가면 숨겼으나, 사용자 피드백(그 화면들엔 SCROLL DOWN이
    // 안 보임)에 따라 콘텐츠 구간과 무관하게 각 섹션이 화면에 틀고정돼 있는
    // 동안은 항상 보이도록 바꿈 — 더 이상 이 JS가 별도로 숨기지 않고,
    // style.css의 html.is-scrolling 규칙으로 스크롤이 실제로 움직이는
    // 동안에만 숨는다.
    // (2026-09-02, 후속N) "우리의 가치" 힌트 — 이 섹션엔 화면 전체를 덮는
    // sticky 프레임이 없어(제목만 sticky) position:fixed로 뷰포트에 고정해두고,
    // "우리의 가치" 제목이 틀고정된 뒤부터 "우리의 신념" 제목이 틀고정되기
    // 전까지만 아래 applyValueFocus()가 is-shown을 토글한다.
    var valueScrollHintEl = document.querySelector(".value-scroll-hint");

    var triggerValueFocusCountUp = function (block) {
      block.querySelectorAll(".count-up[data-count-on-focus]").forEach(function (countEl) {
        if (!countEl.dataset.counted) {
          countEl.dataset.counted = "1";
          runCountUp(countEl);
        }
      });
    };
    var resetValueFocusCountUp = function (block) {
      block.querySelectorAll(".count-up[data-count-on-focus]").forEach(function (countEl) {
        if (countEl.dataset.counted) {
          delete countEl.dataset.counted;
          // (버그 수정) runId를 갱신하지 않으면 아직 실행 중이던 runCountUp()의
          // 이전 tick 루프가 다음 프레임에 자기 진행값으로 textContent를 다시
          // 덮어써버려, 포커스를 잃어도 카운트가 끝까지 계속 올라가는 문제가
          // 있었음(Playwright로 확인). 일반 스크롤-진입 카운트업 리셋과 동일하게
          // runId를 새 세대로 올려 이전 tick이 스스로 멈추게 함.
          countUpRunId.set(countEl, (countUpRunId.get(countEl) || 0) + 1);
          if (!prefersReducedMotion) {
            countEl.textContent = countUpResetText.get(countEl) || "0";
          }
        }
      });
    };

    var applyValueFocus = function () {
      var vh = window.innerHeight || document.documentElement.clientHeight;
      // (후속80) "우리가 하는 일" 제목줄과 완전히 같은 방식 — sticky 제목
      // 자신의 rect.top이 0 이하가 되는(=실제로 상단에 들러붙는) 그 순간
      // is-pinned를 붙여 흰 배경+하단 구분선으로 바뀌게 함. .value-pin-title은
      // .value-list 맨 위에 여백 없이 바로 있어 이 섹션에 들어오자마자
      // 거의 즉시 stuck 상태가 되고, .belief-pin-title은 --postdo-light가
      // 1에 도달하는(= rect.top이 0에 닿는) 순간과 정확히 일치한다.
      var valueTitlePinned = valuePinTitleEl
        ? valuePinTitleEl.getBoundingClientRect().top <= 0
        : false;
      if (valuePinTitleEl) {
        valuePinTitleEl.classList.toggle("is-pinned", valueTitlePinned);
      }
      applyTitleShrinkZoom(valuePinTitleEl, valuePinTitleH2, vh, true);
      var beliefTitlePinned = beliefPinTitleEl
        ? beliefPinTitleEl.getBoundingClientRect().top <= 0
        : false;
      if (beliefPinTitleEl) {
        beliefPinTitleEl.classList.toggle("is-pinned", beliefTitlePinned);
      }
      // (2026-09-02, 후속N) "우리의 가치" SCROLL DOWN 힌트 — 이 제목이
      // 틀고정된 뒤(=이 섹션이 화면을 채운 뒤)부터 "우리의 신념" 제목이
      // 틀고정되기 전까지만("우리의 신념" 구간에 들어서면 그쪽 자신의 힌트가
      // 대신함) 보이도록.
      if (valueScrollHintEl) {
        valueScrollHintEl.classList.toggle(
          "is-shown",
          valueTitlePinned && !beliefTitlePinned
        );
      }
      // (후속82) 영상(.belief-video-wrap)은 top:제목 실측 높이로 sticky —
      // .belief-pin-title(top:0)과 .belief-video-wrap(top:제목높이)은 같은
      // 부모 흐름 안에 여백 없이 붙어 있어 수학적으로 항상 같은 스크롤
      // 위치에서 동시에 stuck되므로, 제목의 is-pinned 판정을 그대로 재사용.
      if (beliefVideoWrap) {
        if (beliefPinTitleEl) {
          // (후속85) 영상이 이제 고정 배너 비율이 아니라 "제목 아래 남은
          // 화면 전체"를 채우므로, top(제목 높이)뿐 아니라 height(뷰포트
          // 높이 - 제목 높이)도 매 프레임 함께 갱신 — 제목+영상이 여백
          // 없이 위아래로 꼭 맞물려 뷰포트를 정확히 채우게 됨.
          var beliefTitleH = beliefPinTitleEl.getBoundingClientRect().height;
          beliefVideoWrap.style.top = beliefTitleH + "px";
          beliefVideoWrap.style.height = Math.max(0, vh - beliefTitleH) + "px";
          // (2026-09-05) 제목이 한 화면 아래에서 날아오기 시작(0)해 상단에
          // 박히는(1) 진행률 — applyTitleShrinkZoom과 같은 공식 — 을
          // --belief-reveal로 넘겨 영상이 제목과 함께 스르륵 나타나게 함.
          var beliefApproach = Math.min(
            1,
            Math.max(0, 1 - beliefPinTitleEl.getBoundingClientRect().top / vh)
          );
          beliefVideoWrap.style.setProperty("--belief-reveal", beliefApproach.toFixed(3));
        }
        beliefVideoWrap.classList.toggle("is-pinned", beliefTitlePinned);
      }
      // (후속82 계속) 영상이 틀고정된 뒤 추가로 스크롤되는 여유 구간
      // (.belief-video-scroll, .stackdo-scroll과 동일한 "100vh + N*Xvh" 공식)의
      // 진행률을 3구간(0:숨김/1:중앙 정지/2:퇴장)으로 나눠 텍스트 박스에
      // 반영 — "한 번 더 스크롤"할 때마다 다음 구간으로 넘어가는 계단식
      // 연출이 되도록 각 구간에 65vh의 스크롤 여유를 둔다.
      if (beliefVideoScroll && (beliefVideoBoxLead || beliefVideoDescText)) {
        var beliefScrollRect = beliefVideoScroll.getBoundingClientRect();
        var beliefScrolled = -beliefScrollRect.top;
        // (2026-09-02) 박스 3구간(zone 0~2)의 타이밍은 항상 고정된 "3*65vh"
        // 예산만 기준으로 계산 — .belief-video-scroll 자신의 높이엔 아래
        // 콜드젯 전환용 여유(+100vh, style.css 참고)가 이미 포함돼 있어,
        // rect.height를 그대로 분모로 쓰면 3구간 전환이 그만큼 느려져 버린다.
        // 늘어난 여유는 순수하게 그 뒤에 이어지는 전환 구간의 몫으로만 쓴다.
        var beliefBoxTotalPx = 3 * 0.65 * vh;
        var beliefProgress = beliefBoxTotalPx > 0
          ? Math.min(1, Math.max(0, beliefScrolled / beliefBoxTotalPx))
          : 0;
        var beliefZones = 3;
        var beliefIdx = beliefProgress > 0
          ? Math.min(beliefZones - 1, Math.floor(beliefProgress * beliefZones))
          : 0;
        if (beliefVideoBoxLead) {
          beliefVideoBoxLead.classList.toggle("is-risen", beliefIdx >= 1);
          beliefVideoBoxLead.classList.toggle("is-exited", beliefIdx >= 2);
        }
        if (beliefVideoDescText) {
          beliefVideoDescText.classList.toggle("is-risen", beliefIdx >= 2);
        }
        // (2026-09-02) "우리의 신념" → "우리는 콜드젯입니다" 전환 — 박스 3구간
        // 예산을 다 쓴 뒤 추가로 스크롤되는 여유(+100vh, 위 beliefBoxTotalPx
        // 이후분)를 이 전환 구간의 예산으로 삼는다. 이 구간에서는:
        //   - 제목(beliefPinTitleEl): 스크롤과 같은 속도(1:1)로 위로 이동
        //     (=스크롤이 멈추지 않았다면 원래 sticky가 풀려 자연스럽게
        //     화면 밖으로 나갔을 움직임을 인라인 transform으로 대신 흉내)
        //   - 영상(beliefVideoWrap): 제목보다 느린 속도(0.35배)로 위로 이동
        //     (아직 화면에 남아 스크롤이 "정상 속도"로 보이는 새 섹션에
        //     서서히 덮이는 동안 자기 자신은 천천히 빠져나가는 효과)
        //   - 본문 문장(beliefVideoDescText): 움직이지 않고 제자리에서
        //     서서히 투명해짐(opacity)
        // 두 요소(제목/영상) 모두 이 구간 내내 CSS상으로는 여전히 sticky로
        // "고정"된 상태다(전환용 여유가 각자의 sticky 컨테이너 높이에 포함돼
        // 있으므로) — 인라인 transform이 그 고정을 상쇄해 서로 다른 속도로
        // 풀려나는 것처럼 보이게 하는 방식. 구간 예산을 다 쓰는 순간(=아래
        // beliefTransitionScrolled가 상한에 도달하는 순간) 두 컨테이너의
        // sticky 범위도 정확히 함께 끝나므로, 그 이후 자연스러운 문서 흐름
        // 스크롤과 인라인 transform이 매끄럽게 이어진다.
        var beliefTransitionTotalPx = 1.0 * vh;
        var beliefTransitionScrolled = Math.min(
          beliefTransitionTotalPx,
          Math.max(0, beliefScrolled - beliefBoxTotalPx)
        );
        var beliefTransitionProgress = beliefTransitionTotalPx > 0
          ? beliefTransitionScrolled / beliefTransitionTotalPx
          : 0;
        if (beliefPinTitleEl) {
          beliefPinTitleEl.style.transform = beliefTransitionScrolled > 0
            ? "translateY(-" + beliefTransitionScrolled + "px)"
            : "";
        }
        if (beliefVideoWrap) {
          var beliefVideoLagPx = beliefTransitionScrolled * 0.35;
          beliefVideoWrap.style.transform = beliefTransitionScrolled > 0
            ? "translateY(-" + beliefVideoLagPx + "px)"
            : "";
        }
        if (beliefVideoDescText) {
          beliefVideoDescText.style.opacity = beliefTransitionProgress > 0
            ? String(Math.max(0, 1 - beliefTransitionProgress * 1.4))
            : "";
        }
      }
      // (2026-09-02, 후속8) 반드시 위 belief 전환 블록"뒤에서" 호출 — 그
      // 블록이 beliefPinTitleEl.style.transform을 매 프레임 무조건 쓰기
      // 때문에(전환 구간이 아니면 ""로 지움), 순서가 바뀌면 이 함수가 준
      // scale이 곧바로 지워져 버린다. clearOnSettle:false로 넘겨 틀고정된
      // 뒤(progress>=1)에는 이 함수가 transform을 아예 건드리지 않게 하고,
      // 그 이후의 값은 전적으로 위 블록(정지 시 ""/전환 구간엔 translateY)에
      // 맡긴다.
      applyTitleShrinkZoom(beliefPinTitleEl, beliefPinTitleH2, vh, false);
      // (2026-09-02) "우리는 콜드젯입니다" 섹션 자체의 제목 sticky pin 여부 →
      // 영상 sticky top/height 갱신 → 2구간 박스/문장 등장 — 위 belief* 블록과
      // 완전히 같은 패턴.
      // (2026-09-02, 후속15) 사용자 요청 — 이 섹션도 "우리의 신념 → 우리는
      // 콜드젯입니다" 전환과 완전히 같은 방식으로 다음 섹션(메뉴 선택)에게
      // 화면을 넘겨주도록, 더 이상 "이 섹션 자신은 전환 로직이 필요 없다"가
      // 아니게 됨 — 아래 coldjetVideoScroll 블록 끝에 belief와 동일한 전환
      // 블록을 추가했다(이 섹션 다음의 .section-menu-picker가 그 여유만큼
      // 음수 margin-top으로 겹쳐 올라오는 CSS 트릭도 style.css에 함께 추가).
      var coldjetTitlePinned = coldjetPinTitleEl
        ? coldjetPinTitleEl.getBoundingClientRect().top <= 0
        : false;
      if (coldjetPinTitleEl) {
        coldjetPinTitleEl.classList.toggle("is-pinned", coldjetTitlePinned);
      }
      // (2026-09-02, 후속4) 영상 프레임이 이제 "제목 아래 남은 영역"이 아니라
      // 뷰포트 전체(top:0/height:100vh, style.css의 .coldjet-video-wrap 참고)로
      // 고정값이 되어, 예전처럼 제목 실측 높이로 top/height를 매 프레임 갱신할
      // 필요가 없어짐 — is-pinned 토글만 남는다.
      if (coldjetVideoWrap) {
        coldjetVideoWrap.classList.toggle("is-pinned", coldjetTitlePinned);
        // (2026-09-05) 제목 접근 진행률(0→1)을 --coldjet-reveal로 넘겨 영상이
        // 제목과 함께 스르륵 나타나게 함(belief와 동일).
        if (coldjetPinTitleEl) {
          var coldjetApproach = Math.min(
            1,
            Math.max(0, 1 - coldjetPinTitleEl.getBoundingClientRect().top / vh)
          );
          coldjetVideoWrap.style.setProperty("--coldjet-reveal", coldjetApproach.toFixed(3));
        }
      }
      // (2026-09-02, 후속2) "박스가 영상 나올 때 함께 올라오게" — 더 이상 박스의
      // 첫 등장(is-risen)을 스크롤 구간(idx)에 걸어두지 않고, 영상 자체가
      // 틀고정되는 순간(coldjetTitlePinned, 위에서 이미 계산됨)과 동시에 뜨도록
      // 바꿈. 이후 "한 번 더 스크롤"하면 박스는 퇴장하고 문장이 그 자리로
      // 올라오는 것은 기존과 동일 — 구간이 2개(0: 박스만 정지/1: 박스 퇴장+문장
      // 등장).
      if (coldjetVideoScroll && (coldjetVideoBoxLead || coldjetVideoDescText)) {
        var coldjetScrollRect = coldjetVideoScroll.getBoundingClientRect();
        var coldjetScrolled = -coldjetScrollRect.top;
        // (2026-09-02, 후속15) belief와 동일하게, 2구간 박스 진행률은 컨테이너
        // 전체 높이(이제 전환 여유 +100vh가 추가돼 있음)와 무관하게 고정
        // 예산(2 * 0.65 * vh)만 기준으로 계산 — 아래 전환 블록이 그 이후분을
        // 별도로 가져다 쓴다(belief의 beliefBoxTotalPx와 정확히 같은 방식).
        var coldjetBoxTotalPx = 2 * 0.65 * vh;
        var coldjetProgress = coldjetBoxTotalPx > 0
          ? Math.min(1, Math.max(0, coldjetScrolled / coldjetBoxTotalPx))
          : 0;
        var coldjetZones = 2;
        var coldjetIdx = coldjetProgress > 0
          ? Math.min(coldjetZones - 1, Math.floor(coldjetProgress * coldjetZones))
          : 0;
        if (coldjetVideoBoxLead) {
          coldjetVideoBoxLead.classList.toggle("is-risen", coldjetTitlePinned);
          coldjetVideoBoxLead.classList.toggle("is-exited", coldjetIdx >= 1);
        }
        if (coldjetVideoDescText) {
          coldjetVideoDescText.classList.toggle("is-risen", coldjetIdx >= 1);
        }
        // (2026-09-02, 후속15) "우리의 신념" → "우리는 콜드젯입니다" 전환
        // 블록(위 beliefTransition* 부분)과 완전히 동일한 방식·속도 —
        // 박스 2구간 예산(coldjetBoxTotalPx)을 다 쓴 뒤 추가로 스크롤되는
        // 여유(+100vh, style.css의 .coldjet-video-scroll 참고)를 이 전환
        // 구간의 예산으로 삼는다:
        //   - 제목(coldjetPinTitleEl): 스크롤과 같은 속도(1:1)로 위로 이동
        //   - 영상(coldjetVideoWrap): 제목보다 느린 속도(0.35배)로 위로 이동
        //   - 본문 문장(coldjetVideoDescText): 제자리에서 서서히 투명해짐
        // 다음 섹션(.section-menu-picker)은 이 전환 여유만큼 음수
        // margin-top으로 끌어올려 겹쳐 두어(style.css 참고), 이 구간을
        // 스크롤하는 동안 순수 문서 흐름 속도(=스크롤과 1:1)로 아래에서
        // 위로 올라오며 이 영상 화면을 덮는다 — .section-coldjet이
        // .belief-video-scroll의 전환 여유를 덮던 것과 정확히 같은 트릭.
        var coldjetTransitionTotalPx = 1.0 * vh;
        var coldjetTransitionScrolled = Math.min(
          coldjetTransitionTotalPx,
          Math.max(0, coldjetScrolled - coldjetBoxTotalPx)
        );
        var coldjetTransitionProgress = coldjetTransitionTotalPx > 0
          ? coldjetTransitionScrolled / coldjetTransitionTotalPx
          : 0;
        if (coldjetPinTitleEl) {
          coldjetPinTitleEl.style.transform = coldjetTransitionScrolled > 0
            ? "translateY(-" + coldjetTransitionScrolled + "px)"
            : "";
        }
        if (coldjetVideoWrap) {
          var coldjetVideoLagPx = coldjetTransitionScrolled * 0.35;
          coldjetVideoWrap.style.transform = coldjetTransitionScrolled > 0
            ? "translateY(-" + coldjetVideoLagPx + "px)"
            : "";
        }
        if (coldjetVideoDescText) {
          coldjetVideoDescText.style.opacity = coldjetTransitionProgress > 0
            ? String(Math.max(0, 1 - coldjetTransitionProgress * 1.4))
            : "";
        }
      }
      // (2026-09-02, 후속15) 반드시 위 콜드젯 전환 블록 "뒤에서" 호출 — belief
      // 쪽(위 applyTitleShrinkZoom(beliefPinTitleEl...) 호출부 주석)과 정확히
      // 같은 이유로 clearOnSettle:false로 변경(기존 true) — 전환 블록이
      // coldjetPinTitleEl.style.transform을 매 프레임 관리하므로, 이 함수가
      // 그 값을 지워버리지 않게 한다.
      applyTitleShrinkZoom(coldjetPinTitleEl, coldjetPinTitleH2, vh, false);
      var focusY = vh * VALUE_FOCUS_LINE_RATIO;
      var VALUE_FOCUS_MAX_DIST = vh * VALUE_FOCUS_MAX_DIST_RATIO;
      var best = null;
      var bestDist = Infinity;
      valueBlocks.forEach(function (block) {
        var rect = block.getBoundingClientRect();
        // 화면 위/아래로 완전히 벗어난 블록은 후보에서 제외
        if (rect.bottom <= 0 || rect.top >= vh) return;
        var center = rect.top + rect.height / 2;
        var dist = Math.abs(center - focusY);
        // (후속73) 두 번째~네 번째 블록은 "직전에 포커스였던 블록과의 라인까지
        // 거리 경쟁"에서 이겨야만 포커스를 넘겨받으므로 자연스럽게 라인 근처에
        // 어느 정도 다가와야 확대되지만, 맨 처음 블록(첫 번째)은 경쟁 상대가
        // 없어 화면 바닥에 살짝 걸치기만 해도(= 유일한 후보) 즉시 확대돼버려
        // "스크롤해서 나타나는 게 아니라 원래부터 확대돼 있던 것처럼" 보인다는
        // 지적을 받음. VALUE_FOCUS_MAX_DIST(라인까지 최대 허용 거리)를 둬서,
        // 후보가 하나뿐이더라도 라인에 충분히 가까워지기 전에는 아무도
        // 포커스되지 않도록(best를 null로 유지) 제한 — 이후 블록들 사이의
        // 자연스러운 교차 전환 타이밍(가장 큰 블록 기준 실측 401px)에는
        // 영향이 없도록 그보다 넉넉하게 잡음.
        if (dist > VALUE_FOCUS_MAX_DIST) return;
        if (dist < bestDist) {
          bestDist = dist;
          best = block;
        }
      });
      // (후속75) "우리의 신념" 제목 진행률(--postdo-light) 계산 — 제목이
      // 화면 하단(rect.top === vh)에서 막 나타나기 시작할 때 0, 스크롤이
      // 진행되어 정확히 화면 상단(rect.top === 0)에 닿아 틀고정될 때 1이
      // 되도록 (vh - rect.top) / vh로 구함. sticky이므로 top:0에 도달한
      // 뒤에는 rect.top이 0에 머물러 자연스럽게 1로 유지되고, 위로
      // 스크롤하면 다시 0으로 돌아가 가역적으로 동작한다.
      if (beliefPinTitleEl) {
        var beliefRect = beliefPinTitleEl.getBoundingClientRect();
        var lightProgress = vh > 0
          ? Math.min(1, Math.max(0, (vh - beliefRect.top) / vh))
          : 0;
        document.documentElement.style.setProperty("--postdo-light", lightProgress.toFixed(3));
      }
      if (best !== valueFocusedBlock) {
        if (valueFocusedBlock) resetValueFocusCountUp(valueFocusedBlock);
        valueFocusedBlock = best;
        // (요청#3) "확대가 되면 숫자 카운트가 되도록" — is-focused로 전환되는
        // 바로 그 순간에만 카운트업을 트리거.
        if (best) triggerValueFocusCountUp(best);
      }
      valueBlocks.forEach(function (block) {
        block.classList.toggle("is-focused", block === best);
      });
      if (best) {
        var tone = best.getAttribute("data-tone");
        var hostContent = best.closest(".value-content");
        if (tone && hostContent) hostContent.style.backgroundColor = tone;
      }
    };

    var onValueScroll = function () {
      if (!valueTicking) {
        valueTicking = true;
        window.requestAnimationFrame(function () {
          applyValueFocus();
          valueTicking = false;
        });
      }
    };
    window.addEventListener("scroll", onValueScroll, { passive: true });
    window.addEventListener("resize", onValueScroll, { passive: true });
    applyValueFocus();
  }

  // 스크롤 리빌 애니메이션 (후속61, 원래는 첫 페이지 정적 섹션 전용이었으나
  // 후속9에서 홈 하단 "메뉴 선택" 카드 섹션 + 사이트 공통 푸터(모든 57개
  // 페이지가 공유)까지 확장됨): 뷰포트에 들어오면
  // .reveal/.reveal-scale/.reveal-pop 요소에 is-visible을 붙여 CSS 트랜지션으로
  // 나타나게 함. 카운트업과 달리 1회성 연출이므로 재생 뒤 관련 클래스를 전부
  // 제거해 :hover 등 요소 자체의 transform과 충돌하지 않도록 정리한다. 이
  // querySelectorAll은 페이지 로드 시 한 번만 실행되므로, 해당 클래스가 없는
  // 페이지에서는 revealEls.length가 0이라 관찰자 자체가 아예 설치되지 않는다
  // (기존 56개 서브페이지가 그랬듯, 오버헤드 없이 자동으로 안전하게 스킵됨).
  var revealEls = document.querySelectorAll(".reveal, .reveal-scale, .reveal-pop");
  if (revealEls.length) {
    var clearRevealClasses = function (el) {
      el.classList.remove("reveal", "reveal-scale", "reveal-pop", "is-visible");
      el.style.removeProperty("--reveal-delay");
    };
    if (prefersReducedMotion || !("IntersectionObserver" in window)) {
      revealEls.forEach(clearRevealClasses);
    } else {
      var revealObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            var el = entry.target;
            revealObserver.unobserve(el);
            el.classList.add("is-visible");
            window.setTimeout(function () {
              clearRevealClasses(el);
            }, 1500);
          });
        },
        { threshold: 0.2, rootMargin: "0px 0px -8% 0px" }
      );
      revealEls.forEach(function (el) {
        revealObserver.observe(el);
      });
    }
  }

  // 문의 폼: 실제 전송 기능은 아직 연결되지 않은 시안 단계임을 안내
  var form = document.querySelector(".quote-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("시안 단계 페이지입니다. 실제 문의 접수는 추후 서버 연동 후 동작합니다.");
    });
  }

  // "우리가 하는 일" — 가로 적층 스크롤: .stackdo-scroll의 여유 높이만큼
  // 스크롤되는 진행률(progress)로 활성 패널 인덱스를 구해, 지나간 항목은
  // 위쪽 가로 탭 줄에 표시하고 현재 항목만 큰 패널로 보여준다.
  var stackdoScroll = document.querySelector(".stackdo-scroll");
  var stackdoPanels = stackdoScroll
    ? Array.prototype.slice.call(stackdoScroll.querySelectorAll(".stackdo-panel"))
    : [];
  var stackdoTabs = stackdoScroll
    ? Array.prototype.slice.call(stackdoScroll.querySelectorAll(".stackdo-tab"))
    : [];
  var stackdoHeads = stackdoScroll
    ? Array.prototype.slice.call(stackdoScroll.querySelectorAll(".stackdo-panel-head"))
    : [];
  if (stackdoScroll && stackdoPanels.length) {
    var stackdoIdx = -1;
    var stackdoTicking = false;
    // 지나간(passed) 항목의 번호+제목(.stackdo-panel-head)이 실제로 자신의
    // 탭(.stackdo-tab) 위치·크기로 "변형되며 날아가 박히도록" 두 요소의
    // 실측 bounding rect 차이를 매번 계산해 정확한 translate/scale을
    // 인라인 style로 대입한다(하드코딩된 방향이 아닌 실측 기반 FLIP).
    var flyHeadToTab = function (headEl, tabEl) {
      headEl.style.transform = "none";
      var hr = headEl.getBoundingClientRect();
      var tr = tabEl.getBoundingClientRect();
      if (!hr.width || !hr.height) return;
      var scale = Math.max(0.28, Math.min(1, tr.height / hr.height));
      var dx = (tr.left + tr.width / 2) - (hr.left + hr.width / 2);
      var dy = (tr.top + tr.height / 2) - (hr.top + hr.height / 2);
      headEl.style.transform =
        "translate(" + dx.toFixed(1) + "px," + dy.toFixed(1) + "px) scale(" + scale.toFixed(3) + ")";
    };
    // 전체 구간을 (항목 수 + 1)단계로 나눔 — 마지막 단계(갤러리 단계)에서는
    // 05번까지 전부 탭으로 날아간 뒤, 탭 5열과 같은 5열 그리드로 이미지
    // 5장이 나란히 정렬되어 보인다. 이 갤러리 단계를 한 번 더 스크롤하면
    // (진행률이 1을 넘어가며) sticky 래퍼가 자연스럽게 풀려 아래로 흘러간다.
    // (2026-09-02, 후속18) 원래는 +1(=6단계)이라 마지막 탭이 붙는 순간과
    // 갤러리(이미지 5장) 등장이 같은 구간 경계에서 동시에 일어나 "렌탈·데모
    // 서비스" 탭이 붙은 화면을 볼 틈이 없었음 — +2(=7단계)로 늘려 "5개 탭
    // 전부 붙음(갤러리 아직)"과 "갤러리 등장"을 서로 다른 구간으로 분리
    // (아래 is-gallery/stackdoGallery의 임계값도 stackdoPanels.length+1로
    // 함께 늦춤). style.css의 .stackdo-scroll 높이 배수도 6→7로 맞춰
    // 늘렸으므로(총 스크롤 길이 자체가 한 단계만큼 늘어남), 기존 단계들의
    // 체감 속도는 그대로 유지된다.
    var stackdoZones = stackdoPanels.length + 2;
    var stackdoGallery = document.getElementById("stackdoGallery");
    var stackdoFrame = stackdoScroll.querySelector(".stackdo-frame");
    // (2026-09-02, 후속8) "우리가 하는 일" 제목줄에도 콜드젯 제목과 같은
    // 확대→축소 연출 적용 — .stackdo-header는 그 자체가 sticky는 아니고
    // sticky인 .stackdo-frame의 맨 위 자식(오프셋 없음)이라, 이 요소 자신의
    // rect.top이 0에 닿는 순간이 곧 프레임이 틀고정되는 순간과 정확히
    // 일치한다(아래 is-pinned 토글에 쓰는 stackdoScroll 기준과도 동일).
    var stackdoHeaderEl = stackdoScroll.querySelector(".stackdo-header");
    var stackdoHeaderH2 = stackdoHeaderEl
      ? stackdoHeaderEl.querySelector("h2")
      : null;
    var updateStackdo = function () {
      stackdoTicking = false;
      var rect = stackdoScroll.getBoundingClientRect();
      if (stackdoFrame) stackdoFrame.classList.toggle("is-pinned", rect.top <= 0);
      applyTitleShrinkZoom(stackdoHeaderEl, stackdoHeaderH2, window.innerHeight, true);
      var total = rect.height - window.innerHeight;
      var scrolled = -rect.top;
      var progress = total > 0 ? Math.min(1, Math.max(0, scrolled / total)) : 0;
      var idx = Math.min(stackdoZones - 1, Math.floor(progress * stackdoZones));
      if (progress <= 0) idx = 0;
      // (후속74 되돌림) --postdo-dark(어둡기 진행률)는 한때 "우리의 가치"
      // 3번째 카드가 제목줄 밑으로 들어가며 제목이 틀고정에서 풀리는 시점
      // 기준으로 재계산하도록 바꿨었으나, 그 결과 1~3번 카드 구간이 원래의
      // 짙은 배경 없이 밝게 보여 기존에 이어붙여 놓은 어두운 배경(우리가
      // 하는 일 → 우리의 가치 → Customer Voice)이 끊겨 보인다는 피드백을
      // 받고 원래대로("우리가 하는 일" 자신의 틀고정 해제 시점 기준)
      // 되돌림. 제목의 틀고정 해제 시점만 3번째 카드 직후로 앞당기는
      // 구조(변경은 generate.py의 .value-list/.value-content-tail 분리로
      // 유지)는 이 어둡기 계산과 무관하게 그대로 유지된다.
      var darkFadeDistance = window.innerHeight * 0.6;
      var darkProgress = darkFadeDistance > 0
        ? Math.min(1, Math.max(0, (scrolled - total) / darkFadeDistance))
        : 0;
      document.documentElement.style.setProperty("--postdo-dark", darkProgress.toFixed(3));
      if (idx !== stackdoIdx) {
        stackdoIdx = idx;
        if (stackdoFrame) stackdoFrame.classList.toggle("is-gallery", idx >= stackdoPanels.length + 1);
        for (var i = 0; i < stackdoPanels.length; i++) {
          stackdoPanels[i].classList.remove("is-active", "is-passed", "is-upcoming");
          stackdoPanels[i].classList.add(i === idx ? "is-active" : i < idx ? "is-passed" : "is-upcoming");
        }
        for (var t = 0; t < stackdoTabs.length; t++) {
          stackdoTabs[t].classList.toggle("is-shown", t < idx);
        }
        for (var h = 0; h < stackdoHeads.length; h++) {
          if (h < idx) flyHeadToTab(stackdoHeads[h], stackdoTabs[h]);
          else stackdoHeads[h].style.transform = "";
        }
        if (stackdoGallery) {
          stackdoGallery.classList.toggle("is-shown", idx >= stackdoPanels.length + 1);
        }
      }
    };
    window.addEventListener(
      "scroll",
      function () {
        if (!stackdoTicking) {
          stackdoTicking = true;
          window.requestAnimationFrame(updateStackdo);
        }
      },
      { passive: true }
    );
    window.addEventListener("resize", updateStackdo);
    updateStackdo();
    // 소제목(탭)과 그 아래 이미지가 서로 다른 위치에 있어도 하나의 짝으로
    // 동작하도록(하나에 마우스오버 하은 늘도 다른 하나에 is-hovered 토관) 연결.
    var stackdoGalleryItems = stackdoGallery
      ? Array.prototype.slice.call(stackdoGallery.querySelectorAll(".stackdo-gallery-item"))
      : [];
    stackdoTabs.forEach(function (tab, i) {
      var img = stackdoGalleryItems[i];
      if (!img) return;
      tab.addEventListener("mouseenter", function () { img.classList.add("is-hovered"); });
      tab.addEventListener("mouseleave", function () { img.classList.remove("is-hovered"); });
    });
    stackdoGalleryItems.forEach(function (img, i) {
      var tab = stackdoTabs[i];
      if (!tab) return;
      img.addEventListener("mouseenter", function () { tab.classList.add("is-hovered"); });
      img.addEventListener("mouseleave", function () { tab.classList.remove("is-hovered"); });
    });
  }

  // (2026-09-03) 클로드 디자인 핸드오프(handoff_megamenu) 적용 — 메가메뉴:
  // 서브메뉴 항목에 마우스를 올리면 슬라이딩 하이라이트 필이 그 항목
  // 위치/높이로 이동하고, 미리보기 이미지·우측 설명이 함께 크로스페이드로
  // 갱신된다(각 대메뉴 패널마다 독립적으로 동작).
  document.querySelectorAll(".megamenu").forEach(function (menu) {
    var items = Array.prototype.slice.call(menu.querySelectorAll(".megamenu-index-item"));
    var highlight = menu.querySelector(".megamenu-index-highlight");
    var previewImg = menu.querySelector(".megamenu-preview-img");
    var detail = menu.querySelector(".megamenu-detail");
    var detailTitle = menu.querySelector(".megamenu-detail-title");
    var detailDesc = menu.querySelector(".megamenu-detail-desc");
    var detailLink = menu.querySelector(".megamenu-detail-link");
    var switchTimer = null;
    var moveHighlight = function (li) {
      if (!highlight) return;
      highlight.style.top = li.offsetTop + "px";
      highlight.style.height = li.offsetHeight + "px";
      highlight.style.opacity = "1";
    };
    var selectItem = function (item, a) {
      items.forEach(function (it) { it.classList.remove("is-active"); });
      item.classList.add("is-active");
      moveHighlight(item);
      var label = a.textContent.replace(/\s+$/, "");
      var desc = a.getAttribute("data-desc") || "";
      var href = a.getAttribute("href");
      var imgUrl = a.getAttribute("data-img");
      if (previewImg) {
        if (imgUrl) {
          // 새 배경 레이어를 만들어 살짝 확대된 상태에서 즉시 스케일+페이드로
          // "팝인"시키고, 이전 레이어는 제거 — setTimeout으로 페이드아웃을
          // 기다리지 않아 반응이 즉각적으로 느껴진다.
          previewImg.classList.remove("img-ph");
          previewImg.style.color = "";
          var oldBgs = previewImg.querySelectorAll(".megamenu-preview-img-bg");
          var bg = document.createElement("div");
          bg.className = "megamenu-preview-img-bg";
          bg.style.backgroundImage = "url('" + imgUrl + "')";
          previewImg.appendChild(bg);
          window.requestAnimationFrame(function () {
            bg.classList.add("is-shown");
          });
          oldBgs.forEach(function (old) { old.remove(); });
        } else {
          previewImg.innerHTML = "";
          previewImg.textContent = label;
          previewImg.classList.add("img-ph");
        }
      }
      if (detail) detail.classList.add("is-fading");
      window.clearTimeout(switchTimer);
      switchTimer = window.setTimeout(function () {
        if (detailTitle) detailTitle.textContent = label;
        if (detailDesc) detailDesc.textContent = desc;
        if (detailLink) detailLink.setAttribute("href", href);
        if (detail) detail.classList.remove("is-fading");
      }, 60);
    };
    items.forEach(function (item) {
      var a = item.querySelector("a");
      if (!a) return;
      item.addEventListener("mouseenter", function () { selectItem(item, a); });
    });
    var activeItem = menu.querySelector(".megamenu-index-item.is-active") || items[0];
    // 하이라이트 필의 최초 위치를 페이지 로드 시 한 번 계산해둔다(패널이
    // opacity:0으로 숨겨져 있을 뿐 display:none은 아니므로 레이아웃 치수는
    // 이미 읽을 수 있음). li의 mouseenter에 걸면 서브메뉴 항목 자신의
    // mouseenter가 버블링되어 매번 활성 항목으로 되돌리는 버그가 있어 제거.
    if (activeItem) moveHighlight(activeItem);
    window.addEventListener("resize", function () {
      var current = menu.querySelector(".megamenu-index-item.is-active");
      if (current) moveHighlight(current);
    });
  });

  // ---------------------------------------------------------------------
  // 서브페이지 패럴랙스 히어로 + 스크롤 블러 (2026-09-04 v2 프로토타입)
  // .subhero-parallax가 있는 페이지에서만 동작(없으면 즉시 종료). 이미지에
  // 위아래 160px 버퍼(assets/css/style.css의 .subhero-parallax-img
  // top:-80px / height:calc(100% + 160px)와 반드시 일치)를 깔아두고, 그
  // 버퍼 안에서만 이동시켜 가장자리가 비는 문제 없이 "본문보다 느리게
  // 움직이는" 패럴랙스를 구현. 동시에 스크롤 진행률(0~1)에 비례해 이미지
  // blur를 키워 방문자 시선이 자연스럽게 본문으로 옮겨가도록 유도한다.
  // ---------------------------------------------------------------------
  var subheroStage = document.querySelector(".subhero-parallax");
  if (subheroStage) {
    var subheroImg = subheroStage.querySelector(".subhero-parallax-img");
    // (2026-09-04 v4) 680px는 이미지 확대율이 너무 커져 "사진이 답답하게
    // 확대돼 보인다"는 피드백 — 버퍼가 클수록 object-fit:cover 확대율도
    // 함께 커지는 구조라, 확대감이 무리 없는 420px로 되돌림(css
    // .subhero-parallax-img의 top/height 버퍼값과 반드시 일치시킬 것).
    var SUBHERO_BUFFER = 420; // px — CSS 버퍼량과 반드시 일치시킬 것
    var SUBHERO_BLUR_MAX = 10; // px
    var subheroTicking = false;

    var updateSubhero = function () {
      subheroTicking = false;
      var rect = subheroStage.getBoundingClientRect();
      var stageHeight = subheroStage.offsetHeight || 1;
      var scrolled = Math.min(Math.max(-rect.top, 0), stageHeight);
      var progress = scrolled / stageHeight;
      var shift = progress * SUBHERO_BUFFER - SUBHERO_BUFFER / 2;
      subheroImg.style.transform = "translate3d(0, " + shift.toFixed(1) + "px, 0)";
      subheroImg.style.filter = "blur(" + (progress * SUBHERO_BLUR_MAX).toFixed(2) + "px)";
    };
    var onSubheroScroll = function () {
      if (!subheroTicking) {
        subheroTicking = true;
        requestAnimationFrame(updateSubhero);
      }
    };
    window.addEventListener("scroll", onSubheroScroll, { passive: true });
    window.addEventListener("resize", onSubheroScroll);
    updateSubhero();
  }
});
