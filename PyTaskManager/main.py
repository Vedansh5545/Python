import argparse
import os

# Define the TaskManager class
class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                lines = f.readlines()
                self.tasks = {}
                for i, line in enumerate(lines):
                    if line.startswith("Task"):
                        task_id, task = line.split(":", 1)
                        self.tasks[int(task_id.split()[1])] = task.strip()
        else:
            self.tasks = {}

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            for task_id, task in self.tasks.items():
                f.write(f"Task {task_id}: {task}\n")

    def add_task(self, task):
        self.tasks[len(self.tasks) + 1] = task
        self.save_tasks()

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_tasks()
        else:
            print(f"Task {task_id} not found.")

    def list_tasks(self):
        if self.tasks:
            for task_id, task in self.tasks.items():
                print(f"{task_id}: {task}")
        else:
            print("No tasks.")

# Define the main function
def main():
    parser = argparse.ArgumentParser(description='Simple Task Manager')
    parser.add_argument('filename', help='File to store tasks')
    parser.add_argument('--add', help='Add a new task')
    parser.add_argument('--delete', type=int, help='Delete a task by id')
    parser.add_argument('--list', action='store_true', help='List all tasks')

    args = parser.parse_args()

    task_manager = TaskManager(args.filename)

    if args.add:
        task_manager.add_task(args.add)
    elif args.delete is not None:
        task_manager.delete_task(args.delete)
    elif args.list:
        task_manager.list_tasks()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
