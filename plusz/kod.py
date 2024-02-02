# A program először saját nevét írja a képernyőre. A következő sorba a programkészítés dátumát írja a képernyőre.

print("Rengel Tamás")
print("2024. 01. 22.")

szam = int(input("Adja meg a kódszámot: "))
engedelyek = 2248
engedelyek2 = 1834
engedelyek3 = 3823

if szam == engedelyek:
    print("Bejutott a rendszerbe!")
elif szam == engedelyek2:
    print("Bejutott a rendszerbe!")
elif szam == engedelyek3:
    print("Bejutott a rendszerbe!")
else:
    print("Sikertelen azonosítás!")


#VAGY
    

szamok = [2248,1834,3823]

szam2 = int(input("Adja meg a kódszámot: "))
if szam2 in szamok:
    print("Bejutott a rendszerbe!")

else:
    print("Sikertelen azonosítás!")
