import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
string_choices = ["rock", "paper", "scissors"]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))
computer_choice = random.randint(0,2)

if user_choice == computer_choice:
    print(f"{string_choices[user_choice]}\n{choices[user_choice]}\nComputer choice:\n{string_choices[computer_choice]}\n{choices[computer_choice]}\nDraw")
elif user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
    print(f"{string_choices[user_choice]}\n{choices[user_choice]}\nComputer choice:\n{string_choices[computer_choice]}\n{choices[computer_choice]}\nComputer Won")
elif computer_choice == 0 and user_choice == 1 or computer_choice == 1 and user_choice == 2 or computer_choice == 2 and user_choice == 0:
    print(f"{string_choices[user_choice]}\n{choices[user_choice]}\nComputer choice:\n{string_choices[computer_choice]}\n{choices[computer_choice]}\nYou Won")
else:
    print("You did not choose a valid option. TRY AGAIN")