#####GRAFICO DE BARRAS CON NIVELES DE INGRESOS#####
import matplotlib.pyplot as xx

months = ['January', 'February ', 'March ', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November']
entries = [2100000 , 2150000, 2200000, 2300000,2250000, 2100000, 2500000, 1900000, 2300000, 2200000, 2400000]
colors =["b","g","r","c","m","y","k","b","g","r","c","m"]

xx.bar(months, entries,width=0.5, color=colors)
xx.title ('Entries during 2020')
xx.xlabel('Month')
xx.ylabel('Salary (millones de pesos)')

xx.savefig('GraphicExample.png')
xx.show()

####TORTA DE CIUDADES####
pieLabels = ['Bogota', 'Medellín', 'Cali', 'Barranquilla ','Cartagena']
sizes = [51,11,16,4,18]
## sus tamaños son km2 : BOGOTA- 1.775, MEDELLIN - 382 km, CALI-564. BARRANQUILLA- 154, CARTAGENA- 609,1
pieExplode = [0.2,0,0,0,0] 

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        pieLabels[i] += indicador+str(sizes[i]/acumulador*100) +'%'

acumulador = 0
etiquetarElementosPorcentuales(sizes,pieLabels,'-')

xx.pie(sizes,labels=pieLabels, 
explode=pieExplode, 
shadow= True, 
counterclock = True, 
startangle= 45)
#####################
xx.title('Cinco ciudades mas importantes de colombia organizadas por su superficie')
xx.savefig('tortasCiudades.png')
#####################
xx.show()