
#Rengel Tamás

kredit = float(input("Elért kreditpontok a félévben: "))
atlag = float(input("Osztályzatok átlaga: "))
index = kredit * atlag / 30

txt = "Ösztöndíj átlaga: {index}"
print(txt.format(index = kredit * atlag / 30))

if index > 5.8:
    print("Jó eredmény!")

elif index < 5.8:
    print("Gyenge eredmény!")