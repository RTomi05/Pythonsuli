import random

RPS=["kő","papír","olló", "kilépés"]

ujra="1"

print("A kő-papír-olló játékszabályai:\n""A kő kicsorbítja az ollót: A kő győz.\nAz olló elvágja a papírt: Az olló győz.\nA papír becsomagolja a követ: A papír győz.""\n""Jó szórakozást!")

while ujra == "1":
    jatekos = 0
    computer = 0
    Pvalasztas = ""
    Cvalasztas = "" 
    print("#"*65)
        #jatekos köre
    for x,elem in enumerate(RPS):
        print(str(x+1)+" "+":", elem)

    while jatekos == 0:
        try:
            jatekos=int(input("Válassz: "))
            if jatekos not in range(len(RPS)+1):
                print("Válassz a listából: ")
        except:
            pass

    if jatekos == 1:
        Pvalasztas= "kő"
    elif jatekos == 2:
        Pvalasztas= "papír"
    elif jatekos == 3:
        Pvalasztas= "olló"
    elif jatekos == 4:
        ujra = "0"
        quit()
        
    #print("#"*65)
          
    if computer == 0:
        computer = random.randint(1,3)
    else:
        pass
    
    if computer == 1:
        Cvalasztas = "kő"
    elif computer == 2:
        Cvalasztas = "papír"
    elif computer == 3:
        Cvalasztas = "olló"
    else:
        pass
        
    if (computer == 1 and jatekos == 1) or (computer == 2 and jatekos == 2) or (computer == 3 and jatekos == 3):
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Döntetlen.")
    if computer == 1 and jatekos == 2:
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Te nyertél.")
    if computer == 1 and jatekos == 3:
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""A számítógép nyert.")
    if computer == 2 and jatekos == 1:
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""A számítógép nyert.")
    if computer == 2 and jatekos == 3:
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Te nyertél.")
    if computer == 3 and jatekos == 1:
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Te nyertél.")
    if computer == 3 and jatekos == 2:
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""A számítógép nyert.")


