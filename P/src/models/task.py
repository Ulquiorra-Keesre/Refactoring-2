class Task:
    def __init__(self, description, completed=False):
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Task must be a non-empty string")
        self.description = description
        self.completed = completed
    
    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "done" if self.completed else "undone"
        return f"[{status}] {self.description}"
    




