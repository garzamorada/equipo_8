class Carrito:
    def __init__(self):
        self.listaDeCompras=[]
        self.TotalAPagar=0
    
    def muestraProductos(self,emuladorDB):
        print('Codigo'.ljust(10),' - ','Nombre'.rjust(30),' : ','Precio'.ljust(11),' - ','Stock'.rjust(15))
        emuladorDB.listarProductosEnStock()
    
    def agregarAlCarrito(self,emuladorDB):
        print(' ')
        item=input('ingrese el codigo del producto: ')
        cantidad=int(input('ingrese la cantidad deseada: '))
        if item in emuladorDB.listaproductos:
            for producto in emuladorDB.listaProductos:
                if producto.codigo==item and producto.stock >= cantidad:
                    producto.stock=cantidad
                    self.listaDeCompras.append(producto)
                    self.TotalAPagar+=int(producto.precio)*cantidad
                elif producto.codigo==item and producto.stock < cantidad:
                    print(' ')
                    print('la cantidad supera al stock, por favor ingrese una cantidad menor')
        else:
            print(' ')
            print('No se encuentra el codigo de producto')
        
    def muestraCarrito(self):
        print('Codigo'.ljust(10),' - ','Nombre'.rjust(30),' : ','Precio'.ljust(11),' - ','Cantidad'.rjust(15))
        total=0
        for producto in self.listaDeCompras:
            producto.print()
            total+=producto.precio*producto.stock
        print( ' ')
        print('El total a pagar es ARS$ ',total)

    def menuOpciones(self,emuladorDB):
        opcion=0
        while opcion != 99:
            print('----------------------------------')
            print(' 1  -  Listar Productos en Stock')
            print(' 2  -  Ver Carrito de Compras')
            print(' 3  -  Vaciar Carrito de Compras')
            print(' 4  -  Confirmar Compra y Salir')
            print(' 5  -  Cancelar Compra y Salir')
            print('----------------------------------')
            opcion=int(input('ingrese la opcipn deseada: '))

            if opcion==1:
                self.muestraProductos(emuladorDB)
                self.agregarAlCarrito(emuladorDB)
            elif opcion==2:
                self.muestraCarrito()
            elif opcion==3:
                self.listaDeCompras.clear()
            elif opcion==4:
                for producto in self.listaDeCompras:
                    emuladorDB.updateProducto(producto.codigo,'restastock',producto.stock)
                print('el total a pagar es de ARS$ ',self.TotalAPagar)
                print('gracias por su compra')
                opcion=99
                break
            elif opcion==5:
                self.listaDeCompras.clear()
                print('lo esperamos nuevamente')
                opcion==99
                break


