from art import logo, vs
from game_data import data
import random


def format_data(account):
    # Format the account data into printable format. 
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")


# Dsplay art
print(logo)

# Generate a random account from the game data. 
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A : {format_data(account_a)}.")
print(vs)
print(f"Against B : {format_data(account_b)}.")

# Ask user for a guess.
guess = input("Who has more follower? Type 'A' or 'B': ").lower()

# Check if the user is correct.
 
# Get follower count of each account. 
a_follower_count = account_a["follower_count"]
b_follower_count = account_a["follower_count"]

# Use if statement to check if user is correct. 

# Give user feedback on their guess. 

# Score keeping.

# Make the game repeatable.

# Making account at position B become the next account at position A. 

# Clear  the screen between rounds.   
