from tasks import add_task, view_tasks

def main():
    tasks = []
    while True:
        print('\n To-Do List Application')
        print('\n 1.Add Task \n 2. Remove task \n 3. View Tasks \n 4. Leave App')
        choice = input('Enter your choice: ')

        if choice == "1":
            task = input('Enter task:')
            add_task(tasks, task)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Exiting app... Good Bye!")
            break
        else:
            print('Invalid choice')
if __name__ == "__main__":
    main()