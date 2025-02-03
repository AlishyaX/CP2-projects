#Alishya xavier, Notes about Dictionaries

car = {
    "make": ["Ford","Chevy", "Toyota"],
    "model": "Escape xlt",
    "year": 2008,
    "color": "Red",
    "name": "Freya"
}

#print(car["make"][2])

student = {
    "first":{
        1: "Vincent",
        2: "Cecily",
        3: "Alishya"
    },
    "sixth": {
        1: "Nicole",
        "color": "Luke",
        3: "Gavin",
        4: "Jackson"
    }
}

#print(student["sixth"]["color"])

#To print keys
print(car.keys())

#To print values
print(car.values())

 
print(car.get("make"))

#To pop item off list
student.pop("first")


#lets you add something
#If it already exists then it will print it from there
print(car)
car.setdefault("drive, 2")
print(car)

#This switches the value
car.update("color": "pink")
print(car)