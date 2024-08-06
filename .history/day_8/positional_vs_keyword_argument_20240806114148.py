# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")
    
greet_with("Anamika Tiwari", "XYZ")


""" 
Positional rguments
-------------------
def my_function(a, b, c):
    #do this with a
    #then do this b
    #Finally do this with c
"""
greet_with("Anamika Tiwari", "XYZ")

""" 
Keyword rguments
-------------------
def my_function(a, b, c):
    #do this with a
    #then do this b
    #Finally do this with c
    
    #function call
    my_function(a=1, b=2, c=3)
    or,
    
"""


#Function with keyword argument
greet_with(name="Anamika", location="XYZ")