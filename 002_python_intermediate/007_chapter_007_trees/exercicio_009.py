'''
B+ Trees

'''


class BPlusNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []  # For internal nodes: child BPlusNodes; for leaves: values/records
        # Linked-list pointer to the next leaf node (leaves only)
        self.next = None


class BPlusTree:
    def __init__(self, order=4):
        """
        order (M): Maximum number of children per internal node.
                   Max keys per node = order - 1.
        """
        self.root = BPlusNode(leaf=True)
        self.order = order

    def _find_leaf(self, key):
        """Navigates from root down to the target leaf node."""
        current = self.root
        while not current.leaf:
            i = 0
            while i < len(current.keys) and key >= current.keys[i]:
                i += 1
            current = current.children[i]
        return current

    def search(self, key):
        """Exact point lookup: returns the value associated with 'key', or None."""
        leaf = self._find_leaf(key)
        for i, k in enumerate(leaf.keys):
            if k == key:
                return leaf.children[i]
        return None

    def range_query(self, start_key, end_key):
        """Returns all (key, value) pairs where start_key <= key <= end_key."""
        results = []
        leaf = self._find_leaf(start_key)

        while leaf:
            for i, k in enumerate(leaf.keys):
                if k > end_key:
                    return results
                if k >= start_key:
                    results.append((k, leaf.children[i]))
            leaf = leaf.next

        return results

    def insert(self, key, value):
        root = self.root
        # If root is full, split it and increase tree height
        if len(root.keys) == self.order - 1:
            new_root = BPlusNode(leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _insert_non_full(self, node, key, value):
        if node.leaf:
            # Update existing key if present, otherwise insert in sorted order
            for i, k in enumerate(node.keys):
                if k == key:
                    node.children[i] = value
                    return
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            node.keys.insert(i, key)
            node.children.insert(i, value)
        else:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1

            # Proactively split full child before descending
            if len(node.children[i].keys) == self.order - 1:
                self._split_child(node, i)
                if key >= node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key, value)

    def _split_child(self, parent, child_index):
        full_child = parent.children[child_index]
        new_sibling = BPlusNode(leaf=full_child.leaf)
        mid = len(full_child.keys) // 2

        if full_child.leaf:
            # LEAF SPLIT: Copy the middle key UP, and keep it in the right leaf
            promoted_key = full_child.keys[mid]
            new_sibling.keys = full_child.keys[mid:]
            new_sibling.children = full_child.children[mid:]

            full_child.keys = full_child.keys[:mid]
            full_child.children = full_child.children[:mid]

            # Maintain the linked list across leaf nodes
            new_sibling.next = full_child.next
            full_child.next = new_sibling
        else:
            # INTERNAL SPLIT: Push the middle key UP (do not duplicate it)
            promoted_key = full_child.keys[mid]
            new_sibling.keys = full_child.keys[mid + 1:]
            new_sibling.children = full_child.children[mid + 1:]

            full_child.keys = full_child.keys[:mid]
            full_child.children = full_child.children[:mid + 1]

        parent.keys.insert(child_index, promoted_key)
        parent.children.insert(child_index + 1, new_sibling)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        kind = "Leaf" if node.leaf else "Index"
        print(f"Level {level} ({kind}): {node.keys}")
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)


# --- Example Usage ---
bpt = BPlusTree(order=4)  # Max 3 keys per node
records = [
    (10, "User_10"), (20, "User_20"), (5, "User_5"),
    (15, "User_15"), (25, "User_25"), (30, "User_30"),
    (35, "User_35"), (12, "User_12")
]

for key, val in records:
    bpt.insert(key, val)

bpt.print_tree()
print("\nPoint Lookup (key=20):", bpt.search(20))
print("Range Query (12 to 28):", bpt.range_query(12, 28))
