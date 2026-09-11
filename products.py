# -*- coding: utf-8 -*-
"""
제품 상세 페이지 생성 모듈 (블라스터 / 펠렛타이저 / CO2 리커버리)
coldjet.com의 "카테고리 목록 → 모델 클릭 → Overview / Cold Jet 강점 / Features / Specifications / Accessories 상세"
페이지 구조를 그대로 재현한다.
generate.py의 main()에서 nav_html/footer_html/page_shell/asset 함수를 인자로 받아 사용한다.
"""
import os

# ---------------------------------------------------------------------------
# 블라스터 데이터
# ---------------------------------------------------------------------------

BLASTER_CATEGORIES = [
    ("smart", "① 스마트 블라스터", "IoT · Industry 4.0 — Cold Jet CONNECT&reg;로 원격 모니터링 · 진단이 가능한 라인입니다."),
    ("pellet", "② 펠릿 블라스터", "범용 산업현장을 위한 표준 라인입니다."),
    ("particle", "③ 마이크로파티클 블라스터", "정밀 세척을 위한 소형 · 정밀 라인입니다."),
    ("specialty", "④ 특수 목적 블라스터", "특수한 작업 조건을 위한 전용 라인입니다."),
]

BLASTER_MODELS = [
    {
        "slug": "aero2-ultra", "category": "smart", "name": "Aero2&reg; ULTRA Series",
        "tagline": "가장 혁신적인 스마트 드라이아이스 블라스터, Aero2 PCS ULTRA · Aero2 PLT ULTRA 2개 모델",
        "overview": [
            "Aero2 ULTRA 시리즈는 Cold Jet이 선보이는 최고 사양의 스마트 드라이아이스 블라스터 라인입니다. "
            "작업자를 배려한 직관적인 HMI 디스플레이와 인체공학적 설계로, 세척 과정을 완전히 제어할 수 있습니다.",
        ],
        "advantages": [
            ("Smart", "Cold Jet CONNECT&reg;를 통한 원격 모니터링 · 진단 (업계 최초)"),
            ("Easy to Use", "7인치 LCD 화면과 디지털 컨트롤로 손쉬운 조작"),
            ("Versatile", "특허받은 입자 제어 시스템(PCS)으로 3mm~0.3mm까지 입자 크기 정밀 조정"),
            ("Efficient", "직선형(straight-through) 에어 시스템으로 공급 효율 극대화"),
            ("Consistent", "특허받은 SureFlow 피더 시스템으로 일관된 드라이아이스 공급"),
        ],
        "features": [
            "Aero2 PCS ULTRA — 특허받은 입자 제어 시스템(PCS)으로 드라이아이스 입자 크기를 3mm~0.3mm까지 정밀 조정",
            "Aero2 PLT ULTRA — 펄스 없는 강력한 분사를 구현하는 혁신적 에어 시스템으로 강력한 오염물 제거",
            "7인치 LCD 터치스크린으로 현장에서 직접 설정 확인 · 조정",
            "Cold Jet CONNECT&reg;를 통한 원격 모니터링 · 진단",
            "Industry 4.0 스마트팩토리 환경에 대응하는 경량화 설계",
        ],
        "specs": [
            ("구성", "Aero2 PCS ULTRA / Aero2 PLT ULTRA 2개 모델"),
            ("제어 방식", "7인치 LCD 터치스크린"),
            ("원격 관리", "Cold Jet CONNECT&reg; 지원"),
            ("입자 조정 범위 (PCS ULTRA)", "3mm ~ 0.3mm"),
            ("상세 스펙", "무게 · 크기 · 압력 · 공기소비량 등 수치 스펙은 정식 스펙시트로 안내해 드립니다"),
        ],
        "accessories": True,
    },
    {
        "slug": "i3-microclean-2", "category": "smart", "name": "i3 MicroClean&reg; 2",
        "tagline": "1세대보다 드라이아이스 사용량을 25% 이상 줄인 2세대 정밀 스마트 블라스터",
        "overview": [
            "\"Soft on Surfaces. Tough on Contaminants.\" i3 MicroClean 2는 향상된 파워와 효율, 직관적인 제어, "
            "IoT 연동 기능을 갖춘 차세대 정밀 세척 솔루션입니다. 1세대 대비 소모품(드라이아이스) 사용량을 25% "
            "이상 절감하면서도, 블록 · 펠릿을 모두 사용할 수 있는 유연성을 유지합니다.",
        ],
        "advantages": [
            ("Efficient", "1세대 i3 MicroClean 대비 소모품 사용량 25% 이상 절감"),
            ("IoT Capability", "Cold Jet CONNECT&reg;로 원격 모니터링 · 진단"),
            ("Intuitive Controls", "7인치 LCD 화면으로 파라미터 조정 · 레시피 저장"),
            ("Designed for Precision", "민감한 표면과 복잡한 형상도 안전하게 세척"),
            ("Low Noise Operation", "낮은 공급 압력으로도 효과적으로 작동해 소음 감소"),
        ],
        "features": [
            "1세대 i3 MicroClean 대비 소모품(드라이아이스) 사용량 25% 이상 절감",
            "Cold Jet CONNECT&reg; 연동으로 사용 데이터 원격 확인",
            "블록 · 펠릿 겸용 호퍼로 유연한 운영",
            "정전기 방지 접지 케이블 내장",
        ],
        "specs": [
            ("전체 시스템 크기 · 무게", "79 × 64 × 119 cm, 86 kg (190 lbs)"),
            ("블라스터 본체 크기 · 무게", "79 × 48 × 53 cm, 60.5 kg (133.4 lbs)"),
            ("호퍼 용량", "11 kg (25 lbs), 블록 · 펠릿 겸용"),
            ("사용 압력", "1.4 ~ 10 bar (20 ~ 145 psi)"),
            ("공기 소비량", "0.3 ~ 1.4 ㎥/min (80 psi 기준)"),
            ("공급 속도", "0 ~ 0.7 kg/min"),
        ],
        "accessories": True,
    },
    {
        "slug": "aero-series", "category": "pellet", "name": "Aero&reg; Series (40FP / 80FP)",
        "tagline": "풀프레셔(Full-Pressure) 전문가용 블라스터, 호퍼 용량별 40FP · 80FP 2종",
        "overview": [
            "\"Proven, time tested machines.\" Aero 시리즈는 오랜 기간 현장에서 검증된 펠릿 블라스터입니다. "
            "20 psi(1.4 bar)의 부드러운 세척부터 300 psi(20 bar)의 강력한 블라스팅까지, 전 압력 구간에서 "
            "안정적인 성능을 제공합니다.",
        ],
        "advantages": [
            ("Performance SureFlow System", "특허받은 시스템으로 호퍼를 가득 채운 채 30m 호스로도 막힘 없이 사용"),
            ("Patented Feeder Technology", "공기역학적 로딩 방식으로 패드 · 로터 마모를 줄여 장비 수명 연장"),
            ("Advanced Radial Feeding System", "펄스 없는 일관된 분사와 정밀한 이송속도 제어"),
            ("Full Range of Pressure", "20 psi(1.4 bar)부터 300 psi(20 bar)까지 전 압력 구간 대응"),
            ("Rugged and Mobile", "고강도 산업 현장에서의 지속적인 사용을 견디는 내구성"),
        ],
        "features": [
            "공기역학적 로딩 설계로 패드 · 로터 마모를 줄여 장비 수명 연장",
            "경량 컴팩트 모터로 무게 절감과 전력 소비 감소",
            "펄스 없는 일관된 펠릿 공급과 정밀 이송속도 제어가 가능한 로터",
            "전 압력 구간(Full range of blast pressure) 대응",
            "온보드 압력 조절기 탑재",
        ],
        "specs": [
            ("무게 (40FP)", "116.8 kg (257 lbs)"),
            ("크기 (40FP)", "91 × 51 × 102 cm"),
            ("호퍼 용량 (40FP)", "18.2 kg (40 lbs)"),
            ("사용 압력", "1.4 ~ 17.2 bar (20 ~ 250 psi)"),
            ("공기 소비량 (40FP)", "2.8 ~ 4.7 ㎥/min (80 psi 기준)"),
            ("공급 속도 (40FP)", "0 ~ 2 kg/min"),
            ("80FP", "40FP와 동일 계열의 대용량 호퍼 모델 (상세 스펙은 견적 문의 시 안내)"),
        ],
        "accessories": True,
    },
    {
        "slug": "elite20-icerocket", "category": "pellet", "name": "Elite 20 &amp; IceRocket PLT",
        "tagline": "전문가급 성능의 입문형 블라스터 2종",
        "overview": [
            "\"Versatile and reliable machines for many applications.\" Elite 20과 IceRocket PLT는 신뢰할 수 있는 "
            "성능을 합리적인 가격에 제공하는 전문가급 입문형 블라스터입니다. 가벼운 작업부터 고강도 작업까지 "
            "폭넓게 대응하는 운영 유연성을 갖췄습니다.",
        ],
        "advantages": [
            ("Durable", "스테인리스 스틸 프레임으로 내구성과 신뢰성 확보"),
            ("Insulated Lid and Hopper", "드라이아이스 승화를 최소화해 중단 없는 세척 보장"),
            ("Easy-adjusting Dosing System", "드라이아이스 투입량을 손쉽게 조절"),
            ("User Friendly Control Panel", "블라스팅 파라미터를 직관적으로 제어"),
        ],
        "features": [
            "스테인리스 스틸 프레임으로 내구성과 신뢰성 확보",
            "단열 뚜껑과 호퍼로 드라이아이스 승화를 최소화, 중단 없는 세척 보장",
            "손쉬운 용량 조절과 사용자 친화적 제어판",
            "IceRocket PLT — 최소한의 압축공기 요구조건으로도 안정적으로 작동",
            "Elite 20 — 다목적 · 중작업용 대형 블라스팅에 적합",
        ],
        "specs": [
            ("구성", "Elite 20 / IceRocket PLT 2개 모델"),
            ("프레임", "스테인리스 스틸"),
            ("호퍼", "단열 설계"),
            ("상세 스펙", "무게 · 크기 · 압력 · 공기소비량 등 수치 스펙은 정식 스펙시트로 안내해 드립니다"),
        ],
        "accessories": True,
    },
    {
        "slug": "i3-microclean", "category": "particle", "name": "i3 MicroClean&reg;",
        "tagline": "특허받은 단일호스 패턴 공급 기술의 탁상형 정밀 블라스터",
        "overview": [
            "\"Gentle Cleaning in a Table-top Format.\" i3 MicroClean은 가볍고 정밀한 단일호스 저압 블라스터로, "
            "최소 12 CFM의 공기로도 작동하며 20~140 psi(1.4~9.7 bar)의 다양한 압력에서 블록 드라이아이스로 "
            "블라스팅할 수 있습니다.",
        ],
        "advantages": [
            ("Efficient", "1회 충전으로 최대 45분 연속 세척"),
            ("Flexibility", "조정 가능한 분사 압력으로 성능 최적화"),
            ("Designed for Precision Applications", "민감한 표면과 복잡한 형상도 안전하게 세척"),
            ("Low Noise Operation", "낮은 공급 압력으로 조용한 작동"),
        ],
        "features": [
            "1회 충전으로 최대 45분 연속 세척 가능",
            "특허받은 단일호스 공급 장치로 최대 분사 정밀도 제공",
            "5×5×10인치 또는 6×6×12인치 블록 드라이아이스 사용",
            "조정 가능한 분사 압력으로 성능 최적화",
            "내장 20마이크론 에어필터로 오염된 압축공기 영향 최소화",
            "인체공학적 조명 적용기, 통합 정전기 방지 본딩 케이블",
            "컴팩트 · 휴대 가능한 설계, 내구성 있는 이동 카트 포함",
        ],
        "specs": [
            ("무게", "59.1 kg (130 lbs)"),
            ("크기", "55.9 × 40.6 × 53.3 cm"),
            ("호퍼 용량", "9.1 kg (20 lbs)"),
            ("사용 압력", "1.4 ~ 9.7 bar (20 ~ 140 psi)"),
            ("공기 소비량", "0.3 ~ 1.4 ㎥/min (140 psi 기준)"),
            ("공급 속도", "0 ~ 0.5 kg/min"),
            ("사용 드라이아이스", "5\"×5\"×10\" 또는 6\"×6\"×12\" 블록"),
            ("부품 번호", "2A0169"),
        ],
        "accessories": True,
    },
    {
        "slug": "sdi-select-60", "category": "particle", "name": "SDI Select&trade; 60",
        "tagline": "바테크가 국내에도 공급해 온 대표 범용 모델",
        "overview": [
            "\"Utilize Any Type of Dry Ice.\" SDI Select 60은 단순하고 사용하기 쉬우며 다재다능한 드라이아이스 "
            "블라스터입니다. 특허받은 피더 기술로 표준 블록부터 3mm 펠릿, 너겟, 슬라이스, 심지어 남은 스크랩 "
            "아이스까지 셰이브 방식으로 사용할 수 있어, 드라이아이스 수급이 제한적인 현장에도 새로운 세척 "
            "기회를 열어줍니다. Aero 계열 노즐 · 액세서리와 호환되며 20~250 PSI 범위에서 부드럽게도, "
            "강력하게도 세척할 수 있습니다.",
        ],
        "advantages": [
            ("Shave with Any Type of Dry Ice", "표준 블록 · 3mm 펠릿 · 너겟 · 슬라이스 · 스크랩 아이스까지 모두 사용 가능"),
            ("Low Noise Levels", "최소 50 CFM부터 세척 가능해 압축공기 비용과 소음 절감"),
            ("Clean Aggressively", "최대 250 PSI까지 압력을 높여 강한 오염물도 제거"),
            ("Versatile", "민감한 표면부터 고강도 오염까지 폭넓게 대응"),
        ],
        "features": [
            "표준 블록부터 스크랩 아이스까지, 어떤 드라이아이스 미디어든 사용 가능(Shave 방식)",
            "3mm 펠릿 성능을 위한 바이패스 기능",
            "최소 50 CFM부터 세척 가능해 압축공기 비용 절감",
            "최대 250 PSI까지 압력 조절 가능",
            "Aero 노즐 및 액세서리와 호환",
        ],
        "specs": [
            ("무게", "155.9 kg (343 lbs)"),
            ("크기", "61 × 71 × 109 cm (24×28×43\")"),
            ("호퍼 용량", "27.2 kg (60 lbs)"),
            ("사용 압력", "1.4 ~ 17.2 bar (20 ~ 250 psi)"),
            ("공기 소비량", "1.4 ~ 6.1 ㎥/min · 50~215 CFM (80 psi 기준)"),
            ("공급 속도", "0 ~ 2.7 kg/min (0~6 lbs/min)"),
            ("부품 번호", "2A0253 / 2A0236"),
        ],
        "accessories": True,
    },
    {
        "slug": "c100", "category": "specialty", "name": "C100",
        "tagline": "전원 없이 압축공기만으로 작동하는 완전 공압식 블라스터",
        "overview": [
            "\"A Fully Pneumatic Machine.\" Aero C100 Pneumatic은 지금까지 나온 공압식 드라이아이스 블라스터 "
            "중 가장 강력하고 효율적인 모델입니다. 다른 공압식 장비 대비 2배 빠른 세척 성능과, 매번 균일하게 "
            "세척되는 펄스 없는 분사 스트림을 제공합니다.",
        ],
        "advantages": [
            ("Fully Pneumatic Machine", "전원 연결 없이 압축공기만으로 작동, 다른 공압식 대비 2배 빠른 세척"),
            ("Performance SureFlow System", "호퍼를 가득 채운 채 30m 호스로도 막힘 없이 사용"),
            ("Advanced Radial Feeding System", "펄스 없는 분사와 정밀한 이송속도 제어"),
            ("Patented Feeder Technology", "공기역학적 로딩으로 패드 · 로터 마모 감소"),
            ("Full Range of Pressure", "20 psi(1.4 bar)부터 250 psi(17.2 bar)까지 전 구간 대응"),
        ],
        "features": [
            "완전 공압식(Fully pneumatic) 기계로 전원 연결이 불필요",
            "다른 공압식 장비 대비 세척 속도 2배",
            "펄스 없는 스트림으로 매번 균일한 세척",
            "최대 30m(100ft) 호스 길이 지원",
            "1인치 Urebrade 블라스트 호스, 에어호스, 무광 어플리케이터, 정전기 방지 케이블, 노즐 행어, "
            "호스랩, 호스 캐리어 기본 포함",
        ],
        "specs": [
            ("호퍼 용량", "45.5 kg (100 lbs)"),
            ("무게", "117 kg (257 lbs)"),
            ("크기", "78.7 × 38.1 × 114.3 cm"),
            ("사용 압력", "1.4 ~ 17.2 bar (20 ~ 250 psi)"),
            ("공기 소비량", "1.4 ~ 5 ㎥/min (80 psi 기준)"),
            ("공급 속도", "0 ~ 3.2 kg/min (0~7 lbs/min)"),
            ("공급 압력 범위", "65 ~ 250 psi"),
            ("부품 번호", "2A0155"),
        ],
        "accessories": True,
    },
    {
        "slug": "e-co2-150", "category": "specialty", "name": "E-CO2&trade; 150",
        "tagline": "연마재 + 드라이아이스 복합 분사, 도장 · 코팅 · 부식 제거 전용",
        "overview": [
            "부식 · 도장 제거 등 기존 세척 방식은 다량의 호흡성 분진과 2차 폐기물을 남기고, 표면에 수분 · "
            "잔여물을 남기는 경우가 많습니다. E-CO2 150은 Cold Jet 드라이아이스 블라스터(PLT 60 · Aero 80 · "
            "C100)와 1.5입방피트 규모의 전용 가압 연마재 포트를 결합해 이 문제를 해결합니다. 트리거 한 번으로 "
            "연마재와 드라이아이스를 동시에 분사합니다.",
        ],
        "advantages": [
            ("Reduce Respirable Dust", "제3자 검증 기준 호흡성 · 유해 분진 최대 97% 감소"),
            ("Meet OSHA and Environmental Guidelines", "호흡성 분진 · 2차 폐기물 관련 규정을 손쉽게 충족"),
            ("Allows for Immediate Re-coating", "표면에 수분 · 잔여물이 남지 않아 별도 건조 공정 불필요"),
            ("Achieve Cleanliness Levels", "SP10 / SA2.5 / NA2 수준의 청정도 달성"),
            ("Environmentally Responsible", "재생 CO2로 만든 드라이아이스와 재생 연마재 사용"),
        ],
        "features": [
            "Cold Jet 고유의 연마재-드라이아이스 혼합물을 트리거 한 번으로 동시 분사",
            "제3자 검증 기준 호흡성 분진 최대 97% 감소",
            "표면에 수분 · 잔여물을 남기지 않아 건조 공정 불필요",
            "SP10 / SA2.5 / NA2 수준의 청정도 달성",
            "도장 제거, 코팅 제거, 부식 제거 등 산업 코팅 제거 작업에 특화",
        ],
        "specs": [
            ("블라스트 포트 용량", "68 kg (150 lbs)"),
            ("건조 중량", "61.2 kg (135 lbs)"),
            ("크기", "61 × 53.3 × 99 cm (24×21×39\")"),
            ("사용 압력", "50 ~ 150 psi"),
            ("공급 압력 범위", "100 ~ 150 psi"),
            ("노즐 공기 소비량", "2.0 ~ 6.1 ㎥/min · 70~215 CFM (80 psi 기준)"),
            ("페어링 가능 블라스터", "PLT 60 · Aero 80 · C100"),
        ],
        "accessories": True,
    },
]

# ---------------------------------------------------------------------------
# 펠렛타이저 데이터
# ---------------------------------------------------------------------------

PELLETIZER_MODELS = [
    {
        "slug": "pe-80", "name": "PE-80", "tagline": "저용량 · 입문형 펠렛타이저",
        "features": [
            "사용자 친화적 인터페이스와 간단한 조작으로 초보자도 쉽게 운영",
            "1.7 / 2.2 / 3.0 / 8.0 / 16.0mm 5가지 펠릿 크기 선택 가능",
            "다양한 전원 사양 지원(400V/50Hz, 480V/60Hz, 220V/50Hz, 200V/60Hz)",
        ],
        "specs": [
            ("생산능력", "최대 80 kg/h (176 lbs/hr)"),
            ("펠릿 크기", "1.7 / 2.2 / 3.0 / 8.0 / 16.0 mm"),
            ("소비전력", "3 kWh (최대 6.5A)"),
            ("크기", "600 × 1000 × 1560 mm"),
            ("무게", "203 kg (447.5 lbs)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 80", "re-co2-80")]},
    },
    {
        "slug": "pr120h", "name": "PR120H", "tagline": "중소용량 고용량 시리즈",
        "features": [
            "7인치 터치스크린 패널PC로 원격 지원 가능",
            "방습 인클로저로 소음 75dB(A) 이하로 감소",
            "서브쿨링 기술로 CO2 낭비 최소화",
        ],
        "specs": [
            ("생산능력", "120 kg/h (265 lbs/hr)"),
            ("펠릿 크기", "3 / 10 / 16 mm (요청 시 다른 크기 가능)"),
            ("크기", "1150 × 650 × 1738 mm"),
            ("무게", "704 kg (1552 lbs, 유압유 포함)"),
            ("기동 시간", "5분 이내"),
            ("공기 품질", "ISO 8573-1, Class 3 이상"),
            ("부품 번호", "512641 (CE & UL 인증)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 160", "re-co2-160")]},
    },
    {
        "slug": "pr350h", "name": "PR350H", "tagline": "중용량 고성능 펠렛타이저",
        "features": [
            "폐쇄형 챔버 기술로 짧은 기동시간과 빠른 생산",
            "원버튼 자동운전",
            "자동 다이 교체로 4가지 펠릿 크기 즉시 전환",
        ],
        "specs": [
            ("생산능력", "350 kg/h (772 lbs/hr)"),
            ("펠릿 크기", "3 / 6 / 10 / 16 mm (자동 다이 교체)"),
            ("크기", "1500 × 1000 × 1800 mm"),
            ("무게", "1515 kg (유압유 포함)"),
            ("기동 시간", "3분 미만"),
            ("소음", "75 dB(A) 이하"),
            ("CO2 변환계수", "2.2 (업계 최저 수준)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 320 V2", "re-co2-320-v2")]},
    },
    {
        "slug": "pr750h", "name": "PR750H", "tagline": "대용량 생산 라인용",
        "features": [
            "폐쇄형 챔버 기술로 빠른 시작과 생산 보장",
            "15인치 터치스크린, 인터넷 연결 시 원격 지원",
            "방음 인클로저로 소음 75dB(A) 이하",
            "서브쿨링 기술, 자동 익스트루더 플레이트 교환으로 다운타임 및 CO2 손실 절감",
        ],
        "specs": [
            ("생산능력", "750 kg/h (1,653 lbs/hr)"),
            ("펠릿 크기", "3 / 6 / 10 / 16 mm (자동 다이 교체)"),
            ("크기", "1500 × 1500 × 1800 mm"),
            ("무게", "1822 kg (4017 lbs, 유압유 포함)"),
            ("모델 번호", "90636 (CE 380V·50Hz) / 90637 (UL 480V·60Hz)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 320 V2", "re-co2-320-v2"), ("RE-CO2 3500", "re-co2-3500")]},
    },
    {
        "slug": "pr1500h", "name": "PR1500H", "tagline": "PR H 시리즈 최상위, 초대형 생산시설용",
        "features": [
            "폐쇄형 챔버 기술, 15인치 터치스크린 원격 지원",
            "이전 세대 대비 연장된 서비스 간격",
            "방음 · 방습 인클로저로 소음 80dB(A) 이하",
            "서브쿨링 기술, 자동 익스트루더 플레이트 교환",
        ],
        "specs": [
            ("생산능력", "1,500 kg/h (3,306 lbs/hr)"),
            ("펠릿 크기", "3 / 6 / 10 / 16 mm"),
            ("크기", "2210 × 1820 × 2150 mm"),
            ("무게", "4000 kg (8818 lbs)"),
            ("CO2 공급 압력", "13 ~ 18 bar (188~261 psi)"),
            ("압축공기 공급", "8 ~ 10 bar (116~145 psi)"),
            ("전력", "3×480V AC / 60Hz (25 kW / 33.5 Hp)"),
            ("소음", "80 dB(A) 이하"),
            ("작동 온도 범위", "5°C ~ 43°C (41~109°F)"),
        ],
        "cross_links": {"label": "추천 CO2 리커버리 조합", "group": "recovery",
                         "items": [("RE-CO2 3500", "re-co2-3500")]},
    },
    {
        "slug": "special-forms", "name": "DS 시리즈 · R 시리즈 (특수 형태)",
        "tagline": "슬라이스형 드라이아이스, 펠릿 → 슬라이스 변환 장비",
        "features": [
            "DS500E / DS1000E — 슬라이스형 드라이아이스를 직접 생산",
            "R Series — 생산된 펠릿을 슬라이스 형태로 변환",
            "특수한 드라이아이스 형태가 필요한 현장을 위한 전용 라인",
        ],
        "specs": [
            ("DS500E / DS1000E 생산능력", "500 ~ 1,000 kg/h"),
            ("R Series 처리능력", "2,500 kg/h"),
        ],
    },
]

# ---------------------------------------------------------------------------
# CO2 리커버리 데이터
# ---------------------------------------------------------------------------

RECOVERY_INTRO_HTML = """
<p>드라이아이스를 생산할 때 액체 CO2를 대기압으로 낮추는 과정에서 절반 가량은 드라이아이스(고체)로,
나머지 절반은 가스로 바뀝니다. 이 가스는 보통 그대로 대기 중에 배출되는데, Cold Jet의
<b>RE-CO2 리커버리 시스템</b>은 이 가스를 회수해 다시 드라이아이스 생산에 투입합니다.
그 결과 액체 CO2 사용량과 비용을 크게 줄일 수 있습니다.</p>
<div class="icon-row" style="grid-template-columns:repeat(4,1fr);">
  <div class="item"><div class="ic">💧</div><span>액체 CO2 최대 40% 절감</span></div>
  <div class="item"><div class="ic">📈</div><span>동일 LCO2로 최대 70% 증산</span></div>
  <div class="item"><div class="ic">🌍</div><span>대기 배출 CO2 저감</span></div>
  <div class="item"><div class="ic">⏱️</div><span>ROI 대부분 12개월 이내</span></div>
</div>
<p style="margin-top:22px; font-size:13px; color:var(--text-muted);">거의 모든 브랜드의 펠렛타이저와 호환되는
모듈식 설계로, 기존 생산 라인에도 비교적 쉽게 추가할 수 있습니다. (출처: Cold Jet 공식 웹사이트)</p>
"""

_RECOVERY_COMMON_FEATURES = [
    "거의 모든 브랜드 펠렛타이저와 호환되는 모듈형 설계",
    "액체 CO2 사용량 절감으로 운영비 감소",
    "동일 액체 CO2 투입량 대비 드라이아이스 증산 가능",
    "대기 중 CO2 배출 저감",
]

RECOVERY_MODELS = [
    {
        "slug": "re-co2-80", "name": "RE-CO2 80", "tagline": "소규모 운영을 위한 모듈형 CO2 리커버리",
        "overview": [
            "RE-CO2 80은 PE-80과 같은 소형 펠렛타이저와 페어링되는 입문형 CO2 리커버리 모델로, "
            "소규모 생산 라인에도 CO2 재사용 효과를 적용할 수 있습니다.",
        ],
        "features": _RECOVERY_COMMON_FEATURES,
        "specs": [
            ("처리 용량", "최대 80 kg/h"),
            ("적합 조합", "PE-80 펠렛타이저"),
            ("상세 스펙", "정식 스펙시트로 안내해 드립니다"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PE-80", "pe-80")]},
    },
    {
        "slug": "re-co2-160", "name": "RE-CO2 160", "tagline": "중소 규모 생산 라인을 위한 CO2 리커버리",
        "overview": [
            "RE-CO2 160은 PR120H와 같은 중소용량 펠렛타이저와 페어링되는 모델로, 중간 규모 운영에서도 "
            "안정적인 CO2 회수 효율을 제공합니다.",
        ],
        "features": _RECOVERY_COMMON_FEATURES,
        "specs": [
            ("처리 용량", "최대 160 kg/h"),
            ("적합 조합", "PR120H 펠렛타이저"),
            ("상세 스펙", "정식 스펙시트로 안내해 드립니다"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PR120H", "pr120h")]},
    },
    {
        "slug": "re-co2-320-v2", "name": "RE-CO2 320 V2",
        "tagline": "가장 지능형 · 확장 가능 · 지속가능한 동급 최대 규모 CO2 리커버리 시스템",
        "overview": [
            "RE-CO2 320 V2는 드라이아이스 생산시설에서 배출되는 CO2 가스를 포집해 액체로 전환한 뒤 다시 "
            "생산에 투입하는 컴팩트한 리커버리 유닛입니다. V2 모델은 Cold Jet 펠렛타이저 제어판과 직접 "
            "통신하며, 여러 대를 동시에 운용할 때도 지능형으로 가스 흐름을 최적화합니다.",
        ],
        "advantages": [
            ("Sustainability", "배출되던 CO2 가스를 생산 자원으로 전환"),
            ("Efficiency", "액체 CO2 낭비를 최소화"),
            ("Cost Reduction", "연간 액체 CO2 비용을 최대 40%까지 절감"),
            ("Output Expansion", "동일한 액체 CO2 투입량으로 생산량을 최대 70%까지 확대"),
            ("User-Friendly", "펠렛타이저 HMI로 플러그앤플레이 제어, 규모에 맞춘 모듈 구성"),
        ],
        "features": [
            "재설계된 버퍼탱크 프레임 · 커버로 최적화된 가스 흐름",
            "개선된 밸브 제어 연결부",
            "과열 컨트롤러가 탑재된 전기 캐비닛",
            "24V DC 코일 및 추가 온도 센서",
            "저온 지역 대응 접근 플러그",
            "고성능 냉각팬 및 클로 커플링 모터",
            "바이패스 밸브가 장착된 리시버",
            "업그레이드된 2단 오일 분리기 · 오일 레귤레이터",
        ],
        "specs": [
            ("액화 용량", "최대 320 kg/h (705.4 lbs/hr)"),
            ("크기 (가로×세로×높이)", "2,718 × 1,320 × 3,751 mm"),
            ("버퍼탱크 미포함 높이", "2,259 mm"),
            ("유닛 무게", "2,175 kg (버퍼탱크 325 kg 별도)"),
            ("전원", "440~480V AC 60Hz 또는 400V AC 50Hz"),
            ("소비전력 · 전류", "50 kWh, 85A"),
            ("냉매유 · 압축기유", "POE32 / PAO68 (식품등급)"),
            ("작동 온도 범위", "5℃ ~ 30℃"),
            ("소음", "최대 85 dB"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PR350H", "pr350h"), ("PR750H", "pr750h")]},
    },
    {
        "slug": "re-co2-3500", "name": "RE-CO2 3500", "tagline": "대형 생산시설을 위한 고용량 · 고효율 CO2 리커버리",
        "overview": [
            "RE-CO2 3500은 대형 생산시설을 위한 고용량 CO2 리커버리 유닛입니다. 배출된 CO2를 압축 · "
            "냉각해 재사용 가능한 액체 CO2로 전환하며, 배출량 저감과 외부 공급 의존도 감소, 액체 CO2 "
            "비용 최대 절반 절감 효과를 기대할 수 있습니다. 컨테이너형 모듈로 최소한의 설비 변경만으로 "
            "설치할 수 있습니다.",
        ],
        "advantages": [
            ("Ultra-Low Energy Use", "동급 시스템 대비 업계 최저 수준의 에너지 소비"),
            ("R744 Refrigerant", "합성 냉매 없이 자연 냉매(CO2, R744) 사용"),
            ("Flexible Operation", "최대 용량 대비 25~100% 범위에서 유동적으로 운전"),
            ("Fully Autonomous", "운영자 개입 없이 완전 자동으로 운전"),
            ("Containerized Setup", "표준 컨테이너형으로 간편하게 설치"),
        ],
        "features": [
            "회수 CO2 톤당 135 kWh 이하의 에너지 소비",
            "합성 냉매가 필요 없는 자연 냉매(R744, CO2) 방식",
            "운영자 개입이 필요 없는 완전 자동 운전",
            "펠렛타이저 1~6대 규모까지 자동으로 생산 규모에 대응",
            "컨테이너형 설계로 최소한의 공간에 간편 설치",
            "오일프리 압축기로 암모니아 시스템 대비 유지보수 부담 최소화",
        ],
        "specs": [
            ("크기", "12.5m × 8.5m × 4.3m (컨테이너형)"),
            ("무게", "35,000 kg"),
            ("표준 처리 용량", "3,500 kg/h (옵션 시 최대 5,000 kg/h)"),
            ("전원", "3×400V+N+PE, 50Hz, TN-S"),
            ("소비전력", "톤당 135 kWh 이하"),
            ("냉매", "R744(CO2) 자연 냉매, 폐쇄루프 방식"),
            ("계장용 공기", "7 barg, ISO 8573-1 Class 2 기준"),
        ],
        "cross_links": {"label": "호환 펠렛타이저", "group": "pelletizer",
                         "items": [("PR750H", "pr750h"), ("PR1500H", "pr1500h")]},
    },
]

ACCESSORIES_HTML = """
<div class="sub-grid">
  <div class="sub-card"><h3>Applicators (어플리케이터)</h3><p>작업자의 편의성과 안전성을 고려해 설계된 핸들형 분사기구입니다.</p></div>
  <div class="sub-card"><h3>Nozzles (노즐)</h3><p>세척 강도와 분사 패턴을 결정하는 업계 최첨단 노즐 라인입니다.</p></div>
  <div class="sub-card"><h3>Hoses (호스)</h3><p>유연하면서도 내구성 있는 에어 · 블라스트 전용 호스입니다.</p></div>
  <div class="sub-card"><h3>Additional Accessories (기타 액세서리)</h3><p>퀵 커넥트 피팅 등 작업 편의를 높이는 부속품입니다.</p></div>
</div>
<p style="font-size:13px; color:var(--text-muted); margin-top:14px;">전체 라인업은
<a href="../nozzle.html">노즐 · 액세서리</a> 페이지에서도 확인하실 수 있습니다.</p>
"""


def _features_html(features):
    return "<ul style=\"padding-left:20px; display:grid; gap:8px;\">" + "".join(
        f"<li>{f}</li>" for f in features
    ) + "</ul>"


def _specs_html(specs):
    rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in specs)
    return f'<table class="compare-table"><tr><th>항목</th><th>사양</th></tr>{rows}</table>'


def _overview_html(paragraphs):
    return "".join(f"<p>{p}</p>" for p in paragraphs)


def _advantages_html(advantages):
    cards = "".join(
        f'<div class="sub-card"><h3>{title}</h3><p>{desc}</p></div>' for title, desc in advantages
    )
    return f"""
      <h2 style="font-size:20px; margin-top:36px;">Cold Jet&reg;만의 강점</h2>
      <div class="sub-grid" style="margin-top:14px;">{cards}</div>
"""


def _cross_links_html(cross_links, depth_group_prefix=".."):
    if not cross_links:
        return ""
    items = cross_links["items"]
    group = cross_links["group"]
    label = cross_links["label"]
    links = " · ".join(
        f'<a href="{depth_group_prefix}/{group}/{slug}.html"><b>{name}</b></a>' if slug else f"<b>{name}</b>"
        for name, slug in items
    )
    return f"""
      <div class="placeholder-note" style="border-style:solid; background:var(--mint); border-color:var(--mint-line); color:var(--text-dark);">
        {label}: {links}
      </div>
"""


def _quicknav(has_accessories):
    items = [("#features", "Features"), ("#specs", "Specifications")]
    if has_accessories:
        items.append(("#accessories", "Accessories"))
    chips = "".join(f'<a class="chip" href="{href}">{label}</a>' for href, label in items)
    return f'<div class="chip-grid" style="margin:20px 0 8px;">{chips}</div>'


def build_group_index(root, code, group_slug, group_title, group_tagline, models,
                       categories, nav_html, footer_html, page_shell, asset, intro_html=""):
    depth = 2
    group_dir = os.path.join(root, code, group_slug)
    os.makedirs(group_dir, exist_ok=True)

    if categories:
        sections = ""
        for cat_key, cat_title, cat_desc in categories:
            cat_models = [m for m in models if m["category"] == cat_key]
            cards = "".join(f"""
        <div class="sub-card">
          <div class="img-ph" style="min-height:120px; margin-bottom:14px;">[제품 이미지]</div>
          <h3>{m['name']}</h3>
          <p>{m['tagline']}</p>
          <a class="more" href="{m['slug']}.html">모델 상세 보기 →</a>
        </div>""" for m in cat_models)
            sections += f"""
      <h2 style="font-size:20px; margin-top:36px; color:var(--blue-dark);">{cat_title}</h2>
      <p style="color:var(--text-muted); font-size:14px; margin-bottom:16px;">{cat_desc}</p>
      <div class="sub-grid">{cards}</div>
"""
    else:
        cards = "".join(f"""
        <div class="sub-card">
          <div class="img-ph" style="min-height:120px; margin-bottom:14px;">[제품 이미지]</div>
          <h3>{m['name']}</h3>
          <p>{m['tagline']}</p>
          <a class="more" href="{m['slug']}.html">모델 상세 보기 →</a>
        </div>""" for m in models)
        sections = f'<div class="sub-grid" style="margin-top:20px;">{cards}</div>'

    body = f"""
  <div class="wrap breadcrumb"><a href="{asset('index.html', depth)}">홈</a> &gt;
    <a href="{asset('products/index.html', depth)}">제품 · 자동화 · 공급</a> &gt; {group_title}</div>
  <section class="page-hero" style="padding-top:24px;">
    <div class="wrap">
      <span class="cat">제품</span>
      <h1>{group_title}</h1>
      <p>{group_tagline}</p>
    </div>
  </section>
  <section>
    <div class="wrap">
      {intro_html}
      {sections}
      <div class="cta-band" style="margin-top:36px;">
        <div>
          <h3>어떤 모델이 맞을지 모르겠다면</h3>
          <p>현장 조건을 알려주시면 담당자가 적합한 모델을 추천해 드립니다.</p>
        </div>
        <a class="cta-btn" href="{asset('products/quote.html', depth)}">견적문의 하기</a>
      </div>
    </div>
  </section>
"""
    html = page_shell(group_title, group_tagline, depth, code, body)
    with open(os.path.join(group_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def build_model_page(root, code, group_slug, group_title, model, siblings,
                      nav_html, footer_html, page_shell, asset):
    depth = 2
    group_dir = os.path.join(root, code, group_slug)
    os.makedirs(group_dir, exist_ok=True)

    overview_block = ""
    if model.get("overview"):
        overview_block = f"""
      {_overview_html(model['overview'])}
"""

    advantages_block = _advantages_html(model["advantages"]) if model.get("advantages") else ""

    accessories_block = ""
    if model.get("accessories"):
        accessories_block = f"""
      <h2 id="accessories" style="font-size:20px; margin-top:36px; scroll-margin-top:90px;">Accessories</h2>
      {ACCESSORIES_HTML}
"""

    cross_links_block = _cross_links_html(model.get("cross_links"))

    other_cards = "".join(f"""
        <div class="sub-card">
          <h3>{s['name']}</h3>
          <p>{s['tagline']}</p>
          <a class="more" href="{s['slug']}.html">모델 상세 보기 →</a>
        </div>""" for s in siblings if s["slug"] != model["slug"])

    maintenance_block = f"""
      <div class="placeholder-note" style="margin-top:20px;">
        정기 점검이 필요하신가요? 예방정비 플랜 안내와 정식 스펙시트 · 카탈로그 자료 요청은
        <a href="{asset('products/quote.html', depth)}">견적문의</a>를 통해 접수해 드립니다.
      </div>
"""

    body = f"""
  <div class="wrap breadcrumb"><a href="{asset('index.html', depth)}">홈</a> &gt;
    <a href="{asset('products/index.html', depth)}">제품 · 자동화 · 공급</a> &gt;
    <a href="index.html">{group_title}</a> &gt; {model['name']}</div>
  <section class="page-hero" style="padding-top:24px;">
    <div class="wrap">
      <span class="cat">제품</span>
      <h1>{model['name']}</h1>
      <p>{model['tagline']}</p>
      {_quicknav(model.get('accessories', False))}
    </div>
  </section>
  <section>
    <div class="wrap">
      <div style="display:grid; grid-template-columns:2fr 1fr 1fr; gap:12px; margin-bottom:28px;">
        <div class="img-ph" style="min-height:240px;">[제품 대표 이미지]</div>
        <div class="img-ph" style="min-height:240px;">[제품 상세 이미지 1]</div>
        <div class="img-ph" style="min-height:240px;">[제품 상세 이미지 2]</div>
      </div>

      {overview_block}
      {advantages_block}

      <h2 id="features" style="font-size:20px; margin-top:36px; scroll-margin-top:90px;">Features</h2>
      {_features_html(model['features'])}

      <h2 id="specs" style="font-size:20px; margin-top:36px; scroll-margin-top:90px;">Specifications</h2>
      {_specs_html(model['specs'])}
      {cross_links_block}
      {accessories_block}
      {maintenance_block}

      <h2 style="font-size:20px; margin-top:36px;">같은 카테고리의 다른 모델</h2>
      <div class="sub-grid">{other_cards}</div>

      <div class="cta-band" style="margin-top:12px;">
        <div>
          <h3>{model['name']} 도입을 검토 중이신가요?</h3>
          <p>현장 조건에 맞는 정확한 견적을 안내해 드립니다.</p>
        </div>
        <a class="cta-btn" href="{asset('products/quote.html', depth)}">견적문의 하기</a>
      </div>
    </div>
  </section>
"""
    html = page_shell(f"{model['name']} | {group_title}", model["tagline"], depth, code, body)
    with open(os.path.join(group_dir, f"{model['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)


# (2026-09-09, 15차 핸드오프 — 블라스터 페이지 신규 제작) products/blaster/index.html
# 을 build_group_index()의 자동 생성 템플릿 대신 완전히 새로 디자인한 14섹션
# 커스텀 페이지로 교체한다. Hero 영상 → Application → 4 Systems → Particle
# Control → Cold Jet Difference → Product Lineup(탭 필터) → Find the Right
# System(매트릭스) → Proven in the Field(국내 고객사 로고 20+) → Cold Jet+VATEK
# → Test Before You Buy → What You Need → Automation → Choosing → Final CTA.
# BLASTER_MODELS/BLASTER_CATEGORIES 데이터 구조는 이 커스텀 디자인에 아직
# 맞춰 재설계되지 않았으므로(범위 밖) 이 상수는 그대로 정적 HTML을 보관한다 —
# 개별 모델 상세 페이지(build_model_page)는 기존 데이터 기반 생성 그대로 유지.
BLASTER_PAGE_TITLE = "드라이아이스 세척기 · DRY ICE BLASTERS"
BLASTER_PAGE_DESC = "세척 대상이 다르면 필요한 블라스터도 달라집니다. Smart · Pellet · MicroParticle · Specialty — Cold Jet 드라이아이스 세척기의 차이와 선택 기준, 그리고 바테크의 테스트·지원을 안내합니다."
BLASTER_SCRIPT = """  <script>
  (function(){
    // 이미지: 로드 완료 시 부드럽게 나타남 (JS가 있을 때만 숨김 → 무-JS 환경 안전)
    document.documentElement.classList.add('js-media-fade');
    var imgs=document.querySelectorAll('.bls-sec img, .bls-pcs img, .bls-hero-stage img');
    var mark=function(img){ img.classList.add('is-loaded'); };
    imgs.forEach(function(img){
      if (img.complete && img.naturalWidth>0) { mark(img); return; }
      img.addEventListener('load',function(){ mark(img); },{once:true});
      img.addEventListener('error',function(){ mark(img); },{once:true});
    });
    // 비디오: 뷰포트 근처에서만 다운로드 시작, 재생 가능해지면 페이드 인
    var vids=document.querySelectorAll('video.bls-media-fade');
    var prime=function(v){
      if (v.dataset.primed) return; v.dataset.primed='1';
      if (v.preload==='none') v.preload='auto';
      v.load();
    };
    vids.forEach(function(v){
      var show=function(){ v.classList.add('is-loaded'); };
      if (v.readyState>=3) show();
      v.addEventListener('loadeddata',show,{once:true});
      v.addEventListener('canplay',show,{once:true});
    });
    if ('IntersectionObserver' in window) {
      var vo=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ prime(e.target); vo.unobserve(e.target); } }); },{rootMargin:'600px 0px'});
      vids.forEach(function(v){ vo.observe(v); });
    } else { vids.forEach(prime); }
  })();
  </script>
  <script>
  (function(){
    var v=document.getElementById('blsDetailVideo'),btn=document.getElementById('blsDetailPlayBtn');
    if (v && btn) {
      btn.addEventListener('click',function(){
        if (v.paused) { v.play(); } else { v.pause(); }
      });
      v.addEventListener('play',function(){
        btn.classList.add('is-playing');
        btn.querySelector('.bls-play-label').textContent='일시정지';
        btn.querySelector('.bls-play-icon').textContent='❙❙';
      });
      v.addEventListener('pause',function(){
        btn.classList.remove('is-playing');
        btn.querySelector('.bls-play-label').textContent='영상 재생';
        btn.querySelector('.bls-play-icon').textContent='▶';
      });
    }
    document.querySelectorAll('.bls-prod-bg-btn').forEach(function(btn){
      btn.addEventListener('click',function(e){
        e.preventDefault();
        var media=btn.closest('.bls-prod-media'), img=media.querySelector('img');
        var toBlack=!media.classList.contains('is-black-bg');
        media.classList.toggle('is-black-bg',toBlack);
        img.style.opacity=0;
        setTimeout(function(){
          img.src = toBlack ? img.getAttribute('data-bg-black') : img.getAttribute('data-bg-white');
          img.style.opacity=1;
        },180);
        btn.textContent = toBlack ? '흰색 배경' : '검정 배경';
      });
    });
    [['pcsVideo1','pcsPlayBtn1'],['pcsVideo2','pcsPlayBtn2']].forEach(function(pair){
      var vv=document.getElementById(pair[0]), bb=document.getElementById(pair[1]);
      if (!vv || !bb) return;
      var media=vv.closest('.bls-pcs-demo-media');
      bb.addEventListener('click',function(){ if (vv.paused) { vv.play(); } else { vv.pause(); } });
      vv.addEventListener('play',function(){ bb.classList.add('is-playing'); bb.querySelector('.bls-play-label').textContent='일시정지'; bb.querySelector('.bls-play-icon').textContent='❙❙'; if (media) media.classList.add('is-playing'); });
      vv.addEventListener('pause',function(){ bb.classList.remove('is-playing'); bb.querySelector('.bls-play-label').textContent='영상 재생'; bb.querySelector('.bls-play-icon').textContent='▶'; if (media) media.classList.remove('is-playing'); });
    });
  })();
  </script>
  <script>
  (function(){
    var tabs=document.querySelectorAll('.bls-tabs button'),cards=document.querySelectorAll('#blsProdGrid .bls-prod');
    tabs.forEach(function(b){b.addEventListener('click',function(){
      if (b.classList.contains('is-active')) return;
      tabs.forEach(function(t){t.classList.toggle('is-active',t===b);});
      var f=b.getAttribute('data-filter');
      var toShow=[],toHide=[];
      cards.forEach(function(c){
        var cats=(c.getAttribute('data-cat')||'').split(' ');
        var show=f==='all'||cats.indexOf(f)>-1;
        var wasHidden=c.classList.contains('is-hidden');
        if (show && wasHidden) toShow.push(c);
        else if (!show && !wasHidden) toHide.push(c);
      });
      toHide.forEach(function(c){ c.classList.add('is-filter-out'); });
      setTimeout(function(){
        toHide.forEach(function(c){ c.classList.add('is-hidden'); c.classList.remove('is-filter-out'); });
        toShow.forEach(function(c,i){
          c.classList.remove('is-hidden');
          c.classList.add('is-filter-in');
          void c.offsetWidth;
          setTimeout(function(){ c.classList.remove('is-filter-in'); }, 40 + i*60);
        });
      }, toHide.length ? 260 : 0);
    });});
  })();
  (function(){
    var scaleEl=document.getElementById('blsScale'),fill=document.getElementById('blsScaleFill'),live=document.getElementById('blsScaleLive');
    var dial=document.getElementById('pcsDial'),panelNum=document.getElementById('pcsLiveNum');
    if (!scaleEl || !fill || !live) return;
    var MIN=0.3, MAX=3.0, STEP=0.1, ticking=false;
    var snapVal=function(v){ return Math.round((v-MIN)/STEP)*STEP+MIN; };
    var sliderPath=document.getElementById('pcsSliderPath'),sliderThumbEl=document.getElementById('pcsSliderThumb');
    var pathLen=sliderPath ? sliderPath.getTotalLength() : 0;
    var placeThumb=function(progress){
      if (!sliderPath || !sliderThumbEl) return;
      var pt=sliderPath.getPointAtLength(progress*pathLen);
      sliderThumbEl.setAttribute('cx',pt.x);
      sliderThumbEl.setAttribute('cy',pt.y);
    };
    var update=function(){
      ticking=false;
      var rect=scaleEl.getBoundingClientRect();
      var start=window.innerHeight*0.85, end=window.innerHeight*0.25;
      var progress=(start-rect.top)/(start-end+rect.height);
      progress=Math.min(Math.max(progress,0),1);
      var value=snapVal(MAX-progress*(MAX-MIN));
      var pct=((value-MIN)/(MAX-MIN))*100;
      progress=(MAX-value)/(MAX-MIN);
      fill.style.width=pct+'%';
      live.textContent=value.toFixed(1)+' mm';
      if (dial) dial.style.transform='translate(-50%,-50%) rotate('+(135-progress*270).toFixed(1)+'deg)';
      if (panelNum) panelNum.textContent=value.toFixed(1);
      placeThumb(progress);
    };
    var onScroll=function(){ if(!ticking){ ticking=true; requestAnimationFrame(update); } };
    window.addEventListener('scroll',onScroll,{passive:true});
    window.addEventListener('resize',onScroll);
    update();

    // 슬라이더 바를 잡고 좌우로 움직여 다이얼 조작
    var slider=document.getElementById('pcsSlider'),thumb=sliderThumbEl;
    var applyProgress=function(progress){
      progress=Math.min(Math.max(progress,0),1);
      var value=snapVal(MAX-progress*(MAX-MIN));
      var pct=((value-MIN)/(MAX-MIN))*100;
      progress=(MAX-value)/(MAX-MIN);
      fill.style.width=pct+'%';
      live.textContent=value.toFixed(1)+' mm';
      if (dial) dial.style.transform='translate(-50%,-50%) rotate('+(135-progress*270).toFixed(1)+'deg)';
      if (panelNum) panelNum.textContent=value.toFixed(1);
      placeThumb(progress);
    };
    if (slider && thumb) {
      var sliding=false;
      var progressFromEvent=function(e){
        var r=slider.getBoundingClientRect();
        return (e.clientX-r.left)/r.width;
      };
      slider.style.cursor='grab';
      slider.addEventListener('pointerdown',function(e){
        sliding=true;
        slider.style.cursor='grabbing';
        slider.setPointerCapture(e.pointerId);
        applyProgress(progressFromEvent(e));
        e.preventDefault();
      });
      slider.addEventListener('pointermove',function(e){
        if (!sliding) return;
        applyProgress(progressFromEvent(e));
      });
      var stopSlide=function(e){
        if (!sliding) return;
        sliding=false;
        slider.style.cursor='grab';
        try { slider.releasePointerCapture(e.pointerId); } catch(err){}
      };
      slider.addEventListener('pointerup',stopSlide);
      slider.addEventListener('pointercancel',stopSlide);
    }
  })();
    </script>

"""
BLASTER_HUB_BODY = """
  <!-- ============ 01 HERO ============ -->
  <section class="subhero-parallax bls-hero-stage">
    <video class="subhero-parallax-img bls-hero-video" autoplay muted loop playsinline preload="auto" poster="../../assets/img/blaster-catalog-hero-natural.png" aria-label="Cold Jet Aero2 PCS ULTRA · PLT ULTRA 블라스터" data-buffer="100" data-pan-scale="1.08" data-no-blur="true">
      <source src="../../assets/video/blaster-hero-banner.mp4" type="video/mp4" />
    </video>
    <div class="subhero-breadcrumb wrap"><a href="../../index.html">홈</a> &gt; <a href="../index.html">제품 · 자동화 · 공급</a> &gt; 드라이아이스 세척기</div>
    <div class="subhero-textbox bls-hero-box">
      <span class="ind-hero-eyebrow">COLD JET × VATEK&nbsp;&nbsp;/&nbsp;&nbsp;DRY ICE BLASTERS</span>
      <h1>세척의 차이를<br>만드는 <span class="bls-hero-accent">기술.</span></h1>
      <p class="bls-hero-main">입자 제어부터 안정적인 분사까지.<br>Cold Jet 드라이아이스 블라스터의 기술을<br>바테크의 현장 지원과 함께 만나보세요.</p>
    </div>
    <div class="bls-hero-mask" aria-hidden="true"></div>
  </section>

  <!-- ============ 02 SEE IT IN ACTION ============ -->
  <section class="bls-sec bls-cover" id="bls-start">
    <div class="wrap">
      <div class="bls-head is-row reveal">
        <div>
          <span class="bls-dot-eyebrow">BUILT WITH PRECISION</span>
          <h2 class="cmp-h2">디테일에서 드러나는<br>Cold Jet의 완성도.</h2>
        </div>
        <p class="bls-sub is-side">Cold Jet 블라스터의 구조와 마감을<br>가까이에서 살펴보세요.</p>
      </div>
      <div class="bls-showcase-frame reveal">
      <div class="bls-showcase">
        <div class="bls-showcase-media">
          <video id="blsDetailVideo" class="bls-media-fade" muted loop playsinline preload="metadata" poster="../../assets/img/blaster-detail-poster.png">
            <source src="../../assets/video/blaster-hero.mp4" type="video/mp4" />
          </video>
          <span class="bls-showcase-cap">COLD JET&nbsp;&nbsp;/&nbsp;&nbsp;PRODUCT DETAILS</span>
          <button type="button" class="bls-play-btn" id="blsDetailPlayBtn" aria-label="영상 재생">
            <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
          </button>
        </div>
        <div class="bls-showcase-body">
          <span class="bls-dot-eyebrow">A CLOSER LOOK</span>
          <h3>가까이 볼수록,<br>드러나는 디테일.</h3>
          <p>장비의 형태와 구성, 각 부분의 마감까지. 짧은 제품 영상으로 Cold Jet 블라스터를 가까이에서 만나보세요.</p>
          <p>그 안에서 세척을 제어하는 입자 · 공급 · 분사 기술도 이어서 살펴볼 수 있습니다.</p>
          <a class="bls-textlink" href="#bls-systems">내부 기술 살펴보기 ↓</a>
        </div>
      </div>
      </div>
    </div>
  </section>

  <!-- ============ 03 PARTICLE CONTROL ============ -->
  <section class="cmp-dark bls-pcs" id="bls-pcs">
    <div class="wrap">
      <div class="bls-pcs-head reveal">
        <span class="cmp-eyebrow">PARTICLE CONTROL</span>
        <h2 class="cmp-h2" style="line-height:61.2px; font-size:48px">더 섬세하게, 더 강력하게,<br /></h2>
        <div class="cmp-dark-body">
          <div><h2 class="cmp-h2" style="line-height:61.2px; font-size:31px; margin-top:0px">입자 크기가 달라지면 더 많은 걸 할 수 있습니다.</h2></div>
        </div>
      </div>
      <div class="bls-scale-row">
      <div class="bls-pcs-left">
      <div class="bls-scale reveal" id="blsScale">
        <div class="bls-scale-ends"><span>PRECISION</span><span>PERFORMANCE</span></div>
        <div class="bls-scale-bar">
          <b>0.3 mm</b>
          <div class="bls-scale-line">
            <div class="bls-scale-fill" id="blsScaleFill"></div>
            <i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i>
          </div>
          <b id="blsScaleLive">3.0 mm</b>
        </div>
        <div class="bls-scale-ends is-sub"><span>Micro Particle</span><span>Full Pellet</span></div>
      </div>
      <div class="bls-pcs-demos reveal">
        <div class="bls-pcs-demo">
          <div class="bls-pcs-demo-media">
            <video id="pcsVideo1" class="bls-media-fade" muted loop playsinline preload="none">
              <source src="../../assets/video/pcs-demo-namecard.mp4" type="video/mp4" />
            </video>
            <div class="bls-pcs-demo-overlay">Micro Particle<br />0.3mm</div>
            <button type="button" class="bls-play-btn is-small" id="pcsPlayBtn1" aria-label="영상 재생">
              <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
            </button>
          </div>
        </div>
        <div class="bls-pcs-demo">
          <div class="bls-pcs-demo-media">
            <video id="pcsVideo2" class="bls-media-fade" muted loop playsinline preload="none">
              <source src="../../assets/video/pcs-demo-asphalt.mp4" type="video/mp4" />
            </video>
            <div class="bls-pcs-demo-overlay">Full Pellet<br />3.0mm</div>
            <button type="button" class="bls-play-btn is-small" id="pcsPlayBtn2" aria-label="영상 재생">
              <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
            </button>
          </div>
        </div>
      </div>
      </div>
      <div class="bls-pcs-panel reveal">
        <div class="bls-pcs-panel-frame">
          <img class="bls-pcs-panel-img" src="../../assets/img/pcs-panel-frame.png" alt="Cold Jet PCS 컨트롤 디스플레이" />
          <span class="bls-pcs-panel-num" id="pcsLiveNum">3.0</span>
          <img class="bls-pcs-panel-dial" id="pcsDial" src="../../assets/img/pcs-dial-knob.png" alt="PCS 조절 다이얼" />
        </div>
        <div class="bls-pcs-slider" id="pcsSlider">
          <svg viewBox="0 0 500 74" preserveAspectRatio="none" width="100%" height="74" style="display:block;">
            <defs>
              <linearGradient id="pcsSliderGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#263238"></stop>
                <stop offset="55%" stop-color="#2f6b74"></stop>
                <stop offset="100%" stop-color="#6fd8cf"></stop>
              </linearGradient>
            </defs>
            <path id="pcsSliderPath" d="M20,10 C20,64 480,64 480,10" fill="none" stroke="url(#pcsSliderGrad)" stroke-width="6" stroke-linecap="round"></path>
            <circle id="pcsSliderThumb" r="9" fill="#fff" stroke="#1b6d78" stroke-width="2" cx="20" cy="10"></circle>
          </svg>
        </div>
        <span class="bls-pcs-panel-cap" style="color:#ffffff; opacity:1; font-size:15px">바를 움직여 사이즈를 조절하세요</span>
      </div>
      </div>
      <div class="bls-pcs-grid">
        <div class="cmp-dark-body bls-pcs-desc">
          <p>Cold Jet의 PCS®는 3 mm 드라이아이스 펠렛을 투입해 0.3 mm에서 3.0 mm까지 0.1 mm 단위로 총 28개의 입자 크기를 선택할 수 있습니다.</p>
          <p>작은 입자와 낮은 압력으로 민감한 표면을 세척하거나, 더 큰 입자와 적절한 압력을 사용해 보다 강한 오염 제거 조건을 설정할 수 있습니다.</p>
        </div>
        <ul class="bls-factors reveal">
          <li><span>01</span><b>PARTICLE SIZE</b><small>입자 크기</small></li>
          <li><span>02</span><b>PRESSURE</b><small>분사 압력</small></li>
          <li><span>03</span><b>FEED RATE</b><small>드라이아이스 공급량</small></li>
          <li><span>04</span><b>NOZZLE &amp; AIRFLOW</b><small>노즐과 공기 흐름</small></li>
        </ul>
      </div>
      <p class="cmp-dark-final bls-dark-final">작업에 맞는 세척 조건을 찾는 것이<br><em>장비 선택의 출발점</em>입니다.</p>
    </div>
  </section>

  <!-- ============ 04 DRY ICE BLASTER SYSTEMS ============ -->
  <section class="bls-sec bls-sys-sec tint-hatch" id="bls-systems">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">DRY ICE BLASTER SYSTEMS</span>
        <h2 class="cmp-h2">작업 목적에 따라 선택하는<br>Cold Jet 블라스터</h2>
        <p class="bls-sub">Cold Jet의 블라스터는 사용하는 드라이아이스 입자와 제어 방식, 필요한 세척 강도와 작업조건에 따라 서로 다른 제품군으로 구성되어 있습니다.</p>
      </div>
      <div class="bls-sys-grid">
        <article class="bls-sys reveal is-large-media" id="bls-sys-smart">
          <div class="bls-sys-media">
            <img class="is-main" src="../../assets/img/blaster-smart-lineup.png" alt="Cold Jet Aero2 PCS ULTRA · PLT ULTRA · i3 MicroClean" loading="lazy" decoding="async" />
          </div>
          <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">01</span>
            <span class="bls-en">SMART BLASTER</span>
            <h3 style="color: #000000">스마트형 블라스터</h3>
            <p class="bls-sys-head">세척 조건을 세밀하게 제어하고,<br>반복해서 사용할 수 있도록.</p>
            <p>Smart 계열은 세척 조건을 디지털 방식으로 설정하고 작업에 맞게 세밀하게 조정할 수 있는 제품군입니다.</p>
            <p>특허 받은 PCS 기술이 적용된 모델은 3 mm 드라이아이스 펠렛을 입력해 0.3 mm부터 3.0 mm까지 0.1mm 단위로 입자 크기를 조절할 수 있어, 민감한 표면의 정밀 세척부터 강력한 세척이 필요한 작업까지 하나의 장비에서 폭넓게 조건을 설정할 수 있습니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="aero2-ultra.html">Aero2 PCS ULTRA</a><span class="bls-badge">PARTICLE CONTROL SYSTEM</span><a class="bls-model-chip" href="aero2-ultra.html">Aero2 PLT ULTRA</a></dd></div>
              <div><dt>PCS ULTRA</dt><dd>0.3 – 3.0 mm · 28 Particle Sizes</dd></div>
            </dl>
            <a class="bls-more" href="aero2-ultra.html">Smart Blaster 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-iot.png" alt="IoT" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
        <article class="bls-sys reveal is-large-media" id="bls-sys-pellet" style="--reveal-delay:0.06s">
          <div class="bls-sys-media">
            <img class="is-main" src="../../assets/img/blaster-pellet-lineup.png" alt="Cold Jet Aero Series · ELITE 20 · IceRocket PLT" loading="lazy" decoding="async" />
          </div>
            <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">02</span>
            <span class="bls-en">PELLET BLASTER</span>
            <h3 style="color: #000000">펠렛형 블라스터</h3>
            <p class="bls-sys-head">일반 산업 세척과<br>강한 오염 제거가 필요한 작업에.</p>
            <p>3 mm 드라이아이스 펠렛을 사용하는 대표적인 산업용 블라스터입니다.</p>
            <p>생산설비와 금형, 오일·그리스, 카본과 고착된 공정 잔류물처럼 상대적으로 높은 세척력이 필요한 작업에 폭넓게 활용됩니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="aero-series.html">Aero Series</a><a class="bls-model-chip" href="elite20-icerocket.html">ELITE 20</a><a class="bls-model-chip" href="elite20-icerocket.html">IceRocket PLT</a></dd></div>
              <div><dt>사용 입자</dt><dd>3 mm PELLET</dd></div>
            </dl>
            <a class="bls-more" href="aero-series.html">Pellet Blaster 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-pellet.png" alt="3mm Pellet" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
        <article class="bls-sys reveal is-large-media" id="bls-sys-micro">
          <div class="bls-sys-media">
            <img class="is-main" src="../../assets/img/blaster-micro-lineup.png" alt="Cold Jet i3 MicroClean · i3 MicroClean 2 · SDI Select 60" loading="lazy" decoding="async" />
          </div>
          <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">03</span>
            <span class="bls-en">MICRO PARTICLE BLASTER</span>
            <h3 style="color: #000000">마이크로파티클 블라스터</h3>
            <p class="bls-sys-head">충격에 민감한 표면에는<br>더 작은 입자로.</p>
            <p>MicroParticle 블라스터는 일반 3 mm 펠렛보다 작은 입자를 사용하여 상대적으로 부드럽고 세밀한 세척이 필요한 작업에 활용됩니다.</p>
            <p>정밀 금형, 부품 마무리, 민감한 표면, 역사적 복원 등 표면 상태를 세심하게 고려해야 하는 작업에 적합합니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="i3-microclean-2.html">i³ MicroClean 2</a><span class="bls-badge">SMART MICRO PARTICLE</span><a class="bls-model-chip" href="i3-microclean.html">i³ MicroClean</a><a class="bls-model-chip" href="sdi-select-60.html">SDI Select 60</a></dd></div>
              <div><dt>사용 입자</dt><dd>MICRO PARTICLE — 블록을 깎아 만든 미세 입자</dd></div>
            </dl>
            <a class="bls-more" href="i3-microclean-2.html">MicroParticle Blaster 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-micro.png" alt="Micro Particle" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
        <article class="bls-sys reveal is-large-media" id="bls-sys-specialty" style="--reveal-delay:0.06s">
          <div class="bls-sys-media is-contain">
            <img class="is-main" src="../../assets/img/blaster-specialty-lineup.png" alt="Cold Jet C100 · E-CO2 150" loading="lazy" style="position: absolute; left: 21px; top: 21px; width: 662px; height: 461px" />
          </div>
          <div class="bls-sys-body" style="position: relative">
            <div class="bls-sys-divider"></div>
            <span class="bls-num">04</span>
            <span class="bls-en">SPECIALTY BLASTER</span>
            <h3 style="color: #000000">특수형 블라스터</h3>
            <p class="bls-sys-head">일반 블라스터로 해결하기 어려운<br>특수한 작업 조건에.</p>
            <p>전기를 사용할 수 없는 환경이나 연마재를 함께 사용해야 하는 표면처리처럼 일반적인 드라이아이스 세척과 다른 조건에는 특수 시스템을 검토할 수 있습니다.</p>
            <p>E-CO2 150은 Cold Jet 블라스터(PLT 60 · Aero 80 · C100)에 가압식 연마재 포트를 결합해 드라이아이스와 연마재를 함께 분사하는 별도의 혼합 블라스팅 시스템으로, 도막·코팅·부식 제거처럼 보다 공격적인 표면처리에 사용합니다.</p>
            <dl class="bls-sys-models">
              <div><dt>대표 모델</dt><dd><a class="bls-model-chip" href="c100.html">C100 — 완전 공압식</a><a class="bls-model-chip" href="e-co2-150.html">E-CO2 150 — 드라이아이스 + 연마재</a></dd></div>
            </dl>
            <a class="bls-more" href="c100.html">Specialty System 자세히 보기 <i>→</i></a>
            <img class="bls-sys-icon-inline" src="../../assets/img/icon-specialty.png" alt="Specialty" style="position: absolute; left: 520px; top: 111px; width: 130px; height: 130px" />
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- ============ 05 PRODUCT LINEUP ============ -->
  <section class="bls-sec bls-lineup-sec tint-hatch" id="bls-lineup">
    <div class="wrap">
      <div class="bls-head is-row reveal">
        <div>
          <span class="cmp-eyebrow">PRODUCT LINEUP</span>
          <h2 class="cmp-h2">Cold Jet 블라스터 라인업</h2>
          <p class="bls-sub">작업 목적과 필요한 세척 조건에 따라 적합한 제품을 비교해보세요.</p>
        </div>
        <div class="bls-tabs" role="tablist" aria-label="제품군 필터">
          <button data-filter="core" type="button"><b>CORE</b><small>핵심 모델</small></button>
          <button class="is-active" data-filter="all" type="button"><b>ALL</b><small>전체 모델</small></button>
          <button data-filter="smart" type="button"><b>SMART</b><small>자동화, 모든 표면</small></button>
          <button data-filter="pellet" type="button"><b>PELLET</b><small>설비 고착 오염</small></button>
          <button data-filter="micro" type="button"><b>MICRO PARTICLE</b><small>정밀·민감한 표면</small></button>
          <button data-filter="specialty" type="button"><b>SPECIALTY</b><small>특수작업</small></button>
        </div>
      </div>
      <div class="bls-prod-grid" id="blsProdGrid">
      <a class="bls-prod reveal" data-cat="core smart pellet micro" href="aero2-ultra.html" style="--reveal-delay:0s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero2-pcs-ultra-white.png" data-bg-black="../../assets/img/blaster-aero2-pcs-ultra.png" data-bg-white="../../assets/img/blaster-aero2-pcs-ultra-white.png" alt="Aero2® PCS ULTRA" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SMART</span><span class="bls-prod-cat">PELLET</span><span class="bls-prod-cat">MICRO PARTICLE</span><span class="bls-badge">PARTICLE CONTROL SYSTEM</span></div>
          <h3>Aero2® PCS ULTRA</h3>
          <p class="bls-prod-pos">입자 크기까지 설정하는 가장 넓은 조건 범위의 스마트 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>정밀 금형 · 민감한 표면 · 고착 오염 · 생산설비 · 로봇 · 자동화 라인</dd></div>
            <div><dt>핵심 기술</dt><dd>PCS® 0.3–3.0 mm · 28단계 · 프로그램 레시피 · 7" HMI · Cold Jet CONNECT®</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="smart pellet" href="aero2-ultra.html" style="--reveal-delay:0.06s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero2-plt-ultra-white.png" data-bg-black="../../assets/img/blaster-aero2-plt-ultra.png" data-bg-white="../../assets/img/blaster-aero2-plt-ultra-white.png" alt="Aero2® PLT ULTRA" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SMART</span><span class="bls-prod-cat">PELLET</span></div>
          <h3>Aero2® PLT ULTRA</h3>
          <p class="bls-prod-pos">3 mm 펠렛으로 세척 조건을 디지털 설정·저장하는 스마트 펠렛 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>생산설비 · 금형 · 반복 세척 공정 · 자동화 연계</dd></div>
            <div><dt>핵심 기술</dt><dd>SureFlow 피더 시스템 · 프로그램 레시피 · HMI · Cold Jet CONNECT®</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="core micro smart" href="i3-microclean-2.html" style="--reveal-delay:0.12s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-i3-microclean-2-white.png" data-bg-black="../../assets/img/blaster-i3-microclean-2.png" data-bg-white="../../assets/img/blaster-i3-microclean-2-white.png" alt="i³ MicroClean® 2" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SMART</span><span class="bls-prod-cat">MICRO PARTICLE</span><span class="bls-badge">SMART MICRO PARTICLE</span></div>
          <h3>i³ MicroClean® 2</h3>
          <p class="bls-prod-pos">정밀 세척 라인의 2세대 — 디지털 제어와 IoT를 갖춘 단일호스 마이크로파티클 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>정밀 금형 · 전자부품 · 부품 마무리 · 민감한 표면</dd></div>
            <div><dt>핵심 기술</dt><dd>블록 · 펠렛 모두 사용 · 최소 0.3 m³/min · 1.4–10 bar · 7" LCD · 레시피 · CONNECT®</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="pellet" href="aero-series.html" style="--reveal-delay:0.18s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero-40fp-white.png" data-bg-black="../../assets/img/blaster-aero-40fp.png" data-bg-white="../../assets/img/blaster-aero-40fp-white.png" alt="Aero® 40FP" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span></div>
          <h3>Aero® 40FP</h3>
          <p class="bls-prod-pos">풀프레셔 산업용 펠렛 블라스터 — 40 lb 호퍼 소형 모델</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>생산설비 유지보수 · 오일 · 그리스 · 고착 잔류물 · 이동이 잦은 현장</dd></div>
            <div><dt>핵심 기술</dt><dd>SureFlow 시스템 · 래디얼 피더 · 정밀 공급량 제어 · 내장 압력 조절기</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="pellet" href="aero-series.html" style="--reveal-delay:0.24s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-aero-80fp-white.png" data-bg-black="../../assets/img/blaster-aero-80fp.png" data-bg-white="../../assets/img/blaster-aero-80fp-white.png" alt="Aero® 80FP" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span></div>
          <h3>Aero® 80FP</h3>
          <p class="bls-prod-pos">풀프레셔 산업용 펠렛 블라스터 — 80 lb 호퍼 대용량 모델</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>생산설비 유지보수 · 오일 · 그리스 · 고착 잔류물 · 주조 · 코어박스</dd></div>
            <div><dt>핵심 기술</dt><dd>SureFlow 시스템 · 래디얼 피더 · 정밀 공급량 제어 · 내장 압력 조절기</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="core pellet micro" href="elite20-icerocket.html" style="--reveal-delay:0s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-elite-20-white.png" data-bg-black="../../assets/img/blaster-elite-20.png" data-bg-white="../../assets/img/blaster-elite-20-white.png" alt="ELITE 20" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span><span class="bls-prod-cat">MICRO PARTICLE</span></div>
          <h3>ELITE 20</h3>
          <p class="bls-prod-pos">전문가급 성능을 갖춘 입문형 펠렛 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>일반 산업 세척 · 설비 · 부품 · 첫 도입</dd></div>
            <div><dt>핵심 기술</dt><dd>3 mm 펠렛 · 단일호스 방식 · 컴팩트 구성</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="core pellet" href="elite20-icerocket.html" style="--reveal-delay:0.06s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-icerocket-plt-white.png" data-bg-black="../../assets/img/blaster-icerocket-plt.png" data-bg-white="../../assets/img/blaster-icerocket-plt-white.png" alt="IceRocket PLT" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">PELLET</span></div>
          <h3>IceRocket PLT</h3>
          <p class="bls-prod-pos">이동성이 좋은 소형 펠렛 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>일반 산업 세척 · 현장 이동 작업 · 첫 도입</dd></div>
            <div><dt>핵심 기술</dt><dd>3 mm 펠렛 · 컴팩트 · 경량 · 단일호스 방식</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="micro" href="i3-microclean.html" style="--reveal-delay:0.12s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-i3-microclean-white.png" data-bg-black="../../assets/img/blaster-i3-microclean.png" data-bg-white="../../assets/img/blaster-i3-microclean-white.png" alt="i³ MicroClean®" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">MICRO PARTICLE</span></div>
          <h3>i³ MicroClean®</h3>
          <p class="bls-prod-pos">드라이아이스 블록을 깎아 분사하는 탁상형 정밀 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>정밀 금형 · 전자부품 · 섬세한 표면 · 소규모 작업 공간</dd></div>
            <div><dt>핵심 기술</dt><dd>특허 쉐이빙 마이크로파티클 · 최소 12 cfm · 1.4–9.7 bar · 저소음 · 단일호스</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="micro pellet" href="sdi-select-60.html" style="--reveal-delay:0.18s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-sdi-select-60-white.png" data-bg-black="../../assets/img/blaster-sdi-select-60.png" data-bg-white="../../assets/img/blaster-sdi-select-60-white.png" alt="SDI Select™ 60" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">MICRO PARTICLE</span><span class="bls-prod-cat">PELLET</span></div>
          <h3>SDI Select™ 60</h3>
          <p class="bls-prod-pos">더스팅 · 일반 · 고압 세 가지 방식을 한 대로 전환하는 범용 모델</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>현장 조건이 다양한 작업 · 정밀 ~ 일반 세척 · 세척 대행</dd></div>
            <div><dt>핵심 기술</dt><dd>3가지 블라스팅 모드 · 단일호스 방식 · 국내 공급 실적 다수</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="specialty" href="c100.html" style="--reveal-delay:0s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-c100-white.png" data-bg-black="../../assets/img/blaster-c100.png" data-bg-white="../../assets/img/blaster-c100-white.png" alt="Cold Jet C100" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SPECIALTY</span></div>
          <h3>Aero® C100</h3>
          <p class="bls-prod-pos">전원 없이 압축공기만으로 작동하는 완전 공압식 블라스터</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>전기 사용이 제한되는 현장 · 방폭 · 옥외 작업 · 장거리 호스 작업</dd></div>
            <div><dt>핵심 기술</dt><dd>완전 공압식 · SureFlow 시스템 · 100 lb 호퍼 · 최대 100 ft 호스</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      <a class="bls-prod reveal" data-cat="specialty" href="e-co2-150.html" style="--reveal-delay:0.06s">
        <div class="bls-prod-media is-fill"><img src="../../assets/img/blaster-e-co2-150-white.png" data-bg-black="../../assets/img/blaster-e-co2-150.png" data-bg-white="../../assets/img/blaster-e-co2-150-white.png" alt="E-CO2™ 150" loading="lazy" decoding="async" /><button type="button" class="bls-prod-bg-btn" aria-label="검정 배경으로 보기">검정 배경</button></div>
        <div class="bls-prod-body">
          <div class="bls-prod-tags"><span class="bls-prod-cat">SPECIALTY</span></div>
          <h3>E-CO2™ 150</h3>
          <p class="bls-prod-pos">드라이아이스 + 연마재 혼합 분사 — 도막 · 코팅 · 부식 제거용 표면처리 시스템</p>
          <dl class="bls-prod-spec">
            <div><dt>대표 적용</dt><dd>도막 · 코팅 제거 · 부식 제거 · 표면 전처리</dd></div>
            <div><dt>핵심 기술</dt><dd>1.5 ft³ 가압식 연마재 포트 · PLT 60 · Aero 80 · C100과 결합 · 드라이아이스 단독 분사 전환</dd></div>
          </dl>
          <span class="bls-more">자세히 보기 <i>→</i></span>
        </div>
      </a>
      </div>
    </div>
  </section>

  <!-- ============ 06 THE COLD JET DIFFERENCE ============ -->
  <section class="bls-sec" id="bls-tech">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">THE COLD JET DIFFERENCE</span>
        <h2 class="cmp-h2">성능과 내구성은,<br>보이지 않는 곳에서 결정됩니다.</h2>
        <p class="bls-sub">드라이아이스 블라스터의 성능은 최대 압력이나 최고 용량만으로 결정되지 않습니다. 드라이아이스를 얼마나 균일하게 공급하는지, 압축공기의 흐름을 얼마나 효율적으로 활용하는지, 노즐에서 원하는 형태로 분사하는지에 따라 실제 세척 결과와 작업 효율이 달라집니다. Cold Jet은 공급부터 분사까지 이어지는 전체 흐름을 하나의 시스템으로 설계합니다.</p>
      </div>
      <div class="bls-tech-list">
        <article class="bls-tech reveal">
          <div class="bls-tech-media"><img src="../../assets/img/sureflow-feeder-system.png" alt="SureFlow 피더 시스템" loading="lazy" style="object-fit: contain; width: 420px; height: 412px" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">01</span>
            <span class="bls-en">SUREFLOW FEEDER SYSTEM</span>
            <h3>드라이아이스의 균일하고 안정적인 공급</h3>
            <p>특허받은 슈어플로우 피더 시스템은 험퍼(Thumper), 램로드(Ramrod), 진동기, 단열 호퍼를 하나로 통합한 시스템입니다. 호퍼를 최적의 상태로 진동·교반해 드라이아이스가 시스템 내부에 균일하게 공급되도록 하며, 안정적이고 일정한 분사 흐름을 유지합니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal" style="--reveal-delay:0.06s">
          <div class="bls-tech-media is-cad is-lg"><img src="../../assets/img/coldjet-feeder-cad.png" alt="Cold Jet 피더 시스템 구조" loading="lazy" decoding="async" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">02</span>
            <span class="bls-en">FEEDING SYSTEM</span>
            <h3>정밀한 공급으로 일정한 드라이아이스 분사 유지</h3>
            <p>드라이아이스를 안정적으로 공급하는 Feeder 설계는 분사 흐름과 실제 작업성에 영향을 줍니다. Cold Jet의 래디얼 피더는 공기역학적 로딩으로 패드와 로터의 마모를 줄이고, 공급량을 정밀하게 제어할 수 있도록 설계되었습니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal">
          <div class="bls-tech-media is-cad is-lg"><img src="../../assets/img/coldjet-nozzle-family.png" alt="Cold Jet 노즐 라인업" loading="lazy" style="object-fit: contain; width: 230%; height: 155%" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">03</span>
            <span class="bls-en">NOZZLE TECHNOLOGY</span>
            <h3>작업에 적합한 기술 집약적 노즐</h3>
            <p>같은 장비라도 노즐의 형상과 크기에 따라 분사폭과 집중도, 공기 소비량과 작업성이 달라질 수 있습니다. Cold Jet의 특허 노즐은 초음속 균일 분사와 낮은 승화 손실을 목표로 설계되어, 작업 대상에 맞게 다양한 형태로 제공됩니다.</p>
          </div>
        </article>
        <article class="bls-tech reveal" style="--reveal-delay:0.06s">
          <div class="bls-tech-media is-product is-lg"><img src="../../assets/img/coldjet-connect-dashboard.png" alt="Cold Jet Connect 대시보드" loading="lazy" decoding="async" /></div>
          <div class="bls-tech-body">
            <span class="bls-num">04</span>
            <span class="bls-en">COLD JET CONNECT®</span>
            <h3>온라인 장비 점검 및 자동 보고서</h3>
            <p>Cold Jet CONNECT®를 이용하면 PC나 모바일에서 장비 상태를 실시간으로 확인하고 원격 진단할 수 있습니다. 교육 자료 확인, 문제 해결, 서비스 지원 등 필요한 기능도 편리하게 이용할 수 있습니다.<br /><br />이 기능은 Aero2 ULTRA 시리즈와 i³ MicroClean 2 등 IoT를 지원하는 모델에 적용됩니다.</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- ============ 07 TRUSTED WORLDWIDE ============ -->
  <section class="bls-sec bls-ref-sec tint-hatch" id="bls-ref">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">TRUSTED WORLDWIDE</span>
        <h2 class="cmp-h2">국내외 다양한 산업 현장에서 Cold Jet과 함께하고 있습니다.</h2>
      </div>
    </div>
    <div class="bls-ref-row">
      <div class="bls-ref-track">
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-hyundai.png" alt="Hyundai" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kia.png" alt="Kia" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kumho-tire.png" alt="Kumho Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-nexen-tire.png" alt="Nexen Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-airbus_logo.png" alt="Airbus" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-spacex_logo.png" alt="SpaceX" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-coca-cola_logo.png" alt="Coca-Cola" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-nestle_logo.png" alt="Nestle" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-p_and_g_procter_and_gamble_logo.png" alt="P&G" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-caterpillar-logo.png" alt="Caterpillar" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-michelin_logo.png" alt="Michelin" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-goodyear_logo.png" alt="Goodyear" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-hyundai.png" alt="Hyundai" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kia.png" alt="Kia" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-kumho-tire.png" alt="Kumho Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-nexen-tire.png" alt="Nexen Tire" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-airbus_logo.png" alt="Airbus" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-aerospace-spacex_logo.png" alt="SpaceX" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-coca-cola_logo.png" alt="Coca-Cola" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-nestle_logo.png" alt="Nestle" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-p_and_g_procter_and_gamble_logo.png" alt="P&G" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-facility-maintenance-caterpillar-logo.png" alt="Caterpillar" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-michelin_logo.png" alt="Michelin" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rubber-tires-goodyear_logo.png" alt="Goodyear" loading="lazy" decoding="async" /></div>
      </div>
    </div>
    <div class="bls-ref-row is-reverse">
      <div class="bls-ref-track">
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-bmw.png" alt="BMW" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-toyota.png" alt="Toyota" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-honda.png" alt="Honda" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-ford.png" alt="Ford" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-tesla.png" alt="Tesla" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-power-generation-siemens_energy_logo.png" alt="Siemens Energy" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-mining-rio_tinto_logo.png" alt="Rio Tinto" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-ball_corporation_logo.png" alt="Ball Corporation" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-smurfit_kappa_logo.png" alt="Smurfit Kappa" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rail-sncf-logo.png" alt="SNCF" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-stryker_corporation_logo.png" alt="Stryker" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-becton-dickinson-logo.png" alt="Becton Dickinson" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-bmw.png" alt="BMW" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-toyota.png" alt="Toyota" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-honda.png" alt="Honda" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-ford.png" alt="Ford" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-logo-tesla.png" alt="Tesla" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-power-generation-siemens_energy_logo.png" alt="Siemens Energy" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-mining-rio_tinto_logo.png" alt="Rio Tinto" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-ball_corporation_logo.png" alt="Ball Corporation" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-packaging-smurfit_kappa_logo.png" alt="Smurfit Kappa" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-rail-sncf-logo.png" alt="SNCF" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-stryker_corporation_logo.png" alt="Stryker" loading="lazy" decoding="async" /></div>
        <div class="ref-pill"><img src="../../assets/img/ref/ref-medical-becton-dickinson-logo.png" alt="Becton Dickinson" loading="lazy" decoding="async" /></div>
      </div>
    </div>
  </section>



  <!-- ============ 10 GLOBAL TECHNOLOGY · LOCAL SUPPORT ============ -->
  <section class="bls-sec bls-partner" id="bls-partner">
    <div class="wrap">
      <div class="bls-head reveal">
        <span class="cmp-eyebrow">GLOBAL TECHNOLOGY · LOCAL SUPPORT</span>
        <h2 class="cmp-h2">장비만큼 중요한 것은,<br>한국에서 누가 지원하느냐입니다.</h2>
      </div>
      <div class="bls-partner-grid">
        <img class="bls-partner-logo reveal" src="../../assets/img/coldjet-logo.png" alt="Cold Jet" />
        <img class="bls-partner-logo reveal" src="../../assets/img/vatek-logo-wordmark.png" alt="VATEK" />

        <div class="bls-partner-name reveal">Cold Jet LLC<span class="bls-partner-tagline">드라이아이스 블라스팅 기술의 개척자이자 글로벌 리더</span></div>
        <div class="bls-partner-name reveal">VATEK Corporation<span class="bls-partner-tagline">Cold Jet 대한민국 공식 총판</span></div>

        <div class="bls-partner-media reveal"><img src="../../assets/img/coldjet-hq-building.jpg" alt="Cold Jet 본사" loading="lazy" decoding="async" /></div>
        <div class="bls-partner-media reveal"><img src="../../assets/img/vatek-building.jpg" alt="바테크 사옥" loading="lazy" decoding="async" /></div>

        <div class="bls-partner-desc reveal"><p>Cold Jet는 현대식 드라이아이스 블라스팅 장비의 원천 특허를 기반으로 기술을 발전시켜 왔으며, 블라스터와 드라이아이스 생산설비, 노즐과 자동화 기술을 개발·공급하고 있습니다.</p></div>
        <div class="bls-partner-desc reveal">
          <p>1988년 설립한 바테크는 Cold Jet의 대한민국 공식 총판으로, 제품 판매뿐 아니라 세척 테스트, 렌탈·데모, 장비 선정, 기술 지원과 A/S 등 국내 고객의 도입과 운용을 지원합니다.</p>
          <p>Cold Jet의 Training, Seminar, Conference 등에 참여하며 관련 기술과 적용사례를 지속적으로 공유하고 있습니다.</p>
        </div>

        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/coldjet-hq-photo-1.jpg" alt="Cold Jet 글로벌 본사" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-2.jpg" alt="Cold Jet 생산 공장" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-3.jpg" alt="Cold Jet 라운지" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-4.jpg" alt="Cold Jet 사내 카페" loading="lazy" decoding="async" />
          <img src="../../assets/img/coldjet-hq-photo-5.jpg" alt="Cold Jet 컨퍼런스" loading="lazy" decoding="async" />
        </div>
        <div class="bls-partner-photos reveal">
          <img src="../../assets/img/vatek-coldjet-photo-1.jpg" alt="Cold Jet 본사 방문" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-2.jpg" alt="Cold Jet Asia Dealer Conference" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-3.jpg" alt="Cold Jet 글로벌 딜러 컨퍼런스" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-4.jpg" alt="Cold Jet 세미나 참석" loading="lazy" decoding="async" />
          <img src="../../assets/img/vatek-coldjet-photo-5.jpg" alt="Cold Jet R&D 신제품 개발" loading="lazy" decoding="async" />
        </div>

        <div class="bls-partner-divider"></div>
        <div class="bls-partner-divider"></div>

        <ul class="bls-facts">
          <li><b>1986</b><small>최초의 드라이아이스 블라스터 제조</small></li>
          <li><b>100+</b><small>글로벌 특허</small></li>
          <li><b>3 · 3</b><small>R&amp;D 연구소 · 생산공장</small></li>
          <li><b>14</b><small>기술센터</small></li>
        </ul>
        <ul class="bls-facts is-vatek">
          <li><b>1988</b><small>설립 · 제조업 기반</small></li>
          <li><b>2014</b><small>기업부설연구소 설립 (하남)</small></li>
          <li><b>TEST</b><small>시편 · 내방 · 방문 테스트</small></li>
          <li><b>A/S</b><small>설치 · 교육 · 기술지원</small></li>
        </ul>
      </div>
      <p class="bls-quote reveal">“Cold Jet의 기술과<br>바테크의 국내 현장 경험을 함께 제공합니다.”</p>
    </div>
  </section>



  <!-- ============ 12 FROM MANUAL TO AUTOMATED ============ -->
  <section class="bls-sec bls-auto" id="bls-auto">
    <div class="wrap">
      <div class="bls-auto-grid">
        <figure class="bls-auto-media reveal"><img src="../../assets/img/coldjet-robot-cell.png" alt="로봇에 통합된 드라이아이스 블라스팅" loading="lazy" decoding="async" /><figcaption>ROBOT-INTEGRATED DRY ICE BLASTING</figcaption></figure>
        <div class="bls-auto-copy">
          <span class="cmp-eyebrow">FROM MANUAL TO AUTOMATED</span>
          <h2 class="cmp-h2">수동 세척에서<br>자동화 공정까지.</h2>
          <div class="cmp-lead">
            <p>동일한 부품을 반복적으로 세척하거나 생산라인에서 일정한 세척 품질과 Cycle을 관리해야 하는 경우, 드라이아이스 블라스터를 로봇 및 자동화설비와 연계할 수 있습니다.</p>
            <p>Cold Jet의 일부 Smart 시스템은 PLC 통신과 자동화 통합을 고려해 설계되어 있으며, 바테크는 실제 생산공정과 세척 조건을 확인한 뒤 자동화 적용 가능성을 함께 검토합니다.</p>
          </div>
          <a class="bls-more" href="../automation.html">드라이아이스 세척 자동화 보기 <i>→</i></a>
        </div>
      </div>
    </div>
  </section>


  <!-- ============ 14 FINAL CTA ============ -->
  <section class="bls-sec bls-final last-freeze" id="bls-final">
    <div class="wrap">
      <div class="bls-final-grid">
        <div>
          <span class="cmp-eyebrow">FIND YOUR BLASTER</span>
          <h2 class="cmp-h2">어떤 장비가 맞는지,<br>실제 세척으로 확인해보세요.</h2>
        </div>
        <div>
          <div class="cmp-lead">
            <p>같은 장비라도 오염물과 작업조건에 따라 세척 결과는 달라질 수 있습니다.</p>
            <p>바테크는 실제 부품과 금형, 설비 또는 샘플을 이용한 테스트를 통해 필요한 세척 조건을 확인하고, 그 조건에 적합한 Cold Jet 블라스터와 노즐을 제안합니다.</p>
          </div>
          <div class="cmp-cta-btns">
            <a class="cta-btn" href="../../rental/demo.html">세척 테스트 신청</a>
            <a class="cmp-btn-ghost" href="../compare-equip.html">장비 상담</a>
          </div>
          <a class="bls-textlink" href="../../rental/index.html">렌탈 · 데모 보기 →</a>
        </div>
      </div>
    </div>
  </section>"""

PELLETIZER_PAGE_TITLE = '드라이아이스 생산 시스템 | 펠렛타이저·슬라이스·자동화'
PELLETIZER_PAGE_DESC = '펠렛타이저부터 슬라이스 제조기, 리포머, 정량 투입·포장·CO2 회수까지 Cold Jet 드라이아이스 생산 시스템과 적용 분야를 살펴보세요.'
PELLETIZER_SCRIPT = """  <script>
  (function () {
    var v = document.getElementById('pltDefinitionVideo'), btn = document.getElementById('pltDefinitionPlayBtn');
    if (v && btn) {
      btn.addEventListener('click', function () { if (v.paused) { v.play(); } else { v.pause(); } });
      v.addEventListener('play', function () {
        btn.classList.add('is-playing');
        btn.querySelector('.bls-play-label').textContent = '일시정지';
        btn.querySelector('.bls-play-icon').textContent = '❙❙';
      });
      v.addEventListener('pause', function () {
        btn.classList.remove('is-playing');
        btn.querySelector('.bls-play-label').textContent = '영상 재생';
        btn.querySelector('.bls-play-icon').textContent = '▶';
      });
    }
  })();
  </script>
  <script>
  (function () {
    var slider = document.getElementById('capacitySelector');
    var capacityNumber = document.getElementById('capacityNumber');
    var form = document.getElementById('productionFinder');
    var dimensionFields = document.getElementById('dimensionFields');
    var dimensionIntro = document.getElementById('dimensionIntro');
    var dimensionHelp = document.getElementById('dimensionHelp');
    var locationField = document.getElementById('locationField');
    var sliceSupplyField = document.getElementById('sliceSupplyField');
    var capacityLimit = document.getElementById('capacityLimit');
    var capacityTicks = document.getElementById('capacityTicks');
    var capacityStep = document.getElementById('capacityStep');
    var dimensionStep = document.getElementById('dimensionStep');
    var dailyDemand = document.getElementById('dailyDemand');
    var dailyHours = document.getElementById('dailyHours');
    var dailyResult = document.getElementById('dailyResult');
    var finderPrev = document.getElementById('finderPrev');
    var finderNextStep = document.getElementById('finderNextStep');
    var finderResult = document.getElementById('finderResult');
    var finderProducts = document.getElementById('finderProducts');
    var finderCurrentStep = document.getElementById('finderCurrentStep');
    var stepThreeLabel = document.getElementById('stepThreeLabel');
    var stepSummaries = [null, document.getElementById('stepSummary1'), document.getElementById('stepSummary2'), document.getElementById('stepSummary3'), document.getElementById('stepSummary4')];
    var progressButtons = Array.prototype.slice.call(document.querySelectorAll('[data-go-step]'));
    var finderSteps = Array.prototype.slice.call(form.querySelectorAll('[data-finder-step]'));
    var currentFinderStep = 1;
    var cards = Array.prototype.slice.call(document.querySelectorAll('.plt-product[data-capacity]'));
    if (!slider || !capacityNumber || !form || !dimensionFields) return;

    var output = {
      type: document.getElementById('finderType'),
      model: document.getElementById('finderModel'),
      reason: document.getElementById('finderReason'),
      config: document.getElementById('finderConfig'),
      next: document.getElementById('finderNext'),
      link: document.getElementById('finderLink'),
      note: document.getElementById('finderNote'),
      tip: document.getElementById('finderNoteTip')
    };
    var pelletModels = [
      { capacity:80, sizes:[3], name:'PE-80', image:'../../assets/img/pelletizer-pe80-official.jpg', link:'pe-80.html' },
      { capacity:120, sizes:[3,10,16], name:'PR120H', image:'../../assets/img/pelletizer-pr120h-official.jpg', link:'pr120h.html' },
      { capacity:350, sizes:[3,6,10,16], name:'PR350H', image:'../../assets/img/pelletizer-pr350h-official.jpg', link:'pr350h.html' },
      { capacity:750, sizes:[3,6,10,16], name:'PR750H', image:'../../assets/img/pelletizer-pr750h-official.jpg', link:'pr750h.html' },
      { capacity:1500, sizes:[3,6,10,16], name:'PR1500H', image:'../../assets/img/pelletizer-pr1500h-official.jpg', link:'pr1500h.html' }
    ];
    var pelletSizes = [1.7,3,6,10,16];
    var sliceFormats = [
      { value:'125 × 125 × 19 mm', models:'500,1000', label:'125 × 125 × 19 mm · R500H / R1000H' },
      { value:'125 × 125 × 25 mm', models:'500,1000,2000', label:'125 × 125 × 25 mm · R500H / R1000H / R2000H' },
      { value:'125 × 125 × 50 mm', models:'500,1000,2000', label:'125 × 125 × 50 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 19 mm', models:'500,1000', label:'127 × 254 × 19 mm · R500H / R1000H' },
      { value:'127 × 254 × 25 mm', models:'500,1000,2000', label:'127 × 254 × 25 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 50 mm', models:'500,1000,2000', label:'127 × 254 × 50 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 60 mm', models:'500,1000,2000', label:'127 × 254 × 60 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 64 mm', models:'500,1000,2000', label:'127 × 254 × 64 mm · R500H / R1000H / R2000H' },
      { value:'127 × 254 × 68 mm', models:'500,1000', label:'127 × 254 × 68 mm · R500H / R1000H' },
      { value:'127 × 254 × 76 mm', models:'2000', label:'127 × 254 × 76 mm · R2000H' },
      { value:'210 × 125 × 19 mm', models:'500,1000', label:'210 × 125 × 19 mm · R500H / R1000H' },
      { value:'210 × 125 × 25 mm', models:'500,1000', label:'210 × 125 × 25 mm · R500H / R1000H' },
      { value:'210 × 125 × 50 mm', models:'500,1000', label:'210 × 125 × 50 mm · R500H / R1000H' },
      { value:'210 × 125 × 60 mm', models:'500,1000', label:'210 × 125 × 60 mm · R500H / R1000H' },
      { value:'210 × 125 × 70 mm', models:'500,1000', label:'210 × 125 × 70 mm · R500H / R1000H' },
      { value:'150 × 150 × 19 mm', models:'500,1000', label:'150 × 150 × 19 mm · R500H / R1000H' },
      { value:'150 × 150 × 25 mm', models:'500,1000', label:'150 × 150 × 25 mm · R500H / R1000H' },
      { value:'150 × 150 × 50 mm', models:'500,1000', label:'150 × 150 × 50 mm · R500H / R1000H' },
      { value:'150 × 150 × 60 mm', models:'500,1000', label:'150 × 150 × 60 mm · R500H / R1000H' },
      { value:'150 × 150 × 70 mm', models:'500,1000', label:'150 × 150 × 70 mm · R500H / R1000H' },
      { value:'150 × 150 × 80 mm', models:'500,1000', label:'150 × 150 × 80 mm · R500H / R1000H' },
      { value:'150 × 150 × 90 mm', models:'500,1000', label:'150 × 150 × 90 mm · R500H / R1000H' },
      { value:'125 × 105 × 19 mm', models:'500,1000', label:'125 × 105 × 19 mm · R500H / R1000H' },
      { value:'125 × 105 × 25 mm', models:'500,1000', label:'125 × 105 × 25 mm · R500H / R1000H' },
      { value:'125 × 105 × 50 mm', models:'500,1000', label:'125 × 105 × 50 mm · R500H / R1000H' },
      { value:'138 × 60 × 19 mm', models:'500,1000', label:'138 × 60 × 19 mm · R500H / R1000H' },
      { value:'138 × 60 × 25 mm', models:'500,1000', label:'138 × 60 × 25 mm · R500H / R1000H' },
      { value:'138 × 60 × 50 mm', models:'500,1000', label:'138 × 60 × 50 mm · R500H / R1000H' },
      { value:'254 × 254 × 25 mm', models:'2000', label:'254 × 254 × 25 mm · R2000H' },
      { value:'254 × 254 × 50 mm', models:'2000', label:'254 × 254 × 50 mm · R2000H' },
      { value:'254 × 254 × 60 mm', models:'2000', label:'254 × 254 × 60 mm · R2000H' },
      { value:'254 × 254 × 64 mm', models:'2000', label:'254 × 254 × 64 mm · R2000H' },
      { value:'254 × 254 × 76 mm', models:'2000', label:'254 × 254 × 76 mm · R2000H' }
    ];
    var sliceFootprints = [
      { value:'125 × 125', inch:'5 × 5 in', className:'is-square' },
      { value:'127 × 254', inch:'5 × 10 in', className:'is-wide' },
      { value:'254 × 254', inch:'10 × 10 in', className:'is-large-square' },
      { value:'210 × 125', inch:'8 × 5 in', className:'is-landscape' },
      { value:'150 × 150', inch:'6 × 6 in', className:'is-square' },
      { value:'125 × 105', inch:'5 × 4 in', className:'is-compact' },
      { value:'138 × 60', inch:'5.4 × 2.4 in', className:'is-slim' }
    ];
    var reformers = [
      { code:'500', capacity:600, name:'R500H' },
      { code:'1000', capacity:1000, name:'R1000H' },
      { code:'2000', capacity:2500, name:'R2000H' }
    ];
    var shapeNames = { pellet:'펠렛·너겟', slice:'슬라이스·블록' };

    function currentShape() {
      return form.querySelector('input[name="iceShape"]:checked').value;
    }
    function currentSliceSupply() {
      return form.querySelector('input[name="sliceSupply"]:checked').value;
    }
    function updateFinderProgress() {
      var shape = currentShape();
      var nextLabels = shape === 'pellet' ? ['','제품 치수','설치 방식','생산량'] : ['','제품 치수','펠렛 공급','생산량'];
      stepThreeLabel.textContent = shape === 'pellet' ? '설치 방법 선택' : '펠렛 공급 방법 선택';
      finderSteps.forEach(function (step) {
        step.classList.toggle('is-active', Number(step.getAttribute('data-finder-step')) === currentFinderStep);
      });
      progressButtons.forEach(function (button) {
        var step = Number(button.getAttribute('data-go-step'));
        button.classList.toggle('is-active', step === currentFinderStep);
        button.classList.toggle('is-complete', step < currentFinderStep);
        button.setAttribute('aria-current', step === currentFinderStep ? 'step' : 'false');
      });
      finderPrev.disabled = currentFinderStep === 1;
      finderCurrentStep.textContent = currentFinderStep;
      if (currentFinderStep < 4) {
        finderNextStep.innerHTML = '다음 <i>→</i>';
      } else {
        finderNextStep.innerHTML = '추천 결과 보기 <i>→</i>';
      }
    }
    function setFinderStep(step) {
      currentFinderStep = Math.max(1, Math.min(4, step));
      if (currentFinderStep < 4) {
        finderResult.hidden = true;
        finderResult.classList.remove('is-visible');
      }
      updateFinderProgress();
    }
    function updateFinderSummaries() {
      var shape = currentShape();
      var shapeInput = form.querySelector('input[name="iceShape"]:checked');
      stepSummaries[1].textContent = shapeInput.nextElementSibling.querySelector('b').textContent;
      stepSummaries[2].textContent = dimensionSummary(shape);
      if (shape === 'pellet') {
        stepSummaries[3].textContent = form.querySelector('input[name="installation"]:checked').value === 'mobile' ? '장소 변경 고려' : '고정 설치';
      } else {
        stepSummaries[3].textContent = currentSliceSupply() === 'produce' ? '펠렛도 함께 생산' : '기존 펠렛 사용';
      }
      stepSummaries[4].textContent = Number(capacityNumber.value || 20).toLocaleString('ko-KR') + ' kg/h';
      updateFinderProgress();
    }
    function renderDimensions() {
      var shape = currentShape();
      locationField.hidden = shape !== 'pellet';
      sliceSupplyField.hidden = shape !== 'slice';
      if (shape === 'pellet') {
        dimensionFields.innerHTML = '<div class="plt-size-choice"><span>펠렛·너겟 직경</span><div>' + pelletSizes.map(function (size) {
          return '<label><input type="radio" name="diameter" value="' + size + '"' + (size === 3 ? ' checked' : '') + '><b>' + size + '</b><i>mm</i></label>';
        }).join('') + '</div></div>';
        dimensionIntro.textContent = '펠렛타이저가 압출·절단해 만드는 낱개 펠렛·너겟의 지름을 선택합니다. 이 규격과 필요한 생산량에 맞는 장비를 검토합니다.';
        dimensionHelp.textContent = '펠렛과 너겟은 길이를 지정하지 않으며, 직경 규격과 필요한 생산량으로 장비를 검토합니다.';
        dimensionStep.textContent = '02';
      } else {
        dimensionFields.innerHTML = '<div class="plt-slice-builder"><span class="plt-field-label">가로 × 세로</span><div class="plt-footprint-options">' + sliceFootprints.map(function (footprint, index) {
          return '<label><input type="radio" name="sliceFootprint" value="' + footprint.value + '"' + (index === 0 ? ' checked' : '') + '><span><i class="' + footprint.className + '" aria-hidden="true"></i><b>' + footprint.value + '</b><small>mm · ' + footprint.inch + '</small></span></label>';
        }).join('') + '</div><span class="plt-field-label plt-thickness-label">두께</span><div class="plt-thickness-options" id="thicknessOptions"></div></div>';
        renderSliceThickness();
        dimensionIntro.textContent = '이 규격은 완성된 슬라이스·블록의 크기입니다. 리포머(R Series)가 드라이아이스 펠렛을 압축해 선택한 가로×세로×두께로 성형합니다.';
        dimensionHelp.textContent = '첨부된 R Series 규격표를 기준으로 선택합니다. R Series는 펠렛을 슬라이스·블록으로 재성형하는 리포머입니다.';
        dimensionStep.textContent = '02';
      }
      Array.prototype.forEach.call(dimensionFields.querySelectorAll('input[name="diameter"]'), function (input) {
        input.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); updateVisual(); });
      });
      Array.prototype.forEach.call(dimensionFields.querySelectorAll('input[name="sliceFootprint"]'), function (input) {
        input.addEventListener('change', function () { renderSliceThickness(); updateCapacityLimit(); updateRecommendation(); updateVisual(); });
      });
      capacityStep.textContent = '04';
      updateFinderProgress();
      updateVisual();
    }
    function renderSliceThickness() {
      var container = dimensionFields.querySelector('#thicknessOptions');
      var selectedFootprint = dimensionFields.querySelector('input[name="sliceFootprint"]:checked');
      if (!container || !selectedFootprint) return;
      var formats = sliceFormats.filter(function (format) { return format.value.indexOf(selectedFootprint.value + ' × ') === 0; });
      container.innerHTML = formats.map(function (format, index) {
        var thickness = format.value.replace(selectedFootprint.value + ' × ', '').replace(' mm', '');
        var modelNames = format.models.split(',').map(function (code) { return 'R' + code + 'H'; }).join(' · ');
        return '<label><input type="radio" name="sliceThickness" value="' + format.value + '" data-models="' + format.models + '"' + (index === 0 ? ' checked' : '') + '><span><b>' + thickness + ' mm</b><small>' + modelNames + '</small></span></label>';
      }).join('');
      Array.prototype.forEach.call(container.querySelectorAll('input'), function (input) {
        input.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); updateVisual(); });
      });
      updateVisual();
    }
    function dimensionSummary(shape) {
      if (shape === 'pellet') return 'Ø ' + dimensionFields.querySelector('input[name="diameter"]:checked').value + ' mm';
      return dimensionFields.querySelector('input[name="sliceThickness"]:checked').value;
    }
    function nums(str) { return (String(str).match(/[\d.]+/g) || []).map(Number); }
    function isoFacePoints(pts) { return pts.map(function (p) { return p.x.toFixed(1) + ',' + p.y.toFixed(1); }).join(' '); }
    function isoBoxSvg(w, d, h) {
      var ux = 0.866, uy = 0.5, vx = -0.866, vy = 0.5;
      var scaleH = 188 / ((w + d) * ux);
      var scaleV = 168 / ((w + d) * uy + h);
      var scale = Math.min(scaleH, scaleV, 1.35);
      var W = w * scale, D = d * scale, H = Math.max(h * scale, 5);
      var cx = 110 - (W * ux - D * ux) / 2;
      var cy = 96 - (W * uy + D * uy + H) / 2;
      var top = { x: cx, y: cy };
      var right = { x: cx + W * ux, y: cy + W * uy };
      var left = { x: cx + D * vx, y: cy + D * vy };
      var front = { x: cx + W * ux + D * vx, y: cy + W * uy + D * vy };
      var rightB = { x: right.x, y: right.y + H };
      var leftB = { x: left.x, y: left.y + H };
      var frontB = { x: front.x, y: front.y + H };
      var fill = 'fill="#ffffff" stroke="none"';
      var edges = [[top, right], [top, left], [right, front], [left, front], [right, rightB], [left, leftB], [front, frontB], [rightB, frontB], [leftB, frontB]];
      var d1 = edges.map(function (e) { return 'M' + e[0].x.toFixed(1) + ',' + e[0].y.toFixed(1) + ' L' + e[1].x.toFixed(1) + ',' + e[1].y.toFixed(1); }).join(' ');
      return '<polygon points="' + isoFacePoints([right, front, frontB, rightB]) + '" ' + fill + '></polygon>' +
        '<polygon points="' + isoFacePoints([left, front, frontB, leftB]) + '" ' + fill + '></polygon>' +
        '<polygon points="' + isoFacePoints([top, right, front, left]) + '" ' + fill + '></polygon>' +
        '<path d="' + d1 + '" fill="none" stroke="#283739" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"></path>';
    }
    function isoCylinderSvg(diameter) {
      var rx = 4 + (diameter / 16) * 20;
      var ry = rx * 0.5;
      var height = rx * 3.4;
      var cx = 110, topY = 96 - (height + ry * 2) / 2 + ry;
      var fill = 'fill="#ffffff" stroke="none"';
      return '<rect x="' + (cx - rx) + '" y="' + topY + '" width="' + (rx * 2) + '" height="' + height + '" ' + fill + '></rect>' +
        '<ellipse cx="' + cx + '" cy="' + (topY + height) + '" rx="' + rx + '" ry="' + ry + '" ' + fill + '></ellipse>' +
        '<ellipse cx="' + cx + '" cy="' + topY + '" rx="' + rx + '" ry="' + ry + '" ' + fill + '></ellipse>' +
        '<path d="M ' + (cx - rx) + ' ' + topY + ' L ' + (cx - rx) + ' ' + (topY + height) + ' A ' + rx + ' ' + ry + ' 0 0 0 ' + (cx + rx) + ' ' + (topY + height) + ' L ' + (cx + rx) + ' ' + topY + '" fill="none" stroke="#283739" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"></path>' +
        '<ellipse cx="' + cx + '" cy="' + topY + '" rx="' + rx + '" ry="' + ry + '" fill="none" stroke="#283739" stroke-width="1.6"></ellipse>';
    }
    function updateVisual() {
      var svg = document.getElementById('finderVisualSvg');
      var caption = document.getElementById('finderVisualCaption');
      if (!svg || !caption) return;
      var shape = currentShape();
      if (shape === 'pellet') {
        var diameterInput = dimensionFields.querySelector('input[name="diameter"]:checked');
        if (!diameterInput) return;
        var d = Number(diameterInput.value);
        svg.innerHTML = isoCylinderSvg(d);
        caption.textContent = 'Ø ' + d + ' mm';
      } else {
        var footprintInput = dimensionFields.querySelector('input[name="sliceFootprint"]:checked');
        var thicknessInput = dimensionFields.querySelector('input[name="sliceThickness"]:checked');
        if (!footprintInput || !thicknessInput) return;
        var fp = nums(footprintInput.value);
        var th = nums(thicknessInput.value);
        var w = fp[0], dep = fp[1], h = th[2];
        svg.innerHTML = isoBoxSvg(w, dep, h);
        caption.textContent = w + ' × ' + dep + ' × ' + h + ' mm';
      }
    }
    function setResult(result) {
      var products = result.products || [{ name:result.name, image:result.image, role:result.productRole || '추천 장비', processImage:result.processImage }];
      finderProducts.innerHTML = products.map(function (product, index) {
        return '<article><div><img src="' + product.image + '" alt="' + product.name + '" class="' + (product.processImage ? 'is-process' : '') + '"></div><span>' + String(index + 1).padStart(2,'0') + ' / ' + product.role + '</span><strong>' + product.name + '</strong></article>';
      }).join('');
      output.type.textContent = result.type;
      output.model.textContent = result.name;
      output.reason.textContent = result.reason;
      output.config.textContent = result.config;
      output.next.textContent = result.next;
      output.link.href = result.link;
      output.link.firstChild.nodeValue = result.linkText + ' ';
      output.note.textContent = result.note || '이 결과는 1차 장비 선정을 위한 안내입니다. 실제 공급 조건과 자동화 범위에 따라 최종 구성이 달라질 수 있습니다.';
      output.tip.textContent = result.tip || '';
      output.tip.style.display = result.tip ? 'block' : 'none';
    }
    function capacityTip(list, need, matched) {
      if (!matched) return null;
      var sorted = list.slice().sort(function (a, b) { return a.capacity - b.capacity; });
      var idx = sorted.findIndex(function (item) { return item.capacity === matched.capacity; });
      var prev = idx > 0 ? sorted[idx - 1] : null;
      var prevCap = prev ? prev.capacity : 0;
      var range = matched.capacity - prevCap;
      if (prev && range > 0 && (need - prevCap) <= range * 0.4) {
        return { type:'down', text:'선택하신 ' + need.toLocaleString('ko-KR') + ' kg/h를 ' + prevCap.toLocaleString('ko-KR') + ' kg/h로 조금만 낮추면 ' + prev.name + ' 모델로도 충분해 투자비를 줄일 수 있습니다.' };
      }
      if (matched.capacity > need) {
        return { type:'up', text:'이번 조건에 추천된 ' + matched.name + '는 최대 ' + matched.capacity.toLocaleString('ko-KR') + ' kg/h까지 생산할 수 있는 모델입니다. 해당 생산량까지는 추가 모델 변경 없이 대응할 수 있습니다.' };
      }
      return null;
    }
    function updateCapacityLimit() {
      var shape = currentShape();
      var max = 1500;
      var description = '고정형 펠렛타이저 기준';
      if (shape === 'pellet') {
        var diameter = Number(dimensionFields.querySelector('input[name="diameter"]:checked').value);
        var mobile = form.querySelector('input[name="installation"]:checked').value === 'mobile';
        if (mobile) {
          max = 350;
          description = 'Production Hub · PR120H 또는 PR350H 기준';
        } else if (diameter === 1.7) {
          max = 1500;
          description = '1.7 mm · 표준 모델 별도 검토';
        }
      } else {
        var selected = dimensionFields.querySelector('input[name="sliceThickness"]:checked');
        var codes = selected.getAttribute('data-models').split(',');
        max = codes.indexOf('2000') !== -1 ? 2500 : (codes.indexOf('1000') !== -1 ? 1000 : 600);
        var supplyDescription = currentSliceSupply() === 'produce' ? ' · 펠렛타이저 함께 구성' : ' · 기존 펠렛 공급';
        description = (codes.indexOf('2000') !== -1 ? '선택 규격의 R2000H 포함 기준' : '선택 규격의 R500H·R1000H 기준') + supplyDescription;
      }
      slider.max = max;
      capacityNumber.max = max;
      var current = Number(capacityNumber.value) || 20;
      if (current > max) current = max;
      if (current < 20) current = 20;
      slider.value = current;
      capacityNumber.value = current;
      capacityLimit.innerHTML = '<b>현재 조건에서 선택 가능</b><span>최대 ' + max.toLocaleString('ko-KR') + ' kg/h · ' + description + '</span>';
      var tickValues = [20, .25, .5, .75, 1].map(function (value, index) {
        if (index === 0) return 20;
        if (index === 4) return max;
        return Math.round((20 + (max - 20) * value) / 10) * 10;
      });
      capacityTicks.innerHTML = tickValues.map(function (value, index) {
        return '<span>' + value.toLocaleString('ko-KR') + (index === 4 ? ' kg/h' : '') + '</span>';
      }).join('');
    }
    function updateRecommendation() {
      var allowedMax = Number(slider.max);
      var need = Math.max(20, Math.min(allowedMax, Number(capacityNumber.value) || 20));
      var shape = currentShape();
      var size = dimensionSummary(shape);
      var result;

      if (shape === 'pellet') {
        var diameter = Number(dimensionFields.querySelector('input[name="diameter"]:checked').value);
        var mobile = form.querySelector('input[name="installation"]:checked').value === 'mobile';
        var candidates = mobile ? pelletModels.filter(function (item) { return item.name === 'PR120H' || item.name === 'PR350H'; }) : pelletModels;
        var machine = candidates.find(function (item) { return item.capacity >= need && item.sizes.indexOf(diameter) !== -1; });
        if (mobile && machine) {
          result = { name:'Production Hub + ' + machine.name, image:'../../assets/img/pelletizer-hub-official.png', link:'../quote.html', linkText:'Production Hub 상담', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'설치 장소 변경을 고려해 ' + machine.name + '를 탑재한 독립형 Production Hub 구성을 추천합니다.', config:size + ' · ' + machine.name + ' 탑재', next:'이동·설치 인프라 확인' };
        } else if (mobile && !machine) {
          result = { name:'Production Hub 맞춤 검토', image:'../../assets/img/pelletizer-hub-official.png', link:'../quote.html', linkText:'Production Hub 상담', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'Production Hub는 PR120H 또는 PR350H 구성만 가능하므로 선택한 직경과 생산량에 대한 별도 검토가 필요합니다.', config:size + ' · Hub 적용성 검토', next:'생산량·설치 장소 확인' };
        } else if (!machine) {
          result = { name:'맞춤 펠렛 생산 시스템', image:'../../assets/img/pelletizer-pr1500h-official.jpg', link:'../quote.html', linkText:'시스템 구성 상담', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'선택한 직경과 생산량을 동시에 충족하는 단일 표준 모델이 없어 다이와 병렬 구성을 함께 검토해야 합니다.', config:size + ' · 다이 및 생산량 검토', next:'일일 운전 시간 확인' };
        } else {
          result = { name:machine.name, image:machine.image, link:machine.link, linkText:'추천 모델 상세 보기', type:shapeNames[shape] + ' 생산 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'입력한 생산량을 충족하는 가장 가까운 펠렛타이저입니다.', config:size + ' · 전용 다이 검토', next:'LCO₂ 공급 조건 확인', tip:(capacityTip(candidates, need, machine) || {}).text };
        }
      } else {
        var formatOption = dimensionFields.querySelector('input[name="sliceThickness"]:checked');
        var supportedModels = formatOption.getAttribute('data-models').split(',');
        var reformer = reformers.find(function (item) { return item.capacity >= need && supportedModels.indexOf(item.code) !== -1; });
        var makePellets = currentSliceSupply() === 'produce';
        var pelletizer = pelletModels.find(function (item) { return item.capacity >= need; });
        if (reformer) {
          if (makePellets && pelletizer) {
            var pelletizerTip = capacityTip(pelletModels, need, pelletizer);
            var reformerCandidates = reformers.filter(function (item) { return supportedModels.indexOf(item.code) !== -1; });
            var reformerTip = capacityTip(reformerCandidates, need, reformer);
            var combinedTip = (pelletizerTip && pelletizerTip.type === 'down') ? pelletizerTip.text : (reformerTip && reformerTip.type === 'down') ? reformerTip.text : (pelletizerTip ? pelletizerTip.text : (reformerTip ? reformerTip.text : ''));
            result = { name:pelletizer.name + ' + ' + reformer.name, image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, products:[{name:pelletizer.name,image:pelletizer.image,role:'펠렛 생산'},{name:reformer.name,image:'../../assets/img/pelletizer-rseries-official.jpg',role:'슬라이스 재성형',processImage:true}], link:'../quote.html', linkText:'통합 생산 시스템 상담', type:shapeNames[shape] + ' 생산·리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'펠렛 생산부터 슬라이스·블록 재성형까지 이어지도록 ' + pelletizer.name + ' 펠렛타이저와 ' + reformer.name + ' 리포머를 함께 구성합니다.', config:size + ' · ' + pelletizer.name + ' → ' + reformer.name, next:'펠렛 이송·버퍼 구성 확인', note:'R Series 자체는 드라이아이스를 생산하지 않는 리포머입니다. 이 추천은 필요한 펠렛을 현장에서 생산하는 펠렛타이저를 함께 포함한 1차 구성입니다.', tip:combinedTip };
          } else if (makePellets && !pelletizer) {
            result = { name:'펠렛타이저 맞춤 구성 + ' + reformer.name, image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, products:[{name:'펠렛타이저 맞춤 구성',image:'../../assets/img/pelletizer-pr1500h-official.jpg',role:'펠렛 생산'},{name:reformer.name,image:'../../assets/img/pelletizer-rseries-official.jpg',role:'슬라이스 재성형',processImage:true}], link:'../quote.html', linkText:'통합 생산 시스템 상담', type:shapeNames[shape] + ' 생산·리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'리포머 처리량에 맞는 펠렛을 함께 생산하려면 복수 펠렛타이저 또는 생산라인 맞춤 구성이 필요합니다.', config:size + ' · 펠렛 생산 병렬 구성 → ' + reformer.name, next:'펠렛타이저 대수·버퍼 용량 확인', note:'R Series 자체는 드라이아이스를 생산하지 않습니다. 시간당 1,500 kg을 초과하는 펠렛 생산은 단일 표준 펠렛타이저 범위를 넘어 병렬 구성과 연속 운전 조건을 함께 검토해야 합니다.' };
          } else {
            result = { name:reformer.name, image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, link:'special-forms.html', linkText:'R Series 상세 보기', type:shapeNames[shape] + ' 리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'기존에 공급되는 펠렛을 선택한 규격으로 재성형하며 필요한 처리량을 충족하는 가장 가까운 R Series 리포머입니다.', config:size + ' · 기존 펠렛 공급 → ' + reformer.name, next:'원료 펠렛 공급량·이송 확인', note:'R Series는 펠렛을 슬라이스·블록으로 재성형하는 리포머입니다. 이 구성은 필요한 양의 펠렛이 기존 제조기 또는 외부 공급을 통해 확보된다는 조건입니다.', tip:(capacityTip(reformers.filter(function (item) { return supportedModels.indexOf(item.code) !== -1; }), need, reformer) || {}).text };
          }
        } else {
          result = { name:'R Series 맞춤 검토', image:'../../assets/img/pelletizer-rseries-official.jpg', processImage:true, link:'../quote.html', linkText:'리포머 구성 상담', type:shapeNames[shape] + ' 리폼 · ' + need.toLocaleString('ko-KR') + ' kg/h', reason:'선택한 규격과 처리량을 동시에 충족하는 표준 R Series 구성이 없어 규격 또는 병렬 운전을 검토해야 합니다.', config:size + (makePellets ? ' · 펠렛타이저 함께 검토' : ' · 기존 펠렛 공급 조건'), next:'규격·처리량 재검토', note:'R Series는 리포머입니다. 펠렛도 함께 생산하는 경우에는 필요한 처리량에 맞는 드라이아이스 제조기 구성까지 함께 검토해야 합니다.' };
        }
      }

      cards.forEach(function (card) { card.classList.remove('is-recommended'); });
      if (shape === 'pellet') {
        var matchingCard = cards.find(function (card) { return card.querySelector('h3').textContent === result.name; });
        if (matchingCard) matchingCard.classList.add('is-recommended');
      }
      setResult(result);
      slider.setAttribute('aria-valuetext', '시간당 ' + need.toLocaleString('ko-KR') + '킬로그램, 추천 ' + result.name);
      updateFinderSummaries();
    }
    function updateFromDailyDemand() {
      var demand = Math.max(1, Number(dailyDemand.value) || 1);
      var hours = Math.max(1, Math.min(24, Number(dailyHours.value) || 1));
      var calculated = Math.ceil(demand / hours);
      var applied = Math.max(20, Math.min(Number(slider.max), calculated));
      dailyResult.innerHTML = '<small>필요 시간당 생산량</small><b>' + calculated.toLocaleString('ko-KR') + ' kg/h</b>' + (calculated > Number(slider.max) ? '<em>현재 조건의 최대 범위를 초과합니다.</em>' : '');
      slider.value = applied;
      capacityNumber.value = applied;
      updateRecommendation();
    }

    slider.addEventListener('input', function () {
      capacityNumber.value = slider.value;
      updateRecommendation();
    });
    capacityNumber.addEventListener('input', function () {
      var raw = Number(capacityNumber.value);
      if (!isNaN(raw) && capacityNumber.value !== '') {
        slider.value = Math.max(20, Math.min(Number(slider.max), raw));
      }
      updateRecommendation();
    });
    capacityNumber.addEventListener('blur', function () {
      var clamped = Math.max(20, Math.min(Number(slider.max), Number(capacityNumber.value) || 20));
      capacityNumber.value = clamped;
      slider.value = clamped;
      updateRecommendation();
    });
    Array.prototype.forEach.call(form.querySelectorAll('input[name="iceShape"]'), function (radio) {
      radio.addEventListener('change', function () { renderDimensions(); updateCapacityLimit(); updateRecommendation(); });
    });
    Array.prototype.forEach.call(form.querySelectorAll('input[name="installation"]'), function (radio) {
      radio.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); });
    });
    Array.prototype.forEach.call(form.querySelectorAll('input[name="sliceSupply"]'), function (radio) {
      radio.addEventListener('change', function () { updateCapacityLimit(); updateRecommendation(); });
    });
    progressButtons.forEach(function (button) {
      button.addEventListener('click', function () { setFinderStep(Number(button.getAttribute('data-go-step'))); });
    });
    finderPrev.addEventListener('click', function () { setFinderStep(currentFinderStep - 1); });
    finderNextStep.addEventListener('click', function () {
      if (currentFinderStep < 4) {
        setFinderStep(currentFinderStep + 1);
      } else {
        finderResult.hidden = false;
        finderResult.classList.remove('is-visible');
        void finderResult.offsetWidth;
        finderResult.classList.add('is-visible');
        output.model.setAttribute('tabindex', '-1');
        output.model.focus({ preventScroll:true });
        finderResult.scrollIntoView({ behavior:'smooth', block:'start' });
      }
    });
    dailyDemand.addEventListener('input', updateFromDailyDemand);
    dailyHours.addEventListener('input', updateFromDailyDemand);
    renderDimensions();
    updateCapacityLimit();
    updateRecommendation();
    setFinderStep(1);
  })();
  </script>
"""
PELLETIZER_HUB_BODY = """
  <main class="plt-page">
    <section class="subhero-parallax pel-hero-stage">
      <video class="subhero-parallax-img pel-hero-video" autoplay muted loop playsinline preload="auto" data-buffer="60" data-pan-scale="1.06" data-blur-start="0.5">
        <source src="../../assets/video/pelletizer-hero.mp4" type="video/mp4" />
      </video>
      <div class="subhero-breadcrumb wrap"><a href="../../index.html">홈</a> &gt; <a href="../index.html">제품 · 자동화 · 공급</a> &gt; 드라이아이스 제조기</div>
      <div class="subhero-textbox">
        <span class="ind-hero-eyebrow">COLD JET × VATEK / DRY ICE PRODUCTION</span>
        <h1>필요한 형태로,<br><span class="bls-hero-accent">생산부터 공급까지.</span></h1>
        <p class="bls-hero-main">액체 CO<sub>2</sub>를 펠렛과 너겟으로 생산하고, 필요한 규격의 슬라이스와 블록으로 재성형합니다. 정량 투입과 포장, 회수 설비까지 사용 목적과 생산량에 맞춰 연결합니다.</p>
        
      </div>
      <div class="pel-hero-mask" aria-hidden="true">
        <img src="../../assets/img/coldjet-logo.png" alt="" />
        <span>×</span>
        <img src="../../assets/img/vatek-logo-wordmark.png" alt="" />
      </div>
    </section>

    <section class="plt-definition pel-cover tint-hatch" id="what-is-pelletizer">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">WHAT IS A PELLETIZER?</span><h2 class="plt-title">펠렛타이저는<br>드라이아이스 펠렛을 만드는 장비입니다.</h2></div>
          <p class="plt-lead">LCO<sub>2</sub>(액화이산화탄소) 탱크에서 공급된 <strong>액체 CO<sub>2</sub></strong>를 이용해 드라이아이스 펠렛 또는 너겟을 생산합니다.</p>
        </div>
        <div class="bls-showcase-frame reveal">
        <div class="bls-showcase">
          <div class="bls-showcase-media">
            <video id="pltDefinitionVideo" class="bls-media-fade" muted loop playsinline preload="metadata" poster="../../assets/img/pelletizer-nozzle-snow.jpg">
              <source src="../../assets/video/pelletizer-definition.mp4" type="video/mp4" />
            </video>
            <span class="bls-showcase-cap">COLD JET&nbsp;&nbsp;/&nbsp;&nbsp;PELLETIZER</span>
            <button type="button" class="bls-play-btn" id="pltDefinitionPlayBtn" aria-label="영상 재생">
              <span class="bls-play-label">영상 재생</span><i class="bls-play-icon">▶</i>
            </button>
          </div>
          <div class="bls-showcase-body">
            <span class="bls-dot-eyebrow">DRY ICE PRODUCTION MACHINES</span>
            <h3>액체 CO<sub>2</sub>에서 시작해,<br>드라이아이스로 완성되는 기술.</h3>
            <p>압축과 팽창의 원리로 균일한 품질의 드라이아이스를 만들어내는 Cold Jet의 첨단 생산 기술은 전 세계 현장에서 검증되었습니다. 고객의 시간과 비용을 절감하는 것이 그 시작입니다.</p>
          </div>
        </div>
        </div>
      </div>
    </section>

    <section class="plt-section plt-ecosystem" id="production-system">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">ONE PRODUCTION ECOSYSTEM</span><h2 class="plt-title">만드는 장비를 넘어,<br>공급 공정 전체를 봅니다.</h2></div>
          <p class="plt-lead">드라이아이스의 형태와 사용 시점이 달라지면 필요한 설비도 달라집니다. Cold Jet는 펠렛 생산부터 슬라이스 성형, 계량, 포장, 원격 생산과 CO<sub>2</sub> 회수까지 하나의 생산 흐름으로 구성합니다.</p>
        </div>
        <div class="plt-system-map" aria-label="Cold Jet 드라이아이스 생산 시스템 구성">
          <article class="plt-system-card is-wide">
            <div class="plt-system-media"><img src="../../assets/img/pelletizer-pr350h-official.jpg" alt="Cold Jet 펠렛타이저" loading="lazy" /></div>
            <div class="plt-system-copy"><span>01 / MAKE PELLETS</span><h3>펠렛타이저</h3><p>액체 CO<sub>2</sub>로 3 mm 블라스팅 펠렛부터 냉각용 너겟까지 생산합니다. 자체 사용부터 상업 생산까지 용량별 모델을 선택할 수 있습니다.</p><a href="#pelletizer-lineup">모델 비교하기 →</a></div>
          </article>
          <article class="plt-system-card">
            <div class="plt-system-media"><img src="../../assets/img/pelletizer-r500h-official.jpg" alt="Cold Jet R Series 드라이아이스 슬라이스 리포머" loading="lazy" /></div>
            <div class="plt-system-copy"><span>02 / REFORM SLICES</span><h3>R Series 리포머</h3><p>별도의 펠렛타이저에서 생산한 펠렛을 밀도 높은 슬라이스와 블록으로 재성형합니다. R500H·R1000H·R2000H로 처리량과 규격에 맞춰 구성합니다.</p><b>600 / 1,000 / 2,500 kg/h 처리</b></div>
          </article>
          <article class="plt-system-card plt-system-process">
            <div class="plt-system-copy"><span>03 / DOSE &amp; PACK</span><h3>정량 투입 · 자동 포장</h3><p>설정한 양의 펠렛·너겟을 배송 상자나 벌크 용기에 직접 투입하고 개별 포장까지 자동화해 반복 작업과 작업자의 접촉을 줄입니다.</p></div>
            <div class="plt-process-pair"><img src="../../assets/img/pelletizer-dosing-official.jpg" alt="Cold Jet 정량 투입 시스템" loading="lazy" /><img src="../../assets/img/pelletizer-bagging-official.jpg" alt="Cold Jet 자동 포장 시스템" loading="lazy" /></div>
          </article>
          <article class="plt-system-card">
            <div class="plt-system-media"><img src="../../assets/img/pelletizer-hub-official.png" alt="Cold Jet 원격 드라이아이스 생산 허브" loading="lazy" /></div>
            <div class="plt-system-copy"><span>04 / REMOTE PRODUCTION</span><h3>Production Hub</h3><p>PR120H 또는 PR350H를 독립형 모듈에 구성해 설치 장소 변경이 예상되거나 원거리·임시 현장에서 펠렛과 너겟을 생산합니다.</p></div>
          </article>
          <article class="plt-system-card plt-system-recovery">
            <div class="plt-system-copy"><span>05 / RECOVER CO<sub>2</sub></span><h3>RE-CO<sub>2</sub> 회수 시스템</h3><p>생산 중 발생하는 CO<sub>2</sub> 리버트 가스를 회수·액화해 다시 드라이아이스 생산에 활용합니다. 대규모 생산에서 원료 사용과 전환 효율을 함께 검토할 수 있습니다.</p><a href="../recovery/index.html">CO<sub>2</sub> 회수 시스템 보기 →</a></div>
          </article>
        </div>
      </div>
    </section>

    <section class="plt-section plt-applications" id="applications">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">WHERE DRY ICE WORKS</span><h2 class="plt-title">생산 목적이 달라지면,<br>적합한 형태도 달라집니다.</h2></div>
          <p class="plt-lead">먼저 “어디에 사용할 것인가”를 정하면 펠렛 크기, 슬라이스 중량, 시간당 생산량과 자동화 범위를 더 정확하게 결정할 수 있습니다.</p>
        </div>
        <div class="plt-use-grid">
          <article><span>01</span><h3>드라이아이스 세척</h3><p>3 mm 펠렛을 현장에서 생산해 블라스터에 안정적으로 공급합니다.</p><b>펠렛타이저</b></article>
          <article><span>02</span><h3>식품 공정 냉각</h3><p>혼합·분쇄·포장 공정에서 제품 온도를 빠르게 낮추거나 유지합니다.</p><b>펠렛 · 너겟 / 정량 투입</b></article>
          <article><span>03</span><h3>식품 배송 · 콜드체인</h3><p>육류, 수산물, 밀키트와 냉동식품의 운송 조건에 맞춰 투입량을 관리합니다.</p><b>슬라이스 / 자동 포장</b></article>
          <article><span>04</span><h3>항공 케이터링</h3><p>기내식과 온도 민감 식품의 이동·보관에 맞는 슬라이스를 생산합니다.</p><b>R Series 리포머</b></article>
          <article><span>05</span><h3>바이오 · 생명과학</h3><p>검체와 의약품 등 온도 관리가 필요한 물류의 냉매 공급을 지원합니다.</p><b>슬라이스 / 정량 투입</b></article>
          <article><span>06</span><h3>드라이아이스 생산 · 판매</h3><p>다양한 규격의 펠렛과 슬라이스를 대량 생산하고 포장해 유통합니다.</p><b>고용량 라인 / 리포머</b></article>
        </div>
      </div>
    </section>

    <section class="plt-section plt-reasons">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">WHY PRODUCE ON DEMAND?</span><h2 class="plt-title">공급받는 드라이아이스에서,<br>직접 생산하는 시스템으로.</h2></div>
          <p class="plt-lead">드라이아이스는 보관하는 동안 승화합니다. 필요한 곳에서 필요한 만큼 생산하면 신선도와 공급 일정, 사용 형태를 직접 관리할 수 있습니다.</p>
        </div>
        <div class="plt-reason-grid">
          <article class="plt-reason"><span class="num">01</span><h3>필요할 때 바로 생산</h3><p>납기나 외부 공급 일정에 맞추기보다 작업과 출하 계획에 맞춰 생산합니다.</p></article>
          <article class="plt-reason"><span class="num">02</span><h3>신선한 고밀도 드라이아이스</h3><p>생산 직후 사용해 보관 중 발생하는 승화와 품질 저하 부담을 줄입니다.</p></article>
          <article class="plt-reason"><span class="num">03</span><h3>용도에 맞는 크기</h3><p>블라스팅, 냉각, 운송 등 사용 목적에 따라 펠렛과 너겟 크기를 선택합니다.</p></article>
          <article class="plt-reason"><span class="num">04</span><h3>생산량의 확장</h3><p>소규모 자체 사용부터 대형 생산·판매 설비까지 수요에 맞춰 구성할 수 있습니다.</p></article>
        </div>
      </div>
    </section>

    <section class="plt-section plt-lineup" id="pelletizer-lineup">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">DRY ICE PRODUCTION LINEUP</span><h2 class="plt-title">생산 규모에 맞춘<br>Cold Jet 라인업.</h2></div>
          <p class="plt-lead">소규모 현장 생산부터 대형 상업 생산, 슬라이스 성형까지 제품군을 먼저 살펴보세요. 각 제품을 선택하면 주요 특징과 상세 사양을 확인할 수 있습니다.</p>
        </div>
        <div class="plt-lineup-grid">
          <a class="plt-product" data-capacity="80" href="pe-80.html">
            <span class="plt-recommend">추천 모델</span>
            <div class="plt-product-media"><img src="../../assets/img/pelletizer-pe80-official.jpg" alt="Cold Jet PE-80 드라이아이스 제조기" loading="lazy" /></div>
            <div class="plt-product-body"><span class="plt-product-tag">LOW VOLUME</span><h3>PE-80</h3><p class="plt-product-desc">3 mm 블라스팅 펠렛 생산을 위한 저용량 드라이아이스 펠렛타이저.</p><dl class="plt-product-spec"><div><dt>생산능력</dt><dd>최대 80 kg/h</dd></div><div><dt>펠렛 크기</dt><dd>3 mm 전용</dd></div><div><dt>적합 용도</dt><dd>자체 사용 · 블라스팅</dd></div></dl><span class="plt-product-more">제품 상세 보기 <i>→</i></span></div>
          </a>
          <a class="plt-product" data-capacity="120" href="pr120h.html">
            <span class="plt-recommend">추천 모델</span>
            <div class="plt-product-media"><img src="../../assets/img/pelletizer-pr120h-official.jpg" alt="Cold Jet PR120H 드라이아이스 제조기" loading="lazy" /></div>
            <div class="plt-product-body"><span class="plt-product-tag">HIGH VOLUME</span><h3>PR120H</h3><p class="plt-product-desc">컴팩트한 크기와 빠른 기동을 갖춘 자동화 펠렛타이저.</p><dl class="plt-product-spec"><div><dt>생산능력</dt><dd>최대 120 kg/h</dd></div><div><dt>펠렛 크기</dt><dd>3 / 10 / 16 mm</dd></div><div><dt>기동 시간</dt><dd>5분 이내</dd></div></dl><span class="plt-product-more">제품 상세 보기 <i>→</i></span></div>
          </a>
          <a class="plt-product is-recommended" data-capacity="350" href="pr350h.html">
            <span class="plt-recommend">추천 모델</span>
            <div class="plt-product-media"><img src="../../assets/img/pelletizer-pr350h-official.jpg" alt="Cold Jet PR350H 드라이아이스 제조기" loading="lazy" /></div>
            <div class="plt-product-body"><span class="plt-product-tag">HIGH VOLUME</span><h3>PR350H</h3><p class="plt-product-desc">자동 다이 교체와 폐쇄형 챔버를 갖춘 중용량 생산 모델.</p><dl class="plt-product-spec"><div><dt>생산능력</dt><dd>최대 350 kg/h</dd></div><div><dt>펠렛 크기</dt><dd>3 / 6 / 10 / 16 mm</dd></div><div><dt>기동 시간</dt><dd>3분 미만</dd></div></dl><span class="plt-product-more">제품 상세 보기 <i>→</i></span></div>
          </a>
          <a class="plt-product" data-capacity="750" href="pr750h.html">
            <span class="plt-recommend">추천 모델</span>
            <div class="plt-product-media"><img src="../../assets/img/pelletizer-pr750h-official.jpg" alt="Cold Jet PR750H 드라이아이스 제조기" loading="lazy" /></div>
            <div class="plt-product-body"><span class="plt-product-tag">INDUSTRIAL</span><h3>PR750H</h3><p class="plt-product-desc">지속적인 대용량 생산과 생산라인 통합을 위한 산업용 모델.</p><dl class="plt-product-spec"><div><dt>생산능력</dt><dd>최대 750 kg/h</dd></div><div><dt>펠렛 크기</dt><dd>3 / 6 / 10 / 16 mm</dd></div><div><dt>제어</dt><dd>15인치 터치 디스플레이</dd></div></dl><span class="plt-product-more">제품 상세 보기 <i>→</i></span></div>
          </a>
          <a class="plt-product" data-capacity="1500" href="pr1500h.html">
            <span class="plt-recommend">추천 모델</span>
            <div class="plt-product-media"><img src="../../assets/img/pelletizer-pr1500h-official.jpg" alt="Cold Jet PR1500H 드라이아이스 제조기" loading="lazy" /></div>
            <div class="plt-product-body"><span class="plt-product-tag">LARGE-SCALE PRODUCTION</span><h3>PR1500H</h3><p class="plt-product-desc">4개의 독립 배럴로 초대형 생산시설을 지원하는 최상위 모델.</p><dl class="plt-product-spec"><div><dt>생산능력</dt><dd>최대 1,500 kg/h</dd></div><div><dt>펠렛 크기</dt><dd>3 / 6 / 10 / 16 mm</dd></div><div><dt>구성</dt><dd>4개 독립 배럴</dd></div></dl><span class="plt-product-more">제품 상세 보기 <i>→</i></span></div>
          </a>
          <a class="plt-product plt-special" href="special-forms.html">
            <div class="plt-product-media"><img src="../../assets/img/pelletizer-rseries-official.jpg" alt="Cold Jet R Series 슬라이스 리포머" loading="lazy" /></div>
            <div class="plt-product-body"><span class="plt-product-tag">SLICE REFORMERS</span><h3>R Series</h3><p class="plt-product-desc">별도 펠렛타이저에서 만든 펠렛을 필요한 규격의 슬라이스·블록으로 재성형하는 리포머 제품군입니다.</p><dl class="plt-product-spec"><div><dt>R500H · R1000H · R2000H</dt><dd>600 / 1,000 / 2,500 kg/h</dd></div><div><dt>구성 조건</dt><dd>펠렛타이저 별도 필요</dd></div></dl><span class="plt-product-more">R Series 자세히 보기 <i>→</i></span></div>
          </a>
        </div>

        <section class="plt-finder" id="model-finder" aria-labelledby="finderTitle">
          <div class="plt-finder-head">
            <div><span class="plt-eyebrow">FIND YOUR PRODUCTION SYSTEM</span><h2 id="finderTitle">고객님께 필요한 장비 조합,<br>30초면 알 수 있습니다.</h2></div>
            <div class="plt-finder-intro"><p>형태, 치수, 설치·공급 조건과 생산량을 차례로 선택하세요. 조건에 맞는 제조기와 리포머 구성을 바로 확인할 수 있습니다.</p></div>
            <nav class="plt-finder-progress" aria-label="장비 선택 단계">
              <button type="button" class="is-active" data-go-step="1"><i>01</i><span>드라이아이스 형태 선택</span><small id="stepSummary1">펠렛 · 너겟</small></button>
              <button type="button" data-go-step="2"><i>02</i><span>희망 규격 선택</span><small id="stepSummary2">Ø 3 mm</small></button>
              <button type="button" data-go-step="3"><i>03</i><span id="stepThreeLabel">설치 방법 선택</span><small id="stepSummary3">고정 설치</small></button>
              <button type="button" data-go-step="4"><i>04</i><span>희망 생산량 선택</span><small id="stepSummary4">350 kg/h</small></button>
            </nav>
          </div>

          <div class="plt-finder-shell">
            <div class="plt-finder-row">
              <div class="plt-finder-main">
                <form class="plt-finder-form" id="productionFinder">
              <fieldset class="plt-shape-field is-active" data-finder-step="1">
                <legend><span>01</span> 원하는 드라이아이스 형태</legend>
                <div class="plt-shape-options">
                  <label><input type="radio" name="iceShape" value="pellet" checked><span><i class="shape-pellet" aria-hidden="true"></i><b>펠렛 · 너겟</b><small>블라스팅 · 식품 공정 · 벌크 냉각</small></span></label>
                  <label><input type="radio" name="iceShape" value="slice"><span><i class="shape-slice" aria-hidden="true"></i><b>슬라이스 · 블록</b><small>배송 · 콜드체인 · 장시간 냉각</small></span></label>
                </div>
              </fieldset>

              <fieldset class="plt-dimension-field" data-finder-step="2">
                <legend><span id="dimensionStep">02</span> 원하는 제품 치수</legend>
                <p class="plt-field-intro" id="dimensionIntro">펠렛타이저가 압출·절단한 낱개 펠렛의 지름을 선택합니다. 필요한 생산량에 맞는 장비를 이 규격으로 검토합니다.</p>
                <div class="plt-dimension-fields" id="dimensionFields"></div>
                <p id="dimensionHelp">치수는 제품 성형 가능 여부와 다이·프레스 구성을 검토하는 기준입니다. 최종 규격은 원료와 운전 조건을 포함한 생산 테스트 후 확정합니다.</p>
              </fieldset>

              <fieldset class="plt-location-field" id="locationField" data-finder-step="3">
                <legend><span id="locationStep">03</span> 설치 장소 변경 가능성</legend>
                <div class="plt-binary-options">
                  <label><input type="radio" name="installation" value="fixed" checked><span><b>고정 설치</b><small>한 장소에서 지속적으로 생산</small></span></label>
                  <label><input type="radio" name="installation" value="mobile"><span><b>장소 변경 고려</b><small>Production Hub 구성 검토</small></span></label>
                </div>
                <p><strong>Production Hub는 PR120H 또는 PR350H만 구성할 수 있습니다.</strong></p>
              </fieldset>

              <fieldset class="plt-supply-field" id="sliceSupplyField" data-finder-step="3" hidden>
                <legend><span>03</span> 리포머에 공급할 펠렛</legend>
                <p class="plt-field-intro">슬라이스·블록은 리포머(R Series)가 드라이아이스 펠렛을 압축해 만듭니다. 이 펠렛을 직접 생산할지, 이미 보유한 펠렛을 사용할지 선택하세요.</p>
                <div class="plt-binary-options">
                  <label><input type="radio" name="sliceSupply" value="produce" checked><span><b>펠렛도 함께 생산</b><small>R Series + 펠렛타이저 구성</small><em>필요 설비: 드라이아이스 펠렛 제조기 + 리포머. 펠렛타이저가 펠렛을 생산하고, 리포머가 이를 압축해 원하는 슬라이스·블록 규격으로 성형합니다.</em></span></label>
                  <label><input type="radio" name="sliceSupply" value="existing"><span><b>기존 펠렛 사용</b><small>보유 제조기 또는 외부 공급 활용</small><em>필요 설비: 리포머. 이미 확보한 드라이아이스 펠렛을 리포머에 투입해 원하는 슬라이스·블록 규격으로 압축·성형합니다.</em></span></label>
                </div>
              </fieldset>

              <fieldset class="plt-capacity-field" data-finder-step="4">
                <legend><span id="capacityStep">04</span> 필요한 시간당 생산량</legend>
                <div class="plt-capacity-limit" id="capacityLimit">현재 조건에서 선택 가능: 최대 1,500 kg/h</div>
                <div class="plt-selector">
                  <label for="capacitySelector" class="plt-selector-label">필요한 시간당 생산량</label>
                  <div class="plt-selector-track">
                    <input id="capacitySelector" type="range" min="20" max="1500" value="350" step="10" aria-describedby="capacityHelp" />
                    <div class="plt-capacity-ticks" id="capacityTicks" aria-hidden="true"></div>
                  </div>
                  <div class="plt-capacity-value"><input id="capacityNumber" type="number" min="1" max="1500" value="350" inputmode="numeric" aria-label="필요한 시간당 생산량 직접 입력"><span>kg/h</span></div>
                </div>
                <p id="capacityHelp">앞에서 선택한 치수와 구성 조건에 맞춰 생산량 범위가 제한됩니다. 피크 수요와 운전 시간을 고려한 여유 용량을 포함해 입력하세요.</p>
                <details class="plt-demand-calc">
                  <summary>시간당 생산량을 모른다면 일일 사용량으로 계산</summary>
                  <div class="plt-demand-fields">
                    <label><span>하루 필요량</span><span class="plt-unit-input"><input id="dailyDemand" type="number" min="1" value="1000" inputmode="numeric"><i>kg/day</i></span></label>
                    <label><span>하루 생산 시간</span><span class="plt-unit-input"><input id="dailyHours" type="number" min="1" max="24" value="8" inputmode="numeric"><i>hours</i></span></label>
                    <output id="dailyResult"><small>필요 시간당 생산량</small><b>125 kg/h</b></output>
                  </div>
                </details>
              </fieldset>
                </form>
              </div>

              <aside class="plt-finder-visual" id="finderVisual" aria-hidden="true">
                <svg id="finderVisualSvg" viewBox="0 0 220 200" role="img" aria-label="선택한 치수의 3D 미리보기"></svg>
                <span class="plt-finder-visual-caption" id="finderVisualCaption"></span>
              </aside>
            </div>

            <div class="plt-finder-nav">
              <button type="button" class="plt-step-back" id="finderPrev" disabled>이전</button>
              <span><b id="finderCurrentStep">1</b> / 4</span>
              <button type="button" class="plt-step-next" id="finderNextStep">다음 <i>→</i></button>
            </div>

            <aside class="plt-finder-result" id="finderResult" aria-live="polite" hidden>
              <div class="plt-result-top"><span class="plt-result-label">조건에 맞는 추천 구성</span><span class="plt-result-live">실시간 업데이트</span></div>
              <div class="plt-result-products" id="finderProducts" aria-label="추천 제품 구성"></div>
              <div class="plt-result-copy">
                <div class="plt-result-summary"><small id="finderType">펠렛 생산 · 350 kg/h</small><h3 id="finderModel">PR350H</h3><p id="finderReason">입력한 생산량을 충족하는 가장 가까운 펠렛타이저입니다.</p></div>
                <div class="plt-result-actions"><dl><div><dt>추천 구성</dt><dd id="finderConfig">펠렛 다이 검토</dd></div><div><dt>다음 단계</dt><dd id="finderNext">실제 사용량 확인</dd></div></dl></div>
              </div>
              <div class="plt-result-note-box">
                <span class="plt-result-note-title">NOTE</span>
                <p id="finderNote">이 결과는 1차 장비 선정을 위한 안내입니다. LCO<sub>2</sub> 공급 조건, 요구 밀도와 자동화 범위에 따라 최종 구성이 달라질 수 있습니다.</p>
                <p id="finderNoteTip"></p>
                <div class="plt-result-note-footer"><a class="plt-btn is-small" id="finderLink" href="pr350h.html">추천 모델 상세 보기 <span>→</span></a></div>
              </div>
            </aside>
          </div>
        </section>
      </div>
    </section>

    <section class="plt-section plt-tech" id="difference">
      <div class="wrap">
        <div class="plt-head">
          <div><span class="plt-eyebrow">THE COLD JET DIFFERENCE</span><h2 class="plt-title">한 대의 사양보다,<br>생산의 연속성을 설계합니다.</h2></div>
          <p class="plt-lead">Cold Jet의 차이는 단순 최대 생산량보다 전환 효율, 가동 방식, 형태 전환과 후공정 연결에서 드러납니다. 실제 적용 기능은 모델과 선택 사양에 따라 달라집니다.</p>
        </div>
        <div class="plt-compare">
          <div class="plt-compare-head"><span>구매 시 비교할 항목</span><b>일반적인 단독 제조기</b><strong>Cold Jet 생산 시스템</strong></div>
          <div class="plt-compare-row"><span>제품 형태와 용량</span><p>한정된 펠렛 규격과 생산량 중심</p><p>80–1,500 kg/h 펠렛 라인과 R Series 슬라이스 리포머 구성</p></div>
          <div class="plt-compare-row"><span>LCO<sub>2</sub> 전환</span><p>기본 팽창·압축 조건 중심</p><p>Sub-Cooling 기술로 전환 효율과 생산 비용 개선을 목표로 설계</p></div>
          <div class="plt-compare-row"><span>운전과 형태 전환</span><p>수동 조작과 생산 중단이 발생할 수 있음</p><p>연속 운전, 원버튼 기동, 지원 모델의 자동 다이 교체</p></div>
          <div class="plt-compare-row"><span>상태 확인과 지원</span><p>현장 점검 위주의 독립 운전</p><p>지원 모델의 Cold Jet CONNECT® 원격 모니터링·진단</p></div>
          <div class="plt-compare-row"><span>후공정 연결</span><p>이송·계량·포장을 별도로 구성</p><p>정량 투입, 포장, 슬라이스 성형과 생산라인 통합 설계</p></div>
          <div class="plt-compare-row"><span>원료 순환</span><p>생산 중 리버트 가스를 배출</p><p>RE-CO<sub>2</sub> 시스템으로 리버트 가스 회수·재사용 선택 가능</p></div>
        </div>
        <p class="plt-compare-note">※ ‘일반적인 단독 제조기’는 비교 이해를 돕기 위한 대표적 구성입니다. 최종 비교는 후보 장비의 실제 사양, LCO<sub>2</sub> 조건, 요구 생산량과 자동화 범위를 기준으로 진행해야 합니다.</p>
      </div>
    </section>

    <section class="plt-section plt-sustainability">
      <div class="wrap plt-sustain-grid">
        <div class="plt-sustain-copy">
          <span class="plt-eyebrow">GIVING CO<sub>2</sub> A SECOND LIFE</span>
          <h2 class="plt-title">포집된 CO<sub>2</sub>를<br>냉각과 세척에 다시 활용합니다.</h2>
          <p>드라이아이스는 산업·바이오가스 시설 등에서 포집된 CO<sub>2</sub>를 액화하고 고체로 전환해 유용한 냉각·세척 매체로 사용하는 CCU(Carbon Capture and Utilization)의 한 형태입니다.</p>
          <p>현장 생산은 장거리 운송과 보관 중 승화 부담을 줄일 수 있고, 생산 규모가 크다면 리버트 가스 회수까지 연결해 액체 CO<sub>2</sub> 사용 효율을 높일 수 있습니다.</p>
          <small>환경 효과는 CO<sub>2</sub> 원천, 전력 구성, 운송 거리, 회수 설비와 대체 공정에 따라 달라집니다. 따라서 실제 도입 시 전체 운영 조건을 함께 평가합니다.</small>
        </div>
        <div class="plt-sustain-visual">
          <img src="../../assets/img/co2-second-life-infographic.png" alt="산업 공정에서 포집된 CO2가 액화·운송·저장 과정을 거쳐 드라이아이스로 전환되는 과정" loading="lazy" />
          <div class="plt-sustain-points"><span>RECYCLED CO<sub>2</sub></span><span>ON-SITE PRODUCTION</span><span>OPTIONAL RECOVERY</span></div>
        </div>
      </div>
    </section>

    <section class="plt-section plt-support">
      <div class="wrap plt-support-grid">
        <div class="plt-support-copy"><span class="plt-eyebrow">VATEK / LOCAL ENGINEERING SUPPORT</span><h2 class="plt-title">생산량 계산부터<br>설치 이후까지.</h2><p>바테크는 사용 목적과 일일 필요량, 액체 CO<sub>2</sub> 공급 조건, 생산 공간과 전원을 확인해 펠렛타이저와 슬라이스, 이송·포장·회수 설비까지 필요한 범위로 구성합니다.</p></div>
        <aside class="plt-support-panel"><h3>도입 전 확인할 내용</h3><ul><li>시간당·일일 필요 생산량</li><li>필요한 펠렛 또는 슬라이스 크기</li><li>액체 CO<sub>2</sub> 저장·공급 조건</li><li>전원·압축공기·설치 공간</li><li>포장·이송·정량 투입·회수 범위</li></ul><a class="plt-btn" href="../quote.html">생산 시스템 상담 <span>→</span></a></aside>
      </div>
    </section>
  </main>
"""


def build_blaster(root, nav_html, footer_html, page_shell, asset):
    depth = 2
    html = page_shell(BLASTER_PAGE_TITLE, BLASTER_PAGE_DESC, depth, "products", BLASTER_HUB_BODY,
                       extra_script=BLASTER_SCRIPT)
    group_dir = os.path.join(root, "products", "blaster")
    os.makedirs(group_dir, exist_ok=True)
    with open(os.path.join(group_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    for m in BLASTER_MODELS:
        build_model_page(root, "products", "blaster", "드라이아이스 세척기 (블라스터)", m, BLASTER_MODELS,
                          nav_html, footer_html, page_shell, asset)
    return 1 + len(BLASTER_MODELS)


def build_pelletizer(root, nav_html, footer_html, page_shell, asset):
    depth = 2
    extra_head = '\n<link rel="stylesheet" href="%spelletizer-page.css?v=20260911-15" />' % asset('assets/css/', depth)
    html = page_shell(PELLETIZER_PAGE_TITLE, PELLETIZER_PAGE_DESC, depth, "products", PELLETIZER_HUB_BODY,
                       extra_script=PELLETIZER_SCRIPT, extra_head=extra_head)
    group_dir = os.path.join(root, "products", "pelletizer")
    os.makedirs(group_dir, exist_ok=True)
    with open(os.path.join(group_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    for m in PELLETIZER_MODELS:
        build_model_page(root, "products", "pelletizer", "드라이아이스 제조기 (펠렛타이저)", m, PELLETIZER_MODELS,
                          nav_html, footer_html, page_shell, asset)
    return 1 + len(PELLETIZER_MODELS)


def build_recovery(root, nav_html, footer_html, page_shell, asset):
    build_group_index(
        root, "products", "recovery", "CO2 리커버리",
        "드라이아이스 생산 중 배출되는 CO2 가스를 회수해 재사용하는 리커버리 시스템입니다. "
        "펠렛타이저 생산능력에 맞춰 4단계 모델을 제공합니다.",
        RECOVERY_MODELS, None, nav_html, footer_html, page_shell, asset,
        intro_html=RECOVERY_INTRO_HTML,
    )
    for m in RECOVERY_MODELS:
        build_model_page(root, "products", "recovery", "CO2 리커버리", m, RECOVERY_MODELS,
                          nav_html, footer_html, page_shell, asset)
    return 1 + len(RECOVERY_MODELS)
