def minValue(list1):
    min_val = list1[0]
    for i in list1:
        if i < min_val:
            min_val = i
    
    return min_val


print(minValue([4, 5, 1, 2, 7, 4]))