class Usuario:
    def __init__(self, email, apellido, nombre,  password, sistema):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.sistema=sistema
        self.level = ""

    def print(self):
        print('-'.center(84,'-'))
        print(f"Nombre y Apellido: {self.nombre} {self.apellido}")
        print(f"Email: {self.email} - Password: {self.password}")
        print('-'.center(84,'-'))
       
    
    # Valida al usuario como tal con validarPassword()
    # Si la contraseña que ingresa es correcta pide que se ingrese la nueva contraseña 2 veces
    # Si las contraseñas ingresadas son iguales, actualiza el valor self.password 
    def cambiarPassword(self):
        print(f"Para cambiar su contraseña necesitamos verificarlo como usuario")
        password=input('ingrese su clave actual: ')
        if self.sistema.validaPassword(self.email,password) == True:
            newPassword = input(f"Ingrese su nueva password: ")
            retryNewPassword = input(f"Para confirmar, ingrese nuevamente su nueva password: ")
            
            if newPassword == retryNewPassword:
                self.password = newPassword
                print(f"Su password ha sido cambiada a {self.password} ")
            else:
                print(f"Sus passwords no coinciden. Ingreso {newPassword} y {retryNewPassword}")
        else:
            print(f"La password es incorrecta. Intente nuevamente")
            print('-'.center(84,'-'))
    
    # Idéntico en estructura a cambiarPassword()
    # Valida al usuario como tal con login()
    # Si la contraseña que ingresa es correcta pide que se ingrese la contraseña
    # Si las contraseñas ingresadas son iguales, actualiza el valor self.email 
    def cambiarEmail(self,emuladorDB):
        print(f"Para cambiar su contraseña necesitamos verificarlo como usuario")
        password=input('ingrese su clave actual: ')
        if emuladorDB.validaPassword(self.email,password) == True:
            newEmail = input(f"Ingrese su nuevo email: ")
            retrynewEmail = input(f"Para confirmar, ingrese nuevamente su nuevo email: ")

            if newEmail == retrynewEmail:
                self.email = newEmail
                print(f"Su email ha sido cambiado a {self.email} ")
            
            else:
                print(f"Sus email no coinciden. Ingreso {newEmail} y {retrynewEmail}")
        
        else:
            print(f"La password es incorrecta. Intente nuevamente")
            print('-'.center(84,'-'))
