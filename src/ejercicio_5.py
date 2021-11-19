# 4- Escribir una funcion que reciba un string con nombre y apellido 
# y devuelva un string con el nombre y apellido 
# pero con capitalizacion(primera letra mayuscula).

""" hay un metodo de strings que hace esto mismo es capitalize(), podes probar hacerlo con ese metodo para acortar código"""

def capitalize(input):
    try:
        # nombres = [nombre.capitalize() for nombre in input.split(" ")]
        print (" ".join(nombre.capitalize() for nombre in input.split(" ")))
    except:
        print ("Ingrese un nombre y apellido")

# capitalize("iago martin edelstein")
# capitalize("manuel")


<<<<<<< HEAD:src/ejercicio_5.py
"podemos probar mandar un segundo parametro y hacer los triangulos centrados, a la izquierda o derecha usando los metodos center(), rjust() y ljust()"

def traingulo(input):
    for i in range(1, input+1):
        print (str(i)*i)
    
#traingulo(5)


# b- Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) 
# y devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente. 
# Ejemplo. "Codo a Codo" Debe imprimir:  o 4 c 2 d 2
def countLetters(input):
    listaLetras = list(input)    
    f   
=======
>>>>>>> 81acf6de3ce46a5897e39bcd61c8e01d7cd6bf25:src/Ej 5.py
