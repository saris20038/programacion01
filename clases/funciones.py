#FUNCIONES SIN ENTRADA 
#FUNCION PARA HACER UN MARCO 
def lineDesign ():
    print('#'*70)
lineDesign()
print("Hello there")
lineDesign()
print("¡General Kenobi!")

#FUNCIONES CON UNA ENTRADA 
def lineDesignEntrada1 (quantity):
    print('#'*quantity)
    return None
lineDesignEntrada1(89)

#FUNCIONES CON DOS ENTRADAS 
def sumar (value1=0, value2=0):
    return value1 + value2

def restar (value1=0, value2=0):
    return value1 - value2

def multiplicar (value1=0, value2=0):
    return value1 * value2

def dividir (value1=0, value2=0):
    return value1 / value2

#FUNCIONES QUE UTILIZAN OTRAS 
def calculadora (accion, value1, value2):
    print (accion(value1 , value2))

calculadora (sumar, 7, 3)
calculadora(restar, 4, 2)
