import transzformaciok

from tkinter import *

#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("800x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="lightgray")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti

TT=[0,0,
    0,20,
    35,20,
    40,90,
    60,90,
    65,20,
    100,20,
    100,0,
    0,0]

AA=[0,0,
    0,20,
    30,20,
    40,90,
    60,90,
    70,20,
    100,20,
    100,0,
    0,0]

nevT = transzformaciok.eltol(TT,20,50)
canvas.create_line(nevT,width=5,fill="red")

nevA = transzformaciok.eltol(AA,150,50)
canvas.create_line(nevA,width=5,fill="red")


win.mainloop()