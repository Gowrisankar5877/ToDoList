class Task:
    def __init__(self,title,description,priority='Medium',due_date=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False
    def mark_completed(self):
        self.completed = True
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{self.priority}] {self.title} - {self.description}-{status}"