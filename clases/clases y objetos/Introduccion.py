class Human():
    def __init__(self, nameInput, oldInput, heightInput):
        print("Hi, Im the new one ")
        self.oldness = oldInput
        self.specie = "Human"
        self.name = nameInput 
        self.height = heightInput
        self.money = 0

    def ShowAtributtes (self):
        print ("My name is ", self.name, ". I'm", self.oldness, 'and', ". my height is", self.height, "Meters")
    
    def speak (self, message):
        print ("I have a message for you: ", message)
    def savings (self):
        '''
        Human will save the amount of money that you introduce
        '''
        saveQuestion = int(input('''Introduce
        S--> if you want to save an amount of money
        N --> if you do not want to save money: '''))
    def savings (self):
        quantitymoney= float(input("How many: "))
        while(saveQuestion != "N"):
            Quantity= float(input(quantitymoney))
            self.money = self.money + Quantity
            print (f"I have  {self.dinero} pesos in savings")
            saveQuestion = int(input('''Introduce
            S--> if you want to save an amount of money
            N --> if you do not want to save money: '''))
        return self.money

class biomedic (Human):
    def biomedicalEquipmentMaintenance (self, EquipmentName):
        print ("Hi, I am", self.name, "and I will give the appropiate manteinance to", EquipmentName)

biomedicHuman = biomedic("Sara", 18, 1.70)
biomedicHuman.biomedicalEquipmentMaintenance ("Electrocardiograph")



human1 = Human("Sara", 18, 1.68)
human1.ShowAtributtes ()
human1.savings()
human1.speak("I hope youre okay")

human2 = Human("Alejandro", 9, 1.80)
human2.speak("see ya later ")