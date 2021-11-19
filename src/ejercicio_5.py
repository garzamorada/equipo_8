# 4- Escribir una funcion que reciba un string con nombre y apellido 
# y devuelva un string con el nombre y apellido 
# pero con capitalizacion(primera letra mayuscula).

""" hay un metodo de strings que hace esto mismo es capitalize(), podes probar hacerlo con ese metodo para acortar código"""

def capitalize(input):
    try:
        nombre, apellido = input.split()
        nombreUp = nombre[0].upper() + nombre[1:]
        apellidoUp = apellido[0].upper() + apellido[1:]
        print (nombreUp + " " + apellidoUp)
    except:
        print ("Ingrese un nombre y apellido")

# capitalize("iago edelstein")
# capitalize("manuel")

#Extra: a- Escribir una funcion que recibe un numero entero 
# y imprima por salida estandar(usando print) un triangulo de numeros 
# de altura igual al numero ingresado. Ej. Si se ingresa el numero 5, 
# debe imprimir:  1 22 333 4444 55555

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
