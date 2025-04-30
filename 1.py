print("Welcome to your Daily Reminders!")
tasks = []

while True:
    print("\nMenu:")  
    print("Press (1) to Add Task")
    print("Press (2) to View Tasks")
    print("Press (3) Delete Task")
    print("Press (4) to Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task added! You now have {len(tasks)} task(s).")
        
    elif choice == "2":
        if tasks:
            print("\n Your Tasks:")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t}")
        else:
            print("Your task list is empty.")
            
    elif choice == "3":
        if tasks:
            print("\nWhich task number do you want to delete?")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t}")
            try:
                task_num = int(input("Enter task number: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' deleted.")
                else:
                    print(" Invalid task number.")
            except ValueError:
                print("Please enter a number.")
        else:
            print(" No tasks to delete.")
            
    elif choice == "4":
        print("Goodbye! Stay productive!")
        break
    else:
        print("Invalid choice, please pick 1-4.") 
