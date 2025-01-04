import os
import time
tasks=[]
we want to access this list everywhere so we keep it as is
def view_tasks():
    for task in range(len(tasks)):
        print(f"#{task}: {tasks[task]}")

def add_tasks():
    add=input("What would you like to add:> ")
    add.append(add)

while True:
    choice=int(input("1. Do you want to Add a task\n2. Delete a task,\n3. View a task,\n4. Mark a task as done or\n5. Exit the program\n:> "))

    elif choice==3:
        view_tasks
    elif choice==5:
        break
print("Youve exited the program")