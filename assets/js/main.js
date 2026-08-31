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

  // 홈 "우리의 능력": 숫자가 화면에 들어올 때마다 0에서 목표값까지 다시 카운트업.
  // (사용자 요청: "스크롤로 사라졌다가 다시 돌아오면 숫자가 또 다시 카운트 되었으면
  // 좋겠어") — 기존에는 IntersectionObserver.unobserve()로 최초 1회만 실행했으나,
  // 화면을 벗어날 때(entry.isIntersecting === false) 0으로 리셋하고 계속 observe를
  // 유지해 재진입 시마다 다시 실행되도록 변경. 같은 요소가 짧은 시간 안에 여러 번
  // 드나들 때 이전 tick 루프와 새 tick 루프가 겹쳐 값이 튀는 것을 막기 위해 요소마다
  // "실행 세대(runId)"를 두어, tick이 자기 세대가 최신일 때만 화면에 반영하도록 함.
  // (후속69) "우리의 가치" 재설계로 .value-stats의 카운트업 숫자는 더 이상
  // 화면에 "들어올 때마다"가 아니라 "자신이 속한 .value-block이 처음 포커스될
  // 때 1회"만 실행되어야 함(data-count-on-focus 속성으로 표시) — 아래
  // valueBlocks IntersectionObserver가 이 요소들을 직접 담당하므로, 여기
  // 일반 스크롤-진입 카운트업 대상에서는 제외.
  var countUpEls = document.querySelectorAll(".count-up:not([data-count-on-focus])");
  if (countUpEls.length && "IntersectionObserver" in window) {
    var countUpRunId = new WeakMap();
    var countUpResetText = new WeakMap();
    var runCountUp = function (el) {
      var target = parseInt(el.getAttribute("data-target"), 10) || 0;
      var prefix = el.getAttribute("data-prefix") || "";
      // (후속59) "1986 등 숫자도 위와 같이 카운트 되게 해줘" — "우리의 능력"
      // 하이라이트(1986/20개+/14개/3개)에도 카운트업을 적용하면서, 숫자 뒤에
      // "개"/"개+" 같은 단위가 붙는 경우를 위해 data-suffix(접미사)도 지원.
      var suffix = el.getAttribute("data-suffix") || "";
      if (prefersReducedMotion) {
        el.textContent = prefix + target + suffix;
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
        el.textContent = prefix + value + suffix;
        if (progress < 1) window.requestAnimationFrame(tick);
      };
      window.requestAnimationFrame(tick);
    };
    countUpEls.forEach(function (el) {
      // 리셋 시 표시할 "0" 텍스트(prefix/suffix 포함)를 최초 마크업 기준으로 미리 기억
      var prefix = el.getAttribute("data-prefix") || "";
      var suffix = el.getAttribute("data-suffix") || "";
      countUpResetText.set(el, prefix + "0" + suffix);
    });
    // (후속69) data-count-on-focus 요소(.value-stats)는 위 countUpEls에서
    // 제외되어 있지만, runCountUp()·countUpResetText는 아래 valueBlocks
    // 블록(같은 함수 스코프, var 호이스팅으로 이 시점 이후에도 접근 가능)에서
    // 그대로 재사용하므로 리셋용 "0" 텍스트만 여기서 동일하게 미리 기억해둠.
    document.querySelectorAll(".count-up[data-count-on-focus]").forEach(function (el) {
      var prefix = el.getAttribute("data-prefix") || "";
      var suffix = el.getAttribute("data-suffix") || "";
      countUpResetText.set(el, prefix + "0" + suffix);
    });
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

  // (후속69) "우리의 가치" 재설계: 구 .ability-pin(100vh 풀-락, CSS만으로 구현,
  // 별도 JS 불필요)을 .section-value(.value-block 4개 + IntersectionObserver
  // 기반 포커스/톤 전환)로 교체. 아래 블록이 그 동작을 전담한다.
  var valueBlocks = document.querySelectorAll(".value-block");
  if (valueBlocks.length && "IntersectionObserver" in window) {
    var valueContent = document.querySelector(".value-content");
    var valueRatios = new WeakMap();
    var applyValueFocus = function () {
      var focused = null;
      var best = -1;
      valueBlocks.forEach(function (block) {
        var ratio = valueRatios.get(block) || 0;
        if (ratio > best) {
          best = ratio;
          focused = block;
        }
      });
      valueBlocks.forEach(function (block) {
        block.classList.toggle("is-focused", block === focused && best > 0);
      });
      if (focused && best > 0 && valueContent) {
        var tone = focused.getAttribute("data-tone");
        if (tone) valueContent.style.backgroundColor = tone;
      }
    };
    var valueObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var block = entry.target;
          valueRatios.set(block, entry.intersectionRatio);
          // data-count-on-focus 카운트업: 블록이 처음 화면에 걸리는 순간
          // (intersectionRatio > 0) 1회 실행하고(el.dataset.counted로 재실행
          // 방지), 화면 밖으로 완전히 벗어나(intersectionRatio === 0) 다시
          // 들어올 때를 대비해 그때만 "0"으로 리셋 — runCountUp()과
          // countUpResetText는 위 count-up 블록에서 이미 정의됨(var 호이스팅).
          // (버그 수정) 블록 하나(.value-stats)에 카운트업 숫자가 4개 있을 수
          // 있어 querySelector(단수)가 아니라 querySelectorAll로 전부 순회해야 함
          // — querySelector만 쓰면 첫 번째 숫자만 카운트되고 나머지 3개는
          // "0"에 멈춰있는 회귀가 있었음(Playwright로 확인 후 수정).
          block.querySelectorAll(".count-up[data-count-on-focus]").forEach(function (countEl) {
            if (entry.intersectionRatio > 0 && !countEl.dataset.counted) {
              countEl.dataset.counted = "1";
              runCountUp(countEl);
            } else if (entry.intersectionRatio === 0 && countEl.dataset.counted) {
              delete countEl.dataset.counted;
              if (!prefersReducedMotion) {
                countEl.textContent = countUpResetText.get(countEl) || "0";
              }
            }
          });
        });
        applyValueFocus();
      },
      { threshold: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] }
    );
    valueBlocks.forEach(function (block) {
      valueRatios.set(block, 0);
      valueObserver.observe(block);
    });
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
