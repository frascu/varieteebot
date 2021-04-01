import requests
from bs4 import BeautifulSoup


class Image:

    def __init__(self, link, title, source):
        self.link = link
        self.title = title
        self.source = source

    def __str__(self):
        return f'{self.link} {self.title} {self.source}'

    def __repr__(self):
        return f'{self.link} {self.title} {self.source}'


def add_qwertee_tees(images):
    # retrieve images from qwertee
    url = "https://www.qwertee.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div_slides = soup.find("div", {"class": "big-slides"})
    my_divs = div_slides.find_all("div", {"class": "index-tee"})

    for my_div in my_divs:
        title = my_div.find("div", {"class": "title"})
        image = my_div.find("img")
        link = image.get("src").replace("mens", "zoom")
        images.append(Image(link, title.text, url))


def add_tee_tee_eu_tees(images):
    # retrieve images from teetee
    url = "https://www.teetee.eu"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div_slides = soup.find("div", {"class": "slide-product"})

    # url_image = soup.find("div", {"class": "sidebar"}).find_all('a')[0]["href"].replace("uploads//", "uploads/")
    div_image = div_slides.find_all("div", {"class": "design"})[0]
    url_image = div_image["style"].replace("background-image:url('", "").replace("');", "").replace("http:", "https:")

    div_title = div_slides.find("div", {"class": "info-product"})
    title = div_title.find("h1").text + " " + div_title.find("h2").text

    images.append(Image(url_image, title, url))


def add_pampling_tees(images):
    # retrieve images from teetee
    url = "https://www.pampling.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div_slides = soup.find(id="modulo-xt-doble")

    div_images = div_slides.find_all("div", {"class": "carousel-inner"})
    div_titles = div_slides.find_all("div", {"class": "franja-autor"})

    for i in range(len(div_images)):
        div_image = div_images[i].find("div", {"class": "active"})
        title = div_titles[i].text.replace("\n", " ").strip()

        url_image = div_image["style"].replace("background-image:url(", "").replace(");", "")

        images.append(Image(url_image, title, url))


def get_tees():
    images = []
    add_qwertee_tees(images)
    # add_tee_tee_eu_tees(images)
    add_pampling_tees(images)
    return images


if __name__ == "__main__":
    for tee in get_tees():
        print(tee)
