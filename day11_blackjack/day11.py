import art
import random
my_cards = []
computer_cards = []

def print_cards():
    print(f"\tYour cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards: list):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #end program
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def start_game():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    choice = choice.lower()
    if choice == 'y':
        my_cards.clear()
        computer_cards.clear()
        print(art.logo)
        for _ in range(2):
            my_cards.append(deal_card())
            computer_cards.append(deal_card())
        if calculate_score(my_cards) and calculate_score(computer_cards)  <= 21:
            print_cards()
            get_another_card()
        else:
            print("INFO: The was an error dealing the cards")
            start_game()
    else:
        "Thanks for playing!"

def get_winner():
    '''Logic to see who the winner of the game is'''
    print(f"\tYour final hand: {my_cards}, final score: {calculate_score(my_cards)}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    if calculate_score(computer_cards) > 21:
        print("Opponent went over. You win 😁")
    elif calculate_score(my_cards) > 21:
        print("You went over, You Lose 😤")
    elif calculate_score(my_cards) > calculate_score(computer_cards):
        print("You have higher. You win 😁")
    elif calculate_score(my_cards) == 21:
        print("You win by BlackJack 😁")
    elif calculate_score(computer_cards) == 21:
        print("Opponent wins by BlackJack 😁")
    elif calculate_score(computer_cards) > calculate_score(my_cards):
        print("You Lose 😤")
    elif calculate_score(my_cards) == calculate_score(computer_cards):
        print("It's a DRAW")

def get_another_card():
    choice2 = (input("Type 'y' to get another card, type 'n' to pass: "))
    choice2 = choice2.lower()
    if choice2 == 'y':
        my_cards.append(deal_card())
        print_cards()
        if calculate_score(my_cards) < 21:
           get_another_card() 
        else:
            get_winner()
            start_game()
    elif choice2 == 'n':
        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())
        get_winner()
        start_game()

start_game()