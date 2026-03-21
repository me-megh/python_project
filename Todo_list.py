# A list to store the tasks
tasks = []

def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Remove a Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def add_task():
    task = input("Enter a task to add: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added successfully!')
    else:
        print("Task cannot be empty!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task["task"]}" removed successfully!')
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f'Task "{tasks[task_num - 1]["task"]}" marked as completed!')
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Start the program
if __name__ == "__main__":
    main()