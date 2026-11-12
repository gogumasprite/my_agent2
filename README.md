# 우리 회사 챗봇

아주대학교 청년도약부트캠프 3일차 Streamlit 실습 프로젝트입니다.

- **채팅 연습**에서 입력과 응답을 화면에 표시하고 세션에 저장합니다.
- **AI 챗봇**에서 대화 내역을 바탕으로 OpenAI 응답을 생성합니다.
- **위젯 연습**에서 엑셀 파일을 올리고 미리 볼 수 있습니다.

## Windows PowerShell에서 실행

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

AI 챗봇을 사용하려면 프로젝트 폴더의 `.env`에 `OPENAI_API_KEY`를 설정하세요. Streamlit Community Cloud에 배포할 때는 앱의 Secrets 설정에 같은 변수를 추가하세요. 로컬의 `.env`와 `.venv`는 Git에 포함하지 않습니다.
