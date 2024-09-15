# List in Python

A list in Python is a collection of elements that can hold heterogeneous types. Lists are mutable, meaning they can be changed after their creation. Here’s an overview of all the list methods and operations in Python, along with examples.

## List Creation
```python
# Create an empty list
empty_list = []

# Create a list with elements
fruits = ['apple', 'banana', 'mango']

print(fruits)  # Output: ['apple', 'banana', 'mango']
```

---

## List Indexing and Slicing
```python
# Access element by index
print(fruits[0])  # Output: 'apple'

# Negative indexing
print(fruits[-1])  # Output: 'mango'

# Slicing
print(fruits[1:3])  # Output: ['banana', 'mango']
```

---

## List Methods

### 1. `append()`
Adds an element at the end of the list.
```python
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'mango', 'orange']
```

### 2. `extend()`
Extends the list by appending all elements from another list.
```python
more_fruits = ['grapes', 'pineapple']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'mango', 'orange', 'grapes', 'pineapple']
```

### 3. `insert()`
Inserts an element at a specific position.
```python
fruits.insert(1, 'cherry')
print(fruits)  # Output: ['apple', 'cherry', 'banana', 'mango', 'orange', 'grapes', 'pineapple']
```

### 4. `remove()`
Removes the first occurrence of the element.
```python
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'mango', 'orange', 'grapes', 'pineapple']
```

### 5. `pop()`
Removes and returns the element at the specified position. If no index is provided, it removes the last item.
```python
last_fruit = fruits.pop()
print(last_fruit)  # Output: 'pineapple'
print(fruits)      # Output: ['apple', 'cherry', 'mango', 'orange', 'grapes']
```

### 6. `clear()`
Removes all elements from the list.
```python
fruits.clear()
print(fruits)  # Output: []
```

### 7. `index()`
Returns the index of the first occurrence of an element.
```python
fruits = ['apple', 'banana', 'mango']
print(fruits.index('banana'))  # Output: 1
```

### 8. `count()`
Returns the number of occurrences of an element.
```python
fruits.append('banana')
print(fruits.count('banana'))  # Output: 2
```

### 9. `sort()`
Sorts the list in ascending order (can be modified to sort in descending order).
```python
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'banana', 'mango']
```

To sort in reverse order:
```python
fruits.sort(reverse=True)
print(fruits)  # Output: ['mango', 'banana', 'banana', 'apple']
```

### 10. `reverse()`
Reverses the elements of the list.
```python
fruits.reverse()
print(fruits)  # Output: ['apple', 'banana', 'banana', 'mango']
```

### 11. `copy()`
Returns a shallow copy of the list.
```python
copy_fruits = fruits.copy()
print(copy_fruits)  # Output: ['apple', 'banana', 'banana', 'mango']
```

---

## List Operations

### 1. Concatenation
Combining two lists using the `+` operator.
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
```

### 2. Repetition
Repeating the elements of a list using the `*` operator.
```python
repeated_list = list1 * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]
```

### 3. Membership
Checking if an element exists in the list using the `in` keyword.
```python
print(1 in list1)  # Output: True
print(7 in list1)  # Output: False
```

---

## List Comprehensions
List comprehensions provide a concise way to create lists.
```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

## List Length
Returns the number of elements in the list.
```python
print(len(fruits))  # Output: 4
```

---

## List Deletion
You can delete elements or the entire list using `del`.
```python
del fruits[1]
print(fruits)  # Output: ['apple', 'banana', 'mango']

del fruits  # Deletes the entire list
```
