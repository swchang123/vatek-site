/* 제품 상세 Features 투어 (공용). 스타일은 assets/css/feature-tour.css
   - 번호(.ft-dot)나 카드(.ft-card)를 누르면 그 기능을 강조하고, 4초마다 다음 기능으로 넘어간다(화면에 보일 때만).
   - 카드나 사진 위 번호에 마우스를 올려도 그 기능으로 바뀐다. 올려 둔 동안은 자동 넘김이 멈추고, 벗어나면 이어진다.
     3D 위 번호는 화면이 움직이면 번호도 따라 움직이므로 올리기에는 반응하지 않고 누를 때만 바뀐다.
   - 섹션이 가까워지면 model-viewer와 모델 데이터 파일을 불러와 사진을 3D로 바꾼다. 불러오지 못하면 사진 그대로 동작한다.
   - 페이지별 값은 HTML에 둔다: #ftTour 의 data-viewer / data-meshopt / data-model / data-model-key,
     각 .ft-dot 의 data-p(위치) data-n(면 방향) data-o(카메라 각도와 거리) data-t(바라보는 지점). 값은 Cold Jet 제품 페이지의 설정 그대로. */
(function(){
  var root=document.getElementById('ftTour');if(!root)return;
  var stage=document.getElementById('ftStage'),label=document.getElementById('ftStageLabel'),btn=document.getElementById('ftToggle');
  var cards=root.querySelectorAll('.ft-card'),n=cards.length,cur=0,timer=null,playing=false,inView=false,mv=null,hov=false,hovT=null;
  var HOT=[];
  root.querySelectorAll('.ft-pic .ft-dot').forEach(function(d){HOT[+d.dataset.i]={p:d.dataset.p,n:d.dataset.n,o:d.dataset.o,t:d.dataset.t,above:d.hasAttribute('data-above')}});
  function show(i){cur=(i+n)%n;
    root.querySelectorAll('.ft-dot').forEach(function(d){var on=+d.dataset.i===cur;d.classList.toggle('is-on',on);d.setAttribute('aria-pressed',on?'true':'false')});
    cards.forEach(function(c){var on=+c.dataset.i===cur;c.classList.toggle('is-on',on);c.setAttribute('aria-pressed',on?'true':'false')});
    var h=HOT[cur];if(mv&&h&&h.o){mv.cameraOrbit=h.o;if(h.t)mv.cameraTarget=h.t}}
  function sync(){if(timer){clearInterval(timer);timer=null}if(playing&&inView&&!hov)timer=setInterval(function(){show(cur+1)},4000)}
  function setPlaying(v){playing=v;if(btn){btn.setAttribute('aria-pressed',v?'true':'false');btn.classList.toggle('is-paused',!v);btn.querySelector('span').textContent=v?'투어 일시정지':'투어 재생'}sync()}
  function pick(el){el.addEventListener('click',function(){show(+el.dataset.i);setPlaying(false)})}
  function isMouse(e){return !e.pointerType||e.pointerType==='mouse'}
  function hover(el){
    el.addEventListener('pointerenter',function(e){if(!isMouse(e))return;hov=true;sync();clearTimeout(hovT);hovT=setTimeout(function(){show(+el.dataset.i)},90)});
    el.addEventListener('pointerleave',function(e){if(!isMouse(e))return;clearTimeout(hovT);hov=false;sync()});
  }
  root.querySelectorAll('.ft-dot').forEach(function(d){pick(d);hover(d)});cards.forEach(function(c){pick(c);hover(c)});
  if(btn)btn.addEventListener('click',function(){setPlaying(!playing)});

  var started3d=false;
  function init3d(){
    var D=root.dataset;
    if(started3d||!stage||!D.viewer||!D.model)return;started3d=true;
    var c=document.createElement('canvas');if(!(window.WebGLRenderingContext&&(c.getContext('webgl2')||c.getContext('webgl'))))return;
    if(navigator.connection&&navigator.connection.saveData)return;
    if(!window.customElements||!window.Promise||!window.URL||!window.Blob)return;
    /* model-viewer는 meshopt 디코더를 내장하지만, 이 주소의 스크립트가 로드돼야 쓰기 시작한다 */
    self.ModelViewerElement=self.ModelViewerElement||{};
    if(D.meshopt)self.ModelViewerElement.meshoptDecoderLocation=D.meshopt;
    function load(src,mod){return new Promise(function(ok,no){var s=document.createElement('script');if(mod)s.type='module';s.src=src;s.onload=ok;s.onerror=no;document.head.appendChild(s)})}
    /* 모델은 base64 데이터 파일로 받아 Blob 주소로 바꿔 뷰어에 넘긴다 */
    Promise.all([load(D.viewer,true).then(function(){return customElements.whenDefined('model-viewer')}),load(D.model)]).then(function(){
      var key=D.modelKey,b64=window.VATEK_MODELS&&window.VATEK_MODELS[key];if(!b64)return;
      var bin=atob(b64),len=bin.length,u8=new Uint8Array(len);for(var j=0;j<len;j++)u8[j]=bin.charCodeAt(j);
      var modelUrl=URL.createObjectURL(new Blob([u8],{type:'model/gltf-binary'}));window.VATEK_MODELS[key]=null;
      var el=document.createElement('model-viewer');el.className='ft-mv';
      var h0=HOT[cur]||{};
      var at={src:modelUrl,alt:D.alt||'3D 모델','camera-controls':'','disable-zoom':'','disable-pan':'','interaction-prompt':'none','touch-action':'pan-y','shadow-intensity':'0.6','shadow-softness':'1','environment-image':'neutral','exposure':'1.25','min-camera-orbit':'auto 12deg 0.9m','max-camera-orbit':'auto 100deg 4m','interpolation-decay':'140'};
      if(h0.o)at['camera-orbit']=h0.o;if(h0.t)at['camera-target']=h0.t;
      for(var k in at)el.setAttribute(k,at[k]);
      stage.querySelectorAll('.ft-pic .ft-dot').forEach(function(d){
        var i=+d.dataset.i,h=HOT[i];if(!h||!h.p)return;
        var b=d.cloneNode(true);b.removeAttribute('style');b.className='ft-dot'+(h.above?' is-above':'');b.setAttribute('slot','hotspot-'+(i+1));b.setAttribute('data-position',h.p);b.setAttribute('data-normal',h.n||'0m 1m 0m');b.setAttribute('data-visibility-attribute','visible');
        pick(b);el.appendChild(b);
      });
      el.addEventListener('load',function(){mv=el;stage.classList.add('is-3d');if(label)label.textContent='INTERACTIVE 3D';show(cur)});
      el.addEventListener('error',function(){if(!mv&&el.parentNode)el.parentNode.removeChild(el)});
      el.addEventListener('camera-change',function(e){if(e.detail&&e.detail.source==='user-interaction')setPlaying(false)});
      stage.appendChild(el);
    }).catch(function(){});
  }
  if('IntersectionObserver' in window){
    new IntersectionObserver(function(es){inView=es[0].isIntersecting;sync()},{threshold:.25}).observe(root);
    var near=new IntersectionObserver(function(es){if(es[0].isIntersecting){near.disconnect();init3d()}},{rootMargin:'700px 0px'});near.observe(root);
  }else{inView=true;init3d()}
  show(0);
  setPlaying(!(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches));
})();

/* 사양 표(.sp): 단위 전환과 전체 펼침. 스타일은 feature-tour.css 아래쪽 */
(function(){
  var sp=document.getElementById('specs');if(!sp)return;
  var more=sp.querySelectorAll('.sp-more'),all=sp.querySelector('.sp-all'),unitName=sp.querySelector('.sp-unit-name'),units=sp.querySelectorAll('.sp-toggle button');
  sp.classList.add('is-js');
  if(all&&more.length){
    /* 펼침과 접힘은 표를 감싼 .sp-clip 의 높이를 움직여 보여 준다(줄 자체는 높이를 움직일 수 없어서).
       접을 때 표 윗부분이 화면 밖이면, 버튼이 제자리에 머물도록 접히는 만큼 화면을 함께 올린다. */
    var table=sp.querySelector('.sp-table'),card=sp.querySelector('.sp-card'),clip=document.createElement('div'),busy=false;
    var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    clip.className='sp-clip';table.parentNode.insertBefore(clip,table);clip.appendChild(table);
    function label(open){all.setAttribute('aria-expanded',open?'true':'false');all.querySelector('span').textContent=open?'접기':'전체 사양 '+sp.dataset.count+'개 보기'}
    function run(from,to,pin,done){
      var fin=false,y0=all.getBoundingClientRect().top;
      clip.style.height=from+'px';void clip.offsetHeight;clip.classList.add('is-anim');clip.style.height=to+'px';
      function follow(){if(fin)return;var d=all.getBoundingClientRect().top-y0;if(d)window.scrollBy(0,d);requestAnimationFrame(follow)}
      function end(e){if(fin||(e&&e.target!==clip))return;if(pin)follow();fin=true;clip.removeEventListener('transitionend',end);clip.classList.remove('is-anim');clip.style.height='';busy=false;if(done)done()}
      if(pin)requestAnimationFrame(follow);
      clip.addEventListener('transitionend',end);setTimeout(end,560);
    }
    all.hidden=false;
    all.addEventListener('click',function(){
      if(busy)return;var open=!sp.classList.contains('is-open');
      if(reduce){sp.classList.toggle('is-open',open);label(open);return}
      busy=true;var h0=clip.offsetHeight;
      if(open){sp.classList.add('is-open');label(true);run(h0,clip.scrollHeight,false)}
      else{var pin=card.getBoundingClientRect().top<96;sp.classList.add('is-closing');label(false);
        run(h0,more[0].offsetTop,pin,function(){sp.classList.remove('is-open');sp.classList.remove('is-closing')})}
    });
  }
  units.forEach(function(b){b.addEventListener('click',function(){var u=b.dataset.unit;sp.dataset.unit=u;
    units.forEach(function(x){var on=x===b;x.classList.toggle('is-on',on);x.setAttribute('aria-pressed',on?'true':'false')});
    if(unitName)unitName.textContent=u==='imperial'?'IMPERIAL':'METRIC'})});
})();
