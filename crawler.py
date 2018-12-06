import pickle
import cssutils
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import queue
from PIL import Image
from io import BytesIO
from urllib.request import urlopen

class OtakuCrawler:
   def __init__(self):
      self.b = 10
      self.url = "https://www.pixiv.net/search.php?s_mode=s_tag&word=moe"

      options = webdriver.ChromeOptions()
      options.add_argument('headless')
      options.add_argument('disable=gpu')

      self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
      self.driver.implicitly_wait(3)
      self.download_que = []

      pickle.dump(self.driver.get_cookies(),open("cookies.pkl","wb"))

   def nextPage(self, page):
      url = self.url + "&p=" + page

   def run(self):
      self.driver.get(self.url)
      cookies = pickle.load(open("cookies.pkl", "rb"))
      for cookie in cookies:
         driver.add_cookie(cookie)
      html = self.driver.page_source
      soup = BeautifulSoup(html, 'html.parser')
      image_list = soup.find("section",id="js-react-search-mid").find("div")

      #for div in image_list:
      #   div_style = div.select("figure > div > a > div")[0]
      #   s = str(div_style)
      #   print(s)
      #   begin = s.find("url(")
      #   end = s.find(");")

      #   url = s[begin + len("url("):end]

      url = "https://i.pximg.net/c/240x240/img-master/img/2018/12/06/07/21/55/71986522_p0_master1200.jpg"
      headers = {"Referer":"https://www.pixiv.net/"}
      response = requests.get(url, headers = headers)
      with open("./Fuckyou.jpg", 'wb') as f:
         f.write(response.content)

otaku = OtakuCrawler()
otaku.run()
