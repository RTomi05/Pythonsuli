#Számítsuk ki egy háromszög kerületét, a háromszög három oldalából! Kérjük be a háromszög oldalait! 


print("Add meg a háromszög oldalait centiméterben!")

oldal_a = float(input("a oldal hossza: "))
oldal_b = float(input("b oldal hossza: "))
oldal_c = float(input("c oldal hossza: "))

txt = "A háromszög kerülete: {kerulet} cm."
print(txt.format(kerulet = oldal_a + oldal_b + oldal_c))






