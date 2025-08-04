def maxValue(list1):
    max_val = list1[0]
    for i in list1:
        if i > max_val:
            max_val = i
    
    return max_val


print(maxValue([4, 5, 1, 2, 7, 4]))