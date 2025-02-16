#Alishya Xavier, Movier Recommender

#imports csv from the list of movies csv file
import csv

#This function reads the csv file and returns the list of movies
def read_movies():

    #makes an empty list to save all of the movies data
    movies = [] 

    # Opens the CSV file containing the list of movies
    with open("Movie Recommender/list_of_movies.csv", mode='r', newline='', encoding='utf-8') as file:
        # This creates a CSV DictReader object to make it able to read the rows in the file as a dictionary
        reader = csv.DictReader(file)  
        # Loop through each row in the CSV file
        for row in reader:
            # Add each row from the CSV file to the movies list
            movies.append(row)  

    return movies 

# This function prints the entire list of movies
def print_movies(movies):
    # Loops through each movie in the list
    for movie in movies:  
        # Prints out the details of the movie 
        print(f"Title: {movie['Title']}, Director: {movie['Director']}, Genre: {movie['Genre']}, Rating: {movie['Rating']}, Length: {movie['Length (min)']} mins, Notable Actors: {movie['Notable Actors']}")


# This function filters th emovies to be able to find ones in that exact information they typed in
def filter_movies(movies, director=None, genre=None, rating=None, length=None, actor=None):
    #This list stores all of the movies that match the information they inputted
    filtered_movies = [] 

    #Loops through each movie
    for movie in movies: 
        # This only provides movies with the specific informations but if it doesn't match then it will skip that movie
        if director and director.lower() not in movie['Director'].lower():
            continue
        if genre and genre.lower() not in movie['Genre'].lower():
            continue
        if rating and rating.lower() not in movie['Rating'].lower():
            continue

        # This lets them pick a time limit fro a movie and only displays movies with that length or lower
        if length:
            try:
                if int(movie['Length (min)']) > length:
                    continue
            except ValueError:
                continue

        #This makes sure that it will skip the movie if they inputted an actor but it doesn't match
        if actor and actor.lower() not in movie['Notable Actors'].lower():
            continue
        # If all of the options match then it will add it to the filtered list
        filtered_movies.append(movie)
    return filtered_movies 

# This is the main function that handles user interface
def main():
    #This reads the list of movies from the CSV file
    movies = read_movies()
    
    #An infinite loop that asks for their option until they type 'end'
    while True: 
        # The options the user can choose for what they want to sort the movies by
        print("\nHow would you like to sort it by:")
        print("1. Director")
        print("2. Genre")
        print("3. Rating")
        print("4. Length")
        print("5. Notable Actors")
        print("6. Show all movies")
        print('7. End')
        
        #A list to save all of the filters the user chooses
        selected_filters = [] 

        # Let the user select as many filters they want until they type in 'done'
        while True:
            # Asks the user for their choice
            choice = input("Enter your choice(type 'done' when you are finished selecting your choices): ")
            
            # If the user types 'done' it makes sure they had at least 2 choices
            if choice == 'done':
                if len(selected_filters) >= 2:
                    break  
                else:
                    print("You must select at least two choices before proceeding.")
                    continue  
            
            # This gathers the users choice for each option and puts it in the selected filter lsit
            if choice == '1':
                director = input("Enter the director: ")
                selected_filters.append(('director', director))
            elif choice == '2':
                genre = input("Enter the genre: ")
                selected_filters.append(('genre', genre)) 
            elif choice == '3':
                rating = input("Enter the rating: ")
                selected_filters.append(('rating', rating)) 
            elif choice == '4':
                try:
                    length = int(input("Enter the maximum length (in minutes): "))
                    selected_filters.append(('length', length))
                except ValueError:
                    #This is makes it more user friendly
                    print("That is not a valid length number.") 
                    continue 
            elif choice == '5':
                actor = input("Enter the actor: ")
                selected_filters.append(('actor', actor))
            elif choice == '6':
                #This displays all of the movie options
                print_movies(movies)
                continue 
            elif choice == '7':
                print("Exiting the program. Bye Bye! :)")
                return
            else:
                print("That is not an option.")
                continue


        
        #This makes them have nothing to start with so that the user can input them into these
        director = genre = rating = length = actor = None

        #This loop collects the users input and puts them equal to variables used later
        for filter_type, filter_value in selected_filters:
            if filter_type == 'director':
                director = filter_value 
            elif filter_type == 'genre':
                genre = filter_value  
            elif filter_type == 'rating':
                rating = filter_value  
            elif filter_type == 'length':
                length = filter_value  
            elif filter_type == 'actor':
                actor = filter_value  
        
        # This puts the filtered movies with the options into a variable to be used to find the movies fit for the movies that fit those catigories
        filtered_movies = filter_movies(movies, director, genre, rating, length, actor)
        
        # This sees if they are in that function and prints all of the recommended movies if there are any
        if filtered_movies:
            print("\nRecommended Movies:")
            print_movies(filtered_movies)  # Display the filtered list of movies
        else:
            print("\nThere are no movies based on those options.")  # If no movies match the filters, print this message


#This is the start of the whole project as it calls the main function
    main()