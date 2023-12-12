
adatok=[]

f = open("autok.txt")
for sor in f:
    adatok.append(sor.strip().split(" ")) #vagy simán: sor.split()
f.close()

for i in range(len(adatok)):
    adatok[i][0]=int(adatok[i][0])
    adatok[i][3]=int(adatok[i][3])
    adatok[i][4]=int(adatok[i][4])
    adatok[i][5]=int(adatok[i][5])
    temp=[]
    temp.append(adatok[i][1])
    #'09:03'
    temp.append(int(adatok[i][1].split(":")[0]))
    temp.append(int(adatok[i][1].split(":")[1]))
    temp.append(temp[1]*60+temp[2])
    adatok[i][1]=temp
    

print(adatok)