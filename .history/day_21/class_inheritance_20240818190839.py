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
        
class Fish:
    def swim(self):
        print("Moving in water.")
        
nemo = Fish swim(self)
nemo.swim