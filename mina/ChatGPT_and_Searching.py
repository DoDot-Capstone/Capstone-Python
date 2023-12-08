import openai
import re
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# OpenAI API 키 설정
openai.api_key = "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"
# MVN URL
MVN_REPOSITORY_URL = 'https://mvnrepository.com/search?q='


def configure_webdriver():
    # 웹 드라이버를 설정하는 함수
    options = Options()
    options.headless = True
    options.add_argument(f"--window-position=0,1000")  # x, y 좌표
    options.add_argument(f"--window-size=10,10")  # 너비, 높이
    return webdriver.Chrome(options=options)


def make_http_request(search_url):
    # HTTP 요청을 보내고 응답을 반환하는 함수
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'ko,en;q=0.9,en-US;q=0.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7'
    }

    proxies = {
        'http': 'http://your_proxy',
        'https': 'https://your_proxy',
    }

    try:
        response = requests.get(search_url, timeout=5, headers=headers, proxies=proxies)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
        sys.exit(1)

    return response


def search_mvn_repository(search):
    # MVN Repository에서 라이브러리 정보를 검색하는 함수
    search_url = MVN_REPOSITORY_URL + search

    with configure_webdriver() as driver:
        driver.get(search_url)
        html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    results = soup.select('.im-title a')

    libs = []

    for idx, result in enumerate(results, 1):
        if idx % 2 != 0:
            lib_name = result.get_text()
            href_value = result['href']
            libs.append((lib_name, href_value))

    return libs


def response(message):
    # GPT-3.5-turbo 모델을 사용하여 메시지에 대한 응답을 생성하는 함수
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "프로그래밍할 때 필요한 라이브러리를 추천해줍니다."},
            {"role": "user", "content": message},
            {"role": "user", "content": "프로그래밍할 때 필요한 라이브러리만 추천해줘야해, 무조건 라이브러리 이름에 해당하는 부분은 양 옆에 !!!를 넣어서 표시해줘. 코드 자료는 필요 없어"}
        ],
        temperature=0,
        max_tokens=256
    )
    return response['choices'][0]['message']['content']


def extract_libraries(result):
    # GPT 응답에서 라이브러리 이름을 추출하는 함수
    extract_word = re.compile('!!!(.+?)!!!')
    return extract_word.findall(result)


def search_libraries_in_mvn(library_list):
    # MVN Repository에서 라이브러리 정보를 검색하고 출력하는 함수
    for library in library_list:
        print(f"검색 중인 라이브러리: {library}")
        result = search_mvn_repository(library)

        for data in result:
            print(f"라이브러리 이름 : {data[0]}, 링크 : {data[1]}")
            print()


if __name__ == "__main__":
    # 사용자로부터 메시지 입력
    message = input("물어봐: ")
    # GPT에 메시지 전달 및 라이브러리 추출
    result = response(message)

    library_list = extract_libraries(result)

    print("추천 라이브러리")
    for name in library_list:
        print(f" - {name}")

    yesno = input("상세하게 보시겠습니까?")

    if yesno.lower() == 'yes':
        search_libraries_in_mvn(library_list)
