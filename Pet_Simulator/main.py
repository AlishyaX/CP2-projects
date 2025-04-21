#Alishya Xavier, Pet Simulator
from simulator import Simulator

def main_menu():
    simulator = Simulator()
    while True:
        print("1. Create Pet\n2. Select Pet\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            simulator.create_pet()
        elif choice == "2":
            pet = simulator.select_pet()
            if pet:
                while True:
                    print("1. Feed\n2. Play\n3. Sleep\n4. Heal\n5. Check Status\n6. Back")
                    action = input("Choose an action: ")
                    if action == "1":
                        food = input("Choose food type (basic food/deluxe food/healthy snack/treat): ")
                        pet.feed(food)
                        simulator.random_event(pet)
                        simulator.time_advance(pet)
                    elif action == "2":
                        pet.play()
                        simulator.random_event(pet)
                        simulator.time_advance(pet)
                    elif action == "3":
                        pet.sleep()
                        simulator.random_event(pet)
                        simulator.time_advance(pet)
                    elif action == "4":
                        method = input("Choose a healing method (medicine/rest/healthy food): ")
                        pet.heal(method)
                        print(f"{pet.name} feels better!")
                    elif action == "5":
                        print(pet.check_status())
                    elif action == "6":
                        break
        elif choice == "3":
            print("Thankyou for using the pet simulator!")
            break

main_menu()
