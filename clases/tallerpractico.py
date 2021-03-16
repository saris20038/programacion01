#Taller recopilatorio 
#LISTAS
Dollarlist = [20000, 30000, 4000, 2500, 1000, 7600 ]
PesosList = []
for EachValue in Dollarlist:
    convertTo = round(EachValue * 3700, 2)
    PesosList.append(convertTo)
EurosList = []
for EachValue in Dollarlist:
    convertTo = round(EachValue*0.84, 2)
    EurosList.append(convertTo)

#MENUS 
INITIAL_MENUN = ''' WHAT DO YOU WANT TO DO TODAY? :
1- CONVERT THE LIST OF DOLLARS INTO PESOS AND EUROS
2- BE CLASIFIED BY YOUR ANUAL INCOMES 
3- INCOME ORGANIZATION 
4- FINISH PROGRAM AND GO TO EAT'''
MESSAGE_CONVERTION = ''' Choose any of the options 
C- In Colombian Pesos 
D- In dollars 
E- In Euros '''

#CLASIFICACIÓN 
ClasificationList =

#CODIGO
print(INITIAL_MENUN)
QuestionInitialMenu = int((input("Which option of the initial menu you want to work with?: ")))
while (QuestionInitialMenu != 4):
    chose1 = (QuestionInitialMenu == 1)
    chose2 = (QuestionInitialMenu == 2)
    chose3 = (QuestionInitialMenu == 3)
    Invaliderror = (QuestionInitialMenu != 4)
    if (chose1):
        print("You chose to convert")
        MoneyOption= str(input(MESSAGE_CONVERTION))
        if (MoneyOption == "C"):
            print(PesosList)
        elif (MoneyOption == "D"):
            print(Dollarlist)
        elif (MoneyOption == "E"):
            print(EurosList)
        else:
            print("choose a valid option")
    elif (chose2):
        print("you chose the second option")
        anualIncome= float(input("How many do you earn in dollar anually: "))
        if (anualIncome <= 1000):
            print("you have low incomes")
        elif (anualIncome > 1000 and anualIncome < 7000):
            print("you have medium incomes")
        elif (anualIncome >= 7000 and anualIncome <= 20000):
            print("you have high incomes")
        elif (anualIncome > 20000):
            print("you're rich motherfucker ")
        else: 
            print ("get a job")
    elif (chose3):
        print("you chose the third and last option")