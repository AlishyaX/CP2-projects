
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
        self.skills = []

    def feed(self, food_type):
        if food_type == "basic food":
            self.hunger = max(0, self.hunger - 10)
            self.happiness += 5
        elif food_type == "treat":
            self.hunger = max(0, self.hunger - 5)
            self.happiness += 10
        elif food_type == "healthy snack":
            self.hunger = max(0, self.hunger - 15)
            self.health += 10

    def play(self):
        if self.energy - 15 < 0:
            print(f"Warning: {self.name} is too tired to play!")
        else:
            self.happiness += 15
            self.energy = max(0, self.energy - 15)
            self.hunger += 10

    def sleep(self):
        self.energy += 30
        self.hunger += 5

    def heal(self, method):
        if method == "medicine":
            self.health = min(100, self.health + 20)
            self.happiness -= 5
        elif method == "rest":
            self.health = min(100, self.health + 10)
            self.energy += 10

    def level_up(self):
        if self.happiness >= 80 and self.health >= 80:
            self.level += 1

            # Define skills based on level
            skill_tree = {
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

            # Check if the current level unlocks a skill
            if self.level in skill_tree:
                new_skill = skill_tree[self.level]
                self.skills.append(new_skill)
                print(f"{self.name} leveled up! New skill unlocked: {new_skill}")



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

    def to_dict(self):
        return self.__dict__

    def from_dict(cls, data):
        pet = cls(data["name"], data["species"], data["age"])
        pet.hunger = data["hunger"]
        pet.happiness = data["happiness"]
        pet.energy = data["energy"]
        pet.health = data["health"]
        pet.level = data["level"]
        pet.skills = data["skills"]
        return pet
