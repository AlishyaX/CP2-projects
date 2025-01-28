#Alishya Xavier
#Random Password Gererator

#These make the code able to randomly pick a choice and use the string constant
import random
import string


#This is the function for the length of each password
def length():
    while True:
        user_password_length = input("What is the length of your password: ")
        if user_password_length.isdigit():
            return int(user_password_length)
        else:
            print('That is not an option')
            


#This is the function to use uppercase letters in the password
def uppercase():
    while True:
        user_uppercase_letters = input("Do you want to use uppercase letters? (y/n): ").lower()
        if user_uppercase_letters == 'y':
            return True
        elif user_uppercase_letters == 'n':
            return False
        else:
            print('That is not an option')
    

#This is the function to use lower case letters in the password
def lowercase():
    while True:
        user_lowercase_letters = input("Do you want to use lowercase letters? (y/n): ").lower()
        if user_lowercase_letters == 'y':
            return True
        elif user_lowercase_letters == 'n':
            return False
        else:
            print('That is not an option')
    


#This is the function to use numbers in the password
def num():
    while True:
        user_num = input("Do you want to use numbers? (y/n): ").lower()
        if user_num == 'y':
            return True
        elif user_num == 'n':
            return False
        else:
            print('That is not an option')

#This is the function to use special characters in the password
def special_char():
    while True:
        user_special_character = input("Do you want to use special characters? (y/n): ").lower()
        if user_special_character == 'y':
            return True
        elif user_special_character == 'n':
            return False
        else:
            print('That is not an option')
    

'''
This is the function that uses ASCII letters to be able to not 
have to make a seperate list with all of the options but instead
just get to pull it from a pre-made one that python already recognizes
'''

def data_collection(length, upper, lower, digits, special):
    char = ''
    if upper:
        char += string.ascii_uppercase
    if lower:
        char += string.ascii_lowercase
    if digits:
        char += string.digits
    if special:
        char += string.punctuation

    password = ''.join(random.choice(char) for x in range(length))
    return password



# This function gathers the information from the variables to then be able to make 4 different passwords with the requirements
def key():
    len = length()
    upper = uppercase()
    lower = lowercase()
    numbers = num()
    special_characters = special_char()
    passwords = [data_collection(len, upper, lower, numbers, special_characters) for x in range(4)]
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")


#This is the main function that handles user interface by asking the user what they want to do
def main():
    while True:
        option = input('What do you want to do:\n1. Make 4 passwords\n2. Exit\n')
        if option == '1':
            key()
        elif option == '2':
            print('Have a good day! :)')
            break
        else:
            print('That is not one of the options')

#This is the start of the program by calling the main function
main()
