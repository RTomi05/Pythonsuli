#Import the required libraries 

from tkinter import *
import math
import random

def eltol(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y
    return pontok
#nagyitas
def nagyit(pontok,x,y=-1):

	if y==-1:
		print(y) 
		for i in range(len(pontok)):
			pontok[i]*=x
	else:
		for i in range(len(pontok)):
			if i %2==0:
				pontok[i]*=x
			else:
				pontok[i]*=y
	
	return pontok
	
#forgatas fuggveny
#x'= cos αx − sin αy
#y' = sin αx + cos αy
def forgatPont(x,y,szog):
    x2=math.cos(math.radians(szog))*x - math.sin(math.radians(szog))*y
    y2=math.sin(math.radians(szog))*x + math.cos(math.radians(szog))*y
	
    return x2,y2

def forgat(lista,szog,oX=0,oY=0):
	
    lista=eltol(lista,-oX,-oY)
	
    for i in range(0,len(lista),2):
        lista[i],lista[i+1]=forgatPont(lista[i],lista[i+1],szog)
	
    lista=eltol(lista,-oX,-oY)
	
    return lista

def kozepSzamol(lista):
	x = 0
	y = 0
	for i in range(len(lista)):
		if i % 2 == 0:
			x += lista[i]
		else:
			y += lista[i]

        x = x / (len(lista)/2)
        y = y / len(lista)*2
	
    return x,y


def faSorsol(darab):
	lista=[]

	temp=[]
	temp.append(random.randint(0,1))
	temp.append(random.randint(0,600))
	temp.append(random.randint(0,600))
	temp.append(random.randint(20,30)/100)

	return lista


#create an instance of tkinter frame or window 
win=Tk()

#Set the size of the tkinter window
win.geometry("600x600")

#Create a canvas widget 
canvas = Canvas(win, width=600, height=600)
canvas.configure(bg="lightgray")
canvas.pack(fill=BOTH, expand=1) #teljes ablakot kitölti 


pontok=[0,0 ,100, 0 ,100 ,100 , 0, 100, 0,0]

#eltolás
for i in range(0,len(pontok),2):
    pontok[i]+=200
    pontok[i+1]+=100




canvas.create_line(pontok,width=5, fill="green")
pontok=eltol(pontok,100,0)
canvas.create_line(pontok,width=5, fill="green")

fenyo1=[200,0,0,400,190,400,190,500,210,500,210,400,400,400,200,0]
pontok=eltol(fenyo1,10,10)
canvas.create_line(fenyo1,width=5, fill="green")

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


fenyo2=nagyit(fenyo2,0.2,0.5)
fenyo2=forgat(fenyo2,90)
fenyo2=eltol(fenyo2,200,100)
canvas.create_line(fenyo2,width=5, fill="darkgreen")



win.mainloop()


