from datetime import datetime

def add_task(tasks, task, priority, deadline):
    if priority not in ["high", "medium", "low"]:
        print("Enter a valid priority, choose high, medium or low")
        return
    if datetime.strptime(deadline, '%m/%d/%Y'):
        print("Enter a valid date")
        return

    tasks.append({"task":task, "priority": priority, "deadline":deadline})
    print(f'{task} has been added to the list with priority {priority} and deadline {deadline}')

def remove_task(tasks):
    if not tasks:
        print("No task removed")
        return

    print("Current to do list")
    for index,task in enumerate(tasks,0):
        print(f"{index}. {task}")

    try:
        task_index = int(input("Enter the task number to remove: "))
        if 0 <= task_index < len(tasks):
            rem_task = tasks.pop(task_index)
            print(f"The task removed was {rem_task}")
        else:
            print("The task that you entered doesn't exist, try again")

    except ValueError:
        print("Please try a valid enter")

def view_tasks(tasks):
    if not tasks:
        print('No tasks in the To-Do List')
    else:
        print('\n To-Do List Tasks')
        for index, task in enumerate(tasks, 1):
            print(f'{index}. {task}')


def suggest_tasks(tasks):
    if not tasks:
        print('No tasks in the To-Do List')
        return
    print("Here are some tasks you might want to work on:")

