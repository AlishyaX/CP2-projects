#This is the Pet class that handles the pet actions/level ups/status and also the way to save and load the pets data to the csv file
class Pet:
    def __init__(self, name, species, age):
        # These are the attributes of the pet that are already set once the pet is created
        self.name = name.strip() 
        self.species = species.strip()
        self.age = max(0, age) 
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.level = 1
        self.skills = []

    # The function that handles feeding the pet
    def feed(self, food_type):
        #These save the food types in a dictionary with the changed in hunger and happiness
        valid_food = {"basic food": (-10, 5), "treat": (-5, 10), "healthy snack": (-15, 10)}
        
        if food_type in valid_food:
            hunger_change, happiness_change = valid_food[food_type]
            self.hunger = max(0, self.hunger + hunger_change)
            self.happiness += happiness_change
        else:
            print("That is not an option. Please choose a valid option.")

    #This function handles the pet playing
    def play(self):
        if self.energy < 15:
            #Doesn't give the pet happiness if it is too tired to play
            print(f"Warning!{self.name} is too tired to play!")
        else:
            self.happiness += 15
            self.energy = max(0, self.energy - 15)
            self.hunger += 10

    #This function handles the pet sleeping
    def sleep(self):
        self.energy = min(100, self.energy + 30)  # Energy max capped at 100
        self.hunger += 5

    #This function handles the pet healing
    def heal(self, method):
        #These save the healing methods with the changes in health and happiness
        valid_methods = {"medicine": (20, -5), "rest": (10, 10)}

        #This makes sure the method works before actualy giving the health and happiness
        if method in valid_methods:
            health_change, happiness_change = valid_methods[method]
            self.health = min(100, self.health + health_change)
            self.happiness += happiness_change
        #Displays to the user if they made a mistake
        else:
            print("That is not an option. Please choose 'medicine' or 'rest'.")

    #This function handles the pet leveling up and unlocking new skills
    def level_up(self):
        #The pet levels up if its happiness and health are both above 80
        if self.happiness >= 80 and self.health >= 80:
            self.level += 1

            # The pet gets these skills once they level up
            skill_level_up = {
                2: "Basic Tricks (Sit, Roll Over)",
                3: "Advanced Tricks (Jump, Spin)",
                4: "Agility Training (Fast Running)",
                5: "Companionship Boost (Stronger Bond)",
                6: "Problem Solving (Find Objects)",
                7: "Guard Instincts (Protect Owner)",
                8: "Expert Communication (Understand Commands)",
                9: "Elite Agility (Dodging, Climbing)",
                10: "Master Skills (Unique Abilities)"
            }

            #This unlocks the skill if the pets level is corresponding with the skills
            if self.level in skill_level_up:
                new_skill = skill_level_up[self.level]
                self.skills.append(new_skill)
                print(f"{self.name} leveled up! New skill unlocked: {new_skill}")

    #This function shows the status of the pet
    def check_status(self):
        return f"""
        Name: {self.name}
        Species: {self.species}
        Age: {self.age:.1f}
        Hunger: {max(0, self.hunger)}
        Happiness: {max(0, self.happiness)}
        Energy: {max(0, self.energy)}
        Health: {max(0, self.health)}
        Level: {self.level}
        Skills: {", ".join(self.skills) if self.skills else "None"}
        """


    #These next two functions help load and save the pets to the csv file

    def to_dict(self):
        #These make the attributes in the right format to be saved in the csv file
        return {
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "hunger": self.hunger,
            "happiness": self.happiness,
            "energy": self.energy,
            "health": self.health,
            "level": self.level,
            "skills": self.skills,
        }

    #'This is used in python to define a method that belongs to the class, rather than an instance of the class.'-copilot
    @classmethod
    #This part of the code I am not that strong with but I think I understand parts of it
    def from_dict(cls, data):
        #'This method creates a Pet instance from a dictionary.'
        try:
            pet = cls(data["name"], data["species"], float(data["age"]))
            pet.hunger = max(0, int(data["hunger"]))
            pet.happiness = max(0, int(data["happiness"]))
            pet.energy = max(0, int(data["energy"]))
            pet.health = max(0, int(data["health"]))
            pet.level = int(data["level"])
            pet.skills = data.get("skills", [])
            return pet
        #Error handling
        except (ValueError, KeyError) as e:
            print(f"Error loading pet from data: {e}")
            return None
