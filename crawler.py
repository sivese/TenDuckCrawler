from bs4 import BeautifulSoup
import requests
import queue

class OtakuCrawler:
    def __init__(self):
        self.b = 10
        self.url = "https://www.pixiv.net/search.php?s_mode=s_tag&word=moe"
        self.download_que = []

    #def searchImageByKeyword(self, keyword):

    def nextPage(self, page):
        url = self.url + "&p=" + page

    def run(self):
        req = requests.get(self.url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        image_list = soup.select('body > div > div > div > section')

        for image in image_list:
            print(image)

otaku = OtakuCrawler()
otaku.run()