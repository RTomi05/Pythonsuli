
def szavakhoz():
    global szo
    while szo != "vége":
        szo = input("Adjon meg egy maximum 12 karakteres szót: ")
        if " " not in szo:
            if len(szo) < 13:
                szavak.append(szo)
            else:
                print("Nem megfelelő!")

        else:
            print("Nem jó.")
    del szavak[-1]
    return print(szavak)

szavak = []
szo = ""

szavakhoz()

paros = []
paratlan = []

for egySzo in szavak:
    if len(egySzo) %2 == 0:
        paros.append(egySzo)
    else:
        paratlan.append(egySzo)

print("A páratlan szavak listája:", paratlan)
print("A páros szavak listája", paros)

if len(paros) > len(paratlan):
    print("A páros szavakból van több.")
elif len(paros) < len(paratlan):
    print("A páratlanból van több.")
else:
    print("A páros és páratlan szavak száma egyenlő.")

szavak.sort()
for egySzo in szavak:
    if len(egySzo) == 6:
        print("Az első hatbetűs szó ABC rendben: {}".format(egySzo))
        break
    else:
        print("Nincs hatbetűs szó a szavak között.")

betuSzam = 0
for egySzo in szavak:
    betuSzam += len(egySzo)

print("A bekérés során megadott szavak betűinek száma: {}".format(betuSzam))