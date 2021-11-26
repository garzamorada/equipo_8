from usuario import Usuario
from carrito import Carrito

class Cliente(Usuario):
    def __init__(self,email, nombre, apellido, password,sistema):
        Usuario.__init__(self, email, nombre, apellido, password, sistema)
        self.level = "cliente"
        self.carrito = Carrito(sistema)
    
    def menuOpciones(self):
        opcion=0
        while opcion != 99:
            print('-'.center(84,'-'))
            print(' 1  -  Listar Productos en Stock')
            print(' 2  -  Ver Carrito de Compras')
            print(' 3  -  Agregar productos al carrito')
            print(' 4  -  Eliminar producto del Carrito')
            print(' 5  -  Vaciar Carrito de Compras')
            print(' 6  -  Confirmar Compra y Salir')
            print(' 7  -  Cancelar Compra y Salir')
            print('-'.center(84,'-'))
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion==1:
                self.carrito.muestraProductos()
            elif opcion==2:
                self.carrito.muestraCarrito()
            elif opcion==4:
                self.carrito.eliminarDelCarrito()
            elif opcion==5:
                self.carrito.listaDeCompras.clear()
            elif opcion==6:
                for producto in self.carrito.listaDeCompras:
                    self.sistema.updateProducto(producto.codigo,'restastock',producto.stock)
                print('el total a pagar es de ARS$ ', self.carrito.TotalAPagar)
                print('gracias por su compra')
                opcion=99
            elif opcion==7:
                self.carrito.listaDeCompras.clear()
                print('lo esperamos nuevamente')
                opcion==99
                break
            elif opcion==3:
                self.carrito.agregarAlCarrito()
            
            print(' ')
            print('-'.center(84,'-'))
            tecla=input ('presione retorno (enter) para continuar...')
            print(' ')
            if tecla != None or tecla == None : 
                print('volviendo al menú...')
            print(' ')
        
    