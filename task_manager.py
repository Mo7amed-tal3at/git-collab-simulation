# Task Manager - Main File
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task})