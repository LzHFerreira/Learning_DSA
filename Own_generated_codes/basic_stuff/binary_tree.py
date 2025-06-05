# Basic implementation of a binary tree in Python, with methods to insert nodes and perform a search.
# This code defines a simple binary tree structure with insertion and search functionalities.

from collections import deque  # Import deque for queue operations in BFS


class Node:
    def __init__(self, data):
        self.left = None  # Left child node
        self.right = None  # Right child node
        self.val = data  # Value of the node


class BinaryTree:
    def __init__(self):
        self.root = None  # Root node of the tree

    def insert(self, data):
        if self.root is None:  # If tree is empty
            self.root = Node(data)  # Set root to new node
        else:
            self._insert_rec(self.root, data)  # Otherwise, insert recursively

    def _insert_rec(self, node, data):
        if data < node.val:  # If data is less, go left
            if node.left is None:
                node.left = Node(data)  # Insert new node if left is empty
            else:
                self._insert_rec(node.left, data)  # Recurse left
        else:  # If data is greater or equal, go right
            if node.right is None:
                node.right = Node(data)  # Insert new node if right is empty
            else:
                self._insert_rec(node.right, data)  # Recurse right

    def search(self, data):
        return self._search_rec(self.root, data)  # Start recursive search from root

    def _search_rec(self, node, data):
        if node is None:  # If node is None, not found
            return False
        if node.val == data:  # If value matches, found
            return True
        elif data < node.val:  # If data is less, search left
            return self._search_rec(node.left, data)
        else:  # If data is greater, search right
            return self._search_rec(node.right, data)

    def pre_order_traversal(self):
        result = []  # List to store traversal
        self._pre_order_rec(self.root, result)  # Start recursion from root
        return result  # Return traversal list

    def _pre_order_rec(self, node, result):
        if node:
            result.append(node.val)  # Visit node
            self._pre_order_rec(node.left, result)  # Traverse left
            self._pre_order_rec(node.right, result)  # Traverse right

    def in_order_traversal(self):
        result = []  # List to store traversal
        self._in_order_rec(self.root, result)  # Start recursion from root
        return result  # Return traversal list

    def _in_order_rec(self, node, result):
        if node:
            self._in_order_rec(node.left, result)  # Traverse left
            result.append(node.val)  # Visit node
            self._in_order_rec(node.right, result)  # Traverse right

    def post_order_traversal(self):
        result = []  # List to store traversal
        self._post_order_rec(self.root, result)  # Start recursion from root
        return result  # Return traversal list

    def _post_order_rec(self, node, result):
        if node:
            self._post_order_rec(node.left, result)  # Traverse left
            self._post_order_rec(node.right, result)  # Traverse right
            result.append(node.val)  # Visit node

    def deepth_first_search(self, data):
        return self._deepth_first_search_rec(self.root, data)  # Start DFS from root

    def _deepth_first_search_rec(self, node, data):
        if node is None:  # If node is None, not found
            return False
        if node.val == data:  # If value matches, found
            return True
        if self._deepth_first_search_rec(node.left, data):  # Search left subtree
            return True
        if self._deepth_first_search_rec(node.right, data):  # Search right subtree
            return True

    def breadth_first_search(self, data):
        if self.root is None:  # If tree is empty
            return False

        queue = deque()  # Create a new deque for BFS
        queue.append(self.root)  # Start with root node

        while queue:  # While there are nodes to process
            node = queue.popleft()  # Get next node from queue
            print(node.val)  # Debugging: print current node value
            if node.val == data:  # If value matches, found
                return True

            if node.left:  # If left child exists, add to queue
                queue.append(node.left)

            if node.right:  # If right child exists, add to queue
                queue.append(node.right)

        return False  # If not found after traversal, return False

    

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()  # Create a new binary tree
    tree.insert(10)  # Insert root node
    tree.insert(5)  # Insert left child
    tree.insert(15)  # Insert right child
    tree.insert(3)  # Insert left-left child
    tree.insert(7)  # Insert left-right child

    print(tree.search(7))  # Output: True, 7 is in the tree
    print(tree.search(8))  # Output: False, 8 is not in the tree
    print(tree.search(10))  # Output: True, 10 is the root

    print(tree.pre_order_traversal())  # Output: [10, 5, 3, 7, 15], pre-order traversal

    print(tree.in_order_traversal())  # Output: [3, 5, 7, 10, 15], in-order traversal

    print(
        tree.post_order_traversal()
    )  # Output: [3, 7, 5, 15, 10], post-order traversal

    print(tree.deepth_first_search(7))  # Output: True, DFS finds 7
    print(tree.deepth_first_search(8))  # Output: False, DFS does not find 8

    print(tree.breadth_first_search(7))  # Output: True, BFS finds 7
    print(tree.breadth_first_search(8))  # Output: False, BFS does not find 8
