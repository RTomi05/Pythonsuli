
#A nemzetközi hüvelyk: 1″ = 2,54 cm Kérjen be egy hüvelyk értéket, majd írja ki centiméterben. 

mennyiseg = float(input("A bekért adat centiméterben: "))

txt = "A megadott mennyiség centiméterben kifejezve: {ertek}"
print(txt.format(ertek = mennyiseg * 2.54))