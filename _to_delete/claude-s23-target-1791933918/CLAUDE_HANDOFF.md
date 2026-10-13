# VATEK Site — 작업 인계 노트 (Claude Code 전달용)

최종 갱신: 2026-10-14 · 대상 저장소: `swchang123/vatek-site` (main)

## 이 번들에 대해
**기준선(baseline) = 저장소 `main`, 2026-09-24T01:52:30Z 시점 동기화.** 그 시점에 저장소 main을 그대로 재가져와(§1–§12 전체 작업분 포함) 프로젝트와 저장소가 **완전히 동일**함을 확인했습니다. 따라서 §1–§12는 이미 저장소에 있으므로 Claude Code가 손댈 필요가 없습니다.

**이번 번들은 그 동기화 "이후" 추가된 변경분만** 담았습니다 — §13(히어로 영상 교체, 5개 페이지) + §14(2026-10-01: 메인 히어로 영상·문구·레이아웃, 헤더 투명화, 블라스터 히어로 삽입 방식 통일) + §15(2026-10-02: 히어로 영상 포스터 이미지 전면 교체) + §16(2026-10-02: 장비비교·구매프로세스 히어로 영상 교체 및 영상 필터 전면 제거) + §17(2026-10-02: 메가메뉴 미리보기 — 라벨 비침 버그 수정, 블라스터 항목 영상화 / 전 페이지 92개 HTML 포함) + §18(2026-10-02: 서브메뉴 영상 6개 추가 적용, 히어로 재사용 cover 크롭, 사전 로드 풀). 포함된 파일을 저장소 동일 경로에 **그대로 덮어쓰기**만 하면 됩니다(추가 구현·재해석 불필요 — 마크업·CSS·JS까지 지금 화면과 100% 동일, 한 글자도 다르지 않게 그대로 복사). 번들에 없는 파일은 손대지 않습니다.

**2026-10-03 갱신 — §19–§33 추가**: 렌탈·데모 하위 5개 페이지 히어로 선명화(§19), 기술·서비스 역량 재구성(§20), 서브메뉴 이미지 추가(V RENTAL §21, 데모 §24, 세척용역 §25, 렌탈 신청·데모 신청·교육 §27/§30/§33), V RENTAL 로고(§26), 히어로 이미지 교체(§22·§23·§25·§27), 대메뉴 클릭 비활성화(§28), 서브메뉴 미리보기 즉시 표시(§29), 데모 일러스트·비용 안내(§31), 기술지원 안내 신규(§32). **같은 항목을 여러 § 가 다룰 때는 번호가 큰 쪽이 최종 상태**입니다(예: §9의 역량 페이지 히어로는 §20이 덮어씀, §32 기술지원은 v2가 최종).

**2026-10-12 갱신 — §34–§49 추가 (히어로·서브메뉴 이미지 전면 교체 라운드)**: 발주자 제공 사진으로 11개 페이지 히어로를 교체·신설하고 전부 **기술지원 안내(support/techsupport.html) 히어로와 동일 구성**으로 통일했습니다 — 21:9 2206×946 WebP 정적 이미지(패럴랙스·블러 없음), 좌측 fit-content 텍스트박스(max-width min(520px,36cqw), h1 clamp(20px,2.8cqw,42px)), 상단 어두운 그라데이션(.66→.22), 본문 첫 섹션 `rec-cover tint-hatch`(히어로 위로 라운드 겹침). 대상: 데모 테스트 §34, 교육·A/S §35→§46, 기술지원 §36·§37, 기술자료 §38→§39~41, 제품 카탈로그 §42, 웹세미나 §43, 렌탈 신청 §44, 데모 신청 §45, 세척용역 §47, 회사소개 §48, 위치/연락처 §49. 각 히어로를 4:3 960×720으로 크롭한 서브메뉴 미리보기(`data-img`)를 전 페이지 메가메뉴에 반영. 교체된 구 이미지 파일은 **삭제됨**(아래 "삭제할 파일" 참조). **같은 페이지를 여러 § 가 다룰 때 번호가 큰 쪽이 최종**(§38은 §39~41로, §35는 §46으로 대체).

### 이 번들 적용 방법 (요약)
1. 압축 해제 후 번들 루트에서 `sha256sum -c MANIFEST.sha256.txt` — 전부 OK인지 확인
2. 번들의 모든 파일을 저장소 동일 경로에 **그대로 덮어쓰기**(HTML 92 · CSS 15 · JS 1 · 이미지 40 · 영상 13). 번들에 없는 파일은 손대지 않음
3. 아래 "삭제할 파일" 목록을 저장소에서 삭제(참조 0건 확인됨)
4. 커밋 전 저장소에서 끊어진 참조 재점검(기존 17건 외 신규 0건이어야 함)

### 삭제할 파일 (2026-10-12 기준, 번들 HTML 어디에서도 참조하지 않음)
`assets/img/demo-hero.webp`, `submenu-demo.webp`, `education-hero.webp`, `submenu-education.webp`, `education-hero-v2.webp`, `submenu-education-v2.webp`, `apply-hero.webp`, `submenu-apply.webp`, `demo-apply-hero.webp`, `submenu-demo-apply.webp`, `partners-hero.webp`, `submenu-partners.webp`. (§33의 `demo-way-*.png` 3개도 여전히 삭제 가능.) `vatek-building.jpg`, `automation-hero.mp4`/`automation-hero-poster.jpg`는 다른 페이지가 사용하므로 **유지**.

### 무결성 검증 결과 (2026-10-12, 번들 생성 직전)
- 번들 HTML **92개**(라이브 87 + handoff3에만 있는 products/recovery 5) 중 라이브와 공통인 87개 전부 바이트 단위 동일(0건 차이). `cases/library.html`은 리다이렉트 스텁이라 번들 제외(기존 동일). `assets/css` 15개 · `assets/js/main.js` 라이브와 동일
- `MANIFEST.sha256.txt`는 2026-10-12에 **전체 재생성**(HTML·CSS·JS·이미지·영상·이 문서 전부, 매니페스트 자신 제외) — 이전 §34~§49 메모의 "HTML 해시 재생성 필요" 단서는 해소됨
- 이번 라운드에서 새로 추가된 CSS: `about-page.css`, `location-page.css`, `resources-page.css`(이전 번들에 없던 파일 — 저장소 파일을 **덮어쓰기**)

### 무결성 검증 결과 (2026-10-03, 이전 번들)
- 번들 HTML **92개 전부**가 프로젝트 원본과 바이트 단위로 동일(0건 차이). `assets/css` 12개 · `assets/js/main.js` 1개도 원본과 동일. 이미지·영상은 파일 크기 일치 확인
- 번들 루트의 **`MANIFEST.sha256.txt`** = 번들 내 전 파일(이 문서 포함, 매니페스트 자신 제외)의 SHA-256. 압축을 푼 뒤 번들 루트에서 `sha256sum -c MANIFEST.sha256.txt`로 전송 오류가 없는지 먼저 확인할 것. 저장소에 덮어쓴 뒤에도 같은 상대 경로로 재검증 가능
- 번들 HTML이 참조하는 자산 762건 중 **끊어진 참조 17건은 이번 변경과 무관한 기존 상태**(이 프로젝트 사본에 없는 파일 — 저장소 기준선에 있을 수 있으니 저장소에서 존재 여부를 확인하고 **새로 만들지 말 것**): `assets/video/belief-co2.{webm,mp4}`, `coldjet-video.{webm,mp4}`, `principle-nozzle.mp4`, 산업별 히어로 배너 영상 8개(`detailing/auto/facility/historical/medical/plastics/restoration/semiconductor-hero-banner.mp4`), `assets/img/ind-card-rail.png`, `products/automation/{combi-pcs,asp-t,duct-robot}.html`(미구축 하위 페이지)
- 번들에 **없는** 자산(예: `guide-hero-work.jpg`, `stackdo-rental.jpg`, `vatek-coldjet-photo-1/5.jpg`, `facility-maintenance-…webp`)은 기존 저장소 파일을 재사용하는 것으로 **저장소 기준선에 이미 존재**해야 함 — 없으면 알려 주세요(임의 대체 금지)
- 더 이상 쓰이지 않아 **삭제 가능**(이번 번들 HTML 어디에서도 참조하지 않음, 삭제는 선택): `assets/img/demo-way-1-ship.png`, `demo-way-2-lab.png`, `demo-way-3-onsite.png`(§31에서 webp로 교체). `pcs-demo-namecard.mp4`는 데모 페이지에서 미사용이나 다른 페이지 사용 여부 확인 후 판단

---

## 마지막 GitHub 동기화 이후 변경 사항 (누적)
`github.md`의 마지막 동기화(2026-09-16T11:21:19Z, main) 이후 작업한 내용 전체입니다. §1–§7은 이전 zip에 포함되어 있었고, §8 이후가 이번 zip에서 새로 추가된 부분입니다.

### 1. 장비 비교 파인더 개편 (products/compare-equip.html)
- 옵션 버튼 클릭 시 자동 진행 → 체크박스형 카드 선택 + "이전/다음" 명시적 스텝 이동 방식으로 변경
- 관련 CSS: `assets/css/compare-equip-page.css`, JS: `assets/js/compare-equip.js`

### 2. 신규 페이지: 구매 프로세스 안내 (products/process.html)
- 6단계 구매 플로우, 결제 방식 4종, 드라이아이스 연간계약/선결제 안내, FAQ 등. 신규 CSS: `assets/css/process-page.css`

### 3. 적용사례 영역 전면 개편 (게시판 형 리소스 허브)
- 신규: `cases/case-studies.html`, `cases/videos.html`, `cases/technical.html`, `cases/webinars.html`, `cases/detail.html`(`?id=`), `cases/watch.html`(`?id=`)
- 데이터 `assets/data/resources.js`, 렌더러 `assets/js/resources.js` / `assets/js/resource-detail.js`, 스타일 `assets/css/resources-page.css`
- `cases/library.html`은 리다이렉트 스텁, `cases/testimonials.html` 삭제

### 4. 사이트 전역 메뉴 재구성 (1차) — §8에서 다시 변경됨, 최종 구조는 §8 참조

### 5. 블라스터 페이지 한국어 카피 전면 교정 (products/blaster/index.html) — "FROM MANUAL TO AUTOMATED" 섹션 삭제

### 6. "GLOBAL TECHNOLOGY · LOCAL SUPPORT" 섹션을 펠렛타이저·리커버리·자동화·노즐 페이지 최하단에 추가 (last-freeze 스크롤 효과 포함)

### 7. 렌탈·데모 메뉴 재편 + 신규 페이지
- 삭제: `rental/recommend.html`, `rental/faq.html`, `rental/visit.html`
- `rental/vrental.html` 재구성 (CSS `assets/css/vrental-page.css`), `rental/apply.html` 신규 (렌탈 신청, CSS `apply-page.css`), `rental/demo.html` 신규 (데모 안내, CSS `demo-page.css`), `rental/demo-apply.html` 신규 (데모 신청), `rental/partners.html` 신규 (세척용역 파트너, CSS `partners-page.css`)
- `support/education.html` 재구성 (CSS `education-page.css`), `support/catalog.html` 게시판형 재구성, `company/about.html` 전면 재구성 (CSS `about-page.css`)
- 신규 이미지: `assets/img/partner-jpmotors-*.png`, `assets/img/demo-way-1-ship.png` / `-2-lab.png` / `-3-onsite.png`, `assets/img/vatek-coldjet-photo-1~5.jpg`, `assets/img/coldjet-hq-*.jpg`, `assets/img/vatek-field-*-graded.png`

---

## 이번 zip에서 새로 추가된 변경 사항 (2026-09-18, §8 이후)

### 8. 사이트 전역 메가메뉴 최종 구조 (전체 HTML 페이지 동일 반영)
상단 메뉴 6개의 **라벨·eyebrow·서브메뉴 항목·그룹 라벨·기본 미리보기**가 아래와 같이 확정되었습니다. 모든 페이지의 `<header>` 메가메뉴가 이 구조와 일치합니다(상대경로 `../` 깊이만 다름). 그룹 라벨은 `<li class="megamenu-index-group">…</li>`(기존 제품 메뉴 전용 CSS 재사용).

**① 드라이아이스 세척가이드** (`cleaning/index.html`) — 변경 없음
드라이아이스 세척의 이해 · 타 세척 방식과 비교 · 산업별 솔루션 · 작업별 솔루션 · 도입 가이드

**② 장비 · 드라이아이스** (`products/index.html`) — 구 "제품·자동화·공급"
- eyebrow `PRODUCTS · AUTOMATION · SUPPLY` / 소제목 "세척부터 생산·회수·자동화까지" (변경 없음)
- 그룹 `EQUIPMENT & SYSTEMS`: 드라이아이스 세척기 (블라스터) · 드라이아이스 제조기 (펠렛타이저) · CO2 리커버리 · 자동화 시스템 · 노즐·액세서리
- 그룹 `SUPPLY & BUYING GUIDE`: **드라이아이스 공급**(구 "드라이아이스 구매·공급") · 장비 비교·추천받기 · 구매 프로세스 안내 — **"견적 요청" 항목 제거**(하단 스트립과 중복)
- 하단 `.megamenu-trust-strip`: 기존 신뢰 문구 4개(`<span>`) → **링크 4개(`<a>`)로 교체**: 견적 요청(`products/quote.html`) · 데모 신청(`rental/demo-apply.html`) · 렌탈 신청(`rental/apply.html`) · 문의하기(`products/quote.html`). 한 줄 고정(줄바꿈 없음), 호버 시 메뉴 항목과 같은 연한 배경(`--blue-pale`) + `--blue-dark` 글자색.
- `products/index.html`: `<title>`, 브레드크럼 "장비 · 드라이아이스", 카드 06 제목 "드라이아이스 공급"
- 푸터 컬럼 제목 "제품·자동화·공급" → "장비 · 드라이아이스" (전 페이지)

**③ 적용 분야** (`cases/index.html`) — 구 "적용사례"
- eyebrow `APPLICATIONS` / 제목 "적용 분야" / 설명 "산업과 작업별 적용 방법, 그리고 실제 현장 사례를 확인하세요."
- 그룹 `APPLICATIONS`: 산업별 솔루션(`cleaning/industry.html`) · 작업별 솔루션(`cleaning/task.html`)
- 그룹 `CASE STUDIES`: 케이스 스터디(`cases/case-studies.html`) · **적용 영상**(`cases/videos.html`, 구 "동영상 보기")
- 기본 미리보기·상세: 산업별 솔루션(`assets/img/industry-thumb.jpg`)
- `cases/index.html`: 제목 "적용 분야", 서브카드 4개(산업별 · 작업별 · 케이스 스터디 · 적용 영상)로 재구성(기술자료·웹세미나 카드 제거)
- `cases/videos.html` `<title>` "적용 영상", 브레드크럼 "적용 분야 > 적용 영상"; `cases/*` 브레드크럼의 "적용사례 · 자료" → "적용 분야"; `cases/case-studies.html` `<title>` "케이스 스터디"; technical/webinars 교차카드 문구 "케이스 스터디" / "적용 영상"
- 푸터 링크: "적용사례 케이스 스터디" → "케이스 스터디", "동영상 보기" → "적용 영상" (전 페이지)

**④ 세척 테스트·렌탈** (`rental/index.html`) — 구 "렌탈·데모"
- eyebrow `TEST & RENTAL` / 제목 "세척 테스트·렌탈"
- 그룹 `SERVICE`: 장비 렌탈(`rental/vrental.html`) · 데모 테스트(`rental/demo.html`) · 세척 용역(`rental/partners.html`)
- 그룹 `REQUEST`: 렌탈 신청(`rental/apply.html`) · 데모 테스트 신청(`rental/demo-apply.html`)
- 기본 상세 제목 "장비 렌탈"
- `rental/index.html`: `<title>`·브레드크럼·h1 "세척 테스트·렌탈", cat `TEST & RENTAL`, 서브카드 5개를 위 순서·명칭으로 재배치
- 푸터 히어로 버튼 "렌탈 · 데모" → "세척 테스트 · 렌탈", 푸터 "사례·지원" 컬럼 링크 "렌탈·데모" → "세척 테스트·렌탈" (전 페이지)
- 각 하위 페이지 내부 제목(V RENTAL 안내 등)은 변경하지 않음

**⑤ 기술지원·자료** (`support/index.html`) — 구 "지원·자료"
- eyebrow `TECHNICAL SUPPORT` / 제목 "기술지원·자료"
- 그룹 `TECHNICAL SUPPORT`: **교육·A/S**(`support/education.html`, 구 "교육 및 사후관리") · **기술지원 안내**(`support/techsupport.html`, 신규 노출)
- 그룹 `RESOURCES`: 기술자료(`cases/technical.html`) · 제품 카탈로그(`support/catalog.html`) · **웨비나**(`cases/webinars.html`, 구 "웹세미나")
- 기본 미리보기·상세 제목 "교육·A/S"
- `support/index.html`: `<title>`·브레드크럼·h1 "기술지원·자료", cat `TECHNICAL SUPPORT`, 서브카드를 위 5개로 교체(설치/시운전 · Knowledge Center · 공지사항·뉴스 카드 제거)
- `support/techsupport.html`, `support/install.html`, `support/knowledge.html`: 브레드크럼 부모 "지원·자료" → "기술지원·자료", cat "TECHNICAL SUPPORT" (본문은 기존 그대로)
- `products/quote.html` 브레드크럼 부모 "제품·자동화·공급" → "장비 · 드라이아이스"

**⑥ 회사소개** (`company/index.html`)
- 서브메뉴 3개: 회사소개(`company/about.html`) · 기술·서비스 역량(`company/capability.html`) · 위치/연락처(`company/location.html`) — **"Cold Jet 대한민국 공식 대리점"(partner.html)·"시설/인증/파트너"(facility.html) 항목 제거**, `data-i` 0/1/2로 재번호
- `company/index.html` 서브카드 동일하게 3개로 축소

**홈(`index.html`) 메뉴 픽커 카드 동기화**: 카드 제목·설명·칩을 위 구조에 맞춤 — 장비 · 드라이아이스 / 적용 분야(칩: 산업별 솔루션 · 작업별 솔루션 · 케이스 스터디 · 적용 영상) / 세척 테스트·렌탈(칩: 장비 렌탈 · 데모 테스트 · 세척 용역 · +2개) / 기술지원·자료(칩: 교육·A/S · 기술지원 안내 · 기술자료 · +2개) / 회사소개(칩: 회사소개 · 기술·서비스 역량 · 위치/연락처). 삭제된 `rental/recommend.html` 칩 링크 제거.

### 9. 신규 페이지 본문: 기술·서비스 역량 (company/capability.html)
스텁(이미지 플레이스홀더 + 카드 4개)을 풀 페이지로 재구성. 신규 CSS `assets/css/capability-page.css` (`cap-*` 접두). `pelletizer-page.css`, `recovery-page.css`, `compare-equip-page.css`도 함께 로드(공용 `plt-*` / `rec-*` / `cmp-*` 어휘 사용 — about.html과 동일 패턴).
- 히어로: `subhero-parallax aut-hero-stage cap-hero-stage`, 이미지 `assets/img/vatek-field-heritage-locomotive-cleaning-graded.png`, 섹션 점프 링크 4개(`.cap-hero-jump`)
- `#pillars` (tint-hatch): "네 가지 역량" 카드 4개 — 세척 응용기술 연구 / 현장 세척 실행 / 장비 기술지원·정비 / 시스템 구성·통합
- `#method` (cmp-dark): "결과를 정하는 다섯 변수"(매체·압력·공급량·노즐·거리·각도) + "접수부터 이관까지 다섯 단계", 키 문장, CTA 2개
- `#field`: 현장 기록 4건(문화재 증기기관차 / 야외 조형물 / 산업 기계·설비 / 유류 오염 정리) — 이미지 `vatek-field-*-graded.png` 4장, 과제/방법 설명
- `#support` (tint-hatch): 2단 지원 체계(TIER 1 바테크 하남 / TIER 2 Cold Jet 글로벌 기술팀) + 보유 인프라 4카드(`.cap-ready`)
- `#cap-final` (bls-final last-freeze): 최종 CTA
- 본문 내 문구는 사진을 바탕으로 일반화해 작성 — 사실 확인 필요 항목은 "미해결 사항" 참조

### 10. 데이터 파일 (assets/data/resources.js)
- 기술자료 "Cold Jet 펠렛타이저 카탈로그" 항목 썸네일: `pelletizer-hero.png`(삭제됨) → `pelletizer-pr750h-official.jpg`

### 11. 공용 CSS 변경 (assets/css/style.css)
- `.megamenu-trust-strip`: `flex-wrap: nowrap; white-space: nowrap; gap: clamp(16px, 2vw, 28px)`
- `.megamenu-trust-strip a` 스타일 추가(불릿 `::before`, `padding: 6px 10px; margin: -6px -10px; border-radius: 8px`, 호버 `background: var(--blue-pale); color: var(--blue-dark)`)
- 그 외 style.css 규칙 변경 없음

---

### 12. 장비·드라이아이스 허브 페이지 레이아웃 전면 개편 (products/index.html)
- 신규 CSS: `assets/css/products-hub-page.css`
- 히어로(데스크톱 상단 고정): 블러(60px) 처리한 `blaster-catalog-hero-natural.png` 배경 + 화이트 그라디언트 오버레이(가독성 확보), 브레드크럼 + 대제목 "장비 · 드라이아이스" + 설명 + 버튼 2개(장비 추천받기 · 견적 요청)
- 히어로 하단 2단 메뉴: 좌측 "01" 아웃라인 숫자 배지(블루 2px 테두리, 투명 채움) + Equipment 링크(화이트 카드), 우측 "02" 아웃라인 배지 + Supply 링크(연한 블루 카드), 50:50 분할, 컴팩트 타이포(14.5px)
- 섹션 01(Equipment & Systems): 히어로 위로 라운드 코너 + 섀도우와 함께 겹쳐 올라오는 스크롤 효과, 타일 그리드(와이드 1 + 일반 4)
- 섹션 02(Supply & Buying Guide) + 요청 밴드(견적·데모·렌탈): 기존 `.last-freeze` 패턴 재사용해 하단 고정, 다 보이면 푸터가 그 위로 덮으며 올라옴(다른 last-freeze 페이지와 동일 동작 — 인라인 스크립트로 높이 동기화)
- 반응형: 960px 이하는 두 고정 레이어 모두 `position: static`으로 전환되어 일반 스크롤 흐름으로 복귀

### 13. 히어로 영상 교체 — 공급/리커버리/자동화/펠렛타이저/노즐 (2026-09-24 ~ 2026-10-01)
5개 페이지의 히어로를 16:9 또는 정지이미지에서 **21:9 영상**으로 통일. 방식은 전 페이지 동일:
- `<video>`에 `data-buffer="0" data-pan-scale="1"` (기존 `data-buffer="60" data-pan-scale="1.06" data-blur-start="0.5"`에서 변경 — 스크롤 시 6% 확대·블러 효과 제거, 항상 원본 그대로 표시)
- 정지이미지 시절 블러 레이어가 남아있던 곳은 제거: `supply-page.css`의 `.sup-hero-stage .hero-fit::before { backdrop-filter: blur(1.5px) … }` → `display: none`

**파일별 변경:**
- `products/supply.html` — 섹션 클래스 `aut-hero-stage sup-hero-stage` → `sup-hero-stage` (16:9 스테이지 규칙 탈피). 영상 `assets/video/supply-hero.mp4` 교체(21:9, 1920×824)
- `products/recovery/index.html` — 영상 `assets/video/recovery-hero.mp4` 교체(21:9, 2206×946). 스테이지는 기존 `rec-hero-stage`(이미 21:9) 그대로
- `products/automation.html` — 영상 `assets/video/automation-hero.mp4` 교체(21:9, 1260×540)
- `products/pelletizer/index.html` — 영상 `assets/video/pelletizer-hero.mp4` 교체(21:9, 2206×946). 스테이지는 기존 `pel-hero-stage`(이미 21:9) 그대로
- `products/nozzle.html` — 영상 `assets/video/nozzle-hero.mp4` 교체(VATEK_accessories_hero_web.mp4). 스테이지는 `noz-hero-stage aut-hero-stage`(16:9) 유지 — 노즐 영상은 21:9 전환 대상이 아니었음

**공용 CSS 변경 (assets/css/style.css):**
- `.bls-hero-stage, .aut-hero-stage { height: min(…, 56.25vw) }` → `.bls-hero-stage`만 16:9 유지, `.pel-hero-stage, .rec-hero-stage, .sup-hero-stage, .aut-hero-stage { height: min(…, 42.86vw) }`로 통합(자동화도 21:9 높이로 편입)
- `.sup-hero-stage .hero-fit { aspect-ratio: 21/9 }` 추가 바로 아래 `.aut-hero-stage .hero-fit { aspect-ratio: 21/9 }` 추가
- 641~1100px 구간(`.bls-hero-stage, .pel-hero-stage, .rec-hero-stage, .aut-hero-stage` 공용 규칙)에 `.sup-hero-stage`도 포함되도록 반영

**`assets/css/supply-page.css` 전용 변경:**
- `.sup-hero-stage .subhero-parallax-img { object-position: 50% 62% }` → `50% 50%`
- `.sup-hero-stage .hero-fit::before`(1.5px 블러) → `display: none`
- 641~1100px 구간 전용 미디어쿼리 추가: 이 구간만 16:9 높이로 복귀 + `.hero-fit` 종횡비 해제(cover로 좌우 크롭) — 21:9 낮은 높이에서 텍스트박스가 브레드크럼과 겹치는 문제 수정

**`assets/css/automation-page.css` 전용 변경:**
- 641~1100px 구간 전용 미디어쿼리 추가 (supply-page.css와 동일 로직 — 16:9 복귀)

**신규/교체된 영상 파일** (모두 번들에 포함, `assets/video/` 경로에 덮어쓰기):
`supply-hero.mp4` (0.37MB) · `recovery-hero.mp4` (0.59MB) · `automation-hero.mp4` (0.80MB) · `pelletizer-hero.mp4` (1.55MB) · `nozzle-hero.mp4` (1.31MB)

### 14. 메인페이지 히어로 전면 수정 (index.html) + 블라스터 히어로 삽입 방식 통일 (2026-10-01)

**a) 메인 히어로 영상 교체 + 틴트 완화**
- `assets/video/main-hero.mp4` 교체(신규 영상). `<source>`에서 존재하지 않던 `main-hero.webm` 참조 제거, mp4 단일 소스로 정리
- `.hero-overlay`(영상 위 어두운 그라디언트 틴트) 완화: 기존 `radial-gradient + linear-gradient(0.92→0.30 불투명도)`를 `linear-gradient(115deg, rgba(27,36,38,.55) 0%, .30 30%, transparent 60%)`로 교체 — 좌측 텍스트 가독성만 남기고 화면 대부분은 투명해 영상이 선명하게 보임

**b) 메인 히어로 문구 교체 + 레이아웃 재배치**
- 제목(`<h1>`): "세계 시장에서 검증된 Cold Jet의 기술, 바테크가 한국 현장에 연결합니다." (2줄, `<br>`로 줄바꿈 고정)
- 본문(`<p class="lead">`): Cold Jet 1986년 원천특허·1988년 세계 최초 상용화 + 바테크 총판 역할 설명으로 교체(3줄, `<br>` 2개로 줄바꿈 고정)
- 버튼("견적문의" · "데모 테스트 신청") 2개 제거, 빈 `.actions` div도 삭제
- **배치**: 사용자가 그려준 영역(좌 4.5vw 지점, 화면 하단에서 최소 112px/11.5vh 위)에 들어가도록 `.hero .wrap`을 `position: absolute`로 전환 — `left: 4.5vw; bottom: max(11.5vh, 112px); width: min(62vw, 1020px);` + `display:flex; flex-direction:column; justify-content:flex-end`(내용이 늘어나면 아래(SCROLL DOWN 인디케이터) 침범 없이 위로 확장)
- 글자 크기 축소: `h1` `clamp(26px, 2.9vw, 40px)`, `p.lead` `clamp(13px, 1vw, 15.5px)` — 좁아진 박스에 맞춤. 둘 다 `word-break: keep-all`로 "기술," 같은 단어가 줄 중간에 끊기는 것 방지
- 820px 이하 모바일: `.hero .wrap`을 `position: static`으로 되돌려 기존 모바일 흐름 유지

**c) 홈페이지 전용 — 헤더 투명화 (961px 이상)**
- 히어로 영상 위에 있는 동안(`.home .site-header:not(.header-solid):not(:hover)`) 헤더의 흰 반투명 배경·테두리·그림자·블러를 모두 제거해 투명하게, 로고·메뉴 글자는 흰색 + text-shadow로 전환
- 마우스를 헤더에 올리면(`:hover`) 즉시 원래 흰 배경으로 복귀
- `assets/js/main.js`: `.home .hero`의 bottom이 헤더 높이(76px) 이하로 올라오면(= 히어로를 지나 스크롤) `header-solid` 클래스를 붙여 흰 배경으로 고정 전환 — 페이지 로드 시 1회 + scroll 이벤트로 갱신

**d) 블라스터 히어로 영상 삽입 방식을 펠렛타이저와 동일하게 통일 (products/blaster/index.html)**
- 스테이지를 16:9(`56.25vw` 캡)에서 21:9(`42.86vw` 캡)로 전환 — `assets/css/style.css`의 공용 규칙(`.bls-hero-stage, .pel-hero-stage, .rec-hero-stage, .sup-hero-stage, .aut-hero-stage`)에 `.bls-hero-stage` 합류, `.bls-hero-stage .hero-fit { aspect-ratio: 21/9 }` 추가
- `<video>`의 `data-buffer="100" data-pan-scale="1.08" data-no-blur="true"` → `data-buffer="0" data-pan-scale="1"`(확대·블러 제거, 펠렛타이저와 동일)
- 641~1100px 구간 전용 미디어쿼리 추가: 이 구간만 16:9로 복귀(다른 21:9 히어로 페이지와 동일한 패턴)

**e) 히어로 영상 저용량 재교체 (§13 영상들 중 3개)**
- `assets/video/recovery-hero.mp4`, `assets/video/blaster-hero-banner.mp4`, `assets/video/pelletizer-hero.mp4` — 사용자가 용량을 낮춰 다시 제공한 버전으로 재교체(경로·파일명 동일, HTML 변경 없음)

**f) 블라스터 히어로 포스터 이미지 교체 (2026-10-02)**
- 증상: 영상 로드 전 옛 `poster`(`blaster-catalog-hero-natural.png`, 구 영상/이미지 기반)가 잠깐 노출된 뒤 새 영상으로 전환되는 깜빡임
- 신규 영상(`blaster-hero-banner.mp4`)의 첫 프레임을 추출해 `assets/img/blaster-hero-poster.jpg`(2206×946)로 신규 생성 → 번들에 포함, 신규 경로이므로 저장소에 **추가**
- `products/blaster/index.html` 히어로 `<video poster="...">` 값을 `blaster-catalog-hero-natural.png` → `blaster-hero-poster.jpg`로 변경(해당 줄 1곳만)

### 15. 히어로 영상 포스터 이미지 전면 교체 (메인 + 나머지 제품 페이지, 2026-10-02)

- 증상: §14-f)와 동일한 문제가 메인 페이지 및 펠렛타이저·리커버리·자동화·공급·노즐 히어로에도 있었음 — 영상 로드 전 옛 포스터(이전 영상/다른 제품 사진 기반)가 잠깐 보인 뒤 새 영상으로 전환되는 깜빡임
- 해결: 각 페이지의 **현재 히어로 영상 파일에서 첫 프레임을 추출**해 신규 포스터 이미지로 교체/추가. 영상 자체는 변경 없음
- `index.html`: `assets/video/main-hero-poster.jpg`를 새 `main-hero.mp4`의 첫 프레임으로 **덮어쓰기**(경로·HTML 동일, 파일 내용만 교체)
- `products/pelletizer/index.html`: `<video class="pel-hero-video">`에 `poster="../../assets/img/pelletizer-hero-poster.jpg"` **신규 추가**(기존엔 poster 속성 없었음)
- `products/recovery/index.html`: `<video class="rec-hero-video">`에 `poster="../../assets/img/recovery-hero-poster.jpg"` **신규 추가**
- `products/automation.html`: `<video class="aut-hero-video">`에 `poster="../assets/img/automation-hero-poster.jpg"` **신규 추가**
- `products/supply.html`: `<video>`에 `poster="../assets/img/supply-hero-poster.jpg"` **신규 추가**
- `products/nozzle.html`: 기존 `poster="../assets/img/blaster-detail-poster.png"`(블라스터 사진이 잘못 걸려 있었음) → `poster="../assets/img/nozzle-hero-poster.jpg"`로 **교체**
- 신규 이미지 5개(모두 번들에 포함, 저장소에 **추가**): `assets/img/pelletizer-hero-poster.jpg`, `assets/img/recovery-hero-poster.jpg`, `assets/img/automation-hero-poster.jpg`, `assets/img/supply-hero-poster.jpg`, `assets/img/nozzle-hero-poster.jpg`

### 16. 장비비교·구매프로세스 히어로 영상 + 히어로 영상 필터 전면 제거 (2026-10-02)

**a) 장비 비교·추천받기 히어로를 정지 이미지 → 영상으로 (`products/compare-equip.html`)**
- `<img class="subhero-parallax-img" src="../assets/img/pelletizer-category-pellet-lineup.jpg" …>` → `<video class="subhero-parallax-img aut-hero-video" autoplay muted loop playsinline preload="auto" poster="https://images.pexels.com/videos/7735496/…" data-buffer="0" data-pan-scale="1">` + `<source src="https://videos.pexels.com/video-files/7735496/7735496-hd_1280_720_25fps.mp4">`
- 영상: Pexels 무료 "Low Angle Shot of People Having a Meeting"(Mikhail Nilov, Pexels License — 출처 표기 불필요). 용량 때문에 720p(3.0MB) 변형 사용(1080p는 7.1MB). **현재 Pexels CDN 핫링크** — 추후 로컬 파일(`assets/video/compare-equip-hero.mp4`)로 교체 예정(미해결 참고)
- `assets/css/compare-equip-page.css`: `.eqf-hero-stage::after` 어두운 틴트(.86) 규칙 삭제(주석으로 대체) → 공용 `.subhero-parallax::after` 사용; `.eqf-hero-stage .hero-fit::before { display:none }` 추가; 641~1100px 16:9 폴백 미디어쿼리 추가(다른 영상 페이지와 동일 로직)

**b) 구매프로세스 히어로 필터 제거 (`assets/css/process-page.css`)**
- `.prc-hero-stage::after` 어두운 틴트(.84) 규칙 삭제 → 공용 틴트 사용; `.prc-hero-stage .subhero-parallax-img`에 `filter:none` 추가; `.prc-hero-stage .hero-fit::before { display:none }` 추가. HTML 변경 없음(영상은 이미 Pexels 핫링크 상태)

**c) 히어로 영상 공통 — 블러·색 필터 전면 제거**
- `assets/js/main.js` (서브히어로 스크롤 블러 블록): `var noBlur = subheroImg.dataset.noBlur === "true";` → `… || subheroImg.tagName === "VIDEO";` — `<video>` 히어로는 스크롤 blur 필터 대상에서 제외(필터 레이어 자체가 영상을 뿌였게 만들었음). 정지 이미지 히어로는 기존 동작 유지
- `assets/css/style.css`: `video.bls-hero-video` / `img.bls-hero-video`의 `filter: saturate(.92) brightness(.97) hue-rotate(-4deg)` 제거; `.subhero-parallax-img`의 `will-change: transform, filter` → `will-change: transform`; `.hero-fit video.subhero-parallax-img { will-change: transform; filter: none; }` 추가

### 17. 메가메뉴 미리보기 — 라벨 비침 버그 수정 + 블라스터 항목 영상화 (2026-10-02)

**a) 버그 수정 — 이미지 뒤로 항목명 텍스트가 비침 (`assets/js/main.js` 메가메뉴 `selectItem`)**
- 사진 없는 항목(img-ph 플레이스홀더)을 거쳐 사진 있는 항목으로 돌아오면 `previewImg.textContent = label`로 넣은 텍스트 노드가 지워지지 않고 이미지 뒤에 남던 문제
- 수정: 이미지/영상 분기 진입 시 `previewImg.childNodes` 중 텍스트 노드(nodeType 3) 제거 코드 1줄 추가

**b) 서브메뉴 미리보기 영상 지원 (신규 기능)**
- 마크업: 메가메뉴 `<a>`에 선택 속성 `data-video="…mp4"` + `data-poster="…jpg"` 추가 가능. 있으면 `data-img` 대신 무음 루프 `<video>` 레이어를 생성, 없으면 기존 사진 동작 그대로
- `assets/js/main.js`: `selectItem`에서 `videoUrl`/`posterUrl` 읽기 → `<video class="megamenu-preview-img-bg is-video" muted loop autoplay playsinline preload="auto" poster>` 생성 후 `play()`; 이전 레이어가 video면 `pause()`·`removeAttribute("src")`·`load()` 후 제거(메모리 해제). 초기화 끝에 **초기 활성 항목에 data-video가 있으면 `selectItem(activeItem, a)`를 한 번 호출** — 메뉴를 열자마자(항목 호버 전) 정적 사진 대신 영상이 재생되도록
- `assets/css/style.css`: `.megamenu-preview-img-bg.is-shown` 다음 줄에 `video.megamenu-preview-img-bg { width:100%; height:100%; object-fit:contain; object-position:center; background:transparent; display:block; }` 추가
- 블라스터 항목 적용: 메가메뉴가 있는 **전 페이지 92개 HTML**의 `<a href="…products/blaster/index.html" … data-img="…stackdo-blaster.jpg">`에 `data-video="…assets/video/submenu-blaster.mp4" data-poster="…assets/img/submenu-blaster-poster.jpg"` 추가(상대경로는 각 페이지 깊이에 맞춤). `cases/library.html`만 메가메뉴 없어 제외. 이 변경 때문에 번들에 사이트 HTML 전체가 들어있음 — **그대로 덮어쓰기**
- 신규 파일(저장소에 **추가**): `assets/video/submenu-blaster.mp4`(960×720, 6초, 0.44MB, 무음), `assets/img/submenu-blaster-poster.jpg`(첫 프레임)
- 다른 서브메뉴(펠렛타이저·리커버리·자동화·노즐·공급 등) 영상은 발주자가 같은 규격(960×720, ≤1MB, MP4 H.264 무음)으로 제공 예정 — 동일 패턴으로 `data-video`/`data-poster`만 추가하면 됨

### 18. 서브메뉴 영상 확대 적용 + 사전 로드 (2026-10-02)

**a) 서브메뉴 영상 추가 (전 페이지 92개 HTML, §17-b 패턴 동일)**
- ~~세척가이드 › "드라이아이스 세척의 이해"(`cleaning/guide.html` 링크): `submenu-guide.mp4`~~ → **발주자 요청으로 되돌림(2026-10-02)**: 전 페이지에서 `data-video`/`data-poster` 제거, 원래 `data-img="…guide-principle-thumb.jpg"`만 유지. `submenu-guide.mp4`/`-poster.jpg` 파일은 미사용 상태로 남김(삭제 가능)
- 장비 › 펠렛타이저(`products/pelletizer/index.html` 링크): `submenu-pelletizer.mp4` / `submenu-pelletizer-poster.jpg` (8초, 0.34MB)
- 장비 › CO2 리커버리(`products/recovery/index.html` 링크, 기존 data-img 없던 항목): `submenu-recovery.mp4` / `submenu-recovery-poster.jpg` (6초, 0.55MB)
- 장비 › 드라이아이스 공급(`products/supply.html` 링크): `submenu-supply.mp4` / `submenu-supply-poster.jpg` (8.5초, 0.54MB)
- 장비 › 장비 비교·추천받기(`products/compare-equip.html` 링크): 해당 페이지 히어로 영상 재사용 — `data-video="https://videos.pexels.com/video-files/7735496/7735496-hd_1280_720_25fps.mp4" data-poster="https://images.pexels.com/videos/7735496/pexels-photo-7735496.jpeg?auto=compress&amp;cs=tinysrgb&amp;w=960" data-fit="cover"`
- 장비 › 구매 프로세스 안내(`products/process.html` 링크): 히어로 재사용 — `data-video="https://videos.pexels.com/video-files/8170599/8170599-hd_1280_720_25fps.mp4" data-poster="https://images.pexels.com/videos/8170599/pexels-photo-8170599.jpeg?auto=compress&amp;cs=tinysrgb&amp;w=960" data-fit="cover"`
- 신규 파일 8개(저장소에 **추가**): `assets/video/submenu-{guide,pelletizer,recovery,supply}.mp4`, `assets/img/submenu-{guide,pelletizer,recovery,supply}-poster.jpg`. 펠렛타이저·리커버리는 발주자가 저용량 버전으로 재제공해 덮어썼음(경로 동일)

**b) `data-fit="cover"` 속성 (신규)**
- 16:9 등 비율이 다른 영상을 4:3 미리보기 칸에 좌우 크롭으로 꿉 채움(파일은 그대로, 표시만 cover). 없으면 contain(960×720 소스는 어차피 꿉 참)
- `assets/js/main.js` `selectItem`: `bg.classList.toggle("is-cover", a.getAttribute("data-fit") === "cover")`
- `assets/css/style.css`: `video.megamenu-preview-img-bg.is-cover { object-fit: cover; }` 추가

**c) 서브메뉴 영상 사전 로드 풀 (`assets/js/main.js` 메가메뉴 블록)**
- 증상: 항목 호버 시점에 `<video>`를 생성·다운로드 시작해 재생까지 딜레이
- 수정: `window.__megamenuVideoPool`(URL → `<video>` 1개) + `getPoolVideo(url, poster)`; 페이지 로드 후 `requestIdleCallback`(timeout 2500ms, 미지원 시 setTimeout 1200ms)으로 메뉴 내 모든 `data-video`를 `preload="auto"`로 미리 로드. `selectItem`은 새 요소를 만들지 않고 풀 요소를 `appendChild` 후 `play()`; 이전 영상은 `pause()` + DOM 분리만(예전 `removeAttribute("src")`/`load()`로 버퍼를 버리던 코드 제거 → 되돌아와도 즉시 재생)
- 비용: 페이지당 백그라운드 약 8MB(로컬 6개 2.8MB + Pexels 2개 5.4MB), 브라우저 캐시로 페이지 간 재다운로드 없음. 모바일 데이터 우려 시 Pexels 2개만 메뉴 오픈 시 로드로 바꿀 수 있음(미해결 참고)

**d) 자동화 시스템·노즐·액세서리 서브메뉴 — 히어로 영상 재사용 (2026-10-02)**
- 장비비교·구매프로세스와 같은 방식: 전용 서브메뉴 파일 없이 해당 페이지 히어로 영상(21:9/16:9)을 `data-fit="cover"`로 4:3 칸에 크롭 표시
- 전 페이지 92개 HTML 메가메뉴에서 `data-img` 제거 후 교체:
  - 자동화 시스템(`products/automation.html` 링크): `data-img="…stackdo-automation.jpg"` 삭제 → `data-video="…assets/video/automation-hero.mp4" data-fit="cover" data-poster="…assets/img/automation-hero-poster.jpg"`
  - 노즐·액세서리(`products/nozzle.html` 링크): `data-img="…blaster-operator-t.png"` 삭제 → `data-video="…assets/video/nozzle-hero.mp4" data-fit="cover" data-poster="…assets/img/nozzle-hero-poster.jpg"`
- 신규 파일 없음(히어로 영상·포스터 재사용). 사전 로드 풀 비용 +2.1MB(automation 0.80 + nozzle 1.31) — 발주자가 960×720 저용량 버전을 주면 `submenu-automation.mp4`/`submenu-nozzle.mp4`로 교체 가능

### 19. 렌탈·세척테스트 메뉴 히어로 — 흐림·어두운 틴트 제거 (2026-10-02)
- 증상: 렌탈·데모 하위 5개 페이지 히어로가 뿌옇고 어두움 — 원인 3가지: ① 페이지 전용 `::after` 틴트가 상단 .84~.86, 본문 .5~.74로 과도 ② `data-pan-scale="1.06" data-buffer="60"` 확대 + 스크롤 블러(`data-blur-start="0.5"`) ③ demo.html 히어로 영상 `transform: scale(1.18)`
- HTML 5개(`rental/demo.html`, `demo-apply.html`, `apply.html`, `partners.html`, `vrental.html`): 히어로 `<img>`/`<video>`의 `data-buffer="60" data-pan-scale="1.06" data-blur-start="0.5"` → `data-buffer="0" data-pan-scale="1" data-no-blur="true"` (§14-d 블라스터와 동일 — 확대·스크롤 블러 없음, 원본 그대로)
- `assets/css/demo-page.css`: `.dm-hero-stage::after` 전용 틴트 삭제(공용 `.subhero-parallax::after` 사용); `.dm-hero-stage video.subhero-parallax-img { transform: scale(1.18) }` → `transform: none; filter: none`
- `assets/css/apply-page.css`: `.ap-hero-stage::after` 전용 틴트 삭제; `.ap-hero-stage .subhero-parallax-img`에 `filter: none`
- `assets/css/partners-page.css`: `.pt-hero-stage::after` 삭제; `.subhero-parallax-img`에 `filter: none`
- `assets/css/vrental-page.css`: `.vr-hero-stage::after` 삭제; `.subhero-parallax-img`에 `filter: none`
- 텍스트 가독성은 기존 반투명 글래스 박스(`.subhero-textbox`, rgba .5 + blur 10px)가 담당하므로 틴트 제거 후에도 유지됨

### 20. 기술·서비스 역량 페이지 — "직접 세척" 전제 수정 (company/capability.html, 2026-10-02)
- 배경: §9의 FIELD RECORD 사진 4장은 바테크 인력이 아니라 **바테크 렌탈 장비로 협력사가 수행한 현장** — 페이지 전체가 "직접 세척해 본 회사" 전제로 쓰여 있어 중심 메시지를 "조건을 찾아 끝까지 지원하는 회사"로 교체
- `<meta description>`, 히어로 h1/본문: "세척을 직접 해 본 회사" → "장비를 파는 데서 끝나지 않고, 조건을 찾아 끝까지 지원합니다" (연구소 시편 테스트 + 설치·교육·정비)
- 히어로 이미지: `vatek-field-heritage-locomotive-cleaning-graded.png` → `assets/img/guide-hero-work.jpg`(기존 파일, 금형 세척 조건 확인 장면); `data-buffer="0" data-pan-scale="1" data-no-blur="true"`로 확대·블러 제거
- 역량 02: "FIELD OPERATION / 현장 세척 실행" → "RENTAL & PARTNER SUPPORT / 렌탈 · 파트너 지원" (협력사·고객 현장에 렌탈 장비·확정 조건·운용 교육 제공, 작업은 파트너 수행)
- `#field`: "FIELD RECORD / 직접 세척한 기록" → "PARTNER FIELD / 파트너사가 수행한 현장" — 리드에 작업 주체(파트너)와 바테크 역할(장비·조건·교육·기술지원) 명시, 사진 4장·과제/방법 유지. 하단 링크 2개로(인증 서비스 파트너 → `rental/partners.html`, 케이스 스터디) — 신규 래퍼 `.cap-field-links`
- 히어로 점프 링크 "현장 기록" → "파트너사 현장"
- `assets/css/capability-page.css`: `.cap-hero-stage::after` 전용 틴트 삭제(공용 사용), `.subhero-parallax-img`에 `filter:none`, `.cap-field-links` 추가
- 사실 확인 완료 항목(발주자 답변): 바테크 인력이 실제 수행하는 현장 업무 = 유료 현장 데모 · 설치/시운전 · 운용 교육 · 방문 정비/A/S · 시스템 통합 설치 · (일부) 현장 세척 작업

### 21. 렌탈·데모 메뉴 › "장비 렌탈 (V RENTAL)" 서브메뉴 이미지 추가 (2026-10-02)
- 기존엔 이미지 없이 플레이스홀더(img-ph)만 표시되던 항목. 발주자 제공 이미지(960×720 WebP) 적용
- 전 페이지 92개 HTML(+handoff3)의 `<a href="…rental/vrental.html" data-desc="…">`에 `data-img="…assets/img/submenu-vrental.webp"` 추가
- 신규 파일(저장소에 **추가**): `assets/img/submenu-vrental.webp`
- **메가메뉴 초기 미리보기 동기화** (`assets/js/main.js`): 각 메가메뉴의 `.megamenu-preview-img-bg`는 HTML에 정적 `background-image`가 하드코딩되어 있어(렌탈 메뉴는 구 `stackdo-rental.jpg`) 항목 속성과 어긋남. 초기화 시 활성 항목(`is-active`, 없으면 첫 항목)의 `data-video` **또는 `data-img`**가 있으면 `selectItem`을 한 번 호출해 미리보기를 항목 속성과 일치시키도록 조건 확장(기존엔 data-video만). 이제 상위 항목의 이미지/영상이 메뉴를 열자마자 표시되며, HTML의 정적 배경은 JS 실패 시 폴백 역할만 함

### 22. V RENTAL 히어로 이미지 교체 + 블라스터식 좌측 텍스트 구성 (rental/vrental.html, 2026-10-02)
- 히어로 `<img>` `src`: `stackdo-rental.jpg`(16:9) → **`assets/img/vrental-hero.webp`**(21:9, 2206×946, 발주자 제공 — 블라스터 히어로와 동일 해상도; 1915×821 1차본을 같은 경로로 덮어씀). `stackdo-rental.jpg` 파일 자체는 index.html·rental/index.html·rental/apply.html·products/index.html에서 계속 사용하므로 **삭제하지 않음**
- `assets/css/vrental-page.css`: 텍스트 박스를 블라스터 히어로와 같은 좌측 배치(`left:5%`, `top:44%`, `text-align:left`, `max-width:min(440px,28cqw)` — 이미지의 빈 영역이 좌측 약 33%뿐이라 V 레터링과 겹치지 않도록 폭·높이 제한, h1/본문 크기 축소)로 변경, 태그 줄 좌측 정렬(641~1100px 구간은 `object-position:0% 50%`로 우측만 크롭해 좌측 빈 영역 유지 + 박스 `max-width:min(300px,32vw)`, `top:38%`, 태그 숨김); `.vr-hero-stage::after` 상단 스톱만 .55로 — 밝은 벽 위 브레드크럼 가독성; 641~1100px 구간 16:9 복귀 미디어쿼리 추가(`.bls-hero-stage`와 동일 패턴); `object-position` 50% 50%
- 신규 파일(저장소에 **추가**): `assets/img/vrental-hero.webp`

### 23. 데모 테스트 히어로 — 영상 → 21:9 이미지, 블라스터식 좌측 텍스트 구성 (rental/demo.html, 2026-10-02)
- 히어로 `<video src="pcs-demo-namecard.mp4" poster="guide-hero-work.jpg">` → `<img src="../assets/img/demo-hero.webp">`(21:9, 2206×946, 발주자 제공). `data-buffer="0" data-pan-scale="1" data-no-blur="true"` 유지. `pcs-demo-namecard.mp4`는 본문 `.dm-way-media`/`.dm-detail-media`에서 계속 쓰이는지 확인 후 삭제 여부 결정(이 작업에선 파일 유지)
- `assets/css/demo-page.css`: §22 V RENTAL과 동일 패턴 — 텍스트 박스 좌측(`left:5%`, `top:46%`, `max-width:min(520px,38cqw)`; 이미지 빈 영역이 좌측 ~45%라 V RENTAL보다 넓게), `::after` 상단 스톱 .55, 641~1100px 구간 16:9 복귀 + `object-position:0% 50%` + 점프 링크 숨김. 기존 `video.subhero-parallax-img` 규칙 삭제
- 신규 파일(저장소에 **추가**): `assets/img/demo-hero.webp`

### 24. 렌탈·데모 메뉴 › "데모 테스트" 서브메뉴 이미지 추가 (2026-10-02)
- 기존엔 이미지 없이 플레이스홀더만 표시되던 항목. 발주자 제공 이미지(960×720 WebP) 적용 — §21과 동일 패턴
- 전 페이지 92개 HTML(+handoff3)의 `<a href="…rental/demo.html" data-desc="…">`에 `data-img="…assets/img/submenu-demo.webp"` 추가
- 신규 파일(저장소에 **추가**): `assets/img/submenu-demo.webp`

### 25. 세척용역(인증 파트너) 히어로 + 서브메뉴 이미지 (rental/partners.html, 2026-10-03)
- 히어로 `<img src="partner-jpmotors-lift.png">` → **`assets/img/partners-hero.webp`**(21:9, 2206×946, 발주자 제공 "OUR PARTNERS" 인증서 연출). `partner-jpmotors-lift.png`는 본문 파트너 카드에서 계속 사용하므로 유지
- `assets/css/partners-page.css`: §22와 동일 패턴 — 텍스트 박스 좌측(`left:5%`, `top:46%`, `max-width:min(440px,28cqw)`; 레터링이 스테이지 ~33%부터라 좁은 폭), `::after` 상단 .55, 641~1100px 16:9 복귀 + `object-position:0% 50%` + 본문 숨김. 기존 `@media (max-width:1000px)` 본문 숨김 규칙은 새 미디어쿼리에 흡수
- 서브메뉴: 전 페이지 92개 HTML(+handoff3)의 `<a href="…rental/partners.html" data-desc="…">`에 `data-img="…assets/img/submenu-partners.webp"` 추가(기존 이미지 없던 항목)
- 신규 파일(저장소에 **추가**): `assets/img/partners-hero.webp`, `assets/img/submenu-partners.webp`

### 26. 렌탈·데모 메뉴 › "장비 렌탈" 항목 우측에 V RENTAL 로고 (2026-10-03)
- 발주자 제공 로고(1952×722 PNG, "Simple but Powerful" 태그라인 포함)에서 태그라인 제거 + 흰 배경 투명 처리 + **RENTAL(잎·TM 포함)을 V와 같은 높이로 확대 재조합**해 `assets/img/vrental-logo.png`(695×160, 투명 PNG) 생성
- 전 페이지 92개 HTML(+handoff3)의 `<a href="…rental/vrental.html" …>장비 렌탈</a>` → `장비 렌탈<img class="mi-logo" src="…assets/img/vrental-logo.png" alt="V RENTAL" />`
- `assets/css/style.css`: `.megamenu-index-item a .mi-logo { height:1.55em; vertical-align:-0.42em; margin-left:10px }` — 1em은 너무 작아 글자 높이의 1.55배(≈22px)로, 모바일 아코디언에서도 em 기준 자동 추종
- **상세 카드(우측 파란 `.megamenu-detail`) 제목에도 로고 표시**: `main.js` `selectItem`에서 제목 갱신 시 항목의 `.mi-logo`가 있으면 `src`의 `.png`→`-white.png`로 바꾼 `<img class="megamenu-detail-logo">`를 제목 뒤에 추가(파란 배경이라 흰색 버전). CSS `.megamenu-detail-title .megamenu-detail-logo { height:1.45em; vertical-align:-0.38em; margin-left:10px }`
- 신규 파일(저장소에 **추가**): `assets/img/vrental-logo.png`, `assets/img/vrental-logo-white.png`(검정 → 흰색, 잎 녹색 유지)

### 27. 렌탈 신청 히어로 + 서브메뉴 이미지 (rental/apply.html, 2026-10-03)
- 히어로 `<img src="stackdo-rental.jpg">` → **`assets/img/apply-hero.webp`**(21:9, 2206×946, 발주자 제공). `stackdo-rental.jpg`는 index.html·rental/index.html·products/index.html에서 계속 사용하므로 유지
- `rental/apply.html` 히어로 섹션에 전용 클래스 `ap-rental-hero` 추가 → `assets/css/apply-page.css`에서 이 클래스에만 적용(같은 `.ap-hero-stage`를 쓰는 `demo-apply.html`은 영향 없음): `height:min(calc(100vh - 76px),42.86vw)`(기존 `.ap-hero-stage` 38vw 높이는 21:9 이미지를 크롭하므로 공통 21:9 높이로 덮어씀), 텍스트 박스 좌측(`left:4%`, `max-width:min(400px,27cqw)` — 이미지 좌측 ~35%만 비어 있음), `::after` 상단 .45, 641~1100px 16:9 복귀 + `object-position:0% 50%`
- 서브메뉴: 전 페이지 92개 HTML(+handoff3)의 `<a href="…rental/apply.html" data-desc="…">`에 `data-img="…assets/img/submenu-apply.webp"` 추가(기존 이미지 없던 항목)
- 신규 파일(저장소에 **추가**): `assets/img/apply-hero.webp`, `assets/img/submenu-apply.webp`
- **브레드크럼 가독성(밝은 21:9 히어로 4곳 공통: apply·vrental·demo·partners)**: 각 페이지 CSS의 `::after` 상단 그라데이션을 .66→.34(14%)→.08(32%)로 강화하고 `.subhero-breadcrumb`/`a`를 흰색 + 이중 text-shadow로 지정

### 28. 대메뉴(1단) 클릭 비활성화 — 서브메뉴만 사용 (2026-10-03)
- 발주자 결정: 대메뉴 index 페이지(`cleaning/index.html`, `products/index.html`, `cases/index.html`, `rental/index.html`, `support/index.html`, `company/index.html`)는 필요 없음 → 대메뉴는 메가메뉴를 여는 트리거로만 동작
- `assets/js/main.js`: 메가메뉴를 가진 `.main-nav > ul > li > a` 전부에 `click` → `preventDefault()`(모든 폭), `role="button"` `aria-haspopup="true"` `.is-mega-trigger` 부여. 모바일(≤960)은 기존대로 탭 시 아코디언 토글
- `assets/css/style.css`: `.is-mega-trigger { cursor:default }`(모바일은 pointer 유지)
- HTML `href`는 그대로 둠(92개 페이지 수정 없이 JS 한 곳에서 제어; JS 꺼진 환경에선 기존 index 페이지로 폴백). 브레드크럼의 "렌탈 · 데모" 등 index 링크, 푸터 링크는 이번 범위 밖 — 해당 index 페이지를 실제로 삭제하려면 이 링크들 정리가 선행되어야 함(미해결 참고)

### 29. 서브메뉴 미리보기 이미지 즉시 표시 (2026-10-03)
- 증상: 서브메뉴를 오갈 때 이미지가 한 박자 늦게 뜸(장비 메뉴는 빠름). 원인 ① `data-img` 이미지는 첫 호버 때 비로소 다운로드(영상만 사전 로드 풀 대상) ② 레이어 전환 애니메이션 .28s
- `assets/js/main.js`: `warmVideos`에서 `data-img`/`data-poster`도 `new Image()`로 유휴 시 사전 로드(`window.__megamenuImgPool`, 전 메뉴 공유·중복 방지)
- `assets/css/style.css`: `.megamenu-preview-img-bg` 전환 opacity .28s→.14s, transform .28s→.18s, 시작 스케일 1.04→1.02

### 30. 데모 테스트 신청 히어로 + 서브메뉴 이미지 (rental/demo-apply.html, 2026-10-03)
- 히어로 `<img src="guide-hero-work.jpg">` → **`assets/img/demo-apply-hero.webp`**(21:9, 2206×946, 발주자 제공 — 고객이 시편을 연구소 담당자에게 건네는 장면). `guide-hero-work.jpg`는 capability 등 다른 페이지에서 계속 사용
- 섹션에 `ap-rental-hero ap-demo-hero` 클래스 추가 → §27의 21:9 좌측 텍스트 레이아웃 재사용 + `.ap-demo-hero`로 박스 더 좁게(`max-width:min(360px,24cqw)`; 이미지 좌측 빈 영역 ~25%)
- 서브메뉴: 전 페이지 92개 HTML(+handoff3)의 `<a href="…rental/demo-apply.html" data-desc="…">`에 `data-img="…assets/img/submenu-demo-apply.webp"` 추가(기존 이미지 없던 항목). 이로써 렌탈·데모 메뉴 5개 항목 모두 이미지 보유
- 신규 파일(저장소에 **추가**): `assets/img/demo-apply-hero.webp`, `assets/img/submenu-demo-apply.webp`
- 히어로 아래 첫 섹션 `#apply`에 `rec-cover` 클래스 추가 → 렌탈 신청(`#flow`)과 동일하게 히어로 위로 64px 겹쳐 올라오는 상단 라운드(72px) 카드. `apply-page.css`에 `.ap-demo-hero + .plt-section.rec-cover { border-top:none }`

### 31. 데모 테스트 › 세 가지 방법 카드 일러스트 교체 (rental/demo.html, 2026-10-03)
- `.dm-way-media.is-illust` 3장: 원형 아이콘(`demo-way-{1,2,3}-*.png`) → 발주자 제공 4:3 라인 일러스트 **`assets/img/demo-way-1-ship.webp`**(시편 포장·발송) / **`demo-way-2-lab.webp`**(연구소 방문) / **`demo-way-3-onsite.webp`**(현장 방문, 블라스터 이동). 각 960×720 WebP
- `assets/css/demo-page.css`: `.dm-way-media.is-illust img` `object-fit: contain; padding: 6% 0 4%` → `cover; padding: 0` (새 일러스트가 자체 흰 배경이라 카드 16:11 칸을 꽉 채움, 상하 소폭 크롭). FREE/PAID 배지·호버 확대 유지
- 기존 PNG 3장은 다른 페이지에서 미사용이면 삭제 가능(이 작업에선 유지)
- **시편 발송(`#ship`) 팁에 비용 안내 추가**(`.dm-tip.is-warn`): 시편이 많거나 시간이 오래 걸리는 제품, 오염물이 많이 발생하는 세척은 필요에 따라 비용이 청구될 수 있으며 진행 전 사전 안내. `#lab`(연구소로 오세요)에도 동일 문구 추가. ※ 제목 "무료" 배지/`FREE`와 병기되므로 문구 수위(예: "기본 무료") 발주자 확인 필요
- **HOW EACH WORKS(`#ship`/`#lab`/`#onsite`)의 `.dm-detail-media` 3칸도 같은 일러스트로 교체**: ① `<video pcs-demo-namecard.mp4>` → `demo-way-1-ship.webp`(캡션 "시편 포장 · 연구소로 발송") ② `vatek-building.jpg` → `demo-way-2-lab.webp` ③ 기존 미디어 → `demo-way-3-onsite.webp`. 각 칸에 `is-illust` 클래스; CSS `.dm-detail-media.is-illust { background:#fff; border }` + 캡션을 어두운 필(rgba .72)로 — 밝은 일러스트 위 가독성. 이로써 `pcs-demo-namecard.mp4`는 demo.html에서 미사용(다른 페이지 확인 후 삭제 가능)

### 32. 기술지원 안내 페이지 본문 신규 작성 (support/techsupport.html, 2026-10-03, v2)
- 1차 작성본(고장 접수·셀프 체크·정품 부품 = A/S 성격)은 발주자 지적으로 **폐기**. A/S는 `education.html#aftersales`가 담당하므로 이 페이지는 "장비 수리가 아니라 세척이 되게 만드는" **응용 기술지원**으로 재정의(발주자 답변 기반: 범위 5개, 대상 3군, 비용 표기 없음)
- 구성: ① 히어로(21:9 영상 `assets/video/automation-hero.mp4` + `automation-hero-poster.jpg` 재사용 — 로봇 셀 금형 세척; 500×500 webp는 해상도 부족으로 교체; 점프 링크 4개) ② `#who` 대상 3군 — 기존 고객(새 대상·조건 변경) / 세척용역 파트너사 / 자동화·설비 업체(SI) ③ `#areas` 네 영역 행 카드("이런 때 → 하는 일 → 받으시는 것"): 세척 조건 설계(→조건 시트) / 공정 적용 검토(사이클 타임·소비량·압축공기 →적용 검토서) / 자동화·라인 통합 기술 검토(→구성안·인터페이스 요구사항) / 안전·환경 기준 안내(CO₂ 환기 등 →안전 체크리스트) ④ `#how` 다크 — 문의 시 알려 주실 것 6항(대상·오염물·모재·현장 조건·목표·보유 장비) + 진행 4단계(1차 검토 → 연구소 확인 → 조건·구성 제안 → 현장 적용 확인) ⑤ `#coldjet` 05 Cold Jet 본사 기술 자문 연결 + `vatek-coldjet-photo-1.jpg` ⑥ 최종 CTA(시편 테스트 신청 · 이메일 제목 "[기술지원] 대상/오염물" 프리필 · A/S 접수는 교육·A/S로 안내 링크)
- CSS `assets/css/techsupport-page.css` v2 전면 교체(ts-who / ts-row / ts-request / ts-coldjet). `pelletizer/recovery/compare-equip/capability-page.css` 로드(cap-vars·cap-steps·cap-hero-jump 재사용)
- `<title>` "기술지원 안내", `<meta description>` 갱신
- **발주자 확인 필요**: ① "받으시는 것" 문서명(조건 시트 · 적용 검토서 · 구성안 · 안전 체크리스트)이 실제 제공 형태와 맞는지 ② Cold Jet 본사 자동화팀 설계 검토 · 적용 사례 데이터 조회 문구 ③ 사진 캡션(`vatek-coldjet-photo-1.jpg` 인물·장소)
- 메가메뉴 "기술지원 안내" 항목은 아직 `data-img` 없음 — 서브메뉴용 960×720 이미지 주시면 적용

### 33. 교육·A/S 히어로 + 서브메뉴 이미지 (support/education.html, 2026-10-03)
- 히어로 `<img src="guide-hero-work.jpg" data-buffer="60" data-pan-scale="1.06" data-blur-start="0.5">` → **`assets/img/education-hero.webp`**(21:9, 2206×946, 발주자 제공 — 공구함·서비스 매뉴얼·멀티미터·씰). `data-buffer="0" data-pan-scale="1" data-no-blur="true"`로 확대·블러 제거. `guide-hero-work.jpg`는 capability.html 등에서 계속 사용하므로 파일 유지
- `assets/css/education-page.css`: §22와 동일 패턴 — 텍스트 박스 좌측(`left:5%`, `top:46%`, `max-width:min(520px,36cqw)`), 점프 링크 좌측 정렬, `::after` 상단 .66 그라데이션 + 브레드크럼 흰색·이중 그림자, 641~1100px 16:9 복귀 + `object-position:0% 50%`
- 서브메뉴: 전 페이지 92개 HTML(+handoff3)의 `<a href="…support/education.html" data-desc="…">`에 `data-img="…assets/img/submenu-education.webp"` 추가. 기술지원·자료 메가메뉴의 초기 미리보기 플레이스홀더(`.img-ph` "교육·A/S")도 이미지 배경으로 교체
- 신규 파일(저장소에 **추가**): `assets/img/education-hero.webp`, `assets/img/submenu-education.webp`

### 33. 교육·A/S 히어로 + 서브메뉴 이미지 교체 (2026-10-08)
- 발주자 제공 이미지로 **같은 경로 덮어쓰기**(기존 파일 삭제와 동일, 잔존 파일 없음): `assets/img/education-hero.webp`(21:9, 2206×946), `assets/img/submenu-education.webp`(960×720). HTML `src`/`data-img` 경로 변경 없음
- 구도가 기존과 동일(좌측 ~40% 작업대·배경 장비, 우측 공구함·SERVICE MANUAL)해 `education-page.css` 레이아웃 규칙 변경 없음. `support/education.html` 히어로 `alt`만 갱신
- **발주자 확인 필요**: 제공 이미지의 공구함에 **DeWALT 상표**가 선명하게 보임(히어로 + 서브메뉴). 타사 브랜드 노출이 의도된 것인지 확인 — 문제가 되면 상표 제거본 필요

## 미해결 사항 (코드 작업 아님 — 발주자 확인 필요)
- **대메뉴 index 페이지 삭제 여부**: §28로 대메뉴 클릭은 막았지만 6개 index 페이지 파일과 브레드크럼·푸터의 index 링크는 남아 있음. 삭제하려면 ① 브레드크럼 2단계 링크를 비링크 텍스트로 ② 푸터·본문의 index.html 참조 정리 ③ 파일 삭제 + 리다이렉트 — 진행 여부 확인 필요

- 서브메뉴 영상 사전 로드가 Pexels 2개(5.4MB)까지 포함 — 발주자가 해당 히어로 영상을 960×720 저용량으로 편집해 제공하면 로컬 파일로 교체 예정
- 장비비교(`products/compare-equip.html`)·구매프로세스(`products/process.html`) 히어로 영상이 Pexels CDN 핫링크 상태 — 발주자가 다운로드·저용량화한 파일을 주면 로컬 경로 + 첫 프레임 포스터로 교체 예정
- `rental/apply.html` 사업자번호 형식·체크섬 검증 버튼 미구현 (서버 연동 시점)
- `support/catalog.html` 카탈로그 PDF 파일 대기
- A/S 접수·당일 회신 시간 문구 확정 필요 (education.html)
- 이메일 주소 통일: `company/about.html` 개요표 `info@vatek.net` vs 푸터 `sales@vatek.co.kr`
- 바테크 사진(사무실·연구소·창고 5장) 원본 파일 대기
- `company/capability.html` 현장 기록 4건의 과제/방법 서술, TIER 2(Cold Jet) 지원 항목 사실 확인
- `support/techsupport.html`은 구형 스텁 — 메뉴에 노출되므로 내용 보강 권장
- 데모 신청·렌탈 신청 폼은 `mailto:` 임시 방식 (서버 연동 전)

## 저장소 경로 매핑
이 zip의 파일 경로는 저장소 루트 기준 경로와 **동일**합니다. `uploads/`(작업용 임시 파일)는 번들에서 제외했습니다.

## 참고
`github.md`에 최신 커밋 SHA는 기록되어 있지 않습니다 — 병합 전 저장소의 현재 HEAD와 diff로 충돌 여부를 확인하세요.

### 34. 데모 테스트 히어로 + 서브메뉴 이미지 교체 (rental/demo.html, 2026-10-10)
- 발주자 제공 신규 이미지(VATEK 작업복 + 금속 "TEST" 글자, 1584×672 원본)로 교체. 히어로 2206×946(21:9 중앙 크롭) / 서브메뉴 960×720(4:3, TEST 글자 중심 크롭).
- 파일명 변경: `demo-hero.webp` → `demo-hero-test.webp`, `submenu-demo.webp` → `submenu-demo-test.webp` (구 파일 삭제). 전 HTML의 `<img src>` 및 `data-img` 참조 일괄 갱신(+handoff3/products/recovery/ 5개 포함).
- MANIFEST.sha256.txt: 이미지 2개 항목 교체. HTML 항목 해시는 참조 문자열 변경으로 달라졌으므로 커밋 전 `sha256sum` 재생성 필요.
- §23·§24의 파일명은 본 항목으로 대체됨.

### 35. 교육·A/S 히어로 + 서브메뉴 이미지 교체 (support/education.html, 2026-10-10)
- 발주자 제공 신규 이미지(브랜드 로고 없는 공구함·서비스 매뉴얼·멀티미터, 3120×1328 원본)로 교체. 히어로 2206×946(21:9 중앙 크롭) / 서브메뉴 960×720(공구함·매뉴얼 중심 크롭).
- 파일명 변경: `education-hero.webp` → `education-hero-v2.webp`, `submenu-education.webp` → `submenu-education-v2.webp` (구 파일 삭제). 전 HTML `<img src>`·`data-img`·프리뷰 `background-image` 참조 일괄 갱신(+handoff3).
- §33 미결 사항이었던 DEWALT 로고 상표 이슈 해소(새 이미지에 로고 없음).
- MANIFEST.sha256.txt: 이미지 2개 항목 교체(HTML 해시는 §34와 같이 커밋 전 재생성).

### 36. 기술지원 안내 히어로 신규 이미지 + 서브메뉴 프리뷰 추가 (support/techsupport.html, 2026-10-11)
- 발주자 제공 이미지(기술 검토 회의실: 화이트보드 금형 스케치·발표자·테이블 위 금형 시편, 1584×672 PNG 1.8MB)를 웹용으로 압축.
  - `assets/img/techsupport-hero.webp` 2206×946(21:9 중앙 크롭, q0.82, 약 91KB)
  - `assets/img/submenu-techsupport.webp` 960×720(4:3, 화이트보드+발표자+시편 중심 크롭, 약 39KB)
- 히어로: 임시로 쓰던 `<video automation-hero.mp4>`+포스터 → `<img techsupport-hero.webp>`로 교체. 섹션 클래스에서 `aut-hero-stage` 제거(`ts-hero-stage`만 유지). techsupport-page.css 주석 갱신.
- 서브메뉴: 전 페이지 메가메뉴의 "기술지원 안내" 항목에 `data-img` 추가(이전엔 없어 hover 시 교육·A/S 이미지가 잔류). 라이브 87 + handoff3 92. `cases/library.html`은 메뉴 구조가 달라 제외(기존 상태).
- MANIFEST.sha256.txt: 이미지 2개 항목 추가(HTML/CSS 해시는 §34와 같이 커밋 전 재생성).

### 37. 기술지원 히어로 구성을 교육·A/S와 동일하게 (support/techsupport.html, 2026-10-11)
- `.ts-hero-stage` 히어로 CSS를 `.edu-hero-stage`와 같은 값으로 재작성: 텍스트박스 좌측 정렬(top 46% / left 5% / width fit-content / max-width min(520px,36cqw) / padding 28px 32px), h1 clamp(20px,2.8cqw,42px), 하단 그라데이션 .08→.22, 태블릿(641~1100px) 규칙(object-position 0% 50%, 박스 340px) 동일 적용.
- 점프 링크: `cap-hero-jump`(capability-page.css 의존, 가운데 정렬) → 전용 `ts-hero-jump`(edu-hero-jump와 동일 스타일, 좌측 정렬, ≤1280px 숨김).
- 섹션에 `aut-hero-stage` 클래스 복원(교육 페이지와 동일한 베이스 레이아웃 사용). 리드 문장 소폭 축약(좁아진 박스 폭 대응).
- techsupport-page.css 버전 쿼리 `?v=20261011-1`.

### 38. 기술자료 히어로 사진 + 서브메뉴 프리뷰 교체 (cases/technical.html, 2026-10-11)
- 발주자 제공 이미지(흰 책상 위 서류 묶음·노트북 도면·금속 부품, 1584×672 PNG 1.6MB)를 웹용으로 압축.
  - `assets/img/technical-hero.webp` 2206×946(21:9 중앙 크롭, q0.8, 약 49KB)
  - `assets/img/submenu-technical.webp` 960×720(4:3, 서류 묶음+노트북 중심 크롭, 약 31KB)
- 히어로: 자료실 페이지는 사진 히어로 없이 다크 밴드(`.res-top`)를 쓰는 구조라 섹션을 바꾸지 않고 `.res-top-photo` 변형 추가 — `<img class="res-top-bg">`를 밴드 배경으로 깔고 좌→우 네이비 오버레이(.9→.42)로 좌측 텍스트·검색창 가독성 유지, 우측 노트북·서류는 보이게. 다른 자료실 3페이지(case-studies/videos/webinars)는 변경 없음.
- 서브메뉴: 전 페이지 "기술자료" 항목 `data-img`를 `adopt-basic-setup.jpg` → `submenu-technical.webp`로 교체(라이브 87 + handoff3 92; cases/library.html 제외).
- `resources-page.css`는 handoff3에 없던 파일이라 이번에 추가(버전 쿼리 `?v=20261011-1`). MANIFEST에 3개 항목 추가.

### 39. 기술자료 히어로 → 풀 사진 히어로로 전환 (cases/technical.html, 2026-10-11, §38 대체)
- §38의 다크 밴드+오버레이 방식은 사진이 거의 묻혀 폐기. 교육·A/S·기술지원과 동일한 `.subhero-parallax.aut-hero-stage` 구성으로 교체: `<img technical-hero.webp>` 풀 사진 + 좌측 텍스트박스(.tec-hero-stage, edu/ts와 같은 값).
- 검색창·필터 초기화는 히어로 아래 슬림 다크 밴드(`.res-top.res-top-slim`)로 이동(상단 패딩·TECH 워터마크 제거). 리드 문장에서 "제목이나 키워드로 검색해 보세요" 문구 제거(검색창이 바로 아래 있음).
- `.res-top-photo` 규칙은 삭제. resources-page.css `?v=20261011-3`.

### 40. 기술자료 히어로에 점프 링크 추가 — 기술지원 안내와 완전 동일 구성 (cases/technical.html, 2026-10-11)
- 텍스트박스 하단에 `.tec-hero-jump`(ts-hero-jump와 동일 스타일) 3개: 자료 검색(#resSearch) · 기술자료 목록(#resRoot) · 다른 자료실(#resMore, res-cross 섹션에 id 부여). ≤1280px 숨김.
- resources-page.css `?v=20261011-4`.

### 41. 기술자료 본문 시작부를 기술지원과 동일하게 — 다크 검색 밴드 제거, rec-cover 라운드 겹침 (cases/technical.html, 2026-10-11)
- §39의 `.res-top.res-top-slim` 밴드 삭제. `.res-main`에 `rec-cover tint-hatch`(recovery-page.css, 히어로 위로 -64px 겹치는 라운드 커버) 적용 → 기술지원 페이지와 같은 히어로→본문 전환.
- 검색창·필터 초기화는 본문 툴바(.res-toolbar-search) 우측으로 이동, 라이트 스타일(.res-filterbar-light). 760px 이하에서 한 줄 아래로 줄바꿈.
- 히어로 점프 "자료 검색"(#resSearch)은 그대로 동작. resources-page.css `?v=20261011-5`.
- (수정) technical.html에 recovery-page.css 링크 추가(rec-cover 정의 파일). 라이트 검색창 규칙은 `.res-main` 접두로 특이도 상향(다크 .res-filterbar 규칙에 밀리던 문제). resources-page.css `?v=20261011-6`.

### 42. 제품 카탈로그 히어로 신규 이미지 + 서브메뉴 프리뷰 추가 (support/catalog.html, 2026-10-11)
- 발주자 제공 이미지(책상 위 Cold Jet 카탈로그 3권 + 노트북, 1584×672 PNG 1.6MB) 압축: `assets/img/catalog-hero.webp` 2206×946(21:9, q0.8, 약 45KB) / `assets/img/submenu-catalog.webp` 960×720(카탈로그 중심 크롭, 약 28KB).
- 기술자료(§39~41)와 완전히 같은 전환: 다크 밴드 → `.subhero-parallax.aut-hero-stage.tec-hero-stage` 풀 사진 히어로(좌측 텍스트박스 + 점프 링크 3개), 본문 `.res-main.rec-cover.tint-hatch`(라운드 겹침), 검색창은 본문 툴바 우측 라이트 스타일. recovery-page.css 링크 추가, resources-page.css `?v=20261011-6`.
- 서브메뉴: 전 페이지 "제품 카탈로그" 항목에 `data-img` 추가(이전엔 없었음). MANIFEST 2개 항목 추가.

### 43. 웹세미나 히어로 신규 이미지 + 서브메뉴 프리뷰 교체 (cases/webinars.html, 2026-10-11)
- 발주자 제공 이미지(사무실 책상에서 모니터로 온라인 세미나 시청, 1584×672 PNG) 압축: `assets/img/webinars-hero.webp` 2206×946(21:9, q0.8, 약 57KB) / `assets/img/submenu-webinars.webp` 960×720(모니터+시청자 중심 크롭, 약 25KB).
- 기술자료·카탈로그(§39~42)와 완전히 같은 전환: 다크 밴드 → `.tec-hero-stage` 풀 사진 히어로(좌측 텍스트박스 + 점프 링크 3개), 본문 `.res-main.rec-cover.tint-hatch`, 검색창 본문 툴바 우측 라이트 스타일. recovery-page.css 링크 추가, resources-page.css `?v=20261011-6`.
- 서브메뉴: 전 페이지 "웹세미나" 항목 `data-img` → `submenu-webinars.webp`. MANIFEST 2개 항목 추가.
- 자료실 4페이지 중 case-studies.html · videos.html은 아직 다크 밴드 구조(변경 없음).

### 44. 렌탈 신청 히어로 + 서브메뉴 이미지 교체 (rental/apply.html, 2026-10-11)
- 발주자 제공 이미지(회의 테이블에서 클립보드 신청서를 함께 검토하는 장면, 1584×672 PNG) 압축: `assets/img/apply-hero-v2.webp` 2206×946(21:9, q0.8, 약 48KB) / `assets/img/submenu-apply-v2.webp` 960×720(클립보드·손 중심 크롭, 약 25KB).
- 페이지 구조는 이미 기술지원과 동일(풀 사진 히어로 .ap-rental-hero + rec-cover 라운드 본문)이라 이미지만 교체. 구 `apply-hero.webp` / `submenu-apply.webp` 삭제, 전 HTML `data-img` 갱신(라이브 87 + handoff3 92). MANIFEST 2개 항목 교체.

### 45. 데모 테스트 신청 히어로 + 서브메뉴 이미지 교체 (rental/demo-apply.html, 2026-10-11)
- 발주자 제공 이미지(연구소 작업대에서 시편 트레이를 다루는 기술자와 고객, 1584×672 PNG) 압축: `assets/img/demo-apply-hero-v2.webp` 2206×946(21:9, q0.8, 약 75KB) / `assets/img/submenu-demo-apply-v2.webp` 960×720(기술자·시편 중심 크롭, 약 38KB).
- 페이지 구조는 이미 기술지원과 동일(.ap-demo-hero 풀 사진 히어로 + rec-cover 라운드 본문)이라 이미지만 교체. 구 `demo-apply-hero.webp` / `submenu-demo-apply.webp` 삭제, 전 HTML `data-img` 갱신(라이브 87 + handoff3 92). MANIFEST 2개 항목 교체.

### 46. 교육·A/S 히어로 + 서브메뉴 이미지 재교체 (support/education.html, 2026-10-11, §35 대체)
- 발주자 제공 이미지(교육실 작업대 — 태블릿 매뉴얼·측정 케이블·부품, 교육 진행 장면, 1584×672 PNG) 압축: `assets/img/education-hero-v3.webp` 2206×946(21:9, q0.8) / `assets/img/submenu-education-v3.webp` 960×720(태블릿·매뉴얼 중심 크롭).
- 페이지 구조는 이미 기술지원과 동일(.edu-hero-stage 풀 사진 히어로 + rec-cover 라운드 본문)이라 이미지만 교체. 구 v2 파일 삭제, 전 HTML `data-img`·프리뷰 `background-image` 갱신(라이브 87 + handoff3 92). education-page.css 주석·MANIFEST 2개 항목 갱신.

### 47. 세척용역 히어로 + 서브메뉴 이미지 교체 (rental/partners.html, 2026-10-11)
- 발주자 제공 이미지(OUR PARTNERS 금속 레터링 + Certified Service Partner 인증서 9장, 1584×672 PNG) 압축: `assets/img/partners-hero-v2.webp` 2206×946(21:9, q0.8) / `assets/img/submenu-partners-v2.webp` 960×720(인증서·레터링 중심 크롭).
- 페이지 구조는 이미 기술지원과 동일(.pt-hero-stage 풀 사진 히어로 + rec-cover 라운드 본문)이라 이미지만 교체. 구 파일 삭제, 전 HTML `data-img` 갱신(라이브 87 + handoff3 92). partners-page.css 주석·MANIFEST 2개 항목 갱신.

### 48. 회사소개 히어로 신규 이미지 + 서브메뉴 프리뷰 추가 (company/about.html, 2026-10-11)
- 발주자 제공 이미지(하남 사옥 외벽 + VATEK 사인, 1584×672 PNG) 압축: `assets/img/about-hero.webp` 2206×946(21:9, q0.8) / `assets/img/submenu-about.webp` 960×720(사인·창 중심 크롭).
- 히어로: 기존 `vatek-building.jpg`(16:9, 패럴랙스 buffer 60·pan 1.06·블러) → 정적 21:9 이미지(buffer 0 / pan 1 / no-blur). `.ab-hero-stage` CSS를 기술지원(.ts-hero-stage)과 같은 값으로 재작성(좌측 fit-content 텍스트박스 36cqw, h1 2.8cqw, 그라데이션 .66→.22, 태블릿 규칙). 로고 행(.ab-hero-logos) 좌측 정렬. 본문 rec-cover 라운드 겹침은 기존 그대로. about-page.css `?v=20261011-1`.
- 서브메뉴: 전 페이지 회사소개 메뉴 "회사소개" 항목에 `data-img` 추가(이전엔 회사소개 메뉴 전체에 프리뷰 없음). `vatek-building.jpg`는 다른 페이지에서 쓰일 수 있어 유지.
- handoff3에 about-page.css 추가(없던 파일). MANIFEST 3개 항목 추가.

### 49. 위치/연락처 히어로 신설 + 서브메뉴 프리뷰 추가 (company/location.html, 2026-10-11)
- 발주자 제공 이미지(사무실 테이블 지도 위 VATEK 위치 핀, 1584×672 PNG) 압축: `assets/img/location-hero.webp` 2206×946(21:9, q0.8) / `assets/img/submenu-location.webp` 960×720(핀 중심 크롭).
- 이 페이지는 사진 히어로 없는 구형 `.page-hero` + "[제품 사진/영상 영역]" 플레이스홀더 상태였음 → 기술지원과 동일한 `.subhero-parallax.aut-hero-stage.lc-hero-stage` 풀 사진 히어로(좌측 텍스트박스) + 본문 첫 섹션 `.plt-section.rec-cover.tint-hatch`(라운드 겹침, plt-head 제목)로 교체. 플레이스홀더 div 제거, 연락처 표·하위 카드·CTA는 그대로.
- 신규 `assets/css/location-page.css`(.lc-hero-stage, ts와 같은 값). pelletizer-page.css · recovery-page.css 링크 추가.
- 서브메뉴: 전 페이지 "위치/연락처" 항목에 `data-img` 추가. MANIFEST 3개 항목 추가.
- 연락처 표의 "[입력 필요]" 값은 기존 그대로 — 실제 주소·전화·이메일 입력 필요.

### 50. 케이스 스터디·적용 영상·작업별·산업별·세척의 이해·도입 가이드·타 세척 비교 히어로 표준화 (2026-10-12)
- 7개 페이지(`cases/case-studies.html`, `cases/videos.html`, `cleaning/task.html`, `cleaning/industry.html`, `cleaning/guide.html`, `cleaning/adopt.html`, `cleaning/compare.html`)를 기술지원과 동일한 `.subhero-parallax.aut-hero-stage.tec-hero-stage` 풀 사진 히어로(21:9 2206×946 WebP, 좌측 텍스트박스, `.tec-hero-jump` 점프 링크 3개, 본문 `rec-cover` 라운드 겹침)로 통일.
- 신규 이미지: `cases-hero.webp`, `videos-hero.webp`, `task-hero.webp`, `industry-hero.webp`, `guide-hero.webp`, `adopt-hero.webp`, `compare-hero.webp`(히어로) / `submenu-cases.webp`, `submenu-videos.webp`, `submenu-task.webp`, `submenu-industry.webp`(서브메뉴 4:3 960×720). 전 페이지 적용분야 메가메뉴 `data-img` 교체.
- guide · adopt · compare · task에 `resources-page.css` 링크 추가(`.tec-hero-stage` 정의 파일). 점프 링크 대상 섹션에 `id` 부여.
- 구 `compare-hero.jpg`는 `cleaning/industry.html` 본문에서, `task-thumb.jpg`는 세척 가이드북 메뉴 프리뷰에서 계속 사용 — 삭제하지 않음.

### 51. 메뉴 라벨 변경 (전 페이지 92개 HTML, 2026-10-13)
- 1단 메뉴·메가메뉴 제목·브레드크럼·홈 메뉴 픽커: `드라이아이스 세척가이드` → **`드라이아이스 세척 가이드북`** (푸터 컬럼 "세척 가이드"는 그대로).
- **적용 분야 메가메뉴에서만** `산업별 솔루션` → `산업별 적용분야`, `작업별 솔루션` → `작업별 적용분야` (서브메뉴 항목 + 기본 선택 상세 제목 + 홈 메뉴 픽커 칩). 세척 가이드북 메가메뉴의 같은 항목과 본문 카드 제목은 변경 없음. `href`·`data-img` 변경 없음.

### 52. 기술·서비스 역량 히어로 신규 이미지 + 서브메뉴 프리뷰 추가 (company/capability.html, 2026-10-13)
- 발주자 제공 인포그래픽(블러 작업장 배경 + VATEK 기술 역량 5축 레이더 차트, 1915×821 PNG 1.5MB) 압축: `assets/img/capability-hero.webp` 2206×946(21:9, q0.8, 약 53KB) / `assets/img/submenu-capability.webp` 960×720(VATEK 로고 중앙 크롭, 약 30KB).
- 히어로 섹션 클래스 `cap-hero-stage` → **`tec-hero-stage`**, 점프 링크 `cap-hero-jump` → `tec-hero-jump`(기술지원과 완전 동일 구성). `resources-page.css?v=20261011-6` 링크 추가(capability-page.css 뒤). 구 히어로 `guide-hero-work.jpg`는 `cleaning/industry.html`에서 계속 사용.
- 서브메뉴: 전 페이지 회사소개 메가메뉴 "기술·서비스 역량" 항목에 `data-img` 추가(이전엔 없었음).

### 53. 전 사이트 이미지 웹 최적화 — 250KB 초과 이미지 111개 WebP 전환 (2026-10-13)
- 전체 미디어 687개를 스캔, 250KB 초과 이미지 116개 중 HTML에서 참조되는 **111개를 WebP로 변환**(미참조 5개는 삭제만: `coldjet-aero-family.png`, `demo-way-1-ship.png`, `demo-way-3-onsite.png`, `submenu-guide-poster.jpg`, `blaster-catalog-original.jpg`).
- 규칙: 최대 폭 1600px(히어로 영상 포스터 1920, `icon-*` 800), 품질 0.8에서 시작해 180KB(포스터 150KB) 이하가 될 때까지 0.06씩 하향, 투명 PNG는 알파 유지. 결과 대부분 20–150KB(1–3MB → 95% 이상 감소). 유일한 예외 `lineup-trimmed-t.webp` 208KB(투명 와이드 라인업).
- 파일명은 확장자만 변경(`name.png`/`.jpg` → `name.webp`). 이미 WebP였던 대용량 3개(`auto-asp-t`, `auto-duct-robot-track`, `auto-vatek-custom`, 각 1.1MB)는 같은 경로에 재인코딩(약 60–70KB).
- 92개 HTML의 참조 856곳 일괄 교체(`<img src>`, `<video poster>`, `data-img`, `data-poster`, 프리뷰 `background-image`). CSS에는 해당 파일 참조 없음.
- **저장소에서 삭제할 원본 113개는 `DELETED_FILES.txt`에 목록화** — 반드시 삭제해 주세요(같은 이름의 .webp가 대체).
- 영상은 브라우저 환경에서 재인코딩 불가 — 아래 "미해결 사항" 참조.

### 54. handoff3 미러 보정 (2026-10-13)
- `products/blaster/*`, `products/pelletizer/*`, `products/recovery/*` 하위 21개 페이지가 §51 라벨 변경·§52 data-img 추가 패스에서 누락되어 있었음 → 라이브 버전으로 덮어써 전체 동기화. `cases/library.html`(리다이렉트 스텁)은 handoff3에 없음(변경 없음).

## 미해결 사항 추가 (2026-10-13)
- **영상 용량** (브라우저에서 재인코딩 불가, 발주자가 ffmpeg로 처리 후 전달 필요): `pelletizer-definition.mp4` 15MB · `blaster-hero.mp4` 8.4MB · `pelletizer-ondemand.mp4` 7.0MB · `pcs-demo-namecard.mp4` 5.3MB · `main-hero.mp4` 5.0MB · `pcs-demo-asphalt.mp4` 4.8MB · `automation-vatek-line.mp4` 4.0MB · `recovery-process.mp4` 2.0MB.
  권장: `ffmpeg -i in.mp4 -vf "scale='min(1920,iw)':-2" -c:v libx264 -crf 28 -preset slow -an -movflags +faststart out.mp4` (히어로 루프는 `-crf 30`, 10–15초 트리밍).
- `assets/video/main-hero-poster.jpg`(0.4MB)·`belief-co2-poster.jpg`(0.2MB)는 250KB 경계 — 영상 교체 시 함께 WebP로.
- `company/location.html` 연락처 표 "[입력 필요]" 값 미입력(§49).

### 55. Aero₂ PCS® ULTRA · Aero₂ PLT® ULTRA 제품 상세 페이지 신규 (products/blaster/aero2-ultra.html, aero2-plt-ultra.html, 2026-10-13~14)
Cold Jet 공식 제품 페이지 구성을 참고해 두 플래그십 블라스터 상세 페이지를 신규 작성. 두 페이지는 같은 골격(`au-*` 접두 클래스, `assets/css/style.css`에 공용 정의)을 공유합니다.
- **공통 구조**: ① 상단 이미지 갤러리(큰 이미지 + 썸네일 전환) ② 좌/우 교차 flex 카피 섹션 ③ 탭 UI(Features / Specifications) — Features 사진 위 핫스팟(hotspot) 툴팁 ④ 전폭 액세서리 그리드 3행(노즐 4 · 어플리케이터 4 · 키트/호스 3, 이미지 우선·카드 테두리 없음) ⑤ 하단 "All Models" 라인업 — `tint-hatch` 배경 안 카테고리 필터 6개(`#auModels`, `data-cat`), 현재 페이지 모델은 teal 테두리 + 배지(`is-current`, `aria-current="page"`), 11개 모델 카드 전부 `products/blaster/*.html`로 링크.
- **PCS 페이지 전용 — 입자 크기 다이얼**: 0.3–3.0 mm 28단계. 드래그·휠·키보드(←/→, ↑/↓)로 조작, 값에 따라 손 데모 이미지·그립 하이라이트가 바뀜. 로드 시 자동 데모가 돌다가 **사용자가 처음 터치하면 자동 데모 정지**. 데모 영상 2개(`pcs-demo-namecard.mp4` 0.3mm / `pcs-demo-asphalt.mp4` 3.0mm, `preload="none"`, 재생 버튼 `.au-pc-play`).
- **PLT 페이지 전용 — 압력 게이지**: 2.4–17.2 bar(35–250 psi). 같은 드래그·휠·키 조작. **10 bar 임계값**에서 "파워" 시각화 전환 — 색상 teal → orange → red, 라벨 확대, 미세 떨림(tremor), 글로우 강화. 데모 영상 1개(`pcs-demo-asphalt.mp4` 재사용).
- **신규 이미지 26개**(모두 WebP, `assets/img/`): 갤러리 `aero2-pcs-ultra-{front,side,performance-kit,precision-kit}.webp`, `aero2-plt-ultra-{front,side,kit}.webp` / Features `adv-{applicator,automation,connectivity,core,defrost,hmi,hmi-plt,motors,pcs-infographic,service,sureflow}.webp` / 액세서리 `acc-{applicator-1,applicator-34,applicator-precision,applicators-all,nozzles-all,nozzles-high,nozzles-low,nozzles-standard}.webp`. 원본은 `uploads/`(번들 제외).
- **크로스 링크 갱신**: `products/blaster/index.html` 제품 카드(`.bls-prod`) → 두 상세 페이지 링크, `products/compare-equip.html` 비교표 행 링크, 두 페이지 상호 라인업 링크.
- **공용 CSS(`assets/css/style.css`)**: `au-*` 다이얼/게이지/갤러리/탭/핫스팟/라인업 규칙 추가. 다른 페이지 규칙 변경 없음.
- **알려진 한계**: PLT Features의 HMI 근접 사진은 Cold Jet 고해상 원본이 없어 정면 사진에서 패널을 크롭한 `adv-hmi-plt.webp`(약 700px, 다소 소프트) 사용 — 고해상 사진 입수 시 같은 경로로 교체만 하면 됨.
- **영상 파일 주의**: `assets/video/pcs-demo-namecard.mp4`(5.3MB)·`pcs-demo-asphalt.mp4`(4.8MB)는 용량 때문에 이 번들에 **포함하지 않음** — 저장소에 이미 있는지 확인하고, 없으면 발주자 원본을 §53 미해결 사항의 ffmpeg 권장 설정으로 압축해 같은 경로에 커밋(또는 외부 호스팅 후 `<source src>` 교체).

## 이 번들 적용 방법 — 2026-10-14 갱신
1. 번들 루트에서 `sha256sum -c MANIFEST.sha256.txt`
2. 전 파일을 저장소 동일 경로에 **그대로 덮어쓰기**(§55 신규 2페이지 + 이미지 26개 포함). 번들에 없는 파일은 손대지 않음
3. `DELETED_FILES.txt` 목록 삭제(§53)
4. `assets/video/pcs-demo-*.mp4` 존재 여부 확인(§55)
