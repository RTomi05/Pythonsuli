
#Írjon programot, amely bekér két számot, majd kiírja melyik nagyobb.

szam1 = float(input("Egyik szám: "))
szam2 = float(input("Másik szám: "))

if szam1 > szam2:
    print("Az első szám a nagyobb.")
elif szam2 > szam1:
    print("A második szám a nagyobb.")
else:
    print("A két szám egyenlő.")