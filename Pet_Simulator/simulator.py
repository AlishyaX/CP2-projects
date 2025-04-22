#These are what are needed to run the code of the simulator
import os
import csv
#Gets the pet class from the pet file
from pet import Pet
import random

#This class runs certain parts of the game for example the random events, creating pet, selecting pet, loading and saving data, and advancing time
class Simulator:
    def __init__(self):
        #These are the attributes needed throughout the class
        self.pets = {}
        self.time = 0
        self.hours = 8
        self.period = "AM"
        self.filename = os.path.join(os.path.dirname(__file__), "pets.csv")  # Ensure it's stored in the same folder

    
    def random_event(self, pet):
        #These are random events that pop up and effect the pet 
        events = ["sick", "find_toy", "injured", "made a friend", "lost_toy", "got bitten by a bug"]
        #Randomly choosing an event
        event = random.choice(events)

        #Depending on each event the pet looses or gains health and happiness
        if event == "sick":
            pet.health = max(0, pet.health - 20)
            pet.happiness = max(0, pet.happiness - 10)
            print(f"{pet.name} is sick! Health decreased.")
        elif event == "find_toy":
            pet.happiness += 10
            print(f"{pet.name} found a toy! Happiness increased.")
        elif event == "injured":
            pet.health = max(0, pet.health - 15)
            pet.happiness = max(0, pet.happiness - 5)
            print(f"{pet.name} got injured! Health decreased.")
        elif event == "made a friend":
            pet.happiness += 20
            print(f"{pet.name} made a new friend! Happiness increased.")
        elif event == "lost_toy":
            pet.happiness = max(0, pet.happiness - 15)
            print(f"{pet.name} lost a toy! Happiness decreased.")
        elif event == "got bitten by a bug":
            pet.health = max(0, pet.health - 10)
            pet.happiness = max(0, pet.happiness - 5)
            print(f"{pet.name} got bitten by a bug! Health decreased.")

    #This function loads the pets from the csv file into the simulator
    def load_data(self):
        #This makes sure the file exists
        if not os.path.exists(self.filename):
            print("No saved data found.")
            return

        #This reads the info inside of the file and adds it to the simulator
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name, species, age, hunger, happiness, energy, health, level, skills = row
                pet = Pet(name, species, float(age))
                pet.hunger = max(0, int(hunger))
                pet.happiness = max(0, int(happiness))
                pet.energy = max(0, int(energy))
                pet.health = max(0, int(health))
                pet.level = int(level)
                pet.skills = skills.split(",") if skills else []
                self.pets[name] = pet

    #This function saves the pets to the csv file making sure that the new and old pets are saved to the file
    def save_data(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "species", "age", "hunger", "happiness", "energy", "health", "level", "skills"])
            for pet in self.pets.values():
                writer.writerow([
                    pet.name, pet.species, pet.age, pet.hunger, pet.happiness,
                    pet.energy, pet.health, pet.level, ",".join(pet.skills)
                ])

        print(f"Your pets have been saved")

    #This function creates a pet 
    def create_pet(self):
        #It makes usre that what the user types in is the valid input that it wants
        name = input("Enter pet name: ").strip()
        species = input("Enter pet species: ").strip()

        #They can't let it be empty
        if not name or not species:
            print("Pet name and species cannot be empty.")
            return

        #Makes sure all Input Validation and Error handling has been taken care of
        while True:
            try:
                age = float(input("Enter pet age: ").strip())  # Validate input
                if age < 0:
                    print("Age cannot be negative. Please enter a valid number.")
                else:
                    break  # Valid input, exit loop
            except ValueError:
                print("Invalid input! Please enter a number for the pet's age.")

        #The new pet has been created and added to the simulator
        self.pets[name] = Pet(name, species, age)
        print(f"{name} has been created!")

    #This function allows the user to select a pet from the list of pets in the simulator
    def select_pet(self):
        #If there are no pets in the simulator
        if not self.pets:
            print("No pets available.")
            return None

        #Displays all of the pets and allows the user to select one of them
        while True:
            print("Available pets:", ", ".join(self.pets.keys()))
            selected = input("Select a pet: ").strip()

            #Makes sure that the users input is valid
            if selected in self.pets:
                return self.pets[selected]  # Return the selected pet if valid
            else:
                print("That is not an option. Please choose a pet from the list.")

    #This function allows the user to advance time in the simulator
    def advance_time(self, hours):
        #Makes sure that the time has to be positive
        if hours <= 0:
            print("Time must be a positive number.")
            return

        #Makes sure format is correct
        self.hours += hours

        #Also made it so that after every 12 hours it changes from AM to PM 
        if self.hours >= 12:
            self.hours -= 12
            self.period = "PM" if self.period == "AM" else "AM"

        if self.hours == 0:
            self.hours = 12

        #Changes the pets energy due to AM or PM in the day
        for pet in self.pets.values():
            if self.period == "AM":
                pet.energy = min(100, pet.energy + 5)  
            else:
                pet.energy = max(0, pet.energy - 5) 

            #This makes sure that the pets hunger and happiness change over time
            pet.age += hours / 24 
            pet.health = max(0, pet.health - max(0, (pet.hunger - pet.happiness) * 0.1))

        #Displays to the user the time that passed doing that action and the current time
        print(f"Time advanced by {hours} hours. Current time: {self.hours} {self.period}")