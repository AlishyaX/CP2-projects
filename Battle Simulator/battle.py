from display_characters import display_characters

# This is the inner function that makes two characters battle
def battle(characters):
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
