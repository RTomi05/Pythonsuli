import tkinter
import math 
import random
from tkinter.tix import Tk

#def eltolas(nev,x,y):
#    for i in range(0,len(nev),2):
#        nev[i]+=x
#        nev[i+1]+=y
#    return nev

win=Tk()

win.geometry("1200x1200")

canvas= tkinter.Canvas(win,width=1200,height=1200)
canvas.configure(bg="beige")
canvas.pack(fill=tkinter.BOTH, expand=1)
tulipan=[100,0,
         150,50,
         200,0,
         250,50,
         300,0,
         300,150,
         
         ]


canvas.create_line(tulipan,width=5, fill="green")
win.mainloop()