#Kérjetek be pozitív és negatív számokat 0 végjelig.
#Összegezzük a pozitív és a negatív számokat.
#Melyik van távolabb a nullától?
#A lista első felében melyik számból volt több ( p / n )?

szamok = []
szam = 1
pozitivÖ = 0
negativÖ = 0
elsoFelp = 0
elsoFeln = 0

while szam != 0:
    szam = int(input("Adj meg egy számot! "))
    if szam != 0:
        szamok.append(szam)
#print(szamok)
        
for szam in szamok:
    if szam < 0:
        negativÖ = negativÖ + szam
    elif szam > 0:
        pozitivÖ = pozitivÖ+ szam

print(pozitivÖ)
print(negativÖ)

#Melyik van távolabb a nullától?

ptav = abs(pozitivÖ)
ntav = abs(negativÖ)
print(ptav)
print(ntav)

if ptav > ntav:
    print("A pozitív összeg távolabb van a nullától.")
elif ntav > ptav:
    print("A negatív összeg távolabb van a nullától.")
else:
    print("A távolságuk egyenlő.")

#print("A lista első fele: {}".format(",".join(szamok[:len(szamok)%2])))
#print(elsoFelp)

elsoFel = szamok[:len(szamok)%2]
for i in elsoFel:
    if elsoFel[i] > 0:
        elsoFelp += 1
    else:
        elsoFeln += 1

print(elsoFeln)
print(elsoFelp)