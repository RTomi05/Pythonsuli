
#Ő itt Ted, a kis karakterünk

magan = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
msh = ["b", "c", "d", "f", "g", "f", "h", "j", "k", "l", "p", "q", "r", "t", "z", "y", "x", "n", "m", "w"]

def Ted():

    finom =  []
    while True:
        beadott = input("Adj meg EGY betűt! ")
        if len(beadott) == 1 and beadott in magan or beadott in msh:
            if beadott in magan:
                print("Ez finom volt!")
                finom.append(beadott)
                if len(finom) == 10:
                    print("Köszi, várj egy kicsit!")
                    print("Ürítés folyamatban!")
                    #Átalakítás
                    print("*"*len(finom))
                    finom = []
                else:
                    pass
            else:
                print("Fúj!")
        
        elif len(beadott) != 1 or beadott == " " or beadott.isnumeric():
            print("Ez nem egy betű volt!")

#Program:

Ted()