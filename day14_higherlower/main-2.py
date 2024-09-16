from art import logo, vs
from game_data import data
import random

#Print the logo
print(logo)
score = 0
continue_game = True

#Compare Guesses
def compare_guess(guess, account1_followers, account2_followers):
    if guess == 'a':
        if account1_followers > account2_followers:
            return True
        else:
            return False
    elif guess == 'b':
        if account2_followers > account1_followers:
            return True
        else:
            return False

#Print accounts
def format_data(account):
    '''Takes in an account and returns a readable outup'''
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}"

account2 = random.choice(data)

while continue_game:
    #Choose 2 random accounts
    account1 = account2
    account2 = random.choice(data)

    if account2 == account1:
        account2 = random.choice(data)

    print(f"Compare A: {format_data(account1)}")
    print(vs)
    print(f"Against B: {format_data(account2)}")

    #Get the number of followers
    account1_followers = account1['follower_count']
    account2_followers = account2['follower_count']

    #Prompt the user to guess
    guess = input("Who has more followers? 'A' or 'B': ")

    print('\n'*20)
    print(logo)

    #Compare Guesses
    comparison = compare_guess(guess, account1_followers, account2_followers)
    if comparison:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False