import math


# Ingresamos la entrada de texto "Ingresa aqui el radio del circulo: "
# Creamos la variable radio_circulo junto con un input para que el usario asigne el valor
while True:
    try:
        radio_circulo = float(input("Inserte aqui el radio de su circulo: "))
        break
    
    except:
        print("Error: ingrese un un valor numerico o un número válido con punto (.) y no con coma (,)")

# Creamos la variable area_circulo y realizamos la operacion para obtener el area del cuadrado.
# A la variable area_circulo asignamos la operacion  pi * (radio_circulo)2

area_circulo = math.pi * (radio_circulo**2)

# Devolvemos al usario la repuesta acerca del area del circulo
# Hacemos un print de area_circulo

print("El area de su circulo con radio:", radio_circulo, "es:", area_circulo)