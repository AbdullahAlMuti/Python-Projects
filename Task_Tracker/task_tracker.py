import json
import os
import sys
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.file_name = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                json.dump([], file)
        with open(self.file_name, 'r') as file:
            self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def generate_task_id(self):
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1

    def add_task(self, description):
        task = {
            "id": self.generate_task_id(),
            "description": description,
            "status": "todo",
            "createdAt": self.get_current_time(),
            "updatedAt": self.get_current_time()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task added successfully (ID: {task["id"]})')

    def update_task(self, task_id, new_description):
        task = self.find_task(task_id)
        if task:
            task["description"] = new_description
            task["updatedAt"] = self.get_current_time()
            self.save_tasks()
            print(f'Task {task_id} updated successfully')

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f'Task {task_id} deleted successfully')

    def mark_in_progress(self, task_id):
        task = self.find_task(task_id)
        if task:
            task["status"] = "in-progress"
            task["updatedAt"] = self.get_current_time()
            self.save_tasks()
            print(f'Task {task_id} marked as in-progress')

    def mark_done(self, task_id):
        task = self.find_task(task_id)
        if task:
            task["status"] = "done"
            task["updatedAt"] = self.get_current_time()
            self.save_tasks()
            print(f'Task {task_id} marked as done')

    def list_tasks(self, status=None):
        filtered_tasks = self.tasks if not status else [task for task in self.tasks if task['status'] == status]
        if not filtered_tasks:
            print("No tasks found")
        else:
            for task in filtered_tasks:
                print(f'{task["id"]}: {task["description"]} - {task["status"].upper()}')

    def find_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        print(f"Task {task_id} not found")
        return None

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Main function to handle CLI commands
def main():
    task_manager = TaskManager()
    args = sys.argv[1:]

    if not args:
        print("Usage: task-cli <command> [<args>]")
        return

    command = args[0]

    if command == "add" and len(args) > 1:
        task_description = " ".join(args[1:])
        task_manager.add_task(task_description)

    elif command == "update" and len(args) > 2:
        task_id = int(args[1])
        task_description = " ".join(args[2:])
        task_manager.update_task(task_id, task_description)

    elif command == "delete" and len(args) == 2:
        task_id = int(args[1])
        task_manager.delete_task(task_id)

    elif command == "mark-in-progress" and len(args) == 2:
        task_id = int(args[1])
        task_manager.mark_in_progress(task_id)

    elif command == "mark-done" and len(args) == 2:
        task_id = int(args[1])
        task_manager.mark_done(task_id)

    elif command == "list":
        if len(args) == 1:
            task_manager.list_tasks()
        elif args[1] in ["done", "todo", "in-progress"]:
            task_manager.list_tasks(args[1])

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
