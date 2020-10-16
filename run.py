# importing the requests library
# pip install requests
# pip install beautifulsoup4
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    sys.exit()

# retrieve images from the sources
URL = "https://www.qwertee.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
my_divs = soup.findAll("div", {"class": "index-tee"})

titles = []
links = []
for my_div in my_divs:
    title = my_div.find("div", {"class": "title"})
    image = my_div.find("img")
    titles.append(title.text)
    links.append(image.get("src"))


# send the images
BASE_URL = "https://api.telegram.org/bot{}/"
API_TOKEN = sys.argv[1]
CHAT_ID = "@varietee"


def send(method, params):
    url_string = BASE_URL.format(API_TOKEN) + method
    print("request:", url_string)
    print("parameters:", params)
    r = requests.get(url=url_string, params=params)

    print("response:", r.json())


#text = "ciao"
# send("sendMessage", {'chat_id': CHAT_ID, 'text': text})

link_photo = "https://cdn.qwertee.com/images/designs/product-thumbs/1602515240-169377-zoom-450x540.jpg"

caption = 'New Today Tee!!\n{}\nhttps://www.qwertee.com/'

for i in range(0, len(links)):
    send("sendPhoto", {"chat_id": CHAT_ID, "photo": links[i], "caption": caption.format(titles[i])})
