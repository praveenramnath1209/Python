lst = []

def add(task):
    lst.append(task)

def delete(task):
    index = task - 1
    if index >= 0 and index < len(lst): 
        x = lst[index]
        lst.remove(x)
        print(f"Removed task: {x}")
    else:
        print("Invalid task number!")

def view():
    print("\n------ Tasks ------")
    if len(lst) == 0:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(lst, 1):
            print(f"{i}. {task}")
    print("-------------------\n")

while True:
    print("-------- To-Do List --------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("----------------------------")

    op = input("Enter an option (1 to 4): ")

    if op == "1":
        task = input("Enter task: ")
        add(task)
    elif op == "2":
        view()
    elif op == "3":
        task = int(input("Enter the task number to remove: "))
        delete(task)
    elif op == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid option. Please enter 1 to 4.\n")
