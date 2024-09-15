'''
Merge Two Sorted Lists

Write a function to merge two sorted lists into one sorted list.
Input: lst1 = [1, 3, 5], lst2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

'''
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]

l3 = lst1+lst2
l3.sort()
print(l3)
