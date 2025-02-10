#Alishya Xavier, Reading Notes Python
import csv
'''
#First way
with open("CP2-projects/Notes/text.txt", "r") as file:
    content = file.read()
    print(content[5:20])
'''
with open("CP2-projects/Notes/text.txt", "r") as file:
    content = file.read()
    print(content[5:20])
    
file = open("CP2-projects/Notes/text.txt", "r").read()

users = {}

with open("CP2-projects/Notes/user_info.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
        users.update({row[0]:row[1]})