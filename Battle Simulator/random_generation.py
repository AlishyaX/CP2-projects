from faker import Faker
import random

faker = Faker()

# Function to generate a backstory with name, birthday, country, and job
def generate_backstory(name):
    birthday = faker.date_of_birth(minimum_age=18, maximum_age=100)  # Random birthday
    country = faker.country()  # Random country
    job = faker.job()  # Random job
    
    # Combine details into a cohesive backstory
    backstory = f"{name} was born on {birthday} in {country}, currently working as a {job}."
    return backstory

# Function to generate a complete random character
def generate_character():
    name = faker.name()  # Generate the character's name
    return {
        'name': name,
        'backstory': generate_backstory(name),  # Use the name in the backstory
        'strength': random.randint(5, 15),  # Random stats
        'defense': random.randint(5, 15),
        'speed': random.randint(5, 15),
        'health': random.randint(20, 100),
        'xp': 0,  # Experience points
        'level': 1  # Initial level
    }

