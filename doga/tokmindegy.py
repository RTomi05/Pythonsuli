
import random

haromJ = []
szam = 1

#függvény és bekérés

def csinaldmar():
    global szam
    while szam != 0:
        szam = int(input("Adjon meg egy háromjegyű számot: "))
        if len(str(szam)) == 3:
            haromJ.append(szam)
        else:
            print("Nem megfelelő vagy 0!")

    return print(haromJ)

csinaldmar()

#páros / páratlan

paros = []
paratlan = []

for egySzam in haromJ:
    if egySzam %2 == 0:
        paros.append(egySzam)
    else:
        paratlan.append(egySzam)

print("A páratlan szavak listája: {}".format(paratlan))
print("A páros szavak listája: {}".format(paros))

#len megtekintés

if len(paratlan) > len(paros):
    print("A páratlan számokból van több.")
elif len(paratlan) < len(paros):
    print("A páros számokból van több.")
else:
    print("A páratlan és páros számok darabszáma egyenlő.")

#véletlen számok

veletlenLista = []

while len(veletlenLista) < 1001:
    randomSzam = random.randint(1000,9999)
    veletlenLista.append(randomSzam)

print("Az 1000 véletlen számot tartalmazó lista:")
print(veletlenLista)

#osztók

for ranSzam in veletlenLista:
    for inpSzam in haromJ:
        if (ranSzam / inpSzam) %2 == 0:
            print("A véletlen szám: {}, osztója {}.".format(ranSzam,inpSzam))
