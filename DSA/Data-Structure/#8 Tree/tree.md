# Trees in Python

Trees are hierarchical data structures with a root node and child nodes forming a tree-like structure. They are useful for representing hierarchical relationships, organizing data, and more. This document covers several types of trees: Binary Trees, Binary Search Trees, AVL Trees, Red-Black Trees, Tries, and B-Trees.

---

## 1. Binary Tree

A **binary tree** is a tree where each node has at most two children: left and right.

### Node Class

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

### BinaryTree Class

```python
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)

    def inorder_traversal(self):
        elements = []
        self._inorder(self.root, elements)
        print(elements)

    def _inorder(self, node, elements):
        if node:
            self._inorder(node.left, elements)
            elements.append(node.data)
            self._inorder(node.right, elements)

    def preorder_traversal(self):
        elements = []
        self._preorder(self.root, elements)
        print(elements)

    def _preorder(self, node, elements):
        if node:
            elements.append(node.data)
            self._preorder(node.left, elements)
            self._preorder(node.right, elements)

    def postorder_traversal(self):
        elements = []
        self._postorder(self.root, elements)
        print(elements)

    def _postorder(self, node, elements):
        if node:
            self._postorder(node.left, elements)
            self._postorder(node.right, elements)
            elements.append(node.data)
```

---

## 2. Binary Search Tree (BST)

A **binary search tree** is a binary tree where each node follows the property that left children are less than the node and right children are greater.

### BinarySearchTree Class

```python
class BinarySearchTree(BinaryTree):
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
```

---

## 3. AVL Tree

An **AVL Tree** is a self-balancing binary search tree where the difference in heights of left and right subtrees is at most one. It ensures O(log n) time complexity for insertions, deletions, and lookups.

### AVLNode Class

```python
class AVLNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.height = 1
```

### AVLTree Class

```python
class AVLTree(BinarySearchTree):
    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _insert(self, node, data):
        node = super()._insert(node, data)
        self._update_height(node)
        return self._balance(node)
```

---

## 4. Red-Black Tree

A **Red-Black Tree** is a balanced binary search tree with additional properties to ensure the tree remains balanced during insertions and deletions. The properties include color-coding nodes and enforcing constraints on the colors and the structure of the tree.

### RedBlackNode Class

```python
class RedBlackNode(TreeNode):
    def __init__(self, data, color='RED'):
        super().__init__(data)
        self.color = color
```

### RedBlackTree Class

Due to the complexity of Red-Black Trees, a complete implementation involves handling various cases for insertions and deletions to maintain balance. For brevity, refer to a comprehensive implementation or library for practical use.

---

## 5. Trie (Prefix Tree)

A **Trie** (or prefix tree) is a specialized tree used for storing strings in a way that allows fast retrieval, especially useful for tasks like autocomplete.

### TrieNode Class

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
```

### Trie Class

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

---

## 6. B-Tree

A **B-Tree** is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. It’s commonly used in databases and file systems.

### BTreeNode Class

```python
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf
        self.keys = []
        self.children = []
```

### BTree Class

A complete B-Tree implementation is extensive due to its balancing and node management. For practical use, refer to an established implementation or library.

