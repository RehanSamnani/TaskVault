# main.py

import argparse
from task_manager import add_task, list_tasks, mark_done, delete_task


def display_tasks(tasks):
    """
    Prints tasks in a clean, readable table format.
    """
    if not tasks:
        print("📭 No tasks found.")
        return

    # Print header
    print(f"\n{'ID':<5} {'Title':<35} {'Status':<12} {'Created'}")
    print("-" * 65)

    for task in tasks:
        status_icon = "✅ done   " if task["status"] == "done" else "⏳ pending"
        print(f"{task['id']:<5} {task['title']:<35} {status_icon:<12} {task['created_at']}")

    print()  # empty line for breathing room


def main():
    # ── Top-level parser ──────────────────────────────────────────
    parser = argparse.ArgumentParser(
        prog="taskvault",
        description="📦 TaskVault — Your personal CLI task manager"
    )

    # argparse subcommands: add, list, done, delete
    subparsers = parser.add_subparsers(dest="command")

    # ── 'add' command ─────────────────────────────────────────────
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title (use quotes for multi-word titles)")

    # ── 'list' command ────────────────────────────────────────────
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "--status",
        choices=["pending", "done"],
        help="Filter by status"
    )

    # ── 'done' command ────────────────────────────────────────────
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID to mark as done")

    # ── 'delete' command ──────────────────────────────────────────
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    # ── Parse & Route ─────────────────────────────────────────────
    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        if task:
            print(f"✅ Added task #{task['id']}: \"{task['title']}\"")

    elif args.command == "list":
        tasks = list_tasks(filter_status=args.status)
        display_tasks(tasks)

    elif args.command == "done":
        success = mark_done(args.id)
        if success:
            print(f"✅ Task #{args.id} marked as done!")
        else:
            print(f"❌ Task #{args.id} not found or already done.")

    elif args.command == "delete":
        success = delete_task(args.id)
        if success:
            print(f"🗑️  Task #{args.id} deleted.")
        else:
            print(f"❌ Task #{args.id} not found.")

    else:
        # No command given — show help
        parser.print_help()


if __name__ == "__main__":
    main()