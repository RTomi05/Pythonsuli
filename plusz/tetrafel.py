
#Adott egy tetraéder. Számoltassa ki a tetraéder felszínét.

abcd1 = 0

a = int(input("Adja meg a tetraédert határoló háromszögek területét: "))
b = int(input("Adja meg a tetraédert határoló háromszögek területét: "))
c = int(input("Adja meg a tetraédert határoló háromszögek területét: "))
d = int(input("Adja meg a tetraédert határoló háromszögek területét: "))

txt = "A tetraéder felszíne: {abcd1}"
print(txt.format(abcd1 = a + b + c + d))