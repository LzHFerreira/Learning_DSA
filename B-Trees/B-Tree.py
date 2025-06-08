
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimal degree (minimum number of children for non-root, except possibly root)
        self.leaf = leaf  # True if node is a leaf node
        self.keys = []  # List of keys in the node
        self.children = []  # List of child pointers

    def __str__(self):
        return f"Keys: {self.keys}, Leaf: {self.leaf}"

    def find_key(self, k):
        # Find the first index in keys[] such that keys[idx] >= k
        idx = 0
        while idx < len(self.keys) and self.keys[idx] < k:
            idx += 1
        return idx

    def get_height(self):
        # Height is 1 for a leaf node, else 1 + height of any child (all paths are same length in B-Tree)
        if self.leaf:
            return 1
        return 1 + self.children[0].get_height()


class BTree:
    
    def __init__(self, t):
        self.root = BTreeNode(t, leaf=True)  # Start with an empty root node (leaf)
        self.t = t  # Minimal degree

    def get_height(self):
        # Returns the height of the B-Tree (number of nodes along the longest path from root to leaf)
        if self.root:
            return self.root.get_height()
        return 0

    def search(self, k, node=None):
        # Search for key k in the B-Tree, starting from node (or root if not specified)
        if node is None:
            node = self.root
        i = 0
        # Find the first key greater than or equal to k
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        # If found, return node and index
        if i < len(node.keys) and node.keys[i] == k:
            return (node, i)
        # If this is a leaf node, key is not present
        if node.leaf:
            return (None, None)
        # Otherwise, search in the appropriate child
        return self.search(k, node.children[i])

    def insert(self, k):
        # Insert key k into the B-Tree
        root = self.root
        # If root is full, tree grows in height
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.insert(0, root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        # Insert key k into a node that is guaranteed not full
        i = len(node.keys) - 1
        if node.leaf:
            # Insert the new key into the correct position in the node's keys
            node.keys.append(None)  # Add a dummy value to extend the list
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]  # Shift keys to the right
                i -= 1
            node.keys[i + 1] = k  # Insert the new key at the correct position
        else:
            # Find the child which is going to have the new key
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            # If the found child is full, split it
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                # After split, the middle key moves up and node.children[i] is split into two
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, parent, i):
        # Split the full child of parent at index i
        t = self.t
        y = parent.children[i]  # Node to be split
        z = BTreeNode(t, leaf=y.leaf)  # New node to store (t-1) keys of y
        z.keys = y.keys[t:]  # z gets the last t-1 keys from y
        y.keys = y.keys[: t - 1]  # y keeps the first t-1 keys
        if not y.leaf:
            z.children = y.children[t:]  # z gets the last t children
            y.children = y.children[:t]  # y keeps the first t children
        parent.children.insert(i + 1, z)  # Insert z as a child of parent
        parent.keys.insert(i, y.keys.pop())  # Move the middle key up to parent

    def traverse(self, node=None, depth=0):
        # Print all keys in the B-Tree in sorted order, with indentation for depth
        if node is None:
            node = self.root
        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i], depth + 1)
            print("  " * depth + str(node.keys[i]))
        if not node.leaf:
            self.traverse(node.children[len(node.keys)], depth + 1)

    def remove(self, k):
        # Remove key k from the B-Tree
        if not self.root:
            return
        self._remove(self.root, k)
        # If the root node has no keys after removal, make its first child the new root
        if len(self.root.keys) == 0:
            if not self.root.leaf:
                self.root = self.root.children[0]
            else:
                self.root = None

    def _remove(self, node, k):
        idx = node.find_key(k)

        if idx < len(node.keys) and node.keys[idx] == k:
            self._remove_from_node(node, k, idx)
        else:
            self._remove_from_subtree(node, k, idx)

    def _remove_from_node(self, node, k, idx):
        if node.leaf:
            node.keys.pop(idx)
        else:
            t = self.t
            if len(node.children[idx].keys) >= t:
                pred = self._get_predecessor(node, idx)
                node.keys[idx] = pred
                self._remove(node.children[idx], pred)
            elif len(node.children[idx + 1].keys) >= t:
                succ = self._get_successor(node, idx)
                node.keys[idx] = succ
                self._remove(node.children[idx + 1], succ)
            else:
                self._merge(node, idx)
                self._remove(node.children[idx], k)

    def _remove_from_subtree(self, node, k, idx):
        t = self.t
        if node.leaf:
            return
        flag = idx == len(node.keys)
        if len(node.children[idx].keys) < t:
            self._fill(node, idx)
        if flag and idx > len(node.keys):
            self._remove(node.children[idx - 1], k)
        else:
            self._remove(node.children[idx], k)

    def _get_predecessor(self, node, idx):
        # Find the predecessor key (rightmost key in left subtree)
        cur = node.children[idx]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def _get_successor(self, node, idx):
        # Find the successor key (leftmost key in right subtree)
        cur = node.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def _fill(self, node, idx):
        t = self.t
        # If previous sibling has >= t keys, borrow from it
        if idx != 0 and len(node.children[idx - 1].keys) >= t:
            self._borrow_from_prev(node, idx)
        # If next sibling has >= t keys, borrow from it
        elif idx != len(node.keys) and len(node.children[idx + 1].keys) >= t:
            self._borrow_from_next(node, idx)
        # Otherwise, merge with a sibling
        else:
            if idx != len(node.keys):
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    def _borrow_from_prev(self, node, idx):
        # Borrow a key from the previous sibling (left sibling)
        child = node.children[idx]
        sibling = node.children[idx - 1]
        # Move the separator key from parent down to child
        child.keys.insert(0, node.keys[idx - 1])
        # If child is not a leaf, move the last child pointer from sibling to child
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        # Move the last key from sibling up to parent
        node.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node, idx):
        # Borrow a key from the next sibling (right sibling)
        child = node.children[idx]
        sibling = node.children[idx + 1]
        # Move the separator key from parent down to child
        child.keys.append(node.keys[idx])
        # If child is not a leaf, move the first child pointer from sibling to child
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        # Move the first key from sibling up to parent
        node.keys[idx] = sibling.keys.pop(0)

    def _merge(self, node, idx):
        # Merge child at idx and child at idx+1, pulling down the separator key from parent
        child = node.children[idx]
        sibling = node.children[idx + 1]
        # Pull down the separator key from parent and add to child
        child.keys.append(node.keys.pop(idx))
        # Add all keys from sibling to child
        child.keys.extend(sibling.keys)
        # If not leaf, add all children from sibling to child
        if not child.leaf:
            child.children.extend(sibling.children)
        # Remove sibling from parent's children
        node.children.pop(idx + 1)


# Example usage:
if __name__ == "__main__":
    btree = BTree(t=2)  # Minimal degree t=2
    elements = [10, 20, 5, 6, 12, 30, 7, 17]
    for el in elements:
        btree.insert(el)

    print("B-Tree traversal (in sorted order):")
    btree.traverse()
    print(f"\nHeight of B-Tree: {btree.get_height()}")

    # Remove keys (test all cases)
    print("\nRemoving 6 (leaf):")
    btree.remove(6)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 13 (not present):")
    btree.remove(13)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 7 (leaf):")
    btree.remove(7)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 4 (not present):")
    btree.remove(4)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 12 (internal):")
    btree.remove(12)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 5 (internal):")
    btree.remove(5)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 10 (internal):")
    btree.remove(10)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 20 (internal):")
    btree.remove(20)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 30 (last key):")
    btree.remove(30)
    btree.traverse()
    print(f"Height: {btree.get_height()}")

    print("\nRemoving 17 (last key):")
    btree.remove(17)
    btree.traverse()
    print(f"Height: {btree.get_height()}")
