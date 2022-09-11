#Juego del Ahorcado
import random
lista_palabras=["juego", "croqueta", "zumo", "melon", "cisma", "martes", "pelota", "puchero"]
letrero=[]
puntos=[]


def juego():
    print("Este es el juego del ahorcado")
    palabra=random.choice(lista_palabras)
    print(palabra)
    print(f"La palabra tiene {len(palabra)} letras.")
    for letra in palabra:
        print("_", end=" ")
        letrero.append("-")
    print("\n")
    print(letrero)
    palabra=list(palabra)
    print(palabra)
    while sum(puntos)<5:
        juega=input("Di una letra: ")
        if juega in palabra:
            print("Está dentro")
            posicion=palabra.index(juega)
            print(posicion)
            letrero[posicion]=juega
            print(letrero)
            if letra in letrero !="-":
                print("has ganado")
                break
        else:
            print("No está")
            puntos.append(1)
            if sum(puntos)==1:
                print(
"""
        ---------
        | O   O |
        |___-___|
""")    
            elif sum(puntos)==2:
                print(
"""
        ---------
        | O   O |
        |___-___|
         |     |
         |_____|
""")
            elif sum(puntos)==3:
                print(
"""
        ---------
        | O   O |
        |___-___|
          _| |_ _
        /|     | |
       / |_____| |
""")
            elif sum(puntos)==4:
                print(
"""
        ---------
        | O   O |
        |___-___|
          _| |_ _
        /|     | |
       / |_____| |
         |  I
         |,,I
         |__|
""")
            elif sum(puntos)==5:
                print(
"""
        ---------
        | O   O |  PERDISTE!!! :(
        |___-___|
          _| |_ _
        /|     | |
       / |_____| |
         |  I  |
         |,,I,,|
         |__|__|
""")                          







#jugar=input("Quieres jugar? ")

#while jugar == "si":
#    juego()    

juego()

print("\nHas salido del juego")