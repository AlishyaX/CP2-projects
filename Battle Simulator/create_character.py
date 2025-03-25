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
