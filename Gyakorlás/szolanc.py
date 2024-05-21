
megy = 0
hanyadik = 1
szavak = []

while megy == 0:
    if hanyadik == 1:
        szo = input("Kérem a(z) {} szót! ".format(hanyadik))
        elozoSzo = szo
        szavak.append(szo)
        hanyadik += 1
    elif hanyadik > 1:
        elozoSzo = szo
        szo = input("Kérem a(z) {} szót! ".format(hanyadik))
        if elozoSzo[-1] == szo[0]:
            hanyadik += 1
            szavak.append(szo)
            print(szavak)
    