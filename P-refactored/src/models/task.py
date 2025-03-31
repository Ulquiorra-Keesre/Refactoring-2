class Task:
    def __init__(self, description: str, completed: bool = False):
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Task description must be a non-empty string.")
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"[{'done' if self.completed else 'undone'}] {self.description}"
