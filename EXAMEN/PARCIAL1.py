#FIRST POINT 
print("FIRST POINT", '#'*70)

print('Tell 3 numbers')
number_1 = float(input("First chosen value: "))
number_2 = float(input("Second chosen value: "))
number_3 = float(input("Third chosen value: "))

def sumar (value1=0, value2=0, value3= 0):
    return (value1 + value2 + value3)

def restar (value1=0, value2=0, value3= 0):
    return (value1 - value2 - value3)

def multiplicar (value1=0, value2=0, value3= 0):
    return (value1 * value2 * value3)

def dividir (value1=0, value2=0, value3= 0):
    return (value1 / value2 / value3)

def potenciar  (value1=0, value2=0, value3= 0):
    return (value1 ** value2**value3)

#FUNCIONES QUE UTILIZAN OTRAS 
def calculadora (thing, value1, value2, value3):
    print(thing(value1, value2, value3))

print("The sume is")
calculadora(sumar, number_1, number_2, number_3)
print("The substraction is")
calculadora(restar, number_1, number_2, number_3)
print("The multiplication is")
calculadora(multiplicar, number_1, number_2, number_3)
print("The division is")
calculadora(dividir, number_1, number_2, number_3)
print("The potential is")
calculadora(potenciar, number_1, number_2, number_3)

#SECOND POINT 
print("SECOND POINT", '#'*70)
List_1= [1, 2, 3, 4]
List_2 =[5, 6 , 7 ,8]
List_3 =[9, 10, 11, 12]
def seelists (list1, list2, list3):
    if (len(list1)== len(list2)== len(list3)):
        print(''' The lists are
        ''', list1, '''
        ''', list2, '''
        ''', list3)
    else:
        print("the lists have to have the same lenght")

seelists(List_1, List_2, List_3)

#TERCER PUNTO
print("THIRD POINT", '#'*70) 
Base_t= float(input("wich is the base of the triangle: "))
altura_t= float(input("which is the alture of the triangle: "))

def trianglearea (base, alture):
    print("the area is", ((base * alture)/2))

trianglearea(Base_t, altura_t)

#CUARTO PUNTO 
print("FOURTH POINT", '#'*70)

List_FOUR = [2, 3, 4, 5, 6]
def showMaxMin (list):
    highest = max(list)
    smallest = min(list)
    sum_total = 0
    for eachvalue in list:
        sum_total += eachvalue
    sizelist= len(list)
    mean = sum_total / sizelist
    print(f" The highest value is {highest}, the smallest {smallest}, the mean is {mean}")

showMaxMin(List_FOUR)

#QUINTO PUNTO 
print("LAST POINT", '#'*70) 

Position= int(input("tell a position for the fibonacci ecuation: "))
def FIBONACCI (n):
    if n < 2:
        return n 
    else:
        print((n-1)+(n-2))

FIBONACCI(Position)