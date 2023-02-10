

import random as rd

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    
    return rd.choice(cards)

user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

def calculate_score(card):
    a = sum(card)
    if a == 21 and len(card) == 2:
        return 0
    elif a > 21 and 11 in a:
        card.remove(11)
        card.append(1)
    return a

calculate_score(user_cards)