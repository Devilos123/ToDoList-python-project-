import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    """Add a task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(task_number):
    """Remove a task from the list."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
            print("Task added.")
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
                print("Task removed.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
