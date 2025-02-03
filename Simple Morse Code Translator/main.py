#Alishya Xavier
#Simple Morse Code Translator

# This is a list of letters and numbers in English
english_number_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

# This is a list of Morse code for letters and numbers
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', ' / ']

# This is a function to translate English to Morse Code
def english_to_morse(english_text):
    # This is an empty string for the morse code translation
    morse_translation = ''
    for char in english_text.upper():
        if char in english_number_letters:
            index = english_number_letters.index(char)
            morse_translation += morse_code[index] + ' '
        else:
            #This is the output if they type in anything other than english letters or numbers
            morse_translation += '[Not written in English] '
    return morse_translation.strip()

# This is a function to translate Morse Code to English
def morse_to_english(morse_text):
    #This makes the code be able to be split into individual ones
    morse_chars = morse_text.split(' ')
    english_translation = ''
    for morse_char in morse_chars:
        if morse_char in morse_code:
            index = morse_code.index(morse_char)
            english_translation += english_number_letters[index]
        else:
            #This is what happens when they type in anything other than morse code letters or numbers
            english_translation += '[Not written in Morse Code] '
    return english_translation.strip()

# This is the Main function for user interface
def main():
    #This loop lets the user to pick one and it keeps going until they want to exit
    while True:
        print("\nMenu:")
        print("1. Translate English to Morse Code")
        print("2. Translate Morse Code to English")
        print("3. Exit")

        choice = input("Enter your choice: ")

        #This then takes each option to the specific function
        if choice == '1':
            english_text = input("Enter English text to translate: ")
            print("Morse Code:", english_to_morse(english_text))
        elif choice == '2':
            morse_text = input("Enter Morse Code to translate (use '/' for spaces): ")
            print("English text:", morse_to_english(morse_text))
        elif choice == '3':
            print("Thankyou for using the simple morse code generator!")
            break
        else:
            print("That is not an option.")

# This is the start of the program that calls the main function
main()
