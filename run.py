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

    r = requests.post(url=url_string, json=params)

    print("RESPONSE:", r.json())


caption = '[New Today\'s Tee]\n{}\n{}'

images = get_tees()
media_array = []
for image in images:
    media_array.append({"type": "photo", "media": image.link, "caption": caption.format(image.title, image.source)})

send("sendMediaGroup", {"chat_id": CHAT_ID, "media": media_array})
