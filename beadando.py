import random
    

lista=[]
paratlanLista=[]
harom=[]

#500db szám

while len(lista) != 500:
    i = random.randint(10000, 99999)
    lista.append(i)
    
print(lista)

#függvényes

def csinaldmar():
    a = 0
    b = 0
    for x in lista:
        if x%2 == 0:
            a = a + 1
        if x%2 != 0:
            b = b + 1
            paratlanLista.append(x)
    print("A programban talált páros számok száma:" , a)
    print("A programban talált páratlan számok száma:" , b)

csinaldmar()

#Melyik a nagyobb?

listafel1=lista[:250]
listafel2=lista[250:]
print(listafel1)
print(listafel2)
print(sum(listafel1))
print(sum(listafel2))
if sum(listafel1) > sum(listafel2):
    print("A lista első fele a nagyobb.")
else:
    print("A lista második fele a nagyobb.")

#páratlan számok összege
print("A páratlan számok összege:")
print(sum(paratlanLista))

for x in lista:
    str(x)[0]
    print(type (str(x)[0]), type(3))
    if str(x)[0] == 3:
    harom.append(x)
print(harom)


        


