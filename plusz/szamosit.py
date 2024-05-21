import random

#A gép száma:
gep = random.randint(0,9)
rossz = 0

while rossz <= 2:
    player = int(input("Szerinted mire gondolt a gép? "))
    if player == gep:
        print("Eltaláltad!")
        break
    else:
        print("Sajnos nem jött össze!")
        rossz += 1

if rossz == 3:
    print("Sajnos elfogytak a lehetőségeid.")
