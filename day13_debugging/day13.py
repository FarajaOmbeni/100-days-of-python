try:
    age = int(input("How old are you? "))
except ValueError:
    print("you have typed an invalid number. Please try again with a numberical value")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}")