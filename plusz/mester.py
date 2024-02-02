
#Kérjen be mondatokat „vége” végjelig.
#Rengel Tamás

szo = ""

nev = ""
nev = input("Adja meg a felhasználónevét! ")
print("Üdvözöllek,",nev)
while True:
    if szo != "vége":
        szo = input("Írjon be egy mondatot: ")
    else:
        exit()
