# storage.py

import json
import os

FILE_PATH = "tasks.json"

def load_tasks():
    """
    Reads tasks.json and returns a list of task dicts.
    Handles 3 real-world failure cases:
      1. File doesn't exist yet (first run)
      2. File is empty
      3. File has corrupted/invalid JSON
    """
    # Case 1: File doesn't exist — return empty list, don't crash
    if not os.path.exists(FILE_PATH):
        return []

    # Case 2 & 3: File exists but might be broken
    try:
        with open(FILE_PATH, "r") as f:
            content = f.read().strip()
            if not content:           # Empty file
                return []
            return json.loads(content)

    except json.JSONDecodeError:
        # Case 3: Corrupted JSON — warn user, don't destroy their data
        print("⚠️  Warning: tasks.json is corrupted. Starting fresh.")
        return []


def save_tasks(tasks):
    """
    Writes the full task list to tasks.json.
    indent=2 makes it human-readable (open the file and see for yourself).
    """
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=2)