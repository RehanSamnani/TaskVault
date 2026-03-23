# task_manager.py

from model import create_task
from storage import load_tasks, save_tasks


def get_next_id(tasks):
    """
    Generates the next unique integer ID.
    If tasks list is empty, starts at 1.
    
    Why not use len(tasks) + 1?
    Because if you delete task #3 from [1,2,3], 
    len = 2, so next ID = 3 again — collision!
    Always base ID on the MAXIMUM existing ID.
    """
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(title):
    """
    Creates a new task and saves it.
    Returns the created task so the caller can confirm it.
    """
    # Guard: reject empty or whitespace-only titles
    title = title.strip()
    if not title:
        print("❌ Error: Task title cannot be empty.")
        return None

    tasks = load_tasks()
    new_task = create_task(get_next_id(tasks), title)
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task


def list_tasks(filter_status=None):
    """
    Returns all tasks, optionally filtered by status.
    filter_status: None | "pending" | "done"
    """
    tasks = load_tasks()

    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]

    return tasks


def mark_done(task_id):
    """
    Finds task by ID and marks it done.
    Returns True on success, False if not found.
    """
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "done":
                print(f"ℹ️  Task #{task_id} is already marked as done.")
                return False
            task["status"] = "done"
            save_tasks(tasks)
            return True

    return False   # ID not found


def delete_task(task_id):
    """
    Removes a task by ID.
    Returns True on success, False if not found.
    """
    tasks = load_tasks()
    original_count = len(tasks)

    # Keep all tasks EXCEPT the one with matching ID
    updated_tasks = [t for t in tasks if t["id"] != task_id]

    if len(updated_tasks) == original_count:
        return False   # Nothing was removed — ID didn't exist

    save_tasks(updated_tasks)
    return True