/* (2026-11-19) 찾기 화면 공통 '출력하기'
   펠렛타이저 생산 시스템 찾기, RE-CO2 찾기, 장비 비교 추천 세 곳이 같은 결과지를 만든다.
   payload = { title, conditions:[[라벨, 값], ...], products:[{ name, image, role }], name, type, reason, note, tip, combine }
   combine:false 이면 제품들을 '+'로 잇지 않는다 (장비 비교 추천처럼 1순위와 함께 검토할 장비를 나란히 보일 때)
   1) 페이지 안에 #finderPrintSheet 를 만들고 window.print()  (인쇄 CSS는 style.css)
   2) 인쇄 대화상자가 막힌 환경(미리보기 프레임 등)이면 products/pelletizer/print.html 을 새 탭으로 연다
   3) 새 탭도 막히면 버튼 옆에 링크를 남긴다 */
window.VatekFinderPrint = (function () {
  function esc(v) { return String(v == null ? '' : v).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function today() { var d = new Date(); return d.getFullYear() + '. ' + (d.getMonth() + 1) + '. ' + d.getDate() + '.'; }
  function abs(u) { try { return new URL(u, document.baseURI).href; } catch (e) { return u; } }
  function normalize(p) {
    var q = {};
    for (var k in p) q[k] = p[k];
    q.title = p.title || '추천 결과';
    q.conditions = (p.conditions || []).filter(function (c) { return c && c[1]; });
    q.products = (p.products || []).map(function (pr) { return { name: pr.name, image: pr.image ? abs(pr.image) : '', role: pr.role || '' }; });
    return q;
  }
  function sheetHTML(p) {
    var html = '<header><b>VATEK × Cold Jet</b><h2>' + esc(p.title) + '</h2><span>' + today() + '</span></header>';
    if (p.conditions.length) html += '<dl class="cond">' + p.conditions.map(function (c) { return '<div><dt>' + esc(c[0]) + '</dt><dd>' + esc(c[1]) + '</dd></div>'; }).join('') + '</dl>';
    html += '<div class="row">' + p.products.map(function (pr, i) {
      return '<article>' + (pr.image ? '<div><img src="' + esc(pr.image) + '" alt="' + esc(pr.name) + '"></div>' : '') + '<span>' + String(i + 1).padStart(2, '0') + (pr.role ? ' / ' + esc(pr.role) : '') + '</span><strong>' + esc(pr.name) + '</strong></article>';
    }).join(p.combine === false ? '' : '<span class="op plus"></span>') + (p.products.length > 1 && p.combine !== false ? '<span class="op eq"></span>' : '') +
      '<div class="sum"><small>' + esc(p.type) + '</small><h3>' + esc(p.name) + '</h3><p>' + esc(p.reason) + '</p></div></div>';
    if (p.note || p.tip) html += '<div class="note"><b>NOTE</b>' + (p.note ? '<p>' + esc(p.note) + '</p>' : '') + (p.tip ? '<p class="tip">' + esc(p.tip) + '</p>' : '') + '</div>';
    html += '<footer><b>(주)바테크 VATEK</b><span>Cold Jet 공식 대리점, 드라이아이스 장비와 공급 상담 031-796-4300</span></footer>';
    return html;
  }
  function build(payload) {
    var p = normalize(payload);
    var old = document.getElementById('finderPrintSheet');
    if (old) old.remove();
    var sheet = document.createElement('div');
    sheet.id = 'finderPrintSheet';
    sheet.setAttribute('aria-hidden', 'true');
    sheet.innerHTML = sheetHTML(p);
    document.body.appendChild(sheet);
    return sheet;
  }
  function encode(payload) {
    var p = normalize(payload);
    return encodeURIComponent(btoa(unescape(encodeURIComponent(JSON.stringify(p)))));
  }
  function run(payload, opts) {
    opts = opts || {};
    var printPage = opts.printPage || 'print.html';
    var sheet = build(payload);
    var fired = false;
    var onBefore = function () { fired = true; };
    var cleanup = function () { sheet.remove(); window.removeEventListener('afterprint', cleanup); window.removeEventListener('beforeprint', onBefore); };
    window.addEventListener('beforeprint', onBefore);
    window.addEventListener('afterprint', cleanup);
    try { window.print(); } catch (e) { fired = false; }
    setTimeout(function () {
      if (fired) return;
      cleanup();
      var url = printPage + '#' + encode(payload);
      var win = null;
      try { win = window.open(url, '_blank'); } catch (e) { win = null; }
      if (!win && opts.button) {
        var old = opts.button.parentNode.querySelector('.finder-print-fallback');
        if (old) old.remove();
        opts.button.insertAdjacentHTML('afterend', '<a class="finder-print-fallback" href="' + url + '" target="_blank" rel="noopener">새 탭에서 출력 페이지 열기 →</a>');
      }
    }, 400);
  }
  return { build: build, run: run, encode: encode };
})();
