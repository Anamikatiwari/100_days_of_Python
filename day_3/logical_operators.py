""" 
if condition1 & condition2 & condition3:
   do this
else:
   do this

------------------------------

logical operators
.................
A and B => return true when both are true , otherwise false
C or D => return true when one is true, if both false return false
not E => complement
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
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a phto taken? Y or N")
    if wants_photo == "Y":
        # Add to their bill $3
        bill += 3
    
    print(f"Your final bill is ${bill}")
        
else:
    print("Sorry, you hae to grow taller before you can ride.")
  
