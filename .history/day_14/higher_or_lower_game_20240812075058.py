from art import logo
from game_data import data
import random

# Dsplay art
print(logo)

# Generate a random account from the game data. 
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

# Format the account data into printable format. 
account_name = account_a["name"]
account_descr = account_a["description"]
account_country = account_a["country"]
print(f"{account_name}, a {account_descr}, from {acc}")

# Ask user for a guess. 

# Check if the user is correct. 
# Get follower count of each account. 
# Use if statement to check if user is correct. 

# Give user feedback on their guess. 

# Score keeping.

# Make the game repeatable.

# Making account at position B become the next account at position A. 

# Clear  the screen between rounds.   
