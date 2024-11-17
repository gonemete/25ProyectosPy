# El juego consiste en adivinar un número secreto generado por el programa por parte del usuario.
# Uso de de la biblioteca de python random, inputs, bucles y funciones
# Usamos random.randint() para generar un entero entre 1 y 100

import random
import time
numero_secreto = random.randint(1,100)

def adivinar_numero_compuntadora(numero):
    respuesta = int(input("Escribe el número secreto: "))
    while respuesta != numero:
        if respuesta>numero:
            print(f"{respuesta} no es el número, sigue intentándolo con un número menor.")
            respuesta=int(input("Escribe el número secreto: "))
            time.sleep(0.1)
        else:
            print(f"{respuesta} no es el número, sigue intentándolo con un número mayor.")
            respuesta=int(input("Escribe el número secreto: "))
            time.sleep(0.1)

    print(f"Enhorabuena {respuesta} es el número secreto.")

adivinar_numero_compuntadora(numero_secreto)



