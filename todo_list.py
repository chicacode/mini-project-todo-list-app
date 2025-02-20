from tasks import add_task, remove_task, view_tasks, suggest_tasks

def main():
    tasks = []
    while True:
        print('\n To-Do List Application')
        print('\n 1.Add Task \n 2. Remove task \n 3. View Tasks \n 4. Suggest Task \n 5. Leave App')
        choice = input('Enter your choice: ')
        if choice == "1":
            task = input('Enter task: ')
            priority = input("Set as High, Medium or Low: ").lower()
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            add_task(tasks, task, priority, deadline)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            suggest_tasks(tasks)
        elif choice == "5":
            print("Exiting app... Good Bye!")
            break
        else:
            print('Invalid choice')
if __name__ == "__main__":
    main()