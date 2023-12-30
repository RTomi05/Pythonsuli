
#Készítsen függvényt, amely bekér két számot, majd összeadja azok értékét, az eredményt pedig visszaadja. 

def szamolj(osszeg):
    szam1 = float(input("Első szám: "))
    szam2 = float(input("Második szám: "))
    osszeg = szam1 + szam2
    return osszeg

osszeg = 0
print(szamolj(osszeg))

#VAGY

def szamolj2():
    szam1 = float(input("Első szám: "))
    szam2 = float(input("Második szám: "))
    return szam1 + szam2

print(szamolj2())