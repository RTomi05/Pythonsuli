
#bejárós ciklus
for x in "banana":
    print(x)


txt="Ez az elem bent van-e"
print("elem" in txt)

a="Hello World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))

#trükk
print(a.replace("l", ""))

#karaktereket számol
print(len(a))

b=a.split("l")
print(b)


#concatenation
a = "Hello "
b = "World"
c = a + b
print(c)

print("#"*65)

#string format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#index-szel való kiíratás

print("#"*65)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 



