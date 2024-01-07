
# Kérje be három hasáb adatait. Számítsa ki a hasábok térfogatát, majd írja a képernyőre a térfogatokat és azok összegét.

print("Adja meg az első hasáb adatait centiméterben!")
a1 = float(input("Első oldal hossza: "))
b1 = float(input("Második oldal hossza: "))
c1 = float(input("Harmadik oldal hossza: "))

print("Adja meg a második hasáb adatait centiméterben!")
a2 = float(input("Első oldal hossza: "))
b2 = float(input("Második oldal hossza: "))
c2 = float(input("Harmadik oldal hossza: "))

print("Adja meg a harmadik hasáb adatait centiméterben!")
a3 = float(input("Első oldal hossza: "))
b3 = float(input("Második oldal hossza: "))
c3 = float(input("Harmadik oldal hossza: "))

print("A három hasáb területei és összegük: ")
txt1 = "Az első hasáb területe: {abc1} cm."
txt2 = "A második hasáb területe: {abc2} cm."
txt3 = "A harmadik hasáb területe: {abc3} cm."
txtossz = "A három térfogat összege: {osszeg} cm."
print(txt1.format(abc1 = a1*b1*c1))
print(txt2.format(abc2 = a2*b2*c2))
print(txt3.format(abc3 = a3*b3*c3))

abc1 = a1*b1*c1
abc2 = a2*b2*c2
abc3 = a3*b3*c3
print(txtossz.format(osszeg = abc1+abc2+abc3))