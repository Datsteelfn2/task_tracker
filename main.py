import os
import time
tasks=[]
#we want to access this list everywhere so we keep it as is
def view_tasks():
    for task in range(len(tasks)):
        print(f"#{task}: {tasks[task]}")

def add_tasks():
    add=input("What would you like to add:> ")
    tasks.append(add)

while True:
    os.system("clear")
    choice=int(input("1. Do you want to Add a task\n2. Delete a task,\n3. View a task,\n4. Mark a task as done or\n5. Exit the program\n:> "))
    if choice==1:
        add_tasks()
    elif choice==3:
        os.system("clear")
        view_tasks()
        time.sleep(2)
    elif choice==5:
        break
    os.system("clear")
    
print("Youve exited the program")