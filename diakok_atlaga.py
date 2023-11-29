import random

#12 fő, 8-12 db jegy (1-5)

jegyek = [1,2,3,4,5]
for i in range(12):
    egyDiak=[]
    for k in range(random.randrange(8,13)):
        jegy = random.randrange(1,6)
        egyDiak.append(jegy)
    jegyek.append(egyDiak)
    print(egyDiak)
    a = sum(egyDiak)/len(egyDiak)
    print(a)