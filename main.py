from to_do_class import Task

tasks = []
def add_task():
    new_task = input("Enter a task: ")
    task = Task(new_task)
    tasks.append(task)

def list_tasks():
    completed = [task for task in tasks if task.complete]
    print(f"\nCompleted tasks: {len(completed)}")
    for task in tasks:
        if task.complete == True:
            print(f"{task.name} - Complete.")
        else:
            print(f"{task.name} - Not Complete.")

def update_task():
    list_tasks()
    upd_choice = int(input("\nEnter number of task to be updated: "))
    upd_choice -= 1
    upd_task = input("Enter new/updated task: ")
    tasks[upd_choice].name = upd_task
    print("\nUpdated list: ")
    list_tasks()

def completed_task():
    list_tasks()
    com_choice = int(input("\nEnter number of task that is completed: "))
    com_choice -= 1
    tasks[com_choice].task_complete()
    print(f"{tasks[com_choice].name} is completed.")
    list_tasks()

def delete_task():
    list_tasks()
    del_choice = int(input("\nEnter number of the task you want to delete: "))
    del_choice -= 1

    del tasks[del_choice]
    print("Task deleted!")

print("         TO-DO APP         ")


print("\n1. Add task")
print("2. List tasks")
print("3. Update task")
print("4. Mark task as complete")
print("5. Delete task")
print("6. Exit")



while True:
    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_task()

        elif choice == 2:
            list_tasks()

        elif choice == 3:
            update_task()

        elif choice == 4:
            completed_task()

        elif choice == 5:
            delete_task()

        elif choice == 6:
            break

    except ValueError:
        print("Please enter a number.")


