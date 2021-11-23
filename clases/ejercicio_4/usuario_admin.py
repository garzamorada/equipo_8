from clases.ejercicio_4.usuario import Usuario


class Admin(Usuario):
    listado = []
    def __init__(self):
        self.level = 'admin'

    #No hace falta volver a decalarar metodos herederados de la clase padre (Usuario)

    def verUsuarios(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
                usuario.print()
    
    def verCarritos(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
                usuario.carrito.print()