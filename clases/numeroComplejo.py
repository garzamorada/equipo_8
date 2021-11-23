"""
1 - Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matemaaticas basicas (+,-,*,/).
formulas: 
z = a + bi, w = c + di
suma: z + w = (a + c) + (b + d)i
resta: z - w = (a - c) + (b - d)i
multiplicacion: z * w = (a * c - b * d) + (a * d + b * c)i
division: z / w = (a * c + b * d) / (c * c + d * d) + ((b * c - a * d) / (c * c + d * d))i
"""

class NumeroComplejo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print(self):
        print("{} + {}i".format(self.a, self.b))


    def suma(self, complejo):
        return NumeroComplejo(self.a + complejo.a, self.b + complejo.b)

    def resta(self, complejo):
        return NumeroComplejo(self.a - complejo.a, self.b - complejo.b)

    def multiplicacion(self, complejo):
        return NumeroComplejo(self.a * complejo.a - self.b * complejo.b, self.a * complejo.b + self.b * complejo.a)

    def division(self, complejo):
        return NumeroComplejo(round((self.a * complejo.a + self.b * complejo.b) / (complejo.a * complejo.a + complejo.b * complejo.b),2),
                              round((self.b * complejo.a - self.a * complejo.b) / (complejo.a * complejo.a + complejo.b * complejo.b),2))

def cargaComplejo():
    print("  ")
    print("ingrese los elementos separados por coma")
    print("del complejo de acuerdo al siguiente modelo:")
    print("  ")
    print("  a + bi  ")
    print("  ")
    elementos = input("elementos: a,b: ").split(",")
    print("  ")

    a = int(elementos[0])
    b = int(elementos[1])

    return NumeroComplejo(a,b)