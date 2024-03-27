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


