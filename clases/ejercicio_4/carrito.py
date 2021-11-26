from producto import Producto

class Carrito:
    def __init__(self,sistema):
        self.listaDeCompras=[]
        self.TotalAPagar=0
        self.sistema=sistema
    
    def muestraProductos(self):
        print('Codigo'.ljust(10),' - ','Nombre'.rjust(30),' : ','Precio'.ljust(11),' - ','cantidad'.rjust(15))
        self.sistema.listarProductosEnStock()
    
    def agregarAlCarrito(self):
        self.muestraProductos()
        print(' ')
        item=input('ingrese el codigo del producto: ')
        cantidad=int(input('ingrese la cantidad deseada: '))
        find = False
        for producto in self.sistema.listaProductos:
            if producto.codigo==item and producto.cantidad >= cantidad:
                productoCarrito=Producto(item,producto.nombre,producto.precio,cantidad)
                self.listaDeCompras.append(productoCarrito)
                self.TotalAPagar+=int(producto.precio)*cantidad
                find = True
            elif producto.codigo==item and producto.cantidad < cantidad:
                print(' ')
                print('la cantidad supera al cantidad, por favor ingrese una cantidad menor')
                find = True
        if find == False:
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

    def eliminarDelCarrito(self):
        self.muestraCarrito()
        print(' ')
        item=input('ingrese el codigo del producto a eliminar: ')
        for producto in self.listaDeCompras:
            if producto.codigo == item:
                self.TotalAPagar = self.TotalAPagar-(producto.precio*producto.cantidad)
                self.listaDeCompras.remove(producto)
                print('se elimino el producto de la lista')
                print('El total a pagar es ARS$ ',self.TotalAPagar)


