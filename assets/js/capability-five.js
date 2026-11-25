/* 기술 및 서비스 역량(company/capability.html) #five: 오각형 그림과 다섯 항목 목록을 함께 움직인다.
   그림의 점이나 이름, 목록의 제목을 누르면 그 항목이 선택되어 설명이 펼쳐지고(자주 묻는 질문과 같은 높이 전환), 가만히 두면 차례로 넘어간다.
   마우스를 올려 두면 멈추고, 직접 고른 뒤에는 읽을 시간을 더 준 다음 다시 넘어간다.
   목록 높이는 가장 긴 설명에 맞춰 잡아 두어, 항목이 바뀌어도 아래 내용이 오르내리지 않는다. 스크립트가 없으면 다섯 설명이 모두 펼쳐져 보인다. */
(function () {
  var root = document.querySelector('[data-five]'); if (!root) return;
  var list = root.querySelector('.cap-five-list'), items = root.querySelectorAll('.cap-five-item');
  var labels = root.querySelectorAll('.cap-five-pt'), dots = root.querySelectorAll('.pt'), beams = root.querySelectorAll('.beam'), kites = root.querySelectorAll('.kite');
  if (!list || !items.length) return;
  var each = function (nodes, fn) { Array.prototype.forEach.call(nodes, fn); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cur = -1, timer = 0, held = false, inView = false, started = false, STEP = 6000, HOLD = 13000, wait = STEP, moving = false, settle = 0;
  root.classList.add('is-js');
  function panel(i) { return items[i].querySelector('.cap-five-a'); }
  function inner(i) { return panel(i).firstElementChild.getBoundingClientRect().height; } // 설명 내용의 실제 높이(소수점까지)
  function fit() { // 펼쳐진 설명의 높이와 목록 전체의 최소 높이를 다시 잰다
    var heads = 0, max = 0;
    each(items, function (it, k) {
      var h = inner(k); if (h > max) max = h;
      heads += it.getBoundingClientRect().height - panel(k).getBoundingClientRect().height;
      if (k === cur && !moving) panel(k).style.height = h + 'px';
    });
    list.style.minHeight = Math.ceil(heads + max) + 'px';
  }
  function show(i) {
    cur = (i + items.length) % items.length;
    moving = true; clearTimeout(settle); settle = setTimeout(function () { moving = false; }, 450); // 여닫는 동안에는 높이를 다시 재지 않는다
    each(items, function (it, k) {
      var on = k === cur;
      it.classList.toggle('is-on', on);
      it.querySelector('.cap-five-q').setAttribute('aria-expanded', on ? 'true' : 'false');
      panel(k).style.height = (on ? inner(k) : 0) + 'px';
    });
    [labels, dots, beams, kites].forEach(function (set) { each(set, function (el, k) { el.classList.toggle('is-on', k === cur); }); });
  }
  function play() { clearTimeout(timer); if (!started || held || !inView || reduce) return; timer = setTimeout(function () { wait = STEP; show(cur + 1); play(); }, wait); }
  function pick(i) { started = true; wait = HOLD; show(i); play(); }
  each(items, function (it, i) { it.querySelector('.cap-five-q').addEventListener('click', function () { pick(i); }); });
  [labels, dots].forEach(function (set) {
    each(set, function (el, i) {
      el.addEventListener('click', function () { pick(i); });
      el.addEventListener('mouseenter', function () { if (root.classList.contains('is-ready')) show(i); });
    });
  });
  root.addEventListener('mouseenter', function () { held = true; play(); });
  root.addEventListener('mouseleave', function () { held = false; play(); });
  show(0); fit();
  window.addEventListener('resize', fit);
  window.addEventListener('load', fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  if (window.ResizeObserver) { var ro = new ResizeObserver(fit); each(items, function (it, k) { ro.observe(panel(k).firstElementChild); }); } // 글꼴이 늦게 바뀌어 줄 수가 달라져도 높이를 맞춘다
  function enter() { // 그림을 펼친 다음 첫 항목 표시와 자동 넘김을 시작한다
    root.classList.add('is-in');
    setTimeout(function () { root.classList.add('is-ready'); started = true; play(); }, reduce ? 0 : 1100);
  }
  if (window.IntersectionObserver) {
    var first = true;
    new IntersectionObserver(function (es) {
      inView = es[0].isIntersecting;
      if (inView && first) { first = false; enter(); }
      play();
    }, { threshold: .3 }).observe(root);
  } else { inView = true; enter(); }
})();
