from usuario import Usuario
from carrito import Carrito

class Cliente(Usuario):
    def __init__(self, email, nombre, apellido, password, level):
        Usuario.__init__(self, email, nombre, apellido, password, level)
        self.level = "cliente"
        self.carrito = Carrito() 
    
    def menuOpciones(self, emuladorDB):
        opcion=0
        while opcion != 99:
            print('----------------------------------')
            print(' 1  -  Listar Productos en Stock')
            print(' 2  -  Ver Carrito de Compras')
            print(' 3  -  Eliminar producto del Carrito')
            print(' 4  -  Vaciar Carrito de Compras')
            print(' 5  -  Confirmar Compra y Salir')
            print(' 6  -  Cancelar Compra y Salir')
            print(' 7  -  Agregar productos al carrito')
            print('----------------------------------')
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion==1:
                self.carrito.muestraProductos(emuladorDB)
            elif opcion==2:
                self.carrito.muestraCarrito()
            elif opcion==3:
                self.carrito.eliminarDelCarrito()
            elif opcion==4:
                self.carrito.listaDeCompras.clear()
            elif opcion==5:
                for producto in self.carrito.listaDeCompras:
                    emuladorDB.updateProducto(producto.codigo,'restastock',producto.stock)
                print('el total a pagar es de ARS$ ', self.carrito.TotalAPagar)
                print('gracias por su compra')
                opcion=99
                break
            elif opcion==6:
                self.listaDeCompras.clear()
                print('lo esperamos nuevamente')
                opcion==99
                break
            elif opcion==7:
                self.carrito.agregarAlCarrito(emuladorDB)
        
    