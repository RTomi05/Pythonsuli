#Kérjen be számokat „vege” végjelig.
#Minden bekért számnak írja ki a második hatványát.

bekert = 1

#while bekert > 0 : 
bekert = input("Adj meg egy számot! ")
if bekert != "vege":
    bekert = int(bekert)
    hatvany = bekert ** 2
    print(hatvany)

