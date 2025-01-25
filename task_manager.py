from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self,task):
        self.tasks.append(task)
    def remove_task(self,task):
        self.tasks.remove(tasks)
    def get_all_tasks(self):
        return self.tasks
    def filter_by_priority(self,priority):
        return [task for task in self.tasks if task.priority == priority]
    def mark_task_completed(self,task):
        task.mark_completed()