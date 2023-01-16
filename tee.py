import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class Image:

    def __init__(self, link, title, source):
        self.link = link
        self.title = title
        self.source = source

    def __str__(self):
        return f'{self.link} {self.title} {self.source}'

    def __repr__(self):
        return f'{self.link} {self.title} {self.source}'


def add_qwertee_tees(images, browser):
    try:
        url = "https://www.qwertee.com"
        browser.get(url)
        for i in range(1, 4):
            title = browser.find_element(by=By.XPATH, value=f'//*[@id="root"]/div[1]/main/div/div[1]/div[{i}]/div[1]/header/div[1]/div')
            image = browser.find_element(by=By.XPATH, value=f'//*[@id="root"]/div[2]/main/div/div[1]/div[{i}]/div[2]/div/div/div[1]/div[2]/img')
            images.append(Image(image.get_attribute('src'), title.text.replace("\n", " "), url))

    except IndexError:
        print("No tees found for qwertee")


def add_tee_tee_eu_tees(images, browser):
    try:
        # retrieve images from teetee
        url = "https://www.teetee.eu"
        browser.get(url)

        image = browser.find_element(by=By.XPATH, value='//*[@id="teecommerce"]/div[2]/div/div/div/div[2]/div[2]/div/a')
        title1 = browser.find_element(by=By.XPATH, value='//*[@id="teecommerce"]/div[1]/div/div/div/div/div[2]/h1')
        title2 = browser.find_element(by=By.XPATH, value='//*[@id="teecommerce"]/div[1]/div/div/div/div/div[2]/h2')

        url_image = image.get_attribute("href")
        title = title1.text + " " + title2.text
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

            url_image = div_image.find("img")['src']

            images.append(Image(url_image, title.strip(), url))

    except IndexError:
        print("No tees found for pampling")


def add_theyetee_tees(images, browser):
    try:
        url = "https://theyetee.com"
        browser.get(url)
        
        a_element = browser.find_element(by=By.XPATH, value='/html/body/div[6]/article/div[3]/section[1]/div[1]/section/div/div/div[1]/a')
        url_image = a_element.get_attribute("href")
        title = browser.find_element(by=By.XPATH, value="/html/body/div[6]/article/div[3]/section[1]/div[2]/div[1]").text
        images.append(Image(url_image.split("?")[0], title.replace("\n", " "), url))

        a_element = browser.find_element(by=By.XPATH, value="/html/body/div[6]/article/div[3]/section[2]/div[1]/section/div/div/div[1]/a")
        url_image = a_element.get_attribute("href")
        title = browser.find_element(by=By.XPATH, value="/html/body/div[6]/article/div[3]/section[2]/div[2]/div[1]").text
        images.append(Image(url_image.split("?")[0], title.replace("\n", " "), url))

    except IndexError:
        print("No tees found for thyeetee")

def get_tees():


    # set preferences
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)

    images = []
    add_qwertee_tees(images, browser)
    add_tee_tee_eu_tees(images, browser)
    add_pampling_tees(images)
    add_theyetee_tees(images, browser)
    # https://www.designbyhumans.com/shop/mens-t-shirts/

    browser.close()
    return images


if __name__ == "__main__":
    for tee in get_tees():
        print(tee)
