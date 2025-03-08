import json
import os
from datetime import datetime

# File to store the to-do list
TODO_FILE = "todo_list.json"

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns:
        list: A list of tasks.
    """
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    Args:
        tasks (list): The list of tasks to save.
    """
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, due_date=None):
    """
    Add a new task to the to-do list.
    Args:
        title (str): The title of the task.
        due_date (str, optional): The due date of the task in YYYY-MM-DD format.
    """
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
        "due_date": due_date
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def view_tasks():
    """
    Display all tasks in the to-do list.
    """
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            due_date = f" (Due: {task['due_date']})" if task["due_date"] else ""
            print(f"{task['id']}. {task['title']} [{status}]{due_date}")

def mark_task_complete(task_id):
    """
    Mark a task as completed.
    Args:
        task_id (int): The ID of the task to mark as completed.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    """
    Delete a task from the to-do list.
    Args:
        task_id (int): The ID of the task to delete.
    """
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

def main():
    """
    Main function to run the to-do list program.
    """
    global tasks
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            title = input("Enter the task title: ")
            due_date = input("Enter the due date (YYYY-MM-DD, optional): ") or None
            add_task(title, due_date)
        elif choice == "3":
            task_id = int(input("Enter the task ID to mark as completed: "))
            mark_task_complete(task_id)
        elif choice == "4":
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()