
<a href="https://www.youtube.com/@INTERNETSTUDENTS" target="_blank">Video Solution | INTERNET STUDENTS | Video Tutorial</a>


# Task Tracker

Task Tracker is a simple command-line application written in Python for managing tasks. It allows users to add, list, update, delete, and change the status of tasks. Tasks are stored in a JSON file, and the application provides various commands for interacting with the task list.

## Features

- **Add a Task:** Add a new task with a description.
- **List Tasks:** List all tasks or filter by status (e.g., `todo`, `in-progress`, `done`).
- **Update a Task:** Update the description of an existing task.
- **Delete a Task:** Remove a task from the list.
- **Mark Task In Progress:** Change the status of a task to "in-progress".
- **Mark Task Done:** Change the status of a task to "done".

## Installation

[python : required] -- No installation is required. Simply clone the repository and run the script using Python.

## Setup

```bash
git clone https://github.com/yourusername/task-tracker.git
```

## Usage

To use the Task Tracker, run the script with the desired command from the command line. The available commands are:

### Add Task
```bash
python task_tracker.py add "Task description"
```

### List All Tasks
```bash
python task_tracker.py list
```
### List Tasks by Status
```bash
python task_tracker.py list <status>
```
### Update a Task
```bash
python task_tracker.py update <task_id> "New description"
```
### Delete a Task
```bash
python task_tracker.py delete <task_id>
```

### Mark Task In Progress
```bash
python task_tracker.py mark-in-progress <task_id>
```
### Mark Task Done
```bash
python task_tracker.py mark-done <task_id>
```
## File Format
```bash
_json_
[
    {
        "id": 1,
        "description": "Task description",
        "status": "todo",
        "createdAt": "YYYY-MM-DD HH:MM:SS",
        "updatedAt": "YYYY-MM-DD HH:MM:SS"
    }
]
```




