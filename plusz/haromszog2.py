
#Számítsuk ki egy háromszög területét, a háromszög egy oldalából, és hozzátartozó magasságból! Kérjük be a háromszög oldalát és magasságát! 

print("Add meg a háromszög egyik oldalát és a hozzá tartozó magasságot centiméterben!")

oldal = float(input("A háromszög oldala: "))
magassag = float(input("A hozzá tartozó magasság: "))

txt = "A háromszög területe {terulet}"
print(txt.format(terulet = oldal * magassag / 2))