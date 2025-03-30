#Parsing Coin Data function(Helper Function)

def parse_coin_data(file_path, country):
    try:
        #This opens the file and reads everything in it
        with open(file_path, 'r') as file:
            #This reads the header line and splits it
            header = file.readline().strip().split(',')
            #For every line in the file 
            for line in file:
                #Splits the line into coutry and denomination data
                row = line.strip().split(',', 1)
                #Makes sure the user typed in a country in the csv and then splits the denominations
                if row[0].strip().lower() == country.strip().lower():
                    denominations = row[1].split(',')
                    #Dictionary that stores the parsed coin data
                    coin_dict = {}
                    for coin in denominations:
                        #Splits the name and value of each coin in denominations
                        name, value = coin.strip().split('-')
                        coin_dict[name] = int(value)
                    #Returns the dictionary to be used to load the coin denominations
                    return coin_dict
    # These handle all error handling and is informative to the user of what happened
            raise ValueError(f"No coin data found for country: {country}")
    except FileNotFoundError:
        raise FileNotFoundError("The coin denomination file was not found.")
    except Exception as e:
        raise Exception(f"Error parsing coin data: {e}")
