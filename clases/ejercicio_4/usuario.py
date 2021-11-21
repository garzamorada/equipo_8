class Usuario(object):
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def presentarse(self):
        print("-" * 20)
        print(f"""Hola soy {self.nombre} {self.apellido}.
               Mi email es {self.email} y mi password es {self.password}""")
        print("-" * 20)

    def validarPassword(self):
        passwordIngresada = input(f"Ingrese su password: ")
        if passwordIngresada == self.password:
            print("La password es correcta")
            print("-" * 20)
            return True
        else:
            print(f"La password es incorrecta. Intente nuevamente")
            print("-" * 20)

    def cambiarPassword(self):
        print(f"Para cambiar su contraseña necesitamos verificarlo como usuario")
        if self.validarPassword() == True:
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

    def cambiarEmail(self):
        print(f"Para cambiar su email necesitamos verificarlo como usuario")
        if self.validarPassword() == True:
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


Juan = Usuario("juan", "carlos", "juancarlos@gmail.com", "password")
Juan.presentarse()
Juan.cambiarPassword()
Juan.cambiarEmail()
Juan.presentarse()
