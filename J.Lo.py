
adatok=[]
f = open("tancrend.txt")

for sor in f:
    adatok.append(sor.strip())
f.close()

print(adatok)

adatok2=[]
