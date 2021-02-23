## PROGRAMA DE EVALUACIÓN TRIGLICERIDOS Y HOMOCISTEÍNA 
MENSAJE_BIENVENIDA = "Bienvenido al programa de evaluación de PERFIL LIPÍDICO"
MENSAJE_BIENVENIDA2 = "Ingrese los datos solicitados y se arrojará el resultado deseado"
MENSAJE_REQUISITOS = "Debe tener los resultados del examén de sangre "
MENSAJE_DESPEDIDA = "Muchas gracias y hasta luego "
print(MENSAJE_BIENVENIDA, MENSAJE_BIENVENIDA2)
print(MENSAJE_REQUISITOS)
## TRIGLICERIDOS 
MENSAJE_TRIGLICERIDO_OPTIMO = "Sus niveles son optimos segun los valores de referencia"
MENSAJE_T_LIMITE = "Sus niveles se encuentran sobre el limite  segun los valores de referencia"
MENSAJE_T_ALTO =  "Sus niveles son altos segun los valores de referencia"
MENSAJE_T_MUYALTO = "Sus niveles son muy altos (WARNING)"

pregunta_triglicerido = "Cual es el resultado de los triglicéridos: "
triglicerido = float(input(pregunta_triglicerido))
isOptimo =  triglicerido < 150
isLimite = triglicerido >= 150 and triglicerido <= 199
isAlto = triglicerido >= 200 and triglicerido <= 499
isMuyAlto= triglicerido >= 500
if (isOptimo):
    print(MENSAJE_TRIGLICERIDO_OPTIMO)
elif (isLimite):
    print(MENSAJE_T_LIMITE)
elif (isAlto):
    print(MENSAJE_T_ALTO)
elif (isMuyAlto):
    print(MENSAJE_T_MUYALTO)
## HOMOCISTEINA 
MENSAJE_HOMO_OPTIMO = "Sus niveles son optimos segun los valores de referencia"
MENSAJE_H_LIMITE = "Sus niveles se encuentran sobre el limite  segun los valores de referencia"
MENSAJE_H_ALTO =  "Sus niveles son altos segun los valores de referencia"
MENSAJE_H_MUYALTO = "Sus niveles son muy altos (WARNING)"

pregunta_homocisteina = "Cual es el resultado de la homocisteina: "
homocisteina = float(input(pregunta_homocisteina))
isOptimoH =  homocisteina >= 2 and homocisteina < 15
isLimiteH = homocisteina >= 15 and homocisteina < 30
isAltoH = homocisteina >= 30 and homocisteina < 100
isMuyAltoH= triglicerido >= 100
if (isOptimoH):
    print(MENSAJE_HOMO_OPTIMO)
elif (isLimiteH):
    print(MENSAJE_H_LIMITE)
elif (isAltoH):
    print(MENSAJE_H_ALTO)
elif (isMuyAltoH):
    print(MENSAJE_H_MUYALTO)

print(MENSAJE_DESPEDIDA)
