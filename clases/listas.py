nombres = [ ]
print(type (nombres))
nombres = ['Cristina', 'fernando', 'Ana maria']
print(nombres[1])
nombres.append('Sara')
edades =[2,3,4,5,6,7,8,9,10]
#al ultimo
print(edades[-1])
#al primero pero no ultimo 
print(edades[0:4])
#si no le ponemos nada toma el incio y hasta el final 
print(edades[0:])
#todas 
print(edades[:])
#re organizar 
edades.sort()
print(edades)
edades.sort(reverse=True)
print(edades)
#mayor o menor 
mayor = max(edades)
menor = min(edades)
#saber numeros de elementos 
largoListaEdades = len(edades)
print(largoListaEdades)
#suma edades
SumaEdades = sum(edades)
#promedio 
PromedioEdades = SumaEdades/largoListaEdades 
print(PromedioEdades)
#Eliminar dato 
edades.pop(2)
print(edades)

#ciclo for y listas 
for indice in range (largoListaEdades): 
    print('estoy en la posicion', indice, 'valgo' , edades[indice])
    