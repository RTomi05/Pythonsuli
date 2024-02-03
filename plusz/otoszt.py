
#Írjon programot, amely kiírja 5 többszöröseit 100-tól – 200-ig. 

actual = 95

szamok = []
while actual < 200:
    actual = actual + 5
    szamok.append(actual)

print(szamok)



#VAGY

szamok = []

actual = 99
while actual < 200:
    actual = actual + 1
    if actual %5 == 0:
        szamok.append(actual)

print(szamok)
    
