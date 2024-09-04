from hangman_words import word_list
from hangman_art import stages
import random

chosen_word = random.choice(word_list)
# print(chosen_word)
placeholder = ""

for underscore in chosen_word:
    placeholder += "_"

print(placeholder)
game_over = False
correct_letters = []
lives = 6
while not game_over:
    print(f"***********You have {lives}/6 lives left**********")
    guess = input("Guess a lettter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    elif guess not in chosen_word:
        print(f"You chose {guess}. You lose a life")
        lives -= 1
    
    print(lives)
    print(stages[lives])
    print(display)
    
    if chosen_word == display:
        print("***********YOU WIN***********")
        game_over = True
    elif lives == 0:
        print(f"***********YOU LOSE. The word was {chosen_word}***********")  