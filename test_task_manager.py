import unittest
from task import Task
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()
        self.task1 = Task("Task 1", "Description 1", "High", "2025-01-31")
        self.task2 = Task("Task 2", "Description 2", "Medium")
        self.task_manager.add_task(self.task1)
        self.task_manager.add_task(self.task2)

    def test_add_task(self):
        self.assertEqual(len(self.task_manager.get_all_tasks()), 2)

    def test_remove_task(self):
        self.task_manager.remove_task(self.task1)
        self.assertEqual(len(self.task_manager.get_all_tasks()), 1)

    def test_filter_by_priority(self):
        high_priority_tasks = self.task_manager.filter_by_priority("High")
        self.assertEqual(len(high_priority_tasks), 1)

    def test_mark_task_completed(self):
        self.task_manager.mark_task_completed(self.task1)
        self.assertTrue(self.task1.completed)

if __name__ == '__main__':
    unittest.main()
