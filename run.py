# importing the requests library
# pip install requests
# pip install beautifulsoup4

import sys

import requests

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

    json = r.json()

    print("RESPONSE:", json)
    if not json["ok"]:
        raise Exception("Sending is failed")


caption = '[New Today\'s Tee]\n{}\n{}'

images = get_tees()
print(images)
media_array = [{"type": "photo", "media": image.link, "caption": caption.format(image.title, image.source)}
               for image in images]

if len(media_array) <= 10:
    send("sendMediaGroup", {"chat_id": CHAT_ID, "media": media_array})
else:
    middle_index = int(len(media_array) / 2)
    send("sendMediaGroup", {"chat_id": CHAT_ID, "media": media_array[:middle_index]})
    send("sendMediaGroup", {"chat_id": CHAT_ID, "media": media_array[middle_index:]})
