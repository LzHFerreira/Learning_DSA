# AVL Tree Implementation in Python
# ---------------------------------
# An AVL tree is a self-balancing binary search tree (BST).
# For every node, the heights of the left and right subtrees differ by at most 1.
# If an insertion or deletion causes this property to be violated, the tree is rebalanced using rotations.
#
# Time Complexity:
#   - Search:      O(log n)
#   - Insertion:   O(log n)
#   - Deletion:    O(log n)
# Space Complexity: O(n)
#
# Reasoning:
#   - AVL trees maintain balance by tracking the height of each node and performing rotations when needed.
#   - This ensures that the tree remains balanced, guaranteeing logarithmic time for search, insert, and delete.
#   - Rotations (left, right, left-right, right-left) are used to restore balance.
#
# Example Usage Cases:
#   - Databases and file systems where fast lookups, inserts, and deletes are required
#   - Memory management and indexing
#   - Any application where balanced search trees are needed


class AVLNode:
    def __init__(self, key):
        self.key = key  # The value stored in the node
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of the node (leaf nodes have height 1)


def get_height(node):
    """
    Returns the height of the node, or 0 if the node is None.
    """
    if not node:
        return 0
    return node.height


def get_balance(node):
    """
    Returns the balance factor of the node.
    Balance = height(left subtree) - height(right subtree)
    """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotate(y):
    """
    Performs a right rotation on the subtree rooted at y.
    Returns the new root of the subtree.
    """
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def left_rotate(x):
    """
    Performs a left rotation on the subtree rooted at x.
    Returns the new root of the subtree.
    """
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def insert(node, key):
    """
    Inserts a key into the AVL tree rooted at node.
    Returns the new root of the subtree.
    """
    # 1. Perform normal BST insertion
    if not node:
        return AVLNode(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        # Duplicate keys are not allowed in BST
        return node

    # 2. Update the height of the ancestor node
    node.height = 1 + max(get_height(node.left), get_height(node.right))

    # 3. Get the balance factor to check whether this node became unbalanced
    balance = get_balance(node)

    # 4. If unbalanced, there are 4 cases

    # Left Left Case
    if balance > 1 and key < node.left.key:
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    # Return the (unchanged) node pointer
    return node


def pre_order(node):
    """
    Prints the keys of the tree in pre-order traversal.
    """
    if not node:
        return
    print(f"{node.key} (h={node.height})", end=" ")
    pre_order(node.left)
    pre_order(node.right)


# Example usage:
if __name__ == "__main__":
    root = None
    # Insert nodes into the AVL tree
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = insert(root, key)

    print("Pre-order traversal of the constructed AVL tree:")
    pre_order(root)
    print()
