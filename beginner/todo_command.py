import sys
import os
from clear_screen import clear_screen

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(BASE_DIR, "tasks.txt")

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the tasks.txt file."""
        try:
            with open(TODO_FILE, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the tasks.txt file."""
        with open(TODO_FILE, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {task}")

    def remove_task(self, task_id):
        """Remove a task by its ID."""
        try:
            task_id = int(task_id)
            if 0 <= task_id < len(self.tasks):
                removed_task = self.tasks.pop(task_id)
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
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")

    def handle_command(self, command):
        """Handle user commands."""
        parts = command.split()
        if not parts:
            return

        cmd = parts[0].lower()
        if cmd == "/add":
            if len(parts) > 1:
                self.add_task(" ".join(parts[1:]))
            else:
                print("Usage: /add <task>")
        elif cmd == "/remove":
            if len(parts) > 1:
                self.remove_task(parts[1])
            else:
                print("Usage: /remove <task_id>")
        elif cmd == "/list":
            self.list_tasks()
        elif cmd == "/exit":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid command. Available commands: /add, /remove, /list, /exit")

def main():
    """Main function to run the to-do list application."""
    todo_list = ToDoList()
    print("To-Do List Application. Type /exit to quit.")
    while True:
        command = input("> ")
        clear_screen()
        todo_list.handle_command(command)

if __name__ == "__main__":
    main()