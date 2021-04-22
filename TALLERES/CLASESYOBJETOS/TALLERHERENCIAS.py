#First point 
print("#"*80)
class Persona():
    def __init__ (self, edadEntrada, nombreEntrada, idEntrada):
        print ("Hola soy una personita muy feliz :D")
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
    def decirmensaje (self, mensaje):
        print (f"Hola soy {self.nombre} y tengo un mensaje que decir...", mensaje)
    def mostrarAtributos (self):
        print (f'''Mi nombre es {self.nombre}
        Mi edad es {self.edad}
        Mi identificación es {self.id}''')
    def recorrerDistancia (self, cantidadPasos):
        for i in range (cantidadPasos):
            print (f"La persona ha dado {i+1} pasos")

persona1 = Persona(33, "Carlos", 3329)
persona1.decirmensaje("Me gusta la pizza con piña")
persona1.recorrerDistancia(22)

#SECOND POINT
print("#"*80)
class Doctor (Persona):
    def __init__ (self, especialidadEntrada,edadEntrada, nombreEntrada, idEntrada):
        Persona.__init__(self, edadEntrada, nombreEntrada, idEntrada)
        self.especialidad = especialidadEntrada
    def TratamientoSickness (self, enfermedad):
        self.sickness = enfermedad
        print (f" Hola soy el {self.especialidad}, mi nombre es: {self.nombre} y empezaré el tratamiento para el/la {self.sickness}") 

Chapatin = Doctor("médico", 21, "Chapatín", "6790876")
Chapatin.TratamientoSickness("cancér")

#THIRD POINT 
print("#"*80)
class Nutricionista (Persona):
    def __init__ (self, UniversidadEntrada,edadEntrada, nombreEntrada, idEntrada):
        Persona.__init__(self, edadEntrada, nombreEntrada, idEntrada)
        self.universidad = UniversidadEntrada
    def hablar (self):
        print (f'''Mi nombre es {self.nombre} y
        Mi identificación es {self.id}''')
    def IMC(self, PesoEntrada, alturaEntrada):
        IMC= round(PesoEntrada / (alturaEntrada**2), 2)
        print (f" El IMC del paciente es {IMC}")

gymNutricionista = Nutricionista("CES", "34 ", "Paula", 6728903746)
gymNutricionista.hablar()
gymNutricionista.IMC(67, 1.90)

#FOURTH POINT
print("#"*80)
class Abogado (Persona):
    def __init__ (self, especialidadEntrada,university, edadEntrada, nombreEntrada, idEntrada):
        Persona.__init__(self, edadEntrada, nombreEntrada, idEntrada)
        self.especialidad = especialidadEntrada
        self.universidad= university
    def Defensacaso(self, nombrecliente, Caso):
        print (f'''En el día de hoy, yo {self.nombre} como {self.especialidad} {self.universidad}
        defensor de mi cliente aquí presente,
        el sr/sra {nombrecliente} que esta en juicio por {Caso} ''')

Doctora_Polo=Abogado("Abogado", "CES", "53", "Ana María Polo", 239494849)
Doctora_Polo.Defensacaso("Murcia", "lavado de dinero")