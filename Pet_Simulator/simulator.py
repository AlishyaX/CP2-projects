import random
from pet import Pet

class Simulator:
    def __init__(self):
        self.pets = {}

    def create_pet(self):
        name = input("Enter pet name: ")
        species = input("Enter pet species: ")
        age = int(input("Enter pet age: "))
        self.pets[name] = Pet(name, species, age)

    def select_pet(self):
        if not self.pets:
            print("No pets available.")
            return None
        print("Pets: ", ", ".join(self.pets.keys()))
        selected = input("Select a pet: ")
        return self.pets.get(selected)

    def random_event(self, pet):
        events = ["sick", "find_toy"]
        event = random.choice(events)
        if event == "sick":
            pet.health -= 10
            print(f"{pet.name} is sick!")
        elif event == "find_toy":
            pet.happiness += 10
            print(f"{pet.name} found a toy!")

    def advance_time(self, hours):
        self.time += hours
        print(f"Time advanced by {hours} hours. Current time: {self.time}")
