"""  
##### Program requirements #####
1. Print report. 
2. Check resources sufficients? 
3. Process coins. 
4. Check transaction successful? 
5. Make coffee. 

"""

# TODO: 2. Check resources sufficient to make drink order. 

MENU = {
        "espresso": {
            "ingredients":{
                "water": 50,
                "coffee": 18,
            },
        "cost": 1.5,
    },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
        "cost": 2.5,
            
    },
        "cappuccino": {
            "ingredients":{
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
        "cost": 3.0,
    },
             
}   

profit = 0 

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}           

# TODO: 1. Print report of all coffee machine resources

def is_resource_sufficient(order_ingredients):
    """ Return True when order can be made, False if ingredients are insufficient """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """ Return the total calculated from coins insterted. """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return(total)


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

is_on = True

while True:
    choice = input("What would you like? (expresso/latte/cappuccino: )")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink)
            
        
