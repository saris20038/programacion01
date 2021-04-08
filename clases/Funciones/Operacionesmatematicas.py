def sumar (value1=0, value2=0, value3= 0):
    return (value1 + value2 + value3)

def restar (value1=0, value2=0, value3= 0):
    return (value1 - value2 - value3)

def multiplicar (value1=0, value2=0, value3= 0):
    return (value1 * value2 * value3)

def dividir (value1=0, value2=0, value3= 0):
    return (value1 / value2 / value3)

def potenciar  (value1=0, value2=0, value3= 0):
    return (value1 ** value2 ** value3)

#FUNCIONES QUE UTILIZAN OTRAS 
def calculadora (value1=0, value2=0, value3= 0):
    print ("the sume is", (sumar(value1, value, value3)), "the substraction is", (restar(value1, value2, value3)), "the multiplication is", multiplicar(value1, value2, value3), "the division is", dividir(value1, value2, value3),"the potential", potenciar(value1, value2, value3) )

calculadora(2, 3, 3)


