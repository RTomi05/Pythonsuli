
def menu(lista):
    for i,elem in enumerate(lista):
        print("{}: {}".format(i+1,elem))

    valasztas=0
    while (valasztas<1 or valasztas>len(lista)) and valasztas!=69:
        try:
            valasztas=int(input("Válassz: "))
        except:
            pass
    
    return valasztas-1
        
lista=["előre", "hátra", "jobbra", "balra"]

#print("\n".join(lista))

#valasz=menu(lista)
#print(valasz,lista[valasz])

d={"Reggel felébredtem. Mit tegyek?":"Reggel felébredtem. Mit tegyek?",
   "fogmosás":"fogmosás",
   "reggeli":"reggeli",
   "öltözés":"öltözés"}

dEng={"Reggel felébredtem. Mit tegyek?":"Woke up. What should I do?",
      "fogmosás":"brush teeth",
      "reggeli":"breakfast",
      "öltözés":"get dressed"}


#import szovegeng as t
#nyelv választás
nyelvLista=["Magyar", "English", "Deutsch", "Russian"]
nyelvId={"Magyar":"szoveghun", "English":"szovegeng"}

print("Válassz nyelvet:")
while True:
    nyelvValasztas=menu(nyelvLista)
    #print(nyelvLista[nyelvValasztas])
    if nyelvLista[nyelvValasztas] in nyelvId:
        break
    else:
        print("Sajnos ez a fordítás még nem készült el!")

if nyelvId[nyelvLista[nyelvValasztas]] =="szoveghun":
    import szoveghun as t
elif nyelvId[nyelvLista[nyelvValasztas]] =="szovegeng":
    import szovegeng as t


tortenet=[
        [
            1,#szál ID
            t.text["Reggel felébredtem. Mit tegyek?"],#szöveg
            [t.text["fogmosás"], t.text["reggeli"],t.text[ "öltözés"]],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            2,#szál ID
            t.text["Elmegyek fogat mosni. Sikálom rendesen, ahogy kell!"],#szöveg
            [t.text["fogmosás"], t.text["reggeli"],t.text[ "öltözés"]],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            3,#szál ID
            t.text["Kellene valamit enni. Anya csinált valamit? Nézzük meg!"],#szöveg
            [t.text["fogmosás"], t.text["reggeli"],t.text[ "öltözés"]],#választási lehetőségek
            [2,3,4] #hova ugorjon
        ],
        [
            4,#szál ID
            t.text["Kissé hűvös van. Kellene valami ruha. \nFelveszek egy nadrágot, meg egy pólót."],#szöveg
            [t.text["fogmosás"], t.text["reggeli"],t.text[ "öltözés"]],#választási lehetőségek
            [2,3,4,66] #hova ugorjon
        ],
        [
            66,#szál ID
            "Vége mindennek...",#szöveg
            [],#választási lehetőségek
            [] #hova ugorjon
        ]
    ]


szalId=1

while True:
    temp=[]
    for e in tortenet:
        temp.append(e[0])
    #másként
    temp=[e[0] for e in tortenet]
    szalIndex=temp.index(szalId)

    print(tortenet[szalIndex][1])
    
    if tortenet[szalIndex][2]==[]:
        break
    
    menuPont=menu(tortenet[szalIndex][2])

    if menuPont == 68:
        break

    szalId=tortenet[szalIndex][3][menuPont]



print("The End")

    

