
#A nemzetközi hüvelyk: 1″ = 2,54 cm Kérjen be egy cm értéket, majd írja ki hüvelykben. 

mennyiseg = float(input("A bekért adat centiméterben: "))

txt = "A megadott mennyiség hüvelykben kifejezve: {ertek}"
print(txt.format(ertek = mennyiseg / 2.54))