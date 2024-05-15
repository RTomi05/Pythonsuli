
szamok = [3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4]
letramezo = [10,20,30,40]
mezo = 0
vissza = 0
lepesek = []


print("2. feladat")
for egySzam in szamok:
    mezo += egySzam
    if mezo in letramezo:
        mezo = mezo-3
        vissza += 1
    lepesek.append(mezo)
print(*lepesek,sep=", ")

print("3. feladat")
print("A játék során {} alkalommal lépett létrára.".format(vissza))

print("4. feladat")
if mezo >= 45:
    print("A játékot befejezte.")
else:
    print("A játékot abbahagyta.")

