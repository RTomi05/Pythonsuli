#Egyszerű Pong Játék
#Start: 2024. 01. 31.
#End: 
#Rengel Tamás


from tkinter import *


jatekHatter = "lightgray"

win=Tk()
win.geometry("600x600+100+20")
win.title("Pong játék")
canvas=Canvas(win, bg=jatekHatter)
canvas.pack(fill = BOTH, expand = 1)


canvas.create_oval(0,0,20,20, fill = "red")
win.mainloop()