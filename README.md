# TaskVault

taskvault/
│
├── main.py          ← entry point
├── task_manager.py  ← core logic
├── storage.py       ← file read/write
├── models.py        ← Task data model
└── tasks.json       ← persistent storage

In models.py, design a Task as a Python dictionary or class:
python{
  "id": 1,
  "title": "Learn data structures",
  "status": "pending",   # or "done"
  "created_at": "2026-03-07"
}


Step 3 — Build the Storage Layer
In storage.py:

load_tasks() → reads tasks.json, returns list of tasks
save_tasks(tasks) → writes updated list back to file
Handle the case where the file doesn't exist yet


Step 4 — Implement Core Logic
In task_manager.py:

add_task(title) → create task, assign ID, save
list_tasks() → show all tasks with their status
mark_done(task_id) → find task by ID, update status
delete_task(task_id) → remove task from list


Step 5 — Build the CLI Interface
In main.py, parse terminal arguments:
bashpython main.py add "Study algorithms"
python main.py list
python main.py done 1
python main.py delete 2
```

Use Python's built-in `sys.argv` or `argparse` library — **no heavy frameworks.**

---

### Step 6 — Handle Edge Cases & Polish Output

Make output readable:
```
ID | Title                  | Status   | Date
---+------------------------+----------+------------
1  | Study algorithms       | ✅ done  | 2026-03-07
2  | Build TaskVault        | ⏳ pending | 2026-03-07
```

---

## 8. Important Edge Cases

| Scenario | What Should Happen? |
|---|---|
| User runs `done 999` (ID doesn't exist) | Print clear error: "Task not found" |
| `tasks.json` is missing on first run | Auto-create it silently |
| `tasks.json` is corrupted / invalid JSON | Warn user, do not crash |
| User adds a task with empty title `""` | Reject it with a message |
| User lists tasks when list is empty | Print "No tasks yet." gracefully |
| Duplicate task titles | Allow it — tasks use ID, not title |

> ⚠️ Real engineers think about **what can go wrong**, not just what works.

---

## 9. Suggested Technologies
```
Language  : Python 3
Libraries : json (built-in), sys / argparse (built-in), datetime (built-in)
Storage   : tasks.json (flat file)
Editor    : VS Code / any IDE
No external libraries needed. This teaches you to build things from scratch.

10. Learning Resources
TypeResource📄 Best ArticleReal Python — Working with JSON📘 DocumentationPython argparse docs🎥 Best VideoCorey Schafer — Python argparse tutorial (YouTube)🔬 Advanced ResourceThe Art of Command Line (GitHub)

11. Stretch Improvements
Once your core version works, push further:

Priority system — add priority: high/medium/low to tasks
Filter by status — python main.py list --status done
Due dates — add due_date field and warn when overdue
Search — python main.py search "algorithm"
Export to CSV — output tasks in spreadsheet format
Color output — use colorama library for colored terminal text


12. Engineering Reflection
After you finish, answer these like an engineer:

What happens if two people run this program at the same time on the same file? (Think: race conditions)
Your tasks.json file grows to 1 million tasks — what breaks first?
Right now you're storing data in a flat JSON file. What are the 3 biggest weaknesses of this approach?
If you had to replace the JSON file with a real database — what would change in your code? Which file would you touch, and why only that file?


13. Bonus Challenge — Hard Mode 🔥

"Redesign the storage layer so TaskVault can sync tasks across two computers using a shared file on Google Drive or Dropbox — without losing data if both computers modify the file at the same time."

Think about:

Conflict detection
What fields would you add to each task?
Can you solve this without a server?


🧭 Mentor's Note
This project seems simple. That is the trap.
The real skill being tested is: Can you write code that is clean, modular, handles failure gracefully, and is easy to extend? 99% of beginners write messy, all-in-one scripts. You should write code that a senior engineer would not be embarrassed to read.
When you finish, come back and type NEXT PROJECT — and we move up. 🚀