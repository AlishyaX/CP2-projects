import csv

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.level = 1
 
    def save(self):
        info = {
            "Name": self.name,
            "Species": self.species,
            "Age": self.age,
            "Hunger": self.hunger,
            "Happiness": self.happiness,
            "Energy": self.energy,
            "Health": self.health,
            "Level": self.level
        }

    def feed(self, food_type):
        if food_type == "basic food":
            self.hunger -= 10
            self.happiness += 5
        elif food_type == "treat":
            self.hunger -= 5
            self.happiness += 10
        elif food_type == "deluxe food":
            self.hunger -= 15
            self.happiness += 15
        elif food_type == "healthy snack":
            self.hunger -= 8
            self.happiness += 8
        else:   
            print("That is not an option!")
            return
        self.hunger = max(0, self.hunger)

    def play(self):
        self.happiness += 10
        self.energy -= 15
        self.hunger += 10

    def sleep(self):
        print(f"{self.name} is sleeping...")
        print(f"{self.name} is now well-rested!")
        self.happiness += 5
        self.energy += 20
        self.hunger += 5

    def check_status(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nHunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}\nHealth: {self.health}\nLevel: {self.level}"

    def heal(self, method):
        if method == "medicine":
            self.health += 20
            self.happiness -= 5  # Pets might dislike taking medicine!
        elif method == "rest":
            self.health += 10
            self.energy += 10
        elif method == "healthy food":
            self.health += 15
            self.hunger -= 10
        
        # Ensure health doesn't exceed 100
        self.health = min(100, self.health)
