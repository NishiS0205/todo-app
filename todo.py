todos = []

def add_task(task):
    todos.append(task)
    print(f"Added: {task}")

def view_tasks():
    if not todos:
        print("No tasks yet!")
    for i, task in enumerate(todos, 1):
        print(f"{i}. {task}")

def delete_task(number):
    removed = todos.pop(number - 1)
    print(f"Removed: {removed}")

while True:
    print("\n1. Add task  2. View tasks  3. Delete task  4. Quit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        num = int(input("Delete task number: "))
        delete_task(num)
    elif choice == "4":
        break