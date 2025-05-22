#Analizamos si el usuario puede ingresar a la disco con su edad

edad_usuario = int(input("Ingrese aqui su edad: "))

#Se analiza a traves de una operacion si el usario puede ingresar

permitido = True

if edad_usuario >= 18:
    permitido = True
else:
    permitido = False

#Se le responde al usuario

if permitido == True:
    print("Tiene permitido ingresar a la disco")
else:
    print("No puede ingresar a la disco")
