szorzotabla=[]

actual = 1

class Tabla:
    def __init__(self, ertek):
        self.Sor=[s*ertek for s in range(1,11)]

while actual < 11:
    szorzotabla.append(Tabla(actual).Sor)
    "\n"
    actual += 1

print(szorzotabla)