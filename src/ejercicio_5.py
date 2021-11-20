"""Ejercico 5 - Escribir una funcion que reciba N numeros, 
los cuales representan la puntuacion de un concurso, y esta devuelve
la puntuacion del subcampeon. 
(ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)
"""

def segundo(thislist):
    thislist.sort(reverse = True)
    for i in range(len(thislist)-1):
        if thislist[i] > thislist[i+1]:
            print("El segundo es: ", thislist[i+1])
            break