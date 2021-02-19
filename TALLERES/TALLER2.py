## Usando el mismo codigo del taller 1, haré un mayor y menor.
print("Segundo taller, con el codigo del primero")
print("--Los dos numeros que tendré seran un supuesto de la nota de calculo que tengo y la nota necesaria para aprobar--")
miNota = 2.8
notaMinima = 3
notaMaxima= 5
print("¿con la nota que tengo, gano la materia? ")
isAprobado = miNota>= 3
pruebaV = True
pruebaF= False
print(isAprobado)
print("Entonces, ¿cuanto me falta para ganar?")
isMeFalta = notaMinima - miNota
print(isMeFalta)
print("Si multiplico mis esfuerzos y por lo tanto mi nota dos veces, ¿sobrepasa el 5? ")
isDoble = miNota * 2
isSobrepasado = isDoble > notaMaxima
print(isSobrepasado)
print("Si divido mi nota entre la nota minima, ¿es menor que 1?")
isMenor = miNota / notaMinima
isMenorQueUno = isMenor < 1
print(isMenorQueUno)
print("Elevando mi nota a la nota minima ¿sobrepasare la nota maxima?")
isMayor= miNota ** notaMinima
isVerdadSobrepasa = isMayor > notaMaxima
print(isVerdadSobrepasa)
print("¿Mi nota es diferente a la nota maxima?")
isDiferente = miNota != notaMaxima
print(isDiferente)
## AQUÍ EMPIEZAN LOS CAMBIOS
MENSAJE_DESPEDIDA = "Hasta luego perdedora, te quedo la nota final de calculo en: "
print (MENSAJE_DESPEDIDA, miNota)
print("Ahora calcularemos el promedio de las dos materias, es decir de calculo con Programación")
PREGUNTA_PROGRAMACIÓN = "¿Cual fue tu nota final en programación? :  "
notaProgramacion = float(input(PREGUNTA_PROGRAMACIÓN))
##como las dos tienen 3 creditos valen lo mismo 
promedioDosMaterias = (notaProgramacion + miNota) / 2 
print(f"su promedio es de: {promedioDosMaterias}")
isPromedioAprobado = promedioDosMaterias > notaMinima
print("¿Con este promedio aprueba (esta encima de 3)?" , isPromedioAprobado)
TuNombre = "¿Como te llamas?: " 
nombrePerdedor = input(TuNombre)
MENSAJE_BYE = "Hasta luego"
MOTIVACIONES = ", estudia más porfi"
print(MENSAJE_BYE , nombrePerdedor , MOTIVACIONES)