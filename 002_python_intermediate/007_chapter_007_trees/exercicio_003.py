'''
AVL Tree Implementation
'''


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def insert(self, root, key):
        # 1. Standard BST insertion
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed

        # 2. Update height of ancestor node
        root.height = 1 + max(self._height(root.left),
                              self._height(root.right))

        # 3. Check balance factor and apply rotations if unbalanced
        balance = self._balance_factor(root)

        # Left-Left (LL)
        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        # Right-Right (RR)
        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        # Left-Right (LR)
        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Right-Left (RL)
        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def preorder(self, root):
        if not root:
            return []
        return [root.key] + self.preorder(root.left) + self.preorder(root.right)


# --- AVL Example Usage ---
avl = AVLTree()
root = None

# Inserting sorted numbers (would create a linked list in a standard BST)
for num in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, num)

# Balanced root becomes 30 instead of 10
print("AVL Pre-order:", avl.preorder(root))  # [30, 20, 10, 25, 40, 50]
