def add_task():
    with open("task.txt", "a") as file:
        while True:
            work = input("Enter your task: ")
            file.write(work + "\n")
            choice = input("Do you want to add more tasks (yes/no)? ").lower()
            if choice != "yes":
                break
def view_task():
    with open("task.txt", "r") as file:
        print(file.read())
def completed_task():
    complete = input("Enter the task you completed: ")
    with open("task.txt", "r") as file:
        tasks = file.readlines()
    with open("task.txt", "w") as file:
        for task in tasks:
            if task.strip() == complete:
                file.write("[Completed]" + task)
            else:
                file.write(task)
def delete_task():
    delete = input("Enter the task you want to remove: ")

    with open("task.txt", "r") as file:
        tasks = file.readlines()
    with open("task.txt", "w") as file:
        for task in tasks:
            clean_task= task.strip()
            if clean_task==delete or clean_task=="[Completed]" + delete:
# Skip the rest of this 
# loop iteration and go to the next iteration."
                continue
            else:
                file.write(task)
print("\n===== TO-DO LIST =====")
print("1. Add task")
print("2. View tasks")
print("3. Mark task as completed")
print("4. Delete task")
print("5. Exit")
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        completed_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

