import webbrowser
url = "https://mvnrepository.com/search?q="
search = input("검색할 내용:")
search_url = url + search
webbrowser.open(search_url)