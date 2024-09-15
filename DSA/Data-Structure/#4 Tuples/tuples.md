
# Tuple in Python

A **tuple** in Python is an ordered collection of elements that can hold heterogeneous types. Unlike lists, tuples are immutable, meaning their elements cannot be changed once the tuple is created. Tuples are commonly used to group related data and are often used for fixed collections of items.

---

## Tuple Creation

```python
# Create an empty tuple
empty_tuple = ()

# Create a tuple with elements
numbers = (1, 2, 3, 4, 5)

print(numbers)  # Output: (1, 2, 3, 4, 5)

# Tuple with heterogeneous elements
mixed = (1, 'apple', 3.14, True)
```

---

## Accessing Tuple Elements

You can access elements by using their index.

```python
# Access element by index
print(numbers[0])  # Output: 1

# Negative indexing
print(numbers[-1])  # Output: 5

# Slicing
print(numbers[1:4])  # Output: (2, 3, 4)
```

---

## Tuple Methods

### 1. `count()`
Returns the number of occurrences of a specified element.
```python
fruits = ('apple', 'banana', 'apple')
print(fruits.count('apple'))  # Output: 2
```

### 2. `index()`
Returns the index of the first occurrence of a specified element. Raises a `ValueError` if the element is not found.
```python
print(fruits.index('banana'))  # Output: 1
```

---

## Tuple Operations

### 1. Concatenation (`+`)
Combining two tuples using the `+` operator.
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)
```

### 2. Repetition (`*`)
Repeating the elements of a tuple using the `*` operator.
```python
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)
```

### 3. Membership (`in`)
Checking if an element exists in the tuple using the `in` keyword.
```python
print(2 in tuple1)  # Output: True
print(7 in tuple1)  # Output: False
```

### 4. Length (`len()`)
Returns the number of elements in the tuple.
```python
print(len(tuple1))  # Output: 3
```

---

## Tuple Packing and Unpacking

### 1. Packing
Creating a tuple by grouping multiple values together.
```python
person = ('John', 25, 'Engineer')
```

### 2. Unpacking
Extracting elements of a tuple into individual variables.
```python
name, age, profession = person
print(name)       # Output: John
print(age)        # Output: 25
print(profession) # Output: Engineer
```

---

## Immutable Nature

- Tuples are immutable, meaning you cannot change their elements after creation.
- If you need to modify a tuple, you must create a new tuple.

```python
# Example of tuple immutability
try:
    person[1] = 30  # This will raise a TypeError
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
```

---

## Tuple Comprehensions

Tuples do not have a direct comprehension syntax, but you can create them using generator expressions within `tuple()`.

```python
squares = tuple(x**2 for x in range(5))
print(squares)  # Output: (0, 1, 4, 9, 16)
```
