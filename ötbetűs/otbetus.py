import random



#listák és stringek meghatározása

msh = ["b", "c", "cs", "d", "dz", "dzs", "f", "g", "gy", "h", "j", "k", "l", "ly", "m", "n", "ny", "p", "q", "r", "s", "sz", "t", "ty", "v", "w", "x", "y", "z", "zs"];
mgh = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"];
mshvagymgh = ["0", "1"];
folyt = ["Nem!", "Igen!"];
folytatas = ""
number = 2



def my_function():
    otb = []
    while len(otb) < 5:
        i = random.choice(mshvagymgh)
        if i == "0":
            x = random.choice(mgh)
            otb.append(x)
            x = random.choice(msh)
            otb.append(x)
            x = random.choice(mgh)
            otb.append(x)
            x = random.choice(msh)
            otb.append(x)
            x = random.choice(mgh)
            otb.append(x)
            print("A kapott szó: ",otb)
            print("Ha tetszik a szó, ajánld nekünk a kéziszótárunkhoz!")
            print("Kérsz még egy szót?")
            for y,elem in enumerate(folyt):
                print(y,":",elem)
            folytatas = int(input("Kérsz még egy szót? "))
            if folytatas == 1:
                my_function()
            elif folytatas == 0:
                quit()

                    
        elif i == "1":
            x = random.choice(msh)
            otb.append(x)
            x = random.choice(mgh)
            otb.append(x)
            x = random.choice(msh)
            otb.append(x)
            x = random.choice(mgh)
            otb.append(x)
            x = random.choice(msh)
            otb.append(x)
            print("A kapott szó: ",otb)
            print("Ha tetszik a szó, ajánld nekünk a kéziszótárunkhoz!")
            print("Kérsz még egy szót?")
            for y,elem in enumerate(folyt):
                print(y,":",elem)
            folytatas = int(input("Kérsz még egy szót? "))
            if folytatas == 1:
                my_function()
            elif folytatas == 0:
                quit()
    
#program
                
print("Ez a program ötbetűs szavakat tud neked létrehozni:")
my_function()
