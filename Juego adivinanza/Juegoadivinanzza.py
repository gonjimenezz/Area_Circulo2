

import random


Numero_secreto = random.randint(0,100)
Adivinado = False
cantidad_intentos = 0
cant_max_int = 6

print("Bienvenidos a Jugar con Susi!!")

while not Adivinado and cantidad_intentos < cant_max_int:
    entrada = input("Introduce un Numero del 0 al 99: ")
    numero = int(entrada)

    if numero == Numero_secreto:
        print("Felicitaciones lo has logrado")
        Adivinado = True

    elif numero < Numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")

    cantidad_intentos += 1

if not cantidad_intentos < cant_max_int:
    print("Pediste maestro; max 5 intentos")



