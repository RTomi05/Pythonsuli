datum = input("Add meg a dátumot: ")
f = open("esemenyek.txt", "a")
f.write(datum)
f.write(":")

esemeny = input("Add meg az eseményt: ")
f.write(esemeny)
f.write("\n")
f.close()