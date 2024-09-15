l = [1,2,4,5,7,8,9,6,3,7]

target = 10

# print all possible sum 

for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i] + l[j] == target:
            print(l[i],l[j])


'''
output :
1 9
2 8
4 6
5 5
7 3
3 7
'''
