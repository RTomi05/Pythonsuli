
# A program első sora a saját nevét és vesszővel tagolva az aktuális évszámot írja a képernyőre.
#Írjon programot, amely bekéri a számokat 0 végjelig, miközben összegezi azokat, ha azok nagyobbak mint 49. 
#Ha szám 49 vagy kisebb, akkor írjon hibaüzenet a felhasználónak. 

nev = "Rengel Tamás"
ev = 2024
print(nev,",",ev)

txt = "A számok összege:"

szamok = []
bekert = 1
osszeg = 0
while bekert > 0 : 
    bekert = int(input("Adj meg egy számot! "))
    if bekert > 49:
        osszeg = bekert + osszeg
        szamok.append(bekert)
    else:
        print("Hiba: A szám 49, vagy kisebb!")
    if bekert == 0:
        break
        
print(txt, osszeg)