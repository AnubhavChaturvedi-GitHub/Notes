# Stack in Python

A **stack** is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last element added to the stack will be the first one to be removed. Stacks are commonly used for tasks like reversing elements, parsing expressions, and managing function calls.

---

## Stack Implementation

### Using a List

In Python, a stack can be easily implemented using a list where the `append()` method is used to push elements onto the stack and the `pop()` method is used to remove elements from the stack.

```python
# Create an empty stack
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # Output: [1, 2, 3]
```

### Pop Elements from the Stack

```python
# Pop elements from the stack
top_element = stack.pop()
print(top_element)  # Output: 3
print(stack)        # Output: [1, 2]
```

### Peek (View Top Element)

To view the top element without removing it, you can use indexing.

```python
# Peek at the top element
top_element = stack[-1]
print(top_element)  # Output: 2
```

### Check if Stack is Empty

```python
# Check if the stack is empty
is_empty = len(stack) == 0
print(is_empty)  # Output: False (or True if the stack is empty)
```

---

## Stack Operations

### 1. Push Operation

Add an element to the top of the stack.

```python
stack.append(4)
print(stack)  # Output: [1, 2, 4]
```

### 2. Pop Operation

Remove the top element from the stack.

```python
stack.pop()
print(stack)  # Output: [1, 2]
```

### 3. Peek Operation

View the top element of the stack without removing it.

```python
print(stack[-1])  # Output: 2
```

### 4. Check if Stack is Empty

Determine if the stack has no elements.

```python
print(len(stack) == 0)  # Output: False
```

---

## Stack Example

Here’s a simple example demonstrating stack operations:

```python
# Create a stack
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

# View stack
print("Stack:", stack)  # Output: [10, 20, 30]

# Peek at the top element
print("Top element:", stack[-1])  # Output: 30

# Pop an element
print("Popped element:", stack.pop())  # Output: 30

# View stack after pop
print("Stack after pop:", stack)  # Output: [10, 20]
```

---

## Stack Operations Using `collections.deque`

For a more efficient stack implementation, especially if you are performing many `pop` and `append` operations, you can use `collections.deque`.

```python
from collections import deque

# Create a stack using deque
stack = deque()

# Push elements
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # Output: deque([1, 2, 3])

# Pop an element
print(stack.pop())  # Output: 3

# Peek at the top element
print(stack[-1])  # Output: 2

# Check if stack is empty
print(len(stack) == 0)  # Output: False
```
