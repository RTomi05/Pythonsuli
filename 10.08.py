lista=["a", "b", "z", "h", "c", "i", "o"]

print(lista)

print("#"*50)

for elem in lista:
    print(elem)

print("#"*50)
    
for i in range(len(lista)):
    print(lista[i])

print("#"*50)

for elem in lista[:3]:
    print(elem)

print("#"*50)

for elem in lista[3:]:
    print(elem)

print("#"*50)

for elem in lista[-2:]:
    print(elem)

print("#"*50)

for elem in lista[::-1]:
    print(elem)

lista2=lista[1:-1]
print(lista2)


print(125 ==5*5**2)
