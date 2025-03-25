#Alishya Xavier, Battle Simulator
from save_characters import save_characters
from check_level_up import check_level_up
from load_characters import load_characters
from create_character import create_character
from display_characters import display_characters
from battle import battle

def main():
    # This is a list that stores all of the characters
    characters = []

    while True:
        # Lets the user input one of the options that keeps repeating until they exit
        print("\nWhat would you like to do?")
        print("1. Create a character")
        print("2. Load characters from file")
        print("3. Save characters to a file")
        print("4. Display characters")
        print("5. Battle")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_character(characters)
        elif choice == '2':
            file_name = input("Enter file name to load: ")
            characters.extend(load_characters(file_name))
        elif choice == '3':
            file_name = input("Enter file name to save: ")
            save_characters(file_name, characters)
        elif choice == '4':
            display_characters(characters)
        elif choice == '5':
            battle(characters)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("That is not an option. Try again...")

# This starts the whole program
main()
