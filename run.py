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
CHAT_ID = sys.argv[2]


def send(method, params):
    url_string = BASE_URL.format(API_TOKEN) + method
    print("CALL: ", BASE_URL + method)
    print("PARAMETERS:", params)

    r = requests.get(url=url_string, params=params)

    print("RESPONSE:", r.json())


caption = '[New Today\'s Tee]\n\n{}\n\n{}'

images = get_tees()
for image in images:
    title = image.title.replace("by", "\nby")
    send("sendPhoto", {"chat_id": CHAT_ID, "photo": image.link, "caption": caption.format(title, image.source),
                       "reply_markup": [[{"text": "text", "url": "https://www.pampling.com"}]]
                       })
