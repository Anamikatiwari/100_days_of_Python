
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

user_cards = []
computer_cards = []

for _ in range(2):
    # new_card = [deal_card()]
    # user_cards.extend(new_card) 
    # user_cards += new_card
    # new_card = deal_card()

    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    

    
    