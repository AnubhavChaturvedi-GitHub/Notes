# Queue in Python

A **queue** is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed. Queues are commonly used in scenarios like task scheduling, handling requests, and implementing breadth-first search.

---

## Queue Implementation

### Using a List

In Python, a queue can be implemented using a list where the `append()` method is used to enqueue elements and the `pop(0)` method is used to dequeue elements. However, using lists for queue operations can be inefficient due to the time complexity of `pop(0)`.

```python
# Create an empty queue
queue = []

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: [1, 2, 3]

# Dequeue an element
first_element = queue.pop(0)
print(first_element)  # Output: 1
print(queue)          # Output: [2, 3]
```

### Using `collections.deque`

For a more efficient queue implementation, especially for frequent enqueue and dequeue operations, use `collections.deque`, which provides O(1) time complexity for append and pop operations.

```python
from collections import deque

# Create a queue using deque
queue = deque()

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # Output: deque([1, 2, 3])

# Dequeue an element
first_element = queue.popleft()
print(first_element)  # Output: 1
print(queue)          # Output: deque([2, 3])
```

---

## Queue Operations

### 1. Enqueue Operation

Add an element to the end of the queue.

```python
queue.append(4)
print(queue)  # Output: deque([2, 3, 4])
```

### 2. Dequeue Operation

Remove and return the element from the front of the queue.

```python
element = queue.popleft()
print(element)  # Output: 2
print(queue)    # Output: deque([3, 4])
```

### 3. Peek (View Front Element)

View the front element of the queue without removing it.

```python
front_element = queue[0]
print(front_element)  # Output: 3
```

### 4. Check if Queue is Empty

Determine if the queue has no elements.

```python
print(len(queue) == 0)  # Output: False
```

---

## Queue Example

Here’s a simple example demonstrating queue operations:

```python
from collections import deque

# Create a queue
queue = deque()

# Enqueue elements
queue.append('A')
queue.append('B')
queue.append('C')

# View queue
print("Queue:", queue)  # Output: deque(['A', 'B', 'C'])

# Peek at the front element
print("Front element:", queue[0])  # Output: 'A'

# Dequeue an element
print("Dequeued element:", queue.popleft())  # Output: 'A'

# View queue after dequeue
print("Queue after dequeue:", queue)  # Output: deque(['B', 'C'])
```

---

## Queue Operations Using `queue.Queue`

Python’s `queue` module provides a `Queue` class that supports multi-producer, multi-consumer queues. It’s thread-safe and suitable for use in threaded programming.

```python
from queue import Queue

# Create a queue using queue.Queue
queue = Queue()

# Enqueue elements
queue.put(1)
queue.put(2)
queue.put(3)

print(queue.queue)  # Output: deque([1, 2, 3])

# Dequeue an element
first_element = queue.get()
print(first_element)  # Output: 1
print(queue.queue)    # Output: deque([2, 3])

# Check if queue is empty
print(queue.empty())  # Output: False
```