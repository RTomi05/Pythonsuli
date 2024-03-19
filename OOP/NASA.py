<<<<<<< HEAD
from NASAclass import *
=======
from NASAClass import *
>>>>>>> 4ca3186d9881e346429529c94788fd8db259a1a0

adatok = []
f = open("NASAlog.txt")
for egySor in f:
<<<<<<< HEAD
    adatok.append(nasa(egySor.strip("\n")))
=======
    adatok.append(Nasa(egySor))
>>>>>>> 4ca3186d9881e346429529c94788fd8db259a1a0

#print(len(adatok))
f.close()

<<<<<<< HEAD
print("5. feladat: Kérések száma: {}".format(len(adatok)))
=======
print("5. feladat: Kérések száma: {}". format(len(adatok)))
>>>>>>> 4ca3186d9881e346429529c94788fd8db259a1a0

osszeg = 0
for egyAdat in adatok:
    osszeg += egyAdat.ByteMeret()

<<<<<<< HEAD
print("6. feladat: Válaszok összes mérete: {} byte".format(osszeg))

darab = 0
for egyAdat in adatok:
    if egyAdat.Domain:
        darab += 1

print("8. feladat: Domain-es kérések: {:.2%}".format(darab / len(adatok)))

stat = {}
for egyAdat in adatok:
    if egyAdat.status in stat.keys():
        stat[egyAdat.status] += 1
    else:
        stat[egyAdat.status] = 1

    #másik
    #try:
    #    stat[egyAdat.status] += 1
    #except:
    #    stat[egyAdat.status] = 1

print("9. feladat: Statisztika:")
for elem in stat:
    print("\t{}: {} db".format(elem, stat[elem]))
=======
print(osszeg)

>>>>>>> 4ca3186d9881e346429529c94788fd8db259a1a0
