import requests
from bs4 import BeautifulSoup

url = "http://motions.cat/top.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
anchors = soup.find_all("a")
images = soup.find_all("img")
# for image in images[3:-5]:
#     src = image["src"]
#     imageUrl = "http://motions.cat/gif/nhn/0146.gif"
for anchor in anchors[4:-6]:
    try:
        href = anchor["href"]
        imageUrl = "http://motions.cat/{}".format(href)
        # part = href.split(".gif")[0]
        # filename = part.split("/")[-1]
        gifFile = href.split("/")[-1]
        filename = gifFile.split(".gif")[0]
        getRequest = requests.get(imageUrl, headers=headers)
        if getRequest.status_code == 200:
            with open(gifFile, "wb") as f:
                # write with binary for "wb"
                # read with binary for "rb"
                fileWrite = f.write(getRequest.content)
                print("Saving {} now...".format(gifFile))
        else:
            print("Error getting {}.".format(gifFile))
    except KeyError:
        print(KeyError)
