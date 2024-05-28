
import math

def szam():
    szam1 = int(input("1. szám "))
    szam2 = int(input("2. szám "))
    szam3 = int(input("3. szám "))
    osszeg = szam1 + szam2 + szam3
    print(osszeg)

def keplet():
    global iksz
    iksz = int(input("Kérek egy számot! "))
    print(iksz)
    kep = (math.sqrt(42*iksz**3 + 12) + 25 * iksz) / (2 * (13-26)) * 4 * (iksz / 6)
    print(kep)

