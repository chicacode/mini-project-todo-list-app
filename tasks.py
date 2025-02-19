def add_task(task_list, task):
    task_list.append(task)
    print(f'{task} has been added to the list')


def remove_task(todo_list):
    if not todo_list:
        print("No tasks to remove.")
        return

    task = input("Enter the task to remove: ")
    if task in todo_list:
        todo_list.remove(task)
        print(f"'{task}' has been removed from the list.")
    else:
        print("Task not found in the list.")

def view_tasks(task_list):
    if not task_list:
        print('No tasks in the To-Do List')
    else:
        print('\n To-Do List Tasks')
        for index, task in enumerate(task_list, 1):
            print(f'{index}. {task}')
