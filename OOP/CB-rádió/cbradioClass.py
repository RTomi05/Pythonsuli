class Adatok:
    def __init__(self, sor):
        #6;0;2;Laci
        vag = sor.split(";")
        self.ora = int(vag[0])
        self.perc = int(vag[1])
        self.adasDb = int(vag[2])
        self.nev = vag[3]

    def __str__(self):
        return "adat tipus"

if __name__ == "__main__":
    proba = Adatok("6;0;2;Laci")
    print(proba)