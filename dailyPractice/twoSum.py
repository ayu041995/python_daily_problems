# "14. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in 
# non-decreasing order, find two numbers such that they add up to a specific target 
# number. Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an 
# integer array [index1, index2] of length 2.
# Input: numbers = [2,7,11,15], target = 9 Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. 
# We return [1, 2].
# Input: numbers = [2,3,4], target = 6 Output: [1,3]
# Input: numbers = [-1,0], target = -1, Output: [1,2]
# "

# Brut force method

# def twoSum(numbers,target):
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             if numbers[i]+numbers[j] == target:
#                 return [i+1,j+1]



# def twoSum(numbers,target):
#     left = 0

#     while left < len(numbers): 
#         for right in range(left+1,len(numbers)):
#             if numbers[left] + numbers[right] == target:
#                 return [left+1,right+1]
        
#         left += 1
#Optimized way

# def twoSum(numbers,target):
#     left = 0
#     right = len(numbers) -1

#     while left < right: 
#         if numbers[left] + numbers[right] == target:
#             return[left+1, right+1]
#         elif numbers[left] + numbers[right] > target:
#             right -= 1
#         elif numbers[left] + numbers[right] < target:
#             left += 1
        


# print(twoSum([2,7,11,15],9))

# print(twoSum([2,3,4],6))

# print(twoSum([-1,0],-1))

# print(twoSum([1,4,5,7,9,10,31],16))

#non sorted array Optimized solution


def twoSum(numbers,target):
    dict1 = {}
    for i in range(len(numbers)):
        if numbers[i] in dict1.keys():
            return[dict1[numbers[i]]+1, i+1]
        dict1[target - numbers[i]] = i   


print(twoSum([15,7,10,5,2],9))

print(twoSum([2,3,4],6))

print(twoSum([-1,1,0],-1))

print(twoSum([31,-4,7,9,21],16))