#Készítette: Rengel Tamás

#A feladat a fob2016 alapján készült.

adatok = []

f = open("fob2016.txt")
for sor in f:
    adatok.append(sor.strip().split(";"))
    
f.close()

for i in range(len(adatok)):
    adatok[i][3] = int(adatok[i][3])
    adatok[i][4] = int(adatok[i][4])
    adatok[i][5] = int(adatok[i][5])
    adatok[i][6] = int(adatok[i][6])
    adatok[i][7] = int(adatok[i][7])
    adatok[i][8] = int(adatok[i][8])
    adatok[i][9] = int(adatok[i][9])
    adatok[i][10] = int(adatok[i][10])

print(adatok)