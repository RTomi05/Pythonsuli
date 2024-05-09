from csinald import *

adatok = []

f = open("triatlon.txt", encoding="Utf8")
for egySor in f:
    adatok.append(Versenyzo(egySor.strip()))


#print(egySor)

print("2. feladat: A versenyen {} induló volt.".format(len(adatok)-1))

print("3. feladat: A verseny nyertese:")

#for egyAdat in adatok:
#    print(adatok[egyAdat].bringa)


g = open("osszidok.txt", "w")
g.write()
g.close()

f.close()