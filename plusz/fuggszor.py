
#Készítsen függvényt, amely bekér két számot, majd visszaadja azok szorzatát.

def szamolj(szorzat):
    szam1 = float(input("Első szám: "))
    szam2 = float(input("Második szám: "))
    szorzat = szam1 * szam2
    return szorzat

szorzat = 0
print(szamolj(szorzat))

#VAGY

def szamolj2():
    szam1 = float(input("Első szám: "))
    szam2 = float(input("Második szám: "))
    return szam1 * szam2

print(szamolj2())