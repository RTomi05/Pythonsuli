
#Írjon programot, amely arról érdeklődik, hogy mit csinált a felhasználó a mai napon. Kínáljon fel legalább 4 előre megírt választási lehetőséget, utolsóként „Egyéb, leírom: ” szöveggel. Az utóbbi esetben a program kérje be a felhasználó válaszát, majd az eredményt tárolja fájlba. 

tevList = ["Buszoztam.", "Találkoztam egy barátommal.", "Programozás feladatokat csináltam.", "Vártam a GTA 6 kiadását.", "Egyéb, leírom: "]

x = "start"

for i, elem in enumerate(tevList):
        print("\t"+str(i+1)+":",elem)

if x == "start":
    try:
        tev = int(input("Mit csináltál ma? "))
        if tev not in range(len(tevList)+1):
            raise                
    except:
        print("Válassz a listából!")


if tev == 1:
    print("Remélem, jót utaztál.")

if tev == 2:
    print("Remélem, jó időtöltés volt.")

if tev == 3:
    print("Fogadjunk, nem lett jó!")

if tev == 4:
    print("Arra még várhatsz.")

if tev == 5:
    fajlba = input("Kíváncsian hallgatom, írd le! ")
    f = open("tevekenyseg.txt", "w")
    f.write(fajlba)
    f.close