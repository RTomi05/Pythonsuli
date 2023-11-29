import random
import math

def veletlen(mettol, meddig, lepes=1):
	darab=math.ceil((meddig-mettol)/lepes)
	eltolas=mettol
	szam=math.floor(random.random()*darab)*lepes+eltolas

	return szam

Nagyatad=[]
Budapest=[]
Pecs=[]
Szolnok=[]
Levelfalva=[]

for n in range(24):
        elozo = n
        n = veletlen(20,36)
        if n > elozo:
                Budapest.append(n)
                veletlen(20,36)
        else:
                continue
                
print("A tegnapi hőmérsékletadatok Budapestre: ",Budapest)

for n in range(24):
        n = veletlen(20,36)
        Pecs.append(n)
print("A tegnapi hőmérsékletadatok Nagyatádra: ",Pecs)

for n in range(24):
        n = veletlen(20,36)
        Szolnok.append(n)
print("A tegnapi hőmérsékletadatok Nagyatádra: ",Szolnok)

for n in range(24):
        n = veletlen(20,36)
        Levelfalva.append(n)
print("A tegnapi hőmérsékletadatok Nagyatádra: ",Levelfalva)

for n in range(24):
        n = veletlen(20,36)
        Nagyatad.append(n)
print("A tegnapi hőmérsékletadatok Nagyatádra: ",Nagyatad)
