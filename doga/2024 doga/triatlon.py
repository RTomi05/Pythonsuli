
from triClass import *

def idoVissza(mp):
    ora = mp // (60*60)
    perc = mp % 3600 // 60
    masodperc = mp % 3600 % 60
    return "{:02}:{:02}:{:02}".format(ora,perc,masodperc)
    return str(ora) + ":" + str(perc) + ":" + str(masodperc)

adatok = []
f = open("triatlon.txt", "r")
for egySor in f:
    adatok.append(Versenyzo(egySor.strip()))

#print(egySor)

print("2. feladat: A versenyen {} induló volt.".format(len(adatok)-1))
print("3. feladat: A verseny nyertese: ")
print("\tBudai Krisztina")

#for egySor in adatok:
#    print("egySor")

ido = []
ido = adatok[3]
print(ido)

g = open("osszidok.txt", "w")
g.write(egySor)
g.close()
f.close()