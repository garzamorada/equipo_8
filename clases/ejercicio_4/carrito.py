class Carrito:
    def __init__(self):
        self.listaDeCompras=[]
        self.TotalAPagar=0
    
    def muestraProductos(self,emuladorDB):
        print('Codigo'.ljust(10),' - ','Nombre'.rjust(30),' : ','Precio'.ljust(11),' - ','cantidad'.rjust(15))
        emuladorDB.listarProductosEnStock()
    
    def agregarAlCarrito(self,emuladorDB):
        print(' ')
        item=input('ingrese el codigo del producto: ')
        cantidad=int(input('ingrese la cantidad deseada: '))
        if item in emuladorDB.listaProductos:
            for producto in emuladorDB.listaProductos:
                if producto.codigo==item and producto.cantidad >= cantidad:
                    producto.cantidad=cantidad
                    self.listaDeCompras.append(producto)
                    self.TotalAPagar+=int(producto.precio)*cantidad
                elif producto.codigo==item and producto.cantidad < cantidad:
                    print(' ')
                    print('la cantidad supera al cantidad, por favor ingrese una cantidad menor')
        else:
            print(' ')
            print('No se encuentra el codigo de producto')
        
    def muestraCarrito(self):
        print('Codigo'.ljust(10),' - ','Nombre'.rjust(30),' : ','Precio'.ljust(11),' - ','Cantidad'.rjust(15))
        total=0
        for producto in self.listaDeCompras:
            producto.print()
            total+=producto.precio*producto.cantidad
        print( ' ')
        print('El total a pagar es ARS$ ',total)

    def eliminarDelCarrito(self,item):
        if item in self.listaDeCompras:
            for producto in self.listaDeCompras:
                if producto.codigo == item:
                    self.TotalAPagar = self.TotalAPagar-(producto.precio*producto.cantidad)
                    self.listaDeCompras.remove(producto)
        print('se elimino el producto de la lista')
        print('El total a pagar es ARS$ ',self.listaDeCompras)


