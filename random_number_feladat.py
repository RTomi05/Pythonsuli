import random

numbers=[]

for x in range(500):
    x = str(random.randrange(1,5001))
    numbers.append(x)
    f = open("randomhoz.txt", "a")
    f.write(x)
    f.write(" ")
    f.close()
    f = open("randomhoz.txt", "r")
    print(f.read())

