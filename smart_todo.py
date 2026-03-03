"""
Smart To-Do Manager (CLI)
Author: Prakhar Srivastava
Description: Advanced CLI task manager with priority, status and search.
"""
import json
from datetime import datetime
FILE_NAME = "tasks.json"
# ---------- File Handling ----------
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
# ---------- Features ----------

def add_task(tasks):
    title = input("Enter task: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()

    if priority not in ["High", "Medium", "Low"]:
        priority = "Low"

    task = {
        "title": title,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
    print("\n===== TASK LIST =====")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] [{task['priority'].upper()}] "
              f"{task['title']} ({task['created_at']})")
    print()
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Task number to mark complete: "))
        tasks[num - 1]["completed"] = True
        save_tasks(tasks)
        print("✔ Task completed!\n")
    except (ValueError, IndexError):
        print("Invalid selection!\n")
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"🗑 Removed: {removed['title']}\n")
    except (ValueError, IndexError):
        print("Invalid selection!\n")
def search_task(tasks):
    keyword = input("Search keyword: ").lower()

    results = [t for t in tasks if keyword in t["title"].lower()]

    if not results:
        print("No matching tasks found.\n")
        return

    print("\n🔎 Search Results:")
    for task in results:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] [{task['priority']}] {task['title']}")
    print()
# -Main App --
def smart_todo():
    tasks = load_tasks()

    while True:
        print("""
===== SMART TODO MENU =====
1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Search Task
6. Exit
""")
        choice = input("Choose option (1-6): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            print("Goodbye ✅")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    smart_todo()
    todo_app()
