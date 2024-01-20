import random

nevDb=100

vNev=("Nagy", "Kiss", "Horváth", "Kovács", "Bogdán", "Lakatos", "Fazekas")
kNev=(
    ("Rikárdó","Leonidász","Naruto","Béla", "István"),
	("Rozalinda", "Marika","Piroska","Aranka","Britni")
	)
nevLista=[]

nem=random.randrange(2)
tempNev=random.choice(vNev) + " " + random.choice(kNev[nem])
if random.randrange(0,3) == 0:
    tempNev+= " " + random.choice(kNev[nem])
nevLista.append(tempNev)


print(nevLista)


