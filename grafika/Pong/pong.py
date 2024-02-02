#Egyszerű Pong Játék
#Start: 2024. 01. 31.
#End: 
#Rengel Tamás


from tkinter import *


jatekHatter = "lightgray"

win = Tk()
win.geometry("600x600+100+20")
win.title("Pong játék")
canvas=Canvas(win, bg=jatekHatter)
canvas.pack(fill = BOTH, expand = 1)


canvas.create_oval(0,0,100,100, fill = "red")

labdaSpeed = [1,1]
labdaPos = [200,200]
labdaSize = 50

while True:

    labdaPos[0] += labdaSpeed[0]
    labdaPos[1] += labdaSpeed[1]

    if labdaPos[0] > win.winfo_width() or labdaPos[0] < 0:
        labdaSpeed[0]*= -1
    if labdaPos[1] > win.winfo_height() or labdaPos[1] < 0:
        labdaSpeed[1]*= -1    


    canvas.create_oval(labdaPos[0], labdaPos[1], labdaPos[0] + labdaSize, labdaPos[1] + labdaSize, fill = "red")
    canvas.update()


win.mainloop()