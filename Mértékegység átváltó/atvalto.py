# Mértékegység átváltó
# Rengel Tamás 2023. 10. 06.
# Projektfeladat

tipusok=["Hosszúság", "Terület", "Térfogat", "Tömeg", "Űrmérték", "Űrmérték + térfogat"]
egysegek=[["mm", "cm", "dm", "m", "km"],
            ["mm2", "cm2", "dm2", "m2", "km2"],
            ["mm3", "cm3", "dm3", "m3", "km3"],
          ["g", "dkg", "kg", "t"],
          ["ml", "cl", "dl", "l", "hl"],
          []]

valtok=[[10,10,10,1000,1],
            [100,100,100,1000000,1],
            [1000,1000,1000,1000000000,1],
          [],
          ["ml", "cl", "dl", "l", "hl"],
          []]


    
print("#"*35)
#for elem in tipusok:
#   print(elem)

for i,elem in enumerate(tipusok):
    print("\t"+str(i+1)+":",elem)

print("\t0: Kilépés")

tipusId="alma"
while tipusId=="alma" or tipusId not in range(len(tipusok)+1):
    try:
        tipusId=int(input("Válassz! "))
        if tipusId not in range(len(tipusok)+1):
            raise                
    except:
        print("Válassz a listából!")

print("#"*35)
tipusId-=1
print("Típus:",tipusok[tipusId])


print("Mértékegységek:")

print("Forrás:")
for i,elem in enumerate(egysegek[tipusId]):
    print("\t"+str(i+1)+":",elem)
    
print("\t0: Vissza")

egysegId="alma"
while egysegId=="alma" or egysegId not in range(len(egysegek[tipusId])+1):
    try:
        egysegId=int(input("Válassz! "))
        if egysegId not in range(len(egysegek[tipusId])+1):
            raise                
    except:
        print("Válassz a listából!")


print("Cél:")

for i,elem in enumerate(egysegek[tipusId]):
    print("\t"+str(i+1)+":",elem)
    
print("\t0: Vissza")

egysegId2="alma"
while egysegId2=="alma" or egysegId2 not in range(len(egysegek[tipusId])+1):
    try:
        egysegId2=int(input("Válassz! "))
        if egysegId2 not in range(len(egysegek[tipusId])+1):
            raise                
    except:
        print("Válassz a listából!")



szam=float(input("Mennyiség: "))
egysegId-=1
egysegId2-=1

if egysegId<egysegId2:
    #print(valtok[tipusId][egysegId:egysegId2])
    szorzo=1
    for e in valtok[tipusId][egysegId:egysegId2]:
        szorzo*=e
    eredmeny=szam/szorzo
    
else:
    #print(valtok[tipusId][egysegId2:egysegId])
    szorzo=1
    for e in valtok[tipusId][egysegId2:egysegId]:
        szorzo*=e
    eredmeny=szam*szorzo

print("#"*35)
print("Eredmény:")

print(szam,egysegek[tipusId][egysegId],eredmeny,egysegek[tipusId][egysegId2])
