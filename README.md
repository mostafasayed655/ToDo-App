# Flask To-Do App

A simple task management application built with Flask. Tasks are persisted to a JSON file.

## Features

- ✅ Add new tasks
- ✅ Mark tasks as done/not done using checkboxes
- ✅ Delete tasks
- ✅ Data persisted to JSON file
- ✅ Clean, responsive UI

## Project Structure

```
toDoApp/
├── app.py              # Flask application entry point
├── ps_solution.py      # solution of task 2
├── student.sql         # solution of task 3
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

## Setup

### 1. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

Or using Flask CLI:

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```

### 4. Open in browser

Navigate to [http://localhost:5000](http://localhost:5000)

## Task Entity

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

## License

MIT
