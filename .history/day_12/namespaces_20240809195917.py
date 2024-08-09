# scope: the scope of an object refers to the region of a program where that object is accessible.
#A namespace is a system that has a unique name for each and every object. 

enemies = 1
def increase_enemies():
     enemies =2
     print(f" enemies inside function: {enemies}")
     
increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope: The names that you define in this scope are only available or visible to the code within the scope.
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()
print(potion_strength) 



# Global Scope: The names that you define in this scope are available to all your code.
player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
        
    drink_potion()

print(player_health) 

# In python, there is no block scope