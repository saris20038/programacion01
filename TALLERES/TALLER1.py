print("Primer taller que manda el profe para poner en practica primeros aprendizajes con variables :)")
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
