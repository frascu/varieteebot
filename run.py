# importing the requests library
# pip install requests
# pip install beautifulsoup4

import sys
import requests
from bs4 import BeautifulSoup
from tee import get_tees

if len(sys.argv) < 2:
    sys.exit()

# send the images
BASE_URL = "https://api.telegram.org/bot{}/"
API_TOKEN = sys.argv[1]
CHAT_ID = "@varietee"


def send(method, params):
    url_string = BASE_URL.format(API_TOKEN) + method
    print(BASE_URL)
    print(method)
    print("parameters:", params)
    r = requests.get(url=url_string, params=params)

    print("response:", r.json())


caption = 'New Today Tee!!\n\n{}\n\n{}'

images = get_tees()
for image in images:
    send("sendPhoto", {"chat_id": CHAT_ID, "photo": image.link, "caption": caption.format(image.title, image.source)})
