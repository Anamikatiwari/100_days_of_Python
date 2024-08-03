"""
Nested if/else

if condition:
   if another condition:
      do this
   else:
       do this
else:
    do this         
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("ypu can ride the rollercoaster!")
    age= int(input("What is your age?"))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you hae to grow taller before you can ride.")
    

"""
if/ elif/ else

if condition1:
    do A
else:
        
"""    

