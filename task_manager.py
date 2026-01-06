class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            print(f"{index + 1}. {task.title} - {status}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")


def main():
    manager = TaskManager()

    while True:
        print("\nStudent Task Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_number = int(input("Enter task number: "))
            manager.complete_task(task_number)

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
