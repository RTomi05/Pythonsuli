import random
import math

def veletlen(mettol, meddig, lepes=1):
	darab=math.ceil((meddig-mettol)/lepes)
	eltolas=mettol
	szam=math.floor(random.random()*darab)*lepes+eltolas

	return szam

print(veletlen(10,20))

szamok=[]
for i in range(100):
	szamok.append(veletlen(10,20))	
print(szamok)

szamok=[]
b = veletlen(10,21)
for _ in range(b):
	b2=veletlen(10,21)
	temp=[]
	for _ in range(b2):
		temp.append(veletlen(160,201))
	szamok.append(temp)

print(szamok)

#szamok=[[veletlen(160,200) for _ in range(veletlen(10,21))] for _ in range(veletlen(10,21))]
print(szamok)
