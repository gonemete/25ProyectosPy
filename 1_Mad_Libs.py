#Escribe una historia Mad Libs
#Uso de inputs y f-strings

nombre_persona=input("Escribe un nombre de persona: ")
sustantivo = input("Escribe un sustantivo: ")
adjetivo_sensacion = input("Escribe un adjetivo de sensación: ")
verbo = input("Escribe un verbo: ")
adjetivo_sensacion_2 = input("Escribe otro adjetivo de sensación: ")
animal = input("Escribe el nombre de un animal: ")
verbo_2 = input("Escribe otro verbo: ")
color= input("Escribe un color: ")
verbo_3 = input("Escribe otro verbo: ")
adverbio = input("Escribe un adverbio: ")
numero = input("Escribe un numero: ")
medida_de_tiempo = input("Escribe una medida de tiempo (Horas, minutos, segundos): ")
animal_2= input("Escribe el nombre de otro animal: ")
color_2= input("Escribe otro color: ")
numero_2 = input("Escribe un numero: ")
palabra_tonta = input("Escribe una tontada: ")
sustantivo_plural = input("Escribe un sustantivo plural: ")


print("MAD LIBS: ¡Vamos a acampar!")

print(f"""
Este fin de semana voy a acampar con {nombre_persona}. Empaqué mi linterna, saco de dormir, y {sustantivo}
.Estoy tan {adjetivo_sensacion} para {verbo} en una tienda de campaña. Estoy {adjetivo_sensacion_2} que vamos a ver un(a) {animal}, que son peligrosos.
Vamos a caminar, pescar, y {verbo_2}.
He oído que el lago {color} es genial para {verbo_3}. Entonces vamos a caminar {adverbio}  por del bosque para {numero} {medida_de_tiempo}.
Si veo un(a) {animal_2} {color_2} mientras estoy caminando, ¡lo llevaré a casa como mascota! Por la noche vamos a contar {numero_2} {palabra_tonta}  historias y asar {sustantivo_plural}  alrededor de la fogata !!
""")