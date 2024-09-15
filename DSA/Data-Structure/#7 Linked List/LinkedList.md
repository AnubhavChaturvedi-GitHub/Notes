
# Linked List in Python

A **linked list** is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Linked lists allow efficient insertion and removal of elements from any position. They come in various forms, including singly linked lists, doubly linked lists, and circular linked lists.

---

## Singly Linked List

### Node Class

A node is the basic building block of a linked list, containing the data and a reference to the next node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### LinkedList Class

A linked list class manages the nodes and provides methods to operate on the linked list.

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
```

---

## Linked List Operations

### 1. Append Operation

Add an element to the end of the linked list.

```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: [1, 2, 3]
```

### 2. Prepend Operation

Add an element to the beginning of the linked list.

```python
ll.prepend(0)
ll.display()  # Output: [0, 1, 2, 3]
```

### 3. Delete Operation

Remove the first occurrence of a specified element from the linked list.

```python
ll.delete_with_value(2)
ll.display()  # Output: [0, 1, 3]
```

### 4. Display List

Print the elements of the linked list.

```python
ll.display()  # Output: [0, 1, 3]
```

---

## Doubly Linked List

A doubly linked list is similar to a singly linked list but each node has two references: one to the next node and one to the previous node.

### Node Class

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

### DoublyLinkedList Class

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_with_value(self, value):
        current = self.head
        while current and current.data != value:
            current = current.next
        if current is None:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        current = None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
```

---

## Circular Linked List

In a circular linked list, the last node points back to the first node, creating a circle.

### Node Class

```python
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### CircularLinkedList Class

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

    def display(self):
        elements = []
        if not self.head:
            print(elements)
            return
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        print(elements)
```

---

## Linked List Example

Here’s a simple example demonstrating linked list operations:

```python
# Create a singly linked list
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.display()  # Output: [5, 10, 20]

# Delete an element
ll.delete_with_value(10)
ll.display()  # Output: [5, 20]
```

