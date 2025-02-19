#Testing
import csv

# Function to read the CSV file and return a list of movies
def read_movies():
    movies = []
    with open("Movie Recommender/list_of_movies.csv", mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies

# Function to print movies in a readable format
def print_movies(movies):
    if not movies:
        print("\nNo movies found matching your criteria.")
    else:
        print("\nRecommended Movies:")
        for movie in movies:
            print(f"Title: {movie['Title']}, Director: {movie['Director']}, Genre: {movie['Genre']}, "
                  f"Rating: {movie['Rating']}, Length: {movie['Length (min)']} mins, "
                  f"Notable Actors: {movie['Notable Actors']}")
    

# Function to filter movies based on user criteria
def filter_movies(movies, director=None, genre=None, rating=None, length=None, actor=None):
    filtered_movies = []
    for movie in movies:
        if director and director.lower() not in movie['Director'].lower():
            continue
        if genre and genre.lower() not in movie['Genre'].lower():
            continue
        if rating and rating.lower() not in movie['Rating'].lower():
            continue
        if length:
            try:
                if int(movie['Length (min)']) > length:
                    continue
            except ValueError:
                continue
        if actor and actor.lower() not in movie['Notable Actors'].lower():
            continue
        filtered_movies.append(movie)
    return filtered_movies

# Main function handling user interaction
def main():
    movies = read_movies()
   
    while True:
        selected_filters = []
        while True:
            choice = input("\nHow would you like to filter the movies? (Select at least 2 options)\n1. Director\n2. Genre\n3. Rating\n4. Length\n5. Notable Actors\n6. Show all movies\n7. Exit\nEnter a number for your choice (or type 'done' to finish selecting): ")

            if choice == 'done':
                if len(selected_filters) >= 2:
                    break
                else:
                    print("You must select at least two filters before proceeding.")
                    continue

            if choice == '1':
                director = input("Enter the director's name: ")
                selected_filters.append(('director', director))
            elif choice == '2':
                genre = input("Enter the genre: ")
                selected_filters.append(('genre', genre))
            elif choice == '3':
                rating = input("Enter the rating (e.g., PG, R, etc.): ")
                selected_filters.append(('rating', rating))
            elif choice == '4':
                try:
                    length = int(input("Enter the maximum length (in minutes): "))
                    selected_filters.append(('length', length))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            elif choice == '5':
                actor = input("Enter the name of a notable actor: ")
                selected_filters.append(('actor', actor))
            elif choice == '6':
                print_movies(movies)
                continue  # Restart the loop
            elif choice == '7':
                print("Exiting the program. Have a great day!")
                return
            else:
                print("Invalid option. Please enter a valid number from the list.")

        # Apply filters
        director = genre = rating = length = actor = None
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

        filtered_movies = filter_movies(movies, director, genre, rating, length, actor)
        print_movies(filtered_movies)

# Start the program
main()