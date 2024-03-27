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

tempNap = rc.Nap(1)
for egyUzenet in uzenetek:
    pass