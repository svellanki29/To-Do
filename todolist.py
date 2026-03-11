import json
import os

# The filename where tasks will be stored
DATA_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks_list):
    """Saves the current tasks list to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks_list, file, indent=4)

# Initialize the list by loading existing data
tasks = load_tasks()

while True:
    print("\n--- TO-DO LIST (Auto-Saving) ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        save_tasks(tasks)  # Save after adding
        print("Task added and saved!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)  # Save after removing
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye 👋")
        break
