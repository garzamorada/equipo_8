from usuario import Usuario


class Admin(Usuario):

    def __init__(self,email, nombre, apellido, password):
        Usuario.__init__(self, email, nombre, apellido, password)
        self.level = 'admin'

    #No hace falta volver a decalarar metodos herederados de la clase padre (Usuario)

    def verUsuarios(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
                usuario.print()
    
    def verCarritos(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
                print('-------------------------------------')
                print(' carrito del usuario',usuario.nombre,usuario.apellido)
                print(' ')
                usuario.carrito.muestraCarrito()
                print('-------------------------------------')

    def menuAdmin(self,listaUsuarios):
        opcion=0
        while opcion != 99:
            print('----------------------------------')
            print(' 1  -  Listar Clientes')
            print(' 2  -  Ver Carritos de Compra')
            print(' 99 -  Terminar y Salir')
            print('----------------------------------')
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion == 1:
                print(' ')
                print('-----------------------------------------')
                self.verUsuarios(listaUsuarios)
                print('-----------------------------------------')
                print(' ')
            elif opcion == 2:
                print(' ')
                print('-----------------------------------------')
                self.verCarritos(listaUsuarios)
                print('-----------------------------------------')
                print(' ')
            else:
                print(' ')
                print(' hasta la proxima')
                opcion=99
                break

            print(' ')
            print('-----------------------------------------------')
            tecla=input ('presione retorno (enter) para continuar...')
            print(' ')
            if tecla != None or tecla == None : 
                print('volviendo al menú...')
            print(' ')





