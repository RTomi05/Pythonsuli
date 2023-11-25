import random

RPS=["kő","papír","olló"]


ujra="1"


while ujra == "1":
    jatekos= "0"
    computer= "0"
    Pvalasztas=""
    Cvalasztas="" 
    print("#"*65)
        #jatekos köre
    for x,elem in enumerate(RPS):
        print(str(x+1)+" "+":", elem)

    while jatekos == "0":
        try:
            jatekos=str(input("Válassz: "))
            if jatekos not in range(len(RPS)+1):
                raise
        except:
            pass

    if jatekos == "1":
        Pvalasztas= "kő"
    elif jatekos == "2":
        Pvalasztas= "papír"
    elif jatekos == "3":
        Pvalasztas= "olló"
    else:
        pass
        
    print("#"*65)
          
    if computer == "0":
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
        
    if (computer == 1 and jatekos == "1") or (computer == 2 and jatekos == "2") or (computer == 3 and jatekos == "3"):
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Döntetlen.")
    elif computer == 1 and Pvalasztas == "2":
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Te nyertél.")
    elif computer == 1 and Pvalasztas == "3":
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""A számítógép nyert.")
    elif computer == 2 and Pvalasztas == "1":
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""A számítógép nyert.")
    elif computer == 2 and Pvalasztas == "3":
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Te nyertél.")
    elif computer == 3 and Pvalasztas == "1":
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""Te nyertél.")
    elif computer == 3 and Pvalasztas == "2":
        print("Választásod:",Pvalasztas,"\nSzámítógép választása:",Cvalasztas,"\n""A számítógép nyert.")
    
    
        
    

    
