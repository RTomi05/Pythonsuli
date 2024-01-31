import transzformaciok

from tkinter import *

#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("920x410")

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

A2Vonalka1=[320,250,
          375,250,
          ]

AVonalka2=[330,220,
           370,220,
          ]

A2Vonalka2=[330,220,
           370,220,
          ]

Mkulso=[440,282,
        440,97,
        510,160,
        580,97,
        580,282
        ]

Mbelso=[438,282,
        450,282,
        450,120,
        510,180,
        570,120,
        570,282,
        583,282]

ekezet=[650,50,
        660,90,
        680,90,
        670,50,
        650,50]

SS = [810,90,
      750,90,
      750,180,
      810,180,
      810,270,
      750,270,
      750,280,
      825,280,
      825,165,
      760,165,
      760,105,
      825,105,
      825,90,
      800,90
      ]


hatter="#ffffff"
betuszinek=["red",hatter,"blue"]



#eredeti megtartása (copy)
A2szele = transzformaciok.masol(ASzele)
A2szele = transzformaciok.eltol(A2szele,320,0)
A2kozepe = transzformaciok.masol(AKozepe)
A2kozepe = transzformaciok.eltol(A2kozepe,320,0)
A2Vonalka1 = transzformaciok.eltol(A2Vonalka1,320,0)
A2Vonalka2 = transzformaciok.eltol(A2Vonalka2,320,0)



#tamas = TT + ASzele + AKozepe + AVonalka1 + A2Vonalka1 + AVonalka2 + A2Vonalka2 + Mkulso + Mbelso + ekezet + SS
#print(tamas)




for e in TT:
    e = transzformaciok.eltol(e,40,50)
    e = transzformaciok.nagyit(e,2)
    e = transzformaciok.forgat(e,45)


for e in TT:
    e = transzformaciok.forgat(TT,0.1)
    canvas.create_line(e,width=5,fill="green")

canvas.create_line(ASzele,width=5,fill="red")
canvas.create_line(AKozepe,width=5,fill="red")
canvas.create_line(AVonalka1,width=5,fill="red")
canvas.create_line(AVonalka2,width=5,fill="red")
canvas.create_line(Mkulso,width=5,fill="red")
canvas.create_line(Mbelso,width=5,fill="red")
canvas.create_line(A2szele,width=5,fill="red")
canvas.create_line(A2kozepe,width=5,fill="red")
canvas.create_line(A2Vonalka1,width=5,fill="red")
canvas.create_line(A2Vonalka2,width=5,fill="red")
canvas.create_line(ekezet,width=5,fill="blue")
canvas.create_line(SS,width=5,fill="red")



while True:
    TT = transzformaciok.forgat(TT,1)

    #for i,e in enumerate(TT):
        #d = canvas.create_line(TT,width=5,fill="red")
        #canvas.create_polygon(e, fill="betuszinek[i]", outline="blue")
    win.update_idletasks()
    win.update()
#win.mainloop()
