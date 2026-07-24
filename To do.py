# Console-Based To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\n----- TO-DO LIST -----")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. [{status}] {task['task']}")
    print()

while True:
    print("===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task_name = input("Enter the task: ")
        tasks.append({"task": task_name, "completed": False})
        print("Task added successfully!\n")

    elif choice == "3":
        show_tasks()
        if tasks:
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed['task']}' removed successfully!\n")
            except (ValueError, IndexError):
                print("Invalid task number!\n")

    elif choice == "4":
        show_tasks()
        if tasks:
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!\n")
            except (ValueError, IndexError):
                print("Invalid task number!\n")

    elif choice == "5":
        print("Thank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.\n")
