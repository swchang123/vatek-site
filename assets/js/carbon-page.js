/* 카본캡쳐 기술(carbon-capture/index.html): 원리 섹션의 도식 영상.
   보통은 화면에 보일 때 소리 없이 반복 재생한다(main.js가 autoplay 영상을 화면 안에서만 재생한다).
   움직임 줄이기를 켠 방문자에게는 자동으로 재생하지 않고, 직접 재생할 수 있도록 조작 막대를 보여 준다.
   main.js보다 먼저 실행되어야 한다(main.js가 autoplay 영상을 모으기 전에 속성을 뗀다). */
(function () {
  var video = document.querySelector('.cc-flow-video video');
  if (!video) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) return;
  video.removeAttribute('autoplay');
  video.autoplay = false;
  video.pause();
  video.setAttribute('controls', '');
  // 재생 전에도 첫 장면이 보이게 한다
  video.addEventListener('loadedmetadata', function () { try { video.currentTime = 0.01; } catch (e) {} }, { once: true });
})();
