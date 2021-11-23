from clases.ejercicio_4 import usuario
from clases.ejercicio_4 import emuladorDB


class Admin(Usuario):
    listado = []
    def __init__(self):
        self.level = 'admin'

    #No hace falta volver a decalarar metodos herederados de la clase padre (Usuario)

    def verUsuarios(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
            usuario.print()
    
     #Por defecto ponemos el self en los metodos
     #Llamo a los metdos del objeto que contiene las listas de usuarios y carritos
    

    def verCarrito(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
            usuario.carrito.print()