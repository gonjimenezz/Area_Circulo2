nombre1 = input("Hola Jugador 1! ¿Cual es tu nombre? : ")
nombre2 = input("Hola Jugador 2! ¿Cual es tu nombre? : ")

puntos1 = 0
puntos2 = 0

while puntos1 < 3 and puntos2 < 3:
    jugador1 = input(f"Ok {nombre1}, vamos a jugar! Que eliges, ¿piedra papel o tijera?: " )
    jugador2 = input(f"Ok {nombre2}, vamos a jugar! Que eliges, ¿piedra papel o tijera?: " )

    condicion_1 = jugador1 == "tijera" and jugador2 == "papel" 
    condicion_2 = jugador1 == "papel" and jugador2 == "piedra" 
    condicion_3 = jugador1 == "piedra" and jugador2 == "tijera"
    
    if jugador1 == jugador2:
        print("ha sido un empate")
    
    elif condicion_1 or condicion_2 or condicion_3:
        print(f"Gano {nombre1} , suma 1 punto")
        puntos1 += 1
    else:
        print(f"Gano {nombre2} , suma 1 punto")
        puntos1 += 1

    print(f"marcador {nombre1} {puntos1} - {nombre2} {puntos2}\n")

if puntos1 == 3:
    print(f"Ha ganado {nombre1}")

else:
    print(f"Ha ganado {nombre2}")