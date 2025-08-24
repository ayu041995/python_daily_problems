# Find the lenght of longest subarray whose elements sum to a value less than or equals to k. A subarray is defined as a contiguous block of elements from original array.
# Example :
# a = [1,2,3]
# k = 3
# All possible subarrays : [1],[2],[3],[1,2],[2,3],[1,2,3]
# Subarrays with sum <= k:
# [1] : sum = 1 <= 3 : size 1
# [2] : sum = 2 <= 3 : size 1
# [3] : sum = 3 <= 3 : size 1
# [1,2] : sum = 3 <= 3 : size 2
# [2,3] : sum = 5 : Not valid
# [1,2,3] : sum = 6 : Not valid

# The longest valid subarray is [1,2] with lenght 2

# def maxLength(a,k):
#     left = 0
#     current_sum = 0
#     max_len = 0
#     for right in range(len(a)):
#         current_sum += a[right]
#         print("Outside*****",current_sum)
#         while current_sum > k and left <= right:
#             current_sum -= a[left]
#             print("Inside*****",current_sum)
#             left += 1
#         lenght = right-left+1
#         print("Lenght********",lenght)
#         max_len = max (max_len, lenght)
#     return max_len

    
     

# print(maxLength([1,2,3],3))

def maxLengthEqual(a,k):
    left = 0
    current_sum = 0
    max_len = 0
    for right in range(len(a)):
        current_sum += a[right]
        if current_sum == k:
            max_len = max(max_len, right-left+1)
        while current_sum > k and left <= right:
            current_sum -= a[left]
            if current_sum == k:
                max_len = max(max_len, (right-left+1))
            left += 1
    return max_len


    

print(maxLengthEqual([1,1,0,2,3,1,0,2,1,1,0],5))
print(maxLengthEqual([0,2,0,-2,3,1,1,1,],5))


    



