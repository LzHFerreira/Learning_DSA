
    # BTree Data Structure
    
        BTree implements a B-Tree data structure, which is a balanced tree optimized for systems that read and write large blocks of data.
        B-Trees are commonly used in databases and filesystems.
    Attributes:
        root (BTreeNode): The root node of the B-Tree.
        t (int): The minimum degree (defines the range for number of keys).
    Methods:
        __init__(self, t):
            Initializes a B-Tree with a given minimum degree t.
            Starts with an empty root node (which is a leaf).
        get_height(self):
            Returns the height of the B-Tree, defined as the number of nodes along the longest path from the root to a leaf.
            Returns 0 if the tree is empty.
        search(self, k, node=None):
            Searches for a key 'k' in the B-Tree, starting from the specified node (or root if not provided).
            Returns a tuple (node, index) if the key is found, or (None, None) if not found.
        insert(self, k):
            Inserts a key 'k' into the B-Tree, maintaining the B-Tree properties.
            If the root node is full, the tree grows in height.
        traverse(self, node=None, depth=0):
            Traverses the B-Tree in sorted order, printing all keys.
            Indents output according to the depth of the node for visualization.
        remove(self, k):
            Removes a key 'k' from the B-Tree, maintaining the B-Tree properties.
            If the root node becomes empty after removal, updates the root.
        _insert_non_full(self, node, k):
            Helper method to insert a key 'k' into a node that is guaranteed not to be full.
        _split_child(self, parent, i):
            Helper method to split the full child of a parent node at index 'i'.
            Promotes the median key to the parent and splits the child into two nodes.
        _remove(self, node, k):
            Helper method to remove a key 'k' from the subtree rooted at 'node'.
        _remove_from_node(self, node, k, idx):
            Helper method to remove a key 'k' from a non-leaf node at index 'idx'.
        _remove_from_subtree(self, node, k, idx):
            Helper method to remove a key 'k' from a subtree when the key is not present in the current node.
        _get_predecessor(self, node, idx):
            Finds and returns the predecessor key of the key at index 'idx' in 'node'.
        _get_successor(self, node, idx):
            Finds and returns the successor key of the key at index 'idx' in 'node'.
        _fill(self, node, idx):
            Ensures that the child node at index 'idx' has at least 't' keys by borrowing from siblings or merging.
        _borrow_from_prev(self, node, idx):
            Borrows a key from the previous sibling of the child at index 'idx'.
        _borrow_from_next(self, node, idx):
            Borrows a key from the next sibling of the child at index 'idx'.
        _merge(self, node, idx):
            Merges the child at index 'idx' with its next sibling, pulling down the separator key from the parent.
    Usage:
        - Create a B-Tree by specifying the minimum degree t: `btree = BTree(t)`
        - Insert keys: `btree.insert(key)`
        - Search for keys: `btree.search(key)`
        - Remove keys: `btree.remove(key)`
        - Traverse and print the tree: `btree.traverse()`
    Note:
        - The BTree class relies on a BTreeNode class for node representation.
        - The minimum degree t must be >= 2 for a valid B-Tree.
        - All helper methods (prefixed with '_') are intended for internal use only.
