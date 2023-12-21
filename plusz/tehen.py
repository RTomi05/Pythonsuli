import math

def gazdalkodas(gazdal):
    print("tehenek tartása egy évre:" )
    tehenek = float(input("tehenek száma (/db): "))
    tartas = float(input("tartásdíj (/nap /Ft): "))
    Ft = "Ft"
    gazdal = tehenek * tartas* 365
    return(gazdal)


print("tehenek tartása egy évre:" )
tehenek = float(input("tehenek száma (/db): "))
tartas = float(input("tartásdíj (/nap /Ft): "))
Ft = "Ft"

eredmeny = tehenek * tartas* 365
print("Tartás: ", eredmeny)

#VAGY

gazdalkodas("gazdal")


