import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty.lower()
lives = 0

numbers = list(range(1, 101))
random_choice = random.choice(numbers)

def guessing_game(lives: int):
    while lives != 0:
        user_guess = int(input("Make a guess: "))
        if user_guess < random_choice:
            lives -= 1
            print(f"Too low\nGuess again\nYou have {lives} attemps remaining.")
        elif user_guess > random_choice:
            lives -= 1
            print(f"Too high\nGuess again\nYou have {lives} attemps remaining.")
        elif user_guess == random_choice:
            print(f"You got it! The answer was {random_choice}")
            return
    print(f"You've run out of guesses, lose.\nPsst, the correct answer is {random_choice}")
    

if difficulty == 'easy':
    lives = 10
    print(f"You have {lives} attemps remaining")
    guessing_game(lives)

elif difficulty == 'hard':
    lives = 5
    print(f"You have {lives} attemps remaining")
    guessing_game(lives)
else:
    print("You did not choose an appropriate level")