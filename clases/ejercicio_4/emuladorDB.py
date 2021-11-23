class emuladorDB:
    def __init__(self):
        listaUsuarios=[]
        listaProductos=[]

    def addProducto(self,producto):
        listaProductos.append(producto)

    def addUsuario(self,usuario):
        listaUsuarios.append(usuario)

    def listarUsuarios(self):
        for usuario in listaUsuarios:
            usuario.print()

    def listarProductos(self):
        for producto in listaProductos:
            producto.print()

    def listarProductosEnStock(self):
        for producto in listaProductos:
            if producto.stock > 0: producto.print()

    def updateUsuario(self,email,opcion,valor):
        for user in self.listaUsuarios:
            if user.email == email:
                if opcion=='password':
                    user.password=valor
                    break
                elif opcion=='email':
                    user.email=email
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

            
