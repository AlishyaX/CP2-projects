#Alishya Xavier, Personal Library Program

# this is my function to add a new song with the song name and artist
def add_item(library):

    print('Lets add a new song!')

    song = input('What is the title of the song: ')
    artist = input('What is the artists name: ')

    #This adds them to my library set
    library.add((artist, song))

    print('You have added a new music item!')

#This is my function to search for a song by the artists name
def search_item(library, artist):

    print(f"Here are the songs by {artist}:")

    #This for loop keeps going until there are no more songs by a certain artist
    for song in library:
        if song[0] == artist:
            print(f"- {song[1]}")
        else:
            print('There are no songs by that artist.')

#This function removes a song from the library set
def remove_item(library):

    artist = input('What is the artist name: ')
    song = input('What is the song title: ')

    try:
        library.remove((artist, song))
        print('You removed',song,'by',artist)

    except KeyError:
        print('That song is not in your library.')

#This function prints the whole library to the user
def display_library(library):

    if not library:
        print("Your library is empty.")

    else:
        print("\nYour music library:")

        #Used enumerate to list all of the elements in the library set 
        for i, (artist, song) in enumerate(library, 1):
            print(f"{i}. Artist: {artist}, Song: {song}\n")
        
#This is the main function that is ran first and has most of the user interface
def main():

    #Had to search up what a set would look like if it started with nothing in it(would be a dictionary if the set was empty)
    #This is my library set that all of the songs and artists are put into are removed from
    library = set()

    print('Welcome to your personal library for music!')

    #This is a while true loop that keeps running until the user wants to exit
    while True:
        option = input('\nWhat would you like to do?\n1. Add music\n2. Remove music\n3. Search for music\n4. Display all music\n5. Exit\n\nYour choice: ')
        if option == '1':
            add_item(library)

        elif option == '2':
            remove_item(library)

        elif option == '3':
            artist = input('What artist would you like to search for: ')
            search_item(library, artist)

        elif option == '4':
            display_library(library)

        elif option == '5':
            print('Thankyou for using your personal library! :)')
            break
        
        else:
            print('That is not an option')

#This is the start to the program as it calls the main function that holds the user interface
main()