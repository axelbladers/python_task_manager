print("What would you like to do?")
menu_list = "1: Add Task\n2: View Tasks\n3: Mark Task as Done\n4: Delete Task\n5: Exit Program"
print(menu_list)
list_Of_Tasks = []

while True:
    decision = input("Your Choice:")
    if decision.isdigit():
        decision = int(decision)
    else:
        print("Invalid input. Please enter a number.")
        continue

    if decision == 1:
        task = input("Enter task:")
        list_Of_Tasks.append(task)
    elif decision == 2:
        print("Tasks:")
        for index, task in enumerate(list_Of_Tasks, 1):
            print(f"{index}: {task}")
    elif decision == 3:
        if list_Of_Tasks:
            done_task = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= done_task < len(list_Of_Tasks):
                print(f"Task '{list_Of_Tasks[done_task]}' marked as done.")
                list_Of_Tasks[done_task] += " (Done)"
            else:
                print("Invalid task number.")
        else:
            print("No tasks to mark as done.")
    elif decision == 4:
        if list_Of_Tasks:  
            delete_task = int(input("Enter task number to delete: ")) - 1
            if 0 <= delete_task < len(list_Of_Tasks):
                print(f"Task '{list_Of_Tasks.pop(delete_task)}' deleted.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")
    elif decision == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")


