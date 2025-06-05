from .stack import Stack

class ActionManager:
    def __init__(self):
        self._done = Stack()
        self._undone = Stack()

    def perform(self, action):
        print(f'Performing: {action}')
        self._done.push(action)
        self._undone.clear()

    def undo(self):
        if self._done.is_empty():
            print('Nothing to undo.')
            return
        action = self._done.pop()
        self._undone.push(action)
        print(f'Undid: {action}')

    def redo(self):
        if self._undone.is_empty():
            print('Nothing to redo.')
            return
        action = self._undone.pop()
        self._done.push(action)
        print(f'Redid: {action}')

    def show(self):
        print('Done:', self._done.to_list())
        print('Undone:', self._undone.to_list())
