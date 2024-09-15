nums1 = [1,3]
nums2 = [2]

final_arr = nums1 + nums2
final_arr.sort()
len_final_arr = len(final_arr)
        
if len_final_arr % 2 == 0:  # Even length
    i = len_final_arr // 2
    final_sum = final_arr[i - 1] + final_arr[i]
    print(final_sum / 2.0)  # Ensure float division
else:  # Odd length
    i = len_final_arr // 2
    print(final_arr[i])

'''
output:
2
'''
