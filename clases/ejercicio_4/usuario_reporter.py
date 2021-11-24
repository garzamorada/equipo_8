from usuario import Usuario

class Reporter(Usuario):
    def __init__(self,email, nombre, apellido, password):
        Usuario.__init__(self, email, nombre, apellido, password)
        self.level = 'reporter'

    def verCarritos(self,listaUsuarios):
        for usuario in listaUsuarios:
            if usuario.level == 'cliente':
                print('-------------------------------------')
                print(' carrito del usuario',usuario.nombre,usuario.apellido)
                print(' ')
                usuario.carrito.muestraCarrito()
                print('-------------------------------------')

    def menuReporter(self,listaUsuarios):
        opcion=0
        while opcion != 99:
            print('----------------------------------')
            print(' 1  -  Ver Carritos de Compra')
            print(' 99 -  Terminar y Salir')
            print('----------------------------------')
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion == 1:
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


     #Llamo al metodo del objeto que contiene la lista de carritos