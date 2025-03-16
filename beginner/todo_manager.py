import os
import sys
import json
from datetime import datetime
from typing import Dict, List
from pathlib import Path

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE_JSON = os.path.join(BASE_DIR, "tasks.json")
TODO_FILE_TXT = os.path.join(BASE_DIR, "tasks.txt")

# ToDoList class for categorized tasks
class ToDoList:
    def __init__(self, filename=TODO_FILE_JSON):
        self.filename = filename
        self.tasks: Dict[str, List[dict]] = {}
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if Path(self.filename).exists():
            try:
                with open(self.filename, "r") as file:
                    loaded_data = json.load(file)
                    if isinstance(loaded_data, dict):
                        self.tasks = loaded_data
                    else:
                        print("Error: Invalid data format in tasks.json. Starting fresh.")
                        self.tasks = {}
            except json.JSONDecodeError:
                print("Error: Corrupted file. Starting fresh.")
                self.tasks = {}

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, category: str, task: str):
        """Add a new task to a category."""
        category, task = category.strip(), task.strip()
        if not category:
            print("Category cannot be empty.")
            return
        if not task:
            print("Task cannot be empty.")
            return
        self.tasks.setdefault(category, []).append({
            "task": task,
            "done": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_tasks()
        print(f"Task '{task}' added to category '{category}'.")

    def list_tasks(self, category=None):
        """List tasks by category."""
        if not self.tasks:
            return print("No tasks found.")
        if category and category not in self.tasks:
            print(f"Category '{category}' not found.")
        else:
            for cat in ([category] if category else self.tasks.keys()):
                if cat in self.tasks:
                    print(f"\n{cat}:")
                    for i, t in enumerate(self.tasks[cat], 1):
                        status = "[✔]" if t["done"] else "[ ]"
                        print(f"  {i}. {status} {t['task']} (Created: {t['created']})")

    def mark_done(self, category: str, index: int):
        """Mark a task as done."""
        if category not in self.tasks:
            print(f"Category '{category}' not found.")
        elif not (1 <= index <= len(self.tasks[category])):
            print(f"Invalid task number {index} for category '{category}'.")
        else:
            self.tasks[category][index - 1]["done"] = True
            self.save_tasks()
            print(f"Task {index} in category '{category}' marked as done.")

    def remove_task(self, category: str, index: int):
        """Remove a task."""
        if category not in self.tasks:
            print(f"Category '{category}' not found.")
        elif not (1 <= index <= len(self.tasks[category])):
            print(f"Invalid task number {index} for category '{category}'.")
        else:
            removed_task = self.tasks[category].pop(index - 1)
            if not self.tasks[category]:
                del self.tasks[category]
            self.save_tasks()
            print(f"Task '{removed_task['task']}' removed from category '{category}'.")

# DeadlineToDo class for tasks with deadlines
class DeadlineToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name: str, deadline_str: str):
        """Add a task with a deadline."""
        task_name = task_name.strip()
        if not task_name:
            print("Task name cannot be empty.")
            return
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            self.tasks.append((deadline, task_name))
            print(f"Task '{task_name}' with deadline {deadline_str} added successfully!")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD HH:MM.")

    def show_tasks(self):
        """Show tasks sorted by deadline."""
        if not self.tasks:
            return print("No tasks available.")
        sorted_tasks = sorted(self.tasks)
        for i, (deadline, task) in enumerate(sorted_tasks, 1):
            urgency = "(Urgent!)" if (deadline - datetime.now()).total_seconds() < 3600 else ""
            print(f"{i}. {task} - Due: {deadline.strftime('%Y-%m-%d %H:%M')} {urgency}")

    def remove_task(self, index_str: str):
        """Remove a task by index."""
        try:
            index = int(index_str)
            if 1 <= index <= len(self.tasks):
                sorted_tasks = sorted(self.tasks)
                task_to_remove = sorted_tasks[index - 1]
                self.tasks.remove(task_to_remove)
                print(f"Task '{task_to_remove[1]}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

# SimpleToDo class for basic tasks
class SimpleToDo:
    def __init__(self, filename=TODO_FILE_TXT):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a text file."""
        try:
            with open(self.filename, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to a text file."""
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task: str):
        """Add a new task to the list."""
        task = task.strip()
        if not task:
            print("Task cannot be empty.")
            return
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {task}")

    def remove_task(self, task_id: str):
        """Remove a task by its ID."""
        try:
            task_id = int(task_id)
            if 1 <= task_id <= len(self.tasks):
                removed_task = self.tasks.pop(task_id - 1)
                self.save_tasks()
                print(f"Task removed: {removed_task}")
            else:
                print("Invalid task ID.")
        except ValueError:
            print("Please enter a valid task ID.")

    def list_tasks(self):
        """List all tasks with their IDs."""
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}: {task}")

# Utility function to clear the screen
def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

# Main application logic
def main():
    """Main function to handle user commands."""
    todo = ToDoList()
    deadline_todo = DeadlineToDo()
    simple_todo = SimpleToDo()

    # Command functions
    def add_task():
        category = input("Enter category: ")
        task = input("Enter task: ")
        todo.add_task(category, task)

    def list_tasks():
        category = input("Enter category (press Enter for all): ") or None
        todo.list_tasks(category)

    def mark_done():
        category = input("Enter category: ")
        task_num_str = input("Enter task number: ")
        try:
            task_num = int(task_num_str)
            todo.mark_done(category, task_num)
        except ValueError:
            print("Please enter a valid task number.")

    def remove_task():
        category = input("Enter category: ")
        task_num_str = input("Enter task number: ")
        try:
            task_num = int(task_num_str)
            todo.remove_task(category, task_num)
        except ValueError:
            print("Please enter a valid task number.")

    def deadline_add():
        task_name = input("Task name: ")
        deadline_str = input("Deadline (YYYY-MM-DD HH:MM): ")
        deadline_todo.add_task(task_name, deadline_str)

    def deadline_list():
        deadline_todo.show_tasks()

    def deadline_remove():
        task_num_str = input("Enter task number: ")
        deadline_todo.remove_task(task_num_str)

    def simple_add():
        task = input("Enter task: ")
        simple_todo.add_task(task)

    def simple_list():
        simple_todo.list_tasks()

    def simple_remove():
        task_id_str = input("Enter task number: ")
        simple_todo.remove_task(task_id_str)

    # Help command definitions
    help_commands = [
        ("/add", "Add a new task to a category"),
        ("/list", "List tasks by category or all tasks"),
        ("/done", "Mark a task as done"),
        ("/remove", "Remove a task"),
        ("/deadline_add", "Add a task with a deadline"),
        ("/deadline_list", "Show tasks with deadlines"),
        ("/deadline_remove", "Remove a task with a deadline"),
        ("/simple_add", "Add a simple task"),
        ("/simple_list", "List simple tasks"),
        ("/simple_remove", "Remove a simple task"),
        ("/help", "Show this help message"),
        ("/exit", "Exit the application"),
    ]

    def show_help():
        print("Available commands:")
        for cmd, desc in help_commands:
            print(f"  {cmd:<16} - {desc}")

    # Command dictionary
    commands = {
        "/add": add_task,
        "/list": list_tasks,
        "/done": mark_done,
        "/remove": remove_task,
        "/deadline_add": deadline_add,
        "/deadline_list": deadline_list,
        "/deadline_remove": deadline_remove,
        "/simple_add": simple_add,
        "/simple_list": simple_list,
        "/simple_remove": simple_remove,
        "/help": show_help,
        "/exit": lambda: sys.exit(0)
    }

    print("To-Do List Application. Type /exit to quit.")
    while True:
        command = input("> ").strip().lower()  # Case-insensitive command input
        clear_screen()
        cmd_func = commands.get(command, lambda: print("Invalid command."))
        cmd_func()

if __name__ == "__main__":
    main()