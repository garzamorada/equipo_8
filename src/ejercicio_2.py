""" 2- Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). 
Tiene como limite 100 caracteres."""

def invertCase(input):
    if len(input) < 100:
        print (input.swapcase())
    else:
        print (f"""Disculpe, el limite de caracteres es de 100. 
               \nUsted quizo imprimir {len(input)}
               \nIntentelo nuevamente""")
    
invertCase("hOLA mUNDO")
invertCase("hOLA mUNDO"*100)