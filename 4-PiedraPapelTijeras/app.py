#Juego piedra papel o tijeras
import random
puntos_humano=[]
puntos_maquina=[]
#Lógica del juego
def juego():
    lista = ["piedra", "papel", "tijera"]
    maquina=random.choice(lista)
    humano=input("Elije: ")
    print(f"Has elegido {humano} y la máquina {maquina}")

    if humano == maquina:
        print("Empate!!")
    #Gana humano
    elif maquina == "piedra" and humano == "papel":
        print(f"Humano Gana! {humano} gana a {maquina}")
        puntos_humano.append(1)
    elif maquina == "papel" and humano == "tijera":
        print(f"Humano Gana! {humano} gana a {maquina}")
        puntos_humano.append(1)
    elif maquina == "tijera" and humano == "piedra":
        print(f"Humano Gana! {humano} gana a {maquina}")
        puntos_humano.append(1)
    #Gana máquina
    elif maquina == "papel" and humano == "piedra":
        print(f"Máquina Gana! {maquina} gana a {humano}")
        puntos_maquina.append(1)
    elif maquina == "tijera" and humano == "papel":
        print(f"Máquina Gana! {maquina} gana a {humano}")
        puntos_maquina.append(1)
    elif maquina == "piedra" and humano == "tijera":
        print(f"Máquina Gana! {maquina} gana a {humano}")
        puntos_maquina.append(1)
    else:
        print("No has escrito bien la palabra")

rejugar=input("Quieres jugar?")

while rejugar == "y":
    juego()

    print(f"Tu tienes {sum(puntos_humano)} puntos.")
    print(f"La máquina tiene {sum(puntos_maquina)} puntos.")
    rejugar=input("Quieres volver a jugar?")




#Con un input y un if controlamos si jugamos o no.