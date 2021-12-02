from usuario_cliente import Cliente
from usuario_admin import Admin
from usuario_reporter import Reporter
from producto import Producto

class Sistema:
    def __init__(self):
        self.listaUsuarios=[]
        self.listaProductos=[]

    def listarUsuarios(self,level='cliente'):
        for usuario in self.listaUsuarios:
            if usuario.level==level:
                usuario.print()

    def listarProductos(self):
        for producto in self.listaProductos:
            producto.print()

    def listarProductosEnStock(self):
        for producto in self.listaProductos:
            if producto.cantidad > 0: producto.print()


    def createUsuario(self,email,apellido,nombre,password,level):
        if level == 'cliente':
            usuario= Cliente(email,apellido,nombre,password,self)
        elif level == 'admin':
            usuario= Admin(email,apellido,nombre,password,self)
        elif level == 'reporter':
            usuario= Reporter(email,apellido,nombre,password,self)
                
        self.listaUsuarios.append(usuario)

    def validaPassword(self,email,password):
        for user in self.listaUsuarios:
            if user.email == email and user.password == password: 
                return True
            else:
                return False

    def retornaUsuario(self,email,password):
        for user in self.listaUsuarios:
            if user.email == email and user.password == password:
                if user.email == email: return user

    def createProducto(self,codigo,nombre,precio,stock):
        producto=Producto(codigo,nombre,precio,stock)
        self.listaProductos.append(producto)

    def updateProducto(self,codigo,opcion,valor):
        for producto in self.listaProductos:
            if producto.codigo == codigo:
                if opcion=='precio':
                    producto.precio=valor
                    break
                elif opcion=='nombre':
                    producto.nombre=valor
                    break
                elif opcion=='restastock':
                    producto.cantidad=producto.cantidad-valor
                    break
                elif opcion=='stock':
                    producto.cantidad=valor
                    break

            
