
#A program első sora a „Gyártó: ” szöveget, majd a saját nevét írja a képernyőre. 

print("Gyártó: Rengel Tamás")

#VAGY

a = "Gyártó:"
b = "Rengel"
c = "Tamás"
print(a,b,c)

# Vegyen fel 5 darab változót. Vegyen fel bennük egy valós számot, majd adja össze tartalmukat. 
#Az összegüket egy „osszeg” nevű változóban helyezze el, amelyet osszon el 5-tel. A végeredményt írassa a képernyőre a következő szöveg után: „Atlag: ”.
#Ügyeljen a kiíratandó szövegekben a szóközök és a kettőspontok meglétére.

a1 = 5
b1 = 14
c1 = 2.5
d1 = 8.2
e1 = 10
osszeg = (a1 + b1 + c1 + d1 + e1) / 5

print(osszeg)

#VAGY

osszeg = 0
osszeg = "Az eredmény: {betu}"
print(osszeg.format(betu = (a1 + b1 + c1 + d1 + e1) / 5))


