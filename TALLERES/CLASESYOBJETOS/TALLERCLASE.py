#FIRST POINT 
print("-"*80)
class Torta ():
    '''Resposteria fina a tu gusto
    '''
    def __init__ (self,entradaSabor, entradaForma, entradaAltura):
        print ("Hola soy humano")
        self.sabor = entradaSabor
        self.forma = entradaForma
        self.altura= entradaAltura
    def mostrarAtributos (self):
        print (f'''El sabor que eligió para su torta fue de {self.sabor}
        con una forma de {self.forma}
        y con una altura de {self.altura}''')

torta1 = Torta("fresa", "cuadrada", "40 cm")
torta1.mostrarAtributos()

#SECOND POINT 
print("-"*80)
class EstudianteUniversidad ():
    def __init__ (self, edadEntrada, nombreEntrada, idEntrada, carreraEntrada, semestreEntrada):
        print ("Hi, Im a student")
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
        print (f"Me llamo {self.nombre} , tengo {self.edad}, estudio {self.carrera} actualmente en el semestre {self.semestre} con id {self.id}")
    def RepasoEspecifico(self,materiaEntrada, tiempoEntrada):
        print (f" El estudiante {self.nombre} va a estudiar {materiaEntrada} las siguientes {tiempoEntrada} horas")

Student1 = EstudianteUniversidad("22", "Catalina Mesa", "505068", "Medicina", "5") 
Student1.RepasoEspecifico("Histología", "3")

#THIRD POINT 
print("-"*80)
class Nutricionista ():
    def __init__ (self, edadEntrada, nombreEntrada,universidadEntrada):
        print ("Hi, Im a student")
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.universidad = universidadEntrada
        print (f"Me llamo {self.nombre} , estudio en {self.universidad}")
    def IMC(self, PesoEntrada, alturaEnttrada):
        IMC= PesoEntrada / (alturaEnttrada**2)
        print (f" Su IMC {IMC}")

Nutricionista1 = Nutricionista("21", "Susana Ramirez", "Universidad de Antioquia")
Nutricionista1.IMC(2 , 1.78)

#FOURTH POINT 
print("-"*80)
class Kangaroo():
    def __init__(self, nameInput, idInput, edadInput):
        print("Hi, Im a Kangaroo ")
        self.name = nameInput
        self.idK= idInput
        self.edadK= edadInput
        print (f'''Soy un Canguro y me llamo {self.name}
        tengo {self.edadK} años
        con identificacion: {self.idK}''')
    def recorrerDistancia (self, cantidadSaltos):
        for i in range (cantidadSaltos):
            print (f"El canguroha dado  {i+1} saltos")

Kangaroo1 = Kangaroo("Alfonso", "39909", "2")
Kangaroo1.recorrerDistancia(4)

#FIFTH POINT 
print("-"*80)
class Instrumento ():
    def __init__ (self, calsificacionEntr, nombreEntr, pesoentr ):
        self.clasificacion = calsificacionEntr
        self.nombre = nombreEntr
        self.peso = pesoentr
    def mostrarAtributos (self):
        print (f'''    Esto es un {self.nombre}
        un instrumento de {self.clasificacion} 
        que pesa alrededor de{self.peso}''')
    def InterpretarCancion(self, interpretacion):
        print (f" El pianista esta tocando {interpretacion} en este momento")

piano1=Instrumento("percusion", "piano", "230 kg")
piano1.mostrarAtributos()
piano1.InterpretarCancion("Moonlight")