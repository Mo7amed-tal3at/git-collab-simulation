# Task Manager - Main File
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' deleted!")
    else:
        print("Invalid task number!")