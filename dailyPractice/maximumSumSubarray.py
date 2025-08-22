def max_sum_subarray(nums,k):
    left = 0
    right = left + k 
    window_sum = sum(nums[:k])
    # print(window_sum)
    max_sum = 0
    while right < len(nums):
        window_sum = window_sum - nums[left] + nums[right]
        max_sum = max(max_sum,window_sum)
        right += 1
        left += 1
    return max_sum

print(max_sum_subarray([2,1,5,1,3,2], 3))  # 9 (5+1+3)