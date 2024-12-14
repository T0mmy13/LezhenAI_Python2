import random
import time
from tokenize import PseudoExtras
from urllib.parse import uses_fragment

def card_value(card):
    value_map = {
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 2,
        'Queen': 3,
        'King': 4,
        'Ace': 11
    }
    value, suit = card.split(' of ')
    return value_map[value]

cards = ['6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts',
    '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds',
    '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs',
    '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades']
random.shuffle(cards)

UsersPoints = 0
PcPoints = 0
EndGame = 0

while EndGame < 5:
    if input("Do you want to draw a card? (y/n) ") == "y":
        card = cards.pop()
        UsersPoints += card_value(card)
        print("You are drawing a card...")
        time.sleep(1.5)
        print(f"You drew { card}. You now have {UsersPoints} points.")
    else:
        print("You skipped the turn...")
    if PcPoints < 22:
        print("Opponent is drawing a card...")
        card = cards.pop()
        PcPoints += card_value(card)
        time.sleep(1.5)
    else:
        print("Opponent skipped the turn...")
    EndGame += 1

print(f"Your points: {UsersPoints}\nOpponent points: {PcPoints}")

if (UsersPoints > 21 and UsersPoints < PcPoints) or (UsersPoints < 21 and PcPoints > 21) or UsersPoints == 21:
    print("You win!")
else:
    print("You lose!")