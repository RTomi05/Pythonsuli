
def haromszog():

    global szamok
    szamok = []
    while len(szamok) == 0:
        try:
            szam1 = int(input("A háromszög első oldala: "))
            szamok.append(szam1)
        except:
            print("Ez nem egész szám!")

    while len(szamok) < 2:
        try:
            szam2 = int(input("A háromszög második oldala: "))
            szamok.append(szam2)
        except:
            print("Ez nem egész szám!")

    while len(szamok) < 3:
        try:
            szam3 = int(input("A háromszög harmadik oldala: "))
            szamok.append(szam3)
        except:
            print("Ez nem egész szám!")

    print(szamok)

    adatsor()


def adatsor():
    if adatok1 == []:
        adatok1 = szamok
        elso = 1
    elif adatok2 == [] and elso == 1:
        adatok2 = szamok
    else:
        adatok3 = szamok

    print(adatok1,adatok2,adatok3)




