#Alishya Xavier, Coin Change Problem
from features import features

# Unpack the returned functions
load_coin_denominations, coin_change_solver = features()


def main():
    #The relative path of the csv file is saved into a variable that is used throughout the program
    file_path = "Coin_Change_Problem/denominations.csv"  
    print("Welcome to the Coin Change Solver!")

    #This keeps looping until they choose to exit
    while True:

        choice = input("\nWhat would you like to do?\n1. Type in your coin change amount\n2. Exit\nChoice: ").strip()
        if choice == '1':
            #This lets the user input the country and the amount of cents to be chaanged into coins
            country = input("Enter the country name: ").strip()

            try:
                # Load coin denominations for the given country
                denominations = load_coin_denominations(file_path, country)
                #Displays the coin denominations for that country
                print(f"Coin denominations for {country}: {denominations}")

                # Ensure the target amount is valid
                while True:
                    try:
                        target = int(input("Enter the target amount: ").strip())
                        
                        # Checks if the target is unnecesisarily large
                        if target > 10**6:  
                            print("Error: Target amount is too large to process. Please enter a smaller value.")
                            continue
                        elif target <= 0:  # Makes sure the target amount is more than 0
                            print("Target amount must be greater than 0. Please try again.")
                            continue
                        else:
                            break
                    #Error Handling
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                min_coins, coins_used = coin_change_solver(target, denominations)
                
                #Makes sure that it is possible to use the coins to make the target amount
                if min_coins is None:
                    print(f"The target amount {target} cannot be made with the given coins.")
                else:
                    print(f"Minimum number of coins needed: {min_coins}")
                    print(f"Coins used: {coins_used}")

            #Lets the user know what error happened if one does occur
            except Exception as e:
                print(f"Error: {e}")
        
        #If they want to exit
        elif choice == '2':
            print("Thank you for using the Coin Change Solver!")
            exit()

        #If something other than the options are inputted
        else:
            print("That's not an option. Try Again..")

#Starts the whole program
main()

