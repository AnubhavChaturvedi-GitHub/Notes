Sure, here’s a similar guide for **Dictionaries** in Python:

# Dictionary in Python

A dictionary in Python is an unordered collection of data values used to store data in the form of key-value pairs. Each key in a dictionary must be unique and immutable, while the values can be of any type. Dictionaries are mutable, meaning they can be changed after creation.

## Dictionary Creation
```python
# Create an empty dictionary
empty_dict = {}

# Create a dictionary with key-value pairs
person = {'name': 'Anubhav', 'age': 21, 'city': 'Bangalore'}

print(person)  # Output: {'name': 'Anubhav', 'age': 21, 'city': 'Bangalore'}
```

---

## Accessing Dictionary Elements
You can access elements by using their keys.

```python
# Access value by key
print(person['name'])  # Output: 'Anubhav'

# Using the get() method (prevents KeyError if the key is missing)
print(person.get('age'))  # Output: 21
```

---

## Dictionary Methods

### 1. `get()`
Returns the value of the specified key. If the key does not exist, it returns `None` or a default value.
```python
print(person.get('profession', 'Not specified'))  # Output: 'Not specified'
```

### 2. `keys()`
Returns a view object containing all the keys in the dictionary.
```python
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])
```

### 3. `values()`
Returns a view object containing all the values in the dictionary.
```python
print(person.values())  # Output: dict_values(['Anubhav', 21, 'Bangalore'])
```

### 4. `items()`
Returns a view object containing key-value pairs.
```python
print(person.items())  # Output: dict_items([('name', 'Anubhav'), ('age', 21), ('city', 'Bangalore')])
```

### 5. `update()`
Updates the dictionary with elements from another dictionary or key-value pairs.
```python
person.update({'profession': 'Student'})
print(person)  # Output: {'name': 'Anubhav', 'age': 21, 'city': 'Bangalore', 'profession': 'Student'}
```

### 6. `pop()`
Removes the element with the specified key and returns its value.
```python
age = person.pop('age')
print(age)  # Output: 21
print(person)  # Output: {'name': 'Anubhav', 'city': 'Bangalore', 'profession': 'Student'}
```

### 7. `popitem()`
Removes and returns the last inserted key-value pair as a tuple.
```python
last_item = person.popitem()
print(last_item)  # Output: ('profession', 'Student')
print(person)     # Output: {'name': 'Anubhav', 'city': 'Bangalore'}
```

### 8. `clear()`
Removes all items from the dictionary.
```python
person.clear()
print(person)  # Output: {}
```

### 9. `copy()`
Returns a shallow copy of the dictionary.
```python
new_person = person.copy()
print(new_person)  # Output: {'name': 'Anubhav', 'age': 21, 'city': 'Bangalore'}
```

---

## Dictionary Operations

### 1. Adding or Updating Elements
You can add new key-value pairs or update existing keys by assigning a value to the key.
```python
person['country'] = 'India'  # Adding a new key-value pair
person['age'] = 22           # Updating an existing key's value
print(person)  # Output: {'name': 'Anubhav', 'age': 22, 'city': 'Bangalore', 'country': 'India'}
```

### 2. Deleting Elements
Use the `del` keyword to delete a key-value pair.
```python
del person['city']
print(person)  # Output: {'name': 'Anubhav', 'age': 22, 'country': 'India'}

del person  # Deletes the entire dictionary
```

---

## Dictionary Comprehensions
Similar to list comprehensions, you can use dictionary comprehensions to create dictionaries.
```python
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Dictionary Length
Returns the number of key-value pairs in the dictionary.
```python
print(len(person))  # Output: 3
```

---

This covers the most commonly used dictionary operations and methods in Python.
