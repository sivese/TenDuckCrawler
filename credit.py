from tkinter import *
import webbrowser

class Credit:
	def __init__(self):
		self.credit = Tk()
		self.credit.title("만든이")
		self.credit.geometry("250x150")
		self.credit.resizable(False, False)

		my_name = Label(self.credit, text="\n만든이:Sivese")
		my_name.pack()

		link = Label(self.credit, text="https://github.com/sivese", fg="blue", cursor="hand2")
		link.pack()
		link.bind("<Button-1>", self.toGit)

		description = Label(self.credit, text="\n픽시브에서 이미지를 자동으로 긁어오는 \n프로그램입니다. 버그 및 문의는 \ncodersivese@gmail.com로 해주세요.")
		description.pack()

	def toGit(self, event):
		webbrowser.open_new(event.widget.cget("text"))

	def show(self):
		self.credit.mainloop()