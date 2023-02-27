# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

LETTERS_PATH = "./Input/Letters/starting_letter.txt"
NAMES_PATH = "./Input/Names/invited_names.txt"
OUTPUT_PATH = "Output/ReadyToSend/"
PLACEHOLDER = "[name]"

names_file = open(NAMES_PATH, "r")
names_list = names_file.readlines()

letter_file = open(LETTERS_PATH, "r")
letter_content = letter_file.read()

for name in names_list:
    curr_name = name.strip()  # to remove the newline
    letter_path = OUTPUT_PATH + "letter_for_" + curr_name + ".txt"
    content = letter_content.replace(PLACEHOLDER, curr_name)
    with open(letter_path, mode="w") as file:
        file.write(content)
