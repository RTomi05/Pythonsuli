
szoveg = ""
szam = ""
jo = 0
teszt = 0

szoveg = input("Kérek egy szöveget: ")
while jo == 0:
    try:
        szam = int(input("Kérek egy egész számot: "))
        jo += 1
    except:
        print("Ez nem egész szám!")

while teszt == 0:
    try:
        print(szam * szoveg[szam])
        teszt += 1
    except:
        print("Sajnos nincs ilyen betű.")
        teszt += 1
