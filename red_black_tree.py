# red_black_tree.py

class Node:
    def __init__(self, key, color='red', parent=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, 'black')
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key, 'red', None)
        if self.root == self.NIL:
            self.root = new_node
            self.root.color = 'black'
            self.root.left = self.NIL
            self.root.right = self.NIL
        else:
            self._insert(self.root, new_node)
        self._fix_insert(new_node)

    def _insert(self, root, node):
        if node.key < root.key:
            if root.left == self.NIL:
                root.left = node
                node.parent = root
                node.left = self.NIL
                node.right = self.NIL
            else:
                self._insert(root.left, node)
        else:
            if root.right == self.NIL:
                root.right = node
                node.parent = root
                node.left = self.NIL
                node.right = self.NIL
            else:
                self._insert(root.right, node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_traversal(self, node, result=[]):
        if node != self.NIL:
            self.inorder_traversal(node.left, result)
            result.append((node.key, node.color))
            self.inorder_traversal(node.right, result)
        return result
