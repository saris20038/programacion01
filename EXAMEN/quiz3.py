
class Usuario ():
    def __init__ (self, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.nacionalidad= nacionalidadEntrada
    def mostrarAtributos (self):
        print (f'''Mi nombre es {self.nombre}
        tengo {self.edad} años,
        soy un/a {self.sexo}
        con nacionalidad {self.nacionalidad}''')
    def escucharCancion(self, cancionEntrada):
        print (f" Hola, soy {self.nombre} y estoy escuchando {cancionEntrada}")

Usuario1 = Usuario("21", "Alexa", "mujer", "Española")
Usuario1.mostrarAtributos()
Usuario1.escucharCancion("La flaca")