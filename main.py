import time
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
failedArr=[]
lostArr = ["0066.gif"]
# lostArr = ["0022.gif","0026.gif","0037.gif","0038.gif","0042.gif","0043.gif","0044.gif","0051.gif","0053.gif","0064.gif","0065.gif","0066.gif","0068.gif"]
for anchor in lostArr:
    try:
        imageUrl = "http://motions.cat/gif/nhn/{}".format(anchor)
        gifFile = "http://motions.cat/gif/nhn/{}".format(anchor)
        filename = gifFile.split(".gif")[0]
        # href = anchor["href"]
        # imageUrl = "http://motions.cat/{}".format(href)
        # gifFile = href.split("/")[-1]
        # filename = gifFile.split(".gif")[0]
        getRequest = requests.get(imageUrl, headers=headers)
        if getRequest.status_code == 200:
            with open(anchor, "wb") as f:
                fileWrite = f.write(getRequest.content)
                print("Saving {} now...".format(gifFile))
              
        else:
            print("Error getting {}.".format(gifFile))
            failedArr.append(gifFile)
    except KeyError:
        print(KeyError)
print("All files have been downloaded!")
for item in failedArr:
    print("Except for {}.".format(item))
print(failedArr)



# for image in images[3:-5]:
#     src = image["src"]
#     imageUrl = "http://motions.cat/gif/nhn/0146.gif"
# for anchor in anchors[4:-6]:


# part = href.split(".gif")[0]
# filename = part.split("/")[-1]

# write with binary for "wb"
# read with binary for "rb"