#1. feladat:
class Szovegkezeles:
    def __init__(self):
        self.szoveg = 0
        self.szam = 0

    def bekertSzoveg(self):
        while True:
            self.szoveg = input("Kérek egy szöveget: ")
            if self.szoveg.strip():
                break
            else:
                print("ADD MÁR MEG!")

    def bekertSzam(self):
        while True:
            szamBekeres = input("Kérek egy egész számot: ")
            if szamBekeres.isdigit():
                self.szam = int(szamBekeres)
                break
            else:
                print("Ez nem egy egész szám!")

    def kiirandoKarakter(self):
        if self.szam < 0 or self.szam >= len(self.szoveg):
            print("Sajnos nincs ilyen betű.")
        else:
            karakter = self.szoveg[self.szam]
            print(karakter * self.szam)

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