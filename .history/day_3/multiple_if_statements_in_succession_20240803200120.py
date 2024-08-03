"""
   if/ elif/ else         
   ---------------
   if condition1:
      do A
   elif condition2:
      do B
   else:
      do C    
      
  ............................................................................    
      
    multiple if
    -----------
    if condition1:
       do A
    if condition2:
       do B
    if condition3:
       do C    
"""

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("ypu can ride the rollercoaster!")
    age= int(input("What is your age?"))
    if age < 12:
       print("Child tickets are $5.") 
    elif age <= 18:
        print("Youth tickets are $7.")
    else:
        print("Ad $12.")
else:
    print("Sorry, you hae to grow taller before you can ride.")
  
