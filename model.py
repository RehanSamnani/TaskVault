# models.py

from datetime import date

def create_task(task_id, title):
    """
    Factory function — builds and returns a new task dictionary.
    A dictionary is used instead of a class to stay JSON-compatible.
    """
    return {
        "id": task_id,
        "title": title,
        "status": "pending",
        "created_at": str(date.today())   # e.g. "2026-03-07"
    }