/* 기술 및 서비스 역량(company/capability.html)의 접이식 목록: 자주 묻는 질문과 같은 방식으로 높이를 부드럽게 여닫는다.
   스크립트가 없으면 <details> 기본 동작으로 그대로 여닫힌다. */
(function () {
  var lists = document.querySelectorAll('.cap-acc');
  if (!lists.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  Array.prototype.forEach.call(lists, function (list) {
    list.classList.add('is-js');
    Array.prototype.forEach.call(list.querySelectorAll('details'), function (item) {
      var summary = item.querySelector('summary'), panel = item.querySelector('.cap-acc-a');
      if (!summary || !panel) return;
      var animating = false;
      if (item.hasAttribute('open')) { item.classList.add('is-open'); panel.style.height = 'auto'; }
      summary.addEventListener('click', function (e) {
        e.preventDefault();
        if (animating) return;
        var opening = !item.hasAttribute('open');
        if (reduce) { // 움직임 줄이기: 바로 여닫는다
          if (opening) { item.setAttribute('open', ''); item.classList.add('is-open'); panel.style.height = 'auto'; }
          else { item.classList.remove('is-open'); panel.style.height = '0px'; item.removeAttribute('open'); }
          return;
        }
        animating = true;
        var finish = function (after) {
          var done = false, end = function (ev) { if (ev && ev.propertyName !== 'height') return; if (done) return; done = true; panel.removeEventListener('transitionend', end); after(); animating = false; };
          panel.addEventListener('transitionend', end); setTimeout(function () { end(); }, 500); // 전환 끝 신호가 오지 않아도 멈추지 않게
        };
        if (opening) {
          item.setAttribute('open', ''); item.classList.add('is-open');
          panel.style.height = '0px';
          requestAnimationFrame(function () { panel.style.height = panel.scrollHeight + 'px'; });
          finish(function () { panel.style.height = 'auto'; });
        } else {
          panel.style.height = panel.scrollHeight + 'px';
          item.classList.remove('is-open');
          requestAnimationFrame(function () { requestAnimationFrame(function () { panel.style.height = '0px'; }); });
          finish(function () { item.removeAttribute('open'); });
        }
      });
    });
  });
})();
