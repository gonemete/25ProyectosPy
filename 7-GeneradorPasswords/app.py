#Generador de contraseñas
import random

caracteres='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZºª!@#$%&/()?+*--1234567890'

number=input('Cuantas contraseñas quieres generar?: ')
number=int(number)

longitud=input('Longuitud de la contraseña: ')
longitud=int(longitud)
print('\nEsta es tu contraseña: ')

for pwd in range(number):
    passwords = ''
    for c in range(longitud):
        passwords += random.choice(caracteres)
    print(passwords)
 