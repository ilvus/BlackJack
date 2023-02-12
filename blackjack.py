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
    if a > 21 and 11 in card:
        card.remove(11)
        card.append(1)
        return sum(card)
    return a
print(f"Computer cards: {computer_cards}")
retake = True
while retake:

    if calculate_score(user_cards) < 21 and calculate_score(user_cards) != 0:
        print(user_cards)
        new_card = input("Do you want to drow another card? print 'y' or 'n': ")
        if new_card == "y":
            user_cards.append(deal_cards())
        elif new_card == "n":
            retake = False
    else:
        retake = False

while calculate_score(computer_cards) < 17:
    computer_cards.append(deal_cards())

def compare():
    if calculate_score(user_cards) == 0:
        print(f"This is your cards: {user_cards}")
        print(f"This is computer cards: {computer_cards}")
        return "You win!"
    elif calculate_score(user_cards) > 21:
        print(f"This is your cards: {user_cards}")
        print(f"This is computer cards: {computer_cards}")
        return "You lose!"
    elif calculate_score(computer_cards) == 0:
        print(f"This is your cards: {user_cards}")
        print(f"This is computer cards: {computer_cards}")
        return "You lose!"
    elif calculate_score(computer_cards) > 21:
        print(f"This is your cards: {user_cards}")
        print(f"This is computer cards: {computer_cards}")
        return "You win!"
    elif calculate_score(computer_cards) == calculate_score(user_cards):
        print(f"This is your cards: {user_cards}")
        print(f"This is computer cards: {computer_cards}")
        return "Draw"
    
print(compare())