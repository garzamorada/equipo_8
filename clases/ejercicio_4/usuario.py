class Usuario:
    def __init__(self, usuario, nombre, apellido, email, password):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def presentarse(self):
        print("-" * 20)
        print(f"""Hola soy {self.nombre} {self.apellido}.
               Mi email es {self.email} y mi password es {self.password}""")
        print("-" * 20)

    # Pide al usuario una clave y chequea si es 
    # la misma que fue declarada al crear el usuario
    # Es usada para validar al usuario al cambiar su email y password
    def login(self):
        enteredUsuario = input(f"Ingrese su usuario: ")
        enteredPassword = input(f"Ingrese su contraseña: ")
        if self.usuario == enteredUsuario  and self.password == enteredPassword:
            print("Usted ha sido verificado")
            print("-" * 20)
            return True
        
        elif self.password != enteredPassword:
            print (f"Contraseña incorrecta")
                    
        elif self.usuario not in listaUsuarios:
            print(f"No encontramos un usuario con ese nombre")
            print("-" * 20)
    
    # Valida al usuario como tal con validarPassword()
    # Si la contraseña que ingresa es correcta pide que se ingrese la nueva contraseña 2 veces
    # Si las contraseñas ingresadas son iguales, actualiza el valor self.password 
    def cambiarPassword(self):
        print(f"Para cambiar su contraseña necesitamos verificarlo como usuario")
        if self.login() == True:
            newPassword = input(f"Ingrese su nueva password: ")
            retryNewPassword = input(f"Para confirmar, ingrese nuevamente su nueva password: ")
            
            if newPassword == retryNewPassword:
                self.password = newPassword
                print(f"Su password ha sido cambiada a {self.password} ")
            else:
                print(f"Sus passwords no coinciden. Ingreso {newPassword} y {retryNewPassword}")
        else:
            print(f"La password es incorrecta. Intente nuevamente")
            print("-" * 20)
    
    # Idéntico en estructura a cambiarPassword()
    # Valida al usuario como tal con login()
    # Si la contraseña que ingresa es correcta pide que se ingrese la contraseña
    # Si las contraseñas ingresadas son iguales, actualiza el valor self.email 
    def cambiarEmail(self):
        print(f"Para cambiar su email necesitamos verificarlo como usuario")
        
        if self.login() == True:
            newEmail = input(f"Ingrese su nuevo email: ")
            retrynewEmail = input(f"Para confirmar, ingrese nuevamente su nuevo email: ")

            if newEmail == retrynewEmail:
                self.email = newEmail
                print(f"Su email ha sido cambiado a {self.email} ")
            
            else:
                print(f"Sus email no coinciden. Ingreso {newEmail} y {retrynewEmail}")
        
        else:
            print(f"La password es incorrecta. Intente nuevamente")
            print("-" * 20)


Juan = Usuario("carlos", "juancarlos@gmail.com", "password")
Juan.presentarse()
Juan.cambiarPassword()
Juan.cambiarEmail()
Juan.presentarse()
