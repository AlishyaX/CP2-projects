#Alishya Xavier, To do list

#This helps us be able to check if the file exists before reading it and prevents errors if it doesn't
import os

#This is uppercase because it is a constant throughout the whole code
TODO_FILE = "To do list/todo_list.txt"

#This function is what each function uses that loads the tasks from the file to a list 
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

#This function saves the tasks back to the file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

#This function displays all of the tasks in that file
def display_tasks(tasks):
    if not tasks:
        #If there is nothing there then it will print nothing is there
        print("\nNo tasks found.\n")
        return
    #If there are things in the file then it will print them(with the index to order them with numbers)
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print()

#This function adds a new task to the list at the end by appending it 
def add_task(tasks):
    task = input("Enter a new task: ")
    #Made the brackets look like a check box
    tasks.append(f"[ ] {task}")
    save_tasks(tasks)
    print("Your task has been added to your To Do List.")

#This function marks the task as complete
def mark_task_complete(tasks):
    if not tasks:  # Directly checks if the list is empty
        print("\nNo tasks found.\n")
        return  # Exit the function if there are no tasks
    
    display_tasks(tasks)
    try:
        #Asks which task they want to mark complete
        task_num = int(input("Enter task number to mark as complete: ")) - 1 #Subtracts one because python's index starts at 0
        if 0 <= task_num < len(tasks):
            #Checks to see if task is already completed
            if "[✓]" in tasks[task_num]:
                print("\nYou have already marked that task as complete.")
            else:
                #If its not already checked then it will replace the empty "check box" with a checked one
                tasks[task_num] = tasks[task_num].replace("[ ]", "[✓]", 1) #Used google text for the check mark
                save_tasks(tasks)
                print("This task is now marked as complete.")
        else:
            print("That is not one of the task numbers.")
    except ValueError:
        print("Please enter a proper number for the task. ")

#This function is called when the user wants to delete a task
def delete_task(tasks):
    if not tasks:  # Directly checks if the list is empty
        print("\nNo tasks found.\n")
        return  # Exit the function if there are no tasks
    
    display_tasks(tasks)

    try:
        #This finds the task number(with the right index) and deletes it. 
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            #This saves the new changes into the todo_list.txt
            save_tasks(tasks)
            print("Your task has been deleted.")
        else:
            print("That is not one of the task numbers.")
    except ValueError:
        print("Please enter a proper number for the task. ")

#This is the main function that handles the user-interface
def main():
    #This loads the to do list from the todo_list.txt into a list
    tasks = load_tasks()
    #This keeps the question repeating until they type in 5
    while True:
        #This gathers their choice of what they want to do and implememnts it
        print("\nWhat would you like to do to your To Do List?\n")
        print("1. View your tasks")
        print("2. Add a task")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        #uses the users input and calls the function needed
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thankyou for using your To Do List!\n Remember that all of your tasks will save forever until you delete it.")
            break
        else:
            print("That is not an option. Try again...")

#This is the start of the whole program that calls the main function
main()