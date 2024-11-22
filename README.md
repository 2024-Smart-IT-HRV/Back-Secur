📖 README.md
markdown
코드 복사
# Flask Backend API

## 📂 프로젝트 구조
perl
코드 복사
📁 back/
├── 📂 app/              # 애플리케이션 설정 및 유틸리티
│   ├── __init__.py      # Flask 초기화
│   ├── config.py        # 설정 파일
│   ├── encryption.py    # 암호화 유틸리티
│   ├── validation.py    # 데이터 검증
├── 📂 auth/             # 사용자 인증
│   ├── routes.py        # 로그인 API
│   ├── services.py      # JWT 생성
├── 📂 hrv/              # HRV 데이터 관리
│   ├── routes.py        # HRV 저장/조회 API
├── 📂 study/            # 공부방 및 과목 관리
│   ├── routes.py        # 과목 추가, 공부 기록 저장 API
│   ├── models.py        # 데이터베이스 모델
├── 📂 security/         # 보안 설정
│   ├── tls.py           # TLS/SSL 설정
├── 📂 migrations/       # 데이터베이스 마이그레이션
├── 📂 common_tests/     # 공통 테스트
│   ├── test_validation.py  # 검증 테스트
├── run.py               # 애플리케이션 실행 파일
├── requirements.txt     # 패키지 목록
└── README.md            # 프로젝트 설명



📋 주요 기능
1. 사용자 인증
로그인: /auth/login (POST)
2. HRV 데이터 관리
저장: /hrv/data (POST)
조회: /hrv/data (GET)
3. 공부방 및 과목 관리
과목 추가: /study/subjects (POST)
공부 기록 저장: /study/logs (POST)

