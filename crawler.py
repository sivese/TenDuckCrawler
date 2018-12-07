from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import queue

class OtakuCrawler:
    def __init__(self):
        self.b = 10
        self.url = "https://www.pixiv.net/search.php?s_mode=s_tag&word=moe"

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable=gpu')

        self.driver = webdriver.Chrome('./driver/chromedriver.exe', chrome_options=options)
        self.driver.implicitly_wait(3)
        self.download_que = []

    #def searchImageByKeyword(self, keyword):

    def nextPage(self, page):
        url = self.url + "&p=" + page

    def run(self):
        self.driver.get(self.url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        image_list = soup.select('body > div > div > div > section > div > div')

        for image in image_list:
            print(image)

otaku = OtakuCrawler()
otaku.run()