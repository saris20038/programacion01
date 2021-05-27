#####FIRST POINT####
import string
import matplotlib.pyplot as xx
colors =["b","g","r","c","m"]

print(''' Tell me 8 of your favorite dishes an its price''')
snackList = [] 
n=8
while (n > 0):
    Input1= str(input("Dish : "))
    snackList.append(Input1)
    n=n-1

snackPrice = []
n=8
while (n>0):
    priceInput= float(input("Price : "))
    snackPrice.append(priceInput)
    n=n-1


xx.bar(snackList, snackPrice, color= colors)
xx.title ('Dishes with its prices')
xx.xlabel('Dish')
xx.ylabel('price')

xx.savefig('Dishhh.png')
xx.show()

####SECOND POINT####
class Human ():
    def __init__ (self, edadEntrada, nombreEntrada, sexoEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
    def hablar (self, mensaje):
        print (f"Hello my name is  {self.nombre} and I have something to say...", mensaje)

Human1= Human("21", "Alexa", "female")
Human1.hablar("Im from Pluton, such and exquisite planet ")

class Doctor (Human):
    def __init__ (self, edadEntrada, nombreEntrada, sexoEntrada):
        Human.__init__ (self, edadEntrada, nombreEntrada, sexoEntrada)
    def IMC (self):
        peso = float(input("¿Cuánto pesas?: "))
        altura = float(input("¿Cuánto mides?: "))
        imc = peso/(altura**2)
        print (f'Tu IMC es de {imc} %')

doctor1 = Doctor('Carmen', 'male', 30)
doctor1.IMC()

####THIRD POINT####
Repeticiones = 1
while (Repeticiones== 1):
    try:
        nombre = str(input('Your name: '))
        assert (nombre.isalpha())
        Repeticiones = 2
    except AssertionError:
        print ('Pls enter a valid name-NO NUMBERS')

while (Repeticiones == 2):
    try:
        Dolarss = int(input('Value in dolars '))
        Repeticiones = 3
    except ValueError:
        print ('No valid value')

print (f'You: {nombre} have in dolars: {Dolarss}') 

Euros = round(Dolarss*0.82, 3)

print (f'Hi, {nombre} your money in dollars is equal to {Euros} euros')

####FOURTH POINT####
from os import fsdecode
import sys

nombreArchivo = 'patient.txt'
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    descripcion = 'Client management document.'
    archivo.writelines(descripcion)
    sys.exit(1)

PatientName = str(input("Patient's name: "))
SicknessDescription = str(input('What does the patient have?: '))
PriceC = float(input('Price of the the  medical check: '))

archivo = open(nombreArchivo, 'a')
linea = '\nnombre:' + str(PatientName) + ', Sickness :' + str(SicknessDescription) + ', Price per medical checkout:' + str(PriceC)  
archivo.writelines(linea)
archivo.close