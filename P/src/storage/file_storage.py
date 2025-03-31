import json
from src.models.task import Task

class FileStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save_tasks(self, tasks):
        data = [{"description": task.description, "completed": task.completed} for task in tasks]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
    
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Task(item["description"], item["completed"]) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        




