#Kérjen be számokat „vege” végjelig.
#Minden bekért számnak írja ki a második hatványát.

bekert = 1

while bekert != "vege":
    bekert = input("Adj meg egy számot! ")
    if bekert == "vege":
        break
    else:
        bekert = int(bekert)
    hatvany = bekert ** 2
    print(hatvany)

