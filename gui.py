from tkinter import *
from PIL import ImageTk, Image
from crawler import *

class Application:
    def __init__(self):
        self.app = Tk()
        self.app.title("TenDuck Crawler")

        #configuration for menu toolbar setting
        self.toolbar = Menu(self.app)
        self.app.config(menu=self.toolbar)

        #self.save_path = Menu(self.toolbar)
        #self.save_path.add_command(label="종료")

        #Add menu on toolbar
        self.menu = Menu(self.toolbar)
        self.menu.add_command(label="종료",command=self.clientExit)
        self.toolbar.add_cascade(label="메뉴", menu=self.menu)

        self.name_label = Label(self.app, text="검색 키워드")
        self.name_label.grid(row=0, column=0)

        self.text_box = Entry(self.app)
        self.text_box.grid(row=0, column=1)

        self.get_button = Button(self.app, text="Send", command=self.crawlWebImage)
        self.get_button.grid(row=0, column=2)

        #Image initializing
        hommy = ImageTk.PhotoImage(self.getHommyImage())

        self.image_label = Label(self.app, image=hommy)
        self.image_label.image = hommy
        self.image_label.place(x=0, y=25)

        self.app.geometry("300x325")
        self.app.resizable(False, False)

    def getHommyImage(self):
        img = Image.open('./img/hommy.jpg')
        img = img.resize((300, 300), Image.ANTIALIAS)

        return img

    def clientExit(self):
        exit()

    def crawlWebImage(self):
        crawler = OtakuCrawler()
        crawler.searchImageByKeyword(self.text_box.get())

    def run(self):
        self.app.mainloop()