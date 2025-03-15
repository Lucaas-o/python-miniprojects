import json
from typing import Dict, List
from pathlib import Path

class ToDoList:
    def __init__(self, filename: str = "tasks.json"):
        self.tasks: Dict[str, List[dict]] = {}
        self.filename = filename
        self.load_tasks()

    def add_task(self, category: str, task: str) -> bool:
        """Add a task to a category. Returns True if successful."""
        if not category or not task:
            print("Error: Category and task cannot be empty")
            return False
            
        category = category.strip()
        task = task.strip()
        
        if category not in self.tasks:
            self.tasks[category] = []
        self.tasks[category].append({"task": task, "done": False, "created": str(__import__('datetime').datetime.now())})
        return True

    def list_tasks(self, category: str = None) -> None:
        """List all tasks or tasks in a specific category."""
        if not self.tasks:
            print("No tasks found.")
            return

        categories = [category] if category else self.tasks.keys()
        for cat in categories:
            if cat not in self.tasks:
                print(f"No tasks in category '{cat}'")
                continue
            print(f"\n{cat}:")
            for idx, task in enumerate(self.tasks[cat], 1):
                status = "[✔]" if task["done"] else "[ ]"
                print(f"  {idx}. {status} {task['task']} (Created: {task['created'][:19]})")

    def mark_done(self, category: str, index: int) -> bool:
        """Mark a task as done. Returns True if successful."""
        if category not in self.tasks:
            print(f"Error: Category '{category}' not found")
            return False
        if not (0 < index <= len(self.tasks[category])):
            print(f"Error: Invalid task number {index}")
            return False
        self.tasks[category][index - 1]["done"] = True
        return True

    def remove_task(self, category: str, index: int) -> bool:
        """Remove a task. Returns True if successful."""
        if category not in self.tasks:
            print(f"Error: Category '{category}' not found")
            return False
        if not (0 < index <= len(self.tasks[category])):
            print(f"Error: Invalid task number {index}")
            return False
        del self.tasks[category][index - 1]
        if not self.tasks[category]:
            del self.tasks[category]
        return True

    def save_tasks(self) -> bool:
        """Save tasks to file. Returns True if successful."""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.tasks, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False

    def load_tasks(self) -> bool:
        """Load tasks from file. Returns True if successful."""
        try:
            if Path(self.filename).exists():
                with open(self.filename, "r") as file:
                    self.tasks = json.load(file)
            return True
        except json.JSONDecodeError:
            print(f"Error: Corrupted {self.filename} file. Starting with empty task list.")
            self.tasks = {}
            return False
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = {}
            return False

def main():
    todo = ToDoList()
    
    commands = {
        "1": ("Add task", lambda: todo.add_task(
            input("Enter category: "), 
            input("Enter task: ")
        )),
        "2": ("List tasks", lambda: todo.list_tasks(
            input("Enter category (press Enter for all): ") or None
        )),
        "3": ("Mark done", lambda: todo.mark_done(
            input("Enter category: "), 
            safe_int_input("Enter task number: ")
        )),
        "4": ("Remove task", lambda: todo.remove_task(
            input("Enter category: "), 
            safe_int_input("Enter task number: ")
        )),
        "5": ("Quit", lambda: "quit")
    }

    while True:
        print("\nOptions:")
        for key, (desc, _) in commands.items():
            print(f"{key}. {desc}")
        
        choice = input("Choose an option: ").strip()
        
        if choice in commands:
            result = commands[choice][1]()
            if result == "quit":
                todo.save_tasks()
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Try again.")

def safe_int_input(prompt: str) -> int:
    """Safely get integer input from user."""
    while True:
        try:
            value = input(prompt).strip()
            return int(value)
        except ValueError:
            print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()