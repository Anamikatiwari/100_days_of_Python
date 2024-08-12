"""  
##### Program requirements #####
1. Print report. 
2. Check resources sufficients? 
3. Process coins. 
4. Check transaction successful? 
5. Make coffee. 

"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()



# check resources sufficients?
while is_on:
    options = menu.get_items()
    choi