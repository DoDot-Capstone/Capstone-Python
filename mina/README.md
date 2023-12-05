# **MVN 라이브러리 검색**

### 이 스크립트는 OpenAI의 GPT-3.5-turbo 모델을 활용하여 사용자 입력을 기반으로 프로그래밍 라이브러리를 추천합니다. 이 추천은 MVN Repository에서 검색됩니다.

### 사전 준비 사항

Python 3.x
필요한 Python 패키지(다음 명령으로 설치: pip install -r requirements.txt):
* openai
* requests
* beautifulsoup4
* selenium

### 설정

OpenAI에서 API 키를 얻어와 openai.api_key 변수에 설정합니다.
configure_webdriver 함수에서 웹 드라이버를 구성합니다.

### 사용 방법

스크립트를 실행하고 프롬프트에 메시지를 입력합니다.
GPT-3.5-turbo 모델을 사용하여 메시지에 대한 응답 및 라이브러리 추출이 이루어집니다.
추출된 라이브러리를 이용하여 MVN Repository에서 라이브러리 정보를 검색하고 출력합니다.

### 참고 사항

스크립트는 MVN Repository를 통해 라이브러리 정보를 검색합니다.
라이브러리 이름은 사용자 입력에서 추출되며, 라이브러리의 검색 및 사용 빈도가 제시됩니다.
