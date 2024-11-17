# El juego consiste en adivinar un número secreto generado por el programa
# Uso de de la biblioteca de python random, inputs, bucles y funciones
# Usamos random.randint() para generar un entero entre 1 y 100

import random
import time
numero_secreto = random.randint(1,100)

def adivinar_numero_compuntadora(numero):
    respuesta = random.randint(1,100)
    while respuesta != numero:
        if respuesta>numero:
            print(f"{respuesta} no es {numero}, sigue intentándolo con un número menor.")
            respuesta=random.randint(1,numero)
            time.sleep(1)
        else:
            print(f"{respuesta} no es {numero}, sigue intentándolo con un número mayor.")
            respuesta=random.randint(numero,100)
            time.sleep(1)


    print(f"Enhorabuena {respuesta} es el número secreto.")

adivinar_numero_compuntadora(numero_secreto)



