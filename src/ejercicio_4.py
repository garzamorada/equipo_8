# 4- Escribir una funcion que reciba un string con nombre y apellido 
# y devuelva un string con el nombre y apellido 
# pero con capitalizacion(primera letra mayuscula).

def capitalize(input):
    try:
        # nombres = [nombre.capitalize() for nombre in input.split(" ")]
        print (" ".join(nombre.capitalize() for nombre in input.split(" ")))
    except:
        print ("Ingrese un nombre y apellido")

# capitalize("iago martin edelstein")
# capitalize("manuel")


