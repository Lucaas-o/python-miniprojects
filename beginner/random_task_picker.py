import random
import os
import json
import sys

class TaskManager:
    def __init__(self, filename="tasks.json"):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(script_dir, filename)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Ensure we always return a list
                    return data if isinstance(data, list) else []
            return []
        except json.JSONDecodeError:
            print("Error: Corrupted task file. Starting with empty task list.")
            return []
        except Exception as e:
            print(f"Error loading tasks: {str(e)}. Starting with empty task list.")
            return []

    def save_tasks(self):
        """Save tasks to file with error handling"""
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, indent=2)  # Pretty print with indent
            return True
        except Exception as e:
            print(f"Error saving tasks: {str(e)}")
            return False

    def add_task(self, task):
        """Add a new task with error handling"""
        try:
            if task and task.strip():
                if not hasattr(self.tasks, 'append'):  # Fix corrupted tasks
                    self.tasks = []
                self.tasks.append(task.strip())
                return self.save_tasks()
            return False
        except Exception as e:
            print(f"Error adding task: {str(e)}")
            return False

    def get_random_task(self):
        """Pick a random task with error handling"""
        try:
            return random.choice(self.tasks) if self.tasks else None
        except Exception as e:
            print(f"Error selecting random task: {str(e)}")
            return None

    def list_tasks(self):
        """Return all tasks"""
        try:
            return self.tasks if isinstance(self.tasks, list) else []
        except Exception as e:
            print(f"Error listing tasks: {str(e)}")
            return []

    def clear_tasks(self):
        """Clear all tasks"""
        try:
            self.tasks = []
            return self.save_tasks()
        except Exception as e:
            print(f"Error clearing tasks: {str(e)}")
            return False

def display_menu():
    """Display the main menu"""
    print("\n=== Task Manager ===")
    print("1. Add new task")
    print("2. Pick random task")
    print("3. List all tasks")
    print("4. Clear all tasks")
    print("5. Exit")

def main():
    try:
        task_manager = TaskManager()
        print(f"Tasks will be saved to: {task_manager.filename}")
        
        while True:
            display_menu()
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == '1':
                    task = input("Enter task: ").strip()
                    if task_manager.add_task(task):
                        print("Task added successfully!")
                    else:
                        print("Invalid task - cannot be empty!")
                        
                elif choice == '2':
                    task = task_manager.get_random_task()
                    if task:
                        print(f"\nSelected task: {task}")
                    else:
                        print("No tasks available!")
                        
                elif choice == '3':
                    tasks = task_manager.list_tasks()
                    if tasks:
                        print("\nCurrent tasks:")
                        for i, task in enumerate(tasks, 1):
                            print(f"{i}. {task}")
                    else:
                        print("No tasks available!")
                        
                elif choice == '4':
                    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
                    if confirm == 'y':
                        if task_manager.clear_tasks():
                            print("All tasks cleared!")
                        else:
                            print("Failed to clear tasks!")
                        
                elif choice == '5':
                    print("Goodbye!")
                    break
                    
                else:
                    print("Invalid choice! Please select 1-5.")
                    
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                
    except Exception as e:
        print(f"Fatal error initializing Task Manager: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()