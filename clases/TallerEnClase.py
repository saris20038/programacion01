#FIRST POINT 
Celsiuslist = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33] 
def FirstConvertion (list, operation):
    ''' Choose any of the options 
    F- Into Farenheit 
    K- Into Kelvin :
    An invalid option will return you none  '''
    ConvertedList1 = []
    ConvertedList2 = []
    for Eachvalue in list:
        ConvertToo= ((Eachvalue * 1.8) + 32, 2)
        ConvertedList1.append(ConvertToo)
    for Eachvalue in list:
        ConvertTooo= Eachvalue + 273 
        ConvertedList2.append(ConvertTooo)
    if ChosenOption == "F":
        print(ConvertedList1)
    elif ChosenOption == "K":
        print(ConvertedList2)
    else: 
        return None 

#LA USAMOS 
ChosenOption= input("Wich one do you choose?: ")
FirstConvertion(Celsiuslist, ChosenOption)

#CLASIFICAR TEMPERATURAS 
def lineDesign ():
    print('#'*70)
print(lineDesign())

def TemperatureClasification (list):
    ''' HEALTHY TEMPERATURES, IF IS HEALTHY OR SICK
    '''
    Clasification_list= []
    for eachvalue in list:
        if (eachvalue < 36):
            clasification = "Hipotermy"
        elif (eachvalue >= 37.6 ):
            clasification = "Fever"
        else:
            clasification = "Normal  Temperature"
        Clasification_list.append (clasification)
    print(Clasification_list)

TemperatureClasification (Celsiuslist)

