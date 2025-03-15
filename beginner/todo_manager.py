import os
import sys
import json
import heapq
from datetime import datetime
from typing import Dict, List
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE_JSON = os.path.join(BASE_DIR, "tasks.json")


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
                    self.tasks = json.load(file)
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
        self.tasks.setdefault(category, []).append({"task": task, "done": False, "created": str(datetime.now())})

    def list_tasks(self, category=None):
        """List tasks by category."""
        if not self.tasks:
            return print("No tasks found.")
        for cat in ([category] if category else self.tasks.keys()):
            if cat in self.tasks:
                print(f"\n{cat}:")
                for i, t in enumerate(self.tasks[cat], 1):
                    status = "[✔]" if t["done"] else "[ ]"
                    print(f"  {i}. {status} {t['task']} (Created: {t['created'][:19]})")

    def mark_done(self, category, index):
        """Mark a task as done."""
        if category in self.tasks and 0 < index <= len(self.tasks[category]):
            self.tasks[category][index - 1]["done"] = True

    def remove_task(self, category, index):
        """Remove a task."""
        if category in self.tasks and 0 < index <= len(self.tasks[category]):
            del self.tasks[category][index - 1]
            if not self.tasks[category]: del self.tasks[category]


class DeadlineToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name: str, deadline_str: str):
        """Add a task with a deadline."""
        try:
            heapq.heappush(self.tasks, (datetime.strptime(deadline_str, "%Y-%m-%d %H:%M"), task_name))
            print("Task added successfully!")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD HH:MM.")

    def show_tasks(self):
        """Show tasks sorted by deadline."""
        if not self.tasks:
            return print("No tasks available.")
        for i, (deadline, task) in enumerate(sorted(self.tasks)):
            urgency = "(Urgent!)" if (deadline - datetime.now()).total_seconds() < 3600 else ""
            print(f"{i+1}. {task} - Due: {deadline} {urgency}")

    def remove_task(self, index: int):
        """Remove a task by index."""
        if 0 <= index < len(self.tasks):
            print(f"Task '{heapq.heappop(self.tasks)[1]}' removed!")
        else:
            print("Invalid task number.")


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """Main function to handle user commands."""
    todo = ToDoList()
    deadline_todo = DeadlineToDo()

    commands = {
        "/add": lambda: todo.add_task(input("Enter category: "), input("Enter task: ")),
        "/list": lambda: todo.list_tasks(input("Enter category (press Enter for all): ") or None),
        "/done": lambda: todo.mark_done(input("Enter category: "), int(input("Enter task number: "))),
        "/remove": lambda: todo.remove_task(input("Enter category: "), int(input("Enter task number: "))),
        "/deadline_add": lambda: deadline_todo.add_task(input("Task name: "), input("Deadline (YYYY-MM-DD HH:MM): ")),
        "/deadline_list": deadline_todo.show_tasks,
        "/deadline_remove": lambda: deadline_todo.remove_task(int(input("Enter task number: "))),
        "/exit": lambda: sys.exit(0)
    }

    print("To-Do List Application. Type /exit to quit.")
    while True:
        command = input("> ").strip()
        clear_screen()
        commands.get(command, lambda: print("Invalid command."))()


if __name__ == "__main__":
    main()
