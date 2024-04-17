import furdoClass as fc

def idoVissza(mp):
    ora = mp // (60*60)
    perc = mp % 3600 // 60
    masodperc = mp % 3600 % 60
    return str(ora) + ":" + str(perc) + ":" + str(masodperc)

f = open("furdoadat.txt")
lista = []
for egySor in f:
    lista.append(fc.Furdoclass(egySor))
f.close()
print("2.feladat:")
print("Az első vendég {}-kor lépett ki az öltözőből".format(lista[0].ido()))


utolso = lista[0]
for egyElem in lista:
    if not egyElem.belepett and egyElem.reszleg == 0:
        utolso = egyElem 
print("Az utolsó vendég {}-kor lépett ki az öltözőből".format(utolso.ido()))

darab = 0
elozo = -1
temp = 1
for egyElem in lista:
    if elozo == egyElem.vendeg:
        temp += 1
    else:
        if temp == 4:
            darab += 1
        elozo = egyElem.vendeg
        temp = 1

print("3. feladat")
print("A fürdőben {} vendég járt 1 részlegen".format(darab))

kezdoIdo = 0
legtobbIdo = 0
legtobbIdoVendeg = 0
for egyElem in lista:
    if egyElem.belepett and egyElem.reszleg == 0:
        bentiIdo = egyElem.idoMp() - kezdoIdo
        if bentiIdo > legtobbIdo:
            legtobbIdo = bentiIdo
            legtobbIdoVendeg = egyElem.vendeg

    if not egyElem.belepett and egyElem.reszleg == 0:
        kezdoIdo = egyElem.idoMp()

print("4. feladat")
print("A legtöbb időt eltöltött vendég: ")
#if len(idoVissza(legtobbIdo)) == 7:
#    print("Szia")
print(idoVissza(legtobbIdo))
print("{}. vendég {}".format(legtobbIdoVendeg,idoVissza(legtobbIdo)))

stat = [0,0,0]

for egyElem in lista:
    if egyElem.reszleg == 0 and not egyElem.belepett:
        if egyElem.ora < 9:
            stat[0] += 1
        elif egyElem.ora < 16:
            stat[1] += 1
        else:
            stat[2] += 1

print("5. feladat")
print("6-9 óra között {} vendég".format(stat[0]))
print("9-16 óra között {} vendég".format(stat[1]))
print("16-20 óra között {} vendég".format(stat[2]))
#VAGY
#print("6-9 óra között {} vendég\n9-16 óra között {} vendég\n16-20 óra között {} vendég\n".format(*stat))

szaunastat = {}
temp = 0
for egyElem in lista:
    if egyElem.reszleg == 2:
        if egyElem.belepett:
            temp = egyElem.idoMp()
        else:
            szaunastat[egyElem.vendeg] += egyElem.idoMp() - temp

#hf idővisszaváltás kétszámjegyre 0-tól 9-ig (formázott kiiratás str)