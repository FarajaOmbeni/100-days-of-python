import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','&','(',')','*','+']

print("Welcome to the password generator")
nr_letters = int(input("How many letters would you want?\n"))
nr_symbols = int(input("How many symbols would you want?\n"))
nr_numbers = int(input("How many numbers would you want?\n"))

# password_list = []
# full_password = ""
# for letter in range(0, nr_letters):
#     random_letter = random.randint(0, len(letters)-1)
#     letter = letters[random_letter]
#     full_password += letter
#     password_list.append(letter)

# for number in range(0, nr_numbers):
#     random_number = random.randint(0, len(numbers)-1)
#     number = numbers[random_number]
#     full_password += number 
#     password_list.append(number)

# for symbol in range(0, nr_symbols):
#     random_number = random.randint(0, len(symbols)-1)
#     symbol = symbols[random_number]
#     full_password += symbol
#     password_list.append(symbol)

# print(f"Here is your password: {full_password}")
# random.shuffle(password_list)
# randomized_pass = ""
# for i in password_list:
#     randomized_pass += i
# print("randomized password: "+randomized_pass)

#Her Solution
password = ""
password_list = []
for char in range(0, nr_letters):
    # password += random.choice(letters)
    password_list.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    # password += random.choice(symbols)
    password_list.append(random.choice(symbols))
for number in range(0, nr_numbers):
    # password += random.choice(numbers)
    password_list.append(random.choice(numbers))

for char in password_list:
    password += char

print(f"Your password is: {password}")