
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


class Artista (Usuario):
    def __init__(self, generoEntrada, numerocancionesEntrada, albumsEntrada, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada):
        Usuario.__init__(self, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada )
        self.generomusical = generoEntrada
        self.numerocanciones = numerocancionesEntrada
        self.numeroDeAlbums = albumsEntrada
    def asistirConcierto(self, localidadEntrada):
        self.localidadconcert = localidadEntrada
        print (f" Hola, soy {self.nombre}, iré a un concierto en {self.localidadconcert} del genero {self.generomusical} que tiene un total de albums de {self.numeroDeAlbums} con {self.numerocanciones} canciones. ¡QUE EMOCIÓN!")

Fabio= Artista("Country", "30", "22", "67", "Fabio", "hombre", "Colombiano")
Fabio.asistirConcierto("Estados Unidos")