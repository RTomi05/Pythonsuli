#Készítsetek egy listát, ami 500 darab, 5 jegyű számot tartalmaz! A számok legyenek véletlenszerűek! 4 pont

import random
def parosDb(lista):
    return len([i for i in lista if i%2 == 0])
    
szamok=[random.randrange(10000,1000000) for _ in range(500)]

#print(szamok)

#Készítsetek egy függvényt (ha tudtok), ami visszaadja hogy mennyi páros van a listában(paraméterként átadva) 5 pont
#Számoljátok ki és írjátok ki (SZÉPEN, EGÉSZ MONDATBAN!) a páratlan számok összegét! Ha lehet függvénnyel. 4 pont

def paratlanOsszeg(lista):
    print("A páratlan számok összege {}".format(sum([i for i in lista if i %2 == 1])))
    

#Melyik nagyobb, a lista első felének összege, vagy a második? 4 pont

if sum(szamok[:len(szamok)//2]) > sum(szamok[:len(szamok)//2]):
    print("Az első fele nagyobb.")
elif sum(szamok[:len(szamok)//2]) > sum(szamok[:len(szamok)//2]):
    print("A második első fele nagyobb.")
else:
    print("Egyenlőek.")
    
#Mennyi 3xxxx szerű szám van? 4 pont

db=len([i for i in szamok if i//10000==3])
db=len([i for i in szamok if str(i)[0]=="3"])
db=len([i for i in szamok if str(i).startswith("3")])
print(db)

dbLista=[len([i for i in szamok if i//10000==k]) for k in range(10) ]
print(dbLista)
#Válogassátok szét az első számjegy szerint, és írjátok ki, hogy melyikből mennyi van! 4 pont

db=90
eltolas=10000
lepes=1000
import math

szam=math.floor(random.random()*db)*lepes+eltolas
print(szam)