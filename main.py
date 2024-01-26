tasks = []

def main():
    message = """
        ----------------------------
    | Welcome to Task Manager!   |
    | 1 - add tasks to a list    |     
    | 2 - mark task as complete  |
    | 3 - view tasks             |
    | 4 - Quit                   |
        ----------------------------
    """                
    
    while True :
        print(message)
        choice = input("Enter your choice:")

        if choice == "1":
            add_task()

        elif choice == "2":
            mark_task_complete()

        elif choice == "3":
            view_tasks(tasks)

        elif choice == "4":
            break
        else :
            print("Invalid choice ,Please enter a number between 1 et 4")

def add_task():
    task = input("Enter task: ")
    task_info = {"task": task, "completed": False}
    tasks.append(task_info)
    print("Task added to the list successfuly")

def mark_task_complete():
    #show them to user
    incomplete_tasks = [task for task in tasks if task["completed"] == False]
    if len(incomplete_tasks) == 0 :
        print("No Incomplete Tasks Found!")
        return
    
    for i, task in enumerate(incomplete_tasks):
        print(f'{i+1}- {task["task"]}')
        print("-"*30)
    try :
        #get the task from user
        task_number = int(input("choose the task to complete: "))
        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalid Task Number, please choose a valid number" )
            return

        #mark as complited
        incomplete_tasks[task_number - 1]["completed"] = True
        print("Marked as completed successfully.")
    except ValueError :
        print("Invalid Input Please Enter a Number")
    

def view_tasks(tasks_list):
    if not tasks_list :
        print("\n No tasks available \n")
        return
    
    for i, task in enumerate(tasks_list):
        # if task["completed"] :
        #     status = "✅"
        # else :
        #     status = "❌"
        status = "✅" if task["completed"] else "❌"

        print(f'{i+1}. {task["task"]} {status}')

if __name__ == "__main__" :
    main()


