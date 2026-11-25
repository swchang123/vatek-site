/* 기술 및 서비스 역량(company/capability.html) #network: 세 항목을 차례로 강조하고, 지도(global-network.js)에서 그 항목에 해당하는 연결만 밝힌다.
   knowledge = 각국 사이의 교류(가까운 곳끼리 잇는 선), engineering = 바테크와 Cold Jet을 잇는 선, service = 지역 본부에서 각 지점으로 가는 공급선.
   스크립트가 없으면 세 항목과 지도가 그대로 보인다. */
(function () {
  var sec = document.getElementById('network'); if (!sec) return;
  var items = sec.querySelectorAll('.cap-net-item'), map = sec.querySelector('.cap-map');
  if (!items.length || !map) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cur = -1, timer = 0, held = false, inView = false, started = false, STEP = 4600;
  function show(i) {
    cur = (i + items.length) % items.length;
    for (var k = 0; k < items.length; k++) items[k].classList.toggle('is-on', k === cur);
    map.setAttribute('data-focus', items[cur].getAttribute('data-focus'));
  }
  function play() { clearTimeout(timer); if (!started || held || !inView || reduce) return; timer = setTimeout(function () { show(cur + 1); play(); }, STEP); }
  Array.prototype.forEach.call(items, function (it, i) {
    it.addEventListener('mouseenter', function () { held = true; started = true; show(i); play(); });
    it.addEventListener('mouseleave', function () { held = false; play(); });
    it.addEventListener('click', function () { started = true; show(i); play(); });
  });
  function begin() { if (started) return; started = true; show(0); play(); }
  if (window.IntersectionObserver) {
    var first = true;
    new IntersectionObserver(function (es) {
      inView = es[0].isIntersecting;
      if (inView && first) { first = false; setTimeout(begin, reduce ? 0 : 3400); } // 연결망이 다 그려진 뒤에 시작한다
      play();
    }, { threshold: .25 }).observe(map);
  } else { inView = true; begin(); }
})();
