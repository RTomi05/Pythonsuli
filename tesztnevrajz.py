import transzformaciok

from tkinter import *

#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("600x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="lightgray")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti

fenyo2=[200,0,
        0,100,
        150,100,
        0,200,
        150,200,
        0,300,
        150,300,
        150,400,
        250,400,
        250,300,
        400,300,
        250,200,
        400,200,
        250,100,
        400,100,
        200,0]


fenyo2Masolat = transzformaciok.eltol(fenyo2,100,100)
canvas.create_line(fenyo2Masolat,width=5,fill="green")


win.mainloop()