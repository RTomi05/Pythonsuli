from NASAClass import *

adatok = []
f = open("NASAlog.txt")
for egySor in f:
    adatok.append(Nasa(egySor.strip()))

f.close()

print("5. feladat: Kérések száma: {}".format(len(adatok)))

osszeg = 0
for egyAdat in adatok:
    osszeg += egyAdat.ByteMeret()
#print(osszeg)

print("6.feladat: Válaszok összes mérete: {} byte".format(osszeg))

darab = 0 
for egyDomain in adatok:
    if egyDomain.Domain:
        darab += 1

print("8.feladat: Domain-es kérések: {:.2%}".format(darab/len(adatok)))

stat = {}
for egyAdat in adatok:
    if egyAdat.status in stat.keys():
        stat[egyAdat.status]+=1
    else:
        stat[egyAdat.status] =1
'''  
    #másik
    try:
        stat[egyAdat.status]+=1
    except:
        stat[egyAdat.status]=1
''' 
print("9.feladat: Statisztika:")
for elem in stat:
    print("\t{}:{} db".format(elem,stat[elem]))