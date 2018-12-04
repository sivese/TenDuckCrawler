from tkinter import *
#from crawler import *

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
        self.exit_menu = Menu(self.toolbar)
        self.toolbar.add_cascade(label="종료", menu=self.exit_menu)

        self.name_label = Label(self.app, text="저장경로")
        self.name_label.grid(row=0, column=0)

        self.text_box = Entry(self.app)
        self.text_box.grid(row=0, column=1)

        self.get_button = Button(self.app, text="Send", command=self.crawlWebImage())
        self.get_button.grid(row=1, column=1)

        #self.image_labe = Label(image=PhotoImage(file=''))

    def clientExit(self):
        exit()

    def crawlWebImage(self):
        b = 1
    def run(self):
        self.app.mainloop()