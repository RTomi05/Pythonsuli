lista = []
listaPot = ["alma", "Béla", "ez", "kifele", "befele", "lefele", "felfele"]
szo = "a"

print("1. feladat")
while szo != "":
    szo = input("Kérek egy szót: ")
    if szo != "":
        lista.append(szo)

if len(lista) > 0:
    print("A szavak száma: {}".format(len(lista)))
else:
    print("A szavak száma: {}".format(len(listaPot)))

print("A lista első fele: {}".format("_".join(lista[:len(lista)//2])))
