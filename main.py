import os
import time
tasks=[]
#we want to access this list everywhere so we keep it as is
def view_tasks():
    
    os.system("clear")
    for task in range(len(tasks)):
        print(f"{task+1}: {tasks[task]}")
    time.sleep(3)
def add_tasks():
    os.system("clear")
    add=input("What would you like to add:> ")
    tasks.append(add)
def delete_task():
    print("You may only delete \033[31mone\033[0m task at a time")
    name_delete=input("NAME the task you wanat to delete:> ")
    if name_delete in tasks:
        tasks.remove(name_delete)
        print(f"{name_delete} has been deleted from your task list")
        time.sleep(1.5)
    else:
        print(f"{name_delete} is not in your tasks list, press 3 on your menu to see your tasks names")

while True:
    
    choice=int(input("1. Do you want to Add a task\n2. Delete a task,\n3. View a task,\n4. Mark a task as done or\n5.Exit the program\n:> "))
    if choice==1:
        
        add_tasks()
    elif choice==2:
        delete_task()
    elif choice==3:
        
        view_tasks()
        
    elif choice==5:
        break
    
    os.system('clear')
    
print("Youve exited the program")