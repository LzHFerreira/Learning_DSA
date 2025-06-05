from core.tasks import Tasks

def run_cli():
    task_manager = Tasks()
    while True:
        command = input('Enter \"add\" to add a task, \"execute\" to execute a task, \"count\" to check tasks, or \"q\" to quit: ').strip().lower()
        if command == 'q':
            print('Exiting the task manager.')
            break
        elif command == 'add':
            task = input('Enter the task description: ')
            task_manager.add_task(task)
            print(f'Task \"{task}\" added.')
        elif command == 'execute':
            try:
                executed_task = task_manager.execute_task()
                print(f'Executed task: {executed_task}')
            except IndexError as e:
                print(e)
        elif command == 'count':
            print(f'Number of tasks in the queue: {task_manager.task_count()}')
        else:
            print('Invalid command. Please try again.')
