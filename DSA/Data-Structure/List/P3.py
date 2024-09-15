'''
Write a Python function to rotate a list to the right by k positions.
Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

'''
l = [1,2,3,4,5]
k = 2
rotate_elemets_len = len(l) - k
new = l[rotate_elemets_len:]+l[:rotate_elemets_len]
print(new)
