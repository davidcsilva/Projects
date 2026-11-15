'''
Binary Tree
'''

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data=None):
        self.root = Node(root_data) if root_data is not None else None

    def insert(self, data):
        """Inserts a node at the first available spot using level-order (BFS)."""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if not current.left:
                current.left = new_node
                return
            queue.append(current.left)

            if not current.right:
                current.right = new_node
                return
            queue.append(current.right)

    def search(self, target):
        """Searches for a value across the entire tree using BFS."""
        if not self.root:
            return False

        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.data == target:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    def delete(self, key):
        """Deletes a node by replacing it with the deepest rightmost node."""
        if not self.root:
            return False

        if not self.root.left and not self.root.right:
            if self.root.data == key:
                self.root = None
                return True
            return False

        queue = deque([self.root])
        target_node = None
        last_node = None

        while queue:
            last_node = queue.popleft()
            if last_node.data == key:
                target_node = last_node
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        if target_node:
            deepest_val = last_node.data
            self._delete_deepest(last_node)
            target_node.data = deepest_val
            return True
        return False

    def _delete_deepest(self, d_node):
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current is d_node:
                current = None
                return
            if current.right:
                if current.right is d_node:
                    current.right = None
                    return
                queue.append(current.right)
            if current.left:
                if current.left is d_node:
                    current.left = None
                    return
                queue.append(current.left)

    def height(self, node="ROOT"):
        """Returns the height of the tree (empty tree = -1, single node = 0)."""
        if node == "ROOT":
            node = self.root
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    # --- Traversals ---

    def inorder(self, node="ROOT", res=None):
        if node == "ROOT":
            node = self.root
        if res is None:
            res = []
        if node:
            self.inorder(node.left, res)
            res.append(node.data)
            self.inorder(node.right, res)
        return res

    def preorder(self, node="ROOT", res=None):
        if node == "ROOT":
            node = self.root
        if res is None:
            res = []
        if node:
            res.append(node.data)
            self.preorder(node.left, res)
            self.preorder(node.right, res)
        return res

    def postorder(self, node="ROOT", res=None):
        if node == "ROOT":
            node = self.root
        if res is None:
            res = []
        if node:
            self.postorder(node.left, res)
            self.postorder(node.right, res)
            res.append(node.data)
        return res

    def level_order(self):
        if not self.root:
            return []
        res, queue = [], deque([self.root])
        while queue:
            current = queue.popleft()
            res.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return res


# --- Example Usage ---
bt = BinaryTree("A")
for item in ["B", "C", "D", "E", "F", "G"]:
    bt.insert(item)

# Resulting tree structure:
#         A
#       /   \
#      B     C
#     / \   / \
#    D   E F   G

print("Level-order:", bt.level_order())  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print("In-order:   ", bt.inorder())      # ['D', 'B', 'E', 'A', 'F', 'C', 'G']
print("Pre-order:  ", bt.preorder())     # ['A', 'B', 'D', 'E', 'C', 'F', 'G']
print("Post-order: ", bt.postorder())    # ['D', 'E', 'B', 'F', 'G', 'C', 'A']
print("Height:     ", bt.height())       # 2

bt.delete("B")
# ['A', 'G', 'C', 'D', 'E', 'F']
print("After deleting 'B' (Level-order):", bt.level_order())
