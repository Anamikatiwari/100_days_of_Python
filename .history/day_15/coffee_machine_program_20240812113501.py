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
        drink = M
