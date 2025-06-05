from core.action_manager import ActionManager

def run_cli():
    manager = ActionManager()
    while True:
        cmd = input('Enter action, \"undo\", \"redo\", \"show\", or \"q\": ').strip().lower()
        if cmd == 'q':
            print('Exiting.')
            break
        elif cmd == 'undo':
            manager.undo()
        elif cmd == 'redo':
            manager.redo()
        elif cmd == 'show':
            manager.show()
        elif cmd:
            manager.perform(cmd)
