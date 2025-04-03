
todo_file = 'Text.txt'


def add(task):
    with open(todo_file, 'a') as file:
        file.write(task + '\n')
    print(f"Task '{task}' added!")


def remove(task):
    try:
        with open(todo_file, 'r') as file:
            tasks = file.readlines()
       
        tasks = [t.strip() for t in tasks]  
        if task in tasks:
            tasks.remove(task)
            with open(todo_file, 'w') as file: 
                for t in tasks:
                    file.write(t + '\n')
            print(f"Task '{task}' removed!")
        else:
            print(f"Task '{task}' not found.")
    except FileNotFoundError:
        print("No to-do list found.")


def view():
    try:
        with open(todo_file, 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour To-Do List:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("Your to-do list is empty.")
    except FileNotFoundError:
        print("No to-do list found.")


if __name__ == "__main__":

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            add(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove(task)
        elif choice == '3':
            view()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")