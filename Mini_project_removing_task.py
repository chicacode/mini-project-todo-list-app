# To-Do List Application
# 1. Add Task
# 2. Remove Task
# 3. View Tasks
# 4. Exit
# Enter your choice: 2
# Enter the task to remove: Buy groceries
# 'Buy groceries' has been removed from the list.
# To-Do List Application
# 1. Add Task
# 2. Remove Task
# 3. View Tasks
# 4. Exit
# Enter your choice: 3
# To-Do List:
# 1. Finish homework


print("Welcome to your personal task manager!")
print()
print("Get ready to prepare your to-do-list!")
print()
user_choice = input("What do you want to do now?:\n"
                    "Press 1 to add a task\n"
                    "Press 2 to remove a task\n"
                    "Press 3 to visualize all your added tasks\n"+
                    "Press 4 to exit\n")
print()

task_list = []
if user_choice == 2:
    while task_list == task_list:
        task_to_remove = input("Enter the task NAME or the task NUMBER to remove: ")
        if task_to_remove in task_list:
            print(f"Are you sure you want to remove {task_to_remove}?")
            confirmation = input("Type YES to continue or NO to go back: ")
            if confirmation == "YES":
                task_list.pop(task_list[task_to_remove])
            else:
                print(user_choice)



