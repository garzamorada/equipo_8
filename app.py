from src.extra_b import *


cadenaExtraB=input('ingrese su cadena para contar caractares: ')
contarCaracteres(cadenaExtraB)

# Inicio - Ejercicio nro.3
print(
""" 3- Los strings son inmutables, escribir una funcion que reciba 
    un string, un indice y una letra a modificar de ese string y 
    que devuelve el string modificado.""")
cadenaIni3=input('Ingrese la cadena inicial: ')
indice3=input('Ingrese el indice: ')
nvoCaracter3=input('Ingrese el nuevo caracter: ')
i3=int(indice3)
print(cadenaIni3[0:i3]+nvoCaracter3[0:1]+cadenaIni3[i3+1:])
# Fin - Ejercicio nro.3