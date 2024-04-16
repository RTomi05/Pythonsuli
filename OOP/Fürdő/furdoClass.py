class Furdoclass:
    def __init__(self,sor):
        vagas = sor.split(" ")
        self.vendeg = int(vagas[0])
        self.reszleg = int(vagas[1])
        self.belepett = vagas[2]== "0"
        self.ora = int(vagas[3])
        self.perc = int(vagas[4])
        self.masodperc = int(vagas[5])

    def ido(self):
        return ":".join([str(self.ora),str(self.perc),str(self.masodperc)])
    
    def idoMp(self):
        return self.ora*60*60 + self.perc*60 + self.masodperc

