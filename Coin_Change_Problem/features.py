#Main features function

#Gets the function from another file to be used
from parsing import parse_coin_data

def features():
    #This is an inner function for the features function
    def load_coin_denominations(file_path, country):
        #Calls the helper function
        return parse_coin_data(file_path, country)

    #This is another inner function for the features function 
    def coin_change_solver(target, denominations):
        #Had to use AI to figure out how this works
        #Calculations for the minimum amount of coins needed to go from 0 to the target num 
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        # Gets which coin is needed and subtracts it from the target
        coin_tracker = [-1] * (target + 1)

        #This loops through each of the coin and values in the dictionary
        for coin, value in denominations.items():
            for i in range(value, target + 1):  # Start from the coin value up to the target amount
                if dp[i - value] + 1 < dp[i]:  # Check if using the coin reduces the number of coins
                    dp[i] = dp[i - value] + 1  # Update the minimum number of coins needed
                    coin_tracker[i] = coin  # Record the coin used


        if dp[target] == float('inf'):
            return None, None

        result = []
        while target > 0:
            result.append(coin_tracker[target])
            target -= denominations[coin_tracker[target]]

        return len(result), result

    # Correctly return the inner functions
    return load_coin_denominations, coin_change_solver
