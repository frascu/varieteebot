import requests
from bs4 import BeautifulSoup
from lxml import etree


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
    try:
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

    except IndexError:
        print("No tees found for qwertee")


def add_tee_tee_eu_tees(images):
    try:
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
        images.append(Image(url_image.replace("uploads//", "uploads/"), title, url))

    except IndexError:
        print("No tees found for tee tee")


def add_pampling_tees(images):
    try:
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

    except IndexError:
        print("No tees found for pampling")


def add_theyetee_tees(images):
    try:
        url = "https://theyetee.com"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        dom = etree.HTML(str(soup))

        a_element = dom.xpath("/html/body/div[8]/article/div[3]/section[1]/div[1]/section/div/div/div[1]/a")[0]
        url_image = "https:" + a_element.attrib["href"]

        name = dom.xpath("/html/body/div[8]/article/div[3]/section[1]/div[2]/div[1]/h2")[0].text
        owner = dom.xpath("/html/body/div[8]/article/div[3]/section[1]/div[2]/div[1]/div/a")[0].text
        title = name + " by " + owner
        images.append(Image(url_image.split("?")[0], title.strip(), url))

        a_element = dom.xpath("/html/body/div[8]/article/div[3]/section[2]/div[1]/section/div/div/div[1]/a")[0]
        url_image = "https:" + a_element.attrib["href"]

        name = dom.xpath("/html/body/div[8]/article/div[3]/section[2]/div[2]/div[1]/h2")[0].text
        owner = dom.xpath("/html/body/div[8]/article/div[3]/section[2]/div[2]/div[1]/div/a")[0].text
        title = name + " " + owner
        images.append(Image(url_image.split("?")[0], title.strip(), url))

    except IndexError:
        print("No tees found for thyeetee")


def add_othertees_tees(images):
    try:
        base_url = "https://www.othertees.com"
        url = base_url + "/daily-tees"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for i in range(3):
            div_element = soup.select(f'#limited_container > div > div:nth-child({i + 1}) > div.project > div.project-img > div')[0]
            url_image = base_url + div_element.attrs["data-src"]
            title = soup.select(f'#limited_container > div > div:nth-child({i + 1}) > div.project > h4 > a')[0].text
            author = soup.select(f'#limited_container > div > div:nth-child({i + 1}) > div.project > h4 > p > a')[0].text
            title = title + " by " + author
            images.append(Image(url_image, title.strip(), url))
    
    except IndexError:
        print("No tees found for thyeetee")


def get_tees():
    images = []
    add_qwertee_tees(images)
    # add_tee_tee_eu_tees(images)
    add_pampling_tees(images)
    add_theyetee_tees(images)
    add_othertees_tees(images)
    # https://www.designbyhumans.com/shop/mens-t-shirts/
    return images


if __name__ == "__main__":
    for tee in get_tees():
        print(tee)
