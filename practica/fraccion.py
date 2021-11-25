"""esta clase va a manejar las fracciones"""

def validaEntero(funcion):
    def validar(*args):
        if len(args) == 2:
            numero1=args[0]
            numero2=args[1]
            numero1=convierteTipo(numero1)
            numero2=convierteTipo(numero2)
            return funcion(numero1, numero2)
        elif len(args) == 3:
            numero1=args[1]
            numero2=args[2]
            numero1=convierteTipo(numero1)
            numero2=convierteTipo(numero2)
            return funcion(args[0], numero1, numero2)
        else: 
            print('Error: numero de argumentos invalido')
            return False        
    return validar


def convierteTipo(variable):
    if type(variable) == float:
        try:
            variable=int(round(variable))
        except Exception as e:
            print('Error: ', e)
    elif type(variable) == str:
        try:
            variable=int(variable)
        except Exception as e:
            print('Error: ', e)
    elif type(variable) == int:
        pass
    else:
        print('Error: los argumentos deben str, float o int')
        print('variable: ',type(variable))
        return False
    return variable


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
            nuevoNumerador=self.numerador*(nuevoDenominador/self.denominador) + otraFraccion.numerador*(nuevoDenominador/otraFraccion.denominador)     
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def restar(self, otraFraccion):
        if self.denominador == otraFraccion.denominador:
            nuevoNumerador = self.numerador - otraFraccion.numerador
            nuevoDenominador = self.denominador
        else:
            nuevoDenominador=self.mcm(self.denominador, otraFraccion.denominador)
            nuevoNumerador=self.numerador*(nuevoDenominador/self.denominador) - otraFraccion.numerador*(nuevoDenominador/otraFraccion.denominador)     
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def mcm(self,numero1, numero2):
        lista1=[]
        lista2=[]
        vacia=True
        for i in range(1,10):
            lista1.append(numero1*i)
            lista2.append(numero2*i)
            lista1.sort()
        for numero in lista1:
            if numero in lista2:
                vacia = False
                return numero
        if vacia == True:
            return numero1*numero2

    @validaEntero
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
    

def carga():
    fraccion=input('ingrese la fraccion separada por ,: ')
    numeros=fraccion.split(',')
    numerador=numeros[0]
    denominador=numeros[1]
    return Fraccion(numerador, denominador)

fraccion1=carga()
fraccion2=carga()
print(fraccion1)
print(fraccion2)
print(fraccion1.restar(fraccion2))
fraccion3=fraccion1.sumar(fraccion2)
print(fraccion3)
print(fraccion3.simplificar())
