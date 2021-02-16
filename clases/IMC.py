PREGUNTA_PESO = "¿Cuanto pesas  en Kg? : "
PREGUNTA_ALTURA = "¿Cuanto mides en M? : "
MENSAJE_BIENVENIDA = "Hola gordo :D"
MENSAJE_DESPEDIDA= "Bueno chao ps"
print(MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
altura = float(input(PREGUNTA_ALTURA))
IMC = (peso) / (altura **2)
print(IMC)
print(f"Tu IMC es de {IMC}")
isObeso = IMC >= 30
print(f"Estas gorda?....{isObeso}" )
print(MENSAJE_DESPEDIDA)