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
for egyAdat in lista:
    if elozo == egyAdat.vendeg:
        temp += 1
    else:
        if temp == 4:
            darab += 1
        elozo = egyAdat.vendeg
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
print("{}. vendég {}".format(legtobbIdoVendeg,idoVissza(legtobbIdo)))


#hf idővisszaváltás kétszámjegyre 0-tól 9-ig (formázott kiiratás str)