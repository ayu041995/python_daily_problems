# "9. Max Sum Subarray of size K

# Given an array of integers Arr of size N and a number K. 
# Return the maximum sum of a subarray of size K.

# N = 4, K = 2 Arr = [100, 200, 300, 400] Output: 700
# Arr3 + Arr4 =700, which is maximum.

# N = 4, K = 4 Arr = [100, 200, 300, 400], Output: 1000

# Input : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 Output : 39
# Explanation: We get maximum sum by adding subarray 
# {4, 2, 10, 23} of size 4.
# Input : arr[] = {2, 3}, k = 3Output : Invalid
# Explanation: There is no subarray of size 3 as size of array 
# is 2. "

# def sumSub(list1,k):
#     totalSum = 0
#     for i in range(len(list1)):
#         # newlist = []
#         sumNum = 0
#         j = i
#         while j < i + k:
#             # newlist.append(list1[j])
#             sumNum = sumNum + list1[j]
#             # x = sum(newlist)
#             if sumNum > totalSum:
#                 totalSum = sumNum
#             elif j == len(list1)-1:
#                 break
#                 # print(totalSum)
#             j += 1
#     return totalSum
    
    
# print(sumSub([1100,100, 200, 300, 400,1000],3))
# print(sumSub([1100,100, 200, 300, 400,1000],4))
# print(sumSub([-100,200,-300,400,0,100],3))
# print(sumSub([1],1))
# print(sumSub([0],1))


# Sliding window technique

def sumSub(list1,k):
    total_sum = 0
    sumnum = 0
    for i in range(0,k):
        sumnum = sumnum + list1[i]
    total_sum = sumnum

    a = k
    b = 0
    while a < len(list1):
        sumnum = sumnum +list1[a] - list1[b]
        if sumnum > total_sum:
            total_sum = sumnum
        a += 1
        b += 1
    return total_sum
    
print(sumSub([1100,100, 1200, 300, 400,1000],3))
print(sumSub([1100,100, 200, 300, 400,1000],4))
print(sumSub([-100,200,-300,400,0,100],3))
print(sumSub([1],1))
print(sumSub([0],1))