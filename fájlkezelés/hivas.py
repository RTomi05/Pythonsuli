
adatok=[]
f = open("hivas.txt")
for sor in f:
    temp=[]
    #"6 51 8 6 54 58"
    tempSor=sor.split(" ")
    #["6" "51" "8" "6" "54" "58"]
    for elem in tempSor:
        temp.append(int(elem))
        
    temp.append(temp[3]*60*60+temp[4]*60+temp[5]-temp[0]*60*60+temp[1]*60+temp[2])
    
	#[6, 51, 8, 6, 54, 58]
    adatok.append(temp)

f.close()

print(adatok)
