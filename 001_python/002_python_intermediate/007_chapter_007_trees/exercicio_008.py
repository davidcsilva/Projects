'''
B-Trees

'''


class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []       # Sorted list of keys in this node
        self.children = []   # List of child BTreeNode references


class BTree:
    def __init__(self, t):
        """
        t: Minimum degree (t >= 2).
           Each node holds between (t - 1) and (2t - 1) keys.
        """
        self.root = BTreeNode(leaf=True)
        self.t = t

    def search(self, key, node=None):
        """Returns (node, index) if key is found, otherwise None."""
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # Check if the key is at index i in the current node
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)

        # If this is a leaf node, the key does not exist in the tree
        if node.leaf:
            return None

        # Otherwise, recurse into the appropriate child subtree
        return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        # If root is full (2t - 1 keys), split it and grow tree height upward by 1
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _split_child(self, parent, child_index):
        """Splits a full child (2t - 1 keys) into two nodes of (t - 1) keys."""
        t = self.t
        full_child = parent.children[child_index]
        new_sibling = BTreeNode(leaf=full_child.leaf)

        # Median key at index (t - 1) moves up to the parent
        median_key = full_child.keys[t - 1]
        parent.keys.insert(child_index, median_key)
        parent.children.insert(child_index + 1, new_sibling)

        # Right half of keys moves to the new sibling; left half stays
        new_sibling.keys = full_child.keys[t:]
        full_child.keys = full_child.keys[:t - 1]

        # If not a leaf, split the child pointers as well
        if not full_child.leaf:
            new_sibling.children = full_child.children[t:]
            full_child.children = full_child.children[:t]

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            # Insert key into the sorted position in the leaf
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # Find the child subtree where the key belongs
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # Proactively split the child if it is full before descending
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key)

    def traverse(self, node=None):
        """Returns all keys in sorted order."""
        if node is None:
            node = self.root

        result = []
        for i in range(len(node.keys)):
            if not node.leaf:
                result.extend(self.traverse(node.children[i]))
            result.append(node.keys[i])

        if not node.leaf:
            result.extend(self.traverse(node.children[-1]))

        return result

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(f"Level {level}: {node.keys}")
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)


# --- Example Usage (t = 3 -> max 5 keys per node) ---
btree = BTree(t=3)
for val in [10, 20, 5, 6, 12, 30, 7, 17, 3, 25, 40, 50]:
    btree.insert(val)

btree.print_tree()
print("\nSorted keys:", btree.traverse())
print("Search 17:  ", "Found" if btree.search(17) else "Not Found")
print("Search 99:  ", "Found" if btree.search(99) else "Not Found")
