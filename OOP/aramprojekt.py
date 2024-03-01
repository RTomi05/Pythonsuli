
class Jel:
	x = 0
	y = 0
	meret = 100
	szin = "black"
	def __init__(self, x, y, meret, canvas):
		self.x = x
		self.y = y
		self.meret = meret
		self. r = self.meret * 0.06
		#bekötési pont by Taki
		self.bkp = [[self.x, self.y + self.meret * 0.5], [self.x + self.meret, self.y + self.meret * 0.5]]

		self.canvas = canvas
		self.rajz()


	def rajz(self, vonalak = [], korok = []):
		self.canvas.create_rectangle(self.x, self.y, self.x + self.meret, self.y + self.meret, fill = "gray")

		for egyVonal in vonalak:
			self.canvas.create_line(egyVonal, width = self.meret * 0.03, fill = self.szin)
			
		for egyKor in korok:
			self.canvas.create_oval(egyKor, outline = self.szin, width = self.meret * 0.03)


	def vezetek(self, masik, sajatBKP = 1, masikBKP = 0):
		vonalak = [
			[
				self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
				masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
			],
		]
		
		for egyVonal in vonalak:
			self.canvas.create_line(egyVonal, width = self.meret * 0.03, fill = self.szin)


class Elem(Jel):
	def rajz(self):
		vonalak = [
			[
				self.x, self.y + self.meret * 0.5,
				self.x + self.meret * 0.45, self.y + self.meret * 0.5,
			],
			[
				self.x + self.meret * 0.45, self.y + self.meret * 0.2,
				self.x + self.meret * 0.45, self.y + self.meret * 0.8,
			],
			[
				self.x + self.meret * 0.55, self.y + self.meret * 0.4,
				self.x + self.meret * 0.55, self.y + self.meret * 0.6,
			],
			[
				self.x + self.meret * 0.55, self.y + self.meret * 0.5,
				self.x + self.meret * 1.00, self.y + self.meret * 0.5,
			],
		]
		Jel.rajz(self, vonalak)
		
class Kapcsolo(Jel):
	def rajz(self):
		vonalak = [
			[
				self.x, self.y + self.meret * 0.5,
				self.x + self.meret * 0.333 - self.r, self.y + self.meret * 0.5,
			],
			[
				self.x + self.meret * 0.333 + self.r, self.y + self.meret * 0.5,
				self.x + self.meret * 0.666 - self.r, self.y + self.meret * 0.3,
			],
			[
				self.x + self.meret * 0.666 + self.r, self.y + self.meret * 0.5,
				self.x + self.meret * 1.00, self.y + self.meret * 0.5,
			],
		]
		
		korok = [
			[self.x + self.meret * 0.333 - self.r, self.y + self.meret * 0.5 - self.r,
			self.x + self.meret * 0.333 + self.r, self.y + self.meret * 0.5 + self.r
			],
			[self.x + self.meret * 0.666 - self.r, self.y + self.meret * 0.5 - self.r,
			self.x + self.meret * 0.666 + self.r, self.y + self.meret * 0.5 + self.r
			],
		]

		Jel.rajz(self, vonalak, korok)

class Lampa(Jel):
	def rajz(self):
		
		self.r = self.meret * 0.2
		dx = self.r / math.sqrt(2)
		vonalak = [
			[
				self.x, 						self.y + self.meret * 0.5,
				self.x + self.meret * 0.5 - self.r, self.y + self.meret * 0.5,
			],
			[
				self.x + self.meret * 0.5 - dx, self.y + self.meret * 0.5 - dx,
				self.x + self.meret * 0.5 + dx, self.y + self.meret * 0.5 + dx,
			],
			[
				self.x + self.meret * 0.5 - dx, self.y + self.meret * 0.5 + dx,
				self.x + self.meret * 0.5 + dx, self.y + self.meret * 0.5 - dx,
			],
			[
				self.x + self.meret * 0.5 + self.r, self.y + self.meret * 0.5,
				self.x + self.meret * 1.00, self.y + self.meret * 0.5,
			],
		]
		
		korok = [
			[
				self.x + self.meret * 0.5 - self.r, 	self.y + self.meret * 0.5 - self.r,
				self.x + self.meret * 0.5 + self.r, 	self.y + self.meret * 0.5 + self.r
			],
		]

		Jel.rajz(self, vonalak, korok)


class Ellenallas(Jel):
	def rajz(self):

		vonalak = [
			[
				self.x, 	self.y + self.meret * 0.5,
				self.x + self.meret * 0.25,	 	self.y + self.meret * 0.5,
			],

			[
				self.x + self.meret * 0.25,		self.y + self.meret * 0.4,
				self.x + self.meret * 0.25,	 self.y + self.meret*0.6,
				self.x + self.meret * 0.75,	 self.y + self.meret*0.6,
				self.x + self.meret * 0.75,	 self.y + self.meret*0.4,
				self.x + self.meret * 0.25,		self.y + self.meret * 0.4,
			],
			[
				self.x + self.meret * 0.75,		self.y + self.meret * 0.5,
				self.x + self.meret * 1.0,	 	self.y + self.meret*0.5,
			]

		]
		
		Jel.rajz(self,vonalak)

from tkinter import *
import math

win=Tk()
win.geometry("600x620+100+20")
win.title("Áramkör 10.B/1 2024")
canvas = Canvas(win, bg = "white")

canvas.pack(fill = BOTH, expand = 1)


elem1 = Elem(0, 0, 100, canvas)
#elem1.rajz()

elem2 = Elem(200, 100, 50, canvas)
#elem2.rajz()
#elem2.szin = "red"
#elem2.rajz()
kapcsolo1 = Kapcsolo(350, 150, 100, canvas)
lampa1 = Lampa(0, 150, 100, canvas)
ellenallas1 = Ellenallas(500,150,100, canvas)

kapcsolo1.vezetek(ellenallas1)
win.mainloop()