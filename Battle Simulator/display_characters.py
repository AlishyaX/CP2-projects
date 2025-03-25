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
