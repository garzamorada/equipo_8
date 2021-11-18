#Extra: a- Escribir una funcion que recibe un numero entero 
# y imprima por salida estandar(usando print) un triangulo de numeros 
# de altura igual al numero ingresado. Ej. Si se ingresa el numero 5, 
# debe imprimir:  1 22 333 4444 55555

def traingulo(input):
    for i in range(1, input+1):
        print (str(i)*i)
    
#traingulo(5)