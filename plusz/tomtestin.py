
#Kérje be egy ember testtömegét (kg) és testmagasságát (méter).

testtomeg = float(input("Tömeg (kg): "))
testmagassag = float(input("Magasság (m): "))

txt = "Testtömegindexe: {testtomegindex}"
print(txt.format(testtomegindex = testtomeg / (testmagassag**2)))

