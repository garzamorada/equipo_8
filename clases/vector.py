"""2 - Crear una clase que represente un vector de 3 dimensiones. 
Tenga 4 metodos que permitan las operaciones matematicas basicas (+,-,* y / por un escalar)."""

def cargaVector():
    print("  ")
    print("ingrese los elementos separados por coma")
    print("del vector de acuerdo al siguiente modelo:")
    print("  ")
    print("  a1  ")
    print("  a2  ")
    print("  a3  ")
    print("  ")
    elementos = input("elementos: a1,a2,a3: ").split(",")
    print("  ")

    a1 = int(elementos[0])
    a2 = int(elementos[1])
    a3 = int(elementos[2])

    return Vector(a1,a2,a3)

def cargaEscalar():
    print("  ")
    print("ingrese un númro entero: ")
    print("  ")
    escalar = int(input("escalar: "))
    print("  ")
    return escalar

class Vector():
    def __init__(self,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def print(self):
        print("  ")
        print("  vector:  ")
        print(str(self.a1).center(6))
        print(str(self.a2).center(6))
        print(str(self.a3).center(6))
        print("  ")
    
    def suma(self, vector):
        a1 = self.a1 + vector.a1
        a2 = self.a2 + vector.a2
        a3 = self.a3 + vector.a3
        return Vector(a1,a2,a3)
    
    def resta(self, vector):
        a1 = self.a1 - vector.a1
        a2 = self.a2 - vector.a2
        a3 = self.a3 - vector.a3
        return Vector(a1,a2,a3)
    
    def multiplicacion(self, escalar):
        a1 = self.a1 * escalar
        a2 = self.a2 * escalar
        a3 = self.a3 * escalar
        return Vector(a1,a2,a3)
    
    def division(self, escalar):
        a1 = round((self.a1 / escalar),2)
        a2 = round((self.a2 / escalar),2)
        a3 = round((self.a3 / escalar),2)
        return Vector(a1,a2,a3)