#File handling

#This is the function that reads the file the user inputted for the relative path 
def read_file(file_relative_path):
    with open(file_relative_path, 'r') as file:
        content = file.read()
    #This returns the content variable to be used in the main()
    return content

#This is the function that writes on the file the user inputted for the realtive path
def write_file(file_relative_path, content):
    with open(file_relative_path, 'w') as file:
        #This writes on the file of the word count and when it was last updated
        file.write(content)