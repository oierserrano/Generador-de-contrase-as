import random
import string

# Pedir al usuario la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))

if longitud > 0: # Verificamos que la longitud sea mayor a 0

    # Generamos los caracteres para usar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generamos la contraseña con los caracteres seleccionados y la longitud especificada
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

    print("Contraseña generada:", contraseña)
else:
    print("La longitud de la contraseña no puede ser menor o igual a 0.")
