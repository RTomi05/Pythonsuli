
adatok=[]

f = open("fob2016.txt")

for sor in f:
    temp=sor.strip().split(";")
    print(temp)
    for i in range(3,len(temp)):
    	temp[i]=int(temp[i])
        
    adatok.append(temp)

f.close()