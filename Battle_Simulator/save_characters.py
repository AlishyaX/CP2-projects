import csv
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

