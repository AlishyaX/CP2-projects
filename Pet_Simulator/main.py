#Alishya Xavier, Pet Simulator
from simulator import Simulator

def main_menu():
    simulator = Simulator()
    simulator.load_data()  # Load pets from CSV at start
    print('Welcome to the Pet Simulator!')
    print('You can create a pet, select a pet, and perform actions with it.')
    while True:
        print("\n\nWhat would you like to do?\n1. Create Pet\n2. Select Pet\n3. Pull Data from File\n4. Save and Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            simulator.create_pet()
        elif choice == "2":
            pet = simulator.select_pet()
            if pet:
                while True:
                    print("\n\nWhat would you like to do?\n1. Feed\n2. Play\n3. Sleep\n4. Heal\n5. Check Status\n6. Back")
                    action = input("Choose an action: ")
                    if action == "1":
                        food = input("Choose food type (basic food/treat/healthy snack): ")
                        pet.feed(food)
                        simulator.advance_time(2)
                        simulator.random_event(pet)
                        pet.level_up()
                    elif action == "2":
                        print(f"{pet.name} is playing...")
                        pet.play()
                        simulator.advance_time(3)
                        simulator.random_event(pet)
                        pet.level_up()
                    elif action == "3":
                        print(f"{pet.name} is sleeping...")
                        pet.sleep()
                        simulator.advance_time(6)
                        simulator.random_event(pet)
                        pet.level_up()
                    elif action == "4":
                        method = input("Choose healing method (medicine/rest): ")
                        pet.heal(method)
                        simulator.advance_time(4)
                    elif action == "5":
                        print(pet.check_status())
                    elif action == "6":
                        break
                    else:
                        print("That is not an option. Please try again...")
        elif choice == "3":
            print("Reloading pet data from CSV...")
            simulator.load_data()  # Reload pet data from CSV file
        elif choice == "4":
            simulator.save_data()  # Save all pets to CSV before exiting
            print("Thankyou for using the Pet Simulator!")
            break
        else:
            print("That is not an option. Please try again...")

if __name__ == "__main__":
    main_menu()
