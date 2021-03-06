from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import datetime
import os, time
from status import StatusBar

class OtakuCrawler:
	def __init__(self, keyword):
		self.b = 10
		self.page = 0
		self.url = "https://www.pixiv.net/search.php?word="+keyword+"&p="

		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		options.add_argument('window-size=1920x6480')
		options.add_argument('disable=gpu')

		self.driver = webdriver.Chrome('./driver/chromedriver.exe', chrome_options=options)
		self.driver.implicitly_wait(3)
		self.download_que = []
		self.save_directory = ''
		self.counter = 0
		self.end = False

	def crawl(self, range):
		self.save_directory = datetime.datetime.now().strftime('%m%d %H%M%S')
		#work_bar = StatusBar()

		while self.page <= range:
			self.page += 1
			url = self.url + str(self.page)
			self.connect(url)
			self.download_que.clear()

		self.counter = 0
		self.end = True

	def writeDownloadFile(self, url):
		headers = {"Referer": "https://www.pixiv.net/"}
		response = requests.get(url, headers = headers)

		with open("./"+self.save_directory+"/"+ str(self.counter)+".jpg", 'wb') as f:
			f.write(response.content)

		self.counter += 1

	def pushOnDownloadQueue(self, url):
		if not ('background-image' in url):
			return

		begin = url.find("url(\"")
		end = url.find("\");")
		url = url[begin + len("url(\""):end]
		self.download_que.append(url)

	def connect(self, url):
		self.driver.get(url)

		time.sleep(5)

		html = self.driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		image_list = soup.find("section", id="js-react-search-mid").find("div")

		for div in image_list:
			div_style = div.select("figure > div > a > div")[0]
			s = str(div_style)

			self.pushOnDownloadQueue(s)

		try:
			if not (os.path.isdir('./'+self.save_directory)):
				os.makedirs(os.path.join('./'+self.save_directory))
		except OSError as e:
			print("Failed to create directory")
			raise

		for qu in self.download_que:
			self.writeDownloadFile(qu)

	def isEnd(self):
		return self.end