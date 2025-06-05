import unittest
from core.action_manager import ActionManager

class TestActionManager(unittest.TestCase):
    def setUp(self):
        self.manager = ActionManager()

    def test_perform_action(self):
        self.manager.perform('action1')
        self.assertEqual(self.manager._done.to_list(), ['action1'])
        self.assertEqual(self.manager._undone.to_list(), [])

    def test_undo_action(self):
        self.manager.perform('action1')
        self.manager.undo()
        self.assertEqual(self.manager._done.to_list(), [])
        self.assertEqual(self.manager._undone.to_list(), ['action1'])

    def test_redo_action(self):
        self.manager.perform('action1')
        self.manager.undo()
        self.manager.redo()
        self.assertEqual(self.manager._done.to_list(), ['action1'])
        self.assertEqual(self.manager._undone.to_list(), [])

    def test_show_actions(self):
        self.manager.perform('action1')
        self.manager.perform('action2')
        self.manager.undo()
        self.assertEqual(self.manager._done.to_list(), ['action1'])
        self.assertEqual(self.manager._undone.to_list(), ['action2'])

if __name__ == '__main__':
    unittest.main()
