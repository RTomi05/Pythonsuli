#Kérje be egy elektronikai eszköz üzemi hőmérsékletének alsó és felső határát. Ha az alsó határ < 25 °C akkor és a felső határ > 85 °C, akkor katonai célokra megfelel az eszköz.
#A program írja ki, hogy katonai célokra megfelel-e.
#A képernyő első sorában azonban saját nevét és osztályát írja a képernyőre.

print("Rengel Tamás 10.B")

hatarA = int(input("Adja meg az eszköz alsó hőmérsékleti határát Celsius fokban! "))
hatarF = int(input("Adja meg az eszköz felső hőmérsékleti határát Celsius fokban! "))

megfelel = 0

if hatarA < 25:
    megfelel = megfelel + 1
if hatarF > 85:
    megfelel = megfelel + 1

if megfelel == 2:
    print("Az eszköz megfelel a katonai célokra!")

    