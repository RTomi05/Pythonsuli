lista=[]

#A lényeg, hogy ne legyen üres!
beker="q"

while beker!="":
    beker=input("Adj meg valamit!")
    if beker!="":
        lista.append(beker)

print(lista)
utolso=lista[-3:]
utolso.sort()

lista.sort()
print(lista)

for x in lista:
    print(x)

for x in lista[-3:]:
    print(x)

for x in utolso:
    print(x)






