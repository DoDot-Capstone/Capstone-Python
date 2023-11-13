import requests

url = 'https://mvnrepository.com/robots.txt'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Faailed to retrieve {url}. Status code: {response.status_code}")