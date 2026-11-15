'''
Binary Search Tree
'''

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # Duplicate values are ignored in standard BSTs

    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, current, target):
        if current is None:
            return False
        if current.value == target:
            return True
        if target < current.value:
            return self._search_recursive(current.left, target)
        return self._search_recursive(current.right, target)

    # --- Depth-First Traversals (DFS) ---

    def inorder(self):
        """Left -> Root -> Right (Returns sorted order in a BST)"""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def preorder(self):
        """Root -> Left -> Right (Useful for copying/serializing a tree)"""
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder(self):
        """Left -> Right -> Root (Useful for deleting nodes/freeing memory)"""
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)

    # --- Breadth-First Traversal (BFS / Level-Order) ---

    def level_order(self):
        """Visits nodes level by level from top to bottom"""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result


# --- Example Usage ---
bst = BinarySearchTree()
for num in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(num)

print("In-order (sorted):", bst.inorder())       # [20, 30, 40, 50, 60, 70, 80]
print("Pre-order:        ", bst.preorder())      # [50, 30, 20, 40, 70, 60, 80]
print("Post-order:       ", bst.postorder())     # [20, 40, 30, 60, 80, 70, 50]
print("Level-order (BFS):", bst.level_order())   # [50, 30, 70, 20, 40, 60, 80]

print("Search 40:", bst.search(40))  # True
print("Search 99:", bst.search(99))  # False
