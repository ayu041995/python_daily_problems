# "6. Subarray Sum Equals K - total number of subarrays

# Given an array of integers nums and an integer k, return the 
# total number of subarrays whose sum equals to k.

# Input: nums = [1,1,1], k = 2 Output: 2

# Input: nums = [1,2,3], k = 3 Output: 2"



def subarraySum(nums,k):
    count = 0
    for i in range(len(nums)):
        total = nums[i]
        # print("total--1",total)
        if nums[i] == k:
            count += 1
        for j in range(i+1,len(nums)):
            total += nums[j]
            # print("total--2",total)
            if total == k:
                count += 1
                # print("count",count)
    return count


        



print(subarraySum([1,2,3],3))