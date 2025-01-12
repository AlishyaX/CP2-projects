# Alishya Xavier, Financial Calculater

# This is my function for how long it will take to save for a goal based on a weekly or monthly deposit
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
# This is my function for my compound interest calculator
def c_i_calc():
    # Gets all of the users information for initial investments, anual interest rate, years invested, and times interest has been compounded
    initial = float(input('What is your initial investment in dollars: '))
    rate = float(input('What is the annual interest rate as a decimal: '))
    time = float(input('How many years has the money been invested: '))
    per_year = float(input('How many times has interest been compounded per year: '))

    #The compound interest formula
    amount = initial * (1 + rate / per_year) ** (per_year * time)
    #prints the final compund interest amount
    print('Your final compound interest amount: $',amount,'')

#This is my function for the budget allocater
def budget_alloc():
    #Gathers the users information based off of total income, percentage you want saved, percentage for entertainment, and percentage for food
    income = float(input('What is your total income: '))
    savings_percent = float(input('What is the percentage of income you want to save: '))
    entertainment_percent = float(input('What is the percentage of income you want for entertainment: '))
    food_percent = float(input('What is the percentage of income you want for food: '))

    #These formulas divide up the total to allocate money into each group due to percent
    savings = income * savings_percent / 100
    entertainment = income * entertainment_percent / 100
    food = income * food_percent / 100

    #This prints the total outcome of how much money can be spent in each catagory
    print('Here is your allocated budget:\n')
    print('For savings you have:',savings)
    print('For entertainment you have:',entertainment)
    print('For food you have:',food)

#This is my sale price calculater function
def s_p_calc():
    #Thsi gathers the information of the original price and discount percentage
    orig_price = float(input('What is the original price of the item: '))
    discount_perc = float(input('What is the discount percentage as a decimal: '))
    
    #This is the formulas to find the sale price
    discount_amount = orig_price * discount_perc
    sale_price = orig_price - discount_amount

    #Here it displays the sale price in the output
    print('The sale price is $',sale_price)

#This is the tip calculator function
def tip_calc():
    #This gathers the infrmation of the total amount on bill, and desired tip percentage
    total = float(input('What is the total amount of the bill: '))
    tip_perc = float(input('What is your desired tip percentage as a decimal: '))

    #This is ther formula to get the tip amount
    tip_amount = total * tip_perc
    #THis displays the tip amount in the output
    print('The tip amount is $',tip_amount)
#This is the main function that handles user interface
def main():
    #This while True loops the following code until the user types in 6.
    while True:
        #User interface
        #Calls all other functions
        print('Welcome to the basic financial calculator!\n')
        pick = input('What would you like to do?\n1. See how long it will take to save for a goal based on a weekly or monthly deposit\n2. Compound Interest Calculator\n3. Budget Allocator\n4. Sale Price Calculator\n5. Tip Calculator\n6. None\n')
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
        elif pick == '6':
            break
        else:
            print('That is not one of the options')

#This is the start of the whole program by calling the main function
main()
