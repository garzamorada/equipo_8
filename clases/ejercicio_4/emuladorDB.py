class emuladorDB:
    def __init__(self):
        self.listaUsuarios=[]
        self.listaProductos=[]

    def addProducto(self,producto):
       self.listaProductos.append(producto)

    def addUsuario(self,usuario):
        self.listaUsuarios.append(usuario)

    def listarUsuarios(self,level='cliente'):
        for usuario in self.listaUsuarios:
            if usuario.level==level:
                usuario.print()


    def listarProductos(self):
        for producto in self.listaProductos:
            producto.print()

    def listarProductosEnStock(self):
        for producto in self.listaProductos:
            if producto.stock > 0: producto.print()

    def updateUsuario(self,email,opcion,valor):
        for user in self.listaUsuarios:
            if user.email == email:
                if opcion=='password':
                    user.password=valor
                    break
                elif opcion=='email':
                    user.email=valor
                    break

    def createUsuario(self,email,apellido,nombre,password,level):
        if level == 'cliente':
            usuario= Cliente(email,apellido,nombre,password,level)
        elif level == 'admin':
            usuario= Admin(email,apellido,nombre,password,level)
        elif level == 'reporter':
            usuario= Reporter(email,apellido,nombre,password,level)
                
        self.addUsuario(usuario)

    def validaPassword(self,email,password):
        for user in self.listaUsuarios:
            if user.email == email and user.password == password: 
                return True
            else:
                return False

    def createProducto(self,codigo,nombre,precio,stock):
        producto=Producto(codigo,nombre,precio,stock)
        self.addProducto(producto)

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
                    producto.stock=producto.stock-valor
                    break
                elif opcion=='sumastock':
                    producto.stock=producto.stock+valor
                    break

            
