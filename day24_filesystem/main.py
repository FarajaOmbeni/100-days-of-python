#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

""" MY APPROACH WITHOUT read() method """
# with open('day24_filesystem/Input/Names/invited_names.txt', 'r') as name_file:
#     names = name_file.readlines()

# with open('day24_filesystem/Input/Letters/starting_letter.txt', 'r') as letter_file:
#     letter = letter_file.readlines()
# letter = letter[::2]

# greeting = letter[0]
# body = letter[1:]
# print("Started creating letters....\n")
# for i in range(len(names)):
#     name = names[i]
#     personal_greeting = greeting.replace('[name],', name)
#     with open(f'day24_filesystem/Output/ReadyToSend/letter_to_{names[i].strip()}.txt', 'w') as personal_letter:
#         personal_letter.write(f"{personal_greeting.strip()},\n")
#         for j in range(len(body)):
#             personal_letter.write(f"\n{body[j]}")
# print("Letters Created Succesfully!")

""" SIMPLER APPROACH WITH read() method """
with open('day24_filesystem/Input/Names/invited_names.txt', 'r') as name_file:
    names = name_file.readlines()

with open('day24_filesystem/Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace('[name]', stripped_name)
        with open(f'day24_filesystem/Output/ReadyToSend/letter_for_{stripped_name}.txt', 'w') as new_letter_file:
            new_letter_file.write(new_letter)