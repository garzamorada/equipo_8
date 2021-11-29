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
            print(' 3  -  Listar Productos')
            print(' 4  -  Listar Productos en stock')
            print(' 5  -  Modificar stock de producto')
            print(' 6  -  Modificar nombre de producto')
            print(' 7  -  Modificar precio de producto')
            print(' 8  -  Alta de productos')
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
            elif opcion == 3:
                print(' ')
                print('-'.center(84,'-'))
                self.sistema.listarProductos()
                print('-'.center(84,'-'))
                print(' ')
            elif opcion == 4:
                print(' ')
                print('-'.center(84,'-'))
                self.sistema.listarProductosEnStock()
                print('-'.center(84,'-'))
                print(' ')
            elif opcion == 5:
                print(' ')
                print('-'.center(84,'-'))
                codigo=input('ingrese el codigo del producto: ')
                valor=int(input('ingrese la cantidad del stock: '))
                self.sistema.updateProducto(codigo,'stock',valor)
                print('-'.center(84,'-'))
                print(' ')
            elif opcion == 6:
                print(' ')
                print('-'.center(84,'-'))
                codigo=input('ingrese el codigo del producto: ')
                valor=input('ingrese el nuevo nombre del prducto: ')
                self.sistema.updateProducto(codigo,'nombre',valor)
                print('-'.center(84,'-'))
                print(' ')
            elif opcion == 7:
                print(' ')
                print('-'.center(84,'-'))
                codigo=input('ingrese el codigo del producto: ')
                valor=int(input('ingrese el nuevo precio del producto: '))
                self.sistema.updateProducto(codigo,'precio',valor)
                print('-'.center(84,'-'))
                print(' ')
            elif opcion == 8:
                print(' ')
                print('-'.center(84,'-'))
                nombre=input('ingrese el nombre del producto: ')
                stock=int(input('ingrese el stock del producto: '))
                precio=int(input('ingrese el precio del producto: '))
                ultimo=self.sistema.listaProductos[-1].codigo
                nuevonro=int(ultimo.lstrip('0'))+1
                codigo=str(nuevonro).zfill(5)
                self.sistema.createProducto(codigo,nombre,precio,stock)
                print(' el codigo de producto asignado es: ', codigo)
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





