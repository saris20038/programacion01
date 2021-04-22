#FIRST POINT 
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