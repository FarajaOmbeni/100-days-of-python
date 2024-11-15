import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_alphabet = {row.letter:row.code for (index, row) in alphabet.iterrows()}
# print(phonetic_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
sounds = [phonetic_alphabet[letter] for letter in user_input]
print(sounds)