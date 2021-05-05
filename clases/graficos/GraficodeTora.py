import matplotlib.pyplot as xx
pieLabels = ['python', 'java', 'dart', 'js',]
sizes = [50, 25, 10, 15]
pieExplode = [0,0,0.1,0]

###COMPLETO###
pieExplode = [0,0,0.2,0]
xx.pie(sizes,labels=pieLabels, explode=pieExplode)
#####################
xx.title('Uso de lenguajes de programación en el 2021')
xx.savefig('tortasLenguajes.png')
#####################
xx.show()

#####con sombras######
pieExplode = [0,0,0.2,0]
xx.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True, startangle= 45)
#####################
xx.title('Uso de lenguajes de programación en el 2021')
xx.savefig('tortasLenguajes.png')
#####################
xx.show()

#####con porcentajes#####
def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        pieLabels[i] += indicador+str(sizes[i]/acumulador*100) +'%'

pieExplode = [0,0,0.2,0]
acumulador = 0
etiquetarElementosPorcentuales(sizes,pieLabels,'☺')

xx.pie(sizes,labels=pieLabels, 
explode=pieExplode, 
shadow= True, 
counterclock = True, 
startangle= 45)
#####################
xx.title('Uso de lenguajes de programación en el 2021')
xx.savefig('tortasLenguajes.png')
#####################
xx.show()