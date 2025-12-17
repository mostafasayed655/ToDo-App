# Backend Assessment Solutions

This repository contains the complete submission for the backend assessment, covering three main tasks:
1.  **Flask To-Do App:** A complete task management web application.
2.  **Problem Solving:** A Python script to find the shortest string.
3.  **SQL Challenge:** A query to filter students based on grades.

---

## 📂 Project Structure

```text
toDoApp/
├── app.py              # Task 1: Flask application entry point
├── ps_solution.py      # Task 2: Problem Solving solution (Shortest String)
├── student.sql         # Task 3: SQL Query solution
├── storage.py          # JSON persistence layer
├── tasks.json          # Task data storage
├── README.md           # This file
├── templates/
│   ├── base.html       # Base template
│   └── index.html      # Main task list view
└── static/
    ├── styles.css      # Application styles
    └── app.js          # Client-side JavaScript
```
## 1️⃣ Task 1: Flask To-Do App

### Setup

#### 1. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Run the application

```bash
python app.py
```

Or using Flask CLI:

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```

#### 4. Open in browser

Navigate to [http://localhost:5000](http://localhost:5000)

### Task Entity

Each task has the following structure:

```json
{
  "id": 1,
  "title": "Task description",
  "done": false
}
```

## API Endpoints

| Method | Endpoint             | Description        |
| ------ | -------------------- | ------------------ |
| GET    | `/`                  | Display all tasks  |
| POST   | `/tasks`             | Add a new task     |
| POST   | `/tasks/<id>/toggle` | Toggle task status |
| POST   | `/tasks/<id>/update` | Update task status |
| POST   | `/tasks/<id>/delete` | Delete a task      |

---

## 2️⃣ Task 2: Problem Solving

**File:** `ps_solution.py`

A Python script that contains a function to find and return the **shortest string** in a list of strings.

### How to Run
You can run the script directly in the terminal to see the test case output:

```bash
python ps_solution.py

```

---

## 3️⃣ Task 3: SQL Challenge

**File:** `student.sql`

This file contains the SQL query required to retrieve all students who achieved grades between **90 and 100**.

### Schema Used:

* **Table:** `students`
* **Columns:** `student_id`, `name`, `grade`


### License

MIT
