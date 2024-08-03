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
bill = 0
if height >= 120:
    print("ypu can ride the rollercoaster!")
    age= int(input("What is your age?"))
    if age < 12:
       bill = 5
       print("Child tickets are $5.") 
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a phto taken? Y or N")
    if wants_photo == "Y":
        bill += 3
        
else:
    print("Sorry, you hae to grow taller before you can ride.")
  
