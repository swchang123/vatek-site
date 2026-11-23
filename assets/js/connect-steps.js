/* Cold Jet CONNECT QR 5단계 (support/education.html #connect). 스크립트가 없으면 다섯 단계가 목록으로 모두 보인다. */
(function () {
  var root = document.querySelector('[data-qr-steps]');
  if (!root) return;
  var imgs = root.querySelectorAll('.edu-qr-media img'), panels = root.querySelectorAll('.edu-qr-stage > li');
  var bars = root.querySelectorAll('.edu-qr-bar i'), thumbs = root.querySelector('.edu-qr-thumbs');
  var tabs = thumbs ? thumbs.querySelectorAll('button') : [];
  var n = panels.length, cur = 0, timer = 0, auto = true, inView = false, held = false, STEP = 4500;
  if (!n || tabs.length !== n) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) auto = false;
  for (var k = 0; k < imgs.length; k++) { imgs[k].loading = 'eager'; } // 겹쳐 둔 사진은 바뀔 때 바로 보이도록 미리 받는다
  thumbs.hidden = false; root.classList.add('is-js');

  function show(i) {
    cur = (i + n) % n;
    for (var j = 0; j < n; j++) {
      var on = j === cur;
      if (imgs[j]) imgs[j].classList.toggle('is-on', on);
      panels[j].classList.toggle('is-on', on);
      tabs[j].classList.toggle('is-on', on); tabs[j].setAttribute('aria-pressed', on ? 'true' : 'false');
      if (bars[j]) { bars[j].classList.toggle('is-done', j < cur); bars[j].classList.remove('is-on'); }
    }
    if (bars[cur]) { void bars[cur].offsetWidth; bars[cur].classList.add('is-on'); } // 진행 막대를 처음부터 다시 채운다
  }
  function play() { clearTimeout(timer); root.classList.toggle('is-auto', auto && inView && !held); if (auto && inView && !held) timer = setTimeout(function () { show(cur + 1); play(); }, STEP); }
  for (var i = 0; i < n; i++) (function (idx) {
    tabs[idx].addEventListener('click', function () { auto = false; show(idx); play(); }); // 직접 고르면 자동 넘김을 멈춘다
  })(i);
  root.addEventListener('mouseenter', function () { held = true; play(); });
  root.addEventListener('mouseleave', function () { held = false; if (auto) show(cur); play(); });
  root.addEventListener('focusin', function () { held = true; play(); });
  root.addEventListener('focusout', function () { held = false; play(); });
  show(0);
  if (window.IntersectionObserver) new IntersectionObserver(function (es) { inView = es[0].isIntersecting; if (inView && auto) show(cur); play(); }, { threshold: .35 }).observe(root);
})();
