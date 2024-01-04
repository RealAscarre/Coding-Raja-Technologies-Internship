# Made By Ascarre
import json
import os
from datetime import datetime

# Check if the file exists, create an empty list if it doesn't
if not os.path.exists('tasks.json'):
    with open('tasks.json', 'w') as file:
        json.dump([None], file)
    print("\nStorage file created successfully.")
else:
    print("\nStorage file already exists.")

# Load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [None]

# Save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Validate priority input
def validate_priority():
    while True:
        priority = input("Enter priority (high, medium, low): ").lower()
        if priority in ['high', 'medium', 'low']:
            return priority
        else:
            print("Invalid priority! Please enter either 'high', 'medium', or 'low'.")

# Validate due date input
def validate_due_date():
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
            year, month, day = map(int, due_date.split('-'))
            if year < datetime.now().year or not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError
            return due_date
        except ValueError:
            print("Invalid date format or date out of range! Please enter the date in YYYY-MM-DD format.")


# Add a task to the list
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = validate_priority()
    due_date = validate_due_date()

    new_task = {
        'name': task_name,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("\nTask added successfully!")

# Remove a task from the list
def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: "))
    if 1 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("\nTask removed successfully!")
    else:
        print("\nInvalid task index.")

# Mark a task as completed
def complete_task(tasks):
    task_index = int(input("Enter the index of the task completed: "))
    if 1 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print("\nTask marked as completed!")
    else:
        print("\nInvalid task index.")

# Display tasks in a list
def display_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks[1:], start=1):
        if task is not None:
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")
        else:
            print(f"{i}.")
    print()

# Clear all tasks from the list
def clear_tasks(tasks):
    while True:
        confirm = input("This action will clear all tasks. Are you sure? (yes/no) or (y/n): ").lower()
        if confirm == 'yes' or confirm == 'y':
            tasks.clear()
            save_tasks(tasks)
            print("\nAll tasks cleared successfully!")
            break
        elif confirm == 'no' or confirm == 'n':
            print("\nTask clearing cancelled.")
            break
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n===== Main Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            clear_tasks(tasks)
        elif choice == '6':
            print("\nExiting program!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
  
# Made By Ascarre
