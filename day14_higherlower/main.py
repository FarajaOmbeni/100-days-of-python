from art import logo, vs
from game_data import data
import random

#Get 2 random people from the game_data list
random_account = []
for _ in range(2):
    random_account.append(random.choice(data))

def format_data(account):
    name = random_account[account]['name']
    description = random_account[account]['description']
    country = random_account[account]['country']

    return f"{name}, a {description}, from {country}"

def get_followers(account):
    followers = random_account[account]['follower_count']
    return followers

score = 0

#Print the logo
print(logo)

#Create a funcion to print the people we are comparing
def print_contestants():
    print(f"Compare A: {format_data(0)}")
    print(vs)
    print(f"Against B: {format_data(1)}")

#Pint the contestants
print_contestants()

def get_user_choice():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    choice.lower()
    return choice

#Choode another option to compare with
def choose_random_option(index):
    global score
    random_account.remove(random_account[index])
    random_choice = random.choice(data)
    if random_choice not in random_account:
        random_account.append(random_choice)
        score += 1
        print(f"You're right! Current Score: {score}")
        print_contestants()
    else:
        choose_random_option(index)

#Compare the number of followers
def play_game():
    choice = get_user_choice()
    print("\n"*20)
    if choice == 'a' and  get_followers(0) >  get_followers(1):
        print(logo)
        choose_random_option(0)
        play_game()
    elif choice == 'b' and get_followers(1) > get_followers(0):
        print(logo)
        choose_random_option(1)
        play_game()
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final Score: {score}")
        return

play_game()