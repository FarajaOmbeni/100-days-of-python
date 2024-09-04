print("Welcome to the Treasure Island.\nYour mission is to find the treasire")
print("Choose left or right")
choice1 = input("\t\"left\" or \"right\"\n")
if choice1 == "left" or choice1 == "LEFT":
    choice2 = input("You have encountered a lake.\nDo you want to `wait` or `swim` accross the lake?\n")
    if choice2 == "wait" or choice2 == "WAIT":
        choice3 = input("You a in front of 3 doors. red, blue and yellow. Which one do you choose?\n")
        if choice3 == "red" or choice3 == "RED":
            print("Burned by fire. GAME OVER")
        elif choice3 == "blue" or choice3 == "BLUE":
            print("Eaten by beasts. GAME OVER")
        elif choice3 == "yellow" or choice3 == "YELLOW":
            print("YOU WIN")
        else:
            print("You chose a door that does not exist. GAME OVER")
    else:
        print("Game over. You were attacked by a shark")
else:
    print("You fell inside a hole")