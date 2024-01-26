import transzformaciok

from tkinter import *

#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("1200x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="lightgray")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti

TT=[[0,0,
    0,20,
    35,20,
    40,90,
    60,90,
    65,20,
    100,20,
    100,0,
    0,0],
    [0,0,
    0,20,
    35,20,
    40,90,
    60,90,
    65,20,
    100,20,
    100,0,
    0,0]]

ASzele=[302,280,
    350,100,
    400,280,
    403,280
    ]

AKozepe=[300,280,
    315,280,
    350,120,
    380,280,
    403,280
    ]

AVonalka1=[320,250,
          375,250,
          ]

AVonalka2=[330,220,
           370,220,
          ]


hatter="#ffffff"
betuszinek=["red",hatter,"blue"]



#eredeti megtartása (copy)
A2 = transzformaciok.masol(ASzele)



TT2=[]
for e in TT:
    e = transzformaciok.eltol(e,40,50)
    e = transzformaciok.nagyit(e,2)
    TT2.append(e)
	
for e in TT2:
   canvas.create_line(e,width=5,fill="red")


canvas.create_line(ASzele,width=5,fill="red")
canvas.create_line(AKozepe,width=5,fill="red")
canvas.create_line(AVonalka1,width=5,fill="red")
canvas.create_line(AVonalka2,width=5,fill="red")




while True:
    canvas.delete("all")
    TT = transzformaciok.forgat(TT,0.1)

    for i,e in enumerate(TT2):
        #d = canvas.create_line(TT2,width=5,fill="red")
        canvas.create_polygon(e, fill="betuszinek[i]", outline="blue")
    win.update_idletasks()
    win.update()
    #win.mainloop()
