#Juego del ahorcado
#Se usan diccionarios, listas, u condicionales if anidados. 
#También aprenderás como trabajar con cadenas y módulos aleatorios de Python

import random

palabras = [
    "sol", "luna", "estrella", "mar", "cielo", "montaña", "río", "bosque", 
    "flor", "viento", "trueno", "fuego", "arena", "nieve", "hoja", 
    "piedra", "ave", "pez", "camino", "puerta"
]


eleccion = random.choice(palabras)
