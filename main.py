import requests
from bs4 import BeautifulSoup

url = "http://motions.cat/top.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

r = requests.get(url=url,headers=headers)
soup = BeautifulSoup(r.content,"html.parser")
anchor = soup.find_all("a")
images = soup.find_all("img")
for a in anchor:
    src = a.img['src']
    newUrl = "http://motions.cat/{}".format(images)
    # print(newUrl)
    print(src)
