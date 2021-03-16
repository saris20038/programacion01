#ciclo para ahorrar de a mil pesos 
PreguntaPrecio = "¿Cuanto vale el celular?: "
PrehguntaAhorro = "¿Cuanta plata tengo?: "
precio = float(input(PreguntaPrecio))
ahorro = float(input(PrehguntaAhorro))
if (ahorro >= precio):
    print("Tenemos la plata, a comprarlo")

while(precio > ahorro):
    print("Te falta dinero, vamos ahorrando de a mil")
    ahorro += 1000
    print ("Ahora tenemos", ahorro, "y nos falta", precio-ahorro)
print("terminado este ciclo, chao ps")

#Como aplicar el while negado 
#Juego de adivine el numero 
numeroganador = 2
PreguntaNumero = "Di un numero : "
numeroasked = int(input(PreguntaNumero))

while not (numeroasked == numeroganador):
    numeroasked = int(input("ese no era, vuelvelo a hacer: "))
print("fin")

#Adivine la letra secreta
SecretWord = "picky"
WORD_QUESTION ="Say a letter from the secret word: "
SayLetter = (input(WORD_QUESTION))

while(SayLetter not in SecretWord):
    SayLetter = (input("Try it again: "))

if (SayLetter in SecretWord ):
    print(f"You guessed, that letter is in the secret word {SecretWord}")

print("fin ejemplo")