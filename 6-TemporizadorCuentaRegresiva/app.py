#Temporizador de Cuenta Regresiva
#Usar modulo time
#Copiado de https://www.youtube.com/watch?v=SqvVm3QiQVk&t=2531s

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -=1
    print("Timer completede!")

t= input("Enter the time in seconds: ")
t = int(t)

countdown(t)

