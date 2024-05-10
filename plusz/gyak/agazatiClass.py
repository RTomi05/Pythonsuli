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