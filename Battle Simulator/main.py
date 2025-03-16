#Alishya Xavier, Battle Simulator

#Lets us be able to read and write to a csv file
import csv


def main():
    # This is a list that stores all of the characters
    characters = []

    # This is a helper function that saves the characters to the csv file
    def save_characters(file_name, characters):
        if not characters:
            print("No characters to save!")
            return
        with open(file_name, mode='w', newline='') as file:
            # This saves the characters into the csv file by writing it as a dictionary 
            writer = csv.DictWriter(file, fieldnames=characters[0].keys())
            writer.writeheader()
            writer.writerows(characters)
            #Lets the user know what happened
            print(f"You have saved that character to '{file_name}'.")

    # This is a helper function that loads characters from a csv file
    def load_characters(file_name):
        try:
            with open(file_name, mode='r') as file:
                # This makes the characters into lists inside the dictionary
                characters = list(csv.DictReader(file))
                # This converts the stats into int
                for char in characters:
                    char['health'] = int(char['health'])
                    char['strength'] = int(char['strength'])
                    char['defense'] = int(char['defense'])
                    char['speed'] = int(char['speed'])
                    char['xp'] = int(char['xp'])
                    char['level'] = int(char['level'])
                return characters
        except FileNotFoundError:
            # This is what happens if the file isn't found
            print(f"File '{file_name}' has not been found.")
            return []

    # This is a helper function that checks if a character has leveled up
    def check_level_up(character):
        # Checks if the characters xp is higher or the same as it can be
        if int(character['xp']) >= 50:
            # This takes away 50 xp and makes them a level higher
            character['xp'] = int(character['xp']) - 50
            character['level'] = int(character['level']) + 1

            # This is what happens to that characters stats when they level up
            character['health'] += 10
            character['strength'] += 2
            character['defense'] += 1
            character['speed'] += 1
            print(f"{character['name']} leveled up to Level {character['level']}!")

    # This is a inner function that creates a new character.
    def create_character():
        try:
            # This gets the user's input for the details of the character
            name = input("Enter character name: ").strip().lower()
            #Checks if the name already exists
            if any(char['name'] == name for char in characters):
                print("A character with this name already exists. Choose a different name.")
                return
            # Set maximum values for each of the stats
            max_health = 200
            max_strength = 50
            max_defense = 30
            max_speed = 100

            # Informs the user the most the stats can be
            print(f"Health can be a maximum of {max_health}.")
            health = int(input("Enter health: "))
            if health > max_health:
                print(f"Health cannot exceed {max_health}. Please try again.")
                return

            print(f"Strength can be a maximum of {max_strength}.")
            strength = int(input("Enter strength: "))
            if strength > max_strength:
                print(f"Strength cannot exceed {max_strength}. Please try again.")
                return

            print(f"Defense can be a maximum of {max_defense}.")
            defense = int(input("Enter defense: "))
            if defense > max_defense:
                print(f"Defense cannot exceed {max_defense}. Please try again.")
                return

            print(f"Speed can be a maximum of {max_speed}.")
            speed = int(input("Enter speed: "))
            if speed > max_speed:
                print(f"Speed cannot exceed {max_speed}. Please try again.")
                return

            # This adds the character to the list with all of the stats
            characters.append({
                'name': name, 'health': health, 'strength': strength,
                'defense': defense, 'speed': speed, 'xp': 0, 'level': 1
            })
            # Lets the user know their character has been made
            print(f"Character '{name}' created successfully!")
        except ValueError:
            # If they type in not the right format for the stats
            print("That is not a valid option.")

    # This is an inner function that displays all of the characters
    def display_characters():
        # This checks if characters are in the list
        if characters:
            # This displays the detail for each of the characters
            for each_char in characters:
                print(f"{each_char['name']} - Health: {each_char['health']}, Strength: {each_char['strength']}, "
                      f"Defense: {each_char['defense']}, Speed: {each_char['speed']}, XP: {each_char['xp']}, "
                      f"Level: {each_char['level']}")
        else:
            print("There are no characters available!")

    # This is the inner function that makes two characters battle
    def battle():
        # Makes sure there is enough characters to battle
        if len(characters) < 2:
            print("There are not enough characters to battle!")
            return

        # Shows the user their options for characters and asks which ones they choose to fight
        display_characters()
        char1_name = input("Enter the first character: ").strip().lower()
        char2_name = input("Enter the second character: ").strip().lower()

        char1 = next((each_char for each_char in characters if each_char['name'].lower() == char1_name), None)
        char2 = next((each_char for each_char in characters if each_char['name'].lower() == char2_name), None)
        
        # Doesn't work if they are not created or are the same
        if not char1 or not char2 or char1 == char2:
            print("Those are invalid options.")
            return

        #Tells the user that the battle is starting between these two characters
        print('_________________________________________________________________________________')
        print(f"\nBattle starts: {char1['name']} vs {char2['name']}!")
        
        # Check if the characters have identical stats for a tie
        if (
            char1['health'] == char2['health'] and
            char1['strength'] == char2['strength'] and
            char1['defense'] == char2['defense'] and
            char1['speed'] == char2['speed']
        ):
            print(f"The battle between {char1['name']} and {char2['name']} is a tie! Both characters have identical stats.")
            return
        
        
        # This is a loop that makes the battle continue as long as both the char have health above 0
        while char1['health'] > 0 and char2['health'] > 0:
            # Whoever has the same or more speed attacks first(The attacker/defender)
            attacker, defender = (char1, char2) if char1['speed'] >= char2['speed'] else (char2, char1)
            
            # This calculates how much damage the attacker has placed on the defender
            damage = max(0, attacker['strength'] - defender['defense'])
            # Reducing the defenders health based on damage
            defender['health'] = max(0, int(defender['health']) - damage)
            # This shows who attacked who and the health of the defender
            print(f"{attacker['name']} attacks {defender['name']} for {damage} damage! {defender['name']} has {defender['health']} Health left.")

            # This checks when one of the char have been defeated and displays the winner
            if defender['health'] <= 0:
                print(f"{defender['name']} is defeated! {attacker['name']} wins!")
                print('_________________________________________________________________________________')
                # The attacker gets 20 xp for winning
                attacker['xp'] += 20
                check_level_up(attacker)
                break


        # Check for a tie if no meaningful damage occurs
        if char1['health'] > 0 and char2['health'] > 0 and char1['health'] == char2['health']:
            print(f"The battle between {char1['name']} and {char2['name']} ends in a tie!")

    # Main menu
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
            create_character()
        elif choice == '2':
            file_name = input("Enter file name to load: ")
            characters.extend(load_characters(file_name))
        elif choice == '3':
            file_name = input("Enter file name to save: ")
            save_characters(file_name, characters)
        elif choice == '4':
            display_characters()
        elif choice == '5':
            battle()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("That is not an option. Try again...")

# This starts the whole program
main()
