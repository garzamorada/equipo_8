"""
b- Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) 
y devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente. 
Ejemplo. "Codo a Codo" Debe imprimir:
o 4
c 2
d 2
"""

def contarCaracteres(string):
    letrasunicas=''
    for i in range(len(string)): 
        if letrasunicas.count(string[i])==0: letrasunicas+=string[i]
    pares=[]
    for i in letrasunicas: 
        if i != ' ': pares.append((i,string.count(i)))
    pares.sort(key=lambda x: x[1], reverse=True)
    for i in range(0,3): print(pares[i][0],' ',pares[i][1])
