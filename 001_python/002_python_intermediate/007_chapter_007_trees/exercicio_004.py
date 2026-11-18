'''
Red-Black Tree Implementation
'''

RED = True
BLACK = False


class RBNode:
    def __init__(self, key, color=RED, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(key=None, color=BLACK)
        self.root = self.NIL

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        new_node = RBNode(key=key, color=RED, left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        # 1. Standard BST insert
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                return  # Duplicate key

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # 2. Fix Red-Black violations
        self._fix_insert(new_node)

    def _fix_insert(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                uncle = k.parent.parent.right
                # Case 1: Uncle is RED -> Recolor parent, uncle, and grandparent
                if uncle.color == RED:
                    k.parent.color = BLACK
                    uncle.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    # Case 2: Triangle (LR) -> Rotate left to convert to Line (LL)
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_left(k)
                    # Case 3: Line (LL) -> Recolor and rotate right
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._rotate_right(k.parent.parent)
            else:
                uncle = k.parent.parent.left
                # Mirror Case 1: Uncle is RED
                if uncle.color == RED:
                    k.parent.color = BLACK
                    uncle.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    # Mirror Case 2: Triangle (RL)
                    if k == k.parent.left:
                        k = k.parent
                        self._rotate_right(k)
                    # Mirror Case 3: Line (RR)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._rotate_left(k.parent.parent)

        self.root.color = BLACK

    def inorder(self, node="ROOT"):
        if node == "ROOT":
            node = self.root
        if node == self.NIL:
            return []
        color_tag = "R" if node.color == RED else "B"
        return (
            self.inorder(node.left)
            + [f"{node.key}({color_tag})"]
            + self.inorder(node.right)
        )


# --- Red-Black Example Usage ---
rbt = RedBlackTree()
for num in [10, 20, 30, 15, 25, 5]:
    rbt.insert(num)

print("Red-Black In-order:", rbt.inorder())
# ['5(R)', '10(B)', '15(R)', '20(B)', '25(R)', '30(B)']
