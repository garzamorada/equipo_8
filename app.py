from src.extra_b import contarCaracteres
from src.ejercicio_1 import reemplazar
from src.ejercicio_2 import invertCase
from src.ejercicio_3 import cambiaCaracter
from src.ejercicio_4 import capitalize
from src.ejercicio_5 import segundo
from src.extra_a import traingulo
from clases.matriz import Vector,Matriz,cargaMatriz,cargaVector

def listaStingtoInt(lista):
    for i in range(len(lista)): lista[i] = int(lista[i] )
    return lista

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
        print('  10 - objeto matriz')
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
            listaStingtoInt(numeros)
            segundo(numeros)

        elif opcion == 6:
            numero=int(input('ingrese un numero: '))
            traingulo(numero)

        elif opcion == 7:
            cadenaExtraB=input('ingrese su cadena para contar caractares: ')
            contarCaracteres(cadenaExtraB)
        elif opcion == 10:
            matriz1=cargaMatriz()
            matriz2=cargaMatriz()
            vector1=cargaVector()
            matriz1.print()
            matriz2.print()
            vector1.print()
            resultadosuma=matriz1.suma(matriz2)
            resultadoresta=matriz1.resta(matriz2)
            resultadomultiplicacion=matriz1.multiplicacionVector(vector1)
            resultadodivision=matriz1.dividirVector(vector1)
            print(" el resultado de la suma es: ")
            resultadosuma.print()
            print(" el resultado de la resta es: ")
            resultadoresta.print()
            print(" el resultado de la multiplicacion es: ")
            resultadomultiplicacion.print()
            print(" el resultado de la division es: ")
            resultadodivision.print()

        else:
            break
        tecla=input ('presione retorno (enter) para continuar...')
        if tecla != None or tecla == None : 
            print('volviendo al menú...')

menuOpciones()





