document.addEventListener("DOMContentLoaded", function () {
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
      if (li.querySelector(".dropdown") && window.innerWidth <= 960) {
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

    var smoothScrollLoop = function () {
      var diff = smoothTarget - smoothCurrent;
      if (Math.abs(diff) < 0.5) {
        smoothCurrent = smoothTarget;
      } else {
        smoothCurrent += diff * SMOOTH_EASE;
      }
      window.scrollTo(0, smoothCurrent);
      if (smoothCurrent !== smoothTarget) {
        smoothRaf = window.requestAnimationFrame(smoothScrollLoop);
      } else {
        smoothRaf = null;
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
        var deltaY = e.deltaY;
        if (e.deltaMode === 1) {
          deltaY *= 16; // line → px 근사치
        } else if (e.deltaMode === 2) {
          deltaY *= window.innerHeight; // page → px
        }
        e.preventDefault();
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
    window.addEventListener(
      "scroll",
      function () {
        if (smoothRaf === null) {
          smoothCurrent = window.scrollY;
          smoothTarget = window.scrollY;
        }
      },
      { passive: true }
    );
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
        if (currentY <= 8) {
          header.classList.remove("nav-hidden");
        } else if (currentY < lastScrollY) {
          // 위로 스크롤할 때만 다시 나타남
          header.classList.remove("nav-hidden");
        } else if (currentY > lastScrollY) {
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
    // (후속82) "우리의 신념" 제목 바로 아래 CO2 영상 — 제목이 틀고정되는
    // 순간 영상도 함께 틀고정(position:sticky)되고, 그 안의 텍스트 박스는
    // 이후 스크롤에 따라 숨김→중앙 정지→위로 퇴장의 3단계로 움직인다.
    // 아래 applyValueFocus()에서 매 프레임 계산.
    var beliefVideoScroll = document.querySelector(".belief-video-scroll");
    var beliefVideoWrap = beliefVideoScroll
      ? beliefVideoScroll.querySelector(".belief-video-wrap")
      : null;
    var beliefVideoBox = beliefVideoWrap
      ? beliefVideoWrap.querySelector(".belief-video-box")
      : null;

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
      if (valuePinTitleEl) {
        valuePinTitleEl.classList.toggle("is-pinned", valuePinTitleEl.getBoundingClientRect().top <= 0);
      }
      var beliefTitlePinned = beliefPinTitleEl
        ? beliefPinTitleEl.getBoundingClientRect().top <= 0
        : false;
      if (beliefPinTitleEl) {
        beliefPinTitleEl.classList.toggle("is-pinned", beliefTitlePinned);
      }
      // (후속82) 영상(.belief-video-wrap)은 top:제목 실측 높이로 sticky —
      // .belief-pin-title(top:0)과 .belief-video-wrap(top:제목높이)은 같은
      // 부모 흐름 안에 여백 없이 붙어 있어 수학적으로 항상 같은 스크롤
      // 위치에서 동시에 stuck되므로, 제목의 is-pinned 판정을 그대로 재사용.
      if (beliefVideoWrap) {
        if (beliefPinTitleEl) {
          beliefVideoWrap.style.top = beliefPinTitleEl.getBoundingClientRect().height + "px";
        }
        beliefVideoWrap.classList.toggle("is-pinned", beliefTitlePinned);
      }
      // (후속82 계속) 영상이 틀고정된 뒤 추가로 스크롤되는 여유 구간
      // (.belief-video-scroll, .stackdo-scroll과 동일한 "100vh + N*Xvh" 공식)의
      // 진행률을 3구간(0:숨김/1:중앙 정지/2:퇴장)으로 나눠 텍스트 박스에
      // 반영 — "한 번 더 스크롤"할 때마다 다음 구간으로 넘어가는 계단식
      // 연출이 되도록 각 구간에 65vh의 스크롤 여유를 둔다.
      if (beliefVideoScroll && beliefVideoBox) {
        var beliefScrollRect = beliefVideoScroll.getBoundingClientRect();
        var beliefTotal = beliefScrollRect.height - vh;
        var beliefScrolled = -beliefScrollRect.top;
        var beliefProgress = beliefTotal > 0
          ? Math.min(1, Math.max(0, beliefScrolled / beliefTotal))
          : 0;
        var beliefZones = 3;
        var beliefIdx = beliefProgress > 0
          ? Math.min(beliefZones - 1, Math.floor(beliefProgress * beliefZones))
          : 0;
        beliefVideoBox.classList.toggle("is-risen", beliefIdx >= 1);
        beliefVideoBox.classList.toggle("is-exited", beliefIdx >= 2);
      }
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

  // 스크롤 리빌 애니메이션 (후속61, 첫 페이지 정적 섹션 전용): 뷰포트에 들어오면
  // .reveal/.reveal-scale/.reveal-pop 요소에 is-visible을 붙여 CSS 트랜지션으로
  // 나타나게 함. 카운트업과 달리 1회성 연출이므로 재생 뒤 관련 클래스를 전부
  // 제거해 :hover 등 요소 자체의 transform과 충돌하지 않도록 정리한다.
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
    var stackdoZones = stackdoPanels.length + 1;
    var stackdoGallery = document.getElementById("stackdoGallery");
    var stackdoFrame = stackdoScroll.querySelector(".stackdo-frame");
    var updateStackdo = function () {
      stackdoTicking = false;
      var rect = stackdoScroll.getBoundingClientRect();
      if (stackdoFrame) stackdoFrame.classList.toggle("is-pinned", rect.top <= 0);
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
        if (stackdoFrame) stackdoFrame.classList.toggle("is-gallery", idx >= stackdoPanels.length);
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
          stackdoGallery.classList.toggle("is-shown", idx >= stackdoPanels.length);
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
});
