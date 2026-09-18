/* VATEK RESOURCES — 상세 페이지 렌더러 (cases/detail.html, cases/watch.html).
   URL의 ?id= 로 window.VATEK_RESOURCES에서 항목을 찾아 본문에 채운다. */
(function () {
  var D = window.VATEK_RESOURCES; if (!D) return;
  var root = document.getElementById('detailRoot'); if (!root) return;
  var id = new URLSearchParams(location.search).get('id');
  var isWatch = /watch\.html$/.test(location.pathname);
  var crumbTitle = document.getElementById('crumbTitle');
  var related = document.getElementById('relatedGrid');

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fmtDate(d) { var p = d.split('-'); return p[0] + '.' + p[1] + '.' + p[2]; }

  if (!isWatch) {
    var it = (D.cases || []).filter(function (x) { return x.id === id; })[0];
    if (!it) { location.href = 'case-studies.html'; return; }
    document.title = it.title + ' | VATEK';
    if (crumbTitle) crumbTitle.textContent = it.title;
    root.innerHTML = '<div class="rda-hero"><img src="' + it.img + '" alt="" /></div>' +
      '<div class="rda-head"><span class="res-eyebrow">CASE STUDY · ' + esc(it.industry) + '</span><h1>' + esc(it.title) + '</h1>' +
      '<div class="rda-byline"><span>고객 <b>' + esc(it.client) + '</b></span><span>장비 <b>' + esc(it.equipment) + '</b></span><span>작업 <b>' + esc(it.application) + '</b></span><span>게시 <b>' + fmtDate(it.date) + '</b></span></div></div>' +
      '<dl class="rda-stats">' + it.stats.map(function (s) { return '<div><dt>' + esc(s.k) + '</dt><dd>' + esc(s.v) + '</dd></div>'; }).join('') + '</dl>' +
      it.body.map(function (b) { return '<section class="rda-sec"><h3>' + esc(b[0]) + '</h3><p>' + esc(b[1]) + '</p></section>'; }).join('') +
      '<div class="rda-cta"><a class="cta-btn" href="../products/quote.html">비슷한 현장, 상담 요청</a><a class="res-ghost" href="../rental/demo.html">데모 테스트 신청 →</a></div>';
    if (related) {
      var rel = it.related || {}, cards = [];
      (rel.videos || []).slice(0, 1).forEach(function (vid) {
        var v = (D.videos || []).concat(D.webinars || []).filter(function (x) { return x.id === vid; })[0]; if (!v) return;
        cards.push('<a class="res-link-card reveal" href="watch.html?id=' + encodeURIComponent(v.id) + '"><div class="res-link-media"><img src="https://i.ytimg.com/vi/' + v.youtube + '/hqdefault.jpg" alt="" loading="lazy" /><span class="res-play" aria-hidden="true"></span><span class="res-tag">' + esc(v.duration || '') + '</span></div><div class="res-link-body"><small>VIDEO · ' + esc(v.category || v.industry || '') + '</small><b>' + esc(v.title) + '</b><span>' + esc(v.excerpt) + '</span><i>영상 보기 →</i></div></a>');
      });
      if (rel.industry) cards.push('<a class="res-link-card reveal" href="' + rel.industry.href + '" style="--reveal-delay:0.06s"><div class="res-link-media"><img src="' + rel.industry.img + '" alt="" loading="lazy" /></div><div class="res-link-body"><small>INDUSTRY SOLUTION</small><b>' + esc(rel.industry.label) + '</b><span>' + esc(rel.industry.desc) + '</span><i>산업별 솔루션 보기 →</i></div></a>');
      if (rel.task) cards.push('<a class="res-link-card reveal" href="' + rel.task.href + '" style="--reveal-delay:0.12s"><div class="res-link-media"><img src="' + rel.task.img + '" alt="" loading="lazy" /></div><div class="res-link-body"><small>APPLICATION</small><b>' + esc(rel.task.label) + '</b><span>' + esc(rel.task.desc) + '</span><i>작업별 솔루션 보기 →</i></div></a>');
      if (!cards.length) {
        (D.cases || []).filter(function (x) { return x.id !== it.id; }).slice(0, 3).forEach(function (o) { cards.push('<a class="res-cross-card reveal" href="detail.html?id=' + encodeURIComponent(o.id) + '"><small>' + esc(o.industry) + '</small><b>' + esc(o.title) + '</b><span>' + esc(o.excerpt) + '</span></a>'); });
      }
      related.innerHTML = cards.join('');
      related.querySelectorAll('.reveal').forEach(function (el) { requestAnimationFrame(function () { el.classList.add('is-visible'); }); });
      var lead = document.getElementById('relatedLead'); if (lead) lead.textContent = it.industry + ' 현장과 ' + it.application + ' 작업에 해당하는 영상과 솔루션을 골라 두었습니다.';
    }
    return;
  }

  var kind = (D.videos || []).some(function (x) { return x.id === id; }) ? 'videos' : 'webinars';
  var vt = (D[kind] || []).filter(function (x) { return x.id === id; })[0];
  if (!vt) { location.href = 'videos.html'; return; }
  document.title = vt.title + ' | VATEK';
  if (crumbTitle) crumbTitle.textContent = vt.title;
  var crumbParent = document.getElementById('crumbParent');
  if (crumbParent) crumbParent.innerHTML = '<a href="' + kind + '.html">' + (kind === 'videos' ? '동영상 보기' : '웹세미나') + '</a>';
  var metaBits = kind === 'videos' ? [fmtDate(vt.date)] : [];
  if (vt.duration) metaBits.push(esc(vt.duration));
  if (vt.speaker) metaBits.push(esc(vt.speaker));
  if (vt.lang) metaBits.push(esc(vt.lang));
  root.innerHTML = '<div class="res-watch"><div class="res-video"><iframe src="https://www.youtube-nocookie.com/embed/' + vt.youtube + '?rel=0" title="YouTube" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>' +
    '<div class="res-watch-copy"><span class="res-eyebrow">' + (kind === 'videos' ? 'VIDEO' : 'WEBINAR') + ' · ' + esc(vt.category || vt.industry || '') + '</span><h1>' + esc(vt.title) + '</h1>' +
    '<div class="res-watch-meta">' + metaBits.map(function (m) { return '<span>' + m + '</span>'; }).join('') + '</div>' +
    '<p>' + esc(vt.excerpt) + '</p>' +
    '<div class="res-watch-cta"><a class="cta-btn" href="../products/quote.html">비슷한 현장, 상담 요청</a><a class="res-ghost" href="' + kind + '.html">' + (kind === 'videos' ? '다른 영상 보기' : '다른 웹세미나 보기') + ' →</a></div></div></div>';
  if (related) {
    var pool = (D[kind] || []).filter(function (x) { return x.id !== vt.id; }).slice(0, 3);
    related.innerHTML = pool.map(function (o) { return '<a class="res-cross-card reveal" href="watch.html?id=' + encodeURIComponent(o.id) + '"><small>' + esc(kind === 'videos' ? o.category : o.industry) + '</small><b>' + esc(o.title) + '</b><span>' + esc(o.excerpt) + '</span></a>'; }).join('');
    related.querySelectorAll('.reveal').forEach(function (el) { requestAnimationFrame(function () { el.classList.add('is-visible'); }); });
  }
})();
