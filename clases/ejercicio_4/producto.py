class Producto:
    def __init__(self,codigo,nombre,precio,cantidad):
        self.codigo=str(codigo)
        self.nombre=str(nombre)
        self.precio=precio
        self.cantidad=cantidad

    def print(self):
        print(self.codigo.ljust(10),' - ',self.nombre.rjust(30),' : ','ARS $',str(self.precio).ljust(6),' - ',str(self.stock).rjust(6),' unidades')
        
