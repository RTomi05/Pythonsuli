class Versenyzo:
    def __init__(self,sor):
        vag = sor.split(";")
        self.nev = vag[0]
        self.nem = vag[1]
        self.szul = vag[2]
        self.uszas = vag[3]
        self.bringa = vag[4]
        self.futas = vag[5]
        self.rajtszam = vag[6]