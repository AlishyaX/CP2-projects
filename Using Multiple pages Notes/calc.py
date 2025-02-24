#Alishya Xavier, Basics calculations functions

def get_num():
    return int(input('Tell me a number:\n'))

def addition(get_num):
    return get_num() + get_num()

def subtraction(x, y):
    return x - y

def division(x, y):
    return x/y

def multiplication(x, y):
    return x*y

#do not call functions at the end of pages
#Only if multiple pagegs:
if __name__ == "main":
    multiplication(5,2)