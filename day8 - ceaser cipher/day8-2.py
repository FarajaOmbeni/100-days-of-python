from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop = False

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:        
        if letter not in alphabet:
            output_text += letter
        else:
            index = alphabet.index(letter)

            new_index = (index + shift_amount) % len(alphabet)
            output_text += alphabet[new_index]
    print(f"This is the {direction}d result: {output_text}\n")

while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift:\n"))
    ask = ""
    ceaser(text, shift, direction)
    ask = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
    if ask == "no":
        print("Bye! Thanks for coming.")
        stop = True



# def encrypt(text, shift):
#     encoded_text = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         new_index = (index+shift) % len(alphabet)

#         encoded_text += alphabet[new_index]
#     print(f"Here is the encoded result: {encoded_text}")

# def decrypt(text, shift):
#     decrypted_text = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         new_index = (index-shift) % len(alphabet)

#         decrypted_text += alphabet[new_index]
#     print(f"Below is the decrypted text: {decrypted_text}")

# decrypt(text, shift)