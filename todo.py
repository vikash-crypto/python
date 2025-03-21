class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def remove(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Removed task: {task}")
        else:
            print(f"Task '{task}' not found in the list")

    def view(self):
        if self.tasks:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty")

# Example usage:
todo = TodoList()
todo.add("Buy groceries")
todo.add("Complete assignment")
todo.view()
todo.remove("Buy groceries")
todo.view()
