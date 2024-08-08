# part-1

#  _____________________
# |  _________________  |   
# | | Pythonista   0. | |  
# | |_________________| | 
# |  ___ ___ ___   ___  | 
# | | 7 | 8 | 9 | | + | | 
# | |___|___|___| |___| | 
# | | 4 | 5 | 6 | | - | |                      
# | |___|___|___| |___| | 
# | | 1 | 2 | 3 | | x | | 
# | |___|___|___| |___| | 
# | | . | 0 | = | | / | | 
# | |___|___|___| |___| | 
# |_____________________|  

#                       88                        88                     
#                       88                        88              ,d     
#                       88                        88              88     
# ,adPPYba, ,adPPYYba,  88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM  
# a8"     "" ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88     
# 8b         ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88     
# "8a,   ,aa 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,    
# `"Ybbd8"' `"8bbdP"Y8 88  `"Ybbd8"'  `"YbbdP'Y8 88 `"8bbdP"Y8   "Y888 



# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


# creating dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
# num2 = int(input("What's the second number?: "))
for symbol in operations:
    print(symbol)
should_continue = True

while should_continue:
    operation_symbol = input ("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    # answer = calculation_function(num1, num2)
    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")


    peration_symbol = input ("Pick an another operation: ")
    num3 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(calculation_function(num1, num2), num3)

    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")




















