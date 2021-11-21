"""3- Crear una clase que represente una matriz de 3x3 dimensiones. 
Tengan 4 metodos que permitan las operaciones matemaaticas basicas (+,-,* por un vector)."""

def cargaMatriz():
        print("  ")
        print("ingrese los elementos separados por coma")
        print("de la matriz de acuerdo al siguiente modelo:")
        print("  ")
        print("  a1  a2  a3  ")
        print("  b1  b2  b3  ")
        print("  c1  c2  c3  ")
        print("  ")
        elementos = input("elementos: a1,a2,a3,b1,b2,b3,c1,c2,c3: ").split(",")
        print("  ")

        a1 = int(elementos[0])
        a2 = int(elementos[1])
        a3 = int(elementos[2])
        b1 = int(elementos[3])
        b2 = int(elementos[4])
        b3 = int(elementos[5])
        c1 = int(elementos[6])
        c2 = int(elementos[7])
        c3 = int(elementos[8])

        return Matriz(a1,a2,a3,b1,b2,b3,c1,c2,c3)

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



class Matriz():
    def __init__(self,a1,a2,a3,b1,b2,b3,c1,c2,c3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def suma(self, matrizSumar):
        a1 = self.a1 + matrizSumar.a1
        a2 = self.a2 + matrizSumar.a2
        a3 = self.a3 + matrizSumar.a3
        b1 = self.b1 + matrizSumar.b1
        b2 = self.b2 + matrizSumar.b2
        b3 = self.b3 + matrizSumar.b3
        c1 = self.c1 + matrizSumar.c1
        c2 = self.c2 + matrizSumar.c2
        c3 = self.c3 + matrizSumar.c3
        return Matriz(a1, a2, a3, b1, b2, b3, c1, c2, c3)

    def resta(self, matrizRestar):
        a1 = self.a1 - matrizRestar.a1
        a2 = self.a2 - matrizRestar.a2
        a3 = self.a3 - matrizRestar.a3
        b1 = self.b1 - matrizRestar.b1
        b2 = self.b2 - matrizRestar.b2
        b3 = self.b3 - matrizRestar.b3
        c1 = self.c1 - matrizRestar.c1
        c2 = self.c2 - matrizRestar.c2
        c3 = self.c3 - matrizRestar.c3
        return Matriz(a1, a2, a3, b1, b2, b3, c1, c2, c3)
     
    def multiplicacionVector(self, vectorMultiplicar):
        a1 = (self.a1 * vectorMultiplicar.a1)+ (self.a2 * vectorMultiplicar.a2) + (self.a3 * vectorMultiplicar.a3)
        a2 = (self.b1 * vectorMultiplicar.a1 + self.b2 * vectorMultiplicar.a2 + self.b3 * vectorMultiplicar.a3)
        a3 = (self.c1 * vectorMultiplicar.a1 + self.c2 * vectorMultiplicar.a2 + self.c3 * vectorMultiplicar.a3)
        return Vector(a1, a2, a3)

    def matrizInversa(self):
        """
        a1 a2 a3     1 -1  1
        b1 b2 b3    -1  1 -1
        c1 c2 c3     1 -1  1
        """
        a1= ((self.a2 * self.c3) - (self.a3 * self.c2)) * 1
        a2= ((self.a3 * self.c1) - (self.a1 * self.c3)) * -1
        a3= ((self.a1 * self.c2) - (self.a2 * self.c1)) * 1
        b1= ((self.b2 * self.c3) - (self.b3 * self.c2)) * -1
        b2= ((self.b3 * self.c1) - (self.b1 * self.c3)) * 1
        b3= ((self.b1 * self.c2) - (self.b2 * self.c1)) * -1
        c1= ((self.c2 * self.a3) - (self.c3 * self.a2)) * 1
        c2= ((self.c3 * self.a1) - (self.c1 * self.a3)) * -1
        c3= ((self.c1 * self.a2) - (self.c2 * self.a1)) * 1
        return Matriz(a1, a2, a3, b1, b2, b3, c1, c2, c3)

    def dividirVector(self, vectorDividir):
        inversa =  self.matrizInversa()
        return inversa.multiplicacionVector(vectorDividir)


    def print(self):
        print("  ")
        print("  matriz:  ")
        print(str(self.a1).center(6) + str(self.a2).center(6) + str(self.a3).center(6))
        print(str(self.b1).center(6) + str(self.b2).center(6) + str(self.b3).center(6))
        print(str(self.c1).center(6) + str(self.c2).center(6) + str(self.c3).center(6))
        print("  ")


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



    