# scope

enemies = 1
def increase_enemies():
     enemies =2
     print(f" enemies inside function: {enemies}")
     
increase_enemies()
print(f"enemies outside function: {enemies}")

# 
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()
print(potion_strength) 



# Global Scope: The names that you define in this scope are available to all your code.
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)
    
drink_potion()