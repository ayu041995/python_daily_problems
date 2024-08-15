# move_zero_to_last([0,1,0,2,3,4,5,6])

def move_zero_to_last(list1):
    # pass
    list2 = []
    count1 = 0
    for i in list1:
        # print(i)
        if i == 0:
            count1 = count1 + 1
            continue
        else:
            list2.append(i)
    for i in range(count1):
        list2.append(0)
    return list2


print(move_zero_to_last([0,1,0,2,3,4,5,6]))