#Construir un contador de tiempo usando el módulo time de Python.
#Uso de bucles while en Python.


import time

def cuenta_atras(tiempo:int):
    print("Empieza la cuenta Atrás!")
    time.sleep(0.5)
    contador=tiempo
    while contador>0:
        print(f"Faltan: {contador} segundos para el despegue!")
        contador-=1
        time.sleep(1)
    print("Adelanteeeee!")

cuenta_atras(10)