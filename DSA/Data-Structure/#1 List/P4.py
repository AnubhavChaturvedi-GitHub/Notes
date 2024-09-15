'''
Problem 2: Find Duplicates in a List

Write a Python program to find all duplicate elements in a list.
Input: lst = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]

'''

lst = [4, 3, 2, 7, 8, 2, 3, 1]

z = set()

for i in lst:
    if lst.count(i) > 1:
        z.add(i)

print(list(z))
