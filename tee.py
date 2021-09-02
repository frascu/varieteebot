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

    a_element = soup.select_one("#teecommerce > div.content.body-product > div > div > div > div:nth-child(2) > "
                                "div.col-md-4 > div > a")

    url_image = a_element["href"]

    div_title_1 = soup.select_one(
        "#teecommerce > div.content.head-product > div > div > div > div > div.info-product.animated.fadeIn > h1")
    div_title_2 = soup.select_one(
        "#teecommerce > div.content.head-product > div > div > div > div > div.info-product.animated.fadeIn > h2")
    title = div_title_1.text + " " + div_title_2.text
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

        images.append(Image(url_image, title.strip(), url))


def add_theyetee_tees(images):
    url = "https://theyetee.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    a_element = soup.select_one(
        "article > div:nth-child(3) > section.module_timed-item.is--full.is--left > "
        "div.module_timed-item--images")
    a_element = a_element.find_all("a")[0]
    url_image = "https:" + a_element["href"]

    div_title = soup.select_one(
        "article > div:nth-child(3) > section.module_timed-item.is--full.is--left > "
        "div.module_timed-item--content > div.module_timed-item--info")
    title = div_title.findChildren("h2")[0].text + " " + div_title.findChildren("div")[0].text
    images.append(Image(url_image.split("?")[0], title.strip(), url))

    a_element = soup.select_one(
        "article > div:nth-child(3) > section.module_timed-item.is--full.is--right > "
        "div.module_timed-item--images")
    a_element = a_element.find_all("a")[0]
    url_image = "https:" + a_element["href"]

    div_title = soup.select_one(
        "article > div:nth-child(3) > section.module_timed-item.is--full.is--right > "
        "div.module_timed-item--content > div.module_timed-item--info")
    title = div_title.findChildren("h2")[0].text + " " + div_title.findChildren("div")[0].text
    images.append(Image(url_image.split("?")[0], title.strip(), url))


def get_tees():
    images = []
    add_qwertee_tees(images)
    add_tee_tee_eu_tees(images)
    add_pampling_tees(images)
    # add_theyetee_tees(images)
    # https://www.othertees.com/daily-tees
    # https://www.designbyhumans.com/shop/mens-t-shirts/
    return images


if __name__ == "__main__":
    for tee in get_tees():
        print(tee)
