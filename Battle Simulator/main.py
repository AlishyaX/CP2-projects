#Alishya Xavier, Battle Simulator

#Comments
#Error Handling
#ReadME file

from visualization import radar_chart
from data_analysis import analyze_characters
from random_generation import generate_character


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
        print("1. Create a character manually")
        print("2. Generate a random character")  # New option for random generation
        print("3. Load characters from file")
        print("4. Save characters to a file")
        print("5. Display characters")
        print("6. Battle")
        print("7. Visualize a character's stats")  # New option for visualization
        print("8. Analyze character data")        # New option for analysis
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_character(characters)
        elif choice == '2':
            # Generate and add a random character to the list
            random_character = generate_character()
            characters.append(random_character)
            print(f"Random character '{random_character['name']}' created successfully!")
            print(f"Backstory: {random_character['backstory']}")
        elif choice == '3':
            file_name = input("Enter file name to load: ")
            characters.extend(load_characters(file_name))
        elif choice == '4':
            file_name = input("Enter file name to save: ")
            save_characters(file_name, characters)
        elif choice == '5':
            display_characters(characters)
        elif choice == '6':
            battle(characters)
        elif choice == '7':
            # Visualize a character's stats using Matplotlib
            char_name = input("Enter the character's name to visualize: ")
            character = next((char for char in characters if char['name'].lower() == char_name.lower()), None)
            if character:
                radar_chart(character)
            else:
                print("Character not found.")
        elif choice == '8':
            # Analyze character data using Pandas
            if characters:
                analyze_characters(characters)
            else:
                print("No character data available for analysis.")
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("That is not an option. Try again...")

# This starts the whole program
main()
