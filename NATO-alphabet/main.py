import pandas

# TODO 1. Create a dictionary in this fnew_key:new_value for (index, row)ormat:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetic_list = [phonetic_dict.get(letter) for letter in word]
print(phonetic_list)
