#SECOND QUIZ 
#LISTS
Celsiuslist = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33] 
FarenheitList = []
for EachValue in Celsiuslist:
    convertTo = round((EachValue * 1.8) + 32, 2)
    FarenheitList.append(convertTo)
KelvinList = []
for EachValue in Celsiuslist:
    convertTo = round((EachValue-32)/ 1.8, 2)
    KelvinList.append(convertTo)

#MENUS 
INITIAL_MENUN = ''' WHAT DO YOU WANT TO DO TODAY? :
1- CONVERT FROM CELSIUS INTO FARENHEIT AND KELVIN
2- HEALTHY TEMPERATURES, IF IS HEALTHY OR SICK
3- MAXIMUM TEMPERATURE, MINIMUM AND TEMPERATURE TAKING PERIOD
4- FINISH PROGRAM : '''
MESSAGE_CONVERTION = ''' Choose any of the options 
C- In Celsius  
F- Into Farenheit 
K- Into Kelvin : '''

#LIST OF CLASIFICATION TEMPERATURES 
clasificationList= []
for EachValue in Celsiuslist:
    clasification = ""
    if (EachValue < 36):
        clasification = "Hipotermy"
    elif (EachValue >= 37.6 ):
        clasification = "Fever"
    else:
        clasification = "Normal  Temperature"
    clasificationList.append (clasification)

#MAXIMUM TEMPERATURE, MINIMUM AND TEMPERATURE TAKING PERIOD
MinimumTemperature= min (Celsiuslist)
MaximumTemperature = max (Celsiuslist)
PeriodTaking = round (len(Celsiuslist)/24 , 1)

#CODE
print(INITIAL_MENUN)
QuestionInitialMenu = int((input("Which option of the initial menu you want to work with?: ")))
while (QuestionInitialMenu != 4):
    chose1 = (QuestionInitialMenu == 1)
    chose2 = (QuestionInitialMenu == 2)
    chose3 = (QuestionInitialMenu == 3)
    Invaliderror = (QuestionInitialMenu != 4)
    if (chose1):
        print("You chose to convert")
        TemperatureOption= str(input(MESSAGE_CONVERTION))
        if (TemperatureOption == "C"):
            print(Celsiuslist)
            print("There was not convertion")
        elif (TemperatureOption == "F"):
            print(FarenheitList)
        elif (TemperatureOption == "K"):
            print(KelvinList)
        else:
            print("choose a valid option")
    elif (chose2):
        print (clasificationList)
    elif (chose3):
        print ("The maximum temperature was: ", MaximumTemperature)
        print ("The minimum temperature was of: ", MinimumTemperature)
        print ("The temperature was taked every ", PeriodTaking,"hours")
    else:
        print ("choose a valid option")
    QuestionInitialMenu = int((input("Which option of the initial menu you want to work with?: ")))

print ("Have a nice day") 

#THE END 