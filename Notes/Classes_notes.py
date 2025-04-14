#Alishya Xavier, Classes Notes

#1. What is a class in python?
# A blue print for an object
# Objects can have variables or methods inside them

class subject:
    def __init__(self, content, period, teacher,):
        self.content = content
        self.period = period
        self.teacher = teacher

    def __str__(self):
        return f'name: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}'
    


first = subject("World Civilizations", 1, "Mr. M", 210)
second = subject("P.E.", 2, "Mr. Buck", 270)

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f'{self.name} is a {self.species} and they have {self.hp} HP and do {self.dmg} amount of damage in battle.'
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f'{self.name} attacked {opponent.name} for {self.dmg} damage and {opponent.name} now has {opponent.hp} HP.')
            if opponent.hp <= 0:
                print(f'{opponent.name} is knocked out. {self.name} wins!')
            else:
                self.hp -= opponent.dmg
                print(f'{self.name} attacked {opponent.name} for {self.dmg} damage and {opponent.name} now has {opponent.hp} HP.')

                if self.hp <=0:
                    print(f'{opponent.name} is knocked out. {self.name} wins!')

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("Slimy", "Ditto", 100, 70)
spiky = pokemon("Spiky", "Jolteon", 150, 100)

fluffy.battle(spiky)



print(first.content)

print(second.content)
#sentence = "The quick brown fox jumped over the lazy dog"

#print(sentence.upper())

#2. What is an object in python?
# an instance of a class

#3. How do python classes relate to python objects?
# Python classes relate to python objects as classes define the rules while the objects actually use the rules.

#4. How do you create a python class?
# You have to use the class keyword and then the name of your class
# You then have to indent it and then define the attributes and methods inside

#5. What are methods?
#A method is a function that exists for a specific class
#Every method has to take in self

#6. How do you create a python object?
# You use a class as the blue print and then use the class name with parenthesis to create the object 

#7. How to you call a method for an object?
# To call a method for an object you type in the objects name followed by the method name and parenthesis

#8. Why do we use python classes?
# We use python classes to make our code structured and reusable to be able to resemble real world problems.






















