
#Írjon programot, amely bekér egy számot, majd kiírja, hogy nagyobb vagy kisebb mint 50. 

szam = float(input("A megadott szám: "))
if szam > 50:
    print("A szám nagyobb, mint 50.")
elif szam < 50:
    print("A szám kisebb, mint 50.")
else:
    print("A szám egyenlő 50-nel.")