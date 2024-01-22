# A program először saját nevét írja a képernyőre. A következő sorba a programkészítés dátumát írja a képernyőre.

print("Rengel Tamás")
print("2024. 01. 22.")

szam = int(input("Adja meg a kódszámot: "))
while szam == szam:
    if szam == 2248 or 1834 or 3823 :
        print("Bejutott a rendszerbe!")
    elif szam != 2248 or 1834 or 3823:
        print("Sikertelen azonosítás!")
