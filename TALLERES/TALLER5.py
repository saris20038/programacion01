#FIRST POINT 
NAME_INPUT= input("Tell me your name : ")
def welcomemessaje(name):
    print(f'Welcome to the best code ever {name}')
welcomemessaje(NAME_INPUT)

List = [20, 30, 40, 50, 60, 70, 80, 90, 100, 200]
def EachValueForList (List1):
    for EachValue in List :
        print(EachValue)
    return None
EachValueForList(List)

#SECOND POINT 
List2 = [2, 3, 4, 5, 6]
def showMaxMin (list):
    highest = max(list)
    smallest = min(list)
    sum_total = 0
    for eachvalue in list:
        sum_total += eachvalue
    sizelist= len(list)
    mean = sum_total / sizelist
    print(f" The highest value is {highest}, the smallest {smallest}, the mean is {mean}")


#FOURTH POINT 
number_list= [3, 5, 66, 88, 22, 4, 2]
def pairNumber(list):
    pairs = []
    for eachvalue in list:
        if eachvalue % 2 == 0 :
        pairs.append (eachvalue)
    return pairs

pairNumber(number_list)
#SEVENTH POINT 

def farewellmessaje (name):
    print(f'See ya Sr.{name}')
farewellmessaje(NAME_INPUT)