class nasa:
    def __init__(self, sor):
        #rn3.swc.com*20/Jul/1995:00:02:14*GET /history/apollo/apollo-13/apollo-13-patch.jpg*200 90112
        vag = sor.split("*")
        self.url = vag[0]
        self.date = vag[1]
        self.image = vag[2]
        self.status = vag[3].split(" ")[0]
        self.size = vag[3].split(" ")[1]

#ELSŐ
        if self.url[-1].isnumeric():
            self.Domain = False
        else:
            self.Domain = True

#MÁSODIK
        if self.url[-1] in "0123456789":
            self.Domain = False
        else:
            self.Domain = True

#HARMADIK
        try:
            int(self.url[-1])
            self.Domain = False
        except:
            self.Domain = True
            
#NEGYEDIK
        self.Domain = not self.url[-1].isnumeric()

    def ByteMeret(self):
        #self.size = self.size.strip("-\n")
        if self.size == "-":
            return 0
        else:
            return int(self.size)
        
    
        