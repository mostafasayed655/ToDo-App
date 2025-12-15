"""
JSON-based storage layer for tasks.
Handles loading, saving, and ID generation for the tasks.json file.
"""

import json
import os
from typing import List, Dict, Any, Optional

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks() -> List[Dict[str, Any]]:
    """Load all tasks from the JSON file. Returns empty list if file missing or corrupted."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Save all tasks to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def generate_id(tasks: List[Dict[str, Any]]) -> int:
    """Generate a new unique ID based on existing tasks."""
    if not tasks:
        return 1
    return max(task.get("id", 0) for task in tasks) + 1


def get_task_by_id(tasks: List[Dict[str, Any]], task_id: int) -> Optional[Dict[str, Any]]:
    """Find a task by its ID. Returns None if not found."""
    for task in tasks:
        if task.get("id") == task_id:
            return task
    return None


def add_task(title: str) -> Dict[str, Any]:
    """Add a new task with the given title. Returns the created task."""
    tasks = load_tasks()
    new_task = {
        "id": generate_id(tasks),
        "title": title.strip(),
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task


def update_task_status(task_id: int, done: bool) -> bool:
    """Update the done status of a task. Returns True if successful."""
    tasks = load_tasks()
    task = get_task_by_id(tasks, task_id)
    if task is None:
        return False
    task["done"] = done
    save_tasks(tasks)
    return True


def toggle_task_status(task_id: int) -> bool:
    """Toggle the done status of a task. Returns True if successful."""
    tasks = load_tasks()
    task = get_task_by_id(tasks, task_id)
    if task is None:
        return False
    task["done"] = not task.get("done", False)
    save_tasks(tasks)
    return True


def delete_task(task_id: int) -> bool:
    """Delete a task by ID. Returns True if successful."""
    tasks = load_tasks()
    original_len = len(tasks)
    tasks = [t for t in tasks if t.get("id") != task_id]
    if len(tasks) == original_len:
        return False
    save_tasks(tasks)
    return True
