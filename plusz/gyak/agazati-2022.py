#Kérjen be egy szöveget, majd egy egész számot! A második bekérést addig ismételje, amíg nem
#számot kap! Hiba esetén legyen hibaüzenet. A bekért szöveg annyiadik karakterét írja ki annyiszor,
#amennyi a szám.
from agazatiClass import *

#1. feladat:
#print("1. feladat")
#elsoFeladat = Szovegkezeles()
#elsoFeladat.bekertSzoveg()
#elsoFeladat.bekertSzam()
#elsoFeladat.kiirandoKarakter()

#Egy triatlon versenyen 3 versenyszámban teljesítenek különböző távokat az indulók. A
#triatlon.txt tartalmazza a verseny végeredményét, amit minden induló befejezett.

#A forrás első sora az adatok fejlécét tartalmazza. Az adatsorok pontosvesszővel vannak elválasztva, és
#a következők: az induló neve, férfi-e vagy nő, mikor született, az úszás, a kerékpározás, a futás
#időeredménye óó:pp:mp formátumban, és a rajtszám. A forrás a rajtszám sorrendjében került
#rögzítésre.
#A feladat megoldásához használjon OOP megoldásokat! A kiírásokat a minta szerint végezze.
#1. Töltse be a file adatait, és tárolja el egy adatszerkezetben, amivel a következő feladatokat meg
#tudja oldani.
#2. Hány versenyző indult a versenyen?
#3. A verseny nyertese, aki legrövidebb idő alatt teljesítette mind a három számot. Keresse meg, ki lett
#a nyertes, akinek a neve, a rajtszáma, és az összesített ideje jelenjen meg, a minta szerint.
#4. Hozzon létre egy osszidok.txt nevű file-t, amibe az indulók rajtszáma, neve, és az összesített
#ideje kerüljön.

versenyzok = []
class Versenyzo:
    def __init__(self, nev, nem, szuletesnap, uszas, kerekpar, futas, rajtszam):
        self.nev = nev
        self.nem = nem
        self.szuletesnap = szuletesnap
        self.uszas = uszas
        self.kerekpar = kerekpar
        self.futas = futas
        self.rajtszam = rajtszam

    def __str__(self):
        return f"{self.nev} ({self.nem}), született: {self.szuletesnap}, uszás: {self.uszas}, kerékpár: {self.kerekpar}, futás: {self.futas}, rajtszám: {self.rajtszam}"

    def osszIdo(self):
        return sum(int(t.split(":")[0]) * 3600 + int(t.split(":")[1]) * 60 + int(t.split(":")[2]) for t in [self.uszas, self.kerekpar, self.futas])

f=open("triatlon.txt", "r")
next(f)

for egySor in f:
    adat = egySor.strip().split(";")
    nev, nem, szuletesnap, uszas, kerekpar, futas, rajtszam = adat
    versenyzok.append(Versenyzo(nev, nem, szuletesnap, uszas, kerekpar, futas, rajtszam))

f.close()

induloVersenyzo = len(versenyzok)

print("2. feladat: A versenyen "+str(induloVersenyzo)+ " induló volt.")

nyertes = min(versenyzok, key=Versenyzo.osszIdo)

print("3. feladat: A verseny nyertese:")
print("neve:", nyertes.nev)
print("rajtszáma:", nyertes.rajtszam)
osszIdo = nyertes.osszIdo()
print("összideje: " + str(osszIdo // 3600) + ":" + str((osszIdo % 3600) // 60) + ":"+ str(osszIdo % 60))

f=open("osszidok.txt", "w")

for versenyzo in versenyzok:
    ossz_ido = versenyzo.osszIdo()  # Számoljuk az összidőt
    f.write(f"{versenyzo.rajtszam};{versenyzo.nev};{ossz_ido // 3600}:{(ossz_ido % 3600) // 60}:{ossz_ido % 60}\n")

f.close()