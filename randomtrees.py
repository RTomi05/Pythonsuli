
from tkinter import *
import math
import random

def eltol(pontok,x,y):
    for i in range(0, len(pontok),2):
        pontok[i] += x
        pontok[i+1] += y
    return pontok

win=Tk()
win.geometry("600x600")

canvas=Canvas(win, width = 600, height = 300)
canvas.configure(bg = "white")
canvas.pack(fill = BOTH, expand = 1)

pontok=[0, 0, 100, 0, 100, 100, 0, 100, 0, 0]

for i in range(0, len(pontok),2):
    pontok[i] += 200
    pontok[i+1] += 100

canvas.create_line(pontok, width = 5, fill = "green")

pontok=eltol(pontok,0,100)

win.mainloop()