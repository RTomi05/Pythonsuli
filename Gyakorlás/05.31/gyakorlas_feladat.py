#Készíts egy függvényt, ami egy számot kér be, ez a bekérés addig folytatódjon, amíg nem szám!
#A számot adja vissza!

class Szam:
	def __init__(self,sor):
		vagas = sor.split("\n")
		self.number = int(vagas[0])


csinald = 0
def bekeres():
	global csinald
	while csinald == 0:
		try:
			kapottSzam = int(input("Adj meg egy számot!"))
			csinald = 1
		except:
			print("Ez nem szám.")

	return print(kapottSzam)
bekeres()

#Kérj be számokat, amíg nem negatívot adnak meg!

szam = 1
lista = []

while szam > 0 or szam == 0:
	szam = int(input("Adj meg számokat!"))
	print(szam)
	lista.append(szam)

del lista[-1]
print(lista)

#Ezeket a számokat írjuk ki egy fájlba egymás alá

f = open("ezkellide.txt", "w")
for i in lista:
	i = str(i)
	f.write(i+"\n")
f.close()

#Ezeket a számokat töltsük be
kapottBetoltes = []

file = open("ezkellide.txt", "r")
for egySor in file:
	kapottBetoltes.append(Szam(egySor))
file.close()

#Adjuk meg az átlag feletti számok összegét