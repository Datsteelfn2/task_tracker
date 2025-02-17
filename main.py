import os
import time
tasks=[]#we want to access this list everywhere so we keep it outside any function to make it global
done_tasks=[]
def add_tasks():
    os.system("clear")
    add=input("What would you like to add:> ")
    if add not in tasks:
        tasks.append(add)
    else:
        print("No duplicate tasks")
        time.sleep(2)


def delete_task():
    os.system("clear")
    print("You may only delete \033[31mone\033[0m task at a time")
    name_delete=input("NAME the task you wanat to delete:> ")
    if name_delete in tasks:
        delete_assurance=input("\033[0mAre you sure you want to delete this?\033[0m:> ")
        if delete_assurance.lower()=="yes":
            tasks.remove(name_delete)
            print(f"{name_delete} has been deleted from your task list")
            time.sleep(1.5)
    else:
        print(f"{name_delete} is not in your tasks list, press 3 on your menu to see your tasks names")
        time.sleep(3)


def view_tasks():
    os.system("clear")
    print("TASK VIEWER")
    if not tasks:
        print("Your list is empty")
    for task in range(len(tasks)):
        print(f"{task+1}: {tasks[task]}")
    if tasks:
        fully_remove = input("Do you want to remove everything from your to do list:> ")
        if fully_remove == "yes":
            re_fully_remove = input( "\033[31mAre you sure? this is irreversable\033[0m:> ")
            if re_fully_remove.lower() == "yes":
                tasks.clear()
                print("Emptied list")
    time.sleep(1)

def task_done():
    #lets print a list using a different method because why not
    counter=1
    os.system("clear")
    
    whats_done=input("NAME the task you want to mark as done, can only check \033[31mONE TASK\033[0m")
    print("DONE TASKS")
    if whats_done in tasks:
        done_tasks.append(whats_done)
        tasks.remove(whats_done)
        for done in done_tasks:
            print(f"{counter}: {done}")
    else:
        print("\033[31m That is not a task on your list\033[0m")
    time.sleep(3)
while True:
    print("MENU")
    choice=int(input("1. Do you want to Add a task\n2. Delete a task,\n3. View tasks,\n4. Mark a task as done\n5. Edit an existing task\n6. Exit the program\n:> "))
    if choice==1:
        
        add_tasks()
    elif choice==2:
        delete_task()
    elif choice==3:
        view_tasks()
    elif choice==4:
        task_done()
    elif choice==5:
        edit_choice=input("Which task do you want to edit:> ")
        if edit_choice in tasks:
            change_task=input("What dou you wan to change it to:> ")
            for i in range(0,len(tasks)):
                if edit_choice==tasks[i]:
                    tasks[i]=change_task
                    print(f"{edit_choice} has been succesfully been changed to {change_task}")
                    time.sleep(2)
        else:
            print(f"{edit_choice} is not in your list of tasks")
            time.sleep(2)
    elif choice==6:
        break
    
    else:
        print("not a valid command, type one of the following: 1, 2, 3, 4, 5, or 6 (to exit the program) with no spaces")
        time.sleep(3)
    os.system('clear')
    
print("Youve exited the program")

