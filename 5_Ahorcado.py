import random

#Juego del ahorcado
def jugar():
    listado=["año", "estado", "pais", "lugar", "sistema", "palabra", "linea", "nombre", "padre", "fuerza"]
    listado_final=[]
    for l in listado:
        listado_final.append(list(l))
    # print(listado_final)
    palabra=random.choice(listado_final)
    palabra=dict(enumerate(palabra))
    # print(palabra)
    valores = set(palabra.values())
    contraste=set()
    repetidos=set()
    z=0
    while valores != contraste or z<4:
        for p in palabra.values():
            if p in contraste:
                print(p, end=" ")
            else:
                print("_", end=" ")
        valor=input("\n \n Escribe un valor: ")
        if valor in palabra.values():
            contraste.add(valor)      
        else:
            if valor not in repetidos:
                print("No está")
                repetidos.add(valor)
                z+=1
            else:
                print("\nYa has dicho esa letra, escoge otra: ")
                valor=input("\n \n Escribe un valor: ")
        print("Puntuacion: ", z)
        if valores == contraste:
            print("Ganaste!")
            for p in palabra.values():
                print(p,end="")
            break
        if z>4:
            print("Perdiste!")
            for p in palabra.values():
                print(p,end="")
            break

jugar()


