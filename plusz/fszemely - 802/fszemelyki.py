from datetime import date

print("Rengel Tamás", date.today(), "10.B")
print("Ez a program emberek adatait tárolja el egy fájlban.")
ism = int(input(print("Kérem adja meg, hány ember adatait szeretné bekérni: ")))
print("A műveletet {} alkalommal fogjuk ismételni.".format(ism))
elvegzett = 0

def bekero():
    global elvegzett
    global adatok
    while elvegzett != ism:
        actual = []
        sorszam = input("Adja meg a sorszámot! ") + ";"
        nev = input("Adja meg a nevet! ") + ";"
        telepules = input("Adja meg a települést! ") + ";"
        cim = input("Adja meg a címet! ") + ";"
        haviJ = input("Adja meg a havi jövedelmet! ") + ";"

        actual.append(sorszam + nev + telepules + cim + haviJ)
        adatok = ",".join(str(egyAdat) for egyAdat in actual)
        print(adatok)
        elvegzett += 1

        if elvegzett == 1:
            f = open("szemely.txt", "w")
            f.write(adatok)
            f.write("\n")
            f.close()

        else:
            f1 = open("szemely.txt", "a")
            f1.write(adatok)
            f1.write("\n")
            f1.close()
            bekero()

bekero()    
print("Köszönjük, hogy használta a programot!\nKérem, ellenőrizze az elkészült fájlt!")