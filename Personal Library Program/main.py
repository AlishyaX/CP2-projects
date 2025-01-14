#Alishya Xavier, Personal Library Program
items = {}

def add_item():
    print('Lets add a new song!')
    song_name = input('What is the title of the song: ')
    artists_name = input('What is the artists name: ')


def search_item():
    pass

def remove_item():
    pass

def display_library():
    for i in items:
        print(i)

def main():
    print('Welcome to your personal library for music!')
    while True:
        option = input('What would you like to do?\n1. Add an item\n2. Remove an item\n3. Search for an item\n4. Display the library\n5. Exit\n')
        if option == '1':
            add_item()
        elif option == '2':
            remove_item()
        elif option == '3':
            search_item()
        elif option == '4':
            display_library()
        elif option == '5':
            break
        else:
            print('That is not an option')
