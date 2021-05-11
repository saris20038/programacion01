####FIRST POINT####
import string
import matplotlib.pyplot as xx
colors =["b","g","r","c","m"]

print(''' Tell me your top 5 snacks list and their prices ''')
snackList = [] 
n=5
while (n > 0):
    Input1= str(input("Snack : "))
    snackList.append(Input1)
    n=n-1

snackPrice = []
n=5
while (n>0):
    priceInput= float(input("Price : "))
    snackPrice.append(priceInput)
    n=n-1


xx.bar(snackList, snackPrice, color= colors)
xx.title ('Top lists of snack with their prices')
xx.xlabel('Snack')
xx.ylabel('price')

xx.savefig('Snackstt.png')
xx.show()

##SECOND POINT##
print(''' Tell me 5 cities and their population  ''')
City = [] 
n=5
while (n > 0):
    Input0= str(input("City : "))
    City.append(Input0)
    n=n-1

Population= []
n=5
while (n>0):
    priceInput= float(input("Population: "))
    Population.append(priceInput)
    n=n-1

maximum= max(Population)
ubicación=Population.index(maximum)
pieExplode = [0,0,0,0,0]

pieExplode[ubicación]= 0.2

xx.pie(Population,labels= City, 
explode=pieExplode, 
shadow= True, 
counterclock = True, 
startangle= 45)
#####################
xx.title('Cities and their population ')
xx.savefig('Cities.png')
#####################
xx.show()

#THIRD POINT#
import pandas as pd
import matplotlib.pyplot as plt
print ('''An electrocardiogram is a test that checks how your heart is functioning by measuring the electrical activity of the heart''')

ecgData = pd.read_csv ("ecg.csv",encoding="UTF-8",header=0,delimiter=";").to_dict()
muestras = list(ecgData["muestra"].values())
voltajes= list(ecgData["valor"].values())

plt.plot(muestras, voltajes)
plt.title ('EKG')
plt.xlabel ('Time (mS)')
plt.ylabel ('Voltage (microvoltios)')
plt.savefig("cc.png")

plt.show()

###PPG##
print('''A photoplethysmogram (PPG) is an optically obtained plethysmogram that can be used to detect blood volume changes in the microvascular bed of tissue''')

ppgData = pd.read_csv ("ppg.csv",encoding="UTF-8",header=0,delimiter=";").to_dict()
muestras = list(ppgData["muestra"].values())
voltaje1 = list(ppgData["valor"].values())
plt.plot(muestras, voltaje1)
plt.title ('PPG')
plt.xlabel ('Time (uS)')
plt.ylabel ('Voltage (microvoltios)')

plt.savefig("ppg.png")
plt.show()
