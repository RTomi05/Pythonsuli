class elem:
	x = 0
	y = 0
	meret = 100
	def __init__(self,x, y, meret, canvas):
		self.x = x
		self.y = y
		self.meret = meret
		self.canvas = canvas
		self.rajz()

	def rajz(self):
		self.canvas.create_rectangle(self.x, self.y, self.x + self.meret, self.y + self.meret, fill = "red")
		vonalak = [
			[
				self.x, self.y + self.meret * 0.5,
				self.x + self.meret * 0.45, self.y + self.meret * 0.5, 
			],
		]
		for egyVonal in vonalak:
			self.canvas.create_line(egyVonal)

from tkinter import *


win=Tk()
win.geometry("600x620+100+20")
win.title("Áramkör 10.B/1 2024")
canvas = Canvas(win, bg = "white")

canvas.pack(fill = BOTH, expand = 1)


elem1 = elem(0, 0, 100, canvas)
#elem1.rajz()

elem2 = elem(200, 100, 50, canvas)
#elem2.rajz()

win.mainloop()