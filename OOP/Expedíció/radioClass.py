class Uzenet:
    def __init__(self,sor1,sor2):
        #"2 15"
        #"1/0 #gy#domb##l fig###tu# f#i#s ho#a##dalyoz$$"
        self.nap = int(sor1.split(" ")[0])
        self.amator = int(sor1.split(" ")[1])

        self.uzenet = sor2
        self.szamKereso()

        
    def szamKereso(self):
        self.kifejlett = False
        self.kolyok = False

        szamok = self.uzenet.split(" ")[0].split("/")
        if len(szamok) == 2:
            if szamok[0].isnumeric():
                self.kifejlett = int(szamok[0])
            if szamok[1].isnumeric():
                self.kolyok = int(szamok[1])

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
        for i in range(len(szo)):
            if szo[i] < "0" or szo[i] > "9":
                valasz = False

        return valasz

    def radioAmator(self,szam):
        for egyUzenet in self.uzenetek:
            if szam == egyUzenet.amator:
                return egyUzenet
            
        return False