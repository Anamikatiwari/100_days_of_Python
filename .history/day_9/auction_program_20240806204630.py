from art import logo
print(logo)

bids ={}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? type 'yes' or 'no'.")
    if should_continue == "no"