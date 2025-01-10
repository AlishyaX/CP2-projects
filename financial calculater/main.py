# Alishya Xavier, Financial Calculater

'''

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
            payw = int(input('how much are you going to deposit?\n'))
            total = goal/payw
            print('It will take you',total,'weeks to reach your goal.')
            main()

        elif monthorweek == 'monthly':
            paym = int(input('how much are you going to pay monthly?\n'))
            total1 = goal/paym
            print('It will take',total1,'months to reach your goal.')
        else:
            print('That is not an option')
            save_goal()
    def c_i_calc():
        pass
    def budget_alloc():
        pass
    def s_p_calc():
        pass
    def tip_calc():
        price = float(input('How much is your end total?\n'))
        tipamount = float(input('What percentage amount would you like to tip'))
        tipamount/price

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
    main()
