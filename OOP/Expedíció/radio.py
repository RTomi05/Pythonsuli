import radioClass as rc

f = open("veetel.txt")
sorszam = 0
tempSor = ""
uzenetek = []

for egySor in f:
    if sorszam %2 == 0:
        tempSor = egySor
    else:
        uzenetek.append(rc.Uzenet(tempSor, egySor))

    sorszam += 1
    #radiátor továbbképzés
      
f.close()

print("2. feladat")
print("Az első üzenet rögzítője: {}".format(uzenetek[0].amator))
print("Az utolsó üzenet rögzítője: {}".format(uzenetek[-1].amator))
#bűzjelző

print("\n3. feladat")
for egyUzenet in uzenetek:
    if egyUzenet.farkasKereso():
        print("{}. nap {}. rádióamatőr".format(egyUzenet.nap,egyUzenet.amator))


napok = []


while len(napok) < 11:
    tempNap = rc.Nap(len(napok)+1)
    for egyUzenet in uzenetek:
        if egyUzenet.nap == len(napok)+1:
            tempNap.hozzaAd(egyUzenet)
    napok.append(tempNap)

#másik megoldás

#napok = []

#for i in range(1,12):
#    tempNap = rc.Nap(i)
#    for egyUzenet in uzenetek:
#        if egyUzenet.nap ==i:
#            tempNap.hozzaAd(egyUzenet)
#napok.append(tempNap)

print("4. feladat")
for egyNap in napok:
    print("{}.nap {} rádióamatőr".format(egyNap.nap,egyNap.uzenetSzam()))
    #print(f"{egyNap.nap}.nap {egyNap.uzenetSzam()} rádióamatőr")

print(napok[2].helyreallit())

f = open("adaas.txt", "w")
for egyNap in napok:
    f.write(egyNap.helyreallit())
f.close()


