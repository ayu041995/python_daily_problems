def max_sum_subarray(arr,k):
    left = 0
    right = k
    max_sum = 0
    curr_sum = sum(arr[:k])
    # print(curr_sum)
    while right <= len(arr)-1:
        curr_sum = curr_sum - arr[left] + arr[right]
        # print(curr_sum)
        max_sum = max(max_sum,curr_sum)
        left += 1
        right += 1
    return max_sum
        
        

print(max_sum_subarray([2,1,5,1,3,2],3)) # 9 (5+1+3)