
# Our Blackjacks House Rules
# -------------------------------
# The deck is unlimited in size.
# There are no jockers. 
# The Jack/Queen/King all count as 10. 
# The Ace can count as either 1 or 11.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.add()
# cares are not removed from the deck as they are drawn.

import random

def deal_card():
    """ Returns a random card from the deck.  """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Create a function called calculate_score() that takes a list of cards as input and returns the score. 
# Look up the sum() function to help you do this. 

def calculate_score(cards):
    """  Takea list of cards and return the score calculated from the cards """
    # Inside calculate_score() check for a blackjack and return 0 instead of actual score. 0 will represent a blackjack in our game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove(). 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Deal the user and computer 2 cards each using deal_card()
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    # new_card = [deal_card()]
    # user_cards.extend(new_card) 
    # user_cards += new_card
    # new_card = deal_card()
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# call calculate_score(). If the computer or user has a blackjack (0) or if the user's score is over 21, then the game ends.
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards: {user_cards}, current score: {user_score}")
print(f" Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == 'y':
        user_cards.append(deal_card())
    else:
        is_game_over == Tr
    
# If the game has  not ended, ask the user if they want to draw another card. If yes, the use the deal_card() function to add another card to the user_card list. If no, then the game has ended. 


# The score will need to be rechecked with every new card drawn 

# Once the user is done and no longer wants to draw more cards, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17. 



    