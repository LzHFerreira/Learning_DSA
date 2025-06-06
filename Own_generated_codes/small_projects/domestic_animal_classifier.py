# Simple Decision Tree implementation using a binary tree structure
# Now with a CLI to visualize and interact with the tree


class DecisionNode:
    def __init__(self, question=None, left=None, right=None, label=None):
        self.question = question  # The question to ask at this node (None for leaf)
        self.left = left  # Left child (if answer is 'yes' or True)
        self.right = right  # Right child (if answer is 'no' or False)
        self.label = label  # Label for leaf node (classification result)


def traverse(node):
    """
    Traverse the decision tree interactively.
    Args:
        node: The current DecisionNode.
    Returns:
        The label/classification at the leaf node.
    """
    # If this is a leaf node (no question), return its label
    if node.label is not None:
        print(f"Decision: {node.label}")  # Output the decision
        return node.label

    # Otherwise, ask the question at this node
    answer = input(f"{node.question} (yes/no): ").strip().lower()
    # Traverse left if answer is 'yes', right if 'no'
    if answer in ("yes", "y"):
        return traverse(node.left)
    elif answer in ("no", "n"):
        return traverse(node.right)
    else:
        print("Please answer 'yes' or 'no'.")
        return traverse(node)  # Ask again if invalid input


def print_tree(node, indent="", branch="Root"):
    """
    Recursively prints the structure of the decision tree.
    Args:
        node: The current DecisionNode.
        indent: String for indentation.
        branch: Label for the branch ("Root", "Yes", "No").
    """
    if node is None:
        return
    if node.label is not None:
        print(f"{indent}[{branch}] -> [Leaf: {node.label}]")
    else:
        print(f"{indent}[{branch}] -> Q: {node.question}")
        print_tree(node.left, indent + "    ", "Yes")
        print_tree(node.right, indent + "    ", "No")


if __name__ == "__main__":
    # Example: Simple animal classifier decision tree

    # Leaf nodes (final decisions)
    dog = DecisionNode(label="Dog")
    cat = DecisionNode(label="Cat")
    bird = DecisionNode(label="Bird")
    fish = DecisionNode(label="Fish")

    # Internal nodes (questions)
    mammal_node = DecisionNode(
        question="Does it bark?", left=dog, right=cat  # Yes: Dog  # No: Cat
    )
    fly_node = DecisionNode(
        question="Can it fly?", left=bird, right=fish  # Yes: Bird  # No: Fish
    )
    root = DecisionNode(
        question="Is it a mammal?",
        left=mammal_node,  # Yes: ask if it barks
        right=fly_node,  # No: ask about flying
    )

    # CLI menu
    while True:
        print("\nDomestic Animal Classifier Decision Tree CLI")
        print("1. Visualize decision tree")
        print("2. Classify an animal (interactive)")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        if choice == "1":
            print("\nDecision Tree Structure:")
            print_tree(root)
        elif choice == "2":
            print("\nAnswer the questions to classify the animal:")
            traverse(root)
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
