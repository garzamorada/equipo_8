class Menu():
    def __init__(self,sistema):
        self.main=sistema
        self.usuarioActual=None

    def login(self):
        print(' ')
        print('-'.center(84,'-'))
        email = input('ingrese su email: ')
        password = input('ingrese su password: ')
        print('-'.center(84,'-'))
        print(' ')

        self.usuarioActual=self.main.retornaUsuario(email,password)
        self.usuarioActual.print()

        if self.usuarioActual.level == 'cliente':
            self.usuarioActual.menuOpciones(self)
        elif self.usuarioActual.level == 'admin':
            self.usuarioActual.menuAdmin(self)
        elif self.usuarioActual.level == 'reporter':
            self.usuarioActual.menuReporter(self)
    
    
    def deslog(self):
        self.usuarioActual=None
        print('deslogueado')
        tecla=None
        tecla=input('presione enter para continuar...')
        if tecla != None:
            self.muestraMenu()
    
    def registrarse(self):
        print(' ')
        print('-'.center(84,'-'))
        apellido = input('ingrese su apellido: ')
        nombre = input('ingrese su nombre: ')
        email = input('ingrese su email: ')
        password = input('ingrese su password: ')
        print('-'.center(84,'-'))
        print(' ')
        self.main.createUsuario(email,apellido,nombre,password,'cliente')
        print('usuario creado')
        tecla=None
        tecla=input('presione enter para continuar...')
        if tecla != None:
            self.muestraMenu()

    def muestraMenu(self):
        opcion = 0
        while opcion != 99:
            print('-'.center(84,'-'))
            print("Para loguearse ingrese 1.")
            print("Para registrarse ingrese 2.")
            print("Para desloguearse ingrese 3.")
            if self.usuarioActual != None:
                print('Para ir al menu de ',self.usuarioActual.level,' ingrese 4')
            print("Para salir ingrese 99.")
            print('-'.center(84,'-'))
            opcion = int(input("Ingrese su opción: "))
            if (opcion == 1):
                self.login()
            elif opcion == 2:
                self.registrarse()
            elif opcion == 3:
                self.deslog()
            elif opcion==4:
                if self.usuarioActual.level=='cliente':
                    self.usuarioActual.menuOpciones(self)
                elif self.usuarioActual.level=='admin':
                    self.usuarioActual.menuAdmin(self)
                elif self.usuarioActual.level=='reporter':
                    self.usuarioActual.menuReporter(self)
            elif opcion == 99:
                break
