from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”

cm = CoffeeMaker()
m = Menu()
#mI = MenuItem()
mymc = MoneyMachine()

bandera = True
while(bandera):
    cm.__init__()
    askin_user = input("What would you like? (espresso/latte/cappuccino/): ")

    if(askin_user == "espresso" or askin_user == "latte" or askin_user == "cappuccino"):
        print(f"You chose a {askin_user}")
        drink  = m.find_drink(askin_user)
        there = cm.is_resource_sufficient(drink)
        if(there == True):
            #print(f"There are enough resources to make {askin_user}")
            #coins = int(input("Insert coins: "))
            print(f"You must pay ${drink.cost}")
            pay = mymc.make_payment(drink.cost)
            if(pay == True):
                cm.report()
                mymc.report()
                cm.make_coffee(drink)
                cm.report()
                mymc.report()
        
        
    elif(askin_user == "off"):
        #Turn off the Coffee Machine by entering “off” to the prompt
        bandera = False
        
    elif(askin_user == "report"):
        cm.report()
        mymc.report()
         
    else:
        print(f"There is no {askin_user}")