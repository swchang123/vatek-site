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


def build_blaster(root, nav_html, footer_html, page_shell, asset):
    build_group_index(
        root, "products", "blaster", "드라이아이스 세척기 (블라스터)",
        "스마트 · 펠릿 · 마이크로파티클 · 특수 목적, 4개 카테고리 8개 모델 라인업입니다. "
        "모델을 클릭하면 Overview · Cold Jet만의 강점 · Features · Specifications · Accessories를 확인하실 수 있습니다.",
        BLASTER_MODELS, BLASTER_CATEGORIES, nav_html, footer_html, page_shell, asset,
    )
    for m in BLASTER_MODELS:
        build_model_page(root, "products", "blaster", "드라이아이스 세척기 (블라스터)", m, BLASTER_MODELS,
                          nav_html, footer_html, page_shell, asset)
    return 1 + len(BLASTER_MODELS)


def build_pelletizer(root, nav_html, footer_html, page_shell, asset):
    build_group_index(
        root, "products", "pelletizer", "드라이아이스 제조기 (펠렛타이저)",
        "저용량 입문형부터 초대형 생산시설용까지, 생산능력별 라인업입니다. "
        "모델을 클릭하면 Features · Specifications를 확인하실 수 있습니다.",
        PELLETIZER_MODELS, None, nav_html, footer_html, page_shell, asset,
    )
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
