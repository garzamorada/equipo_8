"""esta clase va a manejar las fracciones"""

def validaEntero(funcion):
    def validar(**kwargs):
        try:
            numero1=int(kwargs['numerador'])
            numero2=int(kwargs['denominador'])
        except ValueError:
            print('los numeros deben ser enteros')
        return funcion(numero1, numero2)
    return validar


class Fraccion:
    """esta clase va a manejar las fracciones"""
    atributoComun='xxx'
    @validaEntero
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)
    
    def sumar(self, otraFraccion):
        if self.denominador == otraFraccion.denominador:
            nuevoNumerador = self.numerador + otraFraccion.numerador
            nuevoDenominador = self.denominador
        else:
            nuevoDenominador=self.mcm(self.denominador, otraFraccion.denominador)
            nuevoNumerador=self.numerador*int(nuevoDenominador/self.denominador) + otraFraccion.numerador*int(nuevoDenominador/otraFraccion.denominador)     
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def restar(self, otraFraccion):
        if self.denominador == otraFraccion.denominador:
            nuevoNumerador = self.numerador - otraFraccion.numerador
            nuevoDenominador = self.denominador
        else:
            nuevoDenominador=self.mcm(self.denominador, otraFraccion.denominador)
            nuevoNumerador=self.numerador*int(nuevoDenominador/self.denominador) - otraFraccion.numerador*(nuevoDenominador/otraFraccion.denominador)     
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def mcm(self,numero1, numero2):
        lista1=[]
        lista2=[]
        lista3=[]
        for i in range(1,10):
            lista1.append(numero1*i)
            lista2.append(numero2*i)
        for numero in lista1:
            if numero in lista2:
                lista3.append(numero)
        if len(lista3)==0:
            return numero1*numero2
        else:
            return min(lista3)

    def MCD(self,numero1, numero2):
        lista1=[]
        lista2=[]
        lista3=[]
        for i in range(1,numero1+1):
            if numero1%i==0:
                lista1.append(i)
        for i in range(1,numero2+1):
            if numero2%i==0:
                lista2.append(i)
        for numero in lista1:
            if numero in lista2:
                lista3.append(numero)
        return max(lista3)

    def simplificar(self):
        MCD=self.MCD(self.numerador, self.denominador) 
        return Fraccion(self.numerador/MCD, self.denominador/MCD)
    
    def multiplicar(self, otraFraccion):
        pass
    
    def dividir(self, otraFraccion):
        pass
    
@validaEntero
def carga():
    fraccion=input('ingrese la fraccion separada por ,: ')
    numeros=fraccion.split(',')
    numerador=int(numeros[0])
    denominador=int(numeros[1])
    return Fraccion(numerador, denominador)

fraccion1=carga()
fraccion2=carga()
print(fraccion1)
print(fraccion2)
print(fraccion1.restar(fraccion2))
fraccion3=fraccion1.sumar(fraccion2)
print(fraccion3)
print(fraccion3.simplificar())
