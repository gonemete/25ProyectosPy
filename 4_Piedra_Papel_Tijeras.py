# El juego clásico de Piedara, Papel o Tijeras.
# Uso de de la biblioteca de python random, inputs, condicionales y funciones
# Usamos random.choice() para jugar

import random

def jugarPPT():
    opciones =["Piedra", "Papel", "Tijeras"]
    ptos_jugador=0
    ptos_compu=0
    salida=input("Quieres Jugar?")
    while True:
        
        if salida=="s":
            pregunta=input("Escoge una opción: Piedra - Papel - Tijeras ")
            respuesta_compu=random.choice(opciones)
            if pregunta == "Piedra":
                if respuesta_compu == "Piedra":
                    print("Empate!")
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
                elif respuesta_compu == "Papel":
                    print("Pierdes!")
                    print("Papel gana a Piedra. Pierdes!")
                    ptos_compu+=1
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
                elif respuesta_compu == "Tijeras":
                    print("Ganas!")
                    print("Piedra gana a Tijeras. Ganas!")
                    ptos_jugador+=1
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
            elif pregunta =="Papel":
                if respuesta_compu == "Piedra":
                    print("Ganas!")
                    print("Papel gana a Piedra.!")
                    ptos_jugador+=1
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")                  
                elif respuesta_compu == "Papel":
                    print("Papel empata a Papel.!")
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
                elif respuesta_compu == "Tijeras":
                    print("Pierdes!")
                    print("Tijeras gana a papel!")
                    ptos_compu+=1
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
            elif pregunta =="Tijeras":
                if respuesta_compu == "Piedra":
                    print("Pierdes!")
                    print("Piedra gana a Tijeras.!")
                    ptos_compu+=1
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")                  
                elif respuesta_compu == "Papel":
                    print("Ganas!")
                    print("Papel gana a Tijeras.!")
                    ptos_jugador+=1
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
                elif respuesta_compu == "Tijeras":
                    print("Empatas!")
                    print("Tijeras empata a Tijeras!")
                    print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
            salida=input("Quieres Jugar?")
        else:
            print(f"Ptos Jugador: {ptos_jugador} - Ptos Compu: {ptos_compu}")
            return False    
            

jugarPPT()