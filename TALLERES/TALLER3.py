## TALLER CONDICIONALES 
##DOS NUMEROS Y CUAL ES EL MAYOR 
print("si la edad de mi mama es 49 y mi la de mi papa es 53, ¿quén es mayor?")
edadMama = 49
edadPapa = 53
siEsmayorPapa = 53 > 49
siEsmayorMama= 49 > 53 
MENSAJE_PAPA_MAYOR = "Mi papa es mayor "
MENSAJE_MAMA_MAYOR = "Mi mama es mayor"
if(siEsmayorMama):
    print(MENSAJE_MAMA_MAYOR)
if(siEsmayorPapa):
    print(MENSAJE_PAPA_MAYOR)

##PUNTO 2 EDAD DEL SUJETO 
print("Dinos tu edad y te diremos si eres menor de edad, joven, adulto o adulto mayor")
PREGUNTA_EDAD = "¿Cuantos años tienes?: "
edad = int(input(PREGUNTA_EDAD))
isMenor =  edad < 18
isJoven = edad >= 18 and edad <= 25
isAdulto = edad >= 26  and edad < 60
isAdultoMayor= edad >=60 
MENSA_MENOR = "Oh, eres menor de edad; ¡A ponerse la pijama!"
MENSA_JOVEN = "¡Eres joven!"
ADULTO = "Ya estas adulto, ¡a trabajar!"
ADULMAYOR = "Ya esta viejo, pensionese"
if (isMenor):
    print(MENSA_MENOR)
elif (isJoven):
    print(MENSA_JOVEN)
elif (isAdulto):
    print(ADULTO)
elif(isAdultoMayor):
    print(ADULMAYOR)
print("####chao####")

##PUNTO 3 AÑO ACTUAL 
print("Con el año actual y otro que elija le diremos cuanto ha pasado o cuanto falta (digite sin puntos)")
AÑO_1 = "¿En que año está?: "
AÑO_2 = "¿A que año quiere viajar?: "
año1 = float(input(AÑO_1))
año2 = float(input(AÑO_2))
si1Mayor = año1 > año2
si2Mayor = año1 < año2
siIguales = año1 == año2
RESTA1= año1 - año2
RESTA2= año2 - año1

if(siIguales):
    print("Es el mismo año, bromista, quierase")
elif(si1Mayor):
    print(f"han pasado {RESTA1} años")
elif(si2Mayor):
    print(f"Faltan {RESTA2} años")

##PUNTO 4 DE CM A KM M Y MM
print("Dame una distancia en Cm y la convertiré a Km, m y mm")
DISTANCIA= "Distancia en cm: "
distanciaCM = float(input(DISTANCIA))
kilometros= distanciaCM / 100000
metros= distanciaCM / 100
milimetros = distanciaCM * 10 
print(f"Los {distanciaCM} cm equivalen a {kilometros}km , {metros}m y {milimetros}mm")
print("Hasta luego buen día")