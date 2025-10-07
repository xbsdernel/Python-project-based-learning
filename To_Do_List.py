tasks = []
markedTasks = []

def list_tasks():
    index = 0
    for i in tasks:
        print(index,"-",i)
        index += 1
def list_marked_tasks():
    index = 0
    for i in markedTasks:
        print(index,"-",i)
        index += 1

def add_new_task():
    task = input("Enter the task: ")
    tasks.append(task)

def Mark_tasks_as_completed():
    list_tasks()
    choice = int(input("Enter the task number you wanna mark it: "))
    if choice <= len(tasks) and choice >= 0:
        markedTasks.append(tasks[choice])
        tasks.pop(choice)
        print("all marked tasks")
        list_marked_tasks()
    else:
        print("Invalid number!!, there is no task with that number")

def Delete_tasks():
    list_tasks()
    choice = int(input("Enter the task number: "))
    if choice <= len(tasks) and choice >= 0:
        print("Task",choice,"have been deleted")
        tasks.pop(choice)
    else:
        print("Invalid number!!, there is no task with that number")

def View_all_tasks_currently_stored():
    list_tasks()

def greeting():
    print("Welcome to my To Do list")
    print("Choose one: ")
    print("1- Add new tasks")
    print("2- Mark tasks as completed")
    print("3- Delete tasks")
    print("4- View all tasks currently stored")
    print("5- exit")

def looping():
    while True:
        greeting()
        number = int(input())
        if number == 1:
            add_new_task()
        elif number == 2:
            Mark_tasks_as_completed()
        elif number == 3:
            Delete_tasks()
        elif number == 4:
            View_all_tasks_currently_stored()
        elif number == 5:
            break
        else:
            print("Invalid choice, try again")
            continue

looping()
