#Alishya Xavier
#Random Password Gererator

#These make the code able to randomly pick a choice and use the string constant
import random
import string


#This is the function for the length of each password
def length():
    return int(input("How long do you want your password: "))


#This is the function to use uppercase letters in the password
def uppercase():
    return input("Do you want to use uppercase letters? (y/n): ").lower() == 'y'


#This is the function to use lower case letters in the password
def lowercase():
    return input("Do you want to use lowercase letters? (y/n): ").lower() == 'y'


#This is the function to use numbers in the password
def num():
    return input("Do you want to use numbers? (y/n): ").lower() == 'y'


#This is the function to use special characters in the password
def special_char():
    return input("Do you want to use special characters? (y/n): ").lower() == 'y'

'''
This is the main function that uses ASCII letters to be able to not 
have to make a seperate list with all of the options but instead
just get to pull it from a pre-made one that python already recognizes
'''

def main(length, upper, lower, digits, special):
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


# These variables are used in the key function to be able to print all of the questions together
len = length()
upper = uppercase()
lower = lowercase()
numbers = num()
special_characters = special_char()


# This function gathers the information from the variables to then be able to make 4 different passwords with the requirements
def key():
    passwords = [main(len, upper, lower, numbers, special_characters) for x in range(4)]
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")


#This is the start of the program by calling the key function
key()