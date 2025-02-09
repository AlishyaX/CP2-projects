#Alishya Xavier, Personal Library Program

# this is my function to add a new song with the song name and artist
def add_item(library):

    print('Lets add a new song!')

    #Gathers the information about the song etc.
    song = input('What is the title of the song: ')
    artist = input('What is the artists name: ')
    album = input("What is the album name: ")
    year = input("What is the release year: ")

    #Adds all of that information to the library
    library.append({
        "title": song,
        "artist": artist,
        "album": album,
        "year": year
    })
    

    print('You have added a new music item!')

#This is my function to search for a song by the artists name
def search_item(library, artist):

    print(f"Here are the songs by {artist}:")

    #This for loop keeps running the items unless there arew no songs by that artist
    if_found = False
    for item in library:
        if item["artist"].lower() == artist.lower():
            print(f"- {item['title']} (Album: {item['album']}, Year: {item['year']})")
            if_found = True

    if not if_found:
        print("There are no songs by that artist.")

#This function removes a song from the library set
def remove_item(library):

    artist = input('What is the artist name: ')
    song = input('What is the song title: ')

    # This is a for loop that checks to see if that item is in the library and it will remove it if it is
    for item in library:
        if item["artist"].lower() == artist.lower() and item["title"].lower() == song.lower():
            library.remove(item)
            print(f"You removed '{song}' by {artist}.")
            return

    print("That song is not in your library.")


#This function prints the whole library to the user
def display_library(library):

    if not library:
        print("Your library is empty.")
        return

    #Gathers the info if they want to display just the title and artist or all of the info
    option = input("Would you like to see a simple list or a detailed list? (simple/detailed): ").strip().lower()

    #prints the output depending on what the users input
    if option == "simple":
        print("\nYour music library (Simple List):")
        for i, item in enumerate(library, 1):
            print(f"{i}. {item['title']} by {item['artist']}")
    elif option == "detailed":
        print("\nYour music library (Detailed List):")
        for i, item in enumerate(library, 1):
            print(f"{i}. Title: {item['title']}, Artist: {item['artist']}, Album: {item['album']}, Year: {item['year']}")
    else:
        print("Invalid option. Please choose 'simple' or 'detailed'.")

#New function that updates the library
def update_item(library):
    #Gathers the input for the song title and artist to be able to get the item to update
    song = input("Enter the title of the song to update: ")
    artist = input("Enter the artist's name: ")

    #a for loop that loops through each item in the library
    for item in library:
        #This checks if both the title and the artists are the same
        if item["title"].lower() == song.lower() and item["artist"].lower() == artist.lower():
            #This shows the details before the update of the item
            print("Current details:")
            print(f"Title: {item['title']}, Artist: {item['artist']}, Album: {item['album']}, Year: {item['year']}")
            print("If you don't want to change it then just click enter.")

            #This gathers information for the new updated item(keeps he same value if nothing is inputted in)
            new_title = input("New title: ") or item["title"]
            new_artist = input("New artist: ") or item["artist"]
            new_album = input("New album: ") or item["album"]
            new_year = input("New year: ") or item["year"]

            #Updates the item in the library list
            item.update({"title": new_title, "artist": new_artist, "album": new_album, "year": new_year})
            print("Item updated successfully!")
            return

    
    print("That song is not in your library.")


        
#This is the main function that is ran first and has most of the user interface
def main():

    
    #This is my library set that all of the songs and artists are put into are removed from
    library = [] #Uses a list to be able to support indexing

    print('Welcome to your personal library for music!')

    #This is a while true loop that keeps running until the user wants to exit
    while True:
        option = input('\nWhat would you like to do?\n1. Add music\n2. Remove music\n3. Search for music\n4. Display all music\n5. Update music details\n6. Exit\n\nYour choice: ')
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
            update_item(library)

        elif option == '6':
            print('Thankyou for using your personal library! :)')
            break
        
        else:
            print('That is not an option')

#This is the start to the program as it calls the main function that holds the user interface
main()