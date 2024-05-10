

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