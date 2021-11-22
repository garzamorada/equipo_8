class emuladorDB()
    self.listaUsuarios=[]
    self.listaProductos=[]

    def addProducto(self,producto)
        self.listaProdcutos.append(producto)

    def addUsuario(self,usuario)
        self.listaUsuarios.append(usuario)

    def listarUsuarios(self)
        for usuario in listaUsuarios:
            usuario.print()

    def listarProductos(self)
        for producto in listaProductos:
            producto.print()

    def listarProductosEnStock(self)
        for producto in listaProductos:
            if producto.stock > 0: producto.print()

    def updateUsuario(self,email,opcion,valor)
        for user in self.listaUsuarios:
            if user.email == email:
                if opcion=='password'
                    user.password=valor
                    break
                elif opcion=='email'
                    user.email=email
                    break

    def createUsuario(self,email,apellido,nombre,password,level)
        if level == 'cliente':
            usuario= cliente(email,apellido,nombre,password,level)
        elif level == 'admin'
            usuario= admin(email,apellido,nombre,password,level)
        elif level == 'reporter'
            usuario= reporter(email,apellido,nombre,password,level)
                
        self.addUsuario(usuario)

    def validaPassword(self,email,password)
        for user in self.listaUsuarios:
            if user.email == email and user.password == password: 
                return True
            else:
                return False

            
