from NASAClass import *

adatok = []
f = open("NASAlog.txt")
for egySor in f:
    adatok.append(Nasa(egySor))

#print(len(adatok))
f.close()

print("5. feladat: Kérések száma: {}". format(len(adatok)))

osszeg = 0
for egyAdat in adatok:
    osszeg += egyAdat.ByteMeret()

print(osszeg)

