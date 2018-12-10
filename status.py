from tkinter import *
import tkinter.ttk

class StatusBar:
	def __init__(self):
		self.dialog = Tk()
		self.dialog.title("작업 현황")
		self.dialog.geometry("400x150+50+50")
		self.dialog.resizable(False,False)

		self.status_label = Label(text="")
		self.status_label.place(x=50, y=50)

		self.progress = tkinter.ttk.Progressbar(self.dialog, maximum=100, mode="indeterminate")
		self.progress.place(x=180, y=50)
		self.dialog.protocol("WM_DELETE_WINDOW", self.disableClose)
		self.dialog.mainloop()

	def disableClose(self):
		pass

	def exit(self):
		self.dialog.destroy()

	def setStatusText(self, text):
		self.status_label.configure(text=text)
