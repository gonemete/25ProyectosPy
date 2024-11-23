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

print(eleccion)
palabra_adivinada=[]
for letra in eleccion:
    palabra_adivinada.append("*")

separador = " "  # Aqui puedes poner si prefieres ", "
cadena = "".join(str(parte) for parte in palabra_adivinada)
print(cadena)

pregunta=input("Dime una letra: ")

if letra in eleccion:
    indice=eleccion.index(letra)

    
palabra_adivinada[indice]=letra

print(cadena)