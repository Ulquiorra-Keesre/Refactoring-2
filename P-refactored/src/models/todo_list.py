from src.models.task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, description: str):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                return
        raise ValueError(f"Task '{description}' not found.")

    def mark_task_completed(self, description: str):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                return
        raise ValueError(f"Task '{description}' not found.")

    def get_tasks(self):
        return self.tasks
