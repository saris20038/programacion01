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

nombreIngresar= input("¿Como te llamas?: ")
def welcomemessaje(nombre):
    print(f'Bienvenido a este codigo señor {nombre}')
welcomemessaje(nombreIngresar)