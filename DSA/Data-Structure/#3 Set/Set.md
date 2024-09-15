# Set in Python

A **set** in Python is an unordered collection of unique elements. Sets are mutable, but they do not allow duplicate elements. Sets are commonly used to perform mathematical set operations like union, intersection, and difference.

---

## Set Creation

```python
# Create an empty set
empty_set = set()

# Create a set with elements
numbers = {1, 2, 3, 4, 5}

print(numbers)  # Output: {1, 2, 3, 4, 5}
```

---

## Set Characteristics
- Sets do not allow duplicate elements.
- The order of elements in a set is not guaranteed to be consistent.
- Sets are mutable, meaning you can add or remove elements after creation.

---

## Set Methods

### 1. `add()`
Adds an element to the set.
```python
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}
```

### 2. `update()`
Adds multiple elements (from any iterable) to the set.
```python
numbers.update([7, 8])
print(numbers)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

### 3. `remove()`
Removes the specified element from the set. Raises a `KeyError` if the element does not exist.
```python
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5, 6, 7, 8}
```

### 4. `discard()`
Removes the specified element from the set. Does **not** raise an error if the element does not exist.
```python
numbers.discard(10)  # No error, even though 10 is not in the set
```

### 5. `pop()`
Removes and returns a random element from the set.
```python
random_element = numbers.pop()
print(random_element)  # Output: Random element (e.g., 1)
print(numbers)         # Output: Remaining elements
```

### 6. `clear()`
Removes all elements from the set.
```python
numbers.clear()
print(numbers)  # Output: set()
```

### 7. `copy()`
Returns a shallow copy of the set.
```python
copy_numbers = numbers.copy()
print(copy_numbers)  # Output: copy of the set
```

---

## Set Operations

### 1. Union (`|` or `union()`)
Returns a new set with elements from both sets.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
```
Or using `union()`:
```python
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

### 2. Intersection (`&` or `intersection()`)
Returns a new set with elements common to both sets.
```python
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
```
Or using `intersection()`:
```python
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
```

### 3. Difference (`-` or `difference()`)
Returns a new set with elements from the first set that are not in the second set.
```python
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
```
Or using `difference()`:
```python
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```

### 4. Symmetric Difference (`^` or `symmetric_difference()`)
Returns a new set with elements in either set but not in both.
```python
symmetric_diff_set = set1 ^ set2
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}
```
Or using `symmetric_difference()`:
```python
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}
```

---

## Set Comparisons

### 1. Subset (`<=`)
Checks if all elements of the first set are in the second set.
```python
set_a = {1, 2}
set_b = {1, 2, 3}

print(set_a <= set_b)  # Output: True
```

### 2. Superset (`>=`)
Checks if all elements of the second set are in the first set.
```python
print(set_b >= set_a)  # Output: True
```

### 3. Disjoint (`isdisjoint()`)
Checks if the sets have no elements in common.
```python
set_c = {4, 5}
print(set_a.isdisjoint(set_c))  # Output: True
```

---

## Set Length
Returns the number of elements in the set.
```python
print(len(numbers))  # Output: 5 (for example)
```

---

## Set Comprehensions
Just like list comprehensions, you can create sets using comprehensions.
```python
squares = {x**2 for x in range(6)}
print(squares)  # Output: {0, 1, 4, 9, 16, 25}
```

