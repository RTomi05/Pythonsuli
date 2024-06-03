sor = int(input("Sorok száma: "))
oszlop = int(input("Oszlopok száma: "))
jo = 0
while jo == 0:
    try:
        kar = input("Kérek pontosan 1 karaktert: ")
        if len(kar) == 1:
            jo += 1
            for i in range(sor):
                print(oszlop * kar)
    except:
        print("Nem megfelelő méret.")
