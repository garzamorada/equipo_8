# 3- Los strings son inmutables, escribir una funcion que reciba 
#    un string, un indice y una letra a modificar de ese string y 
#    que devuelve el string modificado.""")
def cambiaCaracter(cadenaIni, indice, nvoCaracter):
    #cadenaIni=input('Ingrese la cadena inicial: ')
    #indice=input('Ingrese el indice: ')
    #nvoCaracter=input('Ingrese el nuevo caracter: ')
    i=int(indice)
    print(cadenaIni[0:i]+nvoCaracter[0:1]+cadenaIni[i+1:])

