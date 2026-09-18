/* VATEK RESOURCES — 게시판 데이터.
   새 글을 올리려면 해당 배열에 객체 하나를 추가하면 됩니다(맨 앞이 최신).
   서버 게시판으로 옮길 때 이 구조를 그대로 DB 필드로 쓰면 됩니다.           */
/* 고정 분류 체계 — 산업이 늘어나도 이 목록에 새 항목을 추가하지 않는 한
   필터에 새 칸이 생기지 않는다. 게시글의 industry/category/type 값은
   반드시 이 목록 중 하나를 그대로 써야 필터에 잡힌다(오타 방지 겸 통제).
   /industries/ 하위 페이지와 동일한 22개 산업명을 그대로 재사용해 사이트
   전체 용어를 통일했다. */
window.VATEK_RESOURCE_TAXONOMY = {
  industry: ['우주 · 항공', '자동차 제조', '자동차 복원 · 디테일링', '전문 세척 서비스', '엔지니어드 우드', '식품 · 음료', '주조 · 다이캐스팅', '역사적 건축물 · 문화재 복원', '의료기기 제조', '광업', '곰팡이 제거', '오일 · 가스', '포장', '플라스틱 · 복합소재', '발전 · 전력', '인쇄', '철도 · 대중교통', '화재 · 수해 복원', '고무 · 타이어', '반도체 · 전자 제조', '섬유', '생산설비 · 시설 유지보수'],
  category: ['제품', '적용 분야', '현장 시연'],
  type: ['도입 가이드', '백서', '카탈로그', '교육자료']
};

window.VATEK_RESOURCES = {

  /* ── 케이스 스터디 ───────────────────────────────────────── */
  cases: [
    {
      id: 'tire-mold-inline',
      date: '2026-08-21',
      industry: '고무 · 타이어',
      equipment: 'Aero2® PCS ULTRA · ASP-T',
      application: '금형 세척',
      title: '가황 프레스 안의 타이어 금형, 분해와 냉각 없이 세척하다',
      client: '국내 타이어 제조사 A사 · 광주 (적용 예시)',
      excerpt: '금형을 내려 세척장으로 옮기던 방식에서 프레스 안 인라인 세척으로 바꿔 가동 정지 시간을 크게 줄였습니다.',
      img: '../assets/img/rubber-tires-cleaning-tire-mold-while-hot-and-online-with-dry-ice-blasting.webp',
      stats: [{ k: '금형당 정지 시간', v: '−80%' }, { k: '분해 · 재조립', v: '0회' }, { k: '벤트홀 막힘', v: '해소' }],
      /* 본문 아래 '함께 보면 좋은 콘텐츠' — 같은 산업 · 같은 작업 · 관련 영상 (서버 게시판에서는 태그로 자동 매칭) */
      related: {
        videos: ['aero2-reinvented'],
        industry: { label: '고무 · 타이어', href: '../industries/rubber-tires.html', img: '../assets/img/rubber-tires-dry-ice-blasting-cleaning-tire-mold-without-disassembly-or-cooldown.webp', desc: '가류기에 장착한 상태로 타이어 · 고무 금형을 세척하는 방식' },
        task: { label: '금형 · 툴링 세척', href: '../applications/mold-tool-cleaning.html', img: '../assets/img/task-mold-tool-cleaning.webp', desc: '이형제 · 수지 · 카본 등 금형에 쌓인 오염물을 분해 없이 제거' }
      },
      body: [
        ['과제', '타이어 금형은 가황 반복으로 이형제와 고무 잔류물이 쌓여 벤트홀이 막히고 표면 품질이 떨어집니다. 기존에는 금형을 프레스에서 내려 냉각한 뒤 세척장에서 처리했고, 한 세트에 반나일이 걸렸습니다.'],
        ['적용', '금형이 뜨거운 상태에서 프레스 안으로 마이크로파티클 노즐을 넣어 세척했습니다. 정밀 형상에는 마이크로파티클, 고착 잔류물에는 3 mm 펠렛으로 전환하는 Aero2 PCS ULTRA를 사용했고, 반복 라인에는 ASP-T 로봇 셀을 검토했습니다.'],
        ['결과', '금형을 분해하지 않아 재조립 공정이 줄었고, 정지 시간은 세트당 약 80% 줄어든 것으로 나타났습니다. 세척 후 잔류물이 남지 않아 건조 공정 부담도 줄었습니다. (수치는 적용 예시 기준입니다)']
      ]
    },
    {
      id: 'food-conveyor-mixer',
      date: '2026-06-03',
      industry: '식품 · 음료',
      equipment: 'Aero® 80FP',
      application: '설비 위생 세척',
      title: '물 없이 매일 세척 — 제과 라인 컨베이어와 믹서의 위생 관리',
      client: '제과 제조사 B사 · 충북 (적용 예시)',
      excerpt: '물과 세제를 쓰지 못하는 구간의 탄화 반죽과 유지를 드라이아이스로 제거해 세척 주기를 주 1회에서 매일로 바꿨습니다.',
      img: '../assets/img/food-beverage-cleaning-conveyors-with-dry-ice-blasting.webp',
      stats: [{ k: '세척 중 물 사용', v: '0 L' }, { k: '세척 주기', v: '주 1회 → 매일' }, { k: '화학 세제', v: '미사용' }],
      related: {
        videos: ['food-mixer'],
        industry: { label: '식품 · 음료', href: '../industries/food-beverage.html', img: '../assets/img/food-beverage-dough-carbon-and-grease-removed-from-food-mixer.webp', desc: '오븐 · 믹서 · 컨베이어 등 식품 설비를 물 없이 현장에서 세척' },
        task: { label: '오일 · 그리스 · 고착 오염 제거', href: '../applications/oil-grease-residue-removal.html', img: '../assets/img/food-beverage-cleaning-oil-residue-from-fryers-and-cookers.webp', desc: '두껍게 축적된 유지 · 탄화물을 분해 없이 제거하는 방식' }
      },
      body: [
        ['과제', '오븐 앞뒤 컨베이어와 믹서 내부에 탄화된 반죽과 유지가 쌓였지만, 전장부와 베어링 때문에 물 세척이 어려워 주말에만 부분 분해 세척을 했습니다.'],
        ['적용', '80 lb 대용량 호퍼의 Aero 80FP로 라인 정지 사이에 세척했습니다. 식품 접촉면에는 식품 등급 드라이아이스 펠렛을, 탄화 구간에는 넓은 팬 노즐을 사용했습니다.'],
        ['결과', '물과 세제를 쓰지 않아 건조 공정 부담을 줄이고 재가동 시간을 앞당겼으며, 매일 짧게 세척하는 방식으로 바뀌면서 이물 관리에 도움이 된 것으로 나타났습니다. (수치는 적용 예시 기준입니다)']
      ]
    },
    {
      id: 'semi-mold-die-automation',
      date: '2026-03-17',
      industry: '반도체 · 전자',
      equipment: 'i³ MicroClean® 2 · 자동화 셀',
      application: '몰드 다이 세척',
      title: '반도체 몰드 다이 세척을 무인 반복 공정으로',
      client: '반도체 패키징 C사 · 경기 (적용 예시)',
      excerpt: '수작업 솔벤트 세척을 마이크로파티클 자동 세척으로 바꿔 표면 영향을 관리하며 반복 조건을 일정하게 유지했습니다.',
      img: '../assets/img/semiconductor-cleaning-the-mold-or-die-after-the-molding-process-of-the-microchips.webp',
      stats: [{ k: '세척 편차', v: '작업자 무관' }, { k: '표면 영향', v: '관리' }, { k: '솔벤트', v: '미사용' }],
      related: {
        videos: ['capabilities-applications'],
        industry: { label: '반도체 · 전자 제조', href: '../industries/semiconductor.html', img: '../assets/img/semiconductor-dry-ice-cleaning-removing-wax-and-gas-buildup-from-semiconductor-molds.webp', desc: '반도체 몰드 · 웨이퍼 장비 · PCB까지 정밀 세척 적용' },
        task: { label: '금형 · 툴링 세척', href: '../applications/mold-tool-cleaning.html', img: '../assets/img/auto-semi-mold-die.png', desc: '미세 형상 금형의 왁스 · 가스 부산물을 표면 손상 없이 제거' }
      },
      body: [
        ['과제', '몰딩 공정 후 다이에 남는 왁스와 가스 부산물을 작업자가 솔벤트로 닦아 냈습니다. 작업자에 따라 결과가 달랐고, 미세 형상 손상과 용제 취급이 부담이었습니다.'],
        ['적용', '마이크로파티클 블라스터 i³ MicroClean 2를 소형 로봇 셀에 통합해 다이 교체 주기에 맞춰 자동 세척했습니다. 입자 크기와 압력을 레시피로 저장해 같은 조건을 반복합니다.'],
        ['결과', '세척 품질이 작업자와 무관하게 일정해졌고, 표면 손상과 용제 사용이 사라졌습니다. 세척 이력이 자동 기록되어 공정 관리에도 활용합니다.']
      ]
    }
  ],

  /* ── 동영상 (YouTube) ────────────────────────────────────── */
  videos: [
    {
      id: 'aero2-reinvented',
      date: '2026-07-10',
      youtube: 'FjTGYES2M_M',
      category: '제품',
      industry: '전 산업',
      duration: '2:31',
      title: 'Aero2® — 드라이아이스 블라스팅을 다시 설계하다',
      excerpt: 'Particle Control™으로 입자 크기를 0.3–3 mm 사이에서 조절하는 Aero2 시리즈. 정밀 세척과 강한 오염 제거를 한 대로 오가는 방식을 보여 줍니다.'
    },
    {
      id: 'capabilities-applications',
      date: '2026-05-02',
      youtube: 'KDwZMKc6djs',
      category: '적용 분야',
      industry: '전 산업',
      duration: '3:05',
      title: '드라이아이스 블라스팅 — 무엇을, 어디까지 세척할 수 있나',
      excerpt: '금형, 생산 설비, 전장부, 표면 전처리까지. 산업별 대표 적용 장면을 모아 한 번에 보여 주는 소개 영상입니다.'
    },
    {
      id: 'food-mixer',
      date: '2026-02-14',
      youtube: 'HzrVVdPBvy4',
      category: '현장 시연',
      industry: '식품 · 음료',
      duration: '1:48',
      title: '식품 믹서의 드라이아이스 세척 시연',
      excerpt: '고착된 사료 반죽을 믹서 내부에서 제거하는 장면을 보여주는 영상입니다.'
    }
  ],

  /* ── 기술자료 ────────────────────────────────────────────── */
  technical: [
    {
      id: 'implementation-checklist',
      date: '2026-08-01',
      type: '도입 가이드',
      format: 'WEB · 12 항목',
      industry: '전 산업',
      title: '드라이아이스 블라스팅 도입 체크리스트 — 압축공기 · 전원 · 드라이아이스 공급',
      excerpt: '장비를 고르기 전에 확인할 현장 조건을 정리했습니다. 필요한 공기량과 압력, 전원 조건, 드라이아이스 보관과 공급 계획까지.',
      img: '../assets/img/adopt-basic-setup.jpg',
      link: '../cleaning/adopt.html',
      cta: '가이드 보기'
    },
    {
      id: 'pellet-vs-micro',
      date: '2026-04-22',
      type: '백서',
      format: 'WEB',
      industry: '전 산업',
      title: '펠렛인가, 마이크로파티클인가 — 세척 매체 선택의 기준',
      excerpt: '입자 크기가 운동 에너지와 표면 영향에 어떻게 작용하는지, 대상 재질과 오염 종류별로 어떤 매체가 맞는지 원리부터 설명합니다.',
      img: '../assets/img/adopt-pellet-vs-micro.jpg',
      link: '../cleaning/guide.html',
      cta: '자료 읽기'
    },
    {
      id: 'catalog-2026',
      date: '2026-01-15',
      type: '카탈로그',
      format: 'PDF',
      industry: '전 산업',
      title: 'Cold Jet 제품 카탈로그 2026 — 블라스터 · 펠렛타이저 · 리커버리',
      excerpt: '전 모델의 주요 사양과 포지셔닝을 한 권에 담았습니다. 인쇄용 PDF는 요청 시 보내 드립니다.',
      img: '../assets/img/coldjet-aero-family.png',
      link: '../support/catalog.html',
      cta: '카탈로그 받기'
    }
  ],

  /* ── 웹세미나 ────────────────────────────────────────────── */
  webinars: [
    {
      id: 'contract-cleaners',
      date: '2025-10-08',
      youtube: '3L2Hw6YVaJg',
      status: 'replay',
      industry: '세척 서비스',
      duration: '45분',
      speaker: 'Mike Henderson · Cold Jet',
      lang: '영어 진행',
      title: '드라이아이스 블라스팅으로 세척 사업 시작하기',
      excerpt: '계약 세척 사업자가 알아야 할 장비 선택, 견적 방식, 현장 안전과 고객 설득 포인트를 다룹니다.'
    },
    {
      id: 'food-safety',
      date: '2025-10-15',
      youtube: 'vwg-V8cOfCM',
      status: 'replay',
      industry: '식품 · 음료',
      duration: '40분',
      speaker: 'Cold Jet Food & Beverage 팀',
      lang: '영어 진행',
      title: '식품 안전의 숨은 재료 — 물 없는 설비 세척',
      excerpt: '긴 설비 정지와 물 사용, 인력 중심 세척이 식품 생산성에 미치는 영향과 드라이아이스 세척으로 바꾼 사례를 소개합니다.'
    },
    {
      id: 'blasting-101',
      date: '2025-10-23',
      youtube: 'z7OPyX4xJqo',
      status: 'replay',
      industry: '전 산업',
      duration: '35분',
      speaker: 'Cold Jet Applications 팀',
      lang: '영어 진행',
      title: 'Dry Ice Blasting 101 — 기초 원리부터 효과까지',
      excerpt: '처음 검토하는 분을 위한 입문 세션. 세척 원리, 기존 방식과의 차이, 적용 가능한 대상과 한계를 차례로 설명합니다.'
    }
  ]
};
