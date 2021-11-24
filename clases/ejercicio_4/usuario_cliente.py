from usuario import Usuario
from carrito import Carrito

class Cliente(Usuario):
    def __init__(self,email, nombre, apellido, password):
        Usuario.__init__(self, email, nombre, apellido, password)
        self.level = "cliente"
        self.carrito = Carrito() 
    
    def menuOpciones(self, emuladorDB):
        opcion=0
        while opcion != 99:
            print('----------------------------------')
            print(' 1  -  Listar Productos en Stock')
            print(' 2  -  Ver Carrito de Compras')
            print(' 3  -  Agregar productos al carrito')
            print(' 4  -  Eliminar producto del Carrito')
            print(' 5  -  Vaciar Carrito de Compras')
            print(' 6  -  Confirmar Compra y Salir')
            print(' 7  -  Cancelar Compra y Salir')
            print('----------------------------------')
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion==1:
                self.carrito.muestraProductos(emuladorDB)
            elif opcion==2:
                self.carrito.muestraCarrito()
            elif opcion==4:
                self.carrito.eliminarDelCarrito()
            elif opcion==5:
                self.carrito.listaDeCompras.clear()
            elif opcion==6:
                for producto in self.carrito.listaDeCompras:
                    emuladorDB.updateProducto(producto.codigo,'restastock',producto.stock)
                print('el total a pagar es de ARS$ ', self.carrito.TotalAPagar)
                print('gracias por su compra')
                opcion=99
            elif opcion==7:
                self.carrito.listaDeCompras.clear()
                print('lo esperamos nuevamente')
                opcion==99
                break
            elif opcion==3:
                self.carrito.agregarAlCarrito(emuladorDB)
            
            print(' ')
            print('-----------------------------------------------')
            tecla=input ('presione retorno (enter) para continuar...')
            print(' ')
            if tecla != None or tecla == None : 
                print('volviendo al menú...')
            print(' ')
        
    