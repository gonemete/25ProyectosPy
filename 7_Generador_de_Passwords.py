#construir un generador aleatorio de contraseñas.
#Coleccionarás datos del usuario basándose en el número de contraseñas y su longitud
#Uso de random y bucles for.

import random


begin = ord('a')
end = ord('z')+1

letras =[]
for i in range(begin, end):
    letras.append(chr(i))

# print(letras)

numeros=[]
for i in range(0,9):
    numeros.append(str(i))

# print(numeros)

simbolos=["@","!","#","$","&","/","(",")","?","+","*","-","_",".",","]
# print(simbolos)
passw=[]
i=0
while i<10:
    a=random.randint(1,3)
    print(a)
    if a==1:
        passw.append(random.choice(simbolos))
        i+=1
        a=random.randint(1,3)
    elif a==2:
        passw.append(random.choice(letras))
        i+=1
        a=random.randint(1,3)
    elif a==3:
        passw.append(random.choice(numeros))
        i+=1
        a=random.randint(1,3)
nombre=str(passw)
print(nombre)
print(f"El pass: {' '.join(passw)}")