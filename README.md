## DissKold-sfellChekc

디스코드 맞춤법 검사봇 구현하기 💡

#### Discord.py API 사용

-   [x] 디스코드 서버 및 봇 계정 생성
-   [x] 서버 연결 및 봇 작동 확인
-   [x] 정규표현식 모듈화
-   [ ] 정규표현식 유형 추가
-   [ ] 테스트

### 사용 방법

```sh
(Linux 기준)
python3.5 이상 버전 필요
python3 -m pip install -U discord.py
git clone
python3 bot.py
.env 파일에 토큰값 입력하고 사용
```

### 디렉토리 구조
```bash
DissKold-sfellChekc
│  .gitignore
│  README.md
│
├─Data
│      data1.csv
│
└─Src
    │  bot.py
    │
    └─spellcheck
            firstStepReg.py
            regExp.py
```
