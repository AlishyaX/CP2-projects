#Alishya Xavier, Using Multiple pages notes



#QUESTIONS:
#-------How do you make multiple files in python?--------
#You can make multiple files in pythonby clicking new file and end it with .py.
#snake case file names
#descriptive names but also short
#-How do you get a function from another file

from calc import addition as add, subtraction as sub
#star lets you import everything
#alising is hwere you import a function and you give it a new name

print(add())
print(sub(20,8))


#--------How do you get variables from another file?-------
#You could add it to the list(from calc import add...)
#Usually you should keep it on one page and what you could do is have the variable in a function and call the function

#---------How do you have a function with multiple returns?-------
#You can have a function with multiple returns by writing return name, age, color
def get_user_info():
    name = input("What is your name:/n")
    age = input("What is your age:/n")
    color = input("What is your favorite color:/n")
    return name, age, color
name, age, color = get_user_info()

print(age)


#---------Why would you use multiple pages for a python project?-------
#You would use multiple pages because:
#Easier to merge github branches if you are writing on seperate pages
#Modularity - breaking program into smaller more managable pieces.
#Functionality - specific functions used in multiple locations should get their own page(keeps code clean)


#Main should only include the intro stuff and the user interface


