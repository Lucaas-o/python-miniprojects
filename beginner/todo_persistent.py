import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(BASE_DIR, "todo_list.txt")

def clear_screen():
    """Clear the terminal screen for better readability."""
    os.system("cls" if os.name == "nt" else "clear")

def load_tasks():
    """Load tasks from file."""
    try:
        with open(TODO_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TODO_FILE, "w") as file:
        file.writelines(f"{task}\n" for task in tasks)

def display_tasks(tasks):
    """Display current tasks clearly."""
    clear_screen()
    print("\n" + "="*30)
    print("📋  TO-DO LIST".center(30))
    print("="*30)

    if not tasks:
        print("✅ No tasks pending!\n")
    else:
        for i, task in enumerate(tasks, 1):
            print(f" {i}. {task}")
    
    print("\n" + "="*30)

def mark_task_done(tasks, task_num):
    """Mark a task as done if not already marked."""
    if 0 <= task_num < len(tasks):
        if not tasks[task_num].startswith("✅"):
            tasks[task_num] = f"✅ {tasks[task_num]}"
            save_tasks(tasks)
            print("✅ Task marked as done!")
        else:
            print("⚠️ Task is already marked as done!")
    else:
        print("⚠️ Invalid task number!")

def undo_task_done(tasks, task_num):
    """Undo a completed task."""
    if 0 <= task_num < len(tasks) and tasks[task_num].startswith("✅ "):
        tasks[task_num] = tasks[task_num][2:].strip()
        save_tasks(tasks)
        print("🔄 Task undone!")
    else:
        print("⚠️ Task is not marked as done or invalid number!")

def main():
    tasks = load_tasks()

    while True:
        display_tasks(tasks)
        print("\nOptions: [A]dd  [R]emove  [D]one  [U]ndo  [Q]uit")
        choice = input("Choose an action: ").strip().lower()

        if choice == "a":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("📝 Task added!")
            else:
                print("⚠️ Task cannot be empty!")
        elif choice == "r":
            try:
                task_num = int(input("Enter task number to remove: ")) - 1
                if 0 <= task_num < len(tasks):
                    removed_task = tasks.pop(task_num)
                    save_tasks(tasks)
                    print(f"🗑️ Removed task: {removed_task}")
                else:
                    print("⚠️ Invalid task number!")
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == "d":
            try:
                task_num = int(input("Enter task number to mark as done: ")) - 1
                mark_task_done(tasks, task_num)
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == "u":
            try:
                task_num = int(input("Enter task number to undo: ")) - 1
                undo_task_done(tasks, task_num)
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == "q":
            print("💾 Saving and exiting...")
            save_tasks(tasks)
            break
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
