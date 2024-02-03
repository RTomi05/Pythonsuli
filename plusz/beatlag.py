
#Írjon programot, amely bekér számokat 0 végjelig, majd kiírja azok átlagát. 

szamok = []
bekert = 1
i = 0

txt = "Átlag: {atlag}"
while bekert > 0 : 
    bekert = int(input("Adj meg egy számot! "))
    i = bekert + i
    if bekert == 0:
        break
    else:
        szamok.append(bekert)


print(txt.format(atlag = i / len(szamok)))
#for i in len(szamok):
    