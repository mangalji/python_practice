# def add_task():
#     task = input("Enter your task: ")

def to_do_list():
    tasks = []

    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("enter the task:")
            tasks.append(task)
        elif choice == '2':
            task = input("enter the task")
            if task in tasks:
                tasks.remove(task)
            else:
                print("task not found")
        elif choice == '3':
            print("Tasks: ")
            for task in tasks:
                print(f"--{task}--")
        elif choice == '4':
            break
        else:
            print("Invalid choice")

print(to_do_list())

