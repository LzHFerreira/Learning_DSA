import unittest
from core.tasks import Tasks

class TestTasks(unittest.TestCase):
    def setUp(self):
        self.tasks = Tasks()

    def test_add_task(self):
        self.tasks.add_task('task1')
        self.assertEqual(self.tasks.task_count(), 1)

    def test_execute_task(self):
        self.tasks.add_task('task1')
        task = self.tasks.execute_task()
        self.assertEqual(task, 'task1')
        self.assertTrue(self.tasks.is_empty())

    def test_is_empty(self):
        self.assertTrue(self.tasks.is_empty())
        self.tasks.add_task('task1')
        self.assertFalse(self.tasks.is_empty())

    def test_task_count(self):
        self.assertEqual(self.tasks.task_count(), 0)
        self.tasks.add_task('task1')
        self.assertEqual(self.tasks.task_count(), 1)

if __name__ == '__main__':
    unittest.main()
