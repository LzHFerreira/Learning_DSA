class DecisionNode:
    def __init__(self, question=None, left=None, right=None, label=None):
        self.question = question
        self.left = left
        self.right = right
        self.label = label

def traverse(node):
    if node.label is not None:
        print(f'Decision: {node.label}')
        return node.label

    answer = input(f'{node.question} (yes/no): ').strip().lower()
    if answer in ('yes', 'y'):
        return traverse(node.left)
    elif answer in ('no', 'n'):
        return traverse(node.right)
    else:
        print('Please answer \"yes\" or \"no\".')
        return traverse(node)

def print_tree(node, indent='', branch='Root'):
    if node is None:
        return
    if node.label is not None:
        print(f'{indent}[{branch}] -> [Leaf: {node.label}]')
    else:
        print(f'{indent}[{branch}] -> Q: {node.question}')
        print_tree(node.left, indent + '    ', 'Yes')
        print_tree(node.right, indent + '    ', 'No')
