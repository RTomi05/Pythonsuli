adatok=[]

f = open("fob2016.txt")

for sor in f:
    temp=[]
    tempSor=sor.split(";")
    for elem in tempSor:
        temp.append(elem)
    adatok.append(temp)

f.close()

print(adatok)