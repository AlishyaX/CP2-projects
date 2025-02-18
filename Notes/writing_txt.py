#Alishya Xavier
"""
r = to read file
w = to write on the file(replaces old content)
w+ = to read and write
a = append(adds info, doesn't delete)(creates file if doesn't exist)
x = create file
a+ = to append and read

"""
import csv
'''
with open("Notes/text.txt", "a" ) as file:
    file.write("random things and stuff")
'''

data = [
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
    {"username": "alishya", "color": "navy"},
]
with open("Notes/user_info.csv", "a", newline ="") as file:
    fieldnames = ["username" , "color"]
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(data)
    #writer.writerows([["sily_username", "Black"]],
    #["panda_hi", "pink"],["ally_xav", "blue"],
    #["happiness_love", "yellow"])
    
with open("Notes/user_info.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"user name: {row[0]} color : {row[1]}")

#Questions:
'''
--------------How do you find a file in a folder?-------------------
- In the file explorer

----------------In a python project how do you open a file?-------------
- you can open a file by using the open() function. You would use with before that to ensure that the file properly closes after even if an error happens. In the end you would write with open("The relitive path", "what you want to do") as file: ...

-------------What is the difference between writing, appending, and creation modes?-----------------------------
-Writing: to write on the file(replaces old content)

with open('example.txt', 'w') as file:
    file.write("Hello, World!")

-Appending:(adds info, doesn't delete)(creates file if doesn't exist)

with open('example.txt', 'a') as file:
    file.write("\nAppend this line.")

-Creation mode: It creates a new file but if the file alreay exists then it won't work.

try:
    with open('example.txt', 'x') as file:
        file.write("This is a new file.")
except FileExistsError:
    print("File already exists.")




'''