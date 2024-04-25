
#Ő itt Ted, a kis karakterünk

magan = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
rossz =  []

def Ted():

    global rossz
    while True:
        beadott = input("Adj meg EGY betűt! ")
        if len(beadott) == 1 and beadott != " ":
            if beadott in magan:
                print("Ez finom volt!")
            else:
                print("Fúj!")
                rossz.append(beadott)
                if len(rossz) == 10:
                    print("Ezeket vidd innen: ", rossz)
                    rossz = []
                else:
                    pass

        elif len(beadott) != 1 or beadott == " ":
            print("Ez nem egy betű volt!")
            #Ted()

#Program:

Ted()