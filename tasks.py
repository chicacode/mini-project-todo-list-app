
def add_task(tasks, task):
    tasks.append(task)
    print(f'{task} has been added to the list')

def remove_task(tasks):
    if not tasks:
        print("No task removed")
        return

    print("Current to do list")
    for index,task in enumerate(tasks,1):
        print(f"{index}. {task}")

    try:
        task_index = int(input("Enter the task number to remove: "))
        if 0 <= task_index < len(tasks):
            # # test = task_index + 1
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

