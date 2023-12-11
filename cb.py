adatok=[]

f = open("cb.txt")
for sor in f:
    adatok.append(sor.strip().split(";"))

f.close()

print(adatok)