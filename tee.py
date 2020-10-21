import requests
from bs4 import BeautifulSoup


class Image:

    def __init__(self, link, title, source):
        self.link = link
        self.title = title
        self.source = source


def get_tees():
    # retrieve images from qwertee
    url = "https://www.qwertee.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div_slides = soup.find("div", {"class": "big-slides"})
    my_divs = div_slides.findAll("div", {"class": "index-tee"})

    images = []
    for my_div in my_divs:
        title = my_div.find("div", {"class": "title"})
        image = my_div.find("img")
        link = image.get("src").replace("mens", "zoom")
        images.append(Image(link, title.text, url))

    # retrieve images from teetee
    url = "https://www.teetee.eu/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div_slides = soup.find("div", {"class": "slide-product"})

    url_image = soup.find("div", {"class": "sidebar"}).find_all('a')[0]["href"]
    div_title = div_slides.find("div", {"class": "info-product"})
    title = div_title.find("h1").text + " " + div_title.find("h2").text

    images.append(Image(url_image, title, url))

    return images
