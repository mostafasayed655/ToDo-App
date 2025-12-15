"""
Flask To-Do App
A simple task management application with JSON file persistence.
"""

from flask import Flask, render_template, request, redirect, url_for, flash

import storage

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-in-production"


@app.route("/")
def index():
    """Display all tasks."""
    tasks = storage.load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    """Add a new task."""
    title = request.form.get("title", "").strip()
    if not title:
        flash("Task title cannot be empty.", "error")
    else:
        storage.add_task(title)
        flash("Task added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id: int):
    """Toggle the done status of a task."""
    if storage.toggle_task_status(task_id):
        flash("Task status updated.", "success")
    else:
        flash("Task not found.", "error")
    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/update", methods=["POST"])
def update_task(task_id: int):
    """Update task status based on checkbox value."""
    done = request.form.get("done") == "on"
    if storage.update_task_status(task_id, done):
        flash("Task status updated.", "success")
    else:
        flash("Task not found.", "error")
    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id: int):
    """Delete a task."""
    if storage.delete_task(task_id):
        flash("Task deleted.", "success")
    else:
        flash("Task not found.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
