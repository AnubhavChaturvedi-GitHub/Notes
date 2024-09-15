# List Declearation

#in python list can contains simelar data types as well as not simmaler data type

l1 = [1,2,3,4,5] 
l2 = ["hello",40]

# Calling the list and printing

print(l1)
print(l2)
print(l1,l2) # using single print we can print multiple varibles

'''
output : 
[1, 2, 3, 4, 5]
['hello', 40]
[1, 2, 3, 4, 5] ['hello', 40]
'''

# Let's find the type of these variables using type method

print(type(l1))
print(type(l2))
print(type(l1),type(l2)) # if you wanna use this print(type(l1,l2)) it will throw error because the type method only take one argument

'''
ouput :
<class 'list'>
<class 'list'>
<class 'list'> <class 'list'>
'''

# now let's print the specific element from the list using indexing
# indexing in list always starts with 0 - (n-1)

# over writing the list again 'we can over write the any variable again in python'

l1 = [20,50,30,70]

print(l1[0]) # print the first element from the list

# we can also do negative indexing in list that alwas start from -1 to n

print(l1[-1])

'''
output :
20
70
'''

# we can also perform the slicing in list 
# slicing is nothing but to print the element from specific index to another specific index

l1 = [20,30,4,5,6,7]
print(l1[0:2]) # the l1 is the list that we are over riding again and here is the example how we can use the indexing slicing in list the first index when ever we use that means we wanna start the element from that area and the second index always get awoided it is like loop the last index is not consider to print that we can also say like that the the slicig follow the rule start printing from the starting index and print till the (second index-1) we can also sa it like that the it same we perform this in loop in loop also the n is always awoided 

'''output:
[20, 30]
'''

# we can also perform negative indexing here

l1 = [58,47,78,75]
print(l1[-3:-1])
# here we need to write this like this if we use the index like print(l1[-1:-3]) it will return [] empty list 
# when we run this print(l1[-3:-1]) the -1 not be included like priveous 

'''
output :
[47, 78]
'''
# then the question is how we can print the last element using the slicing ?

# let's see

print(l1[-3:])

# in this situation we need to leave the space for that 

'''
output:
[47, 78, 75]
'''

# what about the leave space in left side 

# it will print the value till start

print(l1[:-1])

'''
output :
[58, 47, 78]
'''

# Now let's see can we modify the element of the list ?

l1 = [1,5,3,4,5] # and yes list allow you to store the dublicate elements

l1[1] = 2
print(l1)

# Yes we can do this can see here 
'''
output:
[1, 2, 3, 4, 5]
'''

# let's check can be updte the the element with slicing i mean muliple change in single time 

"""
must know

l1 = [08,09,11,48]

if you print this list it will throw the error 
because 0 is not allowed as prefix in list element 

then what about the if we try to print as string

like :- ['05','08',6]
"""
l1 = ['05','08',6]

print(l1)

# yes its allowed

'''
output :
['05', '08', 6]
'''

# let's change now

l1 = [1,5,4,9,4,5,6]

l1[0:2]=2,3

print(l1)
# yes we can change easily
'''
output :
[2, 3, 4, 9, 4, 5, 6]
'''

# let's try to add the new element in the list

a = [1,2,5,7,8,9]

# for that purpuse we need to call the pre defined method or you can also say function named append 

a.append(2)

# it will add the element in last 

print(a)

'''
output :
[1,2,5,7,8,9,2]
'''
# what about the multiple elements appending in single time

# lets see

p = [1,2,3,4,5,6]

# we can't perfrom using like this p.append(2,3) because the append only takes one argument but we are giving 2 

p.append([1,2]) # we can do like this but it will consider as one element only

print(p)

'''output:
[1, 2, 3, 4, 5, 6, [1, 2]]
'''

# by using extend method we can do that

p = [1,2,3,4,5,6]
p.extend([1,2])

print(p)

'''output:
[1,2,3,4,5,6,1,2]
'''

# lets see if i wanna remove the element from the list

l = [1,8,6,9,7,"hello"]

l.remove("hello") # using remove method we can do that

print(l)

'''
output:
[1, 8, 6, 9, 7]
'''

# convert the string in to list

a = 'hello'

a = list(a) # list is the keyword by using that we can change

print(a)

# if you wanna know the index of any element in the list

l = [1,8,5,7,90]

print(l.index(90))

'''
output:
4
'''

# we can also perfrom the pop operation in the list

l = [2,5,7,8,9]

l.pop()

print(l) # output : [2, 5, 7, 8]

l = [2,5,7,8,9]

l.pop(2) # argument inside the pop denote the index of the elemet

print(l) # output : [2, 5, 8, 9]

l = [2,6,7,8,9]

# find the length of the list

print(len(l)) #output : 5

# to conver into list 

print(list(('hello','hey','anubhav'))) # output : ['hello', 'hey', 'anubhav']

# check the element present in the list or not

l = [1,2,3,45,6,78]

if 78 in l:
    print("present")
else:
    print("not present")

#output : present

# insert the element in specific position using index

l = [1,25,8,7]

l.insert(1,45)

print(l) #output : [1, 45, 25, 8, 7]

# can we add 2 list

l1 = [1,2,4,5,7]
l2 = [1,4,7,5]

l3 = l1+l2

print(l3) # [1, 2, 4, 5, 7, 1, 4, 7, 5]

# sort the list

l1 = [1,3,2,4,5,6,8,5,7]

l1.sort()

print(l1) # output : [1, 2, 3, 4, 5, 5, 6, 7, 8]

# second way

print(sorted(l1)) # output : [1, 2, 3, 4, 5, 5, 6, 7, 8]

# we can delete the complete list using the del key word

# we can also perform the del for specific element using index

l = [1,2,3]

del l[0]

print(l) # [2, 3]

# we can clear the string as well 

l = [1,2,3]

l.clear()

print(l) # output : []

# there is a key word that allow to comy the same list as anther list 

l1 = [1,2,4,5,7,8,]
l2 = l1.copy()

print(l2) # output : [1, 2, 4, 5, 7, 8]

# we can also count the elements in list

l1 = [1,2,1,2,1,2,4,5,4,7,8]
print(l1.count(1)) # output : 3

# let's reverse the list 

l1 = [5,4,3,2,1]
print(l1[::-1]) # output : [1, 2, 3, 4, 5]

# The code reverses the list l1 using Python slicing ([::-1]), which steps through the list in reverse order

# second method

l1.reverse()
print(l1) # [1, 2, 3, 4, 5]

# print all the element from the list

l1 = ["first","second","hello","four"]
for i in l1:
    print(i)

'''
output:
first
second
hello
four
'''
