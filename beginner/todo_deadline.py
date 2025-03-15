from datetime import datetime
import heapq

tasks = []

def add_task():
    task_name = input("Enter task name: ")
    deadline_str = input("Enter deadline (YYYY-MM-DD HH:MM): ")
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        heapq.heappush(tasks, (deadline, task_name))
        print("Task added successfully!\n")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD HH:MM\n")

def show_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    print("Tasks sorted by deadline:")
    for i, (deadline, task) in enumerate(sorted(tasks)):
        time_left = deadline - datetime.now()
        urgency = "(Urgent!)" if time_left.total_seconds() < 3600 else ""
        print(f"{i+1}. {task} - Due: {deadline} {urgency}")
    print()

def remove_task():
    show_tasks()
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = heapq.heappop(tasks)[1]
            print(f"Task '{removed_task}' removed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("To-Do List")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
