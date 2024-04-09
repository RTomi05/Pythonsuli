class Uzenet:
    def __init__(self,sor1,sor2):
        #"2 15"
        #"1/0 #gy#domb##l fig###tu# f#i#s ho#a##dalyoz$$"
        self.nap = int(sor1.split(" ")[0])
        self.amator = int(sor1.split(" ")[1])

        self.uzenet = sor2

    def farkasKereso(self):
        return "farkas" in self.uzenet
    
        if "farkas" in self.uzenet:
            return True
        else:
            return False
        

class Nap:
    def __init__(self,nap):
        self.nap = nap
        self.uzenetek = []

    def hozzaAd(self,uzenet):
        self.uzenetek.append(uzenet)

    def uzenetSzam(self):
        return len(self.uzenetek)

    def helyreallit(self):
        megfejtes = self.uzenetek[0].uzenet

        for i,egyBetu in enumerate(megfejtes):
            if egyBetu == "#":
                for egyUzenet in self.uzenetek:
                    if egyUzenet.uzenet[i] != "#":
                        megfejtes = megfejtes[:i] + egyUzenet.uzenet[i] + megfejtes[i+1:]
                        break

        return megfejtes

        """
        Függvény szame(szo:karaktersorozat): logikai
        valasz:=igaz
        Ciklus i:=1-től hossz(szo)-ig
        ha szo[i]<'0' vagy szo[i]>'9' akkor valasz:=hamis
        Ciklus vége
        szame:=valasz
        Függvény vége
        """

    def szame(self,szo): 
        valasz = True
        