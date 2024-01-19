
#Adott egy tetraéder. Számoltassa ki a tetraéder felszínét.

a = input("Adja meg a tetraédert határoló háromszögek területét: ")
b = input("Adja meg a tetraédert határoló háromszögek területét: ")
c = input("Adja meg a tetraédert határoló háromszögek területét: ")
d = input("Adja meg a tetraédert határoló háromszögek területét: ")

txt = "A tetraéder felszíne: {abcd1}"
print(txt.format(abcd1 = a + b + c + d))