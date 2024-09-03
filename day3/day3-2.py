print("Welcome to the rollercoaster")
height = int(input("Enter your height: "))
bill = 0

if height >= 123:
    print("You can ride the rollercoaster")
    age = int(input("What is your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif 45 <= age <=55:
        print("You can ride for free")
    else: 
        bill = 12
        print("Adult tickets are $2")
    
    wants_photo = input("Do you want a photo? y or n. ")
    if wants_photo == 'y':
        bill +=3
    
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")