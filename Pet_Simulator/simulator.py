import os
import csv
from pet import Pet
import random


class Simulator:
    def __init__(self):
        self.pets = {}
        self.time = 0
        self.hours = 8
        self.period = "AM"
        self.filename = os.path.join(os.path.dirname(__file__), "pets.csv")  # Ensure it's stored in the same folder

    
    def random_event(self, pet):
        """Triggers a random event affecting the pet."""
        events = ["sick", "find_toy", "injured", "made a friend", "lost_toy", "got bitten by a bug"]
        event = random.choice(events)

        if event == "sick":
            pet.health -= 20
            pet.happiness -= 10
            print(f"{pet.name} is sick! Health decreased.")
        elif event == "find_toy":
            pet.happiness += 10
            print(f"{pet.name} found a toy! Happiness increased.")
        elif event == "injured":
            pet.health -= 15
            pet.happiness -= 5
            print(f"{pet.name} got injured! Health decreased.")
        elif event == "made a friend":
            pet.happiness += 20
            print(f"{pet.name} made a new friend! Happiness increased.")
        elif event == "lost_toy":
            pet.happiness -= 15
            print(f"{pet.name} lost a toy! Happiness decreased.")
        elif event == "got bitten by a bug":
            pet.health -= 10
            pet.happiness -= 5
            print(f"{pet.name} got bitten by a bug! Health decreased.")

    def load_data(self):
        """Load pet data from the CSV file."""
        if not os.path.exists(self.filename):
            print("No saved data found.")
            return

        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name, species, age, hunger, happiness, energy, health, level, skills = row
                pet = Pet(name, species, float(age))
                pet.hunger = int(hunger)
                pet.happiness = int(happiness)
                pet.energy = int(energy)
                pet.health = int(health)
                pet.level = int(level)
                pet.skills = skills.split(",") if skills else []
                self.pets[name] = pet

    def save_data(self):
        """Save pet data to CSV, ensuring all pets (new and existing) are stored."""
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "species", "age", "hunger", "happiness", "energy", "health", "level", "skills"])
            for pet in self.pets.values():
                writer.writerow([
                    pet.name, pet.species, pet.age, pet.hunger, pet.happiness,
                    pet.energy, pet.health, pet.level, ",".join(pet.skills)
                ])

        print(f"Your pets have been saved")

    def create_pet(self):
        """Create a new pet and add it to the list."""
        name = input("Enter pet name: ")
        species = input("Enter pet species: ")
        age = float(input("Enter pet age: "))
        self.pets[name] = Pet(name, species, age)
        print(f"{name} has been created!")

    def select_pet(self):
        """Allow user to select a pet, validating user input."""
        if not self.pets:
            print("No pets available.")
            return None

        while True:
            print("Available pets:", ", ".join(self.pets.keys()))
            selected = input("Select a pet: ")

            if selected in self.pets:
                return self.pets[selected]  # Return the selected pet if valid
            else:
                print("Please choose a pet from the list.")

    

    def advance_time(self, hours):
        """Advances time while keeping AM/PM format and adjusting pet energy."""
        self.hours += hours

        # Adjust for time overflow (switch AM/PM every 12 hours)
        if self.hours >= 12:
            self.hours -= 12
            self.period = "PM" if self.period == "AM" else "AM"

        if self.hours == 0:
            self.hours = 12

        # Modify pet attributes based on time progression
        for pet in self.pets.values():
            if self.period == "AM":
                pet.energy += 5  # Pets gain energy in the morning
            else:
                pet.energy -= 5  # Pets lose energy in the evening

            pet.age += hours / 24  # Convert hours to days
            pet.health -= max(0, (pet.hunger - pet.happiness) * 0.1)

        print(f"Time advanced by {hours} hours. Current time: {self.hours} {self.period}")
