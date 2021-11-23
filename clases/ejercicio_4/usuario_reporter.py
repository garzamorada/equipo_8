from clases.ejercicio_4.usuario import Usuario

class Reporter(Usuario):
    def __init__(self):
        self.level = 'reporter'

def verCarritos(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
                usuario.carrito.print()


     #Llamo al metodo del objeto que contiene la lista de carritos