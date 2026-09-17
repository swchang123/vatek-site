/* VATEK RESOURCES — 목록 렌더러 · 검색 (cases/*.html). 카드 클릭은 본문 페이지로 이동
   (detail.html?id= / watch.html?id=) — 팝업 없음. */
(function () {
  var root = document.getElementById('resRoot'); if (!root || !window.VATEK_RESOURCES) return;
  var type = root.getAttribute('data-type');
  var items = (window.VATEK_RESOURCES[type] || []).slice().sort(function (a, b) { return a.date < b.date ? 1 : -1; });
  var grid = document.getElementById('resGrid'), count = document.getElementById('resCount'), empty = document.getElementById('resEmpty');
  var search = document.getElementById('resSearch'), resetBtn = document.getElementById('resReset');
  var q = '';

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fmtDate(d) { var p = d.split('-'); return p[0] + '.' + p[1] + '.' + p[2]; }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function yt(id) { return 'https://i.ytimg.com/vi/' + id + '/hqdefault.jpg'; }

  if (search) search.addEventListener('input', function () { q = search.value.trim().toLowerCase(); render(); });
  if (resetBtn) resetBtn.addEventListener('click', function () { q = ''; if (search) search.value = ''; render(); });

  function matches(it) {
    if (!q) return true;
    var hay = [it.title, it.excerpt, it.industry, it.equipment, it.application, it.category, it.type, it.speaker, it.client].join(' ').toLowerCase();
    return hay.indexOf(q) >= 0;
  }

  function card(it, i) {
    var num = '<span class="res-num">' + pad(items.indexOf(it) + 1) + '</span>';
    var d = '<time datetime="' + it.date + '">' + fmtDate(it.date) + '</time>';
    if (type === 'cases') {
      var href = 'detail.html?id=' + encodeURIComponent(it.id);
      return '<article class="res-card is-case reveal" style="--reveal-delay:' + (i % 3) * 0.06 + 's" data-id="' + it.id + '">' +
        '<a class="res-thumb" href="' + href + '"><img src="' + it.img + '" alt="" loading="lazy" decoding="async" /><span class="res-tag">' + esc(it.industry) + '</span></a>' +
        '<div class="res-body">' + num + '<div class="res-meta">' + d + '<i></i><span>' + esc(it.equipment) + '</span></div>' +
        '<h3><a href="' + href + '">' + esc(it.title) + '</a></h3><p>' + esc(it.excerpt) + '</p>' +
        '<dl class="res-stats">' + it.stats.map(function (s) { return '<div><dt>' + esc(s.k) + '</dt><dd>' + esc(s.v) + '</dd></div>'; }).join('') + '</dl>' +
        '<a class="res-more" href="' + href + '">케이스 스터디 읽기 <span>→</span></a></div></article>';
    }
    if (type === 'videos' || type === 'webinars') {
      var vhref = 'watch.html?id=' + encodeURIComponent(it.id);
      var sub = type === 'videos' ? esc(it.category) : (it.status === 'upcoming' ? '예정' : '다시 보기');
      var meta = type === 'videos' ? d + '<i></i><span>' + esc(it.industry) + '</span>' : d + '<i></i><span>' + esc(it.speaker) + '</span>';
      var extra = type === 'webinars' ? '<div class="res-webmeta"><span>' + esc(it.duration) + '</span><span>' + esc(it.lang) + '</span><span>' + esc(it.industry) + '</span></div>' : '';
      return '<article class="res-card is-video reveal" style="--reveal-delay:' + (i % 3) * 0.06 + 's" data-id="' + it.id + '">' +
        '<a class="res-thumb" href="' + vhref + '" aria-label="보기: ' + esc(it.title) + '"><img src="' + yt(it.youtube) + '" alt="" loading="lazy" decoding="async" /><span class="res-play" aria-hidden="true"></span><span class="res-tag">' + sub + '</span>' + (type === 'videos' ? '<span class="res-dur">' + esc(it.duration) + '</span>' : '') + '</a>' +
        '<div class="res-body">' + num + '<div class="res-meta">' + meta + '</div>' +
        '<h3><a href="' + vhref + '">' + esc(it.title) + '</a></h3><p>' + esc(it.excerpt) + '</p>' + extra +
        '<a class="res-more" href="' + vhref + '">' + (type === 'videos' ? '영상 보기' : '웹세미나 다시 보기') + ' <span>→</span></a></div></article>';
    }
    /* technical */
    return '<article class="res-card is-doc reveal" style="--reveal-delay:' + (i % 3) * 0.06 + 's" data-id="' + it.id + '">' +
      '<a class="res-thumb" href="' + it.link + '"><img src="' + it.img + '" alt="" loading="lazy" decoding="async" /><span class="res-tag">' + esc(it.type) + '</span><span class="res-dur">' + esc(it.format) + '</span></a>' +
      '<div class="res-body">' + num + '<div class="res-meta">' + d + '<i></i><span>' + esc(it.industry) + '</span></div>' +
      '<h3><a href="' + it.link + '">' + esc(it.title) + '</a></h3><p>' + esc(it.excerpt) + '</p>' +
      '<a class="res-more" href="' + it.link + '">' + esc(it.cta || '자료 보기') + ' <span>→</span></a></div></article>';
  }

  function render() {
    var list = items.filter(matches);
    grid.innerHTML = list.map(card).join('');
    if (count) count.innerHTML = '<b>' + pad(list.length) + '</b> / ' + pad(items.length);
    if (empty) empty.hidden = list.length > 0;
    grid.querySelectorAll('.reveal').forEach(function (el) { requestAnimationFrame(function () { el.classList.add('is-visible', 'in-view'); }); });
  }

  render();
})();
