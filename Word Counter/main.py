#Alishya Xavier, Word Counter

#These let this file use things from other files
import file_handling
import time_handling

#Main Function(User Interface)
def main():
    #This gets the relative path from the user
    file_relative_path = input("Enter the file's relative path: ")

    #This reads the files contents from the file_handling file
    content = file_handling.read_file(file_relative_path)

    #This calculates the word count 
    word_count = len(content.split())

    #This gets the time stamp from the time_handling file
    timestamp = time_handling.get_current_timestamp()

    #This is the information that puts all of the information gathered into a statement
    updated_content = f"{content}\n\nWord Count: {word_count}\nLast Updated: {timestamp}\n"
    
    #This writes the updated statement back into the file
    file_handling.write_file(file_relative_path, updated_content)
    
    print("The file has been updated.")


#This starts the whole program by running the main function
main()