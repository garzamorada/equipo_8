from usuario import Usuario


class Admin(Usuario):

    def __init__(self,email, nombre, apellido, password,sistema):
        Usuario.__init__(self, email, nombre, apellido, password, sistema)
        self.level = 'admin'

    #No hace falta volver a decalarar metodos herederados de la clase padre (Usuario)

    def verUsuarios(self):
        for usuario in self.sistema.listaUsuarios:
            if usuario.level == 'cliente':
                usuario.print()
    
    def verCarritos(self):
        for usuario in self.sistema.listaUsuarios:
            if usuario.level == 'cliente':
                print('-'.center(84,'-'))
                print(' carrito del usuario',usuario.nombre,usuario.apellido)
                print(' ')
                usuario.carrito.muestraCarrito()
                print('-'.center(84,'-'))

    def menuAdmin(self):
        opcion=0
        while opcion != 99:
            print('-'.center(84,'-'))
            print(' 1  -  Listar Clientes')
            print(' 2  -  Ver Carritos de Compra')
            print(' 99 -  Terminar y Salir')
            print('-'.center(84,'-'))
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion == 1:
                print(' ')
                print('-'.center(84,'-'))
                self.verUsuarios()
                print('-'.center(84,'-'))
                print(' ')
            elif opcion == 2:
                print(' ')
                print('-'.center(84,'-'))
                self.verCarritos()
                print('-'.center(84,'-'))
                print(' ')
            else:
                print(' ')
                print(' hasta la proxima')
                opcion=99
                break

            print(' ')
            print('-'.center(84,'-'))
            tecla=input ('presione retorno (enter) para continuar...')
            print(' ')
            if tecla != None or tecla == None : 
                print('volviendo al menú...')
            print(' ')





