import random

#12 fő, 8-12 db jegy (1-5)

diakok = ["1.","2.","3.","4.","5.","6.","7.","8.","9.","10.","11.","12."]
jegyek = [1,2,3,4,5]
for i in range(12):
    egyDiak=[]
    for k in range(random.randrange(8,13)):
        jegy = random.randrange(1,6)
        egyDiak.append(jegy)
    jegyek.append(egyDiak)
        