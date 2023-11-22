#Irassátok ki az 50 első nemnegatív számot!

for i in range(0,50):
    print(i, end="; ")
else:
    print("\n Kész!")

#Irassátok ki a kétjegyű számokat!

for a in range(10,100):
    print(a, end="; ")
else:
    print("\n Kész!")

#Irassátok ki a 100-nál kisebb 7-tel osztható számokat!

for b in range(7, 100, 7):
    print(b)
else:
    print("\n Kész!")
