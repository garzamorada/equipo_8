from src.extra_b import contarCaracteres
from src.ejercicio_1 import reemplazar
from src.ejercicio_2 import invertCase
from src.ejercicio_3 import cambiaCaracter
from src.ejercicio_4 import capitalize
from src.ejercicio_5 import segundo
from src.extra_a import traingulo

def menuOpciones(opcion=0):
    while opcion != 99:
        print(' ')
        print('  seleccione una opcion:')
        print('  1  - ejercicio 1')
        print('  2  - ejercicio 2')
        print('  3  - ejercicio 3')
        print('  4  - ejercicio 4')
        print('  5  - ejercicio 5')
        print('  6  - extra a')
        print('  7  - extra b')
        print('  99 - terminar y salir')
        print(' ')
        opcion=int(input('ingrese el número de opcion: '))

        if opcion == 1:
            cadena=input('ingrese la cadena a remplazar espacios: ')
            reemplazar(cadena)

        elif opcion == 2:
            cadena=input('ingrese la cadena a cambiar mayusculas: ')
            invertCase(cadena)

        elif opcion == 3:
            cadenaIni=input('Ingrese la cadena inicial: ')
            indice=input('Ingrese el indice: ')
            nvoCaracter=input('Ingrese el nuevo caracter: ')
            cambiaCaracter(cadenaIni, indice, nvoCaracter)

        elif opcion == 4:
            cadena=input('ingrese la cadena para poner las iniciales en mayusculas: ')
            capitalize(cadena)
        
        elif opcion == 5:
            numeros=input('ingrese una lista de numero separados por coma: ').split(',')
            for i in range(len(numeros)): numeros[i] = int(numeros[i] )
            segundo(numeros)

        elif opcion == 6:
            numero=int(input('ingrese un numero: '))
            traingulo(numero)

        elif opcion == 7:
            cadenaExtraB=input('ingrese su cadena para contar caractares: ')
            contarCaracteres(cadenaExtraB)

        else:
            break

menuOpciones()





