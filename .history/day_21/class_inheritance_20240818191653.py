"""
Inheritance
--------------
class Fish(Animal):
def __init__(self, name, species, age, weight, length):
    super().__init__(name, species, age, weight, length)

"""

class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, Exhale.")
        
class Fish(Animal): # inheriting from animal class
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this underwater.")
        
    def swim(self):
        print("Moving in water.")
        
nemo = Fish() #creating object
nemo.swim()
nemo.breathe()
print(nemo.num_eyes) # accessing attribute from parent class

# In day-21, 