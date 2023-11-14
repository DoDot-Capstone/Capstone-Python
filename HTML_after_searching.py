import sys
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://mvnrepository.com/search?q='
search = input("검색해: ")
search_url = url + search
# Selenium 설정
options = Options()
options.headless = True  # 브라우저를 화면에 표시하지 않음(존나게 잘보임)

# Selenium을 사용하여 브라우저를 열지 않고 페이지에 접근 (존나 잘열림)
with webdriver.Chrome(options=options) as driver:
    driver.get(search_url)

    # Selenium을 사용하여 현재 페이지의 소스를 가져오기
    html = driver.page_source

# BeautifulSoup을 사용하여 페이지 소스를 파싱
soup = BeautifulSoup(html, 'html.parser')
text = soup.select("body > div > main > div.content > div:nth-child(4) > div.im-header > h2")
print(text)

# requests를 사용하여 다른 웹 페이지에 HTTP 요청 보내기
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "ko,en;q=0.9,en-US;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

try:
    r = requests.get(url, timeout=5, headers=headers)
    r.raise_for_status()  # 만약 요청이 실패하면 예외를 일으키기
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)
    sys.exit(1)
