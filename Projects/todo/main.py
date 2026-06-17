# TO DO LIST APP

tasks = []

# Add a task

def add_task(title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print(f"Added: {title}")

# View all tasks

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return

    for i, task in enumerate(tasks):
        status = "-DONE-" if task["done"] else "-PENDING-"
        print(f"{i + 1}. [{status}] {task['title']}")

# MARK A TASK AS DONE

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print(f"Marked done: {tasks[index]['title']}")
    else:
        print("Invalid task number")

# DELETE A TASK

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted: {removed['title']}")
    else:
        print("Invalid task number")

# MAIN MENU LOOP

def main():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task: ")
            add_task(title)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            view_tasks()
            num = int(input("Enter task number to complete: "))
            complete_task(num - 1)   

        elif choice == "4":
            view_tasks()
            num = int(input("Enter task number to delete: "))
            delete_task(num - 1)

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid choice, try again")
        
if __name__ == "__main__":
    main()
