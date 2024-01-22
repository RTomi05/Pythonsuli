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

TT2=[0,0,
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
    35,20,
    40,90,
    60,90,
    65,20,
    100,20,
    100,0,
    0,0]


TT3 = []
for e in TT2:
	e = transzformaciok.nagyit(e,10)
	e = transzformaciok.eltol(e,100,100)
	#e = transzformaciok.forgat(e,45)
    
	TT3.append(e)


for e in TT3:
	canvas.create_line(e,width=5,fill="red")



nevT = transzformaciok.eltol(TT,20,50)
canvas.create_line(nevT,width=5,fill="red")
nevT = transzformaciok.eltol(TT2,20,50)
canvas.create_line(nevT,width=5,fill="red")

nevA = transzformaciok.eltol(AA,150,50)
canvas.create_line(nevA,width=5,fill="red")






win.mainloop()