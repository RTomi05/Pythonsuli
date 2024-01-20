#Szöveg ellenörző

import random

betuk = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]

csinald = 1
szukseges = ""
bekeres = ""
hanyBetu = 0


def program():
    hanyBetu = random.randint(4,4)
    if hanyBetu == 4:
        szukseges = str(random.choice(betuk) + random.choice(betuk) + random.choice(betuk) + random.choice(betuk))
        print("A beírandó: ",szukseges)
        bekeres = str(input("Írd be a fenti betűket!"))
        if bekeres == szukseges:
            program()
        elif bekeres != szukseges:
            print("Próbáld újra!")
            program()
        
            
program()


