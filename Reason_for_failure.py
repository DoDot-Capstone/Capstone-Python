import sys
import time
import requests
from bs4 import BeautifulSoup

url = 'https://mvnrepository.com/search?q=what'

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language" : "ko,en;q=0.9,en-US;q=0.8",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

try:
    r = requests.get(url, timeout=5, headers=headers)
    r.raise_for_status()  # 만약 요청이 실패하면 예외를 일으키기
except requests.exceptions.HTTPError as errh:
    print ("HTTP Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("Something went wrong:",err)
    sys.exit(1)