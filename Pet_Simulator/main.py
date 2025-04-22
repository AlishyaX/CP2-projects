#Alishya Xavier, Pet Simulator
#This gets the class simulator from the simulator file
from simulator import Simulator

#This function is the main menu of the pet imulator that handles all of the user inetrface
def main_menu():
    #Saves a variable as the simulator class
    simulator = Simulator()
    print('Welcome to the Pet Simulator!')
    print('You can create a pet, select a pet, and perform actions with it.')

    #Loops the users options until they choose to exit
    while True:
        print("\n\nWhat would you like to do?\n1. Create Pet\n2. Select Pet\n3. Pull Data from File\n4. Save and Exit")
        choice = input("Choose an option: ").strip()

        #To create a pet
        if choice == "1":
            simulator.create_pet()
        #To choose a pet to do actions with
        elif choice == "2":
            pet = simulator.select_pet()
            if pet:
                #Loops the actions until the user chooses to go back to the main menu
                while True:
                    print("\n\nWhat would you like to do?\n1. Feed\n2. Play\n3. Sleep\n4. Heal\n5. Check Status\n6. Back")
                    action = input("Choose an action: ").strip()

                    #To feed the pet
                    if action == "1":
                        food = input("Choose food type (basic food/treat/healthy snack): ").strip().lower()
                        if food in ["basic food", "treat", "healthy snack"]:
                            pet.feed(food)
                            simulator.advance_time(2)
                            simulator.random_event(pet)
                            pet.level_up()
                        else:
                            print("Invalid food choice. Please select from the given options.")

                    #To play with the pet
                    elif action == "2":
                        print(f"{pet.name} is playing...")
                        pet.play()
                        simulator.advance_time(3)
                        simulator.random_event(pet)
                        pet.level_up()

                    #To put the pet to sleep
                    elif action == "3":
                        print(f"{pet.name} is sleeping...")
                        pet.sleep()
                        simulator.advance_time(6)
                        simulator.random_event(pet)
                        pet.level_up()

                    #To heal the pet
                    elif action == "4":
                        method = input("Choose healing method (medicine/rest): ").strip().lower()
                        if method in ["medicine", "rest"]:
                            pet.heal(method)
                            simulator.advance_time(4)
                        else:
                            print("Invalid healing method. Please choose 'medicine' or 'rest'.")

                    #Displays the pets status to the user
                    elif action == "5":
                        print(pet.check_status())

                    #To go back to the main menu
                    elif action == "6":
                        break
                    
                    #Handles invalid inputs for the actions
                    else:
                        print("Invalid action. Please select a valid number.")

        #This gets the saved pets from the csv file and puts it into the simulator
        elif choice == "3":
            print("Reloading pet data from CSV...")
            simulator.load_data()  # Reload pet data from CSV file

        #This exits the program and saves the created pets to the csv file
        elif choice == "4":
            simulator.save_data()  # Save all pets to CSV before exiting
            print("Thank you for using the Pet Simulator!")
            break
        
        #Handles invalid inputs for the main menu
        else:
            print("Invalid option. Please enter a number from 1 to 4.")

main_menu()