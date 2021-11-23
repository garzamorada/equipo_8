from usuario import Usuario

class Cliente(Usuario):
    def __init__(self, usuario, nombre, apellido, email):
        Usuario.__init__(self, usuario, nombre, apellido, email)
        
    