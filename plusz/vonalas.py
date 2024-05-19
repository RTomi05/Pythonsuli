
for i in range(16):
    print("*"*4 + "_",end="")

#VAGY

lista = []
for a in range(16):
    for i in range(4):
        lista.append("*")
    lista.append("_")

print("\n",*lista,sep="",end="")