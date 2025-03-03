#Alishya Xavier, Advanced Functions Notes

#QUESTIONS
#1. What is a helper function?
#A helper function is a function that you write to call in another function
def is_int(user_input):
    try:
        int(user_input)
    except:
        #8. What is recursion?
        #When you call a function inside of itself

        #9. How does recursion work?
        #Giving a function new information as you run the function over and over again.
        print('Please give me a number.')
        user_input = is_int(input('How old are you?\n'))
    return user_input

def age():
    old = is_int(input('How old are you?\n'))

    print(f"Cool. You are {old}")

age()

#2. What is the purpose of a helper function?
#Its purpose is to make your functions simpler by taking so many steps and putting them into multiple helper functions.

#3. What is an inner function?
# An inner function is a function that exists inside another function.

def add(a):
    b = int(input("Give me a number:"))

    def addition():
        print(a+b)
    addition()

add(3)

#4. What is the scope of a variable in a function WITH an inner function?
# It has access to all of the outer functions variables(local function that can access all of the local variables)
# Stuff in th outer function can be accessed in the inner function but not vise versa


#5. Why do we use inner functions?
# This lets us have less returns and variables
# They are used sparingly and only as needed

#6. What is a closure function?
# A closure function is s
# omething that accesses variables from its outer scope, even after the outer function has been run
def add(a):

    def addition(b):
        return a + b
    
    return addition()

base = add(10)
print(base(5))
#7. Why do we write closure functions?
#It saves the information to multiple calls 
# To make a function have private variables that are used throughout that function.

