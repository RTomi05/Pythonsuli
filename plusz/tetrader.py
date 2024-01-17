
# Adott tetraéder. Számoltassa ki a tetraéder térfogatát

terfogat = 0

T = int(input("A tetraéder alapjának a területe: "))
M = int(input("A tetraéder magassága: "))

txt = "A tetraéder térfogata: {terfogat}"
print(txt.format(terfogat = (T * M) / 3))
