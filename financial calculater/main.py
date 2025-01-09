# Alishya Xavier, Financial Calculater

'''
Create a program that completes the following basic financial calculations:
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator

PROJECT STEPS:
Create a main function that will run the user interface
Using project decomposition to figure out what other functions you need and how they interact with each other
Create your functions
Have at least 2 people test your code to make sure it works
'''
while True:

    def save_goal():
        #Finds what their goal is
        #Finds what there monthly or weekly deposits are 
        goal = int(input('What is your goal for how much you want to save:\n'))
        monthorweek = input('Are you going to give deposits weekly or monthly?\n')
        if monthorweek == 'weekly':
            payw = input('')
        elif monthorweek == 'monthly':
        else:
            print('That is not an option')

        pass
    def c_i_calc():
        pass
    def budget_alloc():
        pass
    def s_p_calc():
        pass
    def tip_calc():
        pass
    def main():
        #User interface
        #Calls all other functions
        print('Welcome to the basic financial calculator!\n')
        pick = input('What would you like to do?\n1. See how long it will take to save for a goal based on a weekly or monthly deposit\n2. Compound Interest Calculator\n3. Budget Allocator\n4. Sale Price Calculator\n5. Tip Calculator\n')
        if pick == '1':
            save_goal()
        elif pick == '2':
            c_i_calc()
        elif pick == '3':
            budget_alloc()
        elif pick == '4':
            s_p_calc()
        elif pick == '5':
            tip_calc()
        else:
            print('That is not one of the options')
            break

    main()
